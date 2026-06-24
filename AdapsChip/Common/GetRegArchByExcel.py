"""
RegConfigParseOrGenByExcel - 基于 Excel 配置文件管理寄存器字段定义与批量更新/解析工具
================================================================================

【功能清单】

1. 加载 Excel 格式的寄存器定义文件，建立以下数据结构：
   - logic_fields: {逻辑字段名: [segment_dict, ...]}
       记录每个逻辑字段（如 WC、VC0_FLNR）由哪些物理地址位段组成
   - addr_defaults: {addr: 8bit_default_value}
       每个地址的默认值（由 Excel 中各字段的 default_value 合并而来）
   - addr_to_regname: {addr: reg_name}
       地址到寄存器名的映射
   - addr_descriptions: {addr: 拼接好的位域描述字符串}
       用于日志/打印，例如 "WC: [11:8]：WC[11:8]； [7:0]：WC[7:0]"

2. logical_to_physical(current_config, updates) -> new_config
   功能：根据 updates 字典中的逻辑字段值，自动拆分到对应的物理地址位段
   示例：updates = {"WC": 0x5AA} 自动将 0x5AA 拆分为 WC[7:0]=0xAA、WC[11:8]=0x05
   特点：
   - 只更新 modify=True 的字段
   - 多 bit 跨地址字段（如 WC[11:8] 在一个地址、[7:0] 在另一个地址）全自动处理
   - 只修改 updated 中出现的字段，其他地址保留原值或默认值

3. physical_to_logical(input_config) -> results
   功能：将物理地址的键值对合并为逻辑字段值（logical_to_physical 的逆操作）
   示例：input_config = {0x05: 0xAA, 0x06: 0x05} -> results["WC"] = 0x5AA
   特点：
   - 只返回 analysis=True 的字段
   - 缺失地址使用 addr_defaults 补全后再合并

4. get_excel_parser_or_gen(path) -> RegConfigParseOrGenByExcel（带缓存的单例工厂）
   功能：延迟加载 Excel，避免重复解析；路径相同时返回同一实例

【Excel 格式要求】

Excel 列顺序：address, reg_name, bits, field, type, default_value, modify, analysis

bits 列格式示例：
  - [7:0]        表示 8 bit 宽，起始位 7，结束位 0
  - [3]          表示 1 bit 宽，起始位 3，结束位 3

field 列格式示例：
  - 普通单段字段：Rev, PXL_BINN_SEL
  - 多段逻辑字段：WC[11:8], WC[7:0]（表示同一个逻辑字段 WC 的高 4 位和低 8 位）
  - 带位权字段：VC0_FLNR[12:8]（逻辑位权 12:8，物理位权由 bits 列决定）

modify 列：
  - "Yes" 表示该字段可被 logical_to_physical 更新
  - 其他值表示不可修改

analysis 列：
  - "Yes" 表示该字段会被 physical_to_logical 返回
  - 其他值表示不参与解析

【使用示例】

# ---------- 示例 1：从零构建配置 ----------
from RegConfigParseOrGenByExcel import get_excel_parser_or_gen

mgr = get_excel_parser_or_gen("./reg.xlsx")

# 初始配置（空字典使用 addr_defaults 补全）
new_cfg = mgr.logical_to_physical({}, {"WC": 0x5AA})
# 结果：new_cfg = {0x05: 0xAA, 0x06: 0x05}（假设 WC[7:0] 在 0x05，WC[11:8] 在 0x06）

# ---------- 示例 2：增量更新 ----------
current = {0x05: 0xFF, 0x06: 0x0F}
updated = mgr.logical_to_physical(current, {"WC": 0x5AA})
# 结果：updated = {0x05: 0xAA, 0x06: 0x05}（只改 WC 相关地址，其他字段保留）

# ---------- 示例 3：从物理地址解析逻辑值 ----------
input_cfg = {0x05: 0xAA, 0x06: 0x05}
parsed = mgr.physical_to_logical(input_cfg)
# parsed["WC"] = 0x5AA（即使只有部分位段，也会用默认值补全后合并）

# ---------- 示例 4：打印寄存器描述 ----------
mgr.addr_descriptions[0x05]
# -> "WC: [11:8]：WC[11:8]； [7:0]：WC[7:0]"

【注意事项】

- logic_fields 中每个逻辑字段的 segment 按 Excel 出现顺序排列（高位在前、低位在后）
- logical_to_physical 只更新 modify=True 的字段，不修改其他字段
- physical_to_logical 只返回 analysis=True 的字段
- 路径使用 os.path.abspath 标准化，支持缓存去重
"""

# import openpyxl
import re
import os
from functools import cache


class GetRegArchByExcel:
    def __init__(self, excel_path):
        # logic_fields: {逻辑字段名: [segment_dict, ...]}
        # 每个 segment_dict 包含 addr, p_msb, p_lsb, l_msb, l_lsb, modify, analysis
        self.logic_fields = {}
        # addr_defaults: {addr: 8bit_default_value}，从 Excel 各字段 default_value 合并
        self.addr_defaults = {}
        # addr_to_regname: {addr: reg_name}
        self.addr_to_regname = {}
        # addr_descriptions: 预拼接的位域描述字符串，供日志/打印使用
        self.addr_descriptions = {}
        self._load_template(excel_path)

    def _parse_raw_value(self, val_str):
        """解析 Excel default_value 格式，如 8'h88, 1'b0, 4'd10 -> 返回整数值"""
        if val_str is None:
            return 0
        s = str(val_str).strip().lower()
        if not s:
            return 0
        
        # 严格格式校验 1: Verilog 位宽格式，如 8'h88
        # match = re.match(r"^\d+'([hbd])([0-9a-f]+)$", s)
        match = re.search(r"'([hbd])([0-9a-f]+)", s)
        if match:
            base_map = {'h': 16, 'b': 2, 'd': 10}
            try:
                return int(match.group(2), base_map[match.group(1)])
            except ValueError:
                raise ValueError(f"无法识别的默认值格式 '{val_str}'，进制字符不合法.")
        else:
            # 格式不匹配上述任何一种严格规则
            raise ValueError(f"不支持的值格式 '{val_str}'。必须是 Verilog 格式(如 8'h88, 1'b0, 4'd10)")

    def _load_template(self, path):
        """
        解析 Excel，建立四个核心数据结构：
        1. addr_to_regname: 地址 -> 寄存器名
        2. addr_defaults: 地址 -> 默认值（各字段默认值按物理位偏移合并）
        3. logic_fields: 逻辑字段名 -> [segment, ...]
        4. addr_descriptions: 地址 -> 拼接好的位域描述字符串
        """
        import openpyxl
        wb = openpyxl.load_workbook(path, data_only=True)
        sheet = wb.active
        curr_addr, curr_reg_name = None, None
        # addr_temp_parts: {addr: [描述片段, ...]}，用于最终拼接 addr_descriptions
        addr_temp_parts = {}

        for row_idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
            addr_raw, reg_name_raw, bits_raw, field_raw, _, def_raw, modify, analysis = row[:8]

            # 1. 物理地址向下填充（addr 为空时沿用上一个地址）
            if addr_raw is not None and reg_name_raw is not None:
                try:
                    curr_addr = int(str(addr_raw).strip(), 16)
                except ValueError:
                    raise ValueError(f"Excel 第 {row_idx} 行: 'address' 列格式错误，无法解析为十六进制整数 (当前值: '{addr_raw}')。")
                curr_reg_name = str(reg_name_raw).strip()
                self.addr_to_regname[curr_addr] = curr_reg_name
                    
            if field_raw is None:
                continue

            # 2. 拼接描述片段，例如 "[7:5]: NB"
            desc_part = f"{bits_raw}: {field_raw}"
            if curr_addr not in addr_temp_parts:
                addr_temp_parts[curr_addr] = []
            addr_temp_parts[curr_addr].append(desc_part)

            # 3. 解析物理位域 bits_raw，如 "[7:0]" -> p_msb=7, p_lsb=0
            p_match = re.findall(r'\d+', str(bits_raw))
            if not p_match:
                raise ValueError(f"Excel 第 {row_idx} 行: 'bits' 列格式错误，必须包含数字 (例如 [7:0] 或 [3]，当前值: '{bits_raw}')。")
            p_msb = int(p_match[0])
            p_lsb = int(p_match[-1])

            # 4. 解析默认值并合并到 addr_defaults
            #    逻辑：field_default 左移 p_lsb 位后与其他字段在同一个 addr 中按位或合并
            try:
                field_default = self._parse_raw_value(def_raw)
            except ValueError as e:
                raise ValueError(f"Excel 第 {row_idx} 行: 'default_value' 列解析失败: {e}")
                
            if curr_addr not in self.addr_defaults:
                self.addr_defaults[curr_addr] = 0
            p_mask = ((1 << (p_msb - p_lsb + 1)) - 1) << p_lsb
            self.addr_defaults[curr_addr] = (self.addr_defaults[curr_addr] & ~p_mask) | (field_default << p_lsb)

            # 5. 解析逻辑域名与逻辑位权
            #    示例：WC[11:8] -> logic_name="WC", l_msb=11, l_lsb=8
            #          WC[7:0]  -> logic_name="WC", l_msb=7, l_lsb=0
            #    如果 field 不是多段格式（如 Rev、PXL_BINN_SEL），则 l_msb/l_lsb 等于物理位域
            l_match = re.match(r"(\w+)\[(\d+):?(\d+)?]", str(field_raw).strip())
            if l_match:
                logic_name = l_match.group(1)
                l_msb = int(l_match.group(2))
                l_lsb = int(l_match.group(3)) if l_match.group(3) else l_msb
            else:
                logic_name = str(field_raw).strip()
                if not logic_name:
                    raise ValueError(f"Excel 第 {row_idx} 行: 'field' 列不能为空。")
                l_msb, l_lsb = p_msb, p_lsb

            # 6. 建立 segment 并加入 logic_fields[logic_name]
            segment = {
                "addr": curr_addr,
                "p_msb": p_msb, "p_lsb": p_lsb,   # 物理位域
                "l_msb": l_msb, "l_lsb": l_lsb,     # 逻辑位权
                "modify": str(modify).strip().lower() == "yes",
                "analysis": str(analysis).strip().lower() == "yes"
            }
            self.logic_fields.setdefault(logic_name, []).append(segment)

        # 7. 循环结束后拼接 addr_descriptions
        #    示例结果: "WC: [11:8]：WC[11:8]； [7:0]：WC[7:0]"
        for addr, parts in addr_temp_parts.items():
            reg_name = self.addr_to_regname.get(addr, f"UNK_{hex(addr)}")
            self.addr_descriptions[addr] = f"{reg_name}: {'; '.join(parts)}"

    def logical_to_physical(self, ini_config, updates):
        """
        根据 updates 中的逻辑字段值，自动拆分并写入对应的物理地址位段。

        参数:
            ini_config: {addr: 8bit_value}，当前物理配置；空字典时使用 addr_defaults
            updates: {逻辑字段名: 逻辑值}，例如 {"WC": 0x5AA, "VC0_FLNR": 0x1234}

        返回:
            new_config: 新的 {addr: 8bit_value} 字典

        处理逻辑:
            对于 updates 中的每个 (name, val):
                1. 找到 logic_fields[name] 中的所有 segment
                2. 对每个 modify=True 的 segment：
                   - 从 val 中提取逻辑位段 fragment = (val >> l_lsb) & ((1 << width) - 1)
                   - 写入对应 addr 的物理位段
                3. 多段字段（如 WC[11:8]、WC[7:0]）会分别写入不同地址
        """
        new_config = ini_config.copy()
        for name, val in updates.items():
            if name not in self.logic_fields:
                continue

            for seg in self.logic_fields[name]:
                if not seg["modify"]:
                    continue

                addr = seg["addr"]
                # 提取逻辑值的对应片段
                l_width = seg["l_msb"] - seg["l_lsb"] + 1
                fragment = (val >> seg["l_lsb"]) & ((1 << l_width) - 1)

                # 获取当前值（优先用输入配置，没有则用 addr_defaults）
                reg_val = new_config.get(addr, self.addr_defaults.get(addr, 0))

                # 覆盖物理位段：先清零当前段，再写入 fragment
                p_mask = ((1 << (seg["p_msb"] - seg["p_lsb"] + 1)) - 1) << seg["p_lsb"]
                new_config[addr] = (reg_val & ~p_mask) | (fragment << seg["p_lsb"])
        return new_config

    def physical_to_logical(self, input_config):
        """
        将物理地址的键值对合并为逻辑字段值（logical_to_physical 的逆操作）。

        参数:
            input_config: {addr: 8bit_value}，物理地址配置

        返回:
            results: {逻辑字段名: 逻辑值}，只包含 analysis=True 的字段

        处理逻辑:
            对于每个 analysis=True 的逻辑字段：
                1. 收集其所有 segment
                2. 从 input_config 中取各 segment 对应地址的值（缺失则用 addr_defaults 补全）
                3. 提取物理位段 fragment = (reg_val >> p_lsb) & ((1 << p_width) - 1)
                4. 按逻辑位权合并到 combined_val：combined_val |= (fragment << l_lsb)
        """
        results = {}
        for name, segments in self.logic_fields.items():
            if not any(s["analysis"] for s in segments):
                continue

            combined_val = 0
            for seg in segments:
                addr = seg["addr"]
                # 核心效率：如果 input_config 没给该地址，直接从 addr_defaults 拿
                reg_val = input_config.get(addr, self.addr_defaults.get(addr, 0))

                p_width = seg["p_msb"] - seg["p_lsb"] + 1
                fragment = (reg_val >> seg["p_lsb"]) & ((1 << p_width) - 1)
                combined_val |= (fragment << seg["l_lsb"])

            results[name] = combined_val
        return results


# --- 全局延迟加载工厂（单例模式） ---
@cache
def get_reg_arch(path):
    """
    获取 RegConfigParseOrGenByExcel 实例，带缓存：相同路径返回同一实例。
    内部调用 os.path.abspath 标准化路径，防止重复加载。
    """
    return GetRegArchByExcel(os.path.abspath(path))


if __name__ == '__main__':
    # 演示：假设 Excel 中定义了 WC 字段跨两个地址
    # 0x05: WC[7:0]，0x06: WC[11:8]
    mgr = get_reg_arch("./reg.xlsx")

    # 从零更新：空字典会使用 addr_defaults 补全
    new_cfg = mgr.logical_to_physical({}, {"WC": 0x5AA})
    print(f"Updated Config: {new_cfg}")
    # 输出应包含 {5: 170, 6: 5} (170即0xAA)

    # 解析配置：即使只给一个地址，另一个地址也会用默认值补全后再合并
    parsed = mgr.physical_to_logical({0x05: 0xAA, 0x06: 0x01})
    print(f"Parsed Result WC: {parsed['WC']}")

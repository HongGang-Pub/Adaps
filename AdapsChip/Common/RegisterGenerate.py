import openpyxl
import re
import os
from functools import cache


class RegisterGenerate:
    def __init__(self, excel_path):
        self.logic_fields = {}  # 结构: { logic_name: [segment_dict, ...] }
        self.addr_defaults = {}  # 结构: { addr: 8bit_default_value }
        self.addr_to_regname = {}  # 结构: { addr: reg_name }
        self.addr_descriptions = {}  # 存储直接拼接好的 Excel 原始描述
        self._load_template(excel_path)

    def _parse_raw_value(self, val_str):
        """解析 Excel 中的默认值格式，如 8'h88, 1'b0, 4'd10"""
        if val_str is None:
            return 0
        s = str(val_str).lower()
        # 提取 'h, 'b, 'd 后的数值
        match = re.search(r"'([hbd])([0-9a-f]+)", s)
        if not match:
            return 0

        base_map = {'h': 16, 'b': 2, 'd': 10}
        return int(match.group(2), base_map[match.group(1)])

    def _load_template(self, path):
        wb = openpyxl.load_workbook(path, data_only=True)
        sheet = wb.active
        curr_addr, curr_reg_name = None, None
        # 用于缓存每个地址下拼接好的位域片段
        addr_temp_parts = {}

        for row in sheet.iter_rows(min_row=2, values_only=True):
            addr_raw, reg_name_raw, bits_raw, field_raw, _, def_raw, modify, analysis = row[:8]

            # 1. 物理地址向下填充
            if addr_raw is not None:
                curr_addr = int(str(addr_raw), 16) if isinstance(addr_raw, str) else addr_raw
            if reg_name_raw is not None:
                curr_reg_name = str(reg_name_raw).strip()
                self.addr_to_regname[curr_addr] = curr_reg_name
            if field_raw is None:
                continue

            # 2. 拼接 Excel 原始信息
            # 结果示例："[7:5]：NB"
            desc_part = f"{bits_raw}：{field_raw}"
            if curr_addr not in addr_temp_parts:
                addr_temp_parts[curr_addr] = []
            addr_temp_parts[curr_addr].append(desc_part)

            # 2. 解析物理位域 [7:0] 或 [4]
            p_match = re.findall(r'\d+', str(bits_raw))
            p_msb = int(p_match[0])
            p_lsb = int(p_match[-1])

            # 3. 解析默认值并更新 addr_defaults
            # 逻辑：将当前域的默认值按物理位偏移压入该地址的初始值中
            field_default = self._parse_raw_value(def_raw)
            if curr_addr not in self.addr_defaults:
                self.addr_defaults[curr_addr] = 0
            # 清除该段旧值（以防重复定义）并压入新值
            p_mask = ((1 << (p_msb - p_lsb + 1)) - 1) << p_lsb
            self.addr_defaults[curr_addr] = (self.addr_defaults[curr_addr] & ~p_mask) | (field_default << p_lsb)

            # 4. 解析逻辑域名与逻辑位权 (例如 "WC[11:8]")
            l_match = re.match(r"(\w+)\[(\d+):?(\d+)?]", str(field_raw))
            if l_match:
                logic_name = l_match.group(1)
                l_msb = int(l_match.group(2))
                l_lsb = int(l_match.group(3)) if l_match.group(3) else l_msb
            else:
                logic_name, l_msb, l_lsb = str(field_raw), p_msb, p_lsb

            # 5. 建立映射片段
            segment = {
                "addr": curr_addr,
                "p_msb": p_msb, "p_lsb": p_lsb,
                "l_msb": l_msb, "l_lsb": l_lsb,
                "modify": str(modify).strip().lower() == "yes",
                "analysis": str(analysis).strip().lower() == "yes"
            }
            self.logic_fields.setdefault(logic_name, []).append(segment)

        # 循环结束后的预生成逻辑：
        for addr, parts in addr_temp_parts.items():
            # 从之前存好的字典里拿寄存器名
            reg_name = self.addr_to_regname.get(addr, f"UNK_{hex(addr)}")
            # 直接拼接 Excel 里的原始 bits 和 field 信息
            # 结果示例: "e：[7:5]：NB； [4]：SB； [3:0]：NT"
            self.addr_descriptions[addr] = f"{reg_name}: {'; '.join(parts)}"

    def update_config(self, current_config, updates):
        """
        updates: {"WC": 0x5AA}
        逻辑：自动拆分 12-bit 值到对应的物理地址
        """
        new_config = current_config.copy()
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

                # 覆盖物理位段
                p_mask = ((1 << (seg["p_msb"] - seg["p_lsb"] + 1)) - 1) << seg["p_lsb"]
                new_config[addr] = (reg_val & ~p_mask) | (fragment << seg["p_lsb"])
        return new_config

    def parse_config(self, input_config):
        """
        逻辑：合并物理地址中的位，合成逻辑长值
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


# --- 全局延迟加载工厂 ---
@cache
def get_register_manager(path):
    # 确保路径标准化，防止重复加载
    return RegisterGenerate(os.path.abspath(path))


if __name__ == '__main__':
    # 1. 获取实例（内部会自动执行一次 Excel 解析并建立 addr_defaults）
    mgr = get_register_manager("./reg.xlsx")

    # 2. 假设我们要更新 WC 为 0x5AA (11位数据)
    # 物理上它会被拆分成：
    # 0x05 (WC[7:0]): 0xAA
    # 0x06 (WC[11:8]): 0x05 (只占低4位)
    new_cfg = mgr.update_config({}, {"WC": 0x5AA})
    print(f"Updated Config: {new_cfg}")
    # 输出应包含 {5: 170, 6: 5} (170即0xAA)

    # 3. 解析配置
    # 哪怕你只给出一个地址的值，另一个地址也会用默认值补全后再合并返回
    parsed = mgr.parse_config({0x05: 0xAA, 0x06: 0x01})
    print(f"Parsed Result: {parsed['WC']}")

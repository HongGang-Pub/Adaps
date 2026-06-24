"""
RegScriptIO - 寄存器脚本解析与回写引擎
================================================================================

【功能清单】

1. 解析脚本 (read_script)
   输入：原始脚本行列表（如 ["I2C_Write, 4A, 0037, 00", "// comment", ...]）
   输出：
     - parsed_data: {addr_int: val_int}，所有寄存器地址的当前值
     - line_contexts: 上下文列表，每项标记该行是否为寄存器行及其原始成分

   示例：
     lines = ["I2C_Write, 4A, 0037, 00", "// init", "I2C_Write, 4A, 0038, AA"]
     parsed_data, contexts = engine.read_script(lines)
     # parsed_data = {0x37: 0, 0x38: 0xAA}
     # contexts = [{"is_reg": True, "addr": 0x37, ...}, {"is_reg": False, "raw": "// init"}, ...]

2. 生成脚本 (write_script)
   输入：
     - line_contexts: read_script 返回的上下文列表（保留原始顺序和注释）
     - new_config: {addr: new_val}，待更新的寄存器地址键值对
   输出：
     - new_lines: 新脚本行列表，保持原始顺序，仅数值被更新；新增地址插入到合理位置

   核心原则——最小改动：
     - 存在的地址：原地修改数值，保留注释和格式
     - 不存在的地址（新配置）：插入到 new_config 中前序地址的后面，保持升序
     - 非寄存器行（注释、空行）：原样保留位置

3. 协议模板 (protocol_list)
   通过协议模板定义脚本格式，支持 I2C 和 SPI 两种协议：
     - I2C: ["I2C_Write", "4A", "{ADDR}", "{VAL}"]
     - SPI:  ["SPI_Write", "{ADDR}", "{VAL}"]

   模板中 {ADDR} 和 {VAL} 为占位符，分别被替换为地址和数值。

【使用示例】

# ---------- 示例 1：基本解析与更新 ----------
from RegScriptIO import RegScriptIO

engine = RegScriptIO(protocol_list=["I2C_Write", "4A", "{ADDR}", "{VAL}"], sep=",")

# 原始脚本
raw_script = [
    "I2C_Write, 4A, 0037, 00  // 初始化",
    "// 这是一个注释行",
    "I2C_Write, 4A, 0038, AA"
]

# 1. 解析
parsed_data, contexts = engine.read_script(raw_script)
# parsed_data = {0x37: 0, 0x38: 0xAA}
# contexts 保留了原始顺序、注释信息

# 2. 更新配置（只改存在的地址）
new_config = {0x37: 0x55}

# 3. 生成新脚本
new_script = engine.write_script(contexts, new_config)
# 输出：
# I2C_Write, 4A, 0037, 55  // 初始化
# // 这是一个注释行
# I2C_Write, 4A, 0038, AA

# ---------- 示例 2：新增地址（不在原始脚本中的寄存器） ----------
new_config = {0x37: 0x55, 0x3A: 0x11, 0x3C: 0x22}
new_script = engine.write_script(contexts, new_config)
# 0x3A 和 0x3C 会按顺序插入到 0x38 之后（因为 0x38 是 0x3A/0x3C 的前序已知地址）

# ---------- 示例 3：SPI 协议 ----------
spi_engine = RegScriptIO(protocol_list=["SPI_Write", "{ADDR}", "{VAL}"], sep=",")
raw_script = ["SPI_Write, 0037, 00", "SPI_Write, 0038, AA"]
parsed_data, contexts = spi_engine.read_script(raw_script)
# parsed_data = {0x37: 0, 0x38: 0xAA}

# ---------- 示例 4：结合 ExcelRegMapper 使用 ----------
from ExcelRegMapper import get_excel_mapper
from RegScriptIO import RegScriptIO

mapper = get_excel_mapper("./reg.xlsx")
engine = RegScriptIO(protocol_list=["I2C_Write", "4A", "{ADDR}", "{VAL}"], sep=",")

# 1. 解析原始脚本
csru_datas = PubMethod.read_file("ref_cfg.txt")
current_map, line_contexts = engine.read_script(csru_datas)

# 2. 构建更新（Excel 自动处理多 bit 拆分）
updates = {"WC": 0x5AA, "VC0_FLNR": 0x1234}
new_config = mgr.update_config(current_map, updates)

# 3. 生成新脚本
new_lines = engine.write_script(line_contexts, new_config)

# ---------- 示例 5：结合 Swan01/Hawk01 的 _beta 方法 ----------
# Swan01:
#   GenerateSwanRegConfig_beta(swan01_config)
#   内部：mgr.update_config(current_map, updates) + engine.write_script()

# Hawk01:
#   GenerateHawkRegConfig_beta(hawk01_config)
#   内部：同上

【注意事项】

- write_script 按照 new_config 的 key 顺序（Python 3.7+ 保证字典插入顺序）决定新地址的插入位置
- 如果新地址在原始脚本中不存在，它会被插入到前序已存在地址的后面
- 如果新地址小于第一个已存在地址，会插入到脚本最开头（锚点 -1）
- read_script 使用 partition 保留注释完整性，不会因分割而丢失
- 分隔符默认逗号 + 空格，输出格式固定为 ", " 分隔
"""

import os
from SelfDefinedPackge import PubMethod


class RegScriptOperate:
    def __init__(self, protocol_list, sep=','):
        """
        初始化 RegScriptIO。

        参数:
            protocol_list: 协议模板列表，必须包含 {ADDR} 和 {VAL} 占位符
                          示例：["I2C_Write", "4A", "{ADDR}", "{VAL}"]
            sep: 输入脚本的分隔符，默认为逗号
        """
        self.parse_sep = sep
        # 强制统一输出格式为：逗号 + 空格
        self.output_sep = ", "
        self.protocol = protocol_list
        # 从协议模板中自动获取 {ADDR} 和 {VAL} 的索引位置
        try:
            self.addr_idx = self.protocol.index("{ADDR}")
            self.val_idx = self.protocol.index("{VAL}")
        except ValueError:
            raise ValueError("协议模板必须包含 {ADDR} 和 {VAL} 占位符")
        # 最小长度：协议模板元素数量，用于判断是否为有效寄存器行
        self.min_len = len(self.protocol)

    def read_script(self, lines):
        """
        解析脚本行列表，提取所有寄存器地址和值。

        参数:
            lines: 原始脚本行列表，例如 ["I2C_Write, 4A, 0037, 00", "// comment", ...]

        返回:
            script_config: {addr_int: val_int}，所有寄存器地址的当前值
            script_contexts: 上下文列表，每个元素为：
                - 寄存器行：{"is_reg": True, "addr": int, "parts": [..], "comment": str}
                - 非寄存器行：{"is_reg": False, "raw": str}
        """
        script_config = {}
        script_contexts = []

        for line in lines:
            _str = line.strip().replace("\n", "").replace("\r", "")
            # 使用 partition 保持注释完整性：content 为 // 前部分，comment 为 // 后部分
            content, _, comment = _str.partition('//')
            # 按分隔符拆分并去除空白
            parts = [p.strip() for p in content.split(self.parse_sep) if p.strip()]

            is_target = False
            if len(parts) >= self.min_len:
                try:
                    # 按索引提取地址和数值的十六进制
                    addr_int = int(parts[self.addr_idx], 16)
                    val_int = int(parts[self.val_idx], 16)

                    script_config[addr_int] = val_int
                    script_contexts.append({
                        "is_reg": True,
                        "addr": addr_int,
                        "parts": parts,
                        "comment": comment.strip()
                    })
                    is_target = True
                except (ValueError, IndexError):
                    pass

            if not is_target:
                # 非寄存器行（注释、空行、无效行）保留原始内容
                script_contexts.append({"is_reg": False, "raw": _str})

        return script_config, script_contexts

    def update_script(self, script_contexts, new_config):
        """
        根据 new_config 回写脚本，保持最小改动原则。

        参数:
            script_contexts: read_script 返回的上下文列表
            new_config: {addr: new_val}，待更新的寄存器地址键值对

        返回:
            new_lines: 新脚本行列表，保持原始顺序，仅数值被更新

        处理逻辑（最小改动原则）:
            1. 遍历 line_contexts，按顺序重建脚本
            2. 寄存器行：如果地址在 new_config 中，替换数值；否则原样保留
            3. 非寄存器行：原样保留
            4. 新增地址（不在原始脚本中）：按 new_config 键的顺序，
               插入到其前序已存在地址的后面
        """
        new_lines = []
        # 建立地址到 line_contexts 索引的映射，用于快速查找已有地址
        addr_to_ctx_idx = {
            ctx["addr"]: i
            for i, ctx in enumerate(script_contexts)
            if ctx.get("is_reg")
        }

        # 插入计划：{锚点_ctx_idx: [待插入的行字符串, ...]}
        # 锚点为 -1 表示插入到脚本最开头
        insert_plan = {}
        last_known_ctx_idx = -1  # 默认锚点：脚本最开头

        # 按照 new_config 的 key 顺序遍历（Python 3.7+ 保持插入顺序）
        for addr in new_config.keys():
            if addr in addr_to_ctx_idx:
                # 命中已有行，更新锚点位置
                last_known_ctx_idx = addr_to_ctx_idx[addr]
            else:
                # 新增地址，生成行字符串
                new_row = [
                    p.replace("{ADDR}", f"{addr:04X}").replace("{VAL}", f"{new_config[addr]:02X}")
                    for p in self.protocol
                ]
                new_line_str = f"{self.output_sep.join(new_row)}  // New appended by order"

                # 记录在当前锚点之后插入
                if last_known_ctx_idx not in insert_plan:
                    insert_plan[last_known_ctx_idx] = []
                insert_plan[last_known_ctx_idx].append(new_line_str)

        # 处理锚点 -1 的插入（出现在第一个寄存器之前的配置）
        if -1 in insert_plan:
            new_lines.extend(insert_plan[-1])

        # 按原始顺序重建脚本行
        for i, ctx in enumerate(script_contexts):
            if ctx["is_reg"]:
                addr = ctx["addr"]
                parts = list(ctx["parts"])
                # 如果该地址在 new_config 中，替换数值
                if addr in new_config:
                    parts[self.val_idx] = f"{new_config[addr]:02X}"

                # 重建行字符串，保留原始注释
                line_str = self.output_sep.join(parts)
                if ctx.get("comment"):
                    line_str = f"{line_str}  // {ctx['comment']}"
                new_lines.append(line_str)
            else:
                # 非寄存器行（注释、空行等）原样保留
                new_lines.append(ctx["raw"])

            # 检查当前行索引是否有待插入的"随从"（同锚点的新增行）
            if i in insert_plan:
                new_lines.extend(insert_plan[i])

        return new_lines


if __name__ == '__main__':
    # 演示：手术刀式的精准回写
    engine = RegScriptOperate(protocol_list=["I2C_Write", "4A", "{ADDR}", "{VAL}"], sep=",")

    ref_cfg_file = r"D:\Git\Adaps\Software\ADAPSS~1\SCRIPT~1.10\Input\Hawk01_base_script.txt"
    raw_script = PubMethod.read_file(ref_cfg_file)

    # 1. 解析
    current_map, contexts = engine.read_script(raw_script)
    print(f"Parsed {len(current_map)} registers")

    # 2. 模拟配置更新
    current_map = {}
    current_map[0x37] = 0x55
    current_map[0x3A] = 0x11
    current_map[0x3C] = 0x22

    # 3. 生成新脚本
    updated_script = engine.update_script(contexts, current_map)

    # 输出结果：注释被保留，格式未破坏，只有数值变了
    for line in updated_script:
        print(line)

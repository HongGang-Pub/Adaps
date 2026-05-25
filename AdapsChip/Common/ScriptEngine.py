import os

import os

from SelfDefinedPackge import PubMethod


class ScriptEngine:
    def __init__(self, protocol_list, sep=','):
        """
        protocol_list: 例如 ["I2C_Write", "4A", "{ADDR}", "{VAL}"]
        """
        self.parse_sep = sep
        self.output_sep = ", "  # 强制统一输出格式为：逗号 + 空格
        self.protocol = protocol_list
        # 自动获取索引
        try:
            self.addr_idx = self.protocol.index("{ADDR}")
            self.val_idx = self.protocol.index("{VAL}")
        except ValueError:
            raise ValueError("协议模板必须包含 {ADDR} 和 {VAL} 占位符")
        self.min_len = len(self.protocol)

    def parse_and_store(self, lines):
        parsed_data = {}
        line_contexts = []

        for line in lines:
            _str = line.strip().replace("\n", "").replace("\r", "")
            # 使用 partition 保持注释完整性
            content, _, comment = _str.partition('//')
            # parts = [p.strip() for p in content.split(self.sep.strip())]  # 兼容带空格的分隔符
            parts = [p.strip() for p in content.split(self.parse_sep) if p.strip()]

            is_target = False
            if len(parts) >= self.min_len:
                try:
                    # 尝试按索引提取十六进制数值
                    addr_int = int(parts[self.addr_idx], 16)
                    val_int = int(parts[self.val_idx], 16)

                    parsed_data[addr_int] = val_int
                    line_contexts.append({
                        "is_reg": True,
                        "addr": addr_int,
                        "parts": parts,
                        "comment": comment
                    })
                    is_target = True
                except (ValueError, IndexError):
                    pass

            if not is_target:
                line_contexts.append({"is_reg": False, "raw": _str})

        return parsed_data, line_contexts

    def generate_script(self, line_contexts, updated_map):
        """
        以最小改动原则回写：
        1. 存在的地址原地修改。
        2. 不存在的地址插入到其在 updated_map 中前序地址的后面。
        """
        new_lines = []
        # 记录已在脚本中存在的地址及其在 line_contexts 中的索引
        # addr_to_ctx_idx: {addr: context_list_index}
        addr_to_ctx_idx = {
            ctx["addr"]: i
            for i, ctx in enumerate(line_contexts)
            if ctx.get("is_reg")
        }

        # 预计算：哪些地址需要“插队”，插在谁后面
        # insert_plan: {target_ctx_idx: [new_line_str, ...]}
        insert_plan = {}
        last_known_ctx_idx = -1  # 默认锚点：脚本最开头

        # 按照 updated_map 的 key 顺序遍历（Python 3.7+ 保持插入顺序）
        for addr in updated_map.keys():
            if addr in addr_to_ctx_idx:
                # 命中已有行，更新锚点
                last_known_ctx_idx = addr_to_ctx_idx[addr]
            else:
                # 新增地址，准备插入
                new_row = [p.replace("{ADDR}", f"{addr:04X}").replace("{VAL}", f"{updated_map[addr]:02X}")
                           for p in self.protocol]
                new_line_str = f"{self.output_sep.join(new_row)}  // New appended by order"

                # 记录在当前锚点之后插入
                if last_known_ctx_idx not in insert_plan:
                    insert_plan[last_known_ctx_idx] = []
                insert_plan[last_known_ctx_idx].append(new_line_str)

        # 开始构建最终行列表
        # 处理 -1 锚点（出现在第一个寄存器之前的配置）
        if -1 in insert_plan:
            new_lines.extend(insert_plan[-1])

        for i, ctx in enumerate(line_contexts):
            if ctx["is_reg"]:
                addr = ctx["addr"]
                parts = list(ctx["parts"])
                if addr in updated_map:
                    parts[self.val_idx] = f"{updated_map[addr]:02X}"

                # 压入当前行
                line_str = self.output_sep.join(parts)
                if ctx.get("comment"):
                    line_str = f"{line_str}  // {ctx['comment']}"
                new_lines.append(line_str)
            else:
                # 压入非寄存器行（注释、空行等）
                new_lines.append(ctx["raw"])

            # 检查当前行索引是否有待插入的“随从”
            if i in insert_plan:
                new_lines.extend(insert_plan[i])

        return new_lines


if __name__ == '__main__':
    # --- 演示：手术刀式的精准回写 ---
    engine = ScriptEngine(protocol_list=["I2C_Write", "4A", "{ADDR}", "{VAL}"], sep=",")

    # raw_script = [
    #     "I2C_Write, 4A, 0037, 00  // 初始化配置",
    #     "// 这是一个无关的注释行",
    #     "I2C_Write, 4A, 0038, AA"
    # ]

    ref_cfg_file = r"D:\Git\Adaps\Software\ADAPSS~1\SCRIPT~1.10\Input\Hawk01_base_script.txt"
    raw_script = PubMethod.read_file(ref_cfg_file)
    # 1. 解析
    current_map, contexts = engine.parse_and_store(raw_script)

    # 2. 模拟配置更新：0x37 -> 0x55
    current_map = {}
    current_map[0x37] = 0x55
    current_map[0x3A] = 0x11
    current_map[0x3C] = 0x11

    # 3. 生成新脚本
    updated_script = engine.generate_script(contexts, current_map)

    # 输出结果：注释被保留，格式未破坏，只有数值变了
    for line in updated_script:
        print(line)
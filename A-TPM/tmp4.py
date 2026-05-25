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
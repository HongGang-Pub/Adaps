import os
import re
from SelfDefinedPackge import PubMethod


class RegScriptOperate:
    def __init__(self, in_template, out_template, parse_sep=',', parse_comment_sym='//', gen_comment_sym='#'):
        """
        初始化 RegScriptIO，支持灵活的字符串模板解析与生成。

        参数:
            in_template: 解析用的输入模板字符串
                         支持静态校验: "{val0=I2C_Write}, {val1}, {ADDR:16}, {VAL:16}"
            out_template: 生成用的输出模板字符串（只包含有效字段格式化语法，不包含注释部分）
                          例如："TEST, {val1}, {ADDR:0>4X}, {VAL:0>2X}"
            parse_sep: 解析脚本时的元素分隔符
            parse_comment_sym: 解析脚本时的注释标识符
            gen_comment_sym: 生成脚本时的注释标识符
        """
        self.parse_sep = parse_sep
        self.parse_comment_sym = parse_comment_sym
        self.gen_comment_sym = gen_comment_sym
        self.in_template_str = in_template
        self.out_template_str = out_template

        # 自动提取输入模板中的变量名、进制信息、以及强校验值
        in_keys_raw = re.findall(r"\{([^}]+)\}", self.in_template_str)
        self.in_keys_info = []
        has_addr = False
        has_val = False
        
        for k in in_keys_raw:
            base = None
            match_val = None

            if "=" in k:
                # 例如 val0=I2C_Write
                name, match_val = k.split("=", 1)
            elif ":" in k:
                # 例如 ADDR:16
                name, base_str = k.split(":", 1)
                base = int(base_str)
            else:
                name = k
                
            # 强管控：只有 ADDR 和 VAL 允许拥有进制信息并参与 int 转换，其他全部当作纯字符串
            if name not in ("ADDR", "VAL"):
                base = None
            elif base is None:
                # 是 ADDR/VAL 且没显式声明，兜底给 16
                base = 16
                
            if name == "ADDR": has_addr = True
            if name == "VAL": has_val = True
            
            self.in_keys_info.append((name, base, match_val))

        if not has_addr or not has_val:
            raise ValueError("输入模板(in_template)必须包含 {ADDR} 和 {VAL} 占位符")
        
        self.std_len = len(self.in_keys_info)

    def read_script(self, lines):
        """
        解析脚本行列表，仅返回结构化的上下文 (script_contexts)。
        """
        script_contexts = []

        for line in lines:
            _str = line.strip().replace("\n", "").replace("\r", "")
            # 使用 partition 保持注释完整性
            content, _, comment = _str.partition(self.parse_comment_sym)
            # 按分隔符拆分并去除空白
            parts = [p.strip() for p in content.split(self.parse_sep) if p.strip()]

            is_target = False
            # 严格长度校验
            if len(parts) == self.std_len:
                try:
                    variables = {}
                    match_failed = False
                    
                    for (name, base, match_val), v_str in zip(self.in_keys_info, parts):
                        # 静态强校验：如果输入模板中定义了等于号，必须严格匹配该字符串
                        if match_val is not None and v_str != match_val:
                            match_failed = True
                            break
                            
                        if name in ("ADDR", "VAL"):
                            variables[name] = int(v_str, base)
                        else:
                            variables[name] = v_str
                            
                    if not match_failed:
                        variables["comment"] = comment.strip()

                        addr_int = variables["ADDR"]

                        script_contexts.append({
                            "is_reg": True,
                            "addr": addr_int,
                            "variables": variables,
                            "raw": _str
                        })
                        is_target = True
                except (ValueError, KeyError):
                    pass

            if not is_target:
                # 非寄存器行（注释、空行、无效行）保留原始内容
                script_contexts.append({"is_reg": False, "raw": _str})

        return script_contexts

    def update_script(self, script_contexts, new_config):
        """
        根据 new_config 回写脚本，保持最小改动原则。
        """
        new_lines = []
        addr_to_ctx_idx = {
            ctx["addr"]: i
            for i, ctx in enumerate(script_contexts)
            if ctx.get("is_reg")
        }

        insert_plan = {}
        last_known_ctx_idx = -1 
        
        # 提取上一行已知的字符串变量（例如 val0, val1），供新增行使用
        latest_vals = {}
        for ctx in script_contexts:
            if ctx.get("is_reg"):
                latest_vals.update({k: v for k, v in ctx["variables"].items() if k not in ("ADDR", "VAL", "comment")})
                break  # 拿第一行的做底本即可

        for addr in new_config.keys():
            if addr in addr_to_ctx_idx:
                last_known_ctx_idx = addr_to_ctx_idx[addr]
            else:
                # 构建新增行的变量集合
                new_vars = dict(latest_vals)
                new_vars["ADDR"] = addr
                new_vars["VAL"] = new_config[addr]
                new_vars["comment"] = "New appended by order"
                
                new_line_str = self.out_template_str.format(**new_vars)
                # 统一拼接注释符和注释内容
                new_line_str += f" {self.gen_comment_sym} {new_vars['comment']}"
                
                if last_known_ctx_idx not in insert_plan:
                    insert_plan[last_known_ctx_idx] = []
                insert_plan[last_known_ctx_idx].append(new_line_str)

        if -1 in insert_plan:
            new_lines.extend(insert_plan[-1])

        for i, ctx in enumerate(script_contexts):
            if ctx.get("is_reg"):
                addr = ctx["addr"]
                variables = dict(ctx["variables"])
                
                # 更新寄存器的值
                if addr in new_config:
                    variables["VAL"] = new_config[addr]

                # 通过 format 引擎一键格式化输出
                try:
                    line_str = self.out_template_str.format(**variables)
                    # 如果这行本身带有注释，则自动用指定的生成注释符拼接到末尾
                    if variables["comment"]:
                        line_str += f" {self.gen_comment_sym} {variables['comment']}"
                except KeyError as e:
                    raise ValueError(f"输出模板所需的变量 {e} 没有在输入模板中定义！")

                new_lines.append(line_str)
            else:
                new_lines.append(ctx["raw"])

            if i in insert_plan:
                new_lines.extend(insert_plan[i])

        return new_lines


if __name__ == '__main__':
    # 演示：极简纯净的模板 + 独立的注释符号定义 + 强校验
    in_tpl = "{val0=I2C_Write}, {val1}, {ADDR:16}, {VAL:16}"
    out_tpl = "TEST, {val1},  {ADDR:0>4X}, {VAL:0>2X}"
    engine = RegScriptOperate(in_template=in_tpl, out_template=out_tpl, 
                              parse_sep=",", parse_comment_sym="//", gen_comment_sym="#")

    raw_script = [
        "I2C_Write, 4A, 0037, 00 // init comment",
        "SPI_Write, 4A, 0038, AA", # 会因为强校验失败而被当作非寄存器行跳过
        "// 纯注释行",
        "I2C_Write, 4A, 0039, 11" # 无注释的合法行
    ]

    # 1. 解析
    contexts = engine.read_script(raw_script)
    
    # 外部自己生成 config map
    current_map = {ctx["addr"]: ctx["variables"]["VAL"] for ctx in contexts if ctx.get("is_reg")}
    print(f"Parsed {len(current_map)} registers")

    # 2. 模拟配置更新
    current_map[0x37] = 0x55
    current_map[0x39] = 0x22

    # 3. 生成新脚本
    updated_script = engine.update_script(contexts, current_map)

    # 输出结果
    for line in updated_script:
        print(line)

"""
RegConfigProcessor - 高层统筹类，一键式完成“读取脚本 -> Excel映射解析 -> 回写脚本”流水线
"""

from AdapsChip.Common.GetRegArchByExcel import get_reg_arch
from AdapsChip.Common.RegScriptOperate import RegScriptOperate


def convert_legacy_protocol_list_to_templates(protocol_list):
    """
    将旧版 protocol_list (如 ["I2C_Write", "4A", "{ADDR}", "{VAL}"]) 转换为新版的字符串模板
    """
    in_parts = []
    out_parts = []
    for i, p in enumerate(protocol_list):
        if p == "{ADDR}":
            in_parts.append("{ADDR:16}")
            out_parts.append("{ADDR:0>4X}")
        elif p == "{VAL}":
            in_parts.append("{VAL:16}")
            out_parts.append("{VAL:0>2X}")
        else:
            in_parts.append(f"{{val{i}={p}}}")
            out_parts.append(f"{{val{i}}}")
    in_tpl = ", ".join(in_parts)
    out_tpl = ", ".join(out_parts)
    return in_tpl, out_tpl


class RegConfigProcessor:
    def __init__(self, excel_path, in_template, out_template, parse_sep=',', parse_comment_sym='//', gen_comment_sym='#'):
        """
        初始化高层管家，内部自动挂载 Excel Mapper 和 Script Engine
        """
        self.RegArch = get_reg_arch(excel_path)
        self.ScriptOperate = RegScriptOperate(
            in_template=in_template, 
            out_template=out_template, 
            parse_sep=parse_sep, 
            parse_comment_sym=parse_comment_sym, 
            gen_comment_sym=gen_comment_sym
        )

    def update_script(self, script_lines, updates):
        """
        一键式流水线：读老脚本 -> 注入逻辑更新 -> 吐出新脚本
        """
        script_contexts = self.ScriptOperate.read_script(script_lines)
        old_config = {ctx["addr"]: ctx["variables"]["VAL"] for ctx in script_contexts if ctx.get("is_reg")}
        new_config = self.RegArch.logical_to_physical(old_config, updates)
        return self.ScriptOperate.update_script(script_contexts, new_config)

    def parse_to_logic(self, script_lines):
        """
        一键式流水线：读老脚本 -> 提取所有已分析的逻辑配置字典
        """
        script_contexts = self.ScriptOperate.read_script(script_lines)
        old_config = {ctx["addr"]: ctx["variables"]["VAL"] for ctx in script_contexts if ctx.get("is_reg")}
        return self.RegArch.physical_to_logical(old_config)

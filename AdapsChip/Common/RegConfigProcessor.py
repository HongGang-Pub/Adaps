"""
RegConfigProcessor - 高层统筹类，一键式完成“读取脚本 -> Excel映射解析 -> 回写脚本”流水线
"""

from AdapsChip.Common.GetRegArchByExcel import get_reg_arch
from AdapsChip.Common.RegScriptOperate import RegScriptOperate


class RegConfigProcessor:
    def __init__(self, excel_path, protocol_list, sep=','):
        """
        初始化高层管家，内部自动挂载 Excel Mapper 和 Script Engine
        """
        self.RegArch = get_reg_arch(excel_path)
        self.ScriptOperate = RegScriptOperate(protocol_list=protocol_list, sep=sep)

    def update_script(self, script_lines, updates):
        """
        一键式流水线：读老脚本 -> 注入逻辑更新 -> 吐出新脚本
        """
        old_config, script_contexts = self.ScriptOperate.read_script(script_lines)
        new_config = self.RegArch.logical_to_physical(old_config, updates)
        return self.ScriptOperate.update_script(script_contexts, new_config)

    def parse_to_logic(self, script_lines):
        """
        一键式流水线：读老脚本 -> 提取所有已分析的逻辑配置字典
        """
        script_config, _ = self.ScriptOperate.read_script(script_lines)
        return self.RegArch.physical_to_logical(script_config)

"""
RegConfigProcessor - 高层统筹类，一站式完成：读取脚本 -> Excel映射 -> 写回脚本的流水线
"""

from AdapsChip.Common.GetRegArchByExcel import get_reg_arch
from AdapsChip.Common.FileOperateClass import FileOperateClass


class RegScriptOperate:
    def __init__(self, chip_config: dict):
        excel_path = chip_config["RegExcelPath"]
        template_config = load_template_config(chip_config["ScriptTemplate"])
        
        self.RegArch = get_reg_arch(excel_path)
        self.RegConfigOperate = FileOperateClass(template_config["REG_CONFIG"])
        self.ROISRAMOperate = FileOperateClass(template_config["ROISRAM_CONFIG"])

    def parse_to_logic(self, script_lines):
        old_config = {}
        for line in script_lines:
            is_match, variables = self.RegConfigOperate.parse_line(line)
            if is_match:
                old_config[variables["ADDR"]] = variables["VAL"]
        return self.RegArch.physical_to_logical(old_config)

    def update_script(self, script_lines, updates):
        # 第一遍：解析出所有行的上下文并缓存
        parsed_contexts = []
        old_config = {}
        last_match_idx = -1
        last_vals = {}

        for i, line in enumerate(script_lines):
            is_match, variables = self.RegConfigOperate.parse_line(line)
            parsed_contexts.append((line, is_match, variables))
            
            if is_match:
                old_config[variables["ADDR"]] = variables["VAL"]

        new_config = self.RegArch.logical_to_physical(old_config, updates)

        # 第二遍：直接使用缓存的上下文进行数据覆盖和快速生成
        new_lines = []
        for i, (orig_line, is_match, variables) in enumerate(parsed_contexts):
            if is_match:
                addr = variables["ADDR"]
                if addr in new_config:
                    variables["VAL"] = new_config[addr]
                    new_lines.append(self.RegConfigOperate.generate_line(**variables))
                    last_match_idx = i
                    last_vals = variables
                else:
                    new_lines.append(orig_line)
            else:
                new_lines.append(orig_line)

        for addr, val in new_config.items():
            if addr not in old_config:
                new_vars = dict(last_vals)
                new_vars["ADDR"] = addr
                new_vars["VAL"] = val
                desc = self.RegArch.addr_descriptions.get(addr, f"UNK_{hex(addr)}")
                new_vars["comment"] = f"New appended: {desc}"
                try:
                    new_lines.insert(last_match_idx + 1, self.RegConfigOperate.generate_line(**new_vars))
                    last_match_idx += 1
                except ValueError:
                    pass

        return new_lines

    def update_roi_script(self, script_lines, roi_updates: dict):
        """
        专门处理 ROI 配置更新的方法。
        roi_updates 例如: {"LENGTH": 1200, "ROISRAM_NAME": "my_roi"}
        """
        new_lines = []
        for line in script_lines:
            success, new_line = self.ROISRAMOperate.strconvert(line, **roi_updates)
            if success:
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        return new_lines


import configparser
import os
from SelfDefinedPackge import PubMethod, LogerPubMethod


def load_template_config(ini_path: str) -> dict:
    config = configparser.ConfigParser()
    config.read(ini_path, encoding='utf-8')
    template_config = {}
    if config.has_section("REG_CONFIG"):
        template_config["REG_CONFIG"] = {
            "in_template": config.get("REG_CONFIG", "in_template"),
            "out_template": config.get("REG_CONFIG", "out_template"),
            "parse_sep": config.get("REG_CONFIG", "parse_sep", fallback=","),
            "parse_comment_sym": config.get("REG_CONFIG", "parse_comment_sym", fallback="//"),
            "gen_comment_sym": config.get("REG_CONFIG", "gen_comment_sym", fallback="//")
        }
    if config.has_section("ROISRAM_CONFIG"):
        template_config["ROISRAM_CONFIG"] = {
            "in_template": config.get("ROISRAM_CONFIG", "in_template"),
            "out_template": config.get("ROISRAM_CONFIG", "out_template"),
            "parse_sep": config.get("ROISRAM_CONFIG", "parse_sep", fallback=","),
            "parse_comment_sym": config.get("ROISRAM_CONFIG", "parse_comment_sym", fallback="//"),
            "gen_comment_sym": config.get("ROISRAM_CONFIG", "gen_comment_sym", fallback="//")
        }
    return template_config


def GetCsruConfig_beta(config_file, chip_config) -> dict:
    csru_datas = PubMethod.read_file(fname=config_file)
    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check.")

    processor = RegScriptOperate(chip_config)
    csru_cfg = processor.parse_to_logic(csru_datas)
    return csru_cfg


def ParseRegConfig_beta(script_file, chip_config: dict):
    """
    通用解析配置方法，返回解析后的 csru_cfg
    """
    
    if not os.path.exists(script_file):
        raise ValueError("The reference config file does not exist!")

    csru_cfg = GetCsruConfig_beta(script_file, chip_config)
    
    _hyper_link = LogerPubMethod.create_file_hyperlink(url=script_file)
    info = f"Parse {_hyper_link}..."
    _str  = "---------------------------\n"
    _str += "REG_CONFIG\n"
    _str += "---------------------------\n"
    info_json = PubMethod.dict_print_format(csru_cfg, indent=2, level=1)
    _str += info_json
    _str = LogerPubMethod.create_consolas_str(_str, color="#0076f6")
    print(f"{info}<br>{_str}")
    
    return csru_cfg


def GenerateRegConfig_beta(chip_config: dict, updates: dict, roi_updates: dict = None):
    """
    通用生成与保存配置的方法
    """
    ref_cfg_file = chip_config["ref_cfg_file"]
    if not os.path.exists(ref_cfg_file):
        raise ValueError("The reference config file does not exist!")

    # 读取基准脚本
    csru_datas = PubMethod.read_file(fname=ref_cfg_file)
    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check.")

    # 使用 RegScriptOperate 生成新脚本
    processor = RegScriptOperate(chip_config)
    new_lines = processor.update_script(csru_datas, updates)

    if roi_updates:
        new_lines = processor.update_roi_script(new_lines, roi_updates)

    # --------------------------------------------------------
    # 增加配置说明
    # --------------------------------------------------------
    config_instruction = "config_instruction"
    config_print = "PRINT"
    if config_instruction in chip_config and config_print in chip_config[config_instruction]:
        _str = "// "
        _len = len(chip_config[config_instruction][config_print])
        for i in range(_len):
            config = chip_config[config_instruction][config_print][i]
            if i > 0:
                _str += "; "
            _str += f"{config}: {chip_config[config_instruction][config][chip_config[config]]}"
        new_lines.insert(0, _str)

    PubMethod.data_save(fname=f'{chip_config["reg_name"]}.txt',
                        data_list=new_lines,
                        split='\n',
                        fd_path=chip_config["fd_path"])
    return new_lines


if __name__ == '__main__':
    load_template_config(ini_path=r"D:\Git\Adaps\AdapsChip\ChipUI\.Hawk01Config\Hawk01ScriptTemplate.ini")

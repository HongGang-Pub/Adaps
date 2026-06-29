"""
RegConfigProcessor - 高层统筹类，一站式完成：读取脚本 -> Excel映射 -> 写回脚本的流水线
"""

from AdapsChip.Common.GetRegArchByExcel import get_reg_arch
from AdapsChip.Common.FileOperateClass import FileOperateClass


class RegScriptOperate:
    def __init__(self, chip_config: dict):
        """
        初始化寄存器脚本操作引擎。
        自动加载 Excel 寄存器映射架构 (RegArch) 以及基础和 ROI 模板格式 (FileOperateClass)。
        """
        excel_path = chip_config["RegExcelPath"]
        template_config = load_template_config(chip_config["ScriptTemplate"])
        
        self.RegArch = get_reg_arch(excel_path)
        self.RegConfigOperate = FileOperateClass(template_config["REG_CONFIG"])
        self.ROISRAMOperate = FileOperateClass(template_config["ROISRAM_CONFIG"])

    def parse_to_logic(self, script_lines):
        """
        从基准脚本行中解析所有的寄存器写入指令，并将其物理地址与值映射为易读的逻辑变量名（基于 Excel 模板）。
        
        Args:
            script_lines (list[str]): 原始脚本行列表。
            
        Returns:
            dict: 逻辑变量名到其对应值的映射字典。
        """
        old_config = {}
        # 遍历读取到的每一行脚本
        for line in script_lines:
            # 尝试使用底座 FileOperateClass 的规则去解析当前行
            success, variables = self.RegConfigOperate.parse_line(line)
            if success:
                # 提取出有效的 ADDR 和 VAL 并放入旧配置字典
                old_config[variables["ADDR"]] = variables["VAL"]
                
        # 将物理地址和真实值，通过 RegArch (由 Excel 解析得来) 反转为逻辑变量名字典
        return self.RegArch.physical_to_logical(old_config)

    def update_script(self, script_lines, updates):
        """
        根据给定的逻辑变量更新字典，智能地将旧脚本中相关的寄存器值进行覆盖。
        采用双重遍历和局部修改，保证脚本原本的注释、无关行和空行均保持不变；并支持自动追加新的寄存器。
        
        Args:
            script_lines (list[str]): 待修改的原始脚本行列表。
            updates (dict): 需要更新的逻辑变量字典（如 {"SCAN_MODE": 1, "PLL0_ID": 3}）。
            
        Returns:
            list[str]: 注入了新寄存器配置的全新脚本行列表。
        """
        # 第一遍：解析出所有行的上下文并缓存
        parsed_contexts = []
        old_config = {}
        last_match_idx = -1
        last_vals = {}

        # 遍历基准脚本以构建旧环境映射
        for i, line in enumerate(script_lines):
            success, variables = self.RegConfigOperate.parse_line(line)
            # 缓存原始行、匹配状态以及解析出的变量，供第二遍生成使用
            parsed_contexts.append((line, success, variables))
            
            if success:
                # 记录从脚本中读到的物理地址及其值
                old_config[variables["ADDR"]] = variables["VAL"]

        # 结合旧环境的值与要更新的逻辑变量，计算出需要覆盖或新增的物理寄存器映射字典
        new_config = self.RegArch.logical_to_physical(old_config, updates)

        # 第二遍：直接使用缓存的上下文进行数据覆盖和快速生成
        new_lines = []
        for i, (orig_line, success, variables) in enumerate(parsed_contexts):
            if success:
                addr = variables["ADDR"]
                # 如果这个物理地址在我们新算出来的需要更新的列表中
                if addr in new_config:
                    # 覆盖旧值
                    variables["VAL"] = new_config[addr]
                    # 生成新的一行并追加
                    new_lines.append(self.RegConfigOperate.generate_line(**variables))
                    # 记录最近一次成功写入的寄存器位置，用于后续有可能追加的新寄存器行
                    last_match_idx = i
                    last_vals = variables
                else:
                    # 对于不需要更新的寄存器，保留原样
                    new_lines.append(orig_line)
            else:
                # 非匹配行（如注释、空行、其他不支持的行），完全保留原样
                new_lines.append(orig_line)

        # 第三遍：如果在 new_config 里有原本脚本中不存在的新寄存器，则将其追加到最后一个寄存器行下面
        for addr, val in new_config.items():
            if addr not in old_config:
                # 复制最后一个有效寄存器行中的静态参数 (比如 I2C_Write, Device_ID 等)
                new_vars = dict(last_vals)
                new_vars["ADDR"] = addr
                new_vars["VAL"] = val
                # 根据地址获取其说明信息，构造追踪注释
                desc = self.RegArch.addr_descriptions.get(addr, f"UNK_{hex(addr)}")
                new_vars["comment"] = f"New appended: {desc}"
                try:
                    # 在最后一次成功写入的位置后面插入这行全新的寄存器写入脚本
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
        # 逐行遍历并尝试使用 ROISRAMOperate 的规则进行部分替换
        for line in script_lines:
            success, new_line = self.ROISRAMOperate.strconvert(line, **roi_updates)
            if success:
                # 如果是 ROI 相关的行并且更新成功，则替换为新行
                new_lines.append(new_line)
            else:
                # 如果不是，则保持原样
                new_lines.append(line)
        return new_lines


import configparser
import os
from SelfDefinedPackge import PubMethod, LogerPubMethod


def load_template_config(ini_path: str) -> dict:
    """
    从指定的 .ini 配置文件中加载 REG 和 ROISRAM 相关的脚本读写模板。
    
    Args:
        ini_path (str): 模板配置文件的绝对或相对路径。
        
    Returns:
        dict: 包含了输入、输出模板字符串及解析符信息的配置字典。
    """
    config = configparser.ConfigParser()
    config.read(ini_path, encoding='utf-8')
    template_config = {}
    
    # 尝试读取通用寄存器配置的模板
    if config.has_section("REG_CONFIG"):
        template_config["REG_CONFIG"] = {
            "in_template": config.get("REG_CONFIG", "in_template"),
            "out_template": config.get("REG_CONFIG", "out_template"),
            "parse_sep": config.get("REG_CONFIG", "parse_sep", fallback=","),
            "parse_comment_sym": config.get("REG_CONFIG", "parse_comment_sym", fallback="//"),
            "gen_comment_sym": config.get("REG_CONFIG", "gen_comment_sym", fallback="//")
        }
        
    # 尝试读取 ROISRAM 专用的模板
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
    """
    读取指定的寄存器脚本文件，返回解析所得的逻辑配置字典 (csru_cfg)。
    """
    csru_datas = PubMethod.read_file(fname=config_file)
    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check.")

    processor = RegScriptOperate(chip_config)
    csru_cfg = processor.parse_to_logic(csru_datas)
    return csru_cfg


def ParseRegConfig_beta(script_file, chip_config: dict):
    """
    通用的脚本解析入口函数：
    1. 调用 GetCsruConfig_beta 获取配置字典。
    2. 控制台打印美化后的日志信息，便于在 ChipUI 等终端展示。
    
    Args:
        script_file (str): 寄存器脚本文件的路径。
        chip_config (dict): 芯片相关的基础配置字典（需包含 RegExcelPath 等基础信息）。
        
    Returns:
        dict: 成功解析出的逻辑配置字典。
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
    通用的脚本生成与保存主流程：
    1. 读取参考脚本（基准文件）。
    2. 使用 RegScriptOperate 将 updates 注入到脚本中，生成新脚本。
    3. （可选）对特殊的 ROISRAM 模块进行单独更新。
    4. 注入配置的说明头注释，然后直接落盘保存文件。
    
    Args:
        chip_config (dict): 包含生成所需的外部路径及配置打印指令的基础字典。
        updates (dict): 包含了用户最新选项以及根据频率/模式等计算得出的各逻辑变量。
        roi_updates (dict, optional): 用于单独替换 ROISRAM_NAME 和 LENGTH 的字典。
        
    Returns:
        list[str]: 最终生成的完整脚本行。
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

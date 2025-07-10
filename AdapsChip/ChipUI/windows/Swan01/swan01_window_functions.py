import copy
import os

from AdapsChip.Swan01 import Swan01PubMethod
from SelfDefinedPackge import LogerPubMethod


def ScriptUIOperate(swan01_config: dict, operate: int = 0b11):
    """
    根据配置生成Swan01配置脚本
        swan01_config (dict): Swan 配置集合
        operate (int): operate[0]: slot_read_time_cal: 计算帧率; operate[1]: 保存脚本
    """
    __swan01_config__ = copy.deepcopy(swan01_config)
    # __reg_cfg__ = copy.deepcopy(reg_cfg)
    # print(__swan01_config__)
    work_mode_q = swan01_config["WORK_MODE"]

    def traverse_dict(d, parent_key=''):
        for key, value in d.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                traverse_dict(value, full_key)
            else:
                try:
                    d[key] = eval(value)
                except:
                    pass

    # traverse_dict(d=__reg_cfg__, parent_key='')     # 将reg_config的配置值全部转换为数字类型

    for work_mode in work_mode_q:
        __swan01_config__["WORK_MODE"] = work_mode
        __swan01_config__["reg_name"] = swan01_config["reg_name"] if len(work_mode_q) == 0 \
            else f'SPHR_{swan01_config["reg_name"]}' if work_mode == 0 \
            else f'PHR_{swan01_config["reg_name"]}' if work_mode == 1 \
            else f'FHR_{swan01_config["reg_name"]}' if work_mode == 2 \
            else f'PCM_{swan01_config["reg_name"]}'  # if work_mode == 3 \
        if operate & 0b01:
            Swan01PubMethod.SwanHistReadTimeCal(swan01_config=__swan01_config__)
        if operate & 0b10:
            Swan01PubMethod.GenerateSwanRegConfig(swan01_config=__swan01_config__,
                                                  reg_cfg_fp=__swan01_config__["Swan01RegConfigFile"])
            # Swan01PubMethod.GenerateSwanRegConfigByJson(swan01_config=__swan01_config__, reg_cfg=__reg_cfg__)
            url = f'{__swan01_config__["fd_path"]}/{__swan01_config__["reg_name"]}.txt'
            _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
            info = f"Script data has been save to {_hyper_link}"
            print(info)


def ScriptParse(swan01_config, file):
    Swan01PubMethod.ParseSwanRegConfig(file, swan01_config["protocol"])

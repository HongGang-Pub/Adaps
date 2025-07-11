import copy
import logging
import os

import AdapsChip.Common.common
from AdapsChip.Swan01 import Swan01PubMethod
from AdapsChip.Swan01 import Swan01ROISramOperation
from SelfDefinedPackge import LogerPubMethod


def ScriptUICoinfigOperate(swan01_config: dict, operate: int = 0b001):
    """
    根据配置生成Swan01配置脚本
        swan01_config (dict): Swan 配置集合
        operate (int): operate[0]: slot_read_time_cal: 计算帧率; operate[1]: 保存脚本, operate[2]: 计算 ROI
    """
    __swan01_config__ = copy.deepcopy(swan01_config)
    # __reg_cfg__ = copy.deepcopy(reg_cfg)
    # print(__swan01_config__)
    work_mode_q = swan01_config["WORK_MODE"]
    work_mode_name_q = swan01_config["config_instruction"]["WORK_MODE"]

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

    dataflow_related_config = Swan01PubMethod.SwanDataflowRelateConfigGet(__swan01_config__)
    if operate & 0b01 and dataflow_related_config is not None:
        print(f"MIPI_PKT_INTV: {dataflow_related_config['MIPI_PKT_INTV']} ns")
    for work_mode in work_mode_q:
        __swan01_config__["WORK_MODE"] = work_mode
        __swan01_config__["reg_name"] = swan01_config["reg_name"] if len(work_mode_q) == 0 \
            else f'{work_mode_name_q[work_mode]}_{swan01_config["reg_name"]}'
        __swan01_config__["roi_name"] = swan01_config["roi_name"] if len(work_mode_q) == 0 \
            else f'{work_mode_name_q[work_mode]}_{swan01_config["roi_name"]}'
        # ////////////////////////////////////////////////////////////////////////////
        # 打印读出帧率信息
        # ////////////////////////////////////////////////////////////////////////////
        if operate & 0b001:
            DataflowConfig = Swan01PubMethod.SwanDataflowConfigCal(__swan01_config__, dataflow_related_config)
            print(f"{__swan01_config__["reg_name"]} one slot read time: {DataflowConfig['hist_rd_out_time'] / 100} us")
        # ////////////////////////////////////////////////////////////////////////////
        # 保存 Script 脚本信息
        # ////////////////////////////////////////////////////////////////////////////
        if operate & 0b010:
            Swan01PubMethod.GenerateSwanRegConfig(swan01_config=__swan01_config__,
                                                  reg_cfg_fp=__swan01_config__["Swan01RegConfigFile"])
            # Swan01PubMethod.GenerateSwanRegConfigByJson(swan01_config=__swan01_config__, reg_cfg=__reg_cfg__)
            url = f'{__swan01_config__["fd_path"]}/{__swan01_config__["reg_name"]}.txt'
            _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
            info = f"Script data has been save to {_hyper_link}"
            print(info)
        # ////////////////////////////////////////////////////////////////////////////
        # 保存 ROI 信息
        # ////////////////////////////////////////////////////////////////////////////
        if operate & 0b100:
            DataflowConfig = Swan01PubMethod.SwanDataflowConfigCal(__swan01_config__, dataflow_related_config)
            cur_hist_rd_out_time = DataflowConfig['hist_rd_out_time']  # unit: 0.01us
            __swan01_config__["cur_hist_rd_out_time"] = cur_hist_rd_out_time
            ROISramGenerate(__swan01_config__)
            pass


def ScriptParse(swan01_config, file):
    Swan01PubMethod.ParseSwanRegConfig(file, swan01_config["protocol"])


def ROISramConfigOperation(swan01_config: dict):
    __swan01_config__ = copy.deepcopy(swan01_config)
    # ////////////////////////////////////////////////////////////////////////////
    # ROI generate by GUI
    # ////////////////////////////////////////////////////////////////////////////
    # --------------------------------------------------------
    # 通过 GUI 界面配置生成 ROI
    # --------------------------------------------------------
    if __swan01_config__["roi_generate_by"] == 0:
        ScriptUICoinfigOperate(__swan01_config__, operate=0b100)
    # --------------------------------------------------------
    # 通过选择的寄存器脚本生成 ROI
    # --------------------------------------------------------
    else:
        script_file = __swan01_config__["roi_generate_script_file"]
        protocol = __swan01_config__["protocol"]
        if not os.path.exists(script_file):
            raise ValueError("The reference config file does not exist!")
        csru_cfg = Swan01PubMethod.GetCsruConfig(script_file, protocol)
        __swan01_config__["ANGLE_GRP_SW_NUM"] = csru_cfg["ANGLE_GRP_SW_NUM"]
        __swan01_config__["TRG_I_EN"] = csru_cfg["TRG_I_EN"]
        __swan01_config__["ULR_EN"] = csru_cfg["ULR_EN"]
        __swan01_config__["LSPRD_HOP_EN"] = csru_cfg["LSPRD_HOP_EN"]
        __swan01_config__["LSPRD_HOP_CNTS"] = csru_cfg["LSPRD_HOP_CNTS"]
        __swan01_config__["LSPRD_HOP_STEP"] = csru_cfg["LSPRD_HOP_STEP"]
        __swan01_config__["cur_hist_rd_out_time"] = csru_cfg["HIST_RD_OUT_TIME"]  # unit: 0.01us
        ROISramGenerate(__swan01_config__)
        pass
    return


def ROISramGenerate(swan01_config: dict):
    angle_grp_sw_num = swan01_config["ANGLE_GRP_SW_NUM"] + 1
    TRG_I_EN = swan01_config["TRG_I_EN"]
    excel_file = swan01_config["roi_generate_excel_file"]

    cur_hist_rd_out_time = swan01_config["cur_hist_rd_out_time"]
    manual_setup_slot_time = swan01_config["roi_generate_slot_time_set"] * 100

    # ///////////////////////////////////////////////////////////////
    # slot_time 计算
    # ///////////////////////////////////////////////////////////////
    if swan01_config["roi_generate_slot_time_set_enable"]:  # 手动设置的 slot_time
        slot_time = manual_setup_slot_time
        # 校验手动设置的 slot_time 是否合理, 理论上不能小于读出时间
        if manual_setup_slot_time < cur_hist_rd_out_time:
            logging.warning(f"User defined slot_time need greater than hist read time {cur_hist_rd_out_time / 100} us.")
            return
    else:   # 根据配置自动计算的 slot_time
        slot_time = cur_hist_rd_out_time

    # ///////////////////////////////////////////////////////////////
    # SLOT_IDLETIME 计算
    # ///////////////////////////////////////////////////////////////
    roi_config = Swan01ROISramOperation.read_roi_from_excel(excel_file, sheet_sel=swan01_config["roi_generate_excel_sheet"])
    for grp_index in range(angle_grp_sw_num):
        if TRG_I_EN == 0:
            expo_time = Swan01ROISramOperation.expo_time_cal(swan01_config, roi_config, grp_index)
        else:
            expo_time = roi_config["EXPO_TIME"][grp_index] * 100   # transfer to 0.01us
        # print(slot_time, expo_time)
        roi_config["SLOT_IDLETIME"][grp_index][0] = slot_time - expo_time  # TODO：不能简单的坐减法, 参考 ST 验证平台
    # ///////////////////////////////////////////////////////////////
    # 生成 ROI 数据 并保存
    # ///////////////////////////////////////////////////////////////
    roi_data = Swan01ROISramOperation.roi_sram_generate(roi_config, angle_grp_sw_num)
    roi_data_list = []
    if angle_grp_sw_num > 4:
        roi_data_list.append(roi_data[:674*4])
        roi_data_list.append(roi_data[674*4:])
    else:
        roi_data_list.append(roi_data)

    for sram_index in range(len(roi_data_list)):
        roi_name = f"{swan01_config["roi_name"]}_{sram_index}"
        AdapsChip.Common.common.roi_data_save(f_name=roi_name,
                                              data=roi_data_list[sram_index],
                                              fd_path=swan01_config["roi_fd_path"],
                                              roi_data_format=swan01_config["roi_data_format"])
        url = f'{swan01_config["roi_fd_path"]}/{roi_name}.txt'
        _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
        info = f"ROI data has been save to {_hyper_link}"
        print(info)

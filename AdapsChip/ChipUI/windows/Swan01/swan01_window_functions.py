import copy
import logging
import math
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
    __swan01_config__["ULR_EN"] = 0b11 if swan01_config["ULR_EN"] == 1 else 0b00
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
    if operate & 0b001 and dataflow_related_config is not None:
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
            s = f"MIPI_INFO: WC={DataflowConfig['WC']}; FLNR={DataflowConfig['FLNR']}"
            if not __swan01_config__["ONE_DT_MODE"]:
                s += f"; SLOT_INFO(DT=0x30): {DataflowConfig['txu_info_wc']}byte; "
            print(s)
            print(f"{__swan01_config__["reg_name"]} one slot read time: {DataflowConfig['HIST_RD_OUT_TIME'] / 10} us")
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
            __swan01_config__["SYS_CLK"] = dataflow_related_config["SYS_CLK"]
            __swan01_config__["HIST_RD_OUT_TIME"] = DataflowConfig['HIST_RD_OUT_TIME']
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
        sync_config = ["SYS_CLK", "WORK_MODE", "ANGLE_GRP_SW_NUM", "TRG_I_EN", "DRV_CHSWTME", "ULR_EN", "SEG_NUM", "HIST_MAXBIN_THRS", "HIST_MINBIN_THRS",
                       "LSPRD_HOP_EN", "LSPRD_HOP_CNTS", "LSPRD_HOP_STEP", "HIST_RD_OUT_TIME"]
        for key in sync_config:
            __swan01_config__[key] = csru_cfg[key]
        ROISramGenerate(__swan01_config__)
        pass
    return


def ROISramGenerate(swan01_config: dict):
    angle_grp_sw_num = swan01_config["ANGLE_GRP_SW_NUM"] + 1
    TRG_I_EN = swan01_config["TRG_I_EN"]
    excel_file = swan01_config["roi_generate_excel_file"]

    HIST_RD_OUT_TIME = swan01_config["HIST_RD_OUT_TIME"]
    manual_setup_slot_time = swan01_config["roi_generate_slot_time_set"] * 10

    # ///////////////////////////////////////////////////////////////
    # slot_time 计算
    # ///////////////////////////////////////////////////////////////
    if swan01_config["roi_generate_slot_time_set_enable"]:  # 手动设置的 slot_time
        slot_time = manual_setup_slot_time
        # 校验手动设置的 slot_time 是否合理, 理论上不能小于读出时间
        if manual_setup_slot_time < HIST_RD_OUT_TIME:
            logging.warning(f"User defined slot_time need greater than hist read time {HIST_RD_OUT_TIME / 10} us.")
            return
    else:   # 根据配置自动计算的 slot_time
        slot_time = HIST_RD_OUT_TIME

    # ///////////////////////////////////////////////////////////////
    # SLOT_IDLETIME 计算
    # ///////////////////////////////////////////////////////////////
    # --------------------------------------------------------
    # 获取 ROI config 并进行校验
    # --------------------------------------------------------
    roi_config = Swan01ROISramOperation.read_roi_from_excel(excel_file, sheet_sel=swan01_config["roi_generate_excel_sheet"])

    # 对 SEG_COOR 坐标进行校验
    max_seg_coor = 89 if swan01_config["ChipID"] == "Swan01" else 71
    shift_coor = 0 if swan01_config["ChipID"] == "Swan01" else 9
    for i in range(angle_grp_sw_num):
        for j in range(16):
            if roi_config['SEG_COOR_CFG'][i][j] > max_seg_coor:
                raise ValueError(f'Group[{i+1}] SEG_COOR[{j}] = {roi_config['SEG_COOR_CFG'][i][j]}, '
                                 f'this config exceeds the SPAD boundary[0, {max_seg_coor}].')
            roi_config['SEG_COOR_CFG'][i][j] += shift_coor
    # 对 H_18SPAD_EN 进行校验
    max_spad_en = 18 if swan01_config["ChipID"] == "Swan01" else 15
    spad_str = "H_18SPAD_EN" if swan01_config["ChipID"] == "Swan01" else "H_15SPAD_EN"
    for i in range(angle_grp_sw_num):
        if roi_config['H_18SPAD_EN'][i][0] > max_spad_en:
            raise ValueError(f'Group[{i+1}] {spad_str} = {roi_config['H_18SPAD_EN'][i][0]}, '
                             f'this config exceeds the maximum value of {max_spad_en}.')

    # --------------------------------------------------------
    # Generate
    # --------------------------------------------------------
    T_tdcclk = 4.00
    T_syscclk = 1000 / swan01_config["SYS_CLK"]
    masking_time = 4 + (swan01_config["SEG_NUM"] * 6) + (16 - swan01_config["SEG_NUM"]) - 2  # unit: cyc
    drv_chsw_time = swan01_config["DRV_CHSWTME"]
    transfer_time = (swan01_config["HIST_MAXBIN_THRS"] - swan01_config["HIST_MINBIN_THRS"] + 1) * 2 + 6 + 7  # unit: cyc
    dsp_cfg_rd_time = 14 + (263 - 106 + 1)  # cyc
    read_out_hist_time = (max([transfer_time * T_tdcclk + 40, dsp_cfg_rd_time*T_syscclk+20])) / 100  # unit: 0.1us
    for grp_index in range(angle_grp_sw_num):
        if TRG_I_EN == 0:
            expo_time_cyc = Swan01ROISramOperation.expo_time_cal(swan01_config, roi_config, grp_index)
            expo_time = expo_time_cyc * T_tdcclk / 100  # 0.1us
            print(f"Group_{grp_index} expo_time: {expo_time/10:.3f} us")
        else:
            expo_time = roi_config["EXPO_TIME"][grp_index] * 10   # transfer to 0.1us
        # print(slot_time, expo_time)
        if swan01_config["WORK_MODE"] == 3:  # About master_mode and work_mode is PCM, if expo time long enough, it can be set 0 to improve FPS
            roi_config["SLOT_IDLETIME"][grp_index][0] = 0
        else:
            slot_expo_time = masking_time*T_syscclk/100 + expo_time + drv_chsw_time  # unit: 0.1us
            slot_idle_time = max([slot_time - slot_expo_time, read_out_hist_time])
            slot_idle_time = math.ceil(slot_idle_time)
            if slot_idle_time > 0xFFFF:
                raise ValueError(f"Slot_ideletime[15:0] is out of bounds, it's need to be set{slot_idle_time}.")
            roi_config["SLOT_IDLETIME"][grp_index][0] = slot_idle_time
            print(f"Group_{grp_index} actual SLOT_TIME: {(slot_expo_time+slot_idle_time)/10:.3f} us")
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
        AdapsChip.Common.common.swan01_roi_data_save(f_name=roi_name,
                                                     data=roi_data_list[sram_index],
                                                     fd_path=swan01_config["roi_fd_path"],
                                                     roi_data_format=swan01_config["roi_data_format"],
                                                     roi_info_file=swan01_config["roi_generate_info_file"],
                                                     start_index=sram_index*4)
        url = f'{swan01_config["roi_fd_path"]}/{roi_name}.txt'
        _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
        info = f"ROI data has been save to {_hyper_link}"
        print(info)

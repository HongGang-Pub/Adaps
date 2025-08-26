import logging
import math

from SelfDefinedPackge import PubMethod, LogerPubMethod
from AdapsChip.Common.common import *
from AdapsChip.Swan01.Swan01RegAddr import *
import re
import os


def GetMipiFile(fd_path):
    """
    针对 Dothinker 获取MIPI文件，并按index生成字典，使能顺序读取文件进行数据比对

    Args:
        fd_path: MIPI Data folder dir
    Returns:
        dict: f_dict[key=index, value=mipidata_path]
    """

    file_list = PubMethod.get_fp(fd_path=fd_path, mode=1, match_filter=".txt", f_type="Get MIPI File")
    if len(file_list) == 0:
        raise ValueError("未从指定目录下获取到MIPI文件！！！")

    file_dict = {}
    file_index_list = []
    for index in range(len(file_list)):
        sublist_file = file_list[index].split("-")
        # 针对度信抓包MIPI文件命名格式：mipidata-index-xxxxxxxxx.txt，字典格式为：{index: mipidata_path}
        if len(sublist_file) >= 3:
            file_index = int(file_list[index].split("-")[-2])
            file_dict[file_index] = file_list[index]
            file_index_list.append(file_index)
        else:
            continue

    return file_dict


def GetCsruConfig(config_file, protocol=0) -> dict:
    """
    根据 Swan01 寄存器配置脚本，获取寄存器配置信息

    Args:
        config_file (str): 脚本路径
        protocol (int): 0: i2c, 1: spi

    Returns:
        dict: 寄存相关配置
    """

    min_lens = 4 if protocol == 0 else 3
    addr_index = 2 if protocol == 0 else 1
    csru_cfg = {
        # SYSC
        "SYS_CLK": 0,
        "MST_MODE": 0,
        "WORK_MODE": 0,
        "SEG_NUM": 0,
        "HIST_RD_OUT_TIME": 0,
        "PXL_BINN_SEL": 0,
        "SYNC_POL": 0,
        # TRGU
        "TRG_I_EN": 0,
        "DRV_CHSWTME": 0,
        "ULR_EN": 0,
        "LSPRD_HOP_EN": 0,
        "LSPRD_HOP_CNTS": 0,
        "LSPRD_HOP_STEP": 0,
        # HIST
        "HIST_MINBIN_THRS": 0,
        "HIST_MAXBIN_THRS": 255,
        "NS_MINBIN_THRS": 0,
        "NS_MAXBIN_THRS": 255,
        "SPOT_MON_MINBIN_THRS": 0,
        "HIST_BINFULL_THRS": 0x3F0,
        "INTF_DET_EN": 0,
        "INTF_HIST_MODE": 0,
        "BIN_WIDTH_MODE": 0,
        "BIN_WIDTH_SEL": 0,
        # SHOT
        "ANGLE_GRP_SW_NUM": 5,
        "FRM_SLOT_NUM": 0x4AF,
        # "ANGLE_GRP0_SLOT_NUM": 0,
        # "ANGLE_GRP1_SLOT_NUM": 0,
        # "ANGLE_GRP2_SLOT_NUM": 0,
        # "ANGLE_GRP3_SLOT_NUM": 0,
        # "ANGLE_GRP4_SLOT_NUM": 0,
        # "ANGLE_GRP5_SLOT_NUM": 0,
        # "ANGLE_GRP6_SLOT_NUM": 0,
        # "ANGLE_GRP7_SLOT_NUM": 0,
        "FLEX_SHOT_EN": 0,
        # PACK
        "DATA_WIDTH_SEL": 0,
        "PACK_2PXL_EN": 0,
        "PACK_4PXL_EN": 0,
        "PACK_8PXL_EN": 0,
        "PACK_16PXL_EN": 0,
        "PACK_16PXL_NUM": 0,
        # TXU
        "TX_FRM_MODE": 0,
        "ONE_DT_MODE": 0,
        "PKT_CHKSUM_EN": 0,
        "MIPI_PKT_PL_NUM": 0,
        # DLY
        "FRM_IDLETIME": 0,
        "MIPI_FEND_DLY": 0,
        "MIPI_PKTDLY1_CYC": 0,
        "MIPI_PKTDLY2_CYC": 0,
        "MIPI_PKTDLY3_CYC": 0,
        "MIPI_FSDLY_CYC": 0,
        # DSP
        "OUT_NUMBIN_MODE": 0,
        "OUT_TOTALBIN_NUM": 0,
        "OUT_ECHO_NUM": 0,
        "OUT_ECHOBIN_NUM": 0,
        "OUT_INTF_HIST_SEL": 0,
        "OUT_FIR_RAW_SEL": 0,
        "OUT_OVFL_FLAT_EN": 0,
        "OUT_ECHOBIN_MODE": 0,
        "ECHO_ORDER_NEAR_NUM": 0,
        "FWHM_HALF_COEF": 0,
        "FWHM_SEARCH_NUM": 0,
        # CLK
        "SYSCLK1M_DIV": 399,
        "SYSCLK10M_DIV": 39,
        "XCLK1M_DIV": 0,
        # ROI
        "roi_file": "None",
        # MIPI
        "MIPI": {
            "PKT_TYPE": 0,
            "VC0_FLNR": 0,
            "VC0_WC": 0,
            "VC0_THRESHOLD": 0xC0,
            "NS": 84,
            "MS": 2,
            "PS": 1,
            "DataTxThslpxcnt": 2,
            "DataTxThsexitCnt": 2,
            "DataTxThsprepareCnt": 0,
            "DataTxThszeroCnt": 50,
            "DataTxThstrailCnt": 17,
        }
    }
    regs_write = "I2C_Write" if protocol == 0 else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == 0 else "SPI_Block_Write"

    csru_datas = PubMethod.read_file(fname=config_file)

    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check。")

    for line in range(len(csru_datas)):
        _str = csru_datas[line].strip().replace("\n", "").replace("\r", "")  # 去除换行符, 保存时统一保存

        if _str == '' or _str[0:2] == '//':  # 空行 & 整行注释 场景
            continue
        configs = re.split(",|//", _str)
        for i in range(len(configs)):
            configs[i] = configs[i].strip()

        # register_write
        if configs[0] == regs_write:
            if len(configs) < min_lens:
                raise ValueError(f"Script format error: line{line + 1}: {_str}")
            addr = int(configs[addr_index], 16)
            config_str = configs[addr_index + 1][0:2]
            register_value = int(config_str, 16)

            # SYSC
            if addr == reg_addr['SYS_CTRL']:
                csru_cfg["TX_FRM_MODE"] = (register_value & 0x80) >> 7
                csru_cfg["TRG_I_EN"] = (register_value & 0x40) >> 5
                csru_cfg["WORK_MODE"] = (register_value & 0x06) >> 1
                csru_cfg["MST_MODE"] = (register_value & 0x01) >> 0
            elif addr == reg_addr['UNIQ_FUNC_CFG']:
                csru_cfg["ULR_EN"] = (register_value & 0x03) >> 0
            elif addr == reg_addr['DRV_CHSWTME']:
                csru_cfg["DRV_CHSWTME"] = register_value
            elif addr == reg_addr['LSPRD_HOP_CFG1']:
                csru_cfg["LSPRD_HOP_EN"] = (register_value & 0x80) >> 7
                csru_cfg["LSPRD_HOP_STEP"] = (register_value & 0x3F) >> 0
            elif addr == reg_addr['LSPRD_HOP_CFG2']:
                csru_cfg["LSPRD_HOP_CNTS"] = (register_value & 0xFF) >> 0
            elif addr == reg_addr['PXL_BINN_CFG']:
                csru_cfg["PXL_BINN_SEL"] = register_value & 0x03
            elif addr == reg_addr['SYNC_POL']:
                csru_cfg["SYNC_POL"] = register_value & 0x01
            elif addr == reg_addr['SEG_NUM']:
                csru_cfg["SEG_NUM"] = register_value & 0xFF
            elif addr == reg_addr['HIST_RD_OUT_TIME_L']:
                csru_cfg["HIST_RD_OUT_TIME"] = (csru_cfg["HIST_RD_OUT_TIME"] & (0xFFFF - 0x00FF)) + (register_value << 0)
            elif addr == reg_addr['HIST_RD_OUT_TIME_H']:
                csru_cfg["HIST_RD_OUT_TIME"] = (csru_cfg["HIST_RD_OUT_TIME"] & (0xFFFF - 0xFF00)) + (register_value << 8)
            # HIST
            elif addr == reg_addr['HIST_MINBIN_THRS']:
                csru_cfg["HIST_MINBIN_THRS"] = register_value
            elif addr == reg_addr['HIST_MAXBIN_THRS']:
                csru_cfg["HIST_MAXBIN_THRS"] = register_value
            elif addr == reg_addr['HIST_NS_MINBIN_THRS']:
                csru_cfg["NS_MINBIN_THRS"] = register_value
            elif addr == reg_addr['HIST_NS_MAXBIN_THRS']:
                csru_cfg["NS_MAXBIN_THRS"] = register_value
            elif addr == reg_addr['SPOT_MON_MINBIN_THRS']:
                csru_cfg["SPOT_MON_MINBIN_THRS"] = register_value
            elif addr == reg_addr['HIST_BINFULL_THRS_L']:
                csru_cfg["HIST_BINFULL_THRS"] = (csru_cfg["HIST_BINFULL_THRS"] & (0x03FF - 0x00FF)) + register_value
            elif addr == reg_addr['HIST_BINFULL_THRS_H']:
                csru_cfg["HIST_BINFULL_THRS"] = (csru_cfg["HIST_BINFULL_THRS"] & (0x03FF - 0x0300)) + (register_value << 8)
            elif addr == reg_addr['HIST_MISC_CFG']:
                csru_cfg["INTF_HIST_MODE"] = (register_value & 0x20) >> 5
                csru_cfg["INTF_DET_EN"] = (register_value & 0x10) >> 4
                csru_cfg["FLEX_SHOT_EN"] = (register_value & 0x04) >> 3
                csru_cfg["BIN_WIDTH_MODE"] = (register_value & 0x02) >> 1
                csru_cfg["BIN_WIDTH_SEL"] = (register_value & 0x01) >> 0
            # SHOT
            elif addr == reg_addr['ANGLE_GRP_CFG']:
                csru_cfg["ANGLE_GRP_SW_NUM"] = (register_value & 0x07)
            elif addr == reg_addr['FRM_SLOT_NUM_L']:
                csru_cfg["FRM_SLOT_NUM"] = (csru_cfg["FRM_SLOT_NUM"] & (0xFFFF - 0x00FF)) + (register_value << 0)
            elif addr == reg_addr['FRM_SLOT_NUM_H']:
                csru_cfg["FRM_SLOT_NUM"] = (csru_cfg["FRM_SLOT_NUM"] & (0xFFFF - 0xFF00)) + (register_value << 8)
            # elif addr == reg_addr['ANGLE_GRP0_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP0_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP1_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP1_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP2_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP2_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP3_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP3_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP4_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP4_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP5_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP5_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP6_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP6_SLOT_NUM"] = register_value
            # elif addr == reg_addr['ANGLE_GRP7_SLOT_NUM']:
            #     csru_cfg["ANGLE_GRP7_SLOT_NUM"] = register_value
            # TXU
            elif addr == reg_addr['TXU_CFG']:
                csru_cfg["PKT_CHKSUM_EN"] = (register_value & 0x10) >> 4
                csru_cfg["ONE_DT_MODE"] = (register_value & 0x08) >> 3
                csru_cfg["DATA_WIDTH_SEL"] = (register_value & 0x01) >> 0
            elif addr == reg_addr['MIPI_PKT_PLNUM_L']:
                csru_cfg["MIPI_PKT_PL_NUM"] = (csru_cfg["MIPI_PKT_PL_NUM"] & (0xFFFF - 0x00FF)) + (register_value << 0)
            elif addr == reg_addr['MIPI_PKT_PLNUM_H']:
                csru_cfg["MIPI_PKT_PL_NUM"] = (csru_cfg["MIPI_PKT_PL_NUM"] & (0xFFFF - 0xFF00)) + (register_value << 8)
            # PACK
            elif addr == reg_addr['MIPI_PACK_CTRL']:
                csru_cfg["PACK_2PXL_EN"] = (register_value & 0x01) >> 0
                csru_cfg["PACK_4PXL_EN"] = (register_value & 0x02) >> 1
                csru_cfg["PACK_8PXL_EN"] = (register_value & 0x04) >> 2
                csru_cfg["PACK_16PXL_EN"] = (register_value & 0x08) >> 3
                csru_cfg["PACK_16PXL_NUM"] = (register_value & 0x30) >> 4
            # TXDLY
            elif addr == reg_addr["FRM_IDLETIME"]:
                csru_cfg["FRM_IDLETIME"] = register_value
            elif addr == reg_addr['MIPI_FEND_DLY']:
                csru_cfg["MIPI_FEND_DLY"] = register_value
            elif addr == reg_addr['MIPI_TXDLY1']:
                csru_cfg["MIPI_PKTDLY1_CYC"] = (csru_cfg["MIPI_PKTDLY1_CYC"] & (0xFFFF - 0x00FF)) + (
                        register_value << 0)
            elif addr == reg_addr['MIPI_TXDLY2']:
                csru_cfg["MIPI_PKTDLY1_CYC"] = (csru_cfg["MIPI_PKTDLY1_CYC"] & (0xFFFF - 0xFF00)) + (
                        register_value << 8)
            elif addr == reg_addr['MIPI_TXDLY3']:
                csru_cfg["MIPI_PKTDLY2_CYC"] = (csru_cfg["MIPI_PKTDLY2_CYC"] & (0xFFFF - 0x00FF)) + (
                        register_value << 0)
            elif addr == reg_addr['MIPI_TXDLY4']:
                csru_cfg["MIPI_PKTDLY2_CYC"] = (csru_cfg["MIPI_PKTDLY2_CYC"] & (0xFFFF - 0xFF00)) + (
                        register_value << 8)
            elif addr == reg_addr['MIPI_TXDLY5']:
                csru_cfg["MIPI_PKTDLY3_CYC"] = (csru_cfg["MIPI_PKTDLY3_CYC"] & (0xFFFF - 0x00FF)) + (
                        register_value << 0)
            elif addr == reg_addr['MIPI_TXDLY6']:
                csru_cfg["MIPI_PKTDLY3_CYC"] = (csru_cfg["MIPI_PKTDLY3_CYC"] & (0xFFFF - 0xFF00)) + (
                        register_value << 8)
            elif addr == reg_addr['MIPI_TXDLY7']:
                csru_cfg["MIPI_FSDLY_CYC"] = (csru_cfg["MIPI_FSDLY_CYC"] & (0xFFFF - 0x00FF)) + (register_value << 0)
            elif addr == reg_addr['MIPI_TXDLY8']:
                csru_cfg["MIPI_FSDLY_CYC"] = (csru_cfg["MIPI_FSDLY_CYC"] & (0xFFFF - 0xFF00)) + (
                        (register_value & 0x03) << 8)
            # CLK_DIV
            elif addr == reg_addr['SYSCLK1M_DIVH']:
                csru_cfg["SYSCLK1M_DIV"] = (csru_cfg["SYSCLK1M_DIV"] & (0xFFFF - 0xFF00)) + (
                        (register_value & 0x01) << 8)
                csru_cfg["XCLK1M_DIV"] = (register_value & 0xFC) >> 2
                csru_cfg["SYS_CLK"] = csru_cfg["SYSCLK1M_DIV"] + 1
            elif addr == reg_addr['SYSCLK1M_DIVL']:
                csru_cfg["SYSCLK1M_DIV"] = (csru_cfg["SYSCLK1M_DIV"] & (0xFFFF - 0x00FF)) + (register_value << 0)
                csru_cfg["SYS_CLK"] = csru_cfg["SYSCLK1M_DIV"] + 1
            elif addr == reg_addr['SYSCLK10M_DIV']:
                csru_cfg["SYSCLK10M_DIV"] = register_value
            # DSP
            elif addr == reg_addr['DSP_CFG1']:
                csru_cfg["OUT_TOTALBIN_NUM"] = register_value
            elif addr == reg_addr["DSP_CFG2"]:
                csru_cfg["OUT_ECHOBIN_NUM"] = register_value & 0x7F
            elif addr == reg_addr["DSP_CFG3"]:
                csru_cfg["OUT_OVFL_FLAT_EN"] = (register_value & 0x80) >> 7
                csru_cfg["OUT_ECHOBIN_NUM"] = (register_value & 0x40) >> 6
                csru_cfg["OUT_NUMBIN_MODE"] = (register_value & 0x20) >> 5
                csru_cfg["OUT_FIR_RAW_SEL"] = (register_value & 0x10) >> 4
                csru_cfg["OUT_ECHO_NUM"] = (register_value & 0x0E) >> 1
                csru_cfg["OUT_INTF_HIST_SEL"] = (register_value & 0x01) >> 0
            elif addr == reg_addr["DSP_CFG4"]:
                csru_cfg["ECHO_ORDER_NEAR_NUM"] = (register_value & 0x0F) >> 0
            elif addr == reg_addr["DSP_RGM_CFG1"]:
                csru_cfg["FWHM_HALF_COEF"] = (register_value & 0x0F) >> 0
            elif addr == reg_addr["DSP_RGM_CFG3"]:
                csru_cfg["FWHM_SEARCH_NUM"] = (register_value & 0x0F) >> 0
            # MIPI
            elif addr == reg_addr['MIPIPLL_LPDH']:
                csru_cfg["MIPI"]["NS"] = (csru_cfg["MIPI"]["NS"] & (0xFFFF - 0xFF00)) + ((register_value & 0x01) << 8)
            elif addr == reg_addr['MIPIPLL_LPDL']:
                csru_cfg["MIPI"]["NS"] = (csru_cfg["MIPI"]["NS"] & (0xFFFF - 0x00FF)) + (register_value << 0)
            elif addr == reg_addr['MIPIPLL_PPD']:
                csru_cfg["MIPI"]["MS"] = (register_value & 0xE0) >> 5
                csru_cfg["MIPI"]["PS"] = register_value & 0x1F
            elif addr == reg_addr['VC0_FLNR_L']:
                csru_cfg["MIPI"]["VC0_FLNR"] = (csru_cfg["MIPI"]["VC0_FLNR"] & (0xFFFF - 0x00FF)) + (
                        register_value << 0)
            elif addr == reg_addr['VC0_FLNR_H']:
                csru_cfg["MIPI"]["VC0_FLNR"] = (csru_cfg["MIPI"]["VC0_FLNR"] & (0xFFFF - 0xFF00)) + (
                        register_value << 8)
            elif addr == reg_addr['VC0_WC_L']:
                csru_cfg["MIPI"]["VC0_WC"] = (csru_cfg["MIPI"]["VC0_WC"] & (0xFFFF - 0x00FF)) + (register_value << 0)
            elif addr == reg_addr['VC0_WC_H']:
                csru_cfg["MIPI"]["VC0_WC"] = (csru_cfg["MIPI"]["VC0_WC"] & (0xFFFF - 0xFF00)) + (register_value << 8)
            elif addr == reg_addr["VC0_THRESHOLD"]:
                csru_cfg["MIPI"]["VC0_THRESHOLD"] = register_value
            elif addr == reg_addr["PKT_TYPE"]:
                csru_cfg["MIPI"]["PKT_TYPE"] = register_value & 0x3F
            elif addr == reg_addr["THS_EXIT"]:
                csru_cfg["MIPI"]["DataTxThsexitCnt"] = register_value
            elif addr == reg_addr["THS_PREPARE"]:
                csru_cfg["MIPI"]["DataTxThsprepareCnt"] = register_value
            elif addr == reg_addr["THS_ZERO"]:
                csru_cfg["MIPI"]["DataTxThszeroCnt"] = register_value
            elif addr == reg_addr["THS_TRAIL"]:
                csru_cfg["MIPI"]["DataTxThstrailCnt"] = register_value
        elif configs[0] == roisram_write:
            if len(configs) < 5:
                raise ValueError(f"Script format error: line{line + 1}: {_str}")
            roi_name = configs[4]
            csru_cfg["roi_file"] = roi_name
        else:
            continue
            # raise ValueError(f"The script file format is incorrect: line {line+1}: {_str}")
    return csru_cfg


def CalPkgNum(swan01_config):
    """
    非多帧合一时，一次rolling包的数量
    Args:
        swan01_config (dict): 寄存配置信息

    Returns:
        int: 非多帧合一时，一次rolling包的数量
    """

    work_mode = swan01_config["WORK_MODE"]
    h_vld_seg = swan01_config["H_VLD_SEG"]
    v_pxl_out_num = 6 if swan01_config["V_PXL_OUT_NUM"] == 1 else 1

    if work_mode == 2 or work_mode == 3:
        pkg_num = (h_vld_seg + 1) * v_pxl_out_num * 4 + 2
    else:
        pkg_num = (h_vld_seg + 1) * 16 + 2
    return pkg_num


# def CalMipiFlnrAndWC(csru_cfg):
#     work_mode = csru_cfg["WORK_MODE"]
#     tx_frm_mode = csru_cfg["TX_FRM_MODE"]
#     hist_minbin_thrs = csru_cfg["HIST_MINBIN_THRS"]
#     hist_maxbin_thrs = csru_cfg["HIST_MAXBIN_THRS"]
#     data_width_sel = csru_cfg["DATA_WIDTH_SEL"]
#     frm_slot_num = csru_cfg["FRM_SLOT_NUM"]
#     pack_16pxl_num = csru_cfg["PACK_16PXL_NUM"]
#     pack_16pxl_en = csru_cfg["PACK_16PXL_EN"]
#     pack_8pxl_en = csru_cfg["PACK_8PXL_EN"]
#     pack_4pxl_en = csru_cfg["PACK_4PXL_EN"]
#     pack_2pxl_en = csru_cfg["PACK_2PXL_EN"]
#     pxl_binn_sel = csru_cfg["PXL_BINN_SEL"]
#     bin_widht_sel = csru_cfg["BIN_WIDTH_SEL"]
#     out_totalbin_num = csru_cfg["OUT_TOTALBIN_NUM"]
#     out_echobin_num = csru_cfg["OUT_ECHOBIN_NUM"]
#     out_numbin_mode = csru_cfg["OUT_NUMBIN_MODE"]
#     out_echo_num = csru_cfg["OUT_ECHO_NUM"]
#     one_dt_mode = csru_cfg["ONE_DT_MODE"]
#     pkt_chksum_en = csru_cfg["PKT_CHKSUM_EN"]
#     seg_num = csru_cfg["SEG_NUM"]  # TODO: 需要确认, 有可能需要特殊处理, 寄存器无此配置
#
#     # //////////////////////////////////////////////////////////
#     # 处理寄存器配置特殊情况
#     # //////////////////////////////////////////////////////////
#     out_echo_num = 5 if out_echo_num > 5 else out_echo_num  # 最大输出 6 echo (配置值+1)
#     pxl_binn_sel = 0 if pxl_binn_sel > 2 else pxl_binn_sel  # 当 pxl_binn_sel == 2 时, 一个 segment 为 16pxl
#
#     # //////////////////////////////////////////////////////////
#     # Pixel Pack 相关计算
#     # //////////////////////////////////////////////////////////
#     # 计算一个 Packet 包含多少 Pixel
#     # 1. work_mode == PCM: 一次读出全部的 Pixel 数据
#     # 2. work_mode != PCM: 仅与 pack 配置相关
#     one_pkt_pxl_num = 48 * seg_num if work_mode == 3 else \
#         1 if pack_2pxl_en == 0 else \
#             2 if pack_4pxl_en == 0 else \
#                 4 if pack_8pxl_en == 0 else \
#                     8 if pack_16pxl_en == 0 else \
#                         16 * (pack_16pxl_num + 1)
#
#     # //////////////////////////////////////////////////////////
#     # 针对 binning 相关的数据进行计算 和 校验
#     # //////////////////////////////////////////////////////////
#     # 计算一个 slot, pixel binning 后, 有多少个 Pixel 需要读出
#     pxl_num_after_binn = 48 * seg_num if work_mode == 3 else \
#         (16 >> pxl_binn_sel) * seg_num
#
#     # //////////////////////////////////////////////////////////
#     # 计算一个 image帧 (MIPI image帧 概念), 包含多少个 slot
#     # //////////////////////////////////////////////////////////
#     slot_num_in_img_frm = 1 if tx_frm_mode == 0 else \
#         1 + frm_slot_num
#
#     # //////////////////////////////////////////////////////////
#     # 换算 WC 与 data_width_sel 因子
#     # //////////////////////////////////////////////////////////
#     # data_width_sel == 0: 8bit, data_width_sel == 1: 10bit
#     wc_factor = 1 if data_width_sel == 0 else \
#         1.25
#
#     # //////////////////////////////////////////////////////////
#     # cycle 计算
#     # //////////////////////////////////////////////////////////
#     # 计算不同 work_mode 下, txu 发送单个 pixel 数据的 cycle 数
#     # SPHR
#     if work_mode == 0:
#         match data_width_sel:
#             case 0:
#                 rd_cyc_dsp_1pxl = (4 + 14 * (out_echo_num + 1)) / 2
#             case 1:
#                 rd_cyc_dsp_1pxl = (4 + 12 * (out_echo_num + 1)) / 2
#             case _:
#                 rd_cyc_dsp_1pxl = (4 + 14 * (out_echo_num + 1)) / 2
#     # PHR
#     elif work_mode == 1:
#         match out_numbin_mode:
#             case 0:
#                 rd_cyc_dsp_1pxl = (4 + out_totalbin_num * 2) / 2
#             case 1:
#                 rd_cyc_dsp_1pxl = (4 + (out_echo_num + 1) * (out_echobin_num * 2)) / 2
#             case _:
#                 rd_cyc_dsp_1pxl = (4 + out_totalbin_num * 2) / 2
#     # FHR
#     elif work_mode == 2:
#         rd_cyc_dsp_1pxl = (((hist_maxbin_thrs - hist_minbin_thrs + 1) * 8) >> bin_widht_sel) / 2
#     # PCM
#     else:
#         rd_cyc_dsp_1pxl = 1
#
#     # crc32 TXU 读取 cycle 计算
#     rd_cyc_crc32 = 2 if pkt_chksum_en == 1 else 0  # CRC32 校验位读取需要 2 cycle
#
#     # txu 发送单个 packet 数据的 cycle 数
#     one_pkt_dsp_rd_cyc = rd_cyc_dsp_1pxl * one_pkt_pxl_num + rd_cyc_crc32
#
#     # //////////////////////////////////////////////////////////
#     # 计算 WC && FLNR
#     # //////////////////////////////////////////////////////////
#     # Q1: Why * 2 ?
#     # A1: TXU is dual pixel mode
#     wc = one_pkt_dsp_rd_cyc * 2 * wc_factor
#     flnr = (pxl_num_after_binn / one_pkt_pxl_num + one_dt_mode) * slot_num_in_img_frm
#
#     return int(wc), int(flnr)

def SwanDataflowRelateConfigGet(swan01_config: dict) -> dict:
    """
    获取 Swan 相关的数据流配置
    Args:
        swan01_config(dict): Swan GUI 相关的配置信息
    Returns:
        dict: Swan 相关的数据流配置
    """
    dataflow_related_config = {
        "SYS_CLK": 400,  # 系统时钟(unit: MHz)
        "MIPI_RATE": 1500,  # MIPI 1.5Gbps
        "MIPI_LANE_NUM": 4,  # MIPI 4 lane
        "MIPI_PKT_INTV": 0.9,  # MIPI 1.5Gbps config (unit: us)
        "MIPI_FIFO_SIZE": 960,  # MIPI FIFO: DEPTH = 1024, WIDTH = 32
    }
    if "USER_DEFINE_CONIFG" in swan01_config and swan01_config["USER_DEFINE_CONIFG"]["USER_DEFINE_CONIFG_ENABLE"]:
        dataflow_related_config = swan01_config["USER_DEFINE_CONIFG"]
    else:
        SYS_CLK = 330 if swan01_config['SYS_CLK'] == 0 else 400
        MIPI_RATE = 800 if swan01_config['MIPI_RATE'] == 0 \
            else 1000 if swan01_config['MIPI_RATE'] == 1 \
            else 1200 if swan01_config['MIPI_RATE'] == 2 \
            else 1500
        MIPI_CFG = MIPI_CONFIG_Cal(SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE, display=False)
        MIPI_PKT_INTV = MipiPKGIntvCal(mipi_cfg=MIPI_CFG, SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)
        dataflow_related_config["SYS_CLK"] = SYS_CLK
        dataflow_related_config["MIPI_RATE"] = MIPI_RATE
        dataflow_related_config["MIPI_PKT_INTV"] = MIPI_PKT_INTV + swan01_config["USER_DEFINE_CONIFG"][
            "MIPI_PKT_INTV_MARGIN"]
    return dataflow_related_config


def SwanDataflowConfigCal(csru_cfg: dict, dataflow_related_config: dict = None, function_sel: str = "") -> dict:
    """
    计算 MIPI dataflow 相关参数
    Args:
        csru_cfg(dict): Swan 相关的寄存器配置信息
        dataflow_related_config(dict): 与数据流相关的配置, 但并非寄存器配置
        function_sel(str): if function_sel=="MIPI", Just cal WC & FLNR

    Returns:
        dict: Swan dataflow 相关的配置值
            SwanDataflowConfig = {
                mipi_pktdly1_cyc : 0,   # DSP DLY: 16 bit (unit: cycle)
                mipi_pktdly2_cyc : 0,   # HIST DLY: 实际值=配置值*16， 16 bit (unit: cycle)
                mipi_pktdly3_cyc : 0,   # HIST DLY: 用于调节 第一次 HIST 和 第二次 HIST 之间的 delay, 16 bit (unit: cycle)
                mipi_fsdly_cyc   : 0,   # FS DLY: 调节 FS 和 generic data 之间的间隔, 10 bit (unit: cycle)
                mipi_fenddly     : 0,   # 8 bit (unit: 10us)
                threshold_value  : 0,   # 8 bit
                WC               : 0,   # 16 bit
                FLNR             : 0,   # 16 bit
                hist_read_out_cyc: 0,   # 非寄存器配置值, 此值对应 数据读出所需要的完整时间
            }
    """
    work_mode = csru_cfg["WORK_MODE"]
    tx_frm_mode = csru_cfg["TX_FRM_MODE"]
    hist_minbin_thrs = csru_cfg["HIST_MINBIN_THRS"]
    hist_maxbin_thrs = csru_cfg["HIST_MAXBIN_THRS"]
    data_width_sel = csru_cfg["DATA_WIDTH_SEL"]
    frm_slot_num = csru_cfg["FRM_SLOT_NUM"]
    pack_16pxl_num = csru_cfg["PACK_16PXL_NUM"]
    pack_16pxl_en = csru_cfg["PACK_16PXL_EN"]
    pack_8pxl_en = csru_cfg["PACK_8PXL_EN"]
    pack_4pxl_en = csru_cfg["PACK_4PXL_EN"]
    pack_2pxl_en = csru_cfg["PACK_2PXL_EN"]
    pxl_binn_sel = csru_cfg["PXL_BINN_SEL"]
    bin_widht_sel = csru_cfg["BIN_WIDTH_SEL"]
    out_totalbin_num = csru_cfg["OUT_TOTALBIN_NUM"]
    out_echobin_num = csru_cfg["OUT_ECHOBIN_NUM"]
    out_numbin_mode = csru_cfg["OUT_NUMBIN_MODE"]
    out_echo_num = csru_cfg["OUT_ECHO_NUM"]
    one_dt_mode = csru_cfg["ONE_DT_MODE"]
    pkt_chksum_en = csru_cfg["PKT_CHKSUM_EN"]
    seg_num = csru_cfg["SEG_NUM"]
    fwhm_search_num = csru_cfg["FWHM_SEARCH_NUM"]

    DataflowConfig = {
        "mipi_pktdly1_cyc": 0,  # DSP DLY: 16 bit (unit: cycle)
        "mipi_pktdly2_cyc": 0,  # HIST DLY: 实际值=配置值*16， 16 bit (unit: cycle)
        "mipi_pktdly3_cyc": 0,  # HIST DLY: 用于调节 第一次 HIST 和 第二次 HIST 之间的 delay, 16 bit (unit: cycle)
        "mipi_fsdly_cyc": 0,  # FS DLY: 调节 FS 和 generic data 之间的间隔, 10 bit (unit: cycle)
        "mipi_fenddly": 0,  # 8 bit (unit: 10us)
        "mipi_pkt_pl_num": 0,  # 16 bit
        "hist_read_out_cyc": 0,  # 非寄存器配置值, 此值对应 数据读出所需要的完整时间
        "threshold_value": 0,  # 8 bit
        "WC": 0,  # 16 bit
        "FLNR": 0,  # 16 bit
        "PKT_TYPE": 0x2A,  # MIPI data type
        "MIPI_PKT_DLY": 0,  # unit: us
        "HIST_RD_OUT_TIME": 0,  # 非寄存器配置值, unit: 0.1us
    }
    # //////////////////////////////////////////////////////////
    # 处理寄存器配置特殊情况
    # //////////////////////////////////////////////////////////
    out_echo_num = 5 if out_echo_num > 5 else out_echo_num  # 最大输出 6 echo (配置值+1)
    pxl_binn_sel = 0 if pxl_binn_sel > 2 else pxl_binn_sel  # 当 pxl_binn_sel == 2 时, 一个 segment 为 16pxl

    # //////////////////////////////////////////////////////////
    # Pixel Pack 相关计算
    # //////////////////////////////////////////////////////////
    # 计算一个 Packet 包含多少 Pixel
    # 1. work_mode == PCM: 一次读出全部的 Pixel 数据
    # 2. work_mode != PCM: 仅与 pack 配置相关
    one_pkt_pxl_num = 48 * seg_num if work_mode == 3 \
        else 1 if pack_2pxl_en == 0 \
        else 2 if pack_4pxl_en == 0 \
        else 4 if pack_8pxl_en == 0 \
        else 8 if pack_16pxl_en == 0 \
        else 16 * (pack_16pxl_num + 1)

    # 计算一个 slot, pixel binning 后, 有多少个 Pixel 需要读出
    pxl_num_after_binn = 48 * seg_num if work_mode == 3 else (16 >> pxl_binn_sel) * seg_num
    # 计算一个 slot, 有多少个 Pixel 包需要发送
    one_slot_pxl_pkt_num = pxl_num_after_binn / one_pkt_pxl_num

    # 计算不同 work_mode 下, txu 发送单个 pixel 数据的 cycle 数
    # SPHR
    if work_mode == 0:
        rd_cyc_dsp_1pxl = (4 + 12 * (out_echo_num + 1)) / 2 if data_width_sel == 1 else \
            (4 + 14 * (out_echo_num + 1)) / 2
    # PHR
    elif work_mode == 1:
        rd_cyc_dsp_1pxl = (4 + (out_echo_num + 1) * (out_echobin_num * 2)) / 2 if out_numbin_mode == 1 else \
            (4 + out_totalbin_num * 2) / 2
    # FHR
    elif work_mode == 2:
        rd_cyc_dsp_1pxl = (((hist_maxbin_thrs - hist_minbin_thrs + 1) * 8) >> bin_widht_sel) / 2
    # PCM
    else:
        rd_cyc_dsp_1pxl = 1
    rd_cyc_dsp_1pxl = int(rd_cyc_dsp_1pxl)

    rd_cyc_crc32 = 2 if pkt_chksum_en == 1 else 0  # CRC32 校验位读取需要 2 cycle

    # DSP 发送单个 packet 数据的 cycle 数
    one_pkt_dsp_rd_cyc = rd_cyc_dsp_1pxl * one_pkt_pxl_num + rd_cyc_crc32

    # //////////////////////////////////////////////////////////
    # 计算 WC & FLNR
    # //////////////////////////////////////////////////////////
    slot_num_in_img_frm = 1 if tx_frm_mode == 0 else 1 + frm_slot_num
    wc_factor = 1 if data_width_sel == 0 else 1.25
    DataflowConfig["PKT_TYPE"] = 0x2A if data_width_sel == 0 else 0x2B

    wc = one_pkt_dsp_rd_cyc * 2 * wc_factor  # Q1: Why * 2 ? A1: TXU is dual pixel mode
    flnr = (pxl_num_after_binn / one_pkt_pxl_num + one_dt_mode) * slot_num_in_img_frm

    if wc > 0xFFFF:
        raise ValueError(
            f"wc[16:0] config out of bound, it's need to be config {wc}, please check your binning config.")
    if flnr > 0x1FFF:
        raise ValueError(f"flnr[12:0] config out of bound, it's need to be config {flnr}, "
                         f"please reconfigure your data transfer control.")
    DataflowConfig["WC"] = int(wc)
    DataflowConfig["FLNR"] = int(flnr)
    DataflowConfig["mipi_pkt_pl_num"] = int(wc / wc_factor)
    if function_sel == "MIPI":
        return DataflowConfig

    # //////////////////////////////////////////////////////////
    # 部分 DLY 参数设置 or 获取
    # //////////////////////////////////////////////////////////
    T1 = 13  # T_DSP_FIR_INIT
    T2 = 14  # SYSC hist_rd_out_ind to DSP path delay
    T3 = 2  # SYSC dsp_rd_out_ind to DSP path delay
    if dataflow_related_config is not None:
        SYS_CLK = dataflow_related_config["SYS_CLK"]  # 系统时钟(unit: MHz)
        MIPI_RATE = dataflow_related_config["MIPI_RATE"]  # MIPI 1.5Gbps
        MIPI_LANE_NUM = dataflow_related_config["MIPI_LANE_NUM"]  # MIPI 4 lane
        MIPI_PKT_INTV = dataflow_related_config["MIPI_PKT_INTV"] / 1000  # MIPI 1.5Gbps config (unit: us)
        MIPI_FIFO_SIZE = dataflow_related_config["MIPI_FIFO_SIZE"]  # MIPI FIFO: DEPTH = 1024, WIDTH = 32
    else:
        SYS_CLK = 400
        MIPI_RATE = 1500
        MIPI_LANE_NUM = 4
        MIPI_PKT_INTV = 0.6
        MIPI_FIFO_SIZE = 960
    # print(dataflow_related_config)
    PKT_DLY_MARGIN = 0

    # MIPI_FEND_DLY
    # -- Just for the work_start=0, wait MIPI transfer complete, Then enter MIPI_STD
    # -- If the SUB_IDLETIME calculate correct, MIPI_FEND_DLY just need gather tan macro EXPO_TIME(Masking+DRV_CH_SW+EXPO+Frame_end)
    DataflowConfig["mipi_fenddly"] = 100
    DataflowConfig["MIPI_PKT_DLY"] = MIPI_PKT_INTV

    # //////////////////////////////////////////////////////////
    # 计算 MIN_GAP
    # //////////////////////////////////////////////////////////
    # 在 work_mode == 0 时, 计算 SPHR 模式下, 半高宽计算的开销
    sphr_fwhm_spend_cyc = (out_echo_num + 1) * (2 + (fwhm_search_num + 1) + 1 + 1) + 1 if work_mode == 0 else 0

    # DSP RD MIN GAP (unit: cyc)
    # --NSPHR: 4 cycle is to ensure SRAM switch after previous seg is complete read.
    # -- SPHR: DPS need 3 cycle to complete previous segment data read,Then can cal FWHM.
    DSP_RD_MIN_GAP = sphr_fwhm_spend_cyc + 3 if work_mode == 0 else 4

    # HIST RD MIN GAP (unit: cyc)
    # --NSPHR: Hist data FIR PKS need at least 17 cycle.
    # -- SPHR: When hist data read complete, DSP cal FWHM after at least 5 cycle.
    #          It should be:T2-T3+T1+5:
    #              hist2dsp_cyc(14) - sysc2dsp_path_cyc(2) + dsp_fir_cyc(13) + dsp_do_ready_cal(4)
    HIST_RD_MIN_GAP = sphr_fwhm_spend_cyc + T2 - T3 + T1 + 5 if (work_mode == 0) else 17

    PKT_INTV_MIN_GAP = 4 + (2 * pkt_chksum_en)

    # //////////////////////////////////////////////////////////
    # 速率计算(unit: bit/us)
    # //////////////////////////////////////////////////////////
    mipi_rate = MIPI_RATE * MIPI_LANE_NUM
    dsp_rate = (16 if data_width_sel == 0 else 20) * SYS_CLK
    txu_rate = dsp_rate if one_dt_mode == 0 else 16 * SYS_CLK

    # 计算单次发包, DSP 可以连续读写的数据量
    if dsp_rate > mipi_rate:
        threshold_value = 0x01
        arrive_mipi_thrs_cyc = (SYS_CLK * threshold_value * 4 * 32) / dsp_rate
        can_read_max_cyc = (SYS_CLK * (MIPI_FIFO_SIZE - threshold_value * 4) * 32) / (
                dsp_rate - mipi_rate) + arrive_mipi_thrs_cyc
    elif dsp_rate < mipi_rate:
        threshold_value = 0xF0
        arrive_mipi_thrs_cyc = (SYS_CLK * threshold_value * 4 * 32) / dsp_rate
        can_read_max_cyc = (SYS_CLK * threshold_value * 4 * 32) / (mipi_rate - dsp_rate) + arrive_mipi_thrs_cyc
    else:
        threshold_value = 0x10  # Default case when dsp_rate == mipi_rate
        can_read_max_cyc = 0xFFFF_FFFF
    DataflowConfig["threshold_value"] = threshold_value

    # //////////////////////////////////////////////////////////
    # Cycle 计算
    # //////////////////////////////////////////////////////////
    # 发起一次 HIST read cycle 数
    rd_cyc_hist_1pxl = ((hist_maxbin_thrs - hist_minbin_thrs + 1) * 8) >> bin_widht_sel
    rd_cyc_once_hist_par = rd_cyc_hist_1pxl

    # generic data read cycle
    txu_info_ptk_rd_cyc = one_pkt_dsp_rd_cyc if one_dt_mode == 1 else ((38 + 22 * 4 + 8 + 16) / 2 + rd_cyc_crc32)
    txu_info_ptk_rd_cyc = int(txu_info_ptk_rd_cyc)

    # MIPI 包间间隔 cycle 数
    mipi_pkt_intv_cyc = math.ceil(MIPI_PKT_INTV * SYS_CLK)
    mipi_fsdly_cyc = mipi_pkt_intv_cyc
    if mipi_fsdly_cyc > 0x3FF:
        logging.warning(f"mipi_fsdly_cyc[9:0] config out of bound, it will assign the value from {mipi_fsdly_cyc} to 0x3FF")
        mipi_fsdly_cyc = 0x3FF
    DataflowConfig["mipi_fsdly_cyc"] = mipi_fsdly_cyc

    if work_mode == 3:
        mipi_fsdly_cyc = 0  # About PCM, if expo time long enough, and MIPI_FIFO is large enough, it can be set 0 to improve FPS
        mipi_pktdly1_cyc = 1  # This config is to delay PCM_DONE, if expo time long enough, it doesn't make sense(Because RTL design, it cannot be set 0 )
        hist_read_out_cyc = mipi_fsdly_cyc + txu_info_ptk_rd_cyc + one_pkt_dsp_rd_cyc + mipi_pktdly1_cyc + 30
        DataflowConfig["mipi_pktdly1_cyc"] = int(mipi_pktdly1_cyc)
        DataflowConfig["mipi_fsdly_cyc"] = int(mipi_fsdly_cyc)
        DataflowConfig["hist_read_out_cyc"] = int(hist_read_out_cyc)
        DataflowConfig["HIST_RD_OUT_TIME"] = math.ceil(hist_read_out_cyc / SYS_CLK * 10)
        return DataflowConfig

    # //////////////////////////////////////////////////////////
    # 在非 PCM 模式下, 针对 binning 相关的数据进行计算 和 校验
    # //////////////////////////////////////////////////////////
    # 判断 Pack 配置是否合理(PCM 为串行, 不需要增加此校验)
    if one_pkt_dsp_rd_cyc > can_read_max_cyc:
        if dsp_rate > mipi_rate:
            raise ValueError("Pack configuration is not reasonable, it will cause MIPI FIFO overflow.")
        if dsp_rate < mipi_rate:
            raise ValueError("Pack configuration is not reasonable, it will cause MIPI FIFO underflow.")

    # SEG_NUM 与 binning 配置合法性校验
    if pxl_binn_sel == 0 and seg_num == 0:
        raise ValueError(f"SEG_NUM = {seg_num}, PXL_BINN_SEL = {pxl_binn_sel}")
    elif pxl_binn_sel == 1 and seg_num % 2 != 0:
        raise ValueError(f"PXL_BINN_SEL = {pxl_binn_sel}, SEG_NUM must be divisible by 2")
    elif pxl_binn_sel == 2 and seg_num % 4 != 0:
        raise ValueError(f"PXL_BINN_SEL = {pxl_binn_sel}, SEG_NUM must be divisible by 4")

    # 计算一个 slot, pixel binning 后, 有多少个 SEG 需要读出
    seg_num_after_binn = seg_num >> pxl_binn_sel
    # 数据量 与packing配置 合法性校验
    if pack_2pxl_en == 1 and pack_4pxl_en == 1 and pack_8pxl_en == 1 and pack_16pxl_en == 1:
        if ((seg_num_after_binn <= 4 and seg_num_after_binn % (pack_16pxl_num + 1) > 0) or
                (seg_num_after_binn > 4 and (4 % (pack_16pxl_num + 1) > 0 or
                                             seg_num_after_binn % 4 % (pack_16pxl_num + 1) > 0))):
            raise ValueError(f"DSP will read {16 * seg_num_after_binn} pixels, "
                             f"but each packet is packed in {16 * (pack_16pxl_num + 1)} pixels")

    # //////////////////////////////////////////////////////////
    # 计算 MIPI TXDLY
    # //////////////////////////////////////////////////////////
    # 计算一个 slot, 需要发起多少次 HIST 读
    hist_rd_times = (seg_num_after_binn - 1) // 4 + 1

    # 计算一次完整 HIST 读 (64个DSP), 需要发送多少个 Packet
    one_hist_rd_pkt_num = 64 / one_pkt_pxl_num

    # ----------------------------------------------------------
    # 计算 mipi_pktdly3_cyc & 可以释放的给上一次数据传输的时间
    # ----------------------------------------------------------
    # mipi_pktdly3_cyc: the 1st hist read delay, 16 bit (unit: cycle)
    # When TXU-trans info package, MIPI need add additional time...
    txu_info_wc = wc if one_dt_mode == 1 else txu_info_ptk_rd_cyc * 2
    # sync_code = MIPI_LANE_NM; PH = 4; PF = 2
    lane0_PL = (MIPI_LANE_NUM + 4 + txu_info_wc + 2 - 1) // MIPI_LANE_NUM + 1  # 计算单 Lane0 需要传输的 payload (unit: *8bit)
    # 计算 one_pkt_dly_cyc
    if txu_rate > mipi_rate:
        # one_pkt_dly_cyc = (txu_rate - mipi_rate) * txu_info_ptk_rd_cyc / mipi_rate + mipi_pkt_intv_cyc + PKT_DLY_MARGIN
        mipi_read_cyc = mipi_pkt_intv_cyc + math.ceil((SYS_CLK * lane0_PL * 8) / MIPI_RATE)
        one_pkt_dly_cyc = mipi_read_cyc - txu_info_ptk_rd_cyc + PKT_DLY_MARGIN
    else:
        one_pkt_dly_cyc = 5 + mipi_pkt_intv_cyc + PKT_DLY_MARGIN
    # 计算 mipi_pktdly3_cyc && hist_1st_read_free_cyc
    if (mipi_fsdly_cyc + txu_info_ptk_rd_cyc + one_pkt_dly_cyc) > (rd_cyc_once_hist_par + HIST_RD_MIN_GAP):
        mipi_pktdly3_cyc = (mipi_fsdly_cyc + txu_info_ptk_rd_cyc + one_pkt_dly_cyc) - rd_cyc_once_hist_par
        hist_1st_read_free_cyc = mipi_pkt_intv_cyc if tx_frm_mode == 1 else 0
    else:
        mipi_pktdly3_cyc = HIST_RD_MIN_GAP
        hist_1st_read_free_cyc = ((rd_cyc_once_hist_par + HIST_RD_MIN_GAP) -
                                  (mipi_fsdly_cyc + txu_info_ptk_rd_cyc + one_pkt_dly_cyc) +
                                  (mipi_pkt_intv_cyc if tx_frm_mode == 1 else 0))
    if mipi_pktdly3_cyc > 0xFFFF:
        raise ValueError(f"mipi_fsdly_cyc[15:0] config out of bound, it's need to be config {mipi_pktdly3_cyc}")
    DataflowConfig["mipi_pktdly3_cyc"] = int(mipi_pktdly3_cyc)

    # ----------------------------------------------------------
    # 计算第一次 HIST 读, 实际可以释放的给上一次数据传输的时间
    # ----------------------------------------------------------
    # 极限帧率的处理
    # Cal at 1st hist read, when transfer generic data, how much data the MIPI_FIFO can hold...
    if txu_rate > mipi_rate:
        mipi_fifo_free_size0 = MIPI_FIFO_SIZE * 32 - (txu_rate - mipi_rate) * txu_info_ptk_rd_cyc / SYS_CLK
    else:
        mipi_fifo_free_size0 = MIPI_FIFO_SIZE * 32
    mipi_fifo_free_cyc0 = mipi_fifo_free_size0 / mipi_rate * SYS_CLK

    # Cal at dsp transfer data, how much data the MIPI_FIFO can hold...
    if dsp_rate > mipi_rate:
        # 由于 MIPI_FIFO 一直是累积的, 所以直接考虑最后一个包不溢出的 FIFO 大小即可
        mipi_fifo_free_size1 = MIPI_FIFO_SIZE * 32 - (dsp_rate - mipi_rate) * one_pkt_dsp_rd_cyc / SYS_CLK
    else:
        mipi_fifo_free_size1 = MIPI_FIFO_SIZE * 32
    mipi_fifo_free_cyc1 = mipi_fifo_free_size1 / mipi_rate * SYS_CLK

    if mipi_fifo_free_cyc0 < hist_1st_read_free_cyc:
        hist_1st_read_free_cyc = mipi_fifo_free_cyc0
        print("MIPI INFO: Generic data reduce the 1st hist read free cyc...")
    if mipi_fifo_free_cyc1 < hist_1st_read_free_cyc:
        hist_1st_read_free_cyc = mipi_fifo_free_cyc1
        print("MIPI INFO: Package data size reduce the 1st hist read free cyc...")
    pkt_can_reduce_cyc = int(hist_1st_read_free_cyc / one_slot_pxl_pkt_num)

    # ----------------------------------------------------------
    # 计算 dly1 & dly2
    # ----------------------------------------------------------
    # dly1: DSP DLY: 16 bit (unit: cycle)
    # dly2: HIST DLY: 实际值=配置值*16， 16 bit (unit: cycle)
    lane0_PL = (MIPI_LANE_NUM + 4 + wc + 2 - 1) // MIPI_LANE_NUM + 1  # 计算单 Lane0 需要传输的 payload (unit: *8bit)
    if dsp_rate > mipi_rate:
        mipi_read_cyc = mipi_pkt_intv_cyc + math.ceil((SYS_CLK * lane0_PL * 8) / MIPI_RATE)
        one_pkt_dly_cyc = mipi_read_cyc - one_pkt_dsp_rd_cyc + PKT_DLY_MARGIN
    else:
        # TODO: if mipi_rate > dsp_rate, MIPI_PKT_INTV can hide in CSI wait MIPI_FIFO threshold
        one_pkt_dly_cyc = 5 + mipi_pkt_intv_cyc + PKT_DLY_MARGIN
    one_pkt_dly_cyc = max(one_pkt_dly_cyc, PKT_INTV_MIN_GAP)

    # 极致帧率压缩 one_pkt_dly_cyc 计算
    one_pkt_dly_cyc_tmp = max((one_pkt_dly_cyc - pkt_can_reduce_cyc), PKT_INTV_MIN_GAP)

    # 极致帧率压缩后, 第一次 HIST 读有多少剩余量给到 FS
    hist_1st_residual_cyc = hist_1st_read_free_cyc - (one_pkt_dly_cyc - one_pkt_dly_cyc_tmp) * one_slot_pxl_pkt_num
    one_pkt_dly_cyc = one_pkt_dly_cyc_tmp

    # ----------------------------------------------------------
    # mipi_pktdly1_cyc
    # ----------------------------------------------------------
    mipi_pktdly1_cyc = one_pkt_dly_cyc
    if mipi_pktdly1_cyc > 0xFFFF:
        raise ValueError(f"mipi_pktdly1_cyc[15:0] config out of bound, it's need to be config {mipi_pktdly1_cyc}")
    DataflowConfig["mipi_pktdly1_cyc"] = int(mipi_pktdly1_cyc)

    # ----------------------------------------------------------
    # mipi_pktdly2_cyc
    # ----------------------------------------------------------
    MARGIN = max(0, DSP_RD_MIN_GAP - one_pkt_dly_cyc)
    rd_cyc_once_dsp_par = (one_pkt_dsp_rd_cyc + one_pkt_dly_cyc) * one_hist_rd_pkt_num

    if (rd_cyc_once_dsp_par + MARGIN) >= (rd_cyc_once_hist_par + HIST_RD_MIN_GAP):
        mipi_pktdly2_cyc = math.ceil(((rd_cyc_once_dsp_par + MARGIN) - rd_cyc_once_hist_par) / 16)
    else:
        mipi_pktdly2_cyc = math.ceil(HIST_RD_MIN_GAP / 16)
    if mipi_pktdly2_cyc > 0xFFFF:
        raise ValueError(f"mipi_pktdly2_cyc[15:0] config out of bound, it's need to be config {mipi_pktdly2_cyc}")
    DataflowConfig["mipi_pktdly2_cyc"] = int(mipi_pktdly2_cyc)

    # ----------------------------------------------------------
    # Calculate READ_OUT_HIST time (used for SLAVE MODE)
    # ----------------------------------------------------------
    hist_read_out_cyc0 = rd_cyc_once_hist_par + mipi_pktdly3_cyc  # 1st hist read time
    hist_read_out_cyc1 = (rd_cyc_once_hist_par + mipi_pktdly2_cyc * 16) * (
            hist_rd_times - 1)  # HIST & DSP parallel read time
    hist_read_out_cyc2 = (T2 - T3) + (one_pkt_dsp_rd_cyc + mipi_pktdly1_cyc) * (
            (one_slot_pxl_pkt_num - 1) % one_hist_rd_pkt_num + 1)  # The last DSP read time
    hist_read_out_cyc3 = 3  # The RTL design time of SLOT_RD_DONE is 3 cycle longer than theoretical time
    hist_read_out_cyc4 = max(mipi_pkt_intv_cyc - hist_1st_residual_cyc,
                             0) if tx_frm_mode == 0 else 0  # tx_frm_mode=0, FE 传输需要传输的时间
    hist_read_out_cyc = hist_read_out_cyc0 + hist_read_out_cyc1 + hist_read_out_cyc2 + hist_read_out_cyc3 + hist_read_out_cyc4
    DataflowConfig["hist_read_out_cyc"] = int(hist_read_out_cyc)
    DataflowConfig["HIST_RD_OUT_TIME"] = math.ceil(hist_read_out_cyc / SYS_CLK * 10)  # 0.1us 为单位
    # 在进行极限帧率计算时, if (TX_FRM_MODE=1), 由于配置的 DLY 以 slot 为单位进行计算, img_frm 的 FS 和 FE 没有进行考虑, 因此需要在 frm_idletime 上进行补偿
    DataflowConfig["frm_idletime"] = math.ceil(MIPI_PKT_INTV * 2)
    return DataflowConfig


def GenerateSwanRegConfig(swan01_config: dict, reg_cfg_fp="./Swan01RegConfig.py"):
    """
    本方法主要实现功能为: 基于基准脚本以及最新的配置, 生成新的 Swan 配置脚本
    主要包含以下功能:
        1. 根据 swan01_config["SYS_CLK"] 配置, 配置 PLL1频率 及 与之相关的分频寄存器
        2. 根据 swan01_config["MIPI_RATE"] 配置, 配置 MIPI 速率相关的寄存器
        3. 根据 swan01_config[""] 配置 MIPI WC & FLNR寄存器
        4. 根据 swan01_config[""] 配置 MIPI_TXDLY[5:0] -> MIPI_PKTDLY
        5. 根据 swan01_config["roi_save_n"] 配置 block_write
    """

    # 从本地配置文件获取频率等配置信息
    with open(reg_cfg_fp, 'r', encoding='utf-8') as file:
        content = file.read()
        local_scope = locals()
        exec(content, globals(), local_scope)
        FREQ_Config = local_scope["FREQ_Config"]
        DIV_CONFIG = local_scope["DIV_CONFIG"]
    # ----------------------------------------------------------------------------------------
    # initial
    # ----------------------------------------------------------------------------------------
    protocol = swan01_config["protocol"]
    min_lens = 4 if protocol == 0 else 3
    addr_index = 2 if protocol == 0 else 1
    regs_write = "I2C_Write" if protocol == 0 else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == 0 else "SPI_Block_Write"

    ref_cfg_file = swan01_config["ref_cfg_file"]
    if not os.path.exists(ref_cfg_file):
        raise ValueError("The reference config file does not exist!")

    # ----------------------------------------------------------------------------------------
    # Calculate Register Value
    # ----------------------------------------------------------------------------------------
    # PLL0 config
    # ////////////////////////////////////////////////////////////////////////////
    PLL0_ID = FREQ_Config[swan01_config['XCLK']]["PLL0"][0]["ID"]
    PLL0_OD = FREQ_Config[swan01_config['XCLK']]["PLL0"][0]["OD"]
    PLL0_FB = FREQ_Config[swan01_config['XCLK']]["PLL0"][0]["FB"]
    PLL0_DIV1 = ((PLL0_ID & 0x0007) << 4) + ((PLL0_OD & 0x0003) << 0)
    PLL0_DIV2 = ((PLL0_FB & 0x00FF) << 0)

    # PLL1 config. swan01_config['SYS_CLK'] = 330M, 250M, 200M
    # ////////////////////////////////////////////////////////////////////////////
    PLL1_ID = FREQ_Config[swan01_config['XCLK']]["PLL1"][0]["ID"]
    PLL1_OD = FREQ_Config[swan01_config['XCLK']]["PLL1"][0]["OD"]
    PLL1_FB = FREQ_Config[swan01_config['XCLK']]["PLL1"][0]["FB"]
    PLL1_DIV1 = ((PLL1_ID & 0x0007) << 4) + ((PLL1_OD & 0x0003) << 0)
    PLL1_DIV2 = ((PLL1_FB & 0x00FF) << 0)

    # PLL2 config. swan01_config['SYS_CLK'] = 330M, 400M
    # ////////////////////////////////////////////////////////////////////////////
    PLL2_ID = FREQ_Config[swan01_config['XCLK']]["PLL2"][swan01_config['SYS_CLK']]["ID"]
    PLL2_OD = FREQ_Config[swan01_config['XCLK']]["PLL2"][swan01_config['SYS_CLK']]["OD"]
    PLL2_FB = FREQ_Config[swan01_config['XCLK']]["PLL2"][swan01_config['SYS_CLK']]["FB"]
    PLL2_DIV1 = ((PLL2_ID & 0x0007) << 4) + ((PLL2_OD & 0x0003) << 0)
    PLL2_DIV2 = ((PLL2_FB & 0x00FF) << 0)

    # DIV config
    # ////////////////////////////////////////////////////////////////////////////
    SYSCLK1M_DIVL = (DIV_CONFIG[swan01_config['SYS_CLK']]["SYSCLK1M_DIV"] & 0x00FF)
    SYSCLK1M_DIVH = (DIV_CONFIG[swan01_config['SYS_CLK']]["SYSCLK1M_DIV"] & 0xFF00) >> 8
    SYSCLK10M_DIV = (DIV_CONFIG[swan01_config['SYS_CLK']]["SYSCLK10M_DIV"] & 0xFF)
    TXESC_CLKDIV1 = (DIV_CONFIG[swan01_config['SYS_CLK']]["TXESC_CLKDIV_CNT"] & 0x1F)
    TXESC_CLKDIV2 = (DIV_CONFIG[swan01_config['SYS_CLK']]["TXESC_CLKDIV_DTY"] & 0x0F)

    # MIPI_RATE CONFIG. swan01_config["MIPI_RATE"] = 0.8G, 1.0G, 1.2G, 1.5G
    # ////////////////////////////////////////////////////////////////////////////
    MIPI_NS = FREQ_Config[swan01_config['XCLK']]["MIPI"][swan01_config['MIPI_RATE']]["NS"]
    MIPI_MS = FREQ_Config[swan01_config['XCLK']]["MIPI"][swan01_config['MIPI_RATE']]["MS"]
    MIPI_PS = FREQ_Config[swan01_config['XCLK']]["MIPI"][swan01_config['MIPI_RATE']]["PS"]
    MIPIPLL_LPDH = (MIPI_NS & 0x0100) >> 8
    MIPIPLL_LPDL = (MIPI_NS & 0x00FF) >> 0
    MIPIPLL_PPD = ((MIPI_MS & 0x0007) << 5) + ((MIPI_PS & 0x001F) << 0)

    # MIPI FLNR & WC & TXDLY
    # ////////////////////////////////////////////////////////////////////////////
    SYS_CLK = 330 if swan01_config['SYS_CLK'] == 0 else 400
    MIPI_RATE = 800 if swan01_config['MIPI_RATE'] == 0 \
        else 1000 if swan01_config['MIPI_RATE'] == 1 \
        else 1200 if swan01_config['MIPI_RATE'] == 2 \
        else 1500
    MIPI_CFG = MIPI_CONFIG_Cal(SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE, display=False)
    dataflow_related_config = SwanDataflowRelateConfigGet(swan01_config)
    DataflowConfig = SwanDataflowConfigCal(swan01_config, dataflow_related_config)
    # print(DataflowConfig)
    WC, FLNR, PKT_TYPE = DataflowConfig["WC"], DataflowConfig["FLNR"], DataflowConfig["PKT_TYPE"]
    HIST_RD_OUT_TIME = DataflowConfig["HIST_RD_OUT_TIME"]

    VC0_FLNR_L = (FLNR & 0x00FF) >> 0
    VC0_FLNR_H = (FLNR & 0xFF00) >> 8
    VC0_WC_L = (WC & 0x00FF) >> 0
    VC0_WC_H = (WC & 0xFF00) >> 8
    MIPI_PKTDLY1_CYC_L = (DataflowConfig["mipi_pktdly1_cyc"] >> 0) & 0xFF
    MIPI_PKTDLY1_CYC_H = (DataflowConfig["mipi_pktdly1_cyc"] >> 8) & 0xFF
    MIPI_PKTDLY2_CYC_L = (DataflowConfig["mipi_pktdly2_cyc"] >> 0) & 0xFF
    MIPI_PKTDLY2_CYC_H = (DataflowConfig["mipi_pktdly2_cyc"] >> 8) & 0xFF
    MIPI_PKTDLY3_CYC_L = (DataflowConfig["mipi_pktdly3_cyc"] >> 0) & 0xFF
    MIPI_PKTDLY3_CYC_H = (DataflowConfig["mipi_pktdly3_cyc"] >> 8) & 0xFF
    MIPI_PKT_PL_NUM_L = (DataflowConfig["mipi_pkt_pl_num"] >> 0) & 0xFF
    MIPI_PKT_PL_NUM_H = (DataflowConfig["mipi_pkt_pl_num"] >> 8) & 0xFF
    MIPI_FSDLY_CYC_L = (DataflowConfig["mipi_fsdly_cyc"] >> 0) & 0xFF
    MIPI_FSDLY_CYC_H = (DataflowConfig["mipi_fsdly_cyc"] >> 8) & 0x03
    THRESHOLD_VALUE = DataflowConfig["threshold_value"] & 0xFF
    HIST_READ_OUT_CYC = DataflowConfig["hist_read_out_cyc"] & 0xFF

    # TDC_DLY_CFG1
    # ////////////////////////////////////////////////////////////////////////////
    PLL_OD = ((PLL1_DIV1 & 0x03) >> 0)  # 0~3: 2，4，6，8
    # PHASE_DLY_OPT = 0b011 if PLL_OD == 0 else 0b111  # PHASE_DLY_OPT 根据 PLL1 进行计算

    # ROI length    # TODO: 需要根据 Spadis APP 逻辑进行配置
    # ////////////////////////////////////////////////////////////////////////////
    # roi_length = 674*4

    # ----------------------------------------------------------------------------------------
    # Modify the register configuration according to the baseline script.
    # ----------------------------------------------------------------------------------------
    csru_datas = PubMethod.read_file(ref_cfg_file)
    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check.")

    config_flag = {
        "SYS_CTRL": 0,
        "SYNC_POL": 0,
        "TXU_CFG": 0,
        "PXL_BINN_CFG": 0,
        "MIPI_PACK_CTRL": 0,
    }

    # --------------------------------------------------------
    # 遍历脚本数据
    # --------------------------------------------------------
    for line in range(len(csru_datas)):
        _str = csru_datas[line].strip().replace("\n", "").replace("\r", "")  # 去除换行符, 保存时统一保存
        if _str == '' or _str[0:2] == '//':  # 空行 & 整行注释 场景
            csru_datas[line] = _str
            continue

        configs = re.split(",|//", _str)
        for i in range(len(configs)):
            configs[i] = configs[i].strip()

        # register_write
        if configs[0] == regs_write:
            # print(_str)
            if len(configs) < min_lens:
                raise ValueError(f"Script format error. line{line}: {_str}")
            addr = int(configs[addr_index], 16)
            config_str = configs[addr_index + 1][0:2]
            register_value = int(config_str, 16)

            # text_annotations = f" //{', '.join(configs[min_lens:])}" if len(configs) > min_lens else None
            index = _str.find("//")
            annotation = _str[index:] if index != -1 else ""

            if addr == reg_addr['PXL_BINN_CFG']:
                register_value = (register_value & (0xFF - 0x03)) + (swan01_config['PXL_BINN_SEL'] << 0)
                config_flag['PXL_BINN_CFG'] = 1
            elif addr == reg_addr['SEG_NUM']:
                register_value = swan01_config['SEG_NUM']
            elif addr == reg_addr['HIST_RD_OUT_TIME_L']:
                register_value = ((HIST_RD_OUT_TIME & 0x00FF) >> 0)
            elif addr == reg_addr['HIST_RD_OUT_TIME_H']:
                register_value = ((HIST_RD_OUT_TIME & 0xFF00) >> 8)
            elif addr == reg_addr['SYS_CTRL']:
                register_value = (register_value & (0xFF - 0x80)) + (swan01_config['TX_FRM_MODE'] << 7)
                register_value = (register_value & (0xFF - 0x40)) + (swan01_config["TRG_I_EN"] << 6)
                register_value = (register_value & (0xFF - 0x06)) + (swan01_config["WORK_MODE"] << 1)
                register_value = (register_value & (0xFF - 0x01)) + (swan01_config["MST_MODE"] << 0)
                config_flag['SYS_CTRL'] = 1
            elif addr == reg_addr['SYNC_POL']:
                register_value = (register_value & (0xFF - 0x01)) + (swan01_config["SYNC_POL"] << 0)
                config_flag['SYNC_POL'] = 1
            elif addr == reg_addr['TXU_CFG']:
                register_value = (register_value & (0xFF - 0x01)) + (swan01_config["DATA_WIDTH_SEL"] << 0)
                register_value = (register_value & (0xFF - 0x08)) + (swan01_config["ONE_DT_MODE"] << 3)
                register_value = (register_value & (0xFF - 0x10)) + (swan01_config["PKT_CHKSUM_EN"] << 4)
                config_flag['TXU_CFG'] = 1
            elif addr == reg_addr['MIPI_PACK_CTRL']:
                # pxl_pack_sel = swan01_config["PXL_PACK_SEL"]
                # assert pxl_pack_sel in [0, 1, 2, 3, 4, 5, 6, 7], "PXL_PACK_SEL must in [0, 1, 2, 3, 4, 5, 6, 7]"
                # register_value = 0b0000_0000 if pxl_pack_sel == 0 else \
                #     0b0000_0001 if pxl_pack_sel == 1 else \
                #     0b0000_0011 if pxl_pack_sel == 2 else \
                #     0b0000_0111 if pxl_pack_sel == 3 else \
                #     0b0000_1111 if pxl_pack_sel == 4 else \
                #     0b0001_1111 if pxl_pack_sel == 5 else \
                #     0b0010_1111 if pxl_pack_sel == 6 else \
                #     0b0011_1111 if pxl_pack_sel == 7 else \
                #     0b0000_0000
                register_value = ((swan01_config["PACK_16PXL_NUM"] << 4) +
                                  (swan01_config["PACK_16PXL_EN"] << 3) +
                                  (swan01_config["PACK_8PXL_EN"] << 2) +
                                  (swan01_config["PACK_4PXL_EN"] << 1) +
                                  (swan01_config["PACK_2PXL_EN"] << 0))
                config_flag['MIPI_PACK_CTRL'] = 1
            elif addr == reg_addr['UNIQ_FUNC_CFG']:
                register_value = (swan01_config["ULR_EN"] & 0x03)
            elif addr == reg_addr['LSPRD_HOP_CFG1']:
                register_value = (((swan01_config["LSPRD_HOP_EN"] & 0x01) << 7) +
                                  ((swan01_config["LSPRD_HOP_STEP"] & 0x3F) << 0))
            elif addr == reg_addr['LSPRD_HOP_CFG2']:
                register_value = (swan01_config["LSPRD_HOP_CNTS"] & 0xFF)
            elif addr == reg_addr['HIST_MINBIN_THRS']:
                register_value = swan01_config["HIST_MINBIN_THRS"] & 0xFF
            elif addr == reg_addr['HIST_MAXBIN_THRS']:
                register_value = swan01_config["HIST_MAXBIN_THRS"] & 0xFF
            elif addr == reg_addr['HIST_BINFULL_THRS_L']:
                register_value = swan01_config["HIST_BINFULL_THRS"] & 0xFF
            elif addr == reg_addr['HIST_BINFULL_THRS_H']:
                register_value = (register_value & (0xFF - 0x03)) + ((swan01_config["HIST_BINFULL_THRS"] >> 8) & 0x3)
            elif addr == reg_addr['HIST_NS_MINBIN_THRS']:
                register_value = swan01_config["NS_MINBIN_THRS"] & 0xFF
            elif addr == reg_addr['HIST_NS_MAXBIN_THRS']:
                register_value = swan01_config["NS_MAXBIN_THRS"] & 0xFF
            elif addr == reg_addr['DRV_CHSWTME']:
                register_value = swan01_config["DRV_CHSWTME"] & 0xFF
            elif addr == reg_addr['HIST_MISC_CFG']:
                register_value = (register_value & (0xFF - 0x20)) + (swan01_config["INTF_HIST_MODE"] << 5)
                register_value = (register_value & (0xFF - 0x10)) + (swan01_config["INTF_DET_EN"] << 4)
                register_value = (register_value & (0xFF - 0x08)) + (swan01_config["FLEX_SHOT_EN"] << 3)
                register_value = (register_value & (0xFF - 0x02)) + (swan01_config["BIN_WIDTH_MODE"] << 1)
                register_value = (register_value & (0xFF - 0x01)) + (swan01_config["BIN_WIDTH_SEL"] << 0)
            elif addr == reg_addr['FRM_SLOT_NUM_L']:
                register_value = swan01_config["FRM_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['FRM_SLOT_NUM_H']:
                register_value = (swan01_config["FRM_SLOT_NUM"] >> 8) & 0xFF
            elif addr == reg_addr['ANGLE_GRP_CFG']:
                register_value = (register_value & (0xFF - 0x07)) + (swan01_config["ANGLE_GRP_SW_NUM"] & 0x07)
            elif addr == reg_addr['ANGLE_GRP0_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP0_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP1_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP1_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP2_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP2_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP3_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP3_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP4_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP4_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP5_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP5_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP6_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP6_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['ANGLE_GRP7_SLOT_NUM']:
                register_value = swan01_config["ANGLE_GRP7_SLOT_NUM"] & 0xFF
            elif addr == reg_addr['DSP_CFG1']:
                register_value = swan01_config["OUT_TOTALBIN_NUM"] & 0xFF
            elif addr == reg_addr['DSP_CFG2']:
                register_value = swan01_config["OUT_ECHOBIN_NUM"] & 0xFF
            elif addr == reg_addr['DSP_CFG3']:
                register_value = (((swan01_config["OUT_OVFL_FLAT_EN"] & 0x01) << 7) +
                                  ((swan01_config["OUT_ECHOBIN_MODE"] & 0x01) << 6) +
                                  ((swan01_config["OUT_NUMBIN_MODE"] & 0x01) << 5) +
                                  ((swan01_config["OUT_FIR_RAW_SEL"] & 0x01) << 4) +
                                  ((swan01_config["OUT_ECHO_NUM"] & 0x07) << 1) +
                                  ((swan01_config["OUT_INTF_HIST_SEL"] & 0x01) << 0))
            elif addr == reg_addr['DSP_CFG4']:
                register_value = (register_value & (0xFF - 0x0F)) + (swan01_config["ECHO_ORDER_NEAR_NUM"] & 0x0F)
            elif addr == reg_addr['DSP_RGM_CFG1']:
                register_value = (register_value & (0xFF - 0x0F)) + (swan01_config["FWHM_HALF_COEF"] & 0x0F)
            elif addr == reg_addr['DSP_RGM_CFG3']:
                register_value = (register_value & (0xFF - 0x0F)) + (swan01_config["FWHM_SEARCH_NUM"] & 0x0F)
            # elif addr == reg_addr['ANA_MISC_CFG1']:
                # register_value = (register_value & (0xFF - 0x0E)) + (PHASE_DLY_OPT << 1)
            elif addr == reg_addr['SPOT_MON_MINBIN_THRS']:
                register_value = swan01_config["SPOT_MON_MINBIN_THRS"] & 0xFF
            elif addr == reg_addr['THS_EXIT']:
                register_value = MIPI_CFG["DataTxThsexitCnt"] & 0xFF
            elif addr == reg_addr['THS_PREPARE']:
                register_value = MIPI_CFG["DataTxThsprepareCnt"] & 0xFF
            elif addr == reg_addr['THS_ZERO']:
                register_value = MIPI_CFG["DataTxThszeroCnt"] & 0xFF
            elif addr == reg_addr['THS_TRAIL']:
                register_value = MIPI_CFG["DataTxThstrailCnt"] & 0xFF
            elif addr == reg_addr['SYSCLK1M_DIVL']:
                register_value = SYSCLK1M_DIVL
            elif addr == reg_addr['SYSCLK1M_DIVH']:
                register_value = (register_value & (0xFF - 0x01)) + (SYSCLK1M_DIVH << 0)
            else:
                register_value = SYSCLK10M_DIV if addr == reg_addr['SYSCLK10M_DIV'] \
                    else MIPI_PKTDLY1_CYC_L if addr == reg_addr['MIPI_TXDLY1'] \
                    else MIPI_PKTDLY1_CYC_H if addr == reg_addr['MIPI_TXDLY2'] \
                    else MIPI_PKTDLY2_CYC_L if addr == reg_addr['MIPI_TXDLY3'] \
                    else MIPI_PKTDLY2_CYC_H if addr == reg_addr['MIPI_TXDLY4'] \
                    else MIPI_PKTDLY3_CYC_L if addr == reg_addr['MIPI_TXDLY5'] \
                    else MIPI_PKTDLY3_CYC_H if addr == reg_addr['MIPI_TXDLY6'] \
                    else MIPI_FSDLY_CYC_L if addr == reg_addr['MIPI_TXDLY7'] \
                    else MIPI_FSDLY_CYC_H if addr == reg_addr['MIPI_TXDLY8'] \
                    else TXESC_CLKDIV1 if addr == reg_addr['TXESC_CLKDIV1'] \
                    else TXESC_CLKDIV2 if addr == reg_addr['TXESC_CLKDIV2'] \
                    else PLL0_DIV1 if addr == reg_addr['PLL0_DIV1'] \
                    else PLL0_DIV2 if addr == reg_addr['PLL0_DIV2'] \
                    else PLL1_DIV1 if addr == reg_addr['PLL1_DIV1'] \
                    else PLL1_DIV2 if addr == reg_addr['PLL1_DIV2'] \
                    else PLL2_DIV1 if addr == reg_addr['PLL2_DIV1'] \
                    else PLL2_DIV2 if addr == reg_addr['PLL2_DIV2'] \
                    else MIPI_PKT_PL_NUM_L if addr == reg_addr["MIPI_PKT_PLNUM_L"] \
                    else MIPI_PKT_PL_NUM_H if addr == reg_addr["MIPI_PKT_PLNUM_H"] \
                    else THRESHOLD_VALUE if addr == reg_addr['VC0_THRESHOLD'] \
                    else MIPIPLL_LPDH if addr == reg_addr['MIPIPLL_LPDH'] \
                    else MIPIPLL_LPDL if addr == reg_addr['MIPIPLL_LPDL'] \
                    else MIPIPLL_PPD if addr == reg_addr['MIPIPLL_PPD'] \
                    else VC0_FLNR_L if addr == reg_addr['VC0_FLNR_L'] \
                    else VC0_FLNR_H if addr == reg_addr['VC0_FLNR_H'] \
                    else VC0_WC_L if addr == reg_addr['VC0_WC_L'] \
                    else VC0_WC_H if addr == reg_addr['VC0_WC_H'] \
                    else PKT_TYPE if addr == reg_addr['PKT_TYPE'] \
                    else register_value

            configs[addr_index + 1] = "{:0>2X}".format(register_value)
            csru_datas[line] = f"{', '.join(configs[0: min_lens])} {annotation}"
        # roisram_write
        elif configs[0] == roisram_write:
            if len(configs) < 5:
                raise ValueError(f"Script format error. line{line}: {_str}")
            # configs[3] = "{:0>4X}".format(roi_length)
            # configs[4] = swan01_config["roi_name"]
            configs[4] = "roi_mem"
            csru_datas[line] = ", ".join(configs[0:5])
            continue
        else:
            # raise ValueError(f"The script file format is incorrect: line {line+1}: {_str}")
            csru_datas[line] = _str
    for key, value in config_flag.items():
        if value == 0:
            logging.warning(f"The reference script no {key} ( {reg_addr[key]:0>4X} ) configuration line, "
                            f"which may make the generated script incorrect.")

    # --------------------------------------------------------
    # 增加配置说明
    # --------------------------------------------------------
    config_instruction = "config_instruction"
    config_print = "PRINT"
    if config_instruction in swan01_config and config_print in swan01_config[config_instruction]:
        _str = "// "
        _len = len(swan01_config[config_instruction][config_print])
        for i in range(_len):
            config = swan01_config[config_instruction][config_print][i]
            if i > 0:
                _str += "; "
            _str += f"{config}: {swan01_config[config_instruction][config][swan01_config[config]]}"
        csru_datas.insert(0, _str)  # 根据配置，在行首打印配置信息内容
    PubMethod.data_save(fname=f'{swan01_config["reg_name"]}.txt',
                        data_list=csru_datas,
                        split='\n',
                        fd_path=swan01_config["fd_path"])
    return


def SwanHistReadTimeCal(swan01_config: dict):
    # ////////////////////////////////////////////////////////////////////////////
    dataflow_related_config = SwanDataflowRelateConfigGet(swan01_config)
    DataflowConfig = SwanDataflowConfigCal(swan01_config, dataflow_related_config)
    print(f"{swan01_config["reg_name"]} one slot read time: {DataflowConfig['HIST_RD_OUT_TIME'] / 10} us")


def ParseSwanRegConfig(script_file=None, protocol=0):
    if not os.path.exists(script_file):
        raise ValueError("The reference config file does not exist!")

    csru_cfg = GetCsruConfig(script_file, protocol)
    _hyper_link = LogerPubMethod.create_file_hyperlink(url=script_file)
    info = f"Parse {_hyper_link}..."
    # print(info)
    _str = "---------------------------\n"
    _str += "REG_CONFIG\n"
    _str += "---------------------------\n"

    info_json = PubMethod.dict_print_format(csru_cfg, indent=2, level=1)

    _str += info_json

    _str = LogerPubMethod.create_consolas_str(_str, color="#0076f6")
    print(f"{info}<br>{_str}")

    VC0_WC = csru_cfg["MIPI"]["VC0_WC"]
    VC0_FLNR = csru_cfg["MIPI"]["VC0_FLNR"]

    # WC, FLNR = CalMipiFlnrAndWC(csru_cfg)
    DataflowConfig = SwanDataflowConfigCal(csru_cfg, function_sel="MIPI")
    WC, FLNR = DataflowConfig["WC"], DataflowConfig["FLNR"]
    if VC0_WC != WC or VC0_FLNR != FLNR:
        FLNR_L = (FLNR & 0x00FF) >> 0
        FLNR_H = (FLNR & 0xFF00) >> 8
        WC_L = (WC & 0x00FF) >> 0
        WC_H = (WC & 0xFF00) >> 8
        _str = "ERROR: MIPI WC or FLNR config error!!! It's should be config:\n"
        _str += "  FLNR_L : 0x{:0>2X}\n".format(FLNR_L)
        _str += "  FLNR_H : 0x{:0>2X}\n".format(FLNR_H)
        _str += "  WC_L   : 0x{:0>2X}\n".format(WC_L)
        _str += "  WC_H   : 0x{:0>2X}  ".format(WC_H)
        _str = LogerPubMethod.create_consolas_str(_str, color="red")
        print(_str)
        return
    pass


if __name__ == '__main__':
    chip_cfg = {
        "WORK_MODE": 1,
        "TX_FRM_MODE": 0,
        "HIST_MINBIN_THRS": 0,
        "HIST_MAXBIN_THRS": 255,
        "DATA_WIDTH_SEL": 0,
        "FRM_SLOT_NUM": 0,
        "PACK_16PXL_NUM": 0,
        "PACK_16PXL_EN": 1,
        "PACK_8PXL_EN": 1,
        "PACK_4PXL_EN": 1,
        "PACK_2PXL_EN": 1,
        "PXL_BINN_SEL": 0,
        "BIN_WIDTH_SEL": 1,
        "OUT_TOTALBIN_NUM": 0xba,
        "OUT_ECHOBIN_NUM": 0,
        "OUT_NUMBIN_MODE": 0,
        "OUT_ECHO_NUM": 2,
        "ONE_DT_MODE": 0,
        "PKT_CHKSUM_EN": 0,
        "SEG_NUM": 16,
        "FWHM_SEARCH_NUM": 0,
    }

    dataflow_related_cfg = {
        "SYS_CLK": 400,  # 系统时钟(unit: MHz)
        "MIPI_RATE": 1500,  # MIPI 1.5Gbps
        "MIPI_LANE_NUM": 4,  # MIPI 4 lane
        "MIPI_PKT_INTV": 0.9,  # MIPI 1.5Gbps config (unit: us)
        "MIPI_FIFO_SIZE": 960,  # MIPI FIFO: DEPTH = 1024, WIDTH = 32
        "PKT_DLY_MARGIN": 0,  # 额外的 cycle 开销
    }

    txdlycfg = SwanDataflowConfigCal(chip_cfg, dataflow_related_cfg)
    print(txdlycfg)

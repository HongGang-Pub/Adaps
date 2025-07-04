#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : PubMethod.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    : 本文件包含部分公共方法, 用于 Hawk MIPI 相关的模型计算, 供其他模块调用

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025-04-23 11:55    honggang_li    v1.0        1. 将 mipi帧率计算、mipi_fifo仿真模型、mipi_pktdly最小值
                                                  计算的公共方法, 抽取出来

=================================================================================================
"""
from AdapsChip.Common.common import MipiPKGIntvCal
from HawkConfig import *


def CalMipiFlnrAndWC(csru_cfg, **kwargs):
    """
    计算 MIPI WC & FLNR 包数量(可以根据实际寄存器进行配置, 也可以根据配置, 仅仅计算 1sub-frame 的包数量)

    Args:
        csru_cfg: Hawk 寄存器配置
        **kwargs: if kwargs["unit"]=subframe, then return FLNR is cal for one subframe,
                  else return FLNR is cal for TX_FRM_MODE config

    Returns:
        tuple: (WC, FLNR)

    """
    work_mode = csru_cfg["WORK_MODE"]
    scan_mode = csru_cfg["SCAN_MODE"]
    v_roll_num = csru_cfg["V_ROLL_NUM"]
    h_roll_num = csru_cfg["H_ROLL_NUM"]
    h_vld_seg = csru_cfg["H_VLD_SEG"]
    minbin_thrs = csru_cfg["MINBIN_THRS"]
    maxbin_thrs = csru_cfg["MAXBIN_THRS"]
    out_bin_num = csru_cfg["OUT_BIN_NUM"]
    tx_frm_mode = csru_cfg["TX_FRM_MODE"]
    one_dt_mode = csru_cfg["ONE_DT_MODE"]

    v_pxl_out_num = 6 if csru_cfg["V_PXL_OUT_NUM"] == 1 else 1

    if "unit" in kwargs and kwargs["unit"] == "subframe":
        # return FLNR is cal for one subframe
        total_roll_num = 1
    elif tx_frm_mode == 1:
        if scan_mode == 0:
            total_roll_num = (v_roll_num + 1) if work_mode != 3 else (v_roll_num + 1) * 9
        else:   # scan_mode == 1:
            total_roll_num = (v_roll_num + 1) * (h_roll_num + 1)
    else:
        total_roll_num = 1

    if work_mode == 0:
        PL = 38 * v_pxl_out_num if out_bin_num == 0 else 62 * v_pxl_out_num
        PKT_NUM = 8 * (h_vld_seg + 1)   # 一次 rolling 的 Pixel PKT 数量
    elif work_mode == 1:
        PL = 80 * v_pxl_out_num if out_bin_num == 0 else 132 * v_pxl_out_num
        PKT_NUM = 8 * (h_vld_seg + 1)
    elif work_mode == 2:
        PL = ((maxbin_thrs+1) * 4 - minbin_thrs * 2) * 4
        PKT_NUM = 2 * (h_vld_seg + 1) * v_pxl_out_num
    else:
        PL = 8 * 4
        PKT_NUM = 2 * (h_vld_seg + 1) * v_pxl_out_num
    wc = PL * 1.5
    flnr = (PKT_NUM + one_dt_mode) * total_roll_num
    return int(wc), flnr


def OneSubframePerVCPktNumCal(csru_cfg: dict):
    """
    计算单次曝光, 不包含 generic_date, 单个 VC 的 纯 HIST 数据的包个数

    Args:
        csru_cfg(dict): Hawk 寄存器配置

    Returns:
        int: 单个 VC 的 纯 HIST 数据的包个数
    """
    work_mode = csru_cfg["WORK_MODE"]
    h_vld_seg = csru_cfg["H_VLD_SEG"]

    v_pxl_out_num = 6 if csru_cfg["V_PXL_OUT_NUM"] == 1 else 1

    if work_mode == 0:
        PER_VC_PKT_NUM = 8 * (h_vld_seg + 1)
    elif work_mode == 1:
        PER_VC_PKT_NUM = 8 * (h_vld_seg + 1)
    elif work_mode == 2:
        PER_VC_PKT_NUM = (v_pxl_out_num * 2 * (h_vld_seg + 1))
    else:
        PER_VC_PKT_NUM = (v_pxl_out_num * 2 * (h_vld_seg + 1))
    return PER_VC_PKT_NUM


def print_c(data, color=32):
    """
    颜色样式打印输出功能
    Args:
        data(str): 需要打印的内容
        color(int or str): 指定的颜色, 默认为绿色(32)
            字体色   背景色	颜色描述
            30 	    40	    黑色
            31	    41	    红色
            32	    42	    绿色
            33	    43	    黃色
            34	    44	    蓝色
            35	    45	    紫红色
            36	    46	    青蓝色
            37	    47	    灰色
            38	    38	    白色

    Returns:
        None
    """
    if isinstance(color, int):
        color = str(color)
    elif isinstance(color, str):
        color = 30 if color == "black" \
            else 31 if color == "red" \
            else 32 if color == "green" \
            else 33 if color == "yellow" \
            else 34 if color == "blue" \
            else 35 if color == "magenta" \
            else 36 if color == "cyan" \
            else 37 if color == "gray" \
            else 38 if color == "white" \
            else 32
    else:
        color = 32
    print(f"\033[1;{color}m{data}\033[0m")


def OnceHistReadAddTxdlyCycCalForFHR(csru_cfg: dict):
    """
    计算 WORK_MODE = FHR, 单次 HIST读 + TXDLY 的实际时间

    Args:
        csru_cfg(dict): Hawk 寄存器配置

    Returns:
        list: (unit: cyc)
        基于 RTL 设计, GROUP 0~3, HIST->TXU 的路径延时相同, 为了与 PHR 计算逻辑保持一致, 同样返回 16 个 seg 的数据
    分别计算的时间
    """
    RD_OUT_MIN_GAP = 17

    mipi_pktdly = csru_cfg["MIPI_PKTDLY"]
    maxbin_thrs = csru_cfg["MAXBIN_THRS"]
    minbin_thrs = csru_cfg["MINBIN_THRS"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1

    hist_rd_cyc = ((maxbin_thrs + 1) * 2 - minbin_thrs) * 2

    # 基于 RTL 设计, 4 次 HIST 读组成一个包
    rd_out_ind_cyc = (hist_rd_cyc + 7) * 4 + (1 * 3)  # 4 次 HIST 读, 多 3 拍间隔

    hist_once_read_min_cyc = rd_out_ind_cyc + RD_OUT_MIN_GAP

    # ////////////////////////////////////////////////
    # mipi_txdly 使用 1M 的时钟, 需要用 sysclk1m_div 进行 cycle 计算
    # ////////////////////////////////////////////////
    if mipi_pktdly > 0:
        # 若 1M 时钟不是严格的 1us, 则此值可以理解为针对 1M 分频时钟的次数
        rd_out_ind_us_ave = hist_once_read_min_cyc // sysclk1m_div  # unit: us
        rd_out_ind_us_res = hist_once_read_min_cyc % sysclk1m_div  # unit: cycle
        once_hist_rd_add_txdly_cyc = (rd_out_ind_us_ave + mipi_pktdly) * sysclk1m_div
    else:
        once_hist_rd_add_txdly_cyc = hist_once_read_min_cyc

    once_hist_rd_add_txdly_Q = [(once_hist_rd_add_txdly_cyc, rd_out_ind_cyc) for _ in range(16)]
    return once_hist_rd_add_txdly_Q


def OnceHistReadAddTxdlyCycCalForPHR(csru_cfg: dict):
    """
    计算 WORK_MODE = PHR, 单次 HIST读 + TXDLY 的实际时间

    Args:
        csru_cfg(dict): Hawk 寄存器配置

    Returns:
        list: (unit: cyc)
        基于 RTL 设计, GROUP 0~3(分别对应Seg0~3, 4~7, 8~11, 12~15), HIST->DSP 路径延时逐步递减, 返回时按照 16个 seg 进行返回, 便于后续的数据计算
    分别计算的时间
    """
    hist2dsp_path_dly_cyc = 13
    dsp_mf_cal_cyc = 13
    dsp2txu_path_dly_cyc = 14
    txu2sysc_path_dly_cyc = 1
    RD_OUT_MIN_GAP = 17

    mipi_pktdly = csru_cfg["MIPI_PKTDLY"]
    maxbin_thrs = csru_cfg["MAXBIN_THRS"]
    minbin_thrs = csru_cfg["MINBIN_THRS"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1

    WC, FLNR = CalMipiFlnrAndWC(csru_cfg)

    hist_rd_cyc = ((maxbin_thrs + 1) * 2 - minbin_thrs) * 2
    txu_rd_cyc = int(WC / 1.5)

    # 四个 group, 每个 group 的 dly 不一样
    once_hist_rd_add_txdly_Q = []
    for group_cnt in range(0, 4):
        # 基于 RTL 设计, GROUP 0~3, HIST->DSP 路径延时逐步递减
        rd_out_ind_cyc = ((hist2dsp_path_dly_cyc - group_cnt) + hist_rd_cyc + dsp_mf_cal_cyc +
                          dsp2txu_path_dly_cyc + txu_rd_cyc + txu2sysc_path_dly_cyc)

        hist_once_read_min_cyc = rd_out_ind_cyc + RD_OUT_MIN_GAP

        # ////////////////////////////////////////////////
        # mipi_txdly 使用 1M 的时钟, 需要用 sysclk1m_div 进行 cycle 计算
        # ////////////////////////////////////////////////
        if mipi_pktdly > 0:
            # 若 1M 时钟不是严格的 1us, 则此值可以理解为针对 1M 分频时钟的次数
            rd_out_ind_us_ave = hist_once_read_min_cyc // sysclk1m_div  # unit: us
            rd_out_ind_us_res = hist_once_read_min_cyc % sysclk1m_div  # unit: cycle
            once_hist_rd_add_txdly_cyc = (rd_out_ind_us_ave + mipi_pktdly) * sysclk1m_div
        else:
            once_hist_rd_add_txdly_cyc = hist_once_read_min_cyc
        once_hist_rd_add_txdly_Q.extend([(once_hist_rd_add_txdly_cyc, rd_out_ind_cyc) for _ in range(4)])

    return once_hist_rd_add_txdly_Q


def T_mipi_read_time_cal(csru_cfg: dict, mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500):
    """
    计算单次 HIST 读 MIPI 的读出时间(VC0 + VC1 两个包传输的时间) 以及 generic_data MIPI 的读出时间

    Args:
        csru_cfg(dict): Hawk 寄存器配置
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane

    Returns:
        tuple: (unit: cyc)
    """
    tx_frm_mode = csru_cfg["TX_FRM_MODE"]
    one_dt_mode = csru_cfg["ONE_DT_MODE"]

    mipi_rate = MIPI_RATE * MIPI_LANE_NUM  # unit: bit/us
    WC, FLNR = CalMipiFlnrAndWC(csru_cfg)

    MIPI_PKT_INTV = MipiPKGIntvCal(mipi_cfg, SYS_CLK, MIPI_RATE)  # unit: ns
    MIPIPKT_Tx_HS_Data = (MIPI_LANE_NUM + 4 + WC + 2) * 8 * 1000 / mipi_rate  # unit: ns
    GENERIC_TX_HS_Data = (MIPI_LANE_NUM + 4 + 40 + 2) * 8 * 1000 / mipi_rate if one_dt_mode == 0 \
        else MIPIPKT_Tx_HS_Data  # unit: ns

    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPIPKT_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)
    T_GenericDataMipiReadTime = (MIPI_PKT_INTV + GENERIC_TX_HS_Data) * 2  # if tx_frm_mode == 0 else 0 (tx_frame_mode == 1仍然存在 info 数据)

    once_hist_rd_mipi_read_cyc = int(T_OneHistReadMipiReadTime * SYS_CLK / 1000) + 1
    generic_data_mipi_read_cyc = int(T_GenericDataMipiReadTime * SYS_CLK / 1000) + 1
    return once_hist_rd_mipi_read_cyc, generic_data_mipi_read_cyc


if __name__ == "__main__":
    pass

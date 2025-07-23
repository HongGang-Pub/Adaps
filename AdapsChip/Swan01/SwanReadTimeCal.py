#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : common.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    :

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025-07-04 18:08    honggang_li    v1.0        增加 Swan slot time 计算功能, 提供给外部使用

=================================================================================================
"""

import math

TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 330: 16, 400: 20}


def MIPI_CONFIG_Cal(SYS_CLK=330, MIPI_RATE=1500):
    """
    MIPI 满足 DPHY 协议的时序要求时, DPHY 寄存器相关配置自动计算脚本

    Args:
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane

    Returns:
        MIPI DPYH 寄存器配置值
    """
    TxEscClkDiv = TxEscClkDiv_Q[SYS_CLK]
    TXHSByteClkDiv = 8

    F_TxClkEsc = SYS_CLK / (TxEscClkDiv+1)
    F_TxByteClkHS = MIPI_RATE / TXHSByteClkDiv

    T_TXClkEsc = 1000 / F_TxClkEsc
    T_TxByteClkHS = 1000 / F_TxByteClkHS
    UI = 1000 / MIPI_RATE

    # 标准的时序要求持续时间
    T_std_lp_01 = T_TXClkEsc * 2
    T_std_hs_exit = 100
    T_std_hs_prepare = 40 + 4*UI
    T_std_hs_pre_zero = 145 + 10*UI
    T_std_hs_trail = 60 + 4*UI
    T_std_all_accu = T_std_lp_01 + T_std_hs_exit + T_std_hs_pre_zero + T_std_hs_trail

    # MIPI 寄存器默认配置值的时间计算
    T_default_lp_01 = T_TXClkEsc * 2
    T_default_hs_exit = 2 * T_TXClkEsc
    T_default_hs_prepare = 0 * T_TXClkEsc
    T_default_hs_pre_zero = T_default_hs_prepare + 50 * T_TxByteClkHS
    T_default_hs_trail = 17 * T_TxByteClkHS
    T_default_all_aacu = T_default_lp_01 + T_default_hs_exit + T_default_hs_pre_zero + T_default_hs_trail

    # 在满足 MIPI 时序要求的情况下, 计算包间隔最小的 MIPI 配置
    T_hs_prepare_config = int(T_std_hs_prepare // T_TXClkEsc + (1 if T_std_hs_prepare % T_TXClkEsc > 0 else 0)-1)
    T_hs_zero = T_std_hs_pre_zero - (T_hs_prepare_config+1) * T_TXClkEsc
    T_hs_zero_config = int(T_hs_zero // T_TxByteClkHS + (1 if T_hs_zero % T_TxByteClkHS > 0 else 0))

    T_hs_trail_config = int(T_std_hs_trail // T_TxByteClkHS + (1 if T_std_hs_trail % T_TxByteClkHS > 0 else 0))
    T_hs_exit_config = int(T_std_hs_exit // T_TXClkEsc + (1 if T_std_hs_exit % T_TXClkEsc > 0 else 0))

    # 计算最小配置下 MIPI 耗时
    T_lp_01 = T_TXClkEsc * 2
    T_hs_exit = T_hs_exit_config * T_TXClkEsc
    T_hs_prepare = T_hs_prepare_config * T_TXClkEsc
    T_hs_pre_zero = T_hs_prepare + T_hs_zero_config * T_TxByteClkHS
    T_hs_trail = T_hs_trail_config * T_TxByteClkHS
    T_all_aacu = T_lp_01 + T_hs_exit + T_hs_pre_zero + T_hs_trail

    # print(f"SYS_CLK: {SYS_CLK}MHz, MIPI_RATE: {MIPI_RATE} Gbps/Lane, F_TxClkEsc: {F_TxClkEsc:5.2f} MHz, F_TxByteClkHS: {F_TxByteClkHS:5.2f}MHz:")
    # print(f"\tItem                : CONFIG |  T_cal |  T_std | T_default")
    # print(f"\tT_lpx               : {2:4}   | {T_lp_01:6.2f} | {T_std_lp_01:6.2f} | {T_default_lp_01:6.2f}")
    # print(f"\tT_hs_exit    ('d43) : {T_hs_exit_config:4}   | {T_hs_exit:6.2f} | {T_std_hs_exit:6.2f} | {T_default_hs_exit:6.2f}")
    # print(f"\tT_hs_prepare ('d44) : {T_hs_prepare_config:4}   | {T_hs_prepare:6.2f} | {T_std_hs_prepare:6.2f} | {T_default_hs_prepare:6.2f}")
    # print(f"\tT_hs_pre_zero('d45) : {T_hs_zero_config:4}   | {T_hs_pre_zero:6.2f} | {T_std_hs_pre_zero:6.2f} | {T_default_hs_pre_zero:6.2f}")
    # print(f"\tT_hs_trail   ('d46) : {T_hs_trail_config:4}   | {T_hs_trail:6.2f} | {T_std_hs_trail:6.2f} | {T_default_hs_trail:6.2f}")
    # print(f"\tT_all_aacu          : {'':5}  | {T_all_aacu:6.2f} | {T_std_all_accu:6.2f} | {T_default_all_aacu:6.2f}")
    # print(f"\tTime saving @default:  {T_default_all_aacu-T_all_aacu:6.2f} ns\n")
    mipi_cfg = {
        "DataTxThslpxcnt": 2,
        "DataTxThsexitCnt": T_hs_exit_config,
        "DataTxThsprepareCnt": T_hs_prepare_config,
        "DataTxThszeroCnt": T_hs_zero_config,
        "DataTxThstrailCnt": T_hs_trail_config,
    }
    return mipi_cfg


def MipiPKGIntvCal(mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500):
    """
    MIPI 包间协议开销计算

    Args:
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane

    Returns:
        float: MIPI 包间协议开销 (unit: ns)
    """

    TXHSByteClkDiv = 8
    T_TxClkEsc = 1000 / (SYS_CLK / (TxEscClkDiv_Q[SYS_CLK] + 1))
    T_TxByteClkHS = 1000 / (MIPI_RATE / TXHSByteClkDiv)

    DataTxThslpxcnt = mipi_cfg["DataTxThslpxcnt"]
    DataTxThsexitCnt = mipi_cfg["DataTxThsexitCnt"]
    DataTxThsprepareCnt = mipi_cfg["DataTxThsprepareCnt"]
    DataTxThszeroCnt = mipi_cfg["DataTxThszeroCnt"]
    DataTxThstrailCnt = mipi_cfg["DataTxThstrailCnt"]

    MIPI_PKT_INTV = ((120 if DataTxThsexitCnt == 0 else (320 if MIPI_RATE == 1500 else 360)) +
                     T_TxClkEsc * DataTxThslpxcnt +
                     T_TxClkEsc * (DataTxThsprepareCnt + 1) +
                     T_TxByteClkHS * (DataTxThszeroCnt + 4) +
                     T_TxByteClkHS * (DataTxThstrailCnt + 1)
                     )
    # print(T_TxClkEsc * DataTxThslpxcnt)
    # print(T_TxClkEsc * (DataTxThsprepareCnt + 1))
    # print(T_TxByteClkHS * (DataTxThszeroCnt + 4))
    # print(T_TxByteClkHS * (DataTxThstrailCnt + 1))
    # s = "======================================="
    # s += f"\nSYS_CLK       : {SYS_CLK:>8} M"
    # s += f"\nMIPI_RATE     : {MIPI_RATE:>8} Gbps/Lane"
    # s += f"\nT_TxClkEsc    : {T_TxClkEsc:>8.2f} ns"
    # s += f"\nT_TxByteClkHS : {T_TxByteClkHS:>8.2f} ns"
    # s += f"\nMIPI_PKT_INTV : {MIPI_PKT_INTV:>8.2f} ns"
    # print_c(s)
    return MIPI_PKT_INTV


def SwanDataflowConfigCal(csru_cfg: dict) -> dict:
    """
    计算 MIPI dataflow 相关参数
    Args:
        csru_cfg (dict): Swan 相关的寄存器配置信息

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
    seg_num = csru_cfg["SEG_NUM"]  # TODO: 需要确认, 有可能需要特殊处理, 寄存器无此配置
    fwhm_search_num = csru_cfg["FWHM_SEARCH_NUM"]

    # MIPI_CFG = csru_cfg["MIPI"]

    DataflowConfig = {
        "mipi_pktdly1_cyc": 0,  # DSP DLY: 16 bit (unit: cycle)
        "mipi_pktdly2_cyc": 0,  # HIST DLY: 实际值=配置值*16， 16 bit (unit: cycle)
        "mipi_pktdly3_cyc": 0,  # HIST DLY: 用于调节 第一次 HIST 和 第二次 HIST 之间的 delay, 16 bit (unit: cycle) 
        "mipi_fsdly_cyc": 0,    # FS DLY: 调节 FS 和 generic data 之间的间隔, 10 bit (unit: cycle)
        "mipi_fenddly": 0,      # 8 bit (unit: 10us)
        "mipi_pkt_pl_num": 0,   # 16 bit
        "threshold_value": 0,   # 8 bit
        "WC": 0,  # 16 bit
        "FLNR": 0,  # 16 bit
        "hist_read_out_cyc": 0,  # 非寄存器配置值, 此值对应 数据读出所需要的完整时间
    }

    if work_mode == 3:  # TODO: PCM 模式后续补充
        return DataflowConfig

    # //////////////////////////////////////////////////////////
    # 部分 DLY 参数设置 or 获取
    # //////////////////////////////////////////////////////////
    T1 = 13  # T_DSP_FIR_INIT
    T2 = 14  # SYSC hist_rd_out_ind to DSP path delay
    T3 = 2  # SYSC dsp_rd_out_ind to DSP path delay

    # TODO: 需要根据传参处理
    MIPI_PKT_INTV = 0.9  # MIPI 1.5Gbps config (unit: us)
    MIPI_FIFO_SIZE = 960  # MIPI FIFO: DEPTH = 1024, WIDTH = 32
    PKT_DLY_MARGIN = 0  # 额外的 cycle 开销

    # //////////////////////////////////////////////////////////
    #  此处计算 MIPI 极限优化时的 MIPI 包间间隔
    # //////////////////////////////////////////////////////////
    mipi_cfg = MIPI_CONFIG_Cal(SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)
    MIPI_PKT_INTV = MipiPKGIntvCal(mipi_cfg=mipi_cfg, SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)
    MIPI_PKT_INTV = MIPI_PKT_INTV / 1000    # unit: ns -> us
    # print(f"MIPI_PKT_INTV: {MIPI_PKT_INTV} us")

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
    # 处理寄存器配置特殊情况
    # //////////////////////////////////////////////////////////
    out_echo_num = 5 if out_echo_num > 5 else out_echo_num  # 最大输出 6 echo (配置值+1) 
    pxl_binn_sel = 0 if pxl_binn_sel > 2 else pxl_binn_sel  # 当 pxl_binn_sel == 2 时, 一个 segment 为 16pxl

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
    # Pixel Pack 相关计算
    # //////////////////////////////////////////////////////////
    # 计算一个 Packet 包含多少 Pixel
    # 1. work_mode == PCM: 一次读出全部的 Pixel 数据
    # 2. work_mode != PCM: 仅与 pack 配置相关
    one_pkt_pxl_num = 48 * seg_num if work_mode == 3 else \
        1 if pack_2pxl_en == 0 else \
        2 if pack_4pxl_en == 0 else \
        4 if pack_8pxl_en == 0 else \
        8 if pack_16pxl_en == 0 else \
        16 * (pack_16pxl_num + 1)

    # 计算一个 slot, pixel binning 后, 有多少个 Pixel 需要读出
    pxl_num_after_binn = 48 * seg_num if work_mode == 3 else (16 >> pxl_binn_sel) * seg_num
    # 计算一个 slot, 有多少个 Pixel 包需要发送
    one_slot_pxl_pkt_num = pxl_num_after_binn / one_pkt_pxl_num

    # 计算不同 work_mode 下, txu 发送单个 pixel 数据的 cycle 数
    # SPHR
    if work_mode == 0:
        match data_width_sel:
            case 0:
                rd_cyc_dsp_1pxl = (4 + 14 * (out_echo_num + 1)) / 2
            case 1:
                rd_cyc_dsp_1pxl = (4 + 12 * (out_echo_num + 1)) / 2
            case _:
                rd_cyc_dsp_1pxl = (4 + 14 * (out_echo_num + 1)) / 2
    # PHR
    elif work_mode == 1:
        match out_numbin_mode:
            case 0:
                rd_cyc_dsp_1pxl = (4 + out_totalbin_num * 2) / 2
            case 1:
                rd_cyc_dsp_1pxl = (4 + (out_echo_num + 1) * (out_echobin_num * 2)) / 2
            case _:
                rd_cyc_dsp_1pxl = (4 + out_totalbin_num * 2) / 2
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

    wc = one_pkt_dsp_rd_cyc * 2 * wc_factor  # Q1: Why * 2 ? A1: TXU is dual pixel mode
    flnr = (int(pxl_num_after_binn / one_pkt_pxl_num) + one_dt_mode) * slot_num_in_img_frm

    if wc > 0xFFFF:
        raise ValueError(
            f"wc[16:0] config out of bound, it's need to be config {wc}, please check your binning config.")
    if flnr > 0x1FFF:
        raise ValueError(f"flnr[12:0] config out of bound, it's need to be config {flnr}, "
                         f"please reconfigure your data transfer control.")
    DataflowConfig["WC"] = wc
    DataflowConfig["FLNR"] = flnr
    DataflowConfig["mipi_pkt_pl_num"] = wc / wc_factor

    # //////////////////////////////////////////////////////////
    # Cycle 计算
    # //////////////////////////////////////////////////////////
    # 发起一次 HIST read cycle 数
    rd_cyc_hist_1pxl = ((hist_maxbin_thrs - hist_minbin_thrs + 1) * 8) >> bin_widht_sel
    rd_cyc_once_hist_par = rd_cyc_hist_1pxl

    # generic data read cycle
    txu_info_ptk_rd_cyc = one_pkt_dsp_rd_cyc if one_dt_mode == 1 else ((38 + 22 * 4 + 8 + 16) / 2 + rd_cyc_crc32)

    # MIPI 包间间隔 cycle 数
    mipi_pkt_intv_cyc = math.ceil(MIPI_PKT_INTV * SYS_CLK)
    mipi_fsdly_cyc = mipi_pkt_intv_cyc
    if mipi_fsdly_cyc > 0x3FF:
        raise ValueError(f"mipi_fsdly_cyc[9:0] config out of bound, it's need to be config {mipi_fsdly_cyc}")
    DataflowConfig["mipi_fsdly_cyc"] = mipi_fsdly_cyc

    if work_mode == 3:
        mipi_fsdly_cyc = 0
        mipi_pktdly1_cyc = 1
        hist_read_out_cyc = mipi_fsdly_cyc + txu_info_ptk_rd_cyc + one_pkt_dsp_rd_cyc + mipi_pktdly1_cyc + 30
        DataflowConfig["mipi_pktdly1_cyc"] = mipi_pktdly1_cyc
        DataflowConfig["mipi_fsdly_cyc"] = mipi_fsdly_cyc
        DataflowConfig["hist_read_out_cyc"] = hist_read_out_cyc
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
    if pxl_binn_sel == 0 and seg_num % 16 != 0:
        raise ValueError(f"SEG_NUM = {seg_num}, PXL_BINN_SEL = {pxl_binn_sel}")
    elif pxl_binn_sel == 1 and seg_num % 8 != 0:
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
    DataflowConfig["mipi_pktdly3_cyc"] = mipi_pktdly3_cyc

    # ----------------------------------------------------------
    # 计算第一次 HIST 读, 实际可以释放的给上一次数据传输的时间
    # ----------------------------------------------------------
    # TODO: 这里需要考虑是否做极限帧率的处理
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
    DataflowConfig["mipi_pktdly1_cyc"] = mipi_pktdly1_cyc

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
    DataflowConfig["mipi_pktdly2_cyc"] = mipi_pktdly2_cyc

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
    # TODO: 在进行极限帧率计算时, if (TX_FRM_MODE=1), 由于配置的 DLY 以 slot 为单位进行计算, img_frm 的 FS 和 FE 没有进行考虑, 因此需要在 frm_idletime 上进行补偿
    DataflowConfig["frm_idletime"] = math.ceil(MIPI_PKT_INTV * 2)
    return DataflowConfig


if __name__ == '__main__':
    SYS_CLK = 400  # 系统时钟(unit: MHz)
    TDC_CLK = 250  # TDC 时钟(unit: MHz)
    MIPI_RATE = 1500  # MIPI 1.5Gbps
    MIPI_LANE_NUM = 4  # MIPI 4 lane
    chip_cfg = {
        "WORK_MODE": 1,
        "TX_FRM_MODE": 0,
        "HIST_MINBIN_THRS": 0,
        "HIST_MAXBIN_THRS": 255,
        "DATA_WIDTH_SEL": 0,
        "FRM_SLOT_NUM": 0,
        "PACK_16PXL_NUM": 3,
        "PACK_16PXL_EN": 1,
        "PACK_8PXL_EN": 1,
        "PACK_4PXL_EN": 1,
        "PACK_2PXL_EN": 1,
        "PXL_BINN_SEL": 2,
        "BIN_WIDTH_SEL": 1,
        "OUT_TOTALBIN_NUM": 0x90,
        "OUT_ECHOBIN_NUM": 0x22,
        "OUT_NUMBIN_MODE": 1,
        "OUT_ECHO_NUM": 4,
        "ONE_DT_MODE": 1,
        "PKT_CHKSUM_EN": 0,
        "SEG_NUM": 16,
        "FWHM_SEARCH_NUM": 15,
    }

    txdlycfg = SwanDataflowConfigCal(chip_cfg)
    hist_read_out_cyc = txdlycfg["hist_read_out_cyc"]
    hist_read_out_us = hist_read_out_cyc / SYS_CLK
    print(f"ReadTime: {hist_read_out_us} us")

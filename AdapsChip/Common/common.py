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
2025-07-04 18:08    honggang_li    v1.0        

=================================================================================================
=================================================================================================
"""
import logging
import math
import os
from SelfDefinedPackge import PubMethod

TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 330: 16, 400: 20}


def MipiPKGIntvCal(mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500, TxEscClkDiv=None, clock_mode=1):
    """
    MIPI 包间协议开销计算(适用于 MIPI IP 最高支持 1.5Gbps/Lane)

    Args:
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane
        TxEscClkDiv: TxEscClk 分频, 与 MIPI 相关
        clock_mode: MIPI 非连续时钟模式。0: 非连续时钟，1: 连续时钟。

    Returns:
        float: MIPI 包间协议开销 (unit: ns)
    """

    TXHSByteClkDiv = 8
    TxEscClkDiv = TxEscClkDiv_Q[SYS_CLK] if TxEscClkDiv is None else TxEscClkDiv
    T_TxClkEsc = 1000 / (SYS_CLK / (TxEscClkDiv + 1))
    T_TxByteClkHS = 1000 / (MIPI_RATE / TXHSByteClkDiv)

    DataTxThslpxcnt = mipi_cfg["DataTxThslpxcnt"]
    DataTxThsexitCnt = mipi_cfg["DataTxThsexitCnt"]
    DataTxThsprepareCnt = mipi_cfg["DataTxThsprepareCnt"]
    DataTxThszeroCnt = mipi_cfg["DataTxThszeroCnt"]
    DataTxThstrailCnt = mipi_cfg["DataTxThstrailCnt"]

    if clock_mode == 1:
        MIPI_PKT_INTV = ((120 if DataTxThsexitCnt == 0 else (320 if MIPI_RATE == 1500 else 360)) +
                         T_TxClkEsc * DataTxThslpxcnt +
                         T_TxClkEsc * (DataTxThsprepareCnt + 1) +
                         T_TxByteClkHS * (DataTxThszeroCnt + 4) +
                         T_TxByteClkHS * (DataTxThstrailCnt + 1)
                         )
    else:
        T_clk_intv = (mipi_cfg["ClockLaneWaitCnt"] + mipi_cfg["ClockLaneTrailCnt"] + mipi_cfg["DataLaneWaitCnt"] + 3) * T_TxByteClkHS

        T_hs_mipi_pkt_intv_pre = (100 +                                     # DataTxRequestHS-> DPHY LPX
                                  T_TxClkEsc * DataTxThslpxcnt +            # LPX
                                  T_TxClkEsc * (DataTxThsprepareCnt + 1) +  # Prepare
                                  T_TxByteClkHS * (DataTxThszeroCnt + 4))   # HS-Zero

        MIPI_PKT_INTV = T_clk_intv + T_hs_mipi_pkt_intv_pre + 100           # Margin

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
    MIPI_PKT_INTV = math.ceil(MIPI_PKT_INTV)
    return MIPI_PKT_INTV


def MIPI_CONFIG_Cal(SYS_CLK=330, MIPI_RATE=1500, clock_mode=1, display=True):
    """
    MIPI 满足 DPHY 协议的时序要求时, DPHY 寄存器相关配置自动计算脚本(适用于 MIPI IP 最高支持 1.5Gbps/Lane)

    Args:
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane
        clock_mode: MIPI 非连续时钟模式。0: 非连续时钟，1: 连续时钟。
        display(bool): 是否打印配置信息

    Returns:
        MIPI DPYH 寄存器配置值
    """
    mipi_cfg = {
        "ClkTxThslpxcnt": 0x02,             # TXClkEsc
        "ClkTxThsprepareCnt": 0x00,         # TXClkEsc: config+1    // DPHY no CLK config
        "ClkTxThszeroCnt": 0x3C,            # TxByteClk
        "ClkTxHsPostCnt": 0x11,             # TxByteClk
        "ClkTxThstrailCnt": 0x0F,           # TxByteClk
        "ClkTxThsexitCnt": 0x02,            # TXClkEsc

        "DataTxThslpxcnt": 0x02,            # TXClkEsc
        "DataTxThsprepareCnt": 0x00,        # TXClkEsc
        "DataTxThszeroCnt": 0x32,           # TxByteClk
        "DataTxThstrailCnt": 0x11,          # TxByteClk
        "DataTxThsexitCnt": 0x02,           # T_TXClkEsc

        "ClockLaneWaitCnt": 0x10,           # TxByteClk
        "ClockLaneTrailCnt": 0x10,          # TxByteClk
        "DataLaneWaitCnt": 0x24,            # TxByteClk
    }

    TxEscClkDiv = TxEscClkDiv_Q[SYS_CLK]
    TXHSByteClkDiv = 8

    F_TxClkEsc = SYS_CLK / (TxEscClkDiv+1)
    F_TxByteClkHS = MIPI_RATE / TXHSByteClkDiv

    T_TXClkEsc = 1000 / F_TxClkEsc
    T_TxByteClkHS = 1000 / F_TxByteClkHS
    UI = 1000 / MIPI_RATE

    # ///////////////////////////////////////////////////////////////////////
    # For the Data Lane config calculate
    # ///////////////////////////////////////////////////////////////////////
    # 标准的时序要求持续时间
    T_std_hs_lpx      = T_TXClkEsc * 2
    T_std_hs_prepare  = 40 + 4*UI
    T_std_hs_pre_zero = 145 + 10*UI
    T_std_hs_trail    = 60 + 4*UI
    T_std_hs_exit     = 100
    T_std_hs_all_accu    = T_std_hs_lpx + T_std_hs_exit + T_std_hs_pre_zero + T_std_hs_trail

    # MIPI 寄存器默认配置值的时间计算
    T_default_hs_lpx     = mipi_cfg["DataTxThslpxcnt"] * T_TXClkEsc
    T_default_hs_prepare = (mipi_cfg["DataTxThsprepareCnt"] + 1) * T_TXClkEsc
    T_default_hs_zero    = mipi_cfg["DataTxThszeroCnt"] * T_TxByteClkHS
    T_default_hs_trail   = mipi_cfg["DataTxThstrailCnt"] * T_TxByteClkHS
    T_default_hs_exit    = mipi_cfg["DataTxThsexitCnt"] * T_TXClkEsc
    T_default_hs_all_accu   = T_default_hs_lpx + T_default_hs_exit + T_default_hs_zero + T_default_hs_trail

    # 在满足 MIPI 时序要求的情况下, 计算包间隔最小的 MIPI 配置
    T_hs_prepare_config = int(T_std_hs_prepare // T_TXClkEsc + (1 if T_std_hs_prepare % T_TXClkEsc > 0 else 0)-1)  # 实际值=配置值+1
    T_hs_zero = T_std_hs_pre_zero - (T_hs_prepare_config+1) * T_TXClkEsc
    T_hs_zero_config = int(T_hs_zero // T_TxByteClkHS + (1 if T_hs_zero % T_TxByteClkHS > 0 else 0))

    T_hs_trail_config = int(T_std_hs_trail // T_TxByteClkHS + (1 if T_std_hs_trail % T_TxByteClkHS > 0 else 0))
    T_hs_exit_config = int(T_std_hs_exit // T_TXClkEsc + (1 if T_std_hs_exit % T_TXClkEsc > 0 else 0))

    mipi_cfg["DataTxThsprepareCnt"] = T_hs_prepare_config
    mipi_cfg["DataTxThszeroCnt"]    = T_hs_zero_config
    mipi_cfg["DataTxThstrailCnt"]   = T_hs_trail_config
    mipi_cfg["DataTxThsexitCnt"]    = T_hs_exit_config

    # 计算实际配置下 Data Lane MIPI 耗时
    T_hs_lpx     = mipi_cfg["DataTxThslpxcnt"] * T_TXClkEsc
    T_hs_prepare = (mipi_cfg["DataTxThsprepareCnt"] + 1) * T_TXClkEsc
    T_hs_zero    = mipi_cfg["DataTxThszeroCnt"] * T_TxByteClkHS
    T_hs_trail   = mipi_cfg["DataTxThstrailCnt"] * T_TxByteClkHS
    T_hs_exit    = mipi_cfg["DataTxThsexitCnt"] * T_TXClkEsc
    T_all_accu   = T_hs_lpx + T_hs_exit + T_hs_prepare + T_hs_zero + T_hs_trail
    T_datalane_LP2HS = T_hs_lpx + T_hs_prepare + T_hs_zero

    # ///////////////////////////////////////////////////////////////////////
    # For the non-continuous clock mode, Clock lane config calculate
    # ///////////////////////////////////////////////////////////////////////
    # 标准的时序要求持续时间
    T_std_clock_lpx      = T_TXClkEsc * 2
    T_std_clock_prepare  = 38
    T_std_clock_pre_zero = 300
    T_std_clock_post     = 60 + 52*UI
    T_std_clock_trail    = 60
    T_std_clock_exit     = 100

    # 在满足 MIPI 时序要求的情况下, 计算包间隔最小的 MIPI 配置
    # T_clock_prepare_config = int(T_std_clock_prepare // T_TXClkEsc + (1 if T_std_clock_prepare % T_TXClkEsc > 0 else 0)-1)  # 实际值=配置值+1
    T_clock_prepare_config = 0  # 实际值=配置值+1
    T_clock_zero = T_std_clock_pre_zero - (T_clock_prepare_config+1) * T_TXClkEsc
    T_clock_zero_config = int(T_clock_zero // T_TxByteClkHS + (1 if T_clock_zero % T_TxByteClkHS > 0 else 0))

    T_clock_post_config = int(T_std_clock_post // T_TxByteClkHS + (1 if T_std_clock_post % T_TxByteClkHS > 0 else 0))
    T_clock_trail_config = int(T_std_clock_trail // T_TxByteClkHS + (1 if T_std_clock_trail % T_TxByteClkHS > 0 else 0))
    T_clock_exit_config = int(T_std_clock_exit // T_TXClkEsc + (1 if T_std_clock_exit % T_TXClkEsc > 0 else 0))

    if clock_mode == 0:
        mipi_cfg["ClkTxThsprepareCnt"] = 0
        mipi_cfg["ClkTxThszeroCnt"]    = T_clock_zero_config
        mipi_cfg["ClkTxHsPostCnt"]     = T_clock_post_config
        mipi_cfg["ClkTxThstrailCnt"]   = T_clock_trail_config
        mipi_cfg["ClkTxThsexitCnt"]    = T_clock_exit_config

    # 计算实际配置下 Clock Lane MIPI 耗时
    T_clk_lpx     = mipi_cfg["ClkTxThslpxcnt"] * T_TXClkEsc
    T_clk_prepare = (mipi_cfg["ClkTxThsprepareCnt"] + 1) * T_TXClkEsc
    T_clk_zero    = mipi_cfg["ClkTxThszeroCnt"] * T_TxByteClkHS
    T_clk_post    = mipi_cfg["ClkTxHsPostCnt"] * T_TxByteClkHS
    T_clk_trail   = mipi_cfg["ClkTxThstrailCnt"] * T_TxByteClkHS
    T_clk_exit    = 300  # mipi_cfg["ClkTxThsexitCnt"] * T_TXClkEsc

    T_std_clw = T_clk_trail + T_hs_exit
    T_std_clt = T_hs_trail + T_clk_post
    T_std_dlw = T_clk_lpx + T_clk_prepare + T_clk_zero + max(0, T_clk_exit - T_datalane_LP2HS)

    T_clwr_config = int(T_std_clw // T_TxByteClkHS + (1 if T_std_clw % T_TxByteClkHS > 0 else 0) - 1)
    T_cltr_config = int(T_std_clt // T_TxByteClkHS + (1 if T_std_clt % T_TxByteClkHS > 0 else 0) - 1)
    T_dlwr_config = int(T_std_dlw // T_TxByteClkHS + (1 if T_std_dlw % T_TxByteClkHS > 0 else 0) - 1)

    if T_clwr_config > 0x3F:
        logging.warning(f"MIPI CSI T_clwr_config ({T_clwr_config}) is out of range (0x3F)")
        T_clwr_config = 0x3F

    if T_cltr_config > 0x3F:
        logging.warning(f"MIPI CSI T_cltr_config ({T_cltr_config}) is out of range (0x3F)")
        T_cltr_config = 0x3F

    if T_dlwr_config > 0x7F:
        logging.warning(f"MIPI CSI T_dlwr_config ({T_dlwr_config}) is out of range (0x7F)")
        T_dlwr_config = 0x7F

    if clock_mode == 0:
        mipi_cfg["ClockLaneWaitCnt"] = T_clwr_config
        mipi_cfg["ClockLaneTrailCnt"] = T_cltr_config
        mipi_cfg["DataLaneWaitCnt"] = T_dlwr_config

    MIPI_PKT_INTV0 = MipiPKGIntvCal(mipi_cfg, SYS_CLK, MIPI_RATE, clock_mode=1)
    MIPI_PKT_INTV1 = MipiPKGIntvCal(mipi_cfg, SYS_CLK, MIPI_RATE, clock_mode=0)
    s = ""
    s += f"SYS_CLK: {SYS_CLK}MHz, MIPI_RATE: {MIPI_RATE} Gbps/Lane, F_TxClkEsc: {F_TxClkEsc:5.2f} MHz, F_TxByteClkHS: {F_TxByteClkHS:5.2f}MHz:"
    s += f"\n\tItem                : CONFIG |  T_cal |  T_std | T_default"
    s += f"\n\tT_lpx               : {2:4}   | {T_hs_lpx:6.2f} | {T_std_hs_lpx:6.2f} | {T_default_hs_lpx:6.2f}"
    s += f"\n\tT_hs_exit    ('d43) : {T_hs_exit_config:4}   | {T_hs_exit:6.2f} | {T_std_hs_exit:6.2f} | {T_default_hs_exit:6.2f}"
    s += f"\n\tT_hs_prepare ('d44) : {T_hs_prepare_config:4}   | {T_hs_prepare:6.2f} | {T_std_hs_prepare:6.2f} | {T_default_hs_prepare:6.2f}"
    s += f"\n\tT_hs_zero    ('d45) : {T_hs_zero_config:4}   | {T_hs_zero:6.2f} | {T_std_hs_pre_zero:6.2f} | {T_default_hs_zero:6.2f}"
    s += f"\n\tT_hs_trail   ('d46) : {T_hs_trail_config:4}   | {T_hs_trail:6.2f} | {T_std_hs_trail:6.2f} | {T_default_hs_trail:6.2f}"
    s += f"\n\tT_all_aacu          : {'':5}  | {T_all_accu:6.2f} | {T_std_hs_all_accu:6.2f} | {T_default_hs_all_accu:6.2f}"
    s += f"\n\tTime saving @default: {T_default_hs_all_accu - T_all_accu:6.2f} ns"
    s += f"\n\tMIPI_PKT_INTV_CON   : {MIPI_PKT_INTV0} ns"
    s += f"\n\tMIPI_PKT_INTV_NOCON : {MIPI_PKT_INTV1} ns"
    if display:
        print(s)
    return mipi_cfg


def roi_data_save(f_name, data=None, fd_path=".", roi_data_format=1):
    """
    保存 ROI 数据
    Args:
        f_name (str): 文件名称
        data (list): ROI 数据
        fd_path (str): 文件路径
        roi_data_format (int): 0: Byte; 1: Half-word

    Returns:

    """
    if data is None:
        return

    if not os.path.exists(fd_path):
        # 目录不存在，进行创建操作
        os.makedirs(fd_path)  # 使用os.makedirs()方法创建多层目录

    file = "{}\\{}.txt".format(fd_path, f_name)

    with open(file=file, mode="w", encoding="utf-8") as f:
        for i in range(0, len(data)):
            roi_string = '{:0>4X}'.format(data[i])
            if roi_data_format == 1:    # Half-word
                f.write(roi_string)
                if i < (len(data) - 1):
                    f.write('\n')
            else:                       # Byte
                f.write(roi_string[2:4])
                f.write('\n')
                f.write(roi_string[0:2])
                if i < (len(data) - 1):
                    f.write('\n')
    return


def swan01_roi_data_save(f_name, data=None, fd_path=".", roi_data_format=1, roi_info_file=None, start_index=0, group_length=674):
    """
    保存 ROI 数据
    Args:
        f_name (str): 文件名称
        data (list): ROI 数据
        fd_path (str): 文件路径
        roi_data_format (int): 0: Byte; 1: Half-word
        roi_info_file(str): ROI annotate file
        start_index(int): group start index
        group_length (int): swan01 group length

    Returns:
        None
    """
    if data is None:
        return

    if not os.path.exists(fd_path):
        # 目录不存在，进行创建操作
        os.makedirs(fd_path)  # 使用os.makedirs()方法创建多层目录

    file = "{}\\{}.txt".format(fd_path, f_name)
    if roi_info_file is not None:
        roi_info_data = PubMethod.read_file(fname=roi_info_file)

    with open(file=file, mode="w", encoding="utf-8") as f:
        for i in range(0, len(data)):
            roi_string = '{:0>4X}'.format(data[i])
            if roi_info_file is not None:
                roi_info = f" // Group_{start_index+i//group_length}: {roi_info_data[i%group_length]}"
                roi_info = roi_info.replace("\n", "").replace("\r", "")
                roi_string += roi_info
            if roi_data_format == 1:    # Half-word
                f.write(roi_string)
                if i < (len(data) - 1):
                    f.write('\n')
            else:                       # Byte
                f.write(roi_string[2:4])
                f.write('\n')
                f.write(roi_string[0:2])
                if i < (len(data) - 1):
                    f.write('\n')
    return


if __name__ == "__main__":
    mipi_config = MIPI_CONFIG_Cal(SYS_CLK=400, MIPI_RATE=100)
    # mipi_config = MIPI_CONFIG_Cal(SYS_CLK=330, MIPI_RATE=750)
    print(mipi_config)
    pass

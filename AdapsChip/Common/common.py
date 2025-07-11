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
"""
import logging
import math
import os

TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 330: 16, 400: 20}


def MipiPKGIntvCal(mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500, TxEscClkDiv=None):
    """
    MIPI 包间协议开销计算(适用于 MIPI IP 最高支持 1.5Gbps/Lane)

    Args:
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane
        TxEscClkDiv: TxEscClk 分频, 与 MIPI 相关

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
    MIPI_PKT_INTV = math.ceil(MIPI_PKT_INTV)
    return MIPI_PKT_INTV


def MIPI_CONFIG_Cal(SYS_CLK=330, MIPI_RATE=1500, display=True):
    """
    MIPI 满足 DPHY 协议的时序要求时, DPHY 寄存器相关配置自动计算脚本(适用于 MIPI IP 最高支持 1.5Gbps/Lane)

    Args:
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane
        display(bool): 是否打印配置信息

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
    T_hs_prepare_config = int(T_std_hs_prepare // T_TXClkEsc + (1 if T_std_hs_prepare % T_TXClkEsc > 0 else 0)-1)  # 实际值=配置值+1
    T_hs_zero = T_std_hs_pre_zero - (T_hs_prepare_config+1) * T_TXClkEsc
    T_hs_zero_config = int(T_hs_zero // T_TxByteClkHS + (1 if T_hs_zero % T_TxByteClkHS > 0 else 0))

    T_hs_trail_config = int(T_std_hs_trail // T_TxByteClkHS + (1 if T_std_hs_trail % T_TxByteClkHS > 0 else 0))
    T_hs_exit_config = int(T_std_hs_exit // T_TXClkEsc + (1 if T_std_hs_exit % T_TXClkEsc > 0 else 0))

    # 计算最小配置下 MIPI 耗时
    T_lp_01 = T_TXClkEsc * 2
    T_hs_exit = T_hs_exit_config * T_TXClkEsc
    T_hs_prepare = (T_hs_prepare_config + 1) * T_TXClkEsc
    T_hs_pre_zero = T_hs_prepare + T_hs_zero_config * T_TxByteClkHS
    T_hs_trail = T_hs_trail_config * T_TxByteClkHS
    T_all_aacu = T_lp_01 + T_hs_exit + T_hs_pre_zero + T_hs_trail

    mipi_cfg = {
        "DataTxThslpxcnt": 2,
        "DataTxThsexitCnt": T_hs_exit_config,
        "DataTxThsprepareCnt": T_hs_prepare_config,
        "DataTxThszeroCnt": T_hs_zero_config,
        "DataTxThstrailCnt": T_hs_trail_config,
    }
    MIPI_PKT_INTV = MipiPKGIntvCal(mipi_cfg, SYS_CLK, MIPI_RATE)
    s = ""
    s += f"SYS_CLK: {SYS_CLK}MHz, MIPI_RATE: {MIPI_RATE} Gbps/Lane, F_TxClkEsc: {F_TxClkEsc:5.2f} MHz, F_TxByteClkHS: {F_TxByteClkHS:5.2f}MHz:"
    s += f"\n\tItem                : CONFIG |  T_cal |  T_std | T_default"
    s += f"\n\tT_lpx               : {2:4}   | {T_lp_01:6.2f} | {T_std_lp_01:6.2f} | {T_default_lp_01:6.2f}"
    s += f"\n\tT_hs_exit    ('d43) : {T_hs_exit_config:4}   | {T_hs_exit:6.2f} | {T_std_hs_exit:6.2f} | {T_default_hs_exit:6.2f}"
    s += f"\n\tT_hs_prepare ('d44) : {T_hs_prepare_config:4}   | {T_hs_prepare:6.2f} | {T_std_hs_prepare:6.2f} | {T_default_hs_prepare:6.2f}"
    s += f"\n\tT_hs_pre_zero('d45) : {T_hs_zero_config:4}   | {T_hs_pre_zero:6.2f} | {T_std_hs_pre_zero:6.2f} | {T_default_hs_pre_zero:6.2f}"
    s += f"\n\tT_hs_trail   ('d46) : {T_hs_trail_config:4}   | {T_hs_trail:6.2f} | {T_std_hs_trail:6.2f} | {T_default_hs_trail:6.2f}"
    s += f"\n\tT_all_aacu          : {'':5}  | {T_all_aacu:6.2f} | {T_std_all_accu:6.2f} | {T_default_all_aacu:6.2f}"
    s += f"\n\tTime saving @default: {T_default_all_aacu - T_all_aacu:6.2f} ns"
    s += f"\n\tMIPI_PKT_INTV       : {MIPI_PKT_INTV} ns"
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

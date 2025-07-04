#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : HawkConfig.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    : Hawk 相关配置项入口, 搭配其他模块使用

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025-04-24 09:36    honggang_li    v1.0        1. Mipi Rate计算相关配置统一从此处进行获取

=================================================================================================
"""
# ////////////////////////////////////////////////
# 根据配置脚本填写配置值
# 此配置对应的皆是寄存器配置, 可能与实际业务配置有差异
# ////////////////////////////////////////////////
SYS_CLK = 330
MIPI_RATE = 1000

csru_cfg = {
    "WORK_MODE": 1,
    "SCAN_MODE": 1,
    "V_ROLL_NUM": 21,
    "H_ROLL_NUM": 5,
    "H_VLD_SEG": 1,
    "MINBIN_THRS": 0,
    "MAXBIN_THRS": 167,
    "OUT_BIN_NUM": 0,
    "TX_FRM_MODE": 1,
    "ONE_DT_MODE": 1,
    "V_PXL_OUT_NUM": 1,
    "MIPI_PKTDLY": 1,
    "SUB_IDLETIME": 0,
    "MIPI_FENDDLY": 0,
    "SYSCLK1M_DIV": (SYS_CLK - 1)
}

mipi_cfg = {
    "VC0_THRESHOLD": 0xC0,
    "VC1_THRESHOLD": 0xC0,
    "DataTxThslpxcnt": 2,
    "DataTxThsexitCnt": 2,
    "DataTxThsprepareCnt": 0,
    "DataTxThszeroCnt": 50,
    "DataTxThstrailCnt": 17,
}  # default config: 2, 0, 50, 17


# 一下配置请勿修改, MIPI Rate 相关计算始终基于一下配置进行计算
SEG_HS = 0  #
MIPI_LANE_NUM = 4
MIPI_FIFO_SIZE = 1000

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : MIPI_PKTDLY_Cal.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    : 本文件基于Hawk实际配置, 对流控寄存器(MIPI_PKTDLY)进行计算

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025-04-23 17:40    honggang_li    v1.0        1. 用于计算基于寄存器配置, MIPI_PKTDLY 理论最小配置值;

=================================================================================================
"""
import copy
import math

from PubMethod import *
from HawkConfig import *  # 导入 Hawk 配置


def T_mipi_trans_cyc_cal(csru_cfg: dict, mipi_pktdly: int = None):
    """
    此方法主要是目的是基于不同的 mipi_pktdly 配置, 计算 TXU 和 DPHY 并行传输的时间

    Args:
        csru_cfg(dict): Hawk 配置
        mipi_pktdly(int): 自定义 MIPI_PKTDLY 值, 若为 None, 则使用 MIPI_PKTDLY_Value_Cal 计算的最小值

    Returns:
        int: TXU 和 DPHY 并行传输的时间
    """
    __csru_cfg__ = copy.deepcopy(csru_cfg)
    work_mode = __csru_cfg__["WORK_MODE"]
    h_vld_seg = __csru_cfg__["H_VLD_SEG"]

    PER_VC_PKT_NUM = OneSubframePerVCPktNumCal(__csru_cfg__)

    if mipi_pktdly is not None:
        __csru_cfg__["MIPI_PKTDLY"] = mipi_pktdly

    if work_mode not in [0, 1, 2]:
        raise ValueError(f"MIPI_PKTDLY calculate minimum model is not supported WORK_MODE={work_mode}...")

    once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCalForFHR(__csru_cfg__) if work_mode == 2 \
        else OnceHistReadAddTxdlyCycCalForPHR(__csru_cfg__)  #if work_mode == 1 or work_mode == 0

    T_mipi_trans_cyc = 0
    per_seg_pkg_num = PER_VC_PKT_NUM / (h_vld_seg + 1)
    for seg_cnt in range(0, h_vld_seg + 1, ):
        # 这里采用倒序的方式处理, 主要目的是 PHR 每个 group 的 dly 信息不同, 计算 trans_cyc 时, 应该使用最短时间计算
        # 理论上应该用 seg_hs 获取准确的 seg_index 进行计算更准确
        seg_index = 15 - seg_cnt
        once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[seg_index]
        # T_mipi_trans_cyc += once_hist_rd_add_txdly_cyc * per_seg_pkg_num
        if seg_cnt == h_vld_seg:
            T_mipi_trans_cyc += once_hist_rd_add_txdly_cyc * (per_seg_pkg_num - 1)
        else:
            T_mipi_trans_cyc += once_hist_rd_add_txdly_cyc * per_seg_pkg_num

    return T_mipi_trans_cyc


def MIPI_PKTDLY_Value_Cal(csru_cfg: dict, mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500):
    """
    初步计算 MIPI_PKT_DLY 的最小值

    Returns:
        float: (unit: us)
    """

    # ============================================================================================
    # 计算 MIPI_PKT_DLY 最小值
    # 基于以下实际情况进行计算, 若不满足以下条件, 则不应使用此方法进行计算:
    #     1. VC0 始终后于 VC1 进行传输, 计算 FOFO 条件时, 始终使用 VC0 的 FIFO 进行计算
    #     2. 单个 VC 通道的 MIPI 数据传输速度是大于 TXU 向 FIFO 中的写入速度的, 即: mipi_rate > 12 * SYS_CLK (unit: bit/us)
    # 计算思路为:
    # 1. 计算完整的 HIST 读出时间内, TXU 写入 VC0 FIFO 的数据量, MIPI 读出 VC0 FIFO 的数据量, 数据量的差值是否会导致 FIFO 溢出
    #     假设 HIST 读出时间为 T (cyc), 则 MIPI 在 T 时间内读出的数据量为:
    #         T1 = (T - first_rd_out_ind_cyc - vc0_mipi_pkt_interval_cyc)
    #         读取的完整包数据量 = (T1 / once_hist_rd_mipi_read_cyc) * (WC * 8)
    #         读取的部分包数据量 = (T1 % once_hist_rd_mipi_read_cyc) * MIPI_RATE
    #
    #     Q1: 为什么 T 要减去 first_rd_out_ind_cyc
    #     A1: 不要求严谨, 假设 MIPI threshold 足够大, 第一次 HIST 读没有 MIPI 传输 (实际情况中 FHR 可能会不满足此条件, 不过对计算影响不大)
    #
    #     Q2: 为什么 T 要减去 vc0_mipi_pkt_interval_cyc
    #     A2: VC0 在 VC1 后进行传输
    # 2. 则对 T 的要求为:
    #    HIST总的数据量 - VC0已经传输的数据量 < VC0_FIFO_SIZE
    # ============================================================================================

    tx_frm_mode = csru_cfg["TX_FRM_MODE"]
    one_dt_mode = csru_cfg["ONE_DT_MODE"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1

    mipi_rate = MIPI_RATE * MIPI_LANE_NUM  # unit: bit/us

    WC, FLNR = CalMipiFlnrAndWC(csru_cfg)

    PER_VC_PKT_NUM = OneSubframePerVCPktNumCal(csru_cfg)

    txu_rd_cyc = int(WC / 1.5)
    T_mipi_trans_cyc_dly0 = T_mipi_trans_cyc_cal(csru_cfg, mipi_pktdly=0)
    T_mipi_trans_cyc_dly1 = T_mipi_trans_cyc_cal(csru_cfg, mipi_pktdly=1)

    if one_dt_mode == 1:
        # one_data_type 的情况下, 加上 generic_data 的包
        # one_dt_mode = 0 时, INFO 数据量较小, fifo 计算不用考虑 generic_data 的包
        PER_VC_PKT_NUM += 1
        T_mipi_trans_cyc_dly0 += txu_rd_cyc + 21    # 21 是 ONE_DT_MODE 下 HIST_PKT 与 Genetic_PKT 的固定间隔
        T_mipi_trans_cyc_dly1 += txu_rd_cyc + 21

    MIPI_PKT_INTV = MipiPKGIntvCal(mipi_cfg, SYS_CLK, MIPI_RATE)  # unit: ns
    MIPIPKT_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / mipi_rate  # unit: ns

    VC0_MIPI_PKT_interval = MIPI_PKT_INTV * 2 + MIPIPKT_Tx_HS_Data
    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPIPKT_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)

    vc0_mipi_pkt_interval_cyc = int(VC0_MIPI_PKT_interval * SYS_CLK / 1000) + 1
    once_hist_rd_mipi_read_cyc = int(T_OneHistReadMipiReadTime * SYS_CLK / 1000) + 1

    one_pkt_data_size = WC * 8
    txu_wr_total_data_size = one_pkt_data_size * PER_VC_PKT_NUM
    fifo_size = MIPI_FIFO_SIZE * 32

    # 在 TXU 写入 VC0 FIFO 期间, MIPI-VC0 应该传输的数据量为
    mipi_need_trans_data_size = txu_wr_total_data_size - fifo_size

    mipi_need_trans_pkt_num = mipi_need_trans_data_size // one_pkt_data_size
    mipi_need_trans_data_res = mipi_need_trans_data_size % one_pkt_data_size

    # 计算 VC0 通道需要传输的时间
    T_vc0_min_trans_cyc = (once_hist_rd_mipi_read_cyc * mipi_need_trans_pkt_num +  # unit: cyc
                           mipi_need_trans_data_res * SYS_CLK / mipi_rate  # unit: cyc
                           )

    # 加上从 MIPI 开始传输(VC1 先传)到 VC0 开始传输的时间间隔, 即计算出在 TXU 写入 FIFO 期间, MIPI 最小应该读出的时间
    T_mipi_min_trans_cyc = T_vc0_min_trans_cyc + vc0_mipi_pkt_interval_cyc

    PER_VC_PKT_NUM = OneSubframePerVCPktNumCal(csru_cfg)
    if T_mipi_min_trans_cyc < T_mipi_trans_cyc_dly0:
        mipi_pktdly = 0
    elif T_mipi_min_trans_cyc < T_mipi_trans_cyc_dly1:
        mipi_pktdly = 1
    else:
        pktdly_add = math.ceil((T_mipi_min_trans_cyc - T_mipi_trans_cyc_dly1) / sysclk1m_div / PER_VC_PKT_NUM)
        mipi_pktdly = 1 + pktdly_add

    T_mipi_trans_cyc_dlyx = T_mipi_trans_cyc_cal(csru_cfg, mipi_pktdly=mipi_pktdly)
    print(f"T_mipi_trans_cyc_dly0: {T_mipi_trans_cyc_dly0}")
    print(f"T_mipi_trans_cyc_dly1: {T_mipi_trans_cyc_dly1}")
    print(f"T_mipi_trans_cyc_dlyx: {T_mipi_trans_cyc_dlyx} (mipi_pktdly={mipi_pktdly})")
    print(f"T_mipi_min_trans_cyc : {T_mipi_min_trans_cyc}")
    return mipi_pktdly


if __name__ == '__main__':
    MIPI_PKTDLY = MIPI_PKTDLY_Value_Cal(csru_cfg=csru_cfg, mipi_cfg=mipi_cfg,
                                        SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)

    s = f"[beta] MIPI_PKTDLY Theoretical minimum: {MIPI_PKTDLY}"
    print_c(s)

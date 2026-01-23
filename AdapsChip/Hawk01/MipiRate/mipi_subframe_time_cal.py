#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : mipi_subframe_time.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    : 本文件用于计算 Hawk one-subframe 的时间开销, 输出帧率信息:
                 1. 支持 SCAN_MODE = 1D scan mode/2D scan mode;
                 2. 支持 WORK_MODE = PCM/FHR/PHR/SPHR 配置;
                 3. 支持 ONE_DT_MODE = 0/1 配置;
                 4. 支持 TX_FRM_MODE = 0/1 配置;
                 5. 支持 SYS_CLK, MIPI_RATE 等信息配置, 配置源: ./HawkConfig.py

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025/01/12 09:00    honggang_li    v1.0        1. WORK_MODE 仅支持 PHR 模式计算, 其他模式待完善;
                                               2. MIPI 的协议开销计算方式目前仅支持 1.5 Gbps/Lane;
                                               3. csru_cfg 的配置值请与寄存器配置值保持一致;
                                               4. SYSCLK1M_DIV 根据 SYS_CLk 自动计算, 若需自定义 1M 时
                                                  钟, 需要手动填写分频系数;
                                               5. EXPO_TIME & DRV_CH_TIME 时间需手动填写;
                                               6. 目前算法仅考虑了非多帧和一 & 1D模式;

2025/02/08 09:00    honggang_li    v1.1        1. WORK_MODE 增加支持 FHR;

2025/02/14 09:00    honggang_li    v1.2        1. 重构计算方式, subframe_time 的计算, 不再根据 FLNR 计算, 
                                                  因为其受到 tx_frm_mode 的影响, 且 generic_data 也受到
                                                  此配置的影响;
                                               2. 支持 one_dt_mode 0 / 1 的计算;

2025/02/14 09:00    honggang_li    v1.3        1. 根据配置自动计算 MIPI_PKTDLY 可配置的最小值(beta 版本);
                                               2. 暂时放开 WORK_MODE 为 SPHR 的帧率计算, 与 PHR 共用同一
                                                  套计算逻辑(beta 版本, 未经过仿真验证, 理论上差异不大);

2025/04/23 18:00    honggang_li    v1.4        1. 将自动计算 MIPI_PKTDLY 可配置的最小值计算逻辑(beta 版本)
                                                  移动到另外一个文件进行计算;
                                               2. 抽取公共方法到 PubMethod, 便于其他模块调用;

2026/01/23 12:00    honggang_li    v1.5        1. 帧率计算支持 PCM mode;
                                               2. MIPI busy 场景计算的理论值与实际值误差较大(20us以内),
                                                  主要是由于MIPI 协议开销实际值与理论值存在差异导致, 当一个
                                                  sub-frame 中包数量越多时, 带来的计算误差越大
=================================================================================================
"""

from PubMethod import *
from HawkConfig import *  # 导入 Hawk 配置
# from mipi_pktdly_cal import MIPI_PKTDLY_Value_Cal


# ////////////////////////////////////////////////
# Tsubframe 计算实现
# ////////////////////////////////////////////////
def TSubframReadTimeCalForFHR(csru_cfg: dict, mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500):
    """
    计算 RD_OUT_HIST 状态机的时间

    Args:
        csru_cfg(dict): Hawk 寄存器配置
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane

    Returns:
        float: (unit: us)
    """
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1
    vc1_threshold = mipi_cfg["VC1_THRESHOLD"]

    PER_VC_PKT_NUM = OneSubframePerVCPktNumCal(csru_cfg)
    once_hist_rd_mipi_read_cyc, generic_data_mipi_read_cyc = T_mipi_read_time_cal(csru_cfg=csru_cfg,
                                                                                  mipi_cfg=mipi_cfg,
                                                                                  SYS_CLK=SYS_CLK,
                                                                                  MIPI_RATE=MIPI_RATE)
    once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCalForFHR(csru_cfg)
    once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[0]    # 每个 Seg 数据都相同, 因此仅用 0 进行计算

    if (rd_out_ind_cyc * 12) < (vc1_threshold * 4 * 32):  # 第一次 HIST 读的数据未超过 MIPI threshold, MIPI 会等到 HIST 发送完成才开始数据传输
        print("[TXDLY info]: MIPI data was not transmitted in advance... ")
        first_rd_out_ind_cyc = rd_out_ind_cyc
    else:  # 第一次 HIST 读的数据超过 MIPI threshold, MIPI 会在到达 MIPI threshold 后立马开始传输
        print("[TXDLY info]: MIPI data is transmitted in advance... ")
        first_rd_out_ind_cyc = (vc1_threshold * 4 * 32) / 12

    if once_hist_rd_add_txdly_cyc > once_hist_rd_mipi_read_cyc:
        print(f"[TXDLY info]: mipi free...")
        # 最后一次 HIST 读没有 TXDLY, 因此减去最后一个包传输 mipi_free_cyc
        T_mipi_free_cyc = (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * (PER_VC_PKT_NUM - 1)
    else:
        print(f"[TXDLY info]: mipi busy...")
        T_mipi_free_cyc = 0

    T_frame_hist_read_cyc = (first_rd_out_ind_cyc +  # 第一次 HIST_RD 时间
                             once_hist_rd_mipi_read_cyc * PER_VC_PKT_NUM +  # 实际的 MIPI 传输时间
                             T_mipi_free_cyc +  # MIPI 总的空闲时间
                             generic_data_mipi_read_cyc)  # generic package 的传输时间
    # print(PER_VC_PKT_NUM, once_hist_rd_add_txdly_cyc * (PER_VC_PKT_NUM - 1), once_hist_rd_add_txdly_cyc)
    # 第一次 HIST 读没有与 1M 时钟对齐, 所以做 1us 的冗余
    T_hist_read_time = T_frame_hist_read_cyc / SYS_CLK + 1  # unit: us

    # 此处计数与 1M 时钟为对齐, 至多存在 1us 的误差
    T_mipi_fend_dly_time = 4 * (2 ** csru_cfg["MIPI_FENDDLY"]) * sysclk1m_div / SYS_CLK  # unit: us

    T_hist_read_time = T_hist_read_time + T_mipi_fend_dly_time

    return T_hist_read_time


def TSubframReadTimeCalForPHR(csru_cfg: dict, mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500):
    """
    计算 RD_OUT_HIST 状态机的时间

    Args:
        csru_cfg(dict): Hawk 寄存器配置
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane

    Returns:
        float: (unit: us)
    """
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1
    h_vld_seg = csru_cfg["H_VLD_SEG"]

    PER_VC_PKT_NUM = OneSubframePerVCPktNumCal(csru_cfg)
    once_hist_rd_mipi_read_cyc, generic_data_mipi_read_cyc = T_mipi_read_time_cal(csru_cfg=csru_cfg,
                                                                                  mipi_cfg=mipi_cfg,
                                                                                  SYS_CLK=SYS_CLK,
                                                                                  MIPI_RATE=MIPI_RATE)
    once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCalForPHR(csru_cfg)
    per_seg_pkg_num = PER_VC_PKT_NUM / (h_vld_seg + 1)

    T_mipi_free_cyc = 0
    first_rd_out_ind_cyc = 0
    # for seg_cnt in range(csru_cfg["H_VLD_SEG"], -1, -1):  # 这里的写法目的是做 SEG 的倒序, 便于 T_mipi_free_cyc 的计算
    for seg_cnt in range(0, h_vld_seg + 1, ):
        seg_num = SEG_HS + seg_cnt
        once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[seg_cnt]

        # 第一次 HIST 读之后, 才有 MIPI 数据发送, 计算帧率时, 需要考虑第一次 HIST 读的时间
        if seg_cnt == 0:
            first_rd_out_ind_cyc = rd_out_ind_cyc

        # ////////////////////////////////////////////////
        # 当 MIPI传输时间 小于 HIST_RD+TXDLY 的时间时, MIPI_TX 存在一定时间的空闲时间
        # ////////////////////////////////////////////////
        if once_hist_rd_add_txdly_cyc > once_hist_rd_mipi_read_cyc:
            print(f"[TXDLY info]: SEG_{seg_num} mipi free...")
            T_mipi_free_cyc += (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * per_seg_pkg_num

            # 最后一次 HIST 读没有 TXDLY, 因此减去最后一个包传输 mipi_free_cyc
            if seg_cnt == h_vld_seg:
                last_mipi_free_cyc = once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc
                T_mipi_free_cyc -= last_mipi_free_cyc
        else:
            print(f"[TXDLY info]: SEG_{seg_num} mipi busy...")
            # TODO: Hawk01不存在后面 Group mipi busy, 前面 Group mipi free的场景
            # T_mipi_free_cyc += (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * per_seg_pkg_num
            # T_mipi_free_cyc = 0 if T_mipi_free_cyc < 0 else T_mipi_free_cyc

    T_frame_hist_read_cyc = (first_rd_out_ind_cyc +  # 第一次 HIST_RD 时间
                             once_hist_rd_mipi_read_cyc * PER_VC_PKT_NUM +  # 实际的 MIPI 传输时间
                             T_mipi_free_cyc +  # MIPI 总的空闲时间
                             generic_data_mipi_read_cyc)  # generic package 的传输时间

    # 第一次 HIST 读没有与 1M 时钟对齐, 所以做 1us 的冗余
    T_hist_read_time = T_frame_hist_read_cyc / SYS_CLK + 1  # unit: us

    # 此处计数与 1M 时钟为对齐, 至多存在 1us 的误差
    T_mipi_fend_dly_time = 4 * (2 ** csru_cfg["MIPI_FENDDLY"]) * sysclk1m_div / SYS_CLK  # unit: us

    T_hist_read_time = T_hist_read_time + T_mipi_fend_dly_time

    return T_hist_read_time


def TSubframeCal(csru_cfg: dict, mipi_cfg: dict, SYS_CLK=330, MIPI_RATE=1500, DRV_CH_TIME=0, EXPO_TIME=0):
    """
    计算各个状态的值进行累和

    Args:
        csru_cfg(dict): Hawk 寄存器配置
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane
        DRV_CH_TIME(int): 通道切换时间, unit: us
        EXPO_TIME(int): 曝光时间, unit: us

    Returns:

    """
    work_mode = csru_cfg["WORK_MODE"]
    T_masking_time = (975 - (15 - csru_cfg["H_VLD_SEG"]) * 60) / SYS_CLK
    T_hist_clear_time = 684 / SYS_CLK

    if work_mode == 2 or work_mode == 3:
        T_hist_read_time = TSubframReadTimeCalForFHR(csru_cfg=csru_cfg,
                                                     mipi_cfg=mipi_cfg,
                                                     SYS_CLK=SYS_CLK,
                                                     MIPI_RATE=MIPI_RATE)
    elif work_mode == 1 or work_mode == 0:
        T_hist_read_time = TSubframReadTimeCalForPHR(csru_cfg=csru_cfg,
                                                     mipi_cfg=mipi_cfg,
                                                     SYS_CLK=SYS_CLK,
                                                     MIPI_RATE=MIPI_RATE)
    else:
        # logging.warning(f"Subframe_time calculate model is not supported WORK_MODE = {work_mode}...")
        raise ValueError(f"WORK_MODE={work_mode} is illegal config...")
        # return 0

    # T_sub_idletime 的计数是 1M 时钟分频系数 * 10
    T_sub_idletime = csru_cfg["SUB_IDLETIME"] * (10 * (csru_cfg["SYSCLK1M_DIV"] + 1)) / SYS_CLK  # unit: us

    T_subframe_time = (T_masking_time +
                       T_hist_clear_time +
                       DRV_CH_TIME +
                       EXPO_TIME +
                       T_hist_read_time +
                       T_sub_idletime)

    s = f"=======================================\n"
    s += f"T_masking_time    : {T_masking_time:>8.2f} us\n"
    s += f"T_hist_clear_time : {T_hist_clear_time:>8.2f} us\n"
    s += f"DRV_CH_TIME       : {DRV_CH_TIME:>8.2f} us\n"
    s += f"EXPO_TIME         : {EXPO_TIME:>8.2f} us\n"
    s += f"T_hist_read_time  : {T_hist_read_time:>8.2f} us\n"
    s += f"T_sub_idletime    : {T_sub_idletime:>8.2f} us\n"
    s += f"T_subframe_time   : {T_subframe_time:>8.2f} us\n"
    print(s)
    return T_subframe_time


if __name__ == '__main__':
    SEG_HS = 0          # ROI rolling 起始地址: 0~15
    DRV_CH_TIME = 1     # 通道切换时间, unit: us
    EXPO_TIME = 1000    # 曝光时间, unit: us

    subframe_time = TSubframeCal(csru_cfg=csru_cfg, mipi_cfg=mipi_cfg,
                                 SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE,
                                 DRV_CH_TIME=DRV_CH_TIME, EXPO_TIME=EXPO_TIME)

    # mipi_pktdly = MIPI_PKTDLY_Value_Cal(csru_cfg=csru_cfg, mipi_cfg=mipi_cfg,
    #                                     SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)
    # s = f"[beta] MIPI_PKTDLY Theoretical minimum: {mipi_pktdly}"
    # print_c(s)

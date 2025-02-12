#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : mipi_subframe_time.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025/01/12 09:00    honggang_li    v1.0        1. WORK_MODE 仅支持 PHR 模式计算, 其他模式待完善;
                                               2. MIPI 的协议开销计算方式目前仅支持 1.5 Gbps/Lane;
                                               3. csru_cfg 的配置值请与寄存器配置值保持一致;
                                               4. SYSCLK1M_DIV 根据 SYS_CLk 自动计算, 若需自定义 1M 时
                                                  钟, 需要手动填写分频系数;
                                               5. EXPO_TIME & DRV_CH_TIME 时间需手动填写;
                                               6. 目前算法仅考虑了非多帧和一 & 1D模式

2025/02/08 09:00    honggang_li    v1.1       1. WORK_MODE 增加支持 FHR;
=================================================================================================
"""
import logging

# ////////////////////////////////////////////////
# 系统配置
# 1. 使用方法: 修改相关寄存器配置, 运行脚本, 会自动计算 T_subframe_time
# 2. 此配置对应的皆是寄存器配置, 可能与实际业务配置有差异
# ////////////////////////////////////////////////

SYS_CLK = 324
MIPI_RATE = 1500
EXPO_TIME = 30  # unit: us
DRV_CH_TIME = 0  # unit: us
csru_cfg = {
    "WORK_MODE": 2,  # 目前仅支持 FHR, PHR 模式的帧率计算
    "SCAN_MODE": 1,
    "V_ROLL_NUM": 31,
    "H_ROLL_NUM": 0,
    "H_VLD_SEG": 15,
    "MINBIN_THRS": 0,
    "MAXBIN_THRS": 111,
    "OUT_BIN_NUM": 1,
    "TX_FRAME_MODE": 0,  # 此方法不支持修改此配置
    "ONE_DT_MODE": 0,
    "V_PXL_OUT_NUM": 1,
    "MIPI_PKTDLY": 6,
    "SUB_IDLETIME": 0,
    "MIPI_FENDDLY": 0,
    "SYSCLK1M_DIV": (SYS_CLK - 1)
}
seg_hs = 0

mipi_cfg = {
    "VC0_THRESHOLD": 0xC0,
    "VC1_THRESHOLD": 0xC0,
    "DataTxThslpxcnt": 2,
    "DataTxThsexitCnt": 2,
    "DataTxThsprepareCnt": 0,
    "DataTxThszeroCnt": 19,
    "DataTxThstrailCnt": 12,
}

MIPI_LANE_NUM = 4
TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 330: 16, 400: 20}
MIPI_FIFO_SIZE = 980   # 实际值: 1024, 给出一定余量


# ////////////////////////////////////////////////
# Tsubframe 计算实现
# ////////////////////////////////////////////////
def MipiFlnrAndWcCal():
    """
    计算 MIPI FLNR & WC

    Returns:
        tuple: WC and FLNR
    """
    work_mode = csru_cfg["WORK_MODE"]
    scan_mode = csru_cfg["SCAN_MODE"]
    v_roll_num = csru_cfg["V_ROLL_NUM"]
    h_roll_num = csru_cfg["H_ROLL_NUM"]
    h_vld_seg = csru_cfg["H_VLD_SEG"]
    minbin_thrs = csru_cfg["MINBIN_THRS"]
    maxbin_thrs = csru_cfg["MAXBIN_THRS"]
    out_bin_num = csru_cfg["OUT_BIN_NUM"]
    tx_frame_mode = csru_cfg["TX_FRAME_MODE"]
    one_dt_mode = csru_cfg["ONE_DT_MODE"]

    v_pixel_out_num = 6 if csru_cfg["V_PXL_OUT_NUM"] == 1 else 1

    total_roll_num = 1
    if tx_frame_mode == 1:
        if scan_mode == 0:
            total_roll_num = (v_roll_num + 1) if work_mode != 3 else (v_roll_num + 1) * 9
        if scan_mode == 1:
            total_roll_num = (v_roll_num + 1) * (h_roll_num + 1)

    if work_mode == 0:
        if out_bin_num == 0:
            sphr_pl_num = 38 * v_pixel_out_num
        else:
            sphr_pl_num = 62 * v_pixel_out_num
        wc = sphr_pl_num * 1.5
        flnr = 8 * (h_vld_seg + 1) * total_roll_num + one_dt_mode
    elif work_mode == 1:
        if out_bin_num == 0:
            phr_pl_num = 80 * v_pixel_out_num
        else:
            phr_pl_num = 132 * v_pixel_out_num
        wc = phr_pl_num * 1.5
        flnr = 8 * (h_vld_seg + 1) * total_roll_num + one_dt_mode
    elif work_mode == 2:
        maxbin = (maxbin_thrs + 1) * 2 - 1
        fhr_pl_num = (maxbin - minbin_thrs + 1) * 2 * 4
        wc = fhr_pl_num * 1.5
        flnr = (v_pixel_out_num * 2 * (h_vld_seg + 1)) * total_roll_num + one_dt_mode
    else:
        wc = 32 * 1.5
        flnr = (v_pixel_out_num * 2 * (h_vld_seg + 1)) * total_roll_num + one_dt_mode
    return int(wc), flnr


def MipiPKGIntvCal():
    """
    MIPI 包间协议开销计算

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

    MIPI_PKT_INTV = ((120 if DataTxThsexitCnt == 0 else 320) +
                     T_TxClkEsc * DataTxThslpxcnt +
                     T_TxClkEsc * (DataTxThsprepareCnt + 1) +
                     T_TxByteClkHS * (DataTxThszeroCnt + 4) +
                     T_TxByteClkHS * (DataTxThstrailCnt + 1)
                     )
    # print(T_TxClkEsc * DataTxThslpxcnt)
    # print(T_TxClkEsc * (DataTxThsprepareCnt + 1))
    # print(T_TxByteClkHS * (DataTxThszeroCnt + 4))
    # print(T_TxByteClkHS * (DataTxThstrailCnt + 1))
    print("=======================================")
    print(f"SYS_CLK       : {SYS_CLK:>8} M")
    print(f"MIPI_RATE     : {MIPI_RATE:>8} Gbps/Lane")
    print(f"T_TxClkEsc    : {T_TxClkEsc:>8.2f} ns")
    print(f"T_TxByteClkHS : {T_TxByteClkHS:>8.2f} ns")
    print(f"MIPI_PKT_INTV : {MIPI_PKT_INTV:>8.2f} ns")
    return MIPI_PKT_INTV


def MipiFIFOReleaseCycCal():
    """
    计算 VC0 MIPI FIFO 释放时间(VC0 在 VC1 后面进行传输, 因此计算 MIPI FIFO 额外可以存储的数据时, 以 VC0 的 FIFO 进行计算)
    Returns:
        int: MIPI FIFO 释放时间 (unit: cyc)
    """
    mipi_rate = MIPI_RATE * MIPI_LANE_NUM  # unit: bit/us
    WC, FLNR = MipiFlnrAndWcCal()
    mipi_fifo_free_size = MIPI_FIFO_SIZE * 32 - WC * 8  # VC0 在 VC1 后面进行传输
    mipi_fifo_free_cyc = int(mipi_fifo_free_size / mipi_rate * SYS_CLK)
    return mipi_fifo_free_cyc


def MipiModel():
    """
    计算 VC0 的 model

    Returns:
        float: (unit: us)
    """
    mipi_rate = MIPI_RATE * MIPI_LANE_NUM  # unit: bit/us

    WC, FLNR = MipiFlnrAndWcCal()

    MIPI_PKT_INTV = MipiPKGIntvCal()  # unit: ns
    MIPIPKT_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / mipi_rate  # unit: ns

    VC0_MIPI_PKT_interval = MIPI_PKT_INTV * 2 + MIPIPKT_Tx_HS_Data


def OnceHistReadAddTxdlyCycCalForFHR():
    """
    计算 WORK_MODE = FHR, 单次 HIST读 + TXDLY 的实际时间

    Returns:
        list: (unit: cyc)
        基于 RTL 设计, GROUP 0~3, HIST->DSP 路径延时逐步递减, 因此会返回 4 个 GROUP 的
    分别计算的时间
    """
    RD_OUT_MIN_GAP = 17

    mipi_pktdly = csru_cfg["MIPI_PKTDLY"]
    maxbin_thrs = csru_cfg["MAXBIN_THRS"]
    minbin_thrs = csru_cfg["MINBIN_THRS"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1

    hist_rd_cyc = ((maxbin_thrs + 1) * 2 - minbin_thrs) * 2

    # 基于 RTL 设计, 4 次 HIST 读组成一个包
    rd_out_ind_cyc = (hist_rd_cyc + 7) * 4 + (1 * 3)    # 4 次 HIST 读, 多 3 拍间隔

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

    return once_hist_rd_add_txdly_cyc, rd_out_ind_cyc


def OnceHistReadAddTxdlyCycCalForPHR():
    """
    计算 WORK_MODE = PHR, 单次 HIST读 + TXDLY 的实际时间

    Returns:
        list: (unit: cyc)
        基于 RTL 设计, GROUP 0~3, HIST->DSP 路径延时逐步递减, 因此会返回 4 个 GROUP 的
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

    WC, FLNR = MipiFlnrAndWcCal()

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
            rd_out_ind_us_res = hist_once_read_min_cyc % sysclk1m_div   # unit: cycle
            once_hist_rd_add_txdly_cyc = (rd_out_ind_us_ave + mipi_pktdly) * sysclk1m_div
        else:
            once_hist_rd_add_txdly_cyc = hist_once_read_min_cyc
        once_hist_rd_add_txdly_Q.append((once_hist_rd_add_txdly_cyc, rd_out_ind_cyc))

    return once_hist_rd_add_txdly_Q


def TSubframReadTimeCalForFHR():
    """
    计算 RD_OUT_HIST 状态机的时间

    Returns:
        float: (unit: us)
    """
    one_dt_mode = csru_cfg["ONE_DT_MODE"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1
    vc1_threshold = mipi_cfg["VC1_THRESHOLD"]

    WC, FLNR = MipiFlnrAndWcCal()

    MIPIPKT_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    GENERIC_TX_HS_Data = (40 * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    MIPI_PKT_INTV = MipiPKGIntvCal()  # unit: ns

    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPIPKT_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)
    T_GenericDataMipiReadTime = (MIPI_PKT_INTV + GENERIC_TX_HS_Data) * 2 if one_dt_mode == 0 else 0

    once_hist_rd_mipi_read_cyc = int(T_OneHistReadMipiReadTime * SYS_CLK / 1000) + 1
    generic_data_mipi_read_cyc = int(T_GenericDataMipiReadTime * SYS_CLK / 1000) + 1

    once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = OnceHistReadAddTxdlyCycCalForFHR()

    if (rd_out_ind_cyc * 12) < (vc1_threshold * 4 * 32):    # 第一次 HIST 读的数据未超过 MIPI threshold, MIPI 会等到 HIST 发送完成才开始数据传输
        print("[TXDLY info]: MIPI data was not transmitted in advance... ")
        first_rd_out_ind_cyc = rd_out_ind_cyc
    else:   # 第一次 HIST 读的数据超过 MIPI threshold, MIPI 会在到达 MIPI threshold 后立马开始传输
        print("[TXDLY info]: MIPI data is transmitted in advance... ")
        first_rd_out_ind_cyc = (vc1_threshold * 4 * 32) / 12

    if once_hist_rd_add_txdly_cyc > once_hist_rd_mipi_read_cyc:
        print(f"[TXDLY info]: mipi free...")
        # 最后一次 HIST 读没有 TXDLY, 因此减去最后一个包传输 mipi_free_cyc
        T_mipi_free_cyc = (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * (FLNR - 1)
    else:
        print(f"[TXDLY info]: mipi busy...")
        T_mipi_free_cyc = 0

    T_frame_hist_read_cyc = (first_rd_out_ind_cyc +  # 第一次 HIST_RD 时间
                             once_hist_rd_mipi_read_cyc * FLNR +  # 实际的 MIPI 传输时间
                             T_mipi_free_cyc +  # MIPI 总的空闲时间
                             generic_data_mipi_read_cyc)  # generic package 的传输时间

    # 第一次 HIST 读没有与 1M 时钟对齐, 所以做 1us 的冗余
    T_hist_read_time = T_frame_hist_read_cyc / SYS_CLK + 1  # unit: us

    # 此处计数与 1M 时钟为对齐, 至多存在 1us 的误差
    T_mipi_fend_dly_time = 4 * (2 ** csru_cfg["MIPI_FENDDLY"]) * sysclk1m_div / SYS_CLK  # unit: us

    T_hist_read_time = T_hist_read_time + T_mipi_fend_dly_time

    return T_hist_read_time


def TSubframReadTimeCalForPHR():
    """
    计算 RD_OUT_HIST 状态机的时间

    Returns:
        float: (unit: us)
    """
    one_dt_mode = csru_cfg["ONE_DT_MODE"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1

    mipi_rate = MIPI_RATE * MIPI_LANE_NUM  # unit: bit/us
    WC, FLNR = MipiFlnrAndWcCal()

    MIPI_PKT_INTV = MipiPKGIntvCal()  # unit: ns
    MIPIPKT_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / mipi_rate  # unit: ns
    GENERIC_TX_HS_Data = (40 * 8 + 6 * 8) * 1000 / mipi_rate  # unit: ns

    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPIPKT_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)
    T_GenericDataMipiReadTime = (MIPI_PKT_INTV + GENERIC_TX_HS_Data) * 2 if one_dt_mode == 0 else 0

    once_hist_rd_mipi_read_cyc = int(T_OneHistReadMipiReadTime * SYS_CLK / 1000) + 1
    generic_data_mipi_read_cyc = int(T_GenericDataMipiReadTime * SYS_CLK / 1000) + 1

    once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCalForPHR()
    per_seg_pkg_num = FLNR / (csru_cfg["H_VLD_SEG"] + 1)  # TODO: 这里的算法仅考虑了非多帧和一 & 1D模式
    T_mipi_free_cyc = 0
    first_rd_out_ind_cyc = 0
    # for seg_cnt in range(csru_cfg["H_VLD_SEG"], -1, -1):  # 这里的写法目的是做 SEG 的倒序, 便于 T_mipi_free_cyc 的计算
    for seg_cnt in range(0, csru_cfg["H_VLD_SEG"]+1,):
        seg_num = seg_hs + seg_cnt
        group_cnt = seg_num // 4
        once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[group_cnt]

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
            if seg_cnt == csru_cfg["H_VLD_SEG"]:
                last_mipi_free_cyc = once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc
                T_mipi_free_cyc -= last_mipi_free_cyc
        else:
            print(f"[TXDLY info]: SEG_{seg_num} mipi busy...")
            # TODO: Hawk01不存在后面 Group mipi busy, 前面 Group mipi free的场景
            # T_mipi_free_cyc += (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * per_seg_pkg_num
            # T_mipi_free_cyc = 0 if T_mipi_free_cyc < 0 else T_mipi_free_cyc

    T_frame_hist_read_cyc = (first_rd_out_ind_cyc +  # 第一次 HIST_RD 时间
                             once_hist_rd_mipi_read_cyc * FLNR +  # 实际的 MIPI 传输时间
                             T_mipi_free_cyc +  # MIPI 总的空闲时间
                             generic_data_mipi_read_cyc)  # generic package 的传输时间

    # 第一次 HIST 读没有与 1M 时钟对齐, 所以做 1us 的冗余
    T_hist_read_time = T_frame_hist_read_cyc / SYS_CLK + 1  # unit: us

    # 此处计数与 1M 时钟为对齐, 至多存在 1us 的误差
    T_mipi_fend_dly_time = 4 * (2 ** csru_cfg["MIPI_FENDDLY"]) * sysclk1m_div / SYS_CLK  # unit: us

    T_hist_read_time = T_hist_read_time + T_mipi_fend_dly_time

    return T_hist_read_time


def TSubframeCal():
    """
    计算各个状态的值进行累和

    Returns:
        一个 subframe 的帧率; unit: us
    """
    work_mode = csru_cfg["WORK_MODE"]
    T_masking_time = (975 - (15 - csru_cfg["H_VLD_SEG"]) * 60) / SYS_CLK
    T_hist_clear_time = 684 / SYS_CLK

    if work_mode == 2:
        T_hist_read_time = TSubframReadTimeCalForFHR()
    elif work_mode == 1:
        T_hist_read_time = TSubframReadTimeCalForPHR()
    else:
        # logging.warning(f"Subframe_time calculate model is not supported WORK_MODE = {work_mode}...")
        raise ValueError(f"Subframe_time calculate model is not supported WORK_MODE={work_mode}...")
        # return 0

    # T_sub_idletime 的计数是 1M 时钟分频系数 * 10
    T_sub_idletime = csru_cfg["SUB_IDLETIME"] * (10 * (csru_cfg["SYSCLK1M_DIV"] + 1)) / SYS_CLK  # unit: us

    T_subframe_time = (T_masking_time +
                       T_hist_clear_time +
                       DRV_CH_TIME +
                       EXPO_TIME +
                       T_hist_read_time +
                       T_sub_idletime)

    print(f"=======================================")
    print(f"T_masking_time    : {T_masking_time:>8.2f} us")
    print(f"T_hist_clear_time : {T_hist_clear_time:>8.2f} us")
    print(f"DRV_CH_TIME       : {DRV_CH_TIME:>8.2f} us")
    print(f"EXPO_TIME         : {EXPO_TIME:>8.2f} us")
    print(f"T_hist_read_time  : {T_hist_read_time:>8.2f} us")
    print(f"T_sub_idletime    : {T_sub_idletime:>8.2f} us")
    print(f"T_subframe_time   : {T_subframe_time:>8.2f} us")
    return T_subframe_time


if __name__ == '__main__':
    subframe_time = TSubframeCal()

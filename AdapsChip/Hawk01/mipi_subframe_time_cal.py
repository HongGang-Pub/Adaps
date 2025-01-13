# ////////////////////////////////////////////////
# 系统配置
# ////////////////////////////////////////////////
import logging

SYS_CLK = 324
MIPI_RATE = 1500
EXPO_TIME = 30  # unit: us
DRV_CH_TIME = 0  # unit: us
csru_cfg = {
    "WORK_MODE": 1,
    "SCAN_MODE": 1,
    "V_ROLL_NUM": 31,
    "H_ROLL_NUM": 0,
    "H_VLD_SEG": 15,
    "MINBIN_THRS": 0,
    "MAXBIN_THRS": 111,
    "OUT_BIN_NUM": 1,
    "TX_FRAME_MODE": 0,  # 此方法不支持修改此配置
    "ONE_DT_MODE": 0,
    "V_PXL_OUT_NUM": 0,
    "MIPI_TXDLY": 0,
    "SUB_IDLETIME": 1,
    "MIPI_FENDDLY": 0,
    "SYSCLK1M_DIV": (SYS_CLK - 1)
}
seg_hs = 0

MIPI_DPHY_cfg = {
    "DataTxThslpxcnt": 2,
    "DataTxThsexitCnt": 2,
    "DataTxThsprepareCnt": 0,
    "DataTxThszeroCnt": 50,
    "DataTxThstrailCnt": 17,
}
MIPI_LANE_NUM = 4
TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 330: 16}


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


def MipiPKGIntvCAL():
    """
    MIPI 包间协议开销计算

    Returns:
        float: MIPI 包间协议开销 (unit: ns)
    """
    TXHSByteClkDiv = 8
    T_TxClkEsc = 1000 / (SYS_CLK / (TxEscClkDiv_Q[SYS_CLK] + 1))
    T_TxByteClkHS = 1000 / (MIPI_RATE / TXHSByteClkDiv)

    DataTxThslpxcnt = MIPI_DPHY_cfg["DataTxThslpxcnt"]
    DataTxThsexitCnt = MIPI_DPHY_cfg["DataTxThsexitCnt"]
    DataTxThsprepareCnt = MIPI_DPHY_cfg["DataTxThsprepareCnt"]
    DataTxThszeroCnt = MIPI_DPHY_cfg["DataTxThszeroCnt"]
    DataTxThstrailCnt = MIPI_DPHY_cfg["DataTxThstrailCnt"]

    MIPI_PKT_INTV = ((120 if DataTxThsexitCnt == 0 else 320) +
                     T_TxClkEsc * DataTxThslpxcnt +
                     T_TxClkEsc * (DataTxThsprepareCnt + 1) +
                     T_TxByteClkHS * (DataTxThszeroCnt + 4) +
                     T_TxByteClkHS * (DataTxThstrailCnt + 1)
                     )
    print("=======================================")
    print(f"SYS_CLK       : {SYS_CLK:>8} M")
    print(f"MIPI_RATE     : {MIPI_RATE:>8} Gbps/Lane")
    print(f"T_TxClkEsc    : {T_TxClkEsc:>8.2f} ns")
    print(f"T_TxByteClkHS : {T_TxByteClkHS:>8.2f} ns")
    print(f"MIPI_PKT_INTV : {MIPI_PKT_INTV:>8.2f} ns")
    return MIPI_PKT_INTV


def OnceHistReadAddTxdlyCycCal():
    """
    计算单次 HIST读 + TXDLY 的实际时间

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

    mipi_txdly = csru_cfg["MIPI_TXDLY"]
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
        hist2dsp_path_dly_cyc = 13 - group_cnt
        rd_out_ind_cyc = (hist2dsp_path_dly_cyc + hist_rd_cyc + dsp_mf_cal_cyc +
                          dsp2txu_path_dly_cyc + txu_rd_cyc + txu2sysc_path_dly_cyc)

        hist_once_read_min_cyc = rd_out_ind_cyc + RD_OUT_MIN_GAP

        # ////////////////////////////////////////////////
        # mipi_txdly 使用 1M 的时钟, 需要用 sysclk1m_div 进行 cycle 计算
        # ////////////////////////////////////////////////
        if mipi_txdly > 0:
            # 若 1M 时钟不是严格的 1us, 则此值可以理解为针对 1M 分频时钟的次数
            rd_out_ind_us_ave = hist_once_read_min_cyc // sysclk1m_div  # unit: us
            rd_out_ind_us_res = hist_once_read_min_cyc % sysclk1m_div  # unit: cycle
            once_hist_rd_add_txdly_cyc = (rd_out_ind_us_ave + mipi_txdly) * sysclk1m_div
        else:
            once_hist_rd_add_txdly_cyc = hist_once_read_min_cyc
        once_hist_rd_add_txdly_Q.append((once_hist_rd_add_txdly_cyc, rd_out_ind_cyc))

    return once_hist_rd_add_txdly_Q


def TSubframReadTimeCal():
    """
    计算 RD_OUT_HIST 状态机的时间

    Returns:
        float: (unit: us)
    """
    one_dt_mode = csru_cfg["ONE_DT_MODE"]
    sysclk1m_div = csru_cfg["SYSCLK1M_DIV"] + 1

    WC, FLNR = MipiFlnrAndWcCal()

    MIPIPKT_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    GENERIC_TX_HS_Data = (40 * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    MIPI_PKT_INTV = MipiPKGIntvCAL()  # unit: ns

    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPIPKT_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)
    T_GenericDataMipiReadTime = (MIPI_PKT_INTV + GENERIC_TX_HS_Data) * 2 if one_dt_mode == 0 else 0

    once_hist_rd_mipi_read_cyc = int(T_OneHistReadMipiReadTime * SYS_CLK / 1000) + 1
    generic_data_mipi_read_cyc = int(T_GenericDataMipiReadTime * SYS_CLK / 1000) + 1

    once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCal()
    per_seg_pkg_num = FLNR / (csru_cfg["H_VLD_SEG"] + 1)
    T_mipi_free_cyc = 0
    first_rd_out_ind_cyc = 0
    case0 = 0
    case1 = 0
    for seg_cnt in range(0, csru_cfg["H_VLD_SEG"] + 1):
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
            case0 += 1
            if case1 > 1:
                logging.warning("")     # TODO
            print(f"Group_{group_cnt} mipi free...")
            T_mipi_free_cyc += (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * per_seg_pkg_num

            # 最后一次 HIST 读没有 TXDLY, 因此减去最后一个包传输 mipi_free_cyc
            if seg_cnt == csru_cfg["H_VLD_SEG"]:
                last_mipi_free_cyc = once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc
                T_mipi_free_cyc -= last_mipi_free_cyc
        else:
            case1 += 1
            if case0 > 1:
                logging.warning("")     # TODO
            continue

    T_frame_hist_read_cyc = (first_rd_out_ind_cyc +  # 第一次 HIST_RD 时间
                             once_hist_rd_mipi_read_cyc * FLNR +  # 实际的 MIPI 传输时间
                             T_mipi_free_cyc +  # MIPI 总的空闲时间
                             generic_data_mipi_read_cyc)  # generic package 的传输时间

    # 第一次 HIST 读没有与 1M 时钟对齐, 所以做 1us 的冗余
    T_hist_read_time = T_frame_hist_read_cyc / SYS_CLK + 1  # unit: us

    # 此处计数与 1M 时钟为对齐, 至多存在 1us 的误差
    T_mipi_fend_dly_time = 4 * (2 ** csru_cfg["MIPI_FENDDLY"]) * sysclk1m_div / SYS_CLK  # unit: us

    T_hist_read_time = T_hist_read_time + T_mipi_fend_dly_time

    # print(f"=======================================")
    # print(f"MIPI_PKT_INTV : {MIPI_PKT_INTV:>8.2f} ns")
    # print(f"hist_read_cyc : {T_frame_hist_read_cyc: >8}")
    # print(f"hist_read_time: {T_hist_read_time:>8.2f} us")
    return T_hist_read_time


def TSubframeCal():
    """
    计算各个状态的值进行累和

    Returns:
        一个 subframe 的帧率; unit: us
    """
    T_masking_time = (975 - (15 - csru_cfg["H_VLD_SEG"]) * 10) / SYS_CLK
    T_hist_clear_time = 684 / SYS_CLK
    T_hist_read_time = TSubframReadTimeCal()
    # T_sub_idletime 的计数是 1M 时钟分频系数 * 10
    T_sub_idletime = csru_cfg["SUB_IDLETIME"] * (10 * (csru_cfg["SYSCLK1M_DIV"] + 1)) / SYS_CLK  # unit: us

    T_subframe_time = (T_masking_time +
                       T_hist_clear_time +
                       DRV_CH_TIME +
                       EXPO_TIME +
                       T_hist_read_time +
                       T_sub_idletime)

    print(f"=======================================")
    print(f"T_masking_cyc    : {T_masking_time:>8.2f} us")
    print(f"T_hist_clear_cyc : {T_hist_clear_time:>8.2f} us")
    print(f"DRV_CH_TIME      : {DRV_CH_TIME:>8.2f} us")
    print(f"EXPO_TIME        : {EXPO_TIME:>8.2f} us")
    print(f"T_hist_read_time : {T_hist_read_time:>8.2f} us")
    print(f"T_sub_idletime   : {T_sub_idletime:>8.2f} us")
    print(f"T_subframe_time  : {T_subframe_time:>8.2f} us")
    return T_subframe_time


if __name__ == '__main__':
    subframe_time = TSubframeCal()

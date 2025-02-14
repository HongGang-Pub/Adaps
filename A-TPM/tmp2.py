# ////////////////////////////////////////////////
# 系统配置
# ////////////////////////////////////////////////
SYS_CLK = 324
MIPI_RATE = 1500
EXPO_TIME = 30      # unit: us
DRV_CH_TIME = 0     # unit: us
csru_cfg = {
    "WORK_MODE": 1,
    "SCAN_MODE": 1,
    "V_ROLL_NUM": 31,
    "H_ROLL_NUM": 0,
    "H_VLD_SEG": 15,
    "MINBIN_THRS": 0,
    "MAXBIN_THRS": 111,
    "OUT_BIN_NUM": 1,
    "TX_FRM_MODE": 0,     # 此方法不支持修改此配置
    "ONE_DT_MODE": 0,
    "V_PXL_OUT_NUM": 0,
    "MIPI_TXDLY": 0,
    "SUB_IDLETIME": 1,
    "MIPI_FENDDLY": 0,
}
seg_hs = 0
MIPI_LANE_NUM = 4


# ////////////////////////////////////////////////
# Tsubframe 计算实现
# ////////////////////////////////////////////////
def MipiFlnrAndWcCal():
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

    total_roll_num = 1
    if tx_frm_mode == 1:
        if scan_mode == 0:
            total_roll_num = (v_roll_num + 1) if work_mode != 3 else (v_roll_num + 1) * 9
        if scan_mode == 1:
            total_roll_num = (v_roll_num + 1) * (h_roll_num + 1)

    if work_mode == 0:
        if out_bin_num == 0:
            sphr_pl_num = 38 * v_pxl_out_num
        else:
            sphr_pl_num = 62 * v_pxl_out_num
        wc = sphr_pl_num * 1.5
        flnr = 8 * (h_vld_seg + 1) * total_roll_num + one_dt_mode
    elif work_mode == 1:
        if out_bin_num == 0:
            phr_pl_num = 80 * v_pxl_out_num
        else:
            phr_pl_num = 132 * v_pxl_out_num
        wc = phr_pl_num * 1.5
        flnr = 8 * (h_vld_seg + 1) * total_roll_num + one_dt_mode
    elif work_mode == 2:
        maxbin = (maxbin_thrs + 1) * 2 - 1
        fhr_pl_num = (maxbin - minbin_thrs + 1) * 2 * 4
        wc = fhr_pl_num * 1.5
        flnr = (v_pxl_out_num * 2 * (h_vld_seg + 1)) * total_roll_num + one_dt_mode
    else:
        wc = 32 * 1.5
        flnr = (v_pxl_out_num * 2 * (h_vld_seg + 1)) * total_roll_num + one_dt_mode
    return int(wc), flnr


def MipiPtkIntvCAL():
    TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 330: 16}
    TXHSByteClkDiv = 8

    T_TxClkEsc = 1000 / (SYS_CLK / (TxEscClkDiv_Q[SYS_CLK] + 1))
    T_TxByteClkHS = 1000 / (MIPI_RATE / TXHSByteClkDiv)

    DataTxThslpxcnt = 2
    DataTxThsexitCnt = 2
    DataTxThsprepareCnt = 0
    DataTxThszeroCnt = 50
    DataTxThstrailCnt = 17

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


def OnceHistReadAddTxdlyCycCal(hist_rd_cyc=448, txu_rd_cyc=132):
    hist2dsp_path_dly_cyc = 13
    dsp_mf_cal_cyc = 13
    dsp2txu_path_dly_cyc = 14
    txu2sysc_path_dly_cyc = 1
    RD_OUT_MIN_GAP = 17

    mipi_txdly = csru_cfg["MIPI_TXDLY"]
    maxbin_thrs = csru_cfg["MAXBIN_THRS"]
    minbin_thrs = csru_cfg["MINBIN_THRS"]

    WC, FLNR = MipiFlnrAndWcCal()

    hist_rd_cyc = ((maxbin_thrs + 1) * 2 - minbin_thrs) * 2
    txu_rd_cyc = int(WC / 1.5)

    # 四个 group, 每个 group 的 dly 不一样
    once_hist_rd_add_txdly_Q = []
    for group_cnt in range(0, 4):
        hist2dsp_path_dly_cyc = 13 - group_cnt
        rd_out_ind_cyc = (hist2dsp_path_dly_cyc + hist_rd_cyc + dsp_mf_cal_cyc +
                          dsp2txu_path_dly_cyc + txu_rd_cyc + txu2sysc_path_dly_cyc)

        hist_once_read_min_cyc = rd_out_ind_cyc + RD_OUT_MIN_GAP

        if mipi_txdly > 0:
            rd_out_ind_us_ave = hist_once_read_min_cyc // SYS_CLK   # unit: us
            rd_out_ind_us_res = hist_once_read_min_cyc % SYS_CLK    # unit: cycle
            once_hist_rd_add_txdly_cyc = (rd_out_ind_us_ave + mipi_txdly) * SYS_CLK
        else:
            once_hist_rd_add_txdly_cyc = hist_once_read_min_cyc
        once_hist_rd_add_txdly_Q.append((once_hist_rd_add_txdly_cyc, rd_out_ind_cyc))

    return once_hist_rd_add_txdly_Q


def TSubframReadCycleCal():
    one_dt_mode = csru_cfg["ONE_DT_MODE"]

    WC, FLNR = MipiFlnrAndWcCal()

    MIPIPKT_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    GENERIC_TX_HS_Data = (40 * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    MIPI_PKT_INTV = MipiPtkIntvCAL()    # unit: ns

    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPIPKT_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)
    T_GenericDataMipiReadTime = (MIPI_PKT_INTV + GENERIC_TX_HS_Data) * 2 if one_dt_mode == 0 else 0

    once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCal()

    once_hist_rd_mipi_read_cyc = int(T_OneHistReadMipiReadTime * SYS_CLK / 1000) + 1
    generic_data_mipi_read_cyc = int(T_GenericDataMipiReadTime * SYS_CLK / 1000) + 1

    '''
    if once_hist_rd_add_txdly_cyc > once_hist_rd_mipi_read_cyc:
        # Q1: Why sub txdly_actual_effective_cyc?
        # A1: 最后一个包 TXDLY 不再计时.
        # Q2: Why add once_hist_rd_mipi_read_cyc?
        # A2: 建立在 MIPI 阈值设置比较大, 一个完整的包写完才会进行 MIPI 数据传输.
        T_frame_hist_read_cyc = (once_hist_rd_add_txdly_cyc * FLNR - txdly_actual_effective_cyc +
                                 once_hist_rd_mipi_read_cyc + generic_data_mipi_read_cyc)
    else:
        # 直接以 MIPI 传输数据为准
        T_frame_hist_read_cyc = once_hist_rd_mipi_read_cyc * FLNR + generic_data_mipi_read_cyc
    '''
    per_seg_pkg_num = FLNR / (csru_cfg["H_VLD_SEG"] + 1)
    T_mipi_free_cyc = 0
    first_rd_out_ind_cyc = 0
    for seg_cnt in range(0, csru_cfg["H_VLD_SEG"]+1):
        seg_num = seg_hs + seg_cnt
        group_cnt = seg_num // 4
        once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[group_cnt]

        if seg_cnt == 0:
            first_rd_out_ind_cyc = once_hist_rd_add_txdly_Q[group_cnt][1]
        if once_hist_rd_add_txdly_cyc > once_hist_rd_mipi_read_cyc:
            print(f"Group_{group_cnt} mipi free...")
            T_mipi_free_cyc += (once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc) * per_seg_pkg_num
            if seg_cnt == csru_cfg["H_VLD_SEG"]:
                last_mipi_free_cyc = once_hist_rd_add_txdly_cyc - once_hist_rd_mipi_read_cyc
                T_mipi_free_cyc -= last_mipi_free_cyc

    T_frame_hist_read_cyc = (first_rd_out_ind_cyc +
                             once_hist_rd_mipi_read_cyc * FLNR +
                             T_mipi_free_cyc +
                             generic_data_mipi_read_cyc)

    # 第一次 HIST 读没有与 1M 时钟对齐, 所以做 1us 的冗余
    T_hist_read_time = T_frame_hist_read_cyc / SYS_CLK + 1  # unit: us
    # 此处计数与 1M 时钟为对齐, 至多存在 1us 的误差
    T_mipi_fend_dly_time = 4 * (2**csru_cfg["MIPI_FENDDLY"])     # unit: us

    T_hist_read_time += T_mipi_fend_dly_time

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
    T_masking_time = (975 - (15-csru_cfg["H_VLD_SEG"])*10) / SYS_CLK
    T_hist_clear_time = 684 / SYS_CLK
    T_hist_read_time = TSubframReadCycleCal()
    T_sub_idletime = csru_cfg["SUB_IDLETIME"] * 10  # unit: us

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

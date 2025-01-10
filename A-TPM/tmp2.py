# ////////////////////////////////////////////////
# 系统配置
# ////////////////////////////////////////////////
SYS_CLK = 250
MIPI_RATE = 1000
csru_cfg = {
    "WORK_MODE": 2,
    "SCAN_MODE": 1,
    "V_ROLL_NUM": 32,
    "H_ROLL_NUM": 0,
    "H_VLD_SEG": 16,
    "MINBIN_THRS": 0,
    "MAXBIN_THRS": 335,
    "OUT_BIN_NUM": 1,
    "TX_FRAME_MODE": 0,
    "ONE_DT_MODE": 0,
    "V_PXL_OUT_NUM": 0,
    "MIPI_TXDLY": 0
}
MIPI_LANE_NUM = 4


# ////////////////////////////////////////////////
# Tsubframe 计算实现
# ////////////////////////////////////////////////
def PkgNumCal():
    """
    非多帧合一时，一次rolling包的数量
    Returns:
        int: 非多帧合一时，一次rolling包的数量
    """

    work_mode = csru_cfg["WORK_MODE"]
    h_vld_seg = csru_cfg["H_VLD_SEG"]
    v_pixel_out_num = 6 if csru_cfg["V_PXL_OUT_NUM"] == 1 else 1

    if work_mode == 2 or work_mode == 3:
        pkg_num = (h_vld_seg + 1) * v_pixel_out_num * 4 + 2
    else:
        pkg_num = (h_vld_seg + 1) * 16 + 2
    return pkg_num


def MipiFlnrAndWcCal():
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

    MIPI_PKT_INTV = ((120 if DataTxThsexitCnt == 0 else 360) +
                     T_TxClkEsc * DataTxThslpxcnt +
                     T_TxClkEsc * (DataTxThsprepareCnt + 1) +
                     T_TxByteClkHS * (DataTxThszeroCnt + 4) +
                     T_TxByteClkHS * (DataTxThstrailCnt + 1)
                     )
    print("==================================")
    print(f"SYS_CLK: {SYS_CLK}, MIPI_RATE: {MIPI_RATE}")
    print(f"T_TxClkEsc: {T_TxClkEsc:0.2f}")
    print(f"T_TxByteClkHS: {T_TxByteClkHS:0.2f}")
    print(f"MIPI 包间间隔: {MIPI_PKT_INTV:0.2f}")
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

    rd_out_ind_cyc = (hist2dsp_path_dly_cyc + hist_rd_cyc + dsp_mf_cal_cyc +
                      dsp2txu_path_dly_cyc + txu_rd_cyc + txu2sysc_path_dly_cyc)

    hist_once_read_min_cyc = rd_out_ind_cyc + RD_OUT_MIN_GAP

    if mipi_txdly > 0:
        rd_out_ind_us_ave = hist_once_read_min_cyc // SYS_CLK
        rd_out_ind_us_res = hist_once_read_min_cyc % SYS_CLK
        once_hist_rd_add_txdly_cyc = (rd_out_ind_us_ave + mipi_txdly - (1 if rd_out_ind_us_res == 0 else 0)) * SYS_CLK
    else:
        once_hist_rd_add_txdly_cyc = hist_once_read_min_cyc
    return once_hist_rd_add_txdly_cyc


def TSubframCal():
    WC, FLNT = MipiFlnrAndWcCal()
    MIPI_Tx_HS_Data = (WC * 8 + 6 * 8) * 1000 / (MIPI_RATE * MIPI_LANE_NUM)  # unit: ns
    MIPI_PKT_INTV = MipiPtkIntvCAL()    # unit: ns

    T_OneHistReadMipiReadTime = (MIPI_PKT_INTV + MIPI_Tx_HS_Data) * 2  # VC0 & VC1 (unit: ns)
    once_hist_rd_mipi_read_cyc = T_OneHistReadMipiReadTime * SYS_CLK / 1000 + 1
    once_hist_rd_add_txdly_cyc = OnceHistReadAddTxdlyCycCal()


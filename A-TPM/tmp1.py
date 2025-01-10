MIPI_PKT_interval_dict = {
    # SYS_CLK
    324: {
        # MIPI_RATE:
        800: 1250,
        1000: 1100,
        1200: 1010,
        1500: 900,
    },
    330: {
        # MIPI_RATE:
        800: 1240,
        1000: 1070,
        1200: 980,
        1500: 900,
    }
}


def MIPI_PKT_INTV_CAL(SYS_CLK, MIPI_RATE):
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
                     T_TxByteClkHS * (DataTxThstrailCnt + 1) +
                     (6 * 8 + 8) / (MIPI_RATE * 4))
    print("==================================")
    print(f"SYS_CLK: {SYS_CLK}, MIPI_RATE: {MIPI_RATE}")
    print(f"T_TxClkEsc: {T_TxClkEsc:0.2f}")
    print(f"T_TxByteClkHS: {T_TxByteClkHS:0.2f}")
    print(f"MIPI 包间间隔: {MIPI_PKT_INTV:0.2f}")
    return MIPI_PKT_INTV


if __name__ == '__main__':
    for SYS_CLK in [250, 324, 330]:
        for MIPI_RATE in [1000, 1200, 1500]:
            MIPI_PKT_INTV_CAL(SYS_CLK, MIPI_RATE)
            pass

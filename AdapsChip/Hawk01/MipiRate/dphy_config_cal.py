from AdapsChip.Common.common import MIPI_CONFIG_Cal

if __name__ == '__main__':
    # SYS_CLK_Q = [200, 250, 330, 400]
    # TxEscClkDiv_Q = [11, 14, 16, 16]
    # MIPI_RATE_Q = [800, 1000, 1200, 1500]
    SYS_CLK_Q = [400]
    # TxEscClkDiv_Q = [16, 20]
    MIPI_RATE_Q = [800, 1000]
    for clk_index in range(len(SYS_CLK_Q)):
        for mipi_index in range(len(MIPI_RATE_Q)):
            MIPI_CONFIG_Cal(SYS_CLK=SYS_CLK_Q[clk_index], MIPI_RATE=MIPI_RATE_Q[mipi_index])

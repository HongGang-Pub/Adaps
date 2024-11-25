SYS_CLK = [200, 250, 330]
TxEscClkDiv = [11, 14, 16, 16]
MIPI_RATE = [800, 1000, 1200, 1500]
TXHSByteClkDiv = 8

for clk_index in range(len(SYS_CLK)):
    for mipi_index in range(len(MIPI_RATE)):
        T_txesc_clk = 1000 / (SYS_CLK[clk_index] / (TxEscClkDiv[clk_index]+1))
        T_txhsbyte_clk = 1000 / (MIPI_RATE[mipi_index] / TXHSByteClkDiv)
        UI = 1000 / MIPI_RATE[mipi_index]

        T_std_lp_01 = T_txesc_clk * 2
        T_std_hs_prepare = 40 + 4*UI
        T_std_hs_pre_zero = 145 + 10*UI
        T_std_hs_trail = 60 + 4*UI
        T_std_hs_exit = 100

        T_default_lp_01 = T_txesc_clk * 2
        T_default_hs_prepare = 0 * T_txesc_clk
        T_default_hs_pre_zero = T_default_hs_prepare + 50 * T_txhsbyte_clk
        T_default_hs_trail = 17 * T_txhsbyte_clk
        T_default_hs_exit = 2 * T_txesc_clk
        T_default_all_aacu = T_default_lp_01 + T_default_hs_exit + T_default_hs_pre_zero + T_default_hs_trail

        T_std_all_accu = T_std_lp_01 + T_std_hs_exit + T_std_hs_pre_zero + T_std_hs_trail

        T_hs_prepare_config = int(T_std_hs_prepare // T_txesc_clk + (1 if T_std_hs_prepare % T_txesc_clk > 0 else 0))
        T_hs_zero = T_std_hs_pre_zero - T_hs_prepare_config * T_txesc_clk
        T_hs_zero_config = int(T_hs_zero // T_txhsbyte_clk + (1 if T_hs_zero % T_txhsbyte_clk > 0 else 0))

        T_hs_trail_config = int(T_std_hs_trail // T_txhsbyte_clk + (1 if T_std_hs_trail % T_txhsbyte_clk > 0 else 0))
        T_hs_exit_config = int(T_std_hs_exit // T_txesc_clk + (1 if T_std_hs_exit % T_txesc_clk > 0 else 0))

        T_lp_01 = T_txesc_clk * 2
        T_hs_prepare = T_hs_prepare_config * T_txesc_clk
        T_hs_pre_zero = T_hs_prepare + T_hs_zero_config * T_txhsbyte_clk
        T_hs_trail = T_hs_trail_config * T_txhsbyte_clk
        T_hs_exit = T_hs_exit_config * T_txesc_clk
        T_all_aacu = T_lp_01 + T_hs_exit + T_hs_pre_zero + T_hs_trail

        print(f"SYS_CLK: {SYS_CLK[clk_index]}, MIPI_RATE: {MIPI_RATE[mipi_index]}, T_txesc_clk: {T_txesc_clk:5.2f}, T_txhsbyte_clk: {T_txhsbyte_clk:5.2f}:")
        print(f"\t   Item       : CONFIG |  T_cal |  T_std")
        print(f"\tT_lpx         : {2:4}   | {T_lp_01:6.2f} | {T_std_lp_01:6.2f}")
        print(f"\tT_hs_prepare  : {T_hs_prepare_config:4}   | {T_hs_prepare:6.2f} | {T_std_hs_prepare:6.2f}")
        print(f"\tT_hs_pre_zero : {T_hs_zero_config:4}   | {T_hs_pre_zero:6.2f} | {T_std_hs_pre_zero:6.2f}")
        print(f"\tT_hs_trail    : {T_hs_trail_config:4}   | {T_hs_trail:6.2f} | {T_std_hs_trail:6.2f}")
        print(f"\tT_hs_exit     : {T_hs_exit_config:4}   | {T_hs_exit:6.2f} | {T_std_hs_exit:6.2f}")
        print(f"\tT_all_aacu    :        | {T_all_aacu:6.2f} | {T_std_all_accu:6.2f}")
        print(f"\tT_default_down:        | {T_default_all_aacu:6.2f} | {T_default_all_aacu-T_all_aacu:6.2f}")

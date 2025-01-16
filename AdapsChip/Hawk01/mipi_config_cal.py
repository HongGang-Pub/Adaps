# ////////////////////////////////////////////////
# MIPI 满足时序要求时, 相关配置自动计算逻辑
# ////////////////////////////////////////////////
def MIPI_CONFIG_Cal(SYS_CLK=330, MIPI_RATE=1500, TxEscClkDiv=16, TXHSByteClkDiv=8):
        T_txesc_clk = 1000 / (SYS_CLK / (TxEscClkDiv+1))
        T_txhsbyte_clk = 1000 / (MIPI_RATE / TXHSByteClkDiv)
        UI = 1000 / MIPI_RATE

        # 标准的时序要求持续时间
        T_std_lp_01 = T_txesc_clk * 2
        T_std_hs_exit = 100
        T_std_hs_prepare = 40 + 4*UI
        T_std_hs_pre_zero = 145 + 10*UI
        T_std_hs_trail = 60 + 4*UI
        T_std_all_accu = T_std_lp_01 + T_std_hs_exit + T_std_hs_pre_zero + T_std_hs_trail

        # MIPI 寄存器默认配置值的时间计算
        T_default_lp_01 = T_txesc_clk * 2
        T_default_hs_exit = 2 * T_txesc_clk
        T_default_hs_prepare = 0 * T_txesc_clk
        T_default_hs_pre_zero = T_default_hs_prepare + 50 * T_txhsbyte_clk
        T_default_hs_trail = 17 * T_txhsbyte_clk
        T_default_all_aacu = T_default_lp_01 + T_default_hs_exit + T_default_hs_pre_zero + T_default_hs_trail

        # 在满足 MIPI 时序要求的情况下, 计算包间隔最小的 MIPI 配置
        T_hs_prepare_config = int(T_std_hs_prepare // T_txesc_clk + (1 if T_std_hs_prepare % T_txesc_clk > 0 else 0)-1)
        T_hs_zero = T_std_hs_pre_zero - (T_hs_prepare_config+1) * T_txesc_clk
        T_hs_zero_config = int(T_hs_zero // T_txhsbyte_clk + (1 if T_hs_zero % T_txhsbyte_clk > 0 else 0))

        T_hs_trail_config = int(T_std_hs_trail // T_txhsbyte_clk + (1 if T_std_hs_trail % T_txhsbyte_clk > 0 else 0))
        T_hs_exit_config = int(T_std_hs_exit // T_txesc_clk + (1 if T_std_hs_exit % T_txesc_clk > 0 else 0))

        # 计算最小配置下 MIPI 耗时
        T_lp_01 = T_txesc_clk * 2
        T_hs_exit = T_hs_exit_config * T_txesc_clk
        T_hs_prepare = T_hs_prepare_config * T_txesc_clk
        T_hs_pre_zero = T_hs_prepare + T_hs_zero_config * T_txhsbyte_clk
        T_hs_trail = T_hs_trail_config * T_txhsbyte_clk
        T_all_aacu = T_lp_01 + T_hs_exit + T_hs_pre_zero + T_hs_trail

        print(f"SYS_CLK: {SYS_CLK}M, MIPI_RATE: {MIPI_RATE}, T_txesc_clk: {T_txesc_clk:5.2f}ns, T_txhsbyte_clk: {T_txhsbyte_clk:5.2f}ns:")
        print(f"\t   Item             : CONFIG |  T_cal |  T_std | T_default")
        print(f"\tT_lpx               : {2:4}   | {T_lp_01:6.2f} | {T_std_lp_01:6.2f} | {T_default_lp_01:6.2f}")
        print(f"\tT_hs_exit    ('d43) : {T_hs_exit_config:4}   | {T_hs_exit:6.2f} | {T_std_hs_exit:6.2f} | {T_default_hs_exit:6.2f}")
        print(f"\tT_hs_prepare ('d44) : {T_hs_prepare_config:4}   | {T_hs_prepare:6.2f} | {T_std_hs_prepare:6.2f} | {T_default_hs_prepare:6.2f}")
        print(f"\tT_hs_pre_zero('d45) : {T_hs_zero_config:4}   | {T_hs_pre_zero:6.2f} | {T_std_hs_pre_zero:6.2f} | {T_default_hs_pre_zero:6.2f}")
        print(f"\tT_hs_trail   ('d46) : {T_hs_trail_config:4}   | {T_hs_trail:6.2f} | {T_std_hs_trail:6.2f} | {T_default_hs_trail:6.2f}")
        print(f"\tT_all_aacu          : {'':5}  | {T_all_aacu:6.2f} | {T_std_all_accu:6.2f} | {T_default_all_aacu:6.2f}")
        print(f"\tTime saving @default:  {T_default_all_aacu-T_all_aacu:6.2f} ns")


if __name__ == '__main__':
    # SYS_CLK_Q = [200, 250, 330, 400]
    # TxEscClkDiv_Q = [11, 14, 16, 16]
    # MIPI_RATE_Q = [800, 1000, 1200, 1500]
    SYS_CLK_Q = [330, 400]
    TxEscClkDiv_Q = [16, 20]
    MIPI_RATE_Q = [1200, 1500]
    TXHSByteClkDiv = 8
    for clk_index in range(len(SYS_CLK_Q)):
        for mipi_index in range(len(MIPI_RATE_Q)):
            MIPI_CONFIG_Cal(SYS_CLK=SYS_CLK_Q[clk_index],
                            TxEscClkDiv=TxEscClkDiv_Q[clk_index],
                            MIPI_RATE=MIPI_RATE_Q[mipi_index],
                            TXHSByteClkDiv=TXHSByteClkDiv)

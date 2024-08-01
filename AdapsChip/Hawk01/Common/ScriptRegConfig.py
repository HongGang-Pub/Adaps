csru_addr = {
    "SYS_CTRL": 0x0004,
    "V_ROLL_NUM": 0x000D,
    "H_ROLL_NUM": 0x000E,
    "MINBIN_THRS": 0x0016,
    "MAXBIN_THRS": 0x0017,
    "TXU_CFG": 0x001C,
    "DEPTHU_CFG1": 0x001F,
    "DEPTHU_CFG2": 0x0020,
    "SPAD_CFG1": 0x0055,
    "SPAD_CFG2": 0x0056,
    # PLL0 & DIV
    "PLL0_DIV1": 0x006A,
    "PLL0_DIV2": 0x006B,
    # PLL1 & DIV
    "PLL1_DIV1": 0x006E,
    "PLL1_DIV2": 0x006F,
    "SYSCLK1M_DIVL": 0x0005,
    "SYSCLK1M_DIVH": 0x0006,
    "TXESC_CLKDIV": 0x0079,
    # MIPI RATE
    "MIPIPLL_LPDH": 0x0074,
    "MIPIPLL_LPDL": 0x0075,
    "MIPIPLL_PPD": 0x0077,
    # MIPI PKTDLY
    "MIPI_TXDLY": 0x001B,
    # MIPI WC & FLNR
    "VC0_FLNR_L": 0x0128,
    "VC0_FLNR_H": 0x0129,
    "VC1_FLNR_L": 0x012A,
    "VC1_FLNR_H": 0x012B,
    "VC0_WC_L": 0x0118,
    "VC0_WC_H": 0x0119,
    "VC1_WC_L": 0x011A,
    "VC1_WC_H": 0x011B,
    # HIST UpSampling
    "UPSMP_CFG": 0x15,
    "TDC_DLY_CFG1": 0x5A,
}

FREQ_Config = {
    # FREF freq
    "REF_24M": {
        # PLL >> SYS_CLK freq
        "PLL0": {
            "250M": {"ID": 3, "FB": 250, "OD": 2}
        },
        "PLL1": {
            "200M": {"ID": 3, "FB": 100, "OD": 1},
            "250M": {"ID": 3, "FB": 125, "OD": 1},
            "330M": {"ID": 2, "FB": 55 , "OD": 0}
        },
        # MIPI >> MIPI rete
        "MIPI": {
            "0.8G": {"NS": 200, "MS": 3, "PS": 2},
            "1.0G": {"NS": 84 , "MS": 2, "PS": 1},
            "1.2G": {"NS": 100, "MS": 2, "PS": 1},
            "1.5G": {"NS": 125, "MS": 2, "PS": 1}
        }
    },

    "REF_25M": {
        "PLL0": {
            "250M": {"ID": 2, "FB": 160, "OD": 2}
        },
        "PLL1": {
            "200M": {"ID": 2, "FB": 64, "OD": 1},
            "250M": {"ID": 2, "FB": 80, "OD": 1},
            "330M": {"ID": 3, "FB": 80, "OD": 0}
        },
        "MIPI": {
            "0.8G": {"NS": 192, "MS": 3, "PS": 2},
            "1.0G": {"NS": 80 , "MS": 2, "PS": 1},
            "1.2G": {"NS": 96 , "MS": 2, "PS": 1},
            "1.5G": {"NS": 120, "MS": 2, "PS": 1}
        }
    }
}

DIV_CONFIG = {
    # 系统频率
    "330M": {"SYSCLK1M_DIVL": 0x49, "SYSCLK1M_DIVH": 0x01, "TXESC_CLKDIV": 0xF0},
    "250M": {"SYSCLK1M_DIVL": 0xF9, "SYSCLK1M_DIVH": 0x00, "TXESC_CLKDIV": 0xCE},
    "200M": {"SYSCLK1M_DIVL": 0xC7, "SYSCLK1M_DIVH": 0x00, "TXESC_CLKDIV": 0xCB}
}

MIPI_PKTDLY_CONFIG = {
    # PCM
    # 工作模式 -> 系统频率 -> MIPI速率 - MIPI_PKT_DLY
    3: {
        "330M": {"0.8G": 0x02, "1.0G": 0x02, "1.2G": 0x02, "1.5G": 0x02},
        "250M": {"0.8G": 0x02, "1.0G": 0x02, "1.2G": 0x02, "1.5G": 0x02},
        "200M": {"0.8G": 0x02, "1.0G": 0x02, "1.2G": 0x02, "1.5G": 0x02}
    },
    # FHR
    2: {
        "330M": {"0.8G": 0x0F, "1.0G": 0x0B, "1.2G": 0x0B, "1.5G": 0x0B},
        "250M": {"0.8G": 0x0D, "1.0G": 0x09, "1.2G": 0x09, "1.5G": 0x09},
        "200M": {"0.8G": 0x0D, "1.0G": 0x09, "1.2G": 0x09, "1.5G": 0x09}
    },
    # PHR
    # 工作模式 -> 系统频率 -> out_bin_num -> MIPI速率
    1: {
        "330M": {1: {"0.8G": 0x05, "1.0G": 0x03, "1.2G": 0x02, "1.5G": 0x02},
                 0: {"0.8G": 0x03, "1.0G": 0x02, "1.2G": 0x02, "1.5G": 0x00}, },
        "250M": {1: {"0.8G": 0x03, "1.0G": 0x01, "1.2G": 0x00, "1.5G": 0x00},
                 0: {"0.8G": 0x02, "1.0G": 0x01, "1.2G": 0x00, "1.5G": 0x00}, },
        "200M": {1: {"0.8G": 0x03, "1.0G": 0x01, "1.2G": 0x00, "1.5G": 0x00},
                 0: {"0.8G": 0x02, "1.0G": 0x01, "1.2G": 0x00, "1.5G": 0x00}, },
    },
    # SPHR
    0: {
        "330M": {1: {"0.8G": 0x03, "1.0G": 0x02, "1.2G": 0x01, "1.5G": 0x00},
                 0: {"0.8G": 0x02, "1.0G": 0x02, "1.2G": 0x00, "1.5G": 0x00}, },
        "250M": {1: {"0.8G": 0x03, "1.0G": 0x00, "1.2G": 0x00, "1.5G": 0x00},
                 0: {"0.8G": 0x01, "1.0G": 0x00, "1.2G": 0x00, "1.5G": 0x00}, },
        "200M": {1: {"0.8G": 0x03, "1.0G": 0x00, "1.2G": 0x00, "1.5G": 0x00},
                 0: {"0.8G": 0x01, "1.0G": 0x00, "1.2G": 0x00, "1.5G": 0x00}, },
    }
}
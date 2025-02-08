import json
import logging

from SelfDefinedPackge import PubMethod, LogerPubMethod
from .Hawk01RegAddr import *
import re
import os


def GetMipiFile(fd_path):
    """
    针对 Dothinker 获取MIPI文件，并按index生成字典，使能顺序读取文件进行数据比对

    Args:
        fd_path: MIPI Data folder dir
    Returns:
        dict: f_dict[key=index, value=mipidata_path]
    """

    file_list = PubMethod.get_fp(fd_path=fd_path, mode=1, match_filter=".txt", f_type="Get MIPI File")
    if len(file_list) == 0:
        raise ValueError("未从指定目录下获取到MIPI文件！！！")

    file_dict = {}
    file_index_list = []
    for index in range(len(file_list)):
        sublist_file = file_list[index].split("-")
        # 针对度信抓包MIPI文件命名格式：mipidata-index-xxxxxxxxx.txt，字典格式为：{index: mipidata_path}
        if len(sublist_file) >= 3:
            file_index = int(file_list[index].split("-")[-2])
            file_dict[file_index] = file_list[index]
            file_index_list.append(file_index)
        else:
            continue

    return file_dict


def GetCsruConfig(config_file, protocol=0) -> dict:
    """
    根据 Hawk01 寄存器配置脚本，获取寄存器配置信息

    Args:
        config_file (str): 脚本路径
        protocol (int): 0: i2c, 1: spi

    Returns:
        dict: 寄存相关配置
    """
    csru_cfg = {
        "MST_MODE": 0,
        "WORK_MODE": 0,
        "TX_FRAME_MODE": 0,
        "V_PXL_OUT_NUM": 1,
        "SCAN_MODE": 0,
        "V_ROLL_NUM": 31,
        "H_ROLL_NUM": 0,
        "H_VLD_SEG": 15,
        "MINBIN_THRS": 0,
        "MAXBIN_THRS": 167,
        "ONE_DT_MODE": 0,
        "PKS_ECHO_NUM": 2,
        "OUT_BIN_NUM": 0,
        "MIPI_PKTDLY": 0,
        "MIPI_FENDDLY": 0,
        "SYSCLK1M_DIV": 249,
        "XCLK1M_DIV": 0,
        "roi_file": "None",
        "MIPI": {
            "VC0_FLNR": 0,
            "VC1_FLNR": 0,
            "VC0_WC": 0,
            "VC1_WC": 0,
            "VC0_THRESHOLD": 0xC0,
            "VC1_THRESHOLD": 0xC0,
            "NS": 84,
            "MS": 2,
            "PS": 1,
            "DataTxThslpxcnt": 2,
            "DataTxThsexitCnt": 2,
            "DataTxThsprepareCnt": 0,
            "DataTxThszeroCnt": 50,
            "DataTxThstrailCnt": 17,
        }
    }

    min_lens = 4 if protocol == 0 else 3
    addr_index = 2 if protocol == 0 else 1
    regs_write = "I2C_Write" if protocol == 0 else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == 0 else "SPI_Block_Write"

    csru_datas = PubMethod.read_file(fname=config_file)

    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check。")

    for line in range(len(csru_datas)):
        _str = csru_datas[line].strip().replace("\n", "").replace("\r", "")  # 去除换行符, 保存时统一保存

        if _str == '' or _str[0:2] == '//':  # 空行 & 整行注释 场景
            continue
        configs = re.split(",|//", _str)
        for i in range(len(configs)):
            configs[i] = configs[i].strip()

        # register_write
        if configs[0] == regs_write:
            if len(configs) < min_lens:
                raise ValueError(f"Script format error.\n"
                                 f"line{line+1}: {_str}")
            addr = int(configs[addr_index], 16)
            config_str = configs[addr_index + 1][0:2]
            register_value = int(config_str, 16)

            if addr == csru_addr['SYS_CTRL']:
                csru_cfg["TX_FRAME_MODE"] = (register_value & 0x80) >> 7
                csru_cfg["V_PXL_OUT_NUM"] = (register_value & 0x40) >> 6
                csru_cfg["SCAN_MODE"] = (register_value & 0x08) >> 3
                csru_cfg["WORK_MODE"] = (register_value & 0x06) >> 1
                csru_cfg["MST_MODE"] = (register_value & 0x01) >> 0
            elif addr == csru_addr['V_ROLL_NUM']:
                csru_cfg["V_ROLL_NUM"] = register_value & 0x1F
            elif addr == csru_addr['H_ROLL_NUM']:
                csru_cfg["H_ROLL_NUM"] = register_value & 0x0F
                csru_cfg["H_VLD_SEG"] = (register_value & 0xF0) >> 4
            elif addr == csru_addr['MINBIN_THRS']:
                csru_cfg["MINBIN_THRS"] = register_value
            elif addr == csru_addr['MAXBIN_THRS']:
                csru_cfg["MAXBIN_THRS"] = register_value
            elif addr == csru_addr['TXU_CFG']:
                csru_cfg["ONE_DT_MODE"] = register_value & 0x01
            elif addr == csru_addr['DEPTHU_CFG1']:
                csru_cfg["OUT_BIN_NUM"] = (register_value & 0x10) >> 4
            elif addr == csru_addr['DEPTHU_CFG2']:
                csru_cfg["PKS_ECHO_NUM"] = (register_value & 0x0E) >> 1
            elif addr == csru_addr['MIPI_TXDLY']:
                csru_cfg["MIPI_PKTDLY"] = register_value & 0x3F
                csru_cfg["MIPI_FENDDLY"] = (register_value & 0xB0) >> 6
            elif addr == csru_addr['MIPIPLL_LPDH']:
                csru_cfg["MIPI"]["NS"] = (csru_cfg["MIPI"]["NS"] & (0xFFFF-0xFF00)) + ((register_value & 0x01) << 8)
            elif addr == csru_addr['MIPIPLL_LPDL']:
                csru_cfg["MIPI"]["NS"] = (csru_cfg["MIPI"]["NS"] & (0xFFFF-0x00FF)) + (register_value << 0)
            elif addr == csru_addr['MIPIPLL_PPD']:
                csru_cfg["MIPI"]["MS"] = (register_value & 0xE0) >> 5
                csru_cfg["MIPI"]["PS"] = register_value & 0x1F
            elif addr == csru_addr['VC0_FLNR_L']:
                csru_cfg["MIPI"]["VC0_FLNR"] = (csru_cfg["MIPI"]["VC0_FLNR"] & (0xFFFF-0x00FF)) + (register_value << 0)
            elif addr == csru_addr['VC0_FLNR_H']:
                csru_cfg["MIPI"]["VC0_FLNR"] = (csru_cfg["MIPI"]["VC0_FLNR"] & (0xFFFF-0xFF00)) + (register_value << 8)
            elif addr == csru_addr['VC1_FLNR_L']:
                csru_cfg["MIPI"]["VC1_FLNR"] = (csru_cfg["MIPI"]["VC1_FLNR"] & (0xFFFF-0x00FF)) + (register_value << 0)
            elif addr == csru_addr['VC1_FLNR_H']:
                csru_cfg["MIPI"]["VC1_FLNR"] = (csru_cfg["MIPI"]["VC1_FLNR"] & (0xFFFF-0xFF00)) + (register_value << 8)
            elif addr == csru_addr['VC0_WC_L']:
                csru_cfg["MIPI"]["VC0_WC"] = (csru_cfg["MIPI"]["VC0_WC"] & (0xFFFF-0x00FF)) + (register_value << 0)
            elif addr == csru_addr['VC0_WC_H']:
                csru_cfg["MIPI"]["VC0_WC"] = (csru_cfg["MIPI"]["VC0_WC"] & (0xFFFF-0xFF00)) + (register_value << 8)
            elif addr == csru_addr['VC1_WC_L']:
                csru_cfg["MIPI"]["VC1_WC"] = (csru_cfg["MIPI"]["VC1_WC"] & (0xFFFF-0x00FF)) + (register_value << 0)
            elif addr == csru_addr['VC1_WC_H']:
                csru_cfg["MIPI"]["VC1_WC"] = (csru_cfg["MIPI"]["VC1_WC"] & (0xFFFF-0xFF00)) + (register_value << 8)
            elif addr == csru_addr["VC0_THRESHOLD"]:
                csru_cfg["MIPI"]["VC0_THRESHOLD"] = register_value
            elif addr == csru_addr["VC1_THRESHOLD"]:
                csru_cfg["MIPI"]["VC1_THRESHOLD"] = register_value
            elif addr == csru_addr["THS_EXIT"]:
                csru_cfg["MIPI"]["DataTxThsexitCnt"] = register_value
            elif addr == csru_addr["THS_PREPARE"]:
                csru_cfg["MIPI"]["DataTxThsprepareCnt"] = register_value
            elif addr == csru_addr["THS_ZERO"]:
                csru_cfg["MIPI"]["DataTxThszeroCnt"] = register_value
            elif addr == csru_addr["THS_TRAIL"]:
                csru_cfg["MIPI"]["DataTxThstrailCnt"] = register_value
        elif configs[0] == roisram_write:
            if len(configs) < 5:
                raise ValueError(f"Script format error.\n"
                                 f"line{line+1}: {_str}")
            roi_name = configs[4]
            csru_cfg["roi_file"] = roi_name
        else:
            continue
            # raise ValueError(f"The script file format is incorrect: line {line+1}: {_str}")
    return csru_cfg


def CalPkgNum(hawk01_config):
    """
    非多帧合一时，一次rolling包的数量
    Args:
        hawk01_config (dict): 寄存配置信息

    Returns:
        int: 非多帧合一时，一次rolling包的数量
    """

    work_mode = hawk01_config["WORK_MODE"]
    h_vld_seg = hawk01_config["H_VLD_SEG"]
    v_pixel_out_num = 6 if hawk01_config["V_PXL_OUT_NUM"] == 1 else 1

    if work_mode == 2 or work_mode == 3:
        pkg_num = (h_vld_seg + 1) * v_pixel_out_num * 4 + 2
    else:
        pkg_num = (h_vld_seg + 1) * 16 + 2
    return pkg_num


def CalMipiFlnrAndWC(csru_cfg):
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


def GenerateHawkRegConfig(hawk01_config: dict, reg_cfg_fp="./Hawk01RegConfig.py"):
    """
    本方法主要实现功能为: 基于基准脚本以及最新的配置, 生成新的 Hawk 配置脚本
    主要包含以下功能:
        1. 根据 hawk01_config["SYS_CLK"] 配置, 配置 PLL1频率 及 与之相关的分频寄存器
        2. 根据 hawk01_config["MIPI_RATE"] 配置, 配置 MIPI 速率相关的寄存器
        3. 根据 hawk01_config[""] 配置 MIPI WC & FLNR寄存器
        4. 根据 hawk01_config[""] 配置 MIPI_TXDLY[5:0] -> MIPI_PKTDLY
        5. 根据 hawk01_config["roi_save_n"] 配置 block_write
    """

    with open(reg_cfg_fp, 'r', encoding='utf-8') as file:
        content = file.read()
        local_scope = locals()
        exec(content, globals(), local_scope)
        FREQ_Config = local_scope["FREQ_Config"]
        DIV_CONFIG = local_scope["DIV_CONFIG"]
        MIPI_PKTDLY_CONFIG = local_scope["MIPI_PKTDLY_CONFIG"]
    # ----------------------------------------------------------------------------------------
    # initial
    # ----------------------------------------------------------------------------------------
    protocol = hawk01_config["protocol"]
    min_lens = 4 if protocol == 0 else 3
    addr_index = 2 if protocol == 0 else 1
    regs_write = "I2C_Write" if protocol == 0 else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == 0 else "SPI_Block_Write"

    ref_cfg_file = hawk01_config["ref_cfg_file"]
    if not os.path.exists(ref_cfg_file):
        raise ValueError("The reference config file does not exist!")

    # ----------------------------------------------------------------------------------------
    # Calculate Register Value
    # ----------------------------------------------------------------------------------------

    # MIPI FLNR & WC
    # ////////////////////////////////////////////////////////////////////////////
    # 将界面上无配置入口的内容同步到 hawk01_config
    csru_cfg = GetCsruConfig(ref_cfg_file, protocol)
    hawk01_config["ONE_DT_MODE"] = csru_cfg["ONE_DT_MODE"]
    hawk01_config["TX_FRAME_MODE"] = csru_cfg["TX_FRAME_MODE"]

    WC, FLNR = CalMipiFlnrAndWC(hawk01_config)
    if FLNR >= 8192:
        logging.warning(f"FLNR {FLNR} is greater than 8192, TX_FRAME_MODE will set 0.")
        hawk01_config['TX_FRAME_MODE'] = 0
        WC, FLNR = CalMipiFlnrAndWC(csru_cfg)

    VC0_FLNR_L = (FLNR & 0x00FF) >> 0
    VC0_FLNR_H = (FLNR & 0xFF00) >> 8
    VC1_FLNR_L = (FLNR & 0x00FF) >> 0
    VC1_FLNR_H = (FLNR & 0xFF00) >> 8
    VC0_WC_L = (WC & 0x00FF) >> 0
    VC0_WC_H = (WC & 0xFF00) >> 8
    VC1_WC_L = (WC & 0x00FF) >> 0
    VC1_WC_H = (WC & 0xFF00) >> 8

    # PLL0 config
    # ////////////////////////////////////////////////////////////////////////////
    PLL0_ID = FREQ_Config[hawk01_config['XCLK']]["PLL0"][1]["ID"]
    PLL0_OD = FREQ_Config[hawk01_config['XCLK']]["PLL0"][1]["OD"]
    PLL0_FB = FREQ_Config[hawk01_config['XCLK']]["PLL0"][1]["FB"]
    PLL0_DIV1 = ((PLL0_ID & 0x0007) << 4) + ((PLL0_OD & 0x0003) << 0)
    PLL0_DIV2 = ((PLL0_FB & 0x00FF) << 0)

    # PLL1 config. hawk01_config['SYS_CLK'] = 330M, 250M, 200M
    # ////////////////////////////////////////////////////////////////////////////
    PLL1_ID = FREQ_Config[hawk01_config['XCLK']]["PLL1"][hawk01_config['SYS_CLK']]["ID"]
    PLL1_OD = FREQ_Config[hawk01_config['XCLK']]["PLL1"][hawk01_config['SYS_CLK']]["OD"]
    PLL1_FB = FREQ_Config[hawk01_config['XCLK']]["PLL1"][hawk01_config['SYS_CLK']]["FB"]
    PLL1_DIV1 = ((PLL1_ID & 0x0007) << 4) + ((PLL1_OD & 0x0003) << 0)
    PLL1_DIV2 = ((PLL1_FB & 0x00FF) << 0)

    # DIV config
    # ////////////////////////////////////////////////////////////////////////////
    SYSCLK1M_DIVL = DIV_CONFIG[hawk01_config['SYS_CLK']]["SYSCLK1M_DIVL"]
    SYSCLK1M_DIVH = DIV_CONFIG[hawk01_config['SYS_CLK']]["SYSCLK1M_DIVH"]
    TXESC_CLKDIV = DIV_CONFIG[hawk01_config['SYS_CLK']]["TXESC_CLKDIV"]

    # MIPI_RATE CONFIG. hawk01_config["MIPI_RATE"] = 0.8G, 1.0G, 1.2G, 1.5G
    # ////////////////////////////////////////////////////////////////////////////
    MIPI_NS = FREQ_Config[hawk01_config['XCLK']]["MIPI"][hawk01_config['MIPI_RATE']]["NS"]
    MIPI_MS = FREQ_Config[hawk01_config['XCLK']]["MIPI"][hawk01_config['MIPI_RATE']]["MS"]
    MIPI_PS = FREQ_Config[hawk01_config['XCLK']]["MIPI"][hawk01_config['MIPI_RATE']]["PS"]
    MIPIPLL_LPDH = (MIPI_NS & 0xFF00) >> 8
    MIPIPLL_LPDL = (MIPI_NS & 0x00FF) >> 0
    MIPIPLL_PPD = ((MIPI_MS & 0x0007) << 5) + ((MIPI_PS & 0x001F) << 0)

    # MIPI_PKTDLY
    # ////////////////////////////////////////////////////////////////////////////
    MIPI_PKTDLY = MIPI_PKTDLY_CONFIG[hawk01_config['WORK_MODE']][hawk01_config['SYS_CLK']][
        hawk01_config['MIPI_RATE']] if hawk01_config[
                                           "WORK_MODE"] >= 2 \
        else MIPI_PKTDLY_CONFIG[hawk01_config['WORK_MODE']][hawk01_config['SYS_CLK']][hawk01_config["OUT_BIN_NUM"]][
        hawk01_config['MIPI_RATE']]

    # TDC_DLY_CFG1
    # ////////////////////////////////////////////////////////////////////////////
    PLL_OD = ((PLL1_DIV1 & 0x03) >> 0)  # 0~3: 2，4，6，8
    PHASE_DLY_OPT = 0b011 if PLL_OD == 0 else 0b111

    # ROI length
    # ////////////////////////////////////////////////////////////////////////////
    if hawk01_config["SCAN_MODE"] == 0:
        roi_length = (13 + (hawk01_config["H_VLD_SEG"] + 1) * 6) * (hawk01_config["V_ROLL_NUM"] + 1)
    else:
        roi_length = (13 + (hawk01_config["H_ROLL_NUM"] + 1) * 6) * (hawk01_config["V_ROLL_NUM"] + 1)

    # ----------------------------------------------------------------------------------------
    # Modify the register configuration according to the baseline script.
    # ----------------------------------------------------------------------------------------
    csru_datas = PubMethod.read_file(ref_cfg_file)
    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check.")

    # --------------------------------------------------------
    # 遍历脚本数据
    # --------------------------------------------------------
    for line in range(len(csru_datas)):
        _str = csru_datas[line].strip().replace("\n", "").replace("\r", "")  # 去除换行符, 保存时统一保存
        if _str == '' or _str[0:2] == '//':  # 空行 & 整行注释 场景
            csru_datas[line] = _str
            continue

        configs = re.split(",|//", _str)
        for i in range(len(configs)):
            configs[i] = configs[i].strip()

        # register_write
        if configs[0] == regs_write:
            if len(configs) < min_lens:
                raise ValueError(f"Script format error.\n"
                                 f"line{line}: {_str}")
            addr = int(configs[addr_index], 16)
            config_str = configs[addr_index + 1][0:2]
            register_value = int(config_str, 16)

            # text_annotations = f" //{', '.join(configs[min_lens:])}" if len(configs) > min_lens else None
            index = _str.find("//")
            annotation = _str[index:] if index != -1 else ""

            if addr == csru_addr['SYS_CTRL']:
                register_value = (register_value & (0xFF - 0x80)) + (hawk01_config['TX_FRAME_MODE'] << 7)
                register_value = (register_value & (0xFF - 0x40)) + (hawk01_config["V_PXL_OUT_NUM"] << 6)
                register_value = (register_value & (0xFF - 0x20)) + (hawk01_config["TRG_I_EN"] << 5)
                register_value = (register_value & (0xFF - 0x08)) + (hawk01_config["SCAN_MODE"] << 3)
                register_value = (register_value & (0xFF - 0x06)) + (hawk01_config["WORK_MODE"] << 1)
                register_value = (register_value & (0xFF - 0x01)) + (hawk01_config["MST_MODE"] << 0)
            elif addr == csru_addr['V_ROLL_NUM']:
                register_value = (register_value & (0xFF - 0x1F)) + (hawk01_config["V_ROLL_NUM"] << 0)
            elif addr == csru_addr['H_ROLL_NUM']:
                hawk01_config["H_ROLL_NUM"] = 0 if hawk01_config["SCAN_MODE"] == 0 else hawk01_config["H_ROLL_NUM"]
                register_value = (register_value & (0xFF - 0x0F)) + (hawk01_config["H_ROLL_NUM"] << 0)
                register_value = (register_value & (0xFF - 0xF0)) + (hawk01_config["H_VLD_SEG"] << 4)
            elif addr == csru_addr['UPSMP_CFG']:
                register_value = (register_value & (0xFF - 0x03)) + (hawk01_config["UPSMP_MODE"] << 0)
            elif addr == csru_addr['MINBIN_THRS']:
                register_value = hawk01_config["MINBIN_THRS"]
            elif addr == csru_addr['MAXBIN_THRS']:
                register_value = hawk01_config["MAXBIN_THRS"]
            elif addr == csru_addr['DEPTHU_CFG1']:
                register_value = (register_value & (0xFF - 0x10)) + (hawk01_config["OUT_BIN_NUM"] << 4)
            elif addr == csru_addr['DEPTHU_CFG2']:
                register_value = (register_value & (0xFF - 0x0E)) + (hawk01_config["PKS_ECHO_NUM"] << 1)
            elif addr == csru_addr['MIPI_TXDLY']:
                register_value = (register_value & (0xFF - 0x3F)) + (MIPI_PKTDLY << 0)
            elif addr == csru_addr['TDC_DLY_CFG1']:
                register_value = (register_value & (0xFF - 0x0E)) + (PHASE_DLY_OPT << 1)
            elif addr == csru_addr['SYSCLK1M_DIVL']:
                register_value = SYSCLK1M_DIVL
            elif addr == csru_addr['SYSCLK1M_DIVH']:
                register_value = (register_value & (0xFF - 0x01)) + (SYSCLK1M_DIVH << 0)
            else:
                register_value = PLL0_DIV1 if addr == csru_addr['PLL0_DIV1'] \
                    else PLL0_DIV2 if addr == csru_addr['PLL0_DIV2'] \
                    else PLL1_DIV1 if addr == csru_addr['PLL1_DIV1'] \
                    else PLL1_DIV2 if addr == csru_addr['PLL1_DIV2'] \
                    else TXESC_CLKDIV if addr == csru_addr['TXESC_CLKDIV'] \
                    else MIPIPLL_LPDH if addr == csru_addr['MIPIPLL_LPDH'] \
                    else MIPIPLL_LPDL if addr == csru_addr['MIPIPLL_LPDL'] \
                    else MIPIPLL_PPD if addr == csru_addr['MIPIPLL_PPD'] \
                    else VC0_FLNR_L if addr == csru_addr['VC0_FLNR_L'] \
                    else VC0_FLNR_H if addr == csru_addr['VC0_FLNR_H'] \
                    else VC1_FLNR_L if addr == csru_addr['VC1_FLNR_L'] \
                    else VC1_FLNR_H if addr == csru_addr['VC1_FLNR_H'] \
                    else VC0_WC_L if addr == csru_addr['VC0_WC_L'] \
                    else VC0_WC_H if addr == csru_addr['VC0_WC_H'] \
                    else VC1_WC_L if addr == csru_addr['VC1_WC_L'] \
                    else VC1_WC_H if addr == csru_addr['VC1_WC_H'] \
                    else register_value

            configs[addr_index + 1] = "{:0>2X}".format(register_value)
            csru_datas[line] = f"{', '.join(configs[0: min_lens])} {annotation}"
        # roisram_write
        elif configs[0] == roisram_write:
            if len(configs) < 5:
                raise ValueError(f"Script format error.\n"
                                 f"line{line}: {_str}")
            configs[3] = "{:0>4X}".format(roi_length)
            configs[4] = hawk01_config["roi_name"]
            csru_datas[line] = ", ".join(configs[0:5])
            continue
        else:
            # raise ValueError(f"The script file format is incorrect: line {line+1}: {_str}")
            csru_datas[line] = _str

    # --------------------------------------------------------
    # 增加配置说明
    # --------------------------------------------------------
    config_instruction = "config_instruction"
    config_print = "PRINT"
    if config_instruction in hawk01_config and config_print in hawk01_config[config_instruction]:
        _str = "// "
        _len = len(hawk01_config[config_instruction][config_print])
        for i in range(_len):
            config = hawk01_config[config_instruction][config_print][i]
            if i > 0:
                _str += "; "
            _str += f"{config}: {hawk01_config[config_instruction][config][hawk01_config[config]]}"
        csru_datas.insert(0, _str)  # 根据配置，在行首打印配置信息内容
    PubMethod.data_save(fname=f'{hawk01_config["reg_name"]}.txt',
                        data_list=csru_datas,
                        split='\n',
                        fd_path=hawk01_config["fd_path"])
    return


def ParseHawkRegConfig(script_file=None, protocol=0):
    if not os.path.exists(script_file):
        raise ValueError("The reference config file does not exist!")

    csru_cfg = GetCsruConfig(script_file, protocol)
    _hyper_link = LogerPubMethod.create_file_hyperlink(url=script_file)
    info = f"Parse {_hyper_link}..."
    logging.info(info)
    _str  = "---------------------------<br>"
    _str += "REG_CONFIG<br>"
    _str += "---------------------------<br>"

    info_json = PubMethod.dict_print_format(csru_cfg, indent=2, level=1)

    _str += info_json
    # for key, value in csru_cfg.items():
    #     _str += f"<br> {key:<15}: {value}"
    logging.INFO_PLUS(f'<p><span style="font-family: Consolas; white-space: pre; color: #0076f6">{_str}</span></p>')

    VC0_WC = csru_cfg["MIPI"]["VC0_WC"]
    VC1_WC = csru_cfg["MIPI"]["VC1_WC"]
    VC0_FLNR = csru_cfg["MIPI"]["VC0_FLNR"]
    VC1_FLNR = csru_cfg["MIPI"]["VC1_FLNR"]

    WC, FLNR = CalMipiFlnrAndWC(csru_cfg)
    if VC0_WC != WC or VC1_WC != WC or VC0_FLNR != FLNR or VC1_FLNR != FLNR:
        FLNR_L = (FLNR & 0x00FF) >> 0
        FLNR_H = (FLNR & 0xFF00) >> 8
        WC_L = (WC & 0x00FF) >> 0
        WC_H = (WC & 0xFF00) >> 8
        logging.fatal("MIPI WC or FLNR config error!!! It's should be config: ")
        _str  = " FLNR_L : 0x{:0>2X}<br>".format(FLNR_L)
        _str += " FLNR_H : 0x{:0>2X}<br>".format(FLNR_H)
        _str += " WC_L   : 0x{:0>2X}<br>".format(WC_L)
        _str += " WC_H   : 0x{:0>2X}    ".format(WC_H)
        logging.INFO_PLUS(f'<p><span style="font-family: Consolas; white-space: pre; color: red">{_str}</span></p>')
    pass


if __name__ == '__main__':
    cfg = {}

    GenerateHawkRegConfig(cfg)
    print("Ending")

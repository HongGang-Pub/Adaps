from SelfDefinedPackge import PubMethod
from Hawk.Common.GlobalDef import *
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


def GetCsruConfig(config_file, protocol="i2c") -> dict:
    """
    根据 Hawk 寄存器配置脚本，获取寄存器配置信息

    Args:
        config_file (str): 脚本路径
        protocol (str): i2c or spi

    Returns:
        dict: 寄存相关配置
    """
    csru_cfg = {
        "tx_frame_mode": 0,
        "v_pxl_out_num": 1,
        "scan_mode": 0,
        "work_mode": 0,
        "v_roll_num": 31,
        "h_roll_num": 0,
        "h_vld_seg": 15,
        "minbin_thrs": 0,
        "maxbin_thrs": 167,
        "one_dt_mode": 0,
        "out_bin_num": 0,
    }

    min_lens = 4 if protocol == "i2c" else 3
    addr_index = 2 if protocol == "i2c" else 1
    regs_write = "I2C_Write" if protocol == "i2c" else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == "i2c" else "SPI_Block_Write"

    csru_datas = PubMethod.read_file(fname=config_file)

    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check。")

    # 初始化部分变量
    PXL_SPAD_OUT_EN_L = 0xFF
    PXL_SPAD_OUT_EN_H = 0x01

    for line in range(len(csru_datas)):
        _str = csru_datas[line].strip().replace("\n", "").replace("\r", "")  # 去除换行符, 保存时统一保存

        if _str == '' or _str[0:2] == '//':  # 空行 & 整行注释 场景
            continue
        configs = re.split(",|//", _str)
        for i in range(len(configs)):
            configs[i] = configs[i].strip()

        # register_write
        if configs[0] == regs_write:
            if len(configs) < 4:
                raise ValueError(f"Script format error.\n"
                                 f"line{line}: {_str}")
            addr = int(configs[addr_index], 16)
            config_str = configs[addr_index + 1][0:2]
            register_value = int(config_str, 16)

            if addr == csru_addr['SYS_CTRL']:
                csru_cfg["tx_frame_mode"] = (register_value & 0x80) >> 7
                csru_cfg["v_pxl_out_num"] = (register_value & 0x40) >> 6
                csru_cfg["scan_mode"] = (register_value & 0x08) >> 3
                csru_cfg["work_mode"] = (register_value & 0x06) >> 1
            elif addr == csru_addr['V_ROLL_NUM']:
                csru_cfg["v_roll_num"] = register_value & 0x1F
            elif addr == csru_addr['H_ROLL_NUM']:
                csru_cfg["h_roll_num"] = register_value & 0x0F
                csru_cfg["h_vld_seg"] = (register_value & 0xF0) >> 4
            elif addr == csru_addr['MINBIN_THRS']:
                csru_cfg["minbin_thrs"] = register_value
            elif addr == csru_addr['MAXBIN_THRS']:
                csru_cfg["maxbin_thrs"] = register_value
            elif addr == csru_addr['TXU_CFG']:
                csru_cfg["one_dt_mode"] = register_value & 0x01
            elif addr == csru_addr['DEPTHU_CFG1']:
                csru_cfg["out_bin_num"] = (register_value & 0x10) >> 4

        if configs[0] == roisram_write:
            if len(configs) < 5:
                raise ValueError(f"Script format error.\n"
                                 f"line{line}: {_str}")
            roi_name = configs[4]
            csru_cfg["roi_file"] = roi_name

    # print("\033[1;31;40m寄存器配置信息：\n{}\033[0m".format(csru_cfg))
    return csru_cfg


def cal_pkg_num(cfg):
    """
    非多帧合一时，一次rolling包的数量
    Args:
        cfg (dict): 寄存配置信息

    Returns:
        int: 非多帧合一时，一次rolling包的数量
    """

    work_mode = cfg["work_mode"]
    h_vld_seg = cfg["h_vld_seg"]
    v_pixel_out_num = 6 if cfg["v_pxl_out_num"] == 1 else 1

    if work_mode == 2 or work_mode == 3:
        pkg_num = (h_vld_seg + 1) * v_pixel_out_num * 4 + 2
    else:
        pkg_num = (h_vld_seg + 1) * 16 + 2
    return pkg_num


def CalMipiFlnrAndWC(csru_cfg):
    work_mode = csru_cfg["work_mode"]
    scan_mode = csru_cfg["scan_mode"]
    v_roll_num = csru_cfg["v_roll_num"]
    h_roll_num = csru_cfg["h_roll_num"]
    h_vld_seg = csru_cfg["h_vld_seg"]
    minbin_thrs = csru_cfg["minbin_thrs"]
    maxbin_thrs = csru_cfg["maxbin_thrs"]
    out_bin_num = csru_cfg["out_bin_num"]
    tx_frame_mode = csru_cfg["tx_frame_mode"]
    one_dt_mode = csru_cfg["one_dt_mode"]

    v_pixel_out_num = 6 if csru_cfg["v_pxl_out_num"] == 1 else 1

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
        flnr = 8 * (h_vld_seg + 1 + one_dt_mode) * total_roll_num
    elif work_mode == 1:
        if out_bin_num == 0:
            phr_pl_num = 80 * v_pixel_out_num
        else:
            phr_pl_num = 132 * v_pixel_out_num
        wc = phr_pl_num * 1.5
        flnr = 8 * (h_vld_seg + 1 + one_dt_mode) * total_roll_num

    elif work_mode == 2:
        maxbin = (maxbin_thrs + 1) * 2 - 1
        fhr_pl_num = (maxbin - minbin_thrs + 1) * 2 * 4
        wc = fhr_pl_num * 1.5
        flnr = (v_pixel_out_num * 2 * (h_vld_seg + 1) + one_dt_mode) * total_roll_num
    else:
        wc = 32 * 1.5
        flnr = (v_pixel_out_num * 2 * (h_vld_seg + 1) + one_dt_mode) * total_roll_num
    return int(wc), flnr


def GenerateHawkRegConfig(cfg):
    """
    本方法主要实现功能为: 基于基准脚本以及最新的配置, 生成新的 Hawk 配置脚本
    主要包含以下功能:
        1. 根据 cfg["SYS_FREQ"] 配置, 配置 PLL1频率 及 与之相关的分频寄存器
        2. 根据 cfg["MIPI_RATE"] 配置, 配置 MIPI 速率相关的寄存器
        3. 根据 cfg[""] 配置 MIPI WC & FLNR寄存器
        4. 根据 cfg[""] 配置 MIPI_TXDLY[5:0] -> MIPI_PKTDLY
        5. 根据 cfg["roi_save_n"] 配置 block_write
    """
    protocol = cfg["protocol"]
    min_lens = 4 if protocol == "i2c" else 3
    addr_index = 2 if protocol == "i2c" else 1
    regs_write = "I2C_Write" if protocol == "i2c" else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == "i2c" else "SPI_Block_Write"

    ref_cfg_file = cfg["ref_cfg_file"]
    if not os.path.exists(ref_cfg_file):
        raise ValueError("The reference config file does not exist!")

    csru_cfg = GetCsruConfig(ref_cfg_file, protocol)
    # 将前端配置内容同步到 csru_cfg
    csru_cfg['work_mode'] = cfg["WORK_MODE"]
    csru_cfg['scan_mode'] = cfg["SCAN_MODE"]
    csru_cfg['v_roll_Num'] = cfg["V_ROLL_NUM"]
    csru_cfg['h_roll_Num'] = cfg["H_ROLL_NUM"]
    csru_cfg['h_vld_seg'] = cfg["H_VLD_SEG"]

    # ----------------------------------------------------------------------------------------
    # Calculate Register Value
    # ----------------------------------------------------------------------------------------
    WC, FLNR = CalMipiFlnrAndWC(csru_cfg)
    if FLNR >= 8192:
        csru_cfg['tx_frame_mode'] = 0
        WC, FLNR = CalMipiFlnrAndWC(csru_cfg)

    # MIPI FLNR & WC cal
    VC0_FLNR_L = (FLNR & 0x00FF) >> 0
    VC0_FLNR_H = (FLNR & 0xFF00) >> 8
    VC1_FLNR_L = (FLNR & 0x00FF) >> 0
    VC1_FLNR_H = (FLNR & 0xFF00) >> 8
    VC0_WC_L = (WC & 0x00FF) >> 0
    VC0_WC_H = (WC & 0xFF00) >> 8
    VC1_WC_L = (WC & 0x00FF) >> 0
    VC1_WC_H = (WC & 0xFF00) >> 8
    # MIPI_RATE CONFIG. cfg["MIPI_RATE"] = 0.8G, 1.0G, 1.2G, 1.5G
    MIPIPLL_LPDL = MIPI_RATE_CONFIG[cfg["MIPI_RATE"]]["MIPIPLL_LPDL"]
    MIPIPLL_PPD = MIPI_RATE_CONFIG[cfg["MIPI_RATE"]]["MIPIPLL_PPD"]
    # MIPI_PKTDLY
    MIPI_PKTDLY = MIPI_PKTDLY_CONFIG[cfg['WORK_MODE']][cfg['SYS_FREQ']][cfg['MIPI_RATE']] if cfg["WORK_MODE"] >= 2 \
        else MIPI_PKTDLY_CONFIG[cfg['WORK_MODE']][cfg['SYS_FREQ']][csru_cfg["out_bin_num"]][cfg['MIPI_RATE']]
    # PLL1 and DIV config. cfg['sys_freq'] = 330M, 250M, 200M
    PLL1_DIV1 = PLL1_DIV_CONFIG[cfg['SYS_FREQ']]["PLL1_DIV1"]
    PLL1_DIV2 = PLL1_DIV_CONFIG[cfg['SYS_FREQ']]["PLL1_DIV2"]
    SYSCLK1M_DIVL = PLL1_DIV_CONFIG[cfg['SYS_FREQ']]["SYSCLK1M_DIVL"]
    SYSCLK1M_DIVH = PLL1_DIV_CONFIG[cfg['SYS_FREQ']]["SYSCLK1M_DIVH"]
    TXESC_CLKDIV = PLL1_DIV_CONFIG[cfg['SYS_FREQ']]["TXESC_CLKDIV"]
    # TDC_DLY_CFG1
    PLL_OD = ((PLL1_DIV1 & 0x03) >> 0)  # 0~3: 2，4，6，8
    PHASE_DLY_OPT = 0b011 if PLL_OD == 0 else 0b111

    # ROI length
    if cfg["SCAN_MODE"] == 0:
        roi_length = (13 + (cfg["H_VLD_SEG"] + 1) * 6) * (cfg["V_ROLL_NUM"] + 1)
    else:
        roi_length = (13 + (cfg["H_ROLL_NUM"] + 1) * 6) * (cfg["V_ROLL_NUM"] + 1)

    # ----------------------------------------------------------------------------------------
    # Modify the register configuration according to the baseline script.
    # ----------------------------------------------------------------------------------------
    csru_datas = PubMethod.read_file(ref_cfg_file)
    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check。")

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
            if len(configs) < 4:
                raise ValueError(f"Script format error.\n"
                                 f"line{line}: {_str}")
            addr = int(configs[addr_index], 16)
            config_str = configs[addr_index + 1][0:2]
            register_value = int(config_str, 16)

            # annotation = f" //{', '.join(configs[min_lens:])}" if len(configs) > min_lens else None
            index = _str.find("//")
            annotation = _str[index:] if index != -1 else ""

            if addr == csru_addr['SYS_CTRL']:
                register_value = (register_value & (0xFF - 0x80)) + (csru_cfg['tx_frame_mode'] << 7)
                register_value = (register_value & (0xFF - 0x20)) + (cfg["TRG_I_EN"] << 5)
                register_value = (register_value & (0xFF - 0x08)) + (cfg["SCAN_MODE"] << 3)
                register_value = (register_value & (0xFF - 0x06)) + (cfg["WORK_MODE"] << 1)
                register_value = (register_value & (0xFF - 0x01)) + (cfg["MST_MODE"] << 0)
            elif addr == csru_addr['V_ROLL_NUM']:
                register_value = (register_value & (0xFF - 0x1F)) + (cfg["V_ROLL_NUM"] << 0)
            elif addr == csru_addr['H_ROLL_NUM']:
                register_value = (register_value & (0xFF - 0x0F)) + (cfg["H_ROLL_NUM"] << 0)
                register_value = (register_value & (0xFF - 0xF0)) + (cfg["H_VLD_SEG"] << 4)
            elif addr == csru_addr['UPSMP_CFG']:
                register_value = (register_value & (0xFF - 0x03)) + (cfg["UPSMP_MODE"] << 0)
            elif addr == csru_addr['MIPI_TXDLY']:
                register_value = (register_value & (0xFF - 0x3F)) + (MIPI_PKTDLY << 0)
            elif addr == csru_addr['TDC_DLY_CFG1']:
                register_value = (register_value & (0xFF - 0x0E)) + (PHASE_DLY_OPT << 1)
            else:
                register_value = PLL1_DIV1 if addr == csru_addr['PLL1_DIV1'] \
                    else PLL1_DIV2 if addr == csru_addr['PLL1_DIV2'] \
                    else SYSCLK1M_DIVL if addr == csru_addr['SYSCLK1M_DIVL'] \
                    else SYSCLK1M_DIVH if addr == csru_addr['SYSCLK1M_DIVH'] \
                    else TXESC_CLKDIV if addr == csru_addr['TXESC_CLKDIV'] \
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
            configs[4] = cfg["roi_name"]
            csru_datas[line] = ", ".join(configs[0:5])
            continue
        else:
            csru_datas[line] = _str

    PubMethod.data_save(fname=f'{cfg["config_name"]}.txt',
                        data_list=csru_datas,
                        split='\n',
                        fd_path=cfg["fd_path"])
    return


if __name__ == '__main__':
    cfg = PubMethod.ReadJsonFile('..\HawkGUI\ROIConfig.json')
    GenerateHawkRegConfig(cfg)
    print("Ending")

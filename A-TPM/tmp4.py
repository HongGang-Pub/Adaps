import os

import mplcursors
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import logging
import re

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

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


def read_file(fname: str) -> list:
    """
    获取文件内容

    Args:
        fname(str): file name
    Returns:
        list: 返回列表，若文件不存在，范围空列表
    """
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            data = f.readlines()
        return data
    except FileNotFoundError as msg:
        raise msg


def ArrayImage(array_lst, fd_path=None, fname="ArrayImage", title_list=None,
               nrows=1, ncols=1, cmap='gray', vmin=None, vmax=None):
    """
    并将二维数组成图, 或根据需求保存图片

    成图规则:
        1.根据nrows & ncols 明确了最多能显示的图片数量\n
        2.Array数量大于可成图数量时，仅展示前几张图片\n

    Args:
        array_lst (list): 二维数组列表
        title_list (list): 二维数组标题
        fd_path (str): 文件的存储路径 if fd_path==None，不保存Array，否则保存
        fname (str): 保存图片时，图片名称
        ncols (int): subplots的行数
        nrows (int): subplots的列数
        vmax (int): 图片展示参数
        vmin (int): 图片展示参数
        cmap (str): 图片展示参数

    Returns:
        None: 不返回任何值
    """

    fig, axs = plt.subplots(nrows, ncols)
    image_show_num = nrows * ncols  # 计算总共可显示的图片

    for cnt in range(image_show_num):
        if cnt < len(array_lst):
            index = cnt
            # print(cnt // ncols, cnt % ncols)
            if nrows == 1 and ncols == 1:
                __axs__ = axs
            elif nrows == 1 or ncols == 1:
                __axs__ = axs[cnt]
            else:
                __axs__ = axs[cnt // ncols, cnt % ncols]

            __axs__.imshow(array_lst[index], cmap=cmap, vmin=vmin, vmax=vmax)
            if title_list is None:
                title = "Image {}: max_bin:{}, min_bin:{}, median_bin:{}".format(
                    index, np.max(array_lst[index]), np.min(array_lst[index]), np.median(array_lst[index]))
            else:
                title = title_list[index]

            # --------------------- 配置刻度 --------------------
            __axs__.xaxis.tick_top()  # 设置x坐标轴位置在顶部
            __axs__.xaxis.set_major_locator(MultipleLocator(48))
            __axs__.yaxis.set_major_locator(MultipleLocator(18))
            __axs__.set_title(title)
        else:
            break
    mplcursors.cursor(multiple=True, highlight=True)
    plt.show()


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
        "OUT_BIN_NUM": 0,
        "MIPI_PKTDLY": 0,
        "VC0_FLNR_L": 0,
        "VC0_FLNR_H": 0,
        "VC1_FLNR_L": 0,
        "VC1_FLNR_H": 0,
        "VC0_WC_L": 0,
        "VC0_WC_H": 0,
        "VC1_WC_L": 0,
        "VC1_WC_H": 0,
        "roi_file": "None",
        "MIPI": {
            "NS": 84,
            "MS": 2,
            "PS": 1,
        }
    }

    min_lens = 4 if protocol == 0 else 3
    addr_index = 2 if protocol == 0 else 1
    regs_write = "I2C_Write" if protocol == 0 else "SPI_Write"
    roisram_write = "I2C_Block_Write" if protocol == 0 else "SPI_Block_Write"

    csru_datas = read_file(fname=config_file)

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
            elif addr == csru_addr['MIPIPLL_LPDH']:
                csru_cfg["MIPI"]["NS"] = (register_value & 0x01) * 256 + csru_cfg["MIPI"]["NS"] % 256
            elif addr == csru_addr['MIPIPLL_LPDL']:
                csru_cfg["MIPI"]["NS"] = (csru_cfg["MIPI"]["NS"] // 256) * 256 + register_value
            elif addr == csru_addr['MIPIPLL_PPD']:
                csru_cfg["MIPI"]["MS"] = (register_value & 0xE0) >> 5
                csru_cfg["MIPI"]["PS"] = register_value & 0x1F
            elif addr == csru_addr['MIPI_TXDLY']:
                csru_cfg["MIPI_PKTDLY"] = register_value & 0x3F
            elif addr == csru_addr['VC0_FLNR_L']:
                csru_cfg["VC0_FLNR_L"] = register_value
            elif addr == csru_addr['VC0_FLNR_H']:
                csru_cfg["VC0_FLNR_H"] = register_value
            elif addr == csru_addr['VC1_FLNR_L']:
                csru_cfg["VC1_FLNR_L"] = register_value
            elif addr == csru_addr['VC1_FLNR_H']:
                csru_cfg["VC1_FLNR_H"] = register_value
            elif addr == csru_addr['VC0_WC_L']:
                csru_cfg["VC0_WC_L"] = register_value
            elif addr == csru_addr['VC0_WC_H']:
                csru_cfg["VC0_WC_H"] = register_value
            elif addr == csru_addr['VC1_WC_L']:
                csru_cfg["VC1_WC_L"] = register_value
            elif addr == csru_addr['VC1_WC_H']:
                csru_cfg["VC1_WC_H"] = register_value
        elif configs[0] == roisram_write:
            if len(configs) < 5:
                raise ValueError(f"Script format error.\n"
                                 f"line{line+1}: {_str}")
            roi_name = configs[4]
            csru_cfg["roi_file"] = roi_name
        else:
            raise ValueError(f"The script file format is incorrect: line {line+1}: {_str}")
    return csru_cfg


def GetCsruAndROIConfig(script_file, sramdata_path=None, protocol="i2c") -> dict:
    """
    根据 Hawk 寄存器配置脚本，获取寄存器配置信息

    Args:
        script_file (str): 脚本路径
        sramdata_path (str): SRAMDATA存储路径，用于生成 ROI 文件的路径
        protocol (str): i2c or spi

    Returns:
        dict: 寄存相关配置
    """
    logging.info("获取寄存器配置信息...")
    protocol = 0 if protocol == "i2c" else 1
    hawk01_config = GetCsruConfig(script_file, protocol=protocol)
    hawk01_config["roi_file"] = "{}\\{}.txt".format(sramdata_path, hawk01_config["roi_file"])
    logging.warning("寄存器配置信息：\n  {}".format(hawk01_config))
    return hawk01_config


def ParseRoiMem(hawk01_config, roi_file=None, f_path=None):
    """
    根据寄存器配置解析 ROI 数据
    Args:
        hawk01_config (寄存器配置相关信息):
        roi_file (str): 指定 ROI 文件路径，为 None 时，从cfg中获取 roi_file
        f_path (str): 解析ROI后 masking 成图效果展示

    Returns:
        tuple: zone_roi_mem, msku_roi_mem
    """
    scan_mode = hawk01_config["SCAN_MODE"]
    v_roll_num = hawk01_config["V_ROLL_NUM"]
    h_roll_num = hawk01_config["H_ROLL_NUM"]
    h_vld_seg = hawk01_config["H_VLD_SEG"]

    if roi_file is None:
        roi_file = hawk01_config["roi_file"]
    __roi_data__ = read_file(roi_file)

    roi_mem = []
    zone_roi_mem = []
    msku_roi_mem = []

    if len(__roi_data__[0].strip()) == 2:  # Byte
        for r in range(0, len(__roi_data__) // 2):
            try:
                roi_data = int(__roi_data__[r * 2], 16) + int(__roi_data__[r * 2 + 1], 16) * 256
                roi_mem.append(roi_data)
            except BaseException as e:
                raise ValueError(f"ROI format error:{e}")
    elif len(__roi_data__[0].strip()) == 4:  # Half-work
        for r in range(0, len(__roi_data__)):
            try:
                roi_data = int(__roi_data__[r], 16)
                roi_mem.append(roi_data)
            except BaseException as e:
                raise ValueError(f"ROI format error:{e}")
    else:
        raise ValueError("ROI format error...")

    roi_len = h_vld_seg + 1 if scan_mode == 0 else h_roll_num + 1
    zone_len = roi_len * 6 + 13

    if zone_len * (v_roll_num + 1) != len(roi_mem):
        raise ValueError("ROI data does not match the register configuration, "
                         "Please check ROI or SCAN_MODE, V_ROLL_NUM, H_ROLL_NUM, H_VLD_SEG!!!")

    for v_roll_cnt in range(v_roll_num + 1):
        seg_coor_st_index = v_roll_cnt * zone_len + 13

        zone_mem = roi_mem[seg_coor_st_index - 13:seg_coor_st_index]
        zone_roi_mem.append(zone_mem)

        msku_mem = roi_mem[seg_coor_st_index: seg_coor_st_index + zone_len - 13]
        msku_roi_mem.append(msku_mem)

    return zone_roi_mem, msku_roi_mem


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


def get_fp(fd_path: str, mode: int, match_filter: str, regression: int = 0, f_type: str = "No Define") -> list:
    """
    根据用户自定义的过滤条件，获取指定文件夹下所有符合过滤条件的文件

    Args:
        regression (int): 是否迭代获取当前目录下所有文件夹：0：仅查找当前目录；1：当前目录以及所有子目录
        fd_path(str): Folder_path
        mode(int): 0:根据文件名进行匹配; 1:根据文件类型进行匹配，如：.txt, .doc等
        match_filter(str): 需要匹配的文件名或则文件类型
        f_type(str): 指定获取文件类型，便于error时打印日志

    Returns:
        list: 返回指定路径下满足过滤条件的所有文件的绝对路径
    """

    file_list = []
    if not os.path.exists(fd_path):
        # log = "指定的文件夹不存在，请检查参数: fd_path"
        # print(log)
        # return file_list
        raise ValueError("[{}] 指定的文件夹不存在: {}".format(f_type, fd_path))

    # os.walk()
    if regression == 0:
        files_list = os.listdir(fd_path)
        for file in files_list:
            if re.search(match_filter, os.path.splitext(file)[mode]):
                file_list.append("{}\\{}".format(fd_path, file))
    else:
        for root, dirs, files in os.walk(fd_path):
            for file in files:
                if re.search(match_filter, os.path.splitext(file)[mode]):
                    file_list.append("{}\\{}".format(root, file))

    # Note
    # name = os.path.basename(file_i)   # 文件名 (包含后缀) ps: file_i 为文件绝对路径
    # name_all = os.path.splitext(name) # 分割文件名和后缀
    # name_0 = name_all[0]              # 或者文件名
    return file_list


def GetMipiFile(fd_path):
    """
    针对 Dothinker 获取MIPI文件，并按index生成字典，使能顺序读取文件进行数据比对

    Args:
        fd_path: MIPI Data folder dir
    Returns:
        dict: f_dict[key=index, value=mipidata_path]
    """

    file_list = get_fp(fd_path=fd_path, mode=1, match_filter=".txt", f_type="Get MIPI File")
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


def ChkMipiReliablity(f_dict, pkg_num=None, one_dt_mode=0):
    """
    使用场景：解析 MIPI 包成图或其他时，先 check 是否丢包，丢帧

    Args:
        f_dict (dict): 文件名（字典），按照 key 的升序进行校验
        pkg_num (int): 用于 check 是否丢包, 为 None 时不校验包个数
        one_dt_mode (int): 是否 one_dt_mode

    Returns:
        bool: True or False
    """
    logging.info("MIPI 数据包检查...")
    error = 0
    sub_frame_num = 0

    file_index_list = list(f_dict.keys())
    file_index_list.sort()

    for f_idx in file_index_list:
        sub_frame_num += 1
        file = f_dict[f_idx]
        subframe_data = read_file(file)
        actual_pkg_num = len(subframe_data)

        # 校验包是否为空
        if pkg_num is not None and actual_pkg_num != pkg_num:
            # raise ValueError("数据存在丢包：{}".format(file))
            logging.error("数据存在丢包：{}:实际包数量:{}; 期待包个数:{}".format(file, actual_pkg_num, pkg_num))
            error = 1
            # return False

        """对subframe_info信息进行读取，check是否丢帧"""
        frame_id, vroll_num, hroll_num = GerMipiFrameInfo(file, one_dt_mode)

        if sub_frame_num > 1 and pre_frame_id + 1 != frame_id:
            # raise ValueError("存在丢包：{}->{}, MIPI_{}".format(pre_frame_id, frame_id, f_idx))
            logging.error("存在丢帧：{} -> {}：MIPI_{}".format(pre_frame_id, frame_id, f_idx))
            # return False
            pre_frame_id = frame_id
            error = 1
        else:
            pre_frame_id = frame_id
    if error == 1:
        return False
    else:
        return True


def GetSpecificFile(f_dict, v_roll_num, h_roll_num, mode=0):
    """
    获取指定条件的 MIPI 文件
    Args:
        f_dict (dict): 文件，按照 key 的升序查找符合条件的 mipi 文件
        v_roll_num (int): 需要查找的 v_roll_num
        h_roll_num (int): 需要查找的 h_roll_num
        mode (int): 0: vroll & hroll都相等的；1：vroll相等的；2：hroll相等的；3：不检查，直接返回

    Returns:

    """
    file_index_list = list(f_dict.keys())
    file_index_list.sort()

    for f_idx in file_index_list:
        file = f_dict[f_idx]

        vroll_num, hroll_num, frame_id = GerMipiFrameInfo(file)
        if mode == 0:
            if v_roll_num == vroll_num and h_roll_num == hroll_num:
                return vroll_num, hroll_num, f_idx
        elif mode == 1:
            if v_roll_num == vroll_num:
                return vroll_num, hroll_num, f_idx
        elif mode == 2:
            if h_roll_num == hroll_num:
                return vroll_num, hroll_num, f_idx
        else:
            return vroll_num, hroll_num, f_idx


def GerMipiFrameInfo(file, one_dt_mode=0):
    """
    获取 MIPI 数据的 Frameinfo信息

    Args:
        file (str): MIPI 数据文件
        one_dt_mode (int): one_dt_mode

    Returns:
        list: 返回 Frameinfo 信息
    """
    subframe_data = read_file(file)
    subframe_info = subframe_data[-1].split(" ")
    if one_dt_mode == 0:
        id_l = int(subframe_info[4], 16)  # data_frame_id L
        id_h = int(subframe_info[5], 16)  # data_frame_id H
        # 通过Frame_id检查是否丢帧
        frame_id = id_h * 256 + id_l

        vroll_num = int(subframe_info[7], 16)  # 5'b cur_vroll_num
        hroll_num = int(subframe_info[6], 16) % 16
    else:
        id_l = int(subframe_info[4], 16)  # data_frame_id L
        id_h = int(subframe_info[5], 16)  # data_frame_id H
        # 通过Frame_id检查是否丢帧
        frame_id = id_h * 4096 + id_l

        vroll_num = int(subframe_info[6], 16) >> 6
        hroll_num = int(subframe_info[6], 16) % 16

    return frame_id, vroll_num, hroll_num


def PackageSplit(data: str, bin_number: int = 672, pixel_num: int = 4, PH: int = 4) -> list:
    """
    将单个Package按照 bin_number 配置拆分以pixel为单位

    Args:
        data (str): 包数据
        bin_number (int): 单个 Pixel bin 宽
        pixel_num (int): 每个包的 Pixel 数量
        PH (int): 包头长度

    Returns:
        list: 包拆分后 pixel 数据，为十进制数据
    """
    dt = data.split(" ")
    pixel_data = []
    for i in range(pixel_num):
        index = PH + i * bin_number
        data1 = dt[index: index + bin_number]
        data2 = list(map(lambda x: int(x, 16), data1))
        pixel_data.append(data2)
    return pixel_data


def BinNumberAdd(pkg_data, bin_number=8):
    """
    将每个 Pixel 的 bin_number 数据累加(单个包)
    Args:
        pkg_data (str): 包数据
        bin_number (int): 单个 Pixel bin 宽

    Returns:
        list:  pixel 数据 bin_number 累和
    """
    pixel_num_list = []

    pixel_data = PackageSplit(pkg_data, bin_number=bin_number)  # len = 4
    for per_pixel_data in pixel_data:
        photon = 0
        for number in per_pixel_data:
            photon += number
        pixel_num_list.append(photon)
    return pixel_num_list


def GetPcmDataFromDothinker(file_path, hawk01_config, msku_roi_mem=[]):
    """
    根据 Dothink 的 MIPI 数据解析 PCM

    Args:
        file_path (str): Dothink 抓取的MIPI数据路径
        hawk01_config(dict): 寄存器配置
        msku_roi_mem (list): roi信息

    Returns:
        np.arrays: 二维数组
    """
    v_roll_num = hawk01_config["V_ROLL_NUM"]
    h_vld_seg = hawk01_config["H_VLD_SEG"]
    one_dt_mode = hawk01_config["ONE_DT_MODE"]

    pkg_num = CalPkgNum(hawk01_config=hawk01_config)

    file_dict = GetMipiFile(fd_path=file_path)
    if not ChkMipiReliablity(f_dict=file_dict, pkg_num=pkg_num):
        raise ValueError("MiPi数据错误！！！")

    # PCM 一次rolling, 9个子帧数据, 从其中第 0 帧进行成图
    vroll_num, hroll_num, f_index = GetSpecificFile(f_dict=file_dict, v_roll_num=0, h_roll_num=0, mode=2)

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    spad_array = np.zeros((576, 768))
    spad_data_list = []

    # for vroll_cnt in range(3 + 1):
    for vroll_cnt in range(v_roll_num + 1):
        for pcm_sub in range(9):
            file = file_dict[f_index]
            frame_id, vroll_num, hroll_num = GerMipiFrameInfo(file, one_dt_mode)
            subframe_data = read_file(file)
            for sub_light in range(6):
                if pcm_sub == 0 and sub_light == 0:  # 打印日志
                    logging.info(
                        "MIPI_{:0>5}: vroll_num:{:0>2}, hroll_num:{:0>2}".format(f_index, vroll_num, hroll_num))
                seg_hs = msku_roi_mem[vroll_num][0] >> 10

                for seg_cnt in range(h_vld_seg + 1):
                    h_seg_s = seg_hs + seg_cnt
                    seg_coor_vs = msku_roi_mem[vroll_num][sub_light * (h_vld_seg + 1) + seg_cnt] % 1024

                    col_shift = hroll_num % 3
                    row_shift = (hroll_num // 3 + (3 - seg_coor_vs % 3)) % 3

                    h_s = h_seg_s * 48 + col_shift
                    v_s = seg_coor_vs + row_shift
                    if v_s > 575:
                        continue

                    pkg_index = sub_light * (h_vld_seg + 1) * 4 + seg_cnt * 4

                    for per_seg_pkg_cnt in range(1, 5):
                        pixel_data = BinNumberAdd(subframe_data[pkg_index + per_seg_pkg_cnt - 1])
                        m = 1 if per_seg_pkg_cnt > 2 else 0
                        n = per_seg_pkg_cnt % 2
                        for pixel_cnt in range(4):
                            spad_shift = pixel_cnt * 6
                            spad_array[v_s, h_s + spad_shift + 24 * m + 3 * n] = pixel_data[pixel_cnt]
                            spad_data_list.append(pixel_data[pixel_cnt])
            f_index += 1
    spad_data = np.array(spad_data_list)

    return spad_array, spad_data


def get_pcm_array(script_file, mipi_file, sramdata_path):
    # 获取寄存器配置
    hawk01_config = GetCsruAndROIConfig(script_file, sramdata_path)

    # 获取 msku roi信息
    zone_roi_mem, msku_roi_mem = ParseRoiMem(hawk01_config)

    # 获取 pcm spad arrays
    array, spad_data = GetPcmDataFromDothinker(file_path=mipi_file,
                                               hawk01_config=hawk01_config,
                                               msku_roi_mem=msku_roi_mem)
    return array


def do_work(mipi_file, script_file, sramdata_path, vmin=0, vmax=100):
    array = get_pcm_array(mipi_file=mipi_file, script_file=script_file, sramdata_path=sramdata_path)

    # 成图展示 PCM 灰度图
    # ArrayImageSave(fname="arrays", fd_path="figs")
    name = os.path.basename(mipi_file)  # 文件名 (包含后缀) ps: file_i 为文件绝对路径
    title = os.path.splitext(name)[0]  # 分割文件名和后缀
    ArrayImage(array_lst=[array], title_list=[title])


if __name__ == '__main__':
    script_file = r"D:\Program Files\Software\DothinkTester\Script\Gray_Scale_Mode_reg_config.txt"
    mipi_file = r"C:/Users/honggang.li/Downloads/MipiData"
    sramdata_path = r"D:/Program Files/Software/DothinkTester/SramData"

    do_work(mipi_file, script_file, sramdata_path)

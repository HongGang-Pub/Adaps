import numpy as np

from Hawk.Common.GlobalDef import csru_addr
from SelfDefinedPackge.PubMethod import *
from SelfDefinedPackge.PubMethod import read_file


def ChkMipiReliablity(f_dict, pkg_num=None):
    """
    使用场景：解析 MIPI 包成图或其他时，先 check 是否丢包，丢帧

    Args:
        f_dict (dict): 文件名（字典），按照 key 的升序进行校验
        pkg_num (int): 用于 check 是否丢包, 为 None 时不校验包个数

    Returns:
        bool: True or False
    """

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
            print("数据存在丢包：{}".format(file))
            return False

        """对subframe_info信息进行读取，check是否丢帧"""
        subframe_info = subframe_data[-1].split(" ")
        id_l = int(subframe_info[4], 16)  # data_frame_id L
        id_h = int(subframe_info[5], 16)  # data_frame_id H
        # one_dt_mode == 0
        vroll_num = int(subframe_info[7], 16)  # 5'b cur_vroll_num
        hroll_num = int(subframe_info[6], 16) % 16

        # 通过Frame_id检查是否丢帧
        frame_id = id_h * 256 + id_l

        if sub_frame_num > 1 and pre_frame_id + 1 != frame_id:
            # raise ValueError("存在丢包：{}->{}, MIPI_{}".format(pre_frame_id, frame_id, f_idx))
            print("存在丢帧：{} -> {}：MIPI_{}".format(pre_frame_id, frame_id, f_idx))
            return False
        else:
            pre_frame_id = frame_id

    return True


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


def GerMipiFrameInfo(file):
    """
    获取 MIPI 数据的 Frameinfo信息

    Args:
        file (str): MIPI 数据文件

    Returns:
        list: 返回 Frameinfo 信息
    """
    subframe_data = read_file(file)

    """对subframe_info信息进行读取"""
    subframe_info = subframe_data[-1].split(" ")
    id_l = int(subframe_info[4], 16)  # data_frame_id L
    id_h = int(subframe_info[5], 16)  # data_frame_id H
    vroll_num = int(subframe_info[7], 16)  # 5'b cur_vroll_num
    hroll_num = int(subframe_info[6], 16) % 16
    frame_id = id_h * (2 ^ 12) + id_l

    return vroll_num, hroll_num, frame_id


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
    addr_index = 2 if protocol == "i2c" else 1
    min_lens = 4 if protocol == "i2c" else 3
    block_write = "I2C_Block_Write" if protocol == "i2c" else "SPI_Block_Write"

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
        "seg_hs": 0,
        "h_seg_shift": 0,
        "pxl_spad_out_en": 0x1FF,
        "roi_file": ""
    }

    csru_datas = read_file(fname=script_file)

    if len(csru_datas) == 0:
        raise ValueError("The register configuration file is empty, please check。")

    # 初始化部分变量
    PXL_SPAD_OUT_EN_L = 0xFF
    PXL_SPAD_OUT_EN_H = 0x01

    for sub_data in csru_datas:
        configs = re.split(",|//", sub_data)

        """get_csru_config"""
        if len(configs) > min_lens:
            addr = int(configs[addr_index].strip(), 16)

            if addr == csru_addr['SYS_CTRL']:
                _sys_ctrl = configs[addr_index + 1].strip()[0:3]
                sys_ctrl = int(_sys_ctrl, 16)
                csru_cfg["tx_frame_mode"] = (sys_ctrl & 0x80) >> 7
                csru_cfg["v_pxl_out_num"] = (sys_ctrl & 0x40) >> 6
                csru_cfg["scan_mode"] = (sys_ctrl & 0x08) >> 3
                csru_cfg["work_mode"] = (sys_ctrl & 0x06) >> 1

            if addr == csru_addr['V_ROLL_NUM']:
                _v_roll_num = configs[addr_index + 1].strip()[0:3]
                v_roll_num = int(_v_roll_num, 16)
                csru_cfg["v_roll_num"] = v_roll_num & 0x1F

            if addr == csru_addr['H_ROLL_NUM']:
                _h_roll_num = configs[addr_index + 1].strip()[0:3]
                hroll_num = int(_h_roll_num, 16)
                csru_cfg["h_roll_num"] = hroll_num & 0x0F
                csru_cfg["h_vld_seg"] = (hroll_num & 0xF0) >> 4

            if addr == csru_addr['MINBIN_THRS']:
                _minbin_thrs = configs[addr_index + 1].strip()[0:3]
                minbin_thrs = int(_minbin_thrs, 16)
                csru_cfg["minbin_thrs"] = minbin_thrs

            if addr == csru_addr['MAXBIN_THRS']:
                _maxbin_thrs = configs[addr_index + 1].strip()[0:3]
                maxbin_thrs = int(_maxbin_thrs, 16)
                csru_cfg["maxbin_thrs"] = maxbin_thrs

            if addr == csru_addr['TXU_CFG']:
                _txu_cfg = configs[addr_index + 1].strip()[0:3]
                txu_cfg = int(_txu_cfg, 16)
                csru_cfg["one_dt_mode"] = txu_cfg & 0x01
            # depthu_cfg1
            if addr == csru_addr['DEPTHU_CFG1']:
                _depthu_cfg1 = configs[addr_index + 1].strip()[0:3]
                depthu_cfg1 = int(_depthu_cfg1, 16)
                csru_cfg["out_bin_num"] = (depthu_cfg1 & 0x10) >> 4

            if addr == csru_addr['SPAD_CFG1']:
                _spad_cfg1 = configs[addr_index + 1].strip()[0:3]
                spad_cfg1 = int(_spad_cfg1, 16)
                PXL_SPAD_OUT_EN_L = spad_cfg1
                csru_cfg["pxl_spad_out_en"] = PXL_SPAD_OUT_EN_H * 256 + PXL_SPAD_OUT_EN_L

            if addr == csru_addr['SPAD_CFG2']:
                _spad_cfg2 = configs[addr_index + 1].strip()[0:3]
                spad_cfg2 = int(_spad_cfg2, 16)
                PXL_SPAD_OUT_EN_H = spad_cfg2 >> 7
                csru_cfg["pxl_spad_out_en"] = PXL_SPAD_OUT_EN_H * 256 + PXL_SPAD_OUT_EN_L

        # seg_hs, h_seg_shift
        if sramdata_path is not None and configs[0] == block_write and len(configs) == min_lens + 1:
            roi_name = configs[min_lens].strip()
            roi_file = "{}\\{}.txt".format(sramdata_path, roi_name)
            csru_cfg["roi_file"] = roi_file
            with open(roi_file, 'r', encoding='utf-8') as f1:
                roi_data = f1.readlines()
                seg_hs = int(roi_data[13], 16) // 1024
                csru_cfg["seg_hs"] = seg_hs
                if csru_cfg["scan_mode"] == 1:
                    h_seg_shift = int(roi_data[19], 16) // 1024 - seg_hs
                else:
                    h_seg_shift = 0
                csru_cfg["h_seg_shift"] = h_seg_shift
    print("\033[1;31;40m寄存器配置信息：\n{}\033[0m".format(csru_cfg))
    return csru_cfg


def SpadOutEn(spad_out_en):
    spad_en_list = []
    for i in range(9):
        EN = 1 if spad_out_en & (1 << i) > 0 else 0
        spad_en_list.append(EN)
    OutEN = [spad_en_list[0:3], spad_en_list[3:6], spad_en_list[6:9]]

    spad_out_en_array = np.array(OutEN)
    return spad_out_en_array

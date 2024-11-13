import logging

import numpy as np

from AdapsChip.Hawk01.Hawk01RegAddr import csru_addr
from SelfDefinedPackge.PubMethod import *
from SelfDefinedPackge.PubMethod import read_file
from .HawkPubMethod import GetCsruConfig


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

        frame_id, vroll_num, hroll_num = GerMipiFrameInfo(file)
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
    logging.info("获取寄存器配置信息...")
    protocol = 0 if protocol == "i2c" else 1
    hawk01_config = GetCsruConfig(script_file, protocol=protocol)
    hawk01_config["roi_file"] = "{}\\{}.txt".format(sramdata_path, hawk01_config["roi_file"])
    logging.warning("寄存器配置信息：\n  {}".format(hawk01_config))
    return hawk01_config


def SpadOutEn(spad_out_en):
    spad_en_list = []
    for i in range(9):
        EN = 1 if spad_out_en & (1 << i) > 0 else 0
        spad_en_list.append(EN)
    OutEN = [spad_en_list[0:3], spad_en_list[3:6], spad_en_list[6:9]]

    spad_out_en_array = np.array(OutEN)
    return spad_out_en_array

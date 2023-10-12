from SelfDefinedPackge.PubMethod import *


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


def cal_wc(cfg):
    work_mode = cfg["work_mode"]
    minbin_thrs = cfg["minbin_thrs"]
    maxbin_thrs = cfg["maxbin_thrs"]
    out_bin_num = cfg["out_bin_num"]
    v_pixel_out_num = 6 if cfg["v_pxl_out_num"] == 1 else 1

    if work_mode == 0:
        if out_bin_num == 0:
            sphr_pl_num = 38 * v_pixel_out_num
        else:
            sphr_pl_num = 62 * v_pixel_out_num
        wc = sphr_pl_num * 1.5
    elif work_mode == 1:
        if out_bin_num == 0:
            phr_pl_num = 80 * v_pixel_out_num
        else:
            phr_pl_num = 132 * v_pixel_out_num
        wc = phr_pl_num * 1.5
    elif work_mode == 2:
        maxbin = (maxbin_thrs + 1) * 2 - 1
        fhr_pl_num = (maxbin - minbin_thrs + 1) * 2 * 4
        wc = fhr_pl_num * 1.5
    else:
        wc = 32 * 1.5
    return int(wc)

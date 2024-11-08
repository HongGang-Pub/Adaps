import os
import logging
import numpy as np
import AdapsChip.Hawk01.HawkPubMethod
from SelfDefinedPackge import PubMethod
from AdapsChip.Hawk01 import MipiPubMethod, HawkPubMethod


def GetPcmDataFromSpadisApp(fp, frame_number=1):
    """
    读取 SPADIS App 存储的 .raw格式的数据解析 PCM

    Args:
        fp (str): 文件夹路径
        frame_number (int): 读取帧数，读取多帧时，会将多帧数据求和平均

    Returns:
        np.arrays: 二维数组
    """

    rows = 576  # 图像的行数
    cols = 768  # 图像的列数
    channels = 1  # 图像的通道数，灰度图为1
    tmp_array = np.zeros((576, 768))

    """从指定的文件夹中获取对应的灰度图，用于成图"""
    f1 = PubMethod.get_fp(fd_path=fp, mode=0, match_filter='GrayImage', regression=0, f_type="PCM Imag")
    f_list = []
    for f in f1:
        if os.path.splitext(f)[1] == ".raw":
            f_list.append(f)
            img = np.fromfile(f, dtype='uint32')
            img = img.reshape(rows, cols, channels)
            tmp_array += img[:, :, 0]

            """如果超过设定的融合帧数阈值，停止frame叠加"""
            if len(f_list) == frame_number:
                break

    tmp_array = tmp_array / len(f_list)
    for i in range(576):
        for j in range(768):
            tmp_array[i, j] = round(tmp_array[i, j])

    return tmp_array


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

    pkg_num = AdapsChip.Hawk01.HawkPubMethod.CalPkgNum(hawk01_config=hawk01_config)

    file_dict = HawkPubMethod.GetMipiFile(fd_path=file_path)
    if not MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=pkg_num):
        raise ValueError("MiPi数据错误！！！")

    vroll_num, hroll_num, f_index = MipiPubMethod.GetSpecificFile(f_dict=file_dict, v_roll_num=0, h_roll_num=0, mode=2)

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    spad_array = np.zeros((576, 768))
    spad_data_list = []

    # for vroll_cnt in range(3 + 1):
    for vroll_cnt in range(v_roll_num + 1):
        for pcm_sub in range(9):
            for sub_light in range(6):
                file = file_dict[f_index]
                vroll_num, hroll_num, frame_id = MipiPubMethod.GerMipiFrameInfo(file)
                subframe_data = PubMethod.read_file(file)

                if pcm_sub == 0 and sub_light == 0:  # 打印日志
                    # if qt_trigger != None:
                    #     qt_trigger.emit("MIPI_{}: vroll_num:{}, hroll_num:{}".format(f_index, vroll_num, hroll_num))
                    # logger = logging.getLogger()
                    logging.info("MIPI_{:0>5}: vroll_num:{:0>2}, hroll_num:{:0>2}".format(f_index, vroll_num, hroll_num))
                    # print("MIPI_{}: vroll_num:{}, hroll_num:{}".format(f_index, vroll_num, hroll_num))
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
                        pixel_data = MipiPubMethod.BinNumberAdd(subframe_data[pkg_index + per_seg_pkg_cnt - 1])
                        m = 1 if per_seg_pkg_cnt > 2 else 0
                        n = per_seg_pkg_cnt % 2
                        for pixel_cnt in range(4):
                            spad_shift = pixel_cnt * 6
                            spad_array[v_s, h_s + spad_shift + 24 * m + 3 * n] = pixel_data[pixel_cnt]
                            spad_data_list.append(pixel_data[pixel_cnt])

            f_index += 1
    spad_data = np.array(spad_data_list)

    return spad_array, spad_data

import numpy as np
from SelfDefinedPackge import PubMethod
from AdapsChip.Hawk01 import Hawk01MipiPubMethod, Hawk01PubMethod


def GetFhrDataFromDothinker(file_path, hawk01_config, msku_roi_mem=[]):
    """
    根据 Dothink 的 MIPI 数据解析 FHR，将 bin 累加成灰度图

    Args:
        file_path (str): Dothink 抓取的MIPI数据路径
        hawk01_config(dict): 寄存器配置
        msku_roi_mem (list): roi信息

    Returns:
        np.arrays: 二维数组
    """
    spad_array = np.zeros((576, 768))
    spad_data_list = []

    v_roll_num = hawk01_config["V_ROLL_NUM"]
    h_vld_seg = hawk01_config["H_VLD_SEG"]

    # 根据 SPAD_OUT_EN 配置转换为数组样式
    spad_out_en_array = Hawk01MipiPubMethod.SpadOutEn(spad_out_en=hawk01_config["PXL_SPAD_OUT_EN"])
    pkg_num = Hawk01PubMethod.CalPkgNum(hawk01_config=hawk01_config)

    # 获取 MIPI 文件
    file_dict = Hawk01PubMethod.GetMipiFile(fd_path=file_path)
    if not Hawk01MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=pkg_num):
        raise ValueError("MiPi数据错误!!!")

    # 获取满足条件的文件索引
    vroll_num, hroll_num, f_index = Hawk01MipiPubMethod.GetSpecificMipiFile(f_dict=file_dict, h_roll_num=0)

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    for vroll_cnt in range(v_roll_num + 1):
        file = file_dict[f_index]
        frame_id, vroll_num, hroll_num = Hawk01MipiPubMethod.GerMipiFrameInfo(file)
        seg_hs = msku_roi_mem[vroll_num][0] >> 10

        subframe_data = PubMethod.read_file(file)
        print("MIPI_{}: vroll_num:{}, hroll_num:{}".format(f_index, vroll_num, hroll_num))

        for sub_light in range(6):
            for seg_cnt in range(h_vld_seg + 1):
                h_seg_s = seg_hs + seg_cnt

                seg_coor_vs = msku_roi_mem[vroll_num][sub_light * (h_vld_seg + 1) + seg_cnt] % 1024

                pkg_index = sub_light * (h_vld_seg + 1) * 4 + seg_cnt * 4

                for per_seg_pkg_cnt in range(1, 5):
                    pixel_data = Hawk01MipiPubMethod.BinNumberAdd(pkg_data=subframe_data[pkg_index + per_seg_pkg_cnt - 1],
                                                                  bin_number=672)
                    spad_data_list.extend(pixel_data)

                    m = 1 if per_seg_pkg_cnt > 2 else 0
                    n = per_seg_pkg_cnt % 2  # VC 通道

                    v_s = seg_coor_vs
                    for pixel_cnt in range(4):
                        spad_shift = pixel_cnt * 6
                        h_s = h_seg_s * 48 + spad_shift + 24 * m + 3 * n
                        spad_array[v_s:v_s + 3, h_s:h_s + 3] = spad_out_en_array * pixel_data[pixel_cnt]

        f_index += 1
    spad_data = np.array(spad_data_list)

    return spad_array, spad_data


def GetFhrDataFromDothinker2D(file_path, hawk01_config, msku_roi_mem=[]):
    """
    根据 Dothink 的 MIPI 数据解析 FHR，将 bin 累加成灰度图

    Args:
        file_path (str): Dothink 抓取的MIPI数据路径
        hawk01_config(dict): 寄存器配置
        msku_roi_mem (list): roi信息

    Returns:
        np.arrays: 二维数组
    """
    spad_array = np.zeros((576, 768))
    spad_data_list = []

    scan_mode = hawk01_config["SCAN_MODE"]
    v_roll_num = hawk01_config["V_ROLL_NUM"]
    h_roll_num = hawk01_config["H_ROLL_NUM"] if scan_mode == 1 else 0
    h_vld_seg = hawk01_config["H_VLD_SEG"]

    # 根据 SPAD_OUT_EN 配置转换为数组样式
    spad_out_en_array = Hawk01MipiPubMethod.SpadOutEn(spad_out_en=hawk01_config["PXL_SPAD_OUT_EN"])
    pkg_num = Hawk01PubMethod.CalPkgNum(hawk01_config=hawk01_config)

    # 获取 MIPI 文件
    file_dict = Hawk01PubMethod.GetMipiFile(fd_path=file_path)
    if not Hawk01MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=pkg_num):
        raise ValueError("MiPi数据错误!!!")

    # 获取满足条件的文件索引
    vroll_num, hroll_num, f_index = Hawk01MipiPubMethod.GetSpecificMipiFile(f_dict=file_dict, h_roll_num=0)

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    for vroll_cnt in range(v_roll_num + 1):
        for hroll_cnt in range(h_roll_num + 1):
            file = file_dict[f_index]
            frame_id, vroll_num, hroll_num = Hawk01MipiPubMethod.GerMipiFrameInfo(file)

            seg_hs = msku_roi_mem[vroll_num][hroll_cnt * 6] >> 10

            subframe_data = PubMethod.read_file(file)
            print("MIPI_{}: vroll_num:{}, hroll_num:{}".format(f_index, vroll_num, hroll_num))

            for sub_light in range(6):
                for seg_cnt in range(h_vld_seg + 1):
                    h_seg_s = seg_hs + seg_cnt

                    if h_seg_s > 15:  # 处理二维扫描超边界的场景
                        continue

                    if scan_mode == 0:
                        seg_coor_vs = msku_roi_mem[vroll_num][sub_light * (h_vld_seg + 1) + seg_cnt] % 1024
                    else:
                        seg_coor_vs = msku_roi_mem[vroll_num][hroll_cnt * 6 + sub_light] % 1024

                    pkg_index = sub_light * (h_vld_seg + 1) * 4 + seg_cnt * 4

                    for per_seg_pkg_cnt in range(1, 5):
                        pixel_data = Hawk01MipiPubMethod.BinNumberAdd(pkg_data=subframe_data[pkg_index + per_seg_pkg_cnt - 1],
                                                                      bin_number=672)
                        spad_data_list.extend(pixel_data)

                        m = 1 if per_seg_pkg_cnt > 2 else 0
                        n = per_seg_pkg_cnt % 2  # VC 通道

                        v_s = seg_coor_vs
                        for pixel_cnt in range(4):
                            spad_shift = pixel_cnt * 6
                            h_s = h_seg_s * 48 + spad_shift + 24 * m + 3 * n
                            spad_array[v_s:v_s + 3, h_s:h_s + 3] = spad_out_en_array * pixel_data[pixel_cnt]

            f_index += 1
    spad_data = np.array(spad_data_list)

    return spad_array, spad_data

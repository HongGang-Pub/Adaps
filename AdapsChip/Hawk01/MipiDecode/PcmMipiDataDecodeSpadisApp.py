"""
Spadis App Offline PCM Data数据解码
"""
import os
import matplotlib.pyplot as plt

from SelfDefinedPackge import PubMethod
from AdapsChip.Hawk01 import Hawk01MipiPubMethod, Hawk01PubMethod
from SelfDefinedPackge import ArrayPubMethod, LogerPubMethod
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from SelfDefinedPackge.MatplotExtension import *
import numpy as np


def GetMipiFileSpadisAppOfflineData(fd_path):
    """
    针对 SpadisApp 获取MIPI文件，并按index生成字典，使能顺序读取文件进行数据比对

    Args:
        fd_path: MIPI Data folder dir
    Returns:
        dict: f_dict[key=index, value=mipidata_path]
    """

    file_list = PubMethod.get_fp(fd_path=fd_path, mode=1, match_filter=".pack", f_type="Get MIPI File")
    if len(file_list) == 0:
        raise ValueError("未从指定目录下获取到MIPI文件!!!")

    file_dict = {}
    for index in range(len(file_list)):
        base_name = os.path.basename(file_list[index])   # 文件名 (包含后缀) ps: file_i 为文件绝对路径
        name = os.path.splitext(base_name)[0]            # 分割文件名和后缀
        try:
            file_index = int(name[10:])
            file_dict[file_index] = file_list[index]
        except:
            continue
    return file_dict


def GetMipiFrameData(file, one_dt_mode=0):
    """
    获取 MIPI 数据的 Frameinfo信息

    Args:
        file (str): MIPI 数据文件
        one_dt_mode (int): one_dt_mode

    Returns:
        list: 返回 Frameinfo 信息
    """

    pack_data = np.fromfile(file, dtype='uint16')
    # 利用numpy中array的reshape函数将读取到的数据进行重新排列
    # ini_img = ini_img[::2] + ini_img[1::2]*16
    size = 32 * 4 * 16 * 6
    ini_img = pack_data[0:size]
    frame_data = ini_img.reshape(384, 32)

    frame_id = pack_data[size]
    hroll_num = pack_data[size + 1] & 0x000F
    vroll_num = (pack_data[size + 1] & 0x1F00) >> 8
    return frame_id, vroll_num, hroll_num, frame_data


def GetSpecificFile(f_dict, v_roll_num, h_roll_num, mode=0):
    """
    获取指定条件的 MIPI 文件
    Args:
        f_dict (dict): 文件，按照 key 的升序查找符合条件的 mipi 文件
        v_roll_num (int): 需要查找的 v_roll_num
        h_roll_num (int): 需要查找的 h_roll_num
        mode (int): 0: vroll & hroll都相等的；1: vroll相等的；2: hroll相等的；3: 不检查，直接返回

    Returns:

    """
    file_index_list = list(f_dict.keys())
    file_index_list.sort()

    for f_idx in file_index_list:
        file = f_dict[f_idx]
        frame_id, vroll_num, hroll_num, frame_data = GetMipiFrameData(file)
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


def BinNumberAdd(pkg_data, pixel_number=4, bin_number=8):
    """
    将每个 Pixel 的 bin_number 数据累加(单个包)
    Args:
        pkg_data (str): 包数据
        pixel_number (int): 每个包的 Pixel 数量
        bin_number (int): 单个 Pixel bin 宽

    Returns:
        list:  pixel 数据 bin_number 累和
    """
    pixel_num_list = []

    for pixel_index in range(pixel_number):
        index = pixel_index * bin_number
        photon = np.sum(pkg_data[index: index + bin_number])
        pixel_num_list.append(photon)
    return pixel_num_list


def GetPcmDataFromSpadisAppOfflineData(file_path, hawk01_config, msku_roi_mem=[]):
    """
    根据 Spadis App Offline Data 的 MIPI 数据解析 PCM

    Args:
        file_path (str): MIPI数据路径
        hawk01_config(dict): 寄存器配置
        msku_roi_mem (list): roi信息

    Returns:
        np.arrays: 二维数组
    """
    v_roll_num = hawk01_config["V_ROLL_NUM"]
    h_vld_seg = hawk01_config["H_VLD_SEG"]
    one_dt_mode = hawk01_config["ONE_DT_MODE"]

    file_dict = GetMipiFileSpadisAppOfflineData(fd_path=file_path)

    vroll_num, hroll_num, f_index = GetSpecificFile(f_dict=file_dict, v_roll_num=0, h_roll_num=0, mode=2)

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    img_data_list = []
    img_data = []
    img_cnt = 1
    pkt_cnt = 0
    pkt_num = (v_roll_num + 1) * 9
    pre_frame_id = -1
    for f_idx in file_index_list:
        if img_cnt > img_num:
            break
        file = file_dict[f_idx]
        frame_id, vroll_num, hroll_num, frame_data = GetMipiFrameData(file)
        # print(f"Debug0: f_idx:{f_idx}, pkt_cnt:{pkt_cnt}, frame_id:{frame_id}, vroll_num:{vroll_num}, hroll_num:{hroll_num}")
        # if frame_id != f_idx-1:
        #     print(f"Debug1: f_idx:{f_idx}, pkt_cnt:{pkt_cnt}, frame_id:{frame_id}, vroll_num:{vroll_num}, hroll_num:{hroll_num}")

        if pkt_cnt == 0 and hroll_num != 0:
            continue
        if pkt_cnt == 0 and hroll_num == 0:
            pre_frame_id = frame_id
            img_data.append((frame_id, vroll_num, hroll_num, frame_data))
            pkt_cnt = 1
            # print(f"Debug1: f_idx:{f_idx}, pkt_cnt:{pkt_cnt}, frame_id:{frame_id}, vroll_num:{vroll_num}, hroll_num:{hroll_num}")
            continue
        if pkt_cnt != 0 and frame_id != pre_frame_id+1:
            pkt_cnt = 0
            img_data = []
            # print(f"Debug2: f_idx:{f_idx}, pkt_cnt:{pkt_cnt}, frame_id:{frame_id}, vroll_num:{vroll_num}, hroll_num:{hroll_num}")
            continue
        else:
            img_data.append((frame_id, vroll_num, hroll_num, frame_data))
            pre_frame_id = frame_id
        if pkt_cnt == pkt_num - 1:
            img_data_list.append(img_data)
            pkt_cnt = 0
            img_data = []
            print(f"INFO: img_cnt:{img_cnt}, f_idx:{f_idx}, pkt_cnt:{pkt_cnt}, frame_id:{frame_id}, vroll_num:{vroll_num}, hroll_num:{hroll_num}")
            img_cnt += 1
        else:
            pkt_cnt += 1

    spad_array_list = []
    img_cnt = 0
    for img_data in img_data_list:
        img_cnt += 1
        if img_cnt > img_num:
            break
        if img_list is not None and img_cnt not in img_list:
            continue
        print(f"Do {img_cnt} img frame data!")
        spad_array = np.zeros((576, 768))
        spad_array1 = np.zeros((576, 768))
        for vroll_cnt in range(v_roll_num + 1):
            for pcm_sub in range(9):
                idx = vroll_cnt * 9 + pcm_sub
                frame_id, vroll_num, hroll_num, frame_data = img_data[idx]
                for sub_light in range(6):
                    seg_hs = msku_roi_mem[vroll_num][0] >> 10

                    for seg_cnt in range(h_vld_seg + 1):
                        h_seg_s = seg_hs + seg_cnt
                        seg_coor_vs = msku_roi_mem[vroll_num][sub_light * (h_vld_seg + 1) + seg_cnt] % 1024
                        # print(f"idx:{idx}, sub_light:{sub_light}, seg_cnt: {seg_cnt}, vroll_num:{vroll_num}, h_seg_s:{h_seg_s}, seg_coor_vs:{seg_coor_vs}")

                        col_shift = hroll_num % 3
                        row_shift = (hroll_num // 3 + (3 - seg_coor_vs % 3)) % 3

                        h_s = h_seg_s * 48 + col_shift
                        v_s = seg_coor_vs + row_shift
                        if v_s > 575:
                            continue

                        for per_seg_pkg_cnt in range(0, 4):
                            vc_id = per_seg_pkg_cnt % 2
                            m = 1 if per_seg_pkg_cnt > 1 else 0
                            pkg_base_index = (2 * (h_vld_seg + 1) * 6) * vc_id
                            pkg_idx_shift = sub_light * (h_vld_seg + 1) * 2 + seg_cnt * 2 + per_seg_pkg_cnt // 2

                            a, b, c, frame_data = img_data[idx]
                            pixel_data = BinNumberAdd(frame_data[pkg_base_index + pkg_idx_shift])
                            # for pixel_cnt in range(4):
                            #     spad_shift = pixel_cnt * 6
                            #     v = v_s
                            #     h = h_s + spad_shift + 24 * m + 3 * vc_id
                            #     spad_array[v, h] = pixel_data[pixel_cnt]
                                # spad_array1[v, h] = pixel_data[pixel_cnt]
                                # spad_array[v, h] = sub_light*2+pcm_sub*2

                            if vc_id == 0:
                                a, b, c, frame_data = img_data[idx-1]
                            else:
                                a, b, c, frame_data = img_data[idx]
                            pixel_data = BinNumberAdd(frame_data[pkg_base_index + pkg_idx_shift])
                            for pixel_cnt in range(4):
                                spad_shift = pixel_cnt * 6
                                v = v_s
                                h = h_s + spad_shift + 24 * m + 3 * vc_id
                                spad_array1[v, h] = pixel_data[pixel_cnt]

        # spad_array_list.append(spad_array)
        spad_array_list.append(spad_array1)
    return spad_array_list


def get_pcm_array(script_file, mipi_file, sramdata_path):
    # 获取寄存器配置
    hawk01_config = Hawk01MipiPubMethod.GetCsruAndROIConfig(script_file, sramdata_path)

    # 获取 msku roi信息
    zone_roi_mem, msku_roi_mem = MskuPubMethod.ParseRoiMem(hawk01_config)

    # 获取 pcm spad arrays
    arrays = GetPcmDataFromSpadisAppOfflineData(file_path=mipi_file,
                                                hawk01_config=hawk01_config,
                                                msku_roi_mem=msku_roi_mem)
    return arrays


def do_work(mipi_file, script_file, sramdata_path, vmin=0, vmax=100):
    arrays = get_pcm_array(mipi_file=mipi_file, script_file=script_file, sramdata_path=sramdata_path)

    # 成图展示 PCM 灰度图
    idx = 0
    for arr in arrays:
        plt.figure()
        title = "Image {}: max_bin:{}, min_bin:{}, median_bin:{}".format(idx, np.max(arr), np.min(arr), np.median(arr))
        # plt.imshow(arr, vmin=vmin, vmax=vmax)
        plt.imshow(arr, vmin=vmin, vmax=vmax, cmap="gray")
        plt.title(title)
        fig = plt.gcf()
        fig.savefig(f"figs\\img{idx}", dpi=200)
        idx += 1
        plt.close()
    # cursor = mplcursors.cursor(multiple=True)
    # plt.show()
    # idx = 0
    # for arr in arrays:
    #     idx += 1
    #     cv2.imshow(f"img{idx}", arr)
    # # 等待按键关闭窗口
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    LogerPubMethod.LoggingForConsoleFormat()

    script_file = r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v5.2-189-g1132\OfflineData\DecodeData\Script\gray_wide.txt"
    mipi_file = r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v5.2-189-g1132\OfflineData\DecodeData"
    sramdata_path = r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v5.2-189-g1132\OfflineData\DecodeData\SramData"

    GetMipiFrameData(r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v5.2-189-g1132\OfflineData\DecodeData\DecodeData1.pack")

    # file_dict = GetMipiFileSpadisAppOfflineData(fd_path=mipi_file)
    # vroll_num, hroll_num, f_index = GetSpecificFile(f_dict=file_dict, v_roll_num=0, h_roll_num=0, mode=2)

    img_num = 40
    img_list = None
    do_work(mipi_file, script_file, sramdata_path, vmin=0, vmax=3000)

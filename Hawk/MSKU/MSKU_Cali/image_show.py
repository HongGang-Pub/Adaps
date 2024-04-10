"""
本文件仅用于将.raw图片中指定段的光强展示
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import SelfDefinedPackge.PubMethod
import mplcursors

def get_pcm_file(fp: str, frame_num=5) -> dict:
    """
    从指定的文件夹中获取对应的灰度图，用于成图

    Args:
        fp (str): 文件路径
        frame_num (int): 采用第几帧数据进行标定

    Returns:
        dict: type(dict): {索引：文件路径}
    """
    f1 = SelfDefinedPackge.PubMethod.get_fp(fd_path=fp, mode=0, match_filter='GrayImage', regression=1, f_type="PCM Imag")
    get_frame_cnt = 1

    f_dict = {}
    for f in f1:
        if os.path.splitext(f)[1] == ".raw":
            f_name = os.path.split(f)[1]
            index = float(f_name.split("_")[3])
            if index in f_dict:
                get_frame_cnt += 1
                if get_frame_cnt > frame_num:
                    continue
            else:
                get_frame_cnt = 1
            f_dict[index] = f
    return f_dict


def SegAccumulation(array: np.ndarray, accum_seg: int = 1) -> np.ndarray:
    """
    将面阵按指定的段数进行累加(步径为1)

    Args:
        array (np.ndarray): image数组，shape:567 * 768 * 1
        accum_seg (int): 累加的段数。eg: 1*48 spad 累加

    Returns:
        np.ndarray: 数组，shape:567 * 16 * 1
    """
    seg_sum_array = np.zeros((576, 16))

    for i in range(0, 16):
        if i + accum_seg - 1 < 16:
            seg = array[:, i * 48:(i + accum_seg) * 48]
            seg_sum_array[:, i:i + 1] = np.sum(seg, axis=1)
        else:
            break
    return seg_sum_array


def SCANMODE_1D(img) -> None:
    """
    1D Scan Mode下，根据配置标定ROI

    Args:
        img (np.ndarray): image

    Returns:
        tuple: 返回多个值
    """
    per_img_roi_data = []  # 存储一张PCM灰度图获取的ROI数据

    # 1D scan_mode将 spad 按照 576*48 (共16段划分)，然后累和
    seg_sum_array = SegAccumulation(array=img, accum_seg=1)

    # 按段纵向开窗，找到每段rolling开6行pixel的spad的起始点
    for seg_num in range(Seg_range[0], Seg_range[1]):
        plt.figure()

        # seg_array = np.convolve(seg_sum_array[:, seg_num], [1, 1, 1, 1, 1, 1], mode='same')
        seg_array = seg_sum_array[:, seg_num]
        plt.subplot(1, 1, 1)
        plt.plot(seg_sum_array[:, seg_num])
        # plt.subplot(1, 2, 2)
        # plt.plot(seg_array)
    return


def do_work():
    # file_dict = get_pcm_file(fd_path, frame_num_sel)

    # 利用numpy的fromfile函数读取raw文件，并指定数据格式
    # image = file_dict[float(channel_sel)]
    image = r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v4.0-150-g89df\SavedImages\ROI_18_3_Vs=0_PCM_2024_04_08_06_02_10\GrayImage_frame_1_1097715546.raw"
    ini_img = np.fromfile(image, dtype='uint32')
    # 利用numpy中array的reshape函数将读取到的数据进行重新排列
    ini_img = ini_img.reshape(576, 768, 1)
    plt.imshow(ini_img, vmax=50, cmap="gray")
    # SCANMODE_1D(ini_img)
    cursor = mplcursors.cursor(multiple=True)
    plt.show()
    return


if __name__ == '__main__':
    channel_sel = 1             # 指定通道 (如采集的第 1 通道，则配置为 1)
    frame_num_sel = 5           # 指定使用第几帧数据
    Seg_range = []          # 指定需要显示光强的 segment
    fd_path = r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v4.0-150-g89df\SavedImages\ROI_18_3_PCM_2024_04_08_06_02_10\GrayImage_frame_1_1097715546.raw"
    do_work()

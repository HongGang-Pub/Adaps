import numpy as np
import matplotlib.pyplot as plt


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
    # 利用numpy的fromfile函数读取raw文件，并指定数据格式
    ini_img = np.fromfile(image, dtype='uint32')
    # 利用numpy中array的reshape函数将读取到的数据进行重新排列
    ini_img = ini_img.reshape(576, 768, 1)
    plt.imshow(ini_img)
    SCANMODE_1D(ini_img)
    plt.show()
    return


if __name__ == '__main__':
    Seg_range = [0, 3]
    image = r"C:\Users\honggang.li\Downloads\B12_OD20B衰减片\B12_OD20B衰减片\B12_半圈离焦\GrayImage_frame_1_3123973902.raw"
    do_work()

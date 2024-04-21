"""
本文件用于查看指定通道数据的光条分布，
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import SelfDefinedPackge.PubMethod
import mplcursors

def get_pcm_file(fp: str, frame_num) -> list:
    """
    从指定的文件夹中获取对应的灰度图，用于成图

    Args:
        fp (str): 文件路径
        frame_num (list): 采用第几帧数据进行标定

    Returns:
        list: {文件路径}
    """
    f1 = SelfDefinedPackge.PubMethod.get_fp(fd_path=fp, mode=0, match_filter='GrayImage', regression=1, f_type="PCM Imag")
    get_frame_cnt = 1

    # f_dict = {}
    f_list = []
    for f in f1:
        if os.path.splitext(f)[1] == ".raw":
            f_name = os.path.basename(f)
            f_name = os.path.splitext(f_name)[0]

            index = float(f_name.split("_")[3])
            if index == channel_sel:
                if frame_num[0] <= get_frame_cnt <= frame_num[1]:
                    f_list.append(f)
                    print(f"File_{get_frame_cnt}: {f}")
                else:
                    get_frame_cnt += 1
            else:
                continue

    return f_list


def shift_display(images) -> None:
    """
    1D Scan Mode下，根据配置标定ROI
    """

    handle = []
    for image in images:
        plt.figure()
        for coor in axis:
            plt.subplot(1, 1, 1)
            hdl, = plt.plot(image[:, coor], label=f"coor:{coor}")
            handle.append(hdl)
            # print(f"coor[{coor}] = {np.max(image[:, coor])}")

    font1 = {'family': 'SimHei',
             'weight': 'normal',
             'size': 12, }  # 设置图例大小位置
    legend = plt.legend(handles=handle, prop=font1)
    return


def do_work():
    file_list = get_pcm_file(fd_path, frame_num_sel)

    image = np.zeros((576, 768, 1))

    for file in file_list:
        # 利用numpy的fromfile函数读取raw文件，并指定数据格式
        ini_img = np.fromfile(file, dtype='uint32')
        # 利用numpy中array的reshape函数将读取到的数据进行重新排列
        ini_img = ini_img.reshape(576, 768, 1)
        image += ini_img

    image = image / len(file_list)
    plt.figure()
    plt.imshow(image)
    shift_display([image])
    cursor = mplcursors.cursor(multiple=True)
    plt.show()
    return


if __name__ == '__main__':
    channel_sel = 10             # 指定通道 (如采集的第 1 通道，则配置为 1)
    frame_num_sel = [0, 10]     # 指定使用某几帧数据 (如第0帧到第10帧，则设置为 [0, 10])
    axis = [100, 200, 300]      # 指定 X 轴坐标
    fd_path = r"C:\Users\honggang.li\Downloads\HawkCaliData\B17_ROI_data"

    do_work()

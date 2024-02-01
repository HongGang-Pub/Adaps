import numpy as np
import matplotlib.pyplot as plt
import os
import SelfDefinedPackge.PubMethod


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


def shift_display(images) -> None:
    """
    1D Scan Mode下，根据配置标定ROI

    Args:
        images (list): image

    Returns:
        tuple: 返回多个值
    """
    # 1D scan_mode将 spad 按照 576*48 (共16段划分)，然后累和
    if mode == 0:
        for coor in axis:
            plt.figure()
            for image in images:
                plt.subplot(1, 1, 1)
                plt.plot(image[:, coor])
    else:
        for image in images:
            plt.figure()
            for coor in axis:
                plt.subplot(1, 1, 1)
                plt.plot(image[:, coor])
    return


def do_work():
    file_dict = get_pcm_file(fd_path, frame_num)

    images = []

    for file in file_dict.values():
        # 利用numpy的fromfile函数读取raw文件，并指定数据格式
        ini_img = np.fromfile(file, dtype='uint32')
        # 利用numpy中array的reshape函数将读取到的数据进行重新排列
        ini_img = ini_img.reshape(576, 768, 1)
        images.append(ini_img)
    shift_display(images)
    plt.show()
    return


if __name__ == '__main__':
    mode = 1    # mode=0: 查看帧与帧之间的偏移量， mode=1: 查看同一个光条的不同位置的光强
    frame_num = 3   # 指定使用第几帧数据
    fd_path = r"C:\Users\honggang.li\Downloads\SavedImages(3)\B06_ROI_data_800mm_20240131"
    assign_frame = [1, 5]
    axis = [100, 200, 300]

    do_work()

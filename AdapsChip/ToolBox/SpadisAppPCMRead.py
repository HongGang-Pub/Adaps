"""
本文件仅用于将.raw图片中指定段的光强展示
"""
import logging

from SelfDefinedPackge.MatplotExtension import *
import numpy as np
import matplotlib.pyplot as plt


def do_work(image):
    try:
        ini_img = np.fromfile(image, dtype='uint32')
        # 利用numpy中array的reshape函数将读取到的数据进行重新排列
        # ini_img = ini_img[::2] + ini_img[1::2]*16
        ini_img = ini_img.reshape(576, 768, 1)
        plt.imshow(ini_img, vmax=50, cmap="gray")
        # SCANMODE_1D(ini_img)
        cursor = mplcursors.cursor(multiple=True)
        plt.show()
    except BaseException as e:
        logging.error(f"Fatal: {e}")
    return


if __name__ == '__main__':
    image = r"C:\Users\honggang.li\Downloads\Decode_Result_Depth_0.raw"
    do_work(image)

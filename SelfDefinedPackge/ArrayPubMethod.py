import os
import numpy as np
import matplotlib.pyplot as plt
from SelfDefinedPackge.MatplotExtension import *
from matplotlib.ticker import MultipleLocator


def ArrayImageSave(fname, fd_path):
    if fd_path != "None":
        if not os.path.exists(fd_path):
            # 目录不存在，进行创建操作
            os.makedirs(fd_path)
        fp = "{}\\{}.png".format(fd_path, fname)
        plt.savefig(fp, dpi=200)


def ArrayImage(array_lst, fd_path=None, fname="ArrayImage", title_list=None,
               nrows=1, ncols=1, cmap='gray', vmin=None, vmax=None):
    """
    并将二维数组成图, 或根据需求保存图片

    成图规则:
        1.根据nrows & ncols 明确了最多能显示的图片数量\n
        2.Array数量大于可成图数量时，仅展示前几张图片\n

    Args:
        array_lst (list): 二维数组列表
        title_list (list): 二维数组标题
        fd_path (str): 文件的存储路径 if fd_path==None，不保存Array，否则保存
        fname (str): 保存图片时，图片名称
        ncols (int): subplots的行数
        nrows (int): subplots的列数
        vmax (int): 图片展示参数
        vmin (int): 图片展示参数
        cmap (str): 图片展示参数

    Returns:
        None: 不返回任何值
    """

    fig, axs = plt.subplots(nrows, ncols)
    image_show_num = nrows * ncols  # 计算总共可显示的图片

    for cnt in range(image_show_num):
        if cnt < len(array_lst):
            index = cnt
            # print(cnt // ncols, cnt % ncols)
            if nrows == 1 and ncols == 1:
                __axs__ = axs
            elif nrows == 1 or ncols == 1:
                __axs__ = axs[cnt]
            else:
                __axs__ = axs[cnt // ncols, cnt % ncols]

            __axs__.imshow(array_lst[index], cmap=cmap, vmin=vmin, vmax=vmax)
            if title_list is None:
                title = "Image {}: max_bin:{}, min_bin:{}, median_bin:{}".format(
                    index, np.max(array_lst[index]), np.min(array_lst[index]), np.median(array_lst[index]))
            else:
                title = title_list[index]

            # --------------------- 配置刻度 --------------------
            __axs__.xaxis.tick_top()  # 设置x坐标轴位置在顶部
            __axs__.xaxis.set_major_locator(MultipleLocator(48))
            __axs__.yaxis.set_major_locator(MultipleLocator(18))
            __axs__.set_title(title)
        else:
            break
    if fd_path is None:
        # plt.xlim(0, 768)
        self_plt_show()
        # plt.show()
    else:
        ArrayImageSave(fname=fname, fd_path=fd_path)
        plt.close()

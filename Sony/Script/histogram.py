import os
import sys

# sys.path.append(os.path.join(os.getcwd(), "../../SelfDefinedPackge"))
sys.path.append(r"D:\\Git\Adaps\\")
print(os.getcwd())

import SelfDefinedPackge.PubMethod
import numpy as np
import matplotlib.pyplot as plt
import mplcursors


def fig_close():
    for fig in plt.get_fignums():
        plt.figure(fig)
        plt.close()


def hist_img(data, pixel_id, title=None, is_merge=True, is_save=False, start_bin=0, end_bin=1000):
    def gen_fig():
        fig, ax = plt.subplots()
        plt.xlabel("1ns/bin")
        plt.ylabel("Counts")
        plt.title(title)
        handle = []
        return fig, ax, handle

    def do_mark(coors):
        if coors[1][1] in is_marked_vcoor:
            return
        if coors[0] == coors[1]:
            coors.pop()
            # shift = 15
        for idx in range(len(coors)):
            shift = -15 + idx * 30
            coor = coors[idx]
            is_marked_vcoor.append(coor[1])
            coor_mark = (coor[0] + shift, coor[1] * 1.05)
            plt.annotate(f'{coor}',
                         xy=coor,
                         xytext=coor_mark,
                         arrowprops=dict(facecolor='#74C476',
                                         alpha=0.6,
                                         arrowstyle='->',
                                         connectionstyle='arc3,rad=0.5',  # 有多个参数可选
                                         color='r'
                                         ),
                         )

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签SimHei
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    is_marked_vcoor = []

    fig, ax, handle = gen_fig()

    for index in range(len(pixel_id)):
        if not is_merge and index != 0:
            fig, ax, handle = gen_fig()

        pxl_id = pixel_id[index]
        data1 = data[pxl_id].split("\t")
        data2 = list(map(int, data1[start_bin+16:end_bin+16]))

        data_np = np.array(data2)
        hdl, = plt.plot(data_np, label=f"Pixel_id:{pxl_id - 4}")

        # 折线图 label 标签显示
        handle.append(hdl)
        font1 = {'family': 'SimHei',
                 'weight': 'normal',
                 'size': 12, }  # 设置图例大小位置
        legend = plt.legend(handles=handle, prop=font1)

        # 对图片进行标记
        # /////////////////////////////////////////////////////
        width = np.shape(data_np)[0]
        max_value = np.max(data_np)
        max_indexes = np.argwhere(data_np == max_value).flatten()
        min_index = np.min(max_indexes)
        max_index = np.max(max_indexes)
        # if index == 0:
        #     do_mark(coors=[(min_index, max_value), (max_index, max_value)])
        if is_save:
            do_mark(coors=[(min_index, max_value), (max_index, max_value)])
    # plt.show()
    # plt.savefig(f'..\\figs\\{title}.png', dpi=300)
    # plt.close()


def coor_show():
    cursor = mplcursors.cursor(multiple=True)
    # @cursor.connect("add")
    # def on_add(sel):
    #     x_val = int(sel.target[0])
    #     y_val = sel.target[1]
    #     # sel.annotation.xy = (x_val, y_val)
    #     # print(sel.annotation.xy)
    #     # sel.annotation.set_text(int(sel.index))


def do_work(cfg):
    file_list = cfg["file_sel"]
    is_merge = cfg["merge"]

    pixel_id_sel = cfg["pixel_sel"].split(",")
    pixel_id = list(map(int, pixel_id_sel))
    is_save = False

    for f in file_list:
        f_name = os.path.basename(f)
        name = os.path.splitext(f_name)[0]
        data = SelfDefinedPackge.PubMethod.read_file(f)
        hist_img(data, pixel_id, title=name, is_merge=is_merge, is_save=is_save,
                 start_bin=cfg['start_bin'], end_bin=cfg['end_bin'])
        print(f)
    coor_show()
    plt.show()


if __name__ == '__main__':
    is_merge = False
    is_save = False
    start = 16
    end = 115
    # 激光脉宽: 17.8ns, 4ns
    # 图片数据：1~3：激光脉宽4ns; 4~: 17.8ns脉宽; 7: 测距;8 : 近距离测距；9：直接打激光
    pixel_id = [4, 50, 108, 150, 195]

    # data = SelfDefinedPackge.PubMethod.read_file("../TMP/test.txt")
    # hist_img(data, pixel_id, is_merge)

    file_list = SelfDefinedPackge.PubMethod.get_fp(fd_path="..\第二次测试", mode=1, match_filter=".txt")
    for f in file_list[0:1]:
        f_name = os.path.basename(f)
        name = os.path.splitext(f_name)[0]
        data = SelfDefinedPackge.PubMethod.read_file(f)
        hist_img(data, pixel_id, title=name, is_merge=is_merge, is_save=is_save, start_bin=start, end_bin=end)
        print(f)

    coor_show()
    plt.show()
    # print("END")

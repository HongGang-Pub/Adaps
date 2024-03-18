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
        per_fig = plt.figure(fig)
        plt.close()

def fig_save():
    print(plt.get_fignums())
    for fig in plt.get_fignums():
        per_fig = plt.figure(fig)
        title = per_fig.axes[0].axes.get_title()
        plt.savefig(f'..\\figs\\{title}.png', dpi=300)

def do_mark(data_np):
    width = np.shape(data_np)[0]
    max_value = np.max(data_np)
    max_indexes = np.argwhere(data_np == max_value).flatten()
    min_index = np.min(max_indexes)
    max_index = np.max(max_indexes)

    coors = [(min_index, max_value), (max_index, max_value)]

    if coors[0] == coors[1]:
        coors.pop()
        # shift = 15

    for idx in range(len(coors)):
        shift = (2 * idx - 1) * width * 0.05
        coor = coors[idx]
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


def hist_img(cfg):
    dsp_mode = cfg["dsp_mode"]
    file_list = cfg["file_sel"]
    start_bin = cfg["start_bin"]
    end_bin = cfg["end_bin"]
    start_index = cfg["bin_start_index"]
    is_save = cfg["save"]

    pixel_id_sel = cfg["pixel_sel"].split(",")
    pixel_id = list(map(int, pixel_id_sel))

    f_names = []
    f_datas = []

    font1 = {'family': 'SimHei',
             'weight': 'normal',
             'size': 12, }  # 设置图例大小位置

    def gen_fig():
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签SimHei
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        fig, ax = plt.subplots()
        plt.xlabel("1ns/bin")
        plt.ylabel("Counts")

        handle = []
        return fig, ax, handle

    for f in file_list:
        f_name = os.path.splitext(os.path.basename(f))[0]
        f_data = SelfDefinedPackge.PubMethod.read_file(f)
        f_names.append(f_name)
        f_datas.append(f_data)

    if dsp_mode == 0:  # 一帧多点展示
        for per_frame_data in f_datas:
            fig, ax, handle = gen_fig()
            title = f_names.pop(0)
            plt.title(title)
            for pxl_id in pixel_id:
                data1 = per_frame_data[pxl_id].split("\t")
                data2 = list(map(int, data1[start_bin + start_index:end_bin + start_index]))

                data_np = np.array(data2)
                hdl, = plt.plot(data_np, label=f"Pixel_id:{pxl_id}")

                # 折线图 label 标签显示
                handle.append(hdl)
                legend = plt.legend(handles=handle, prop=font1)

                if is_save:
                    # 对图片进行标记
                    # /////////////////////////////////////////////////////
                    do_mark(data_np)
                    plt.savefig(f'..\\figs\\{title}.png', dpi=300)
                    plt.close()

    else:  # 一帧多点展示
        for pxl_id in pixel_id:
            fig, ax, handle = gen_fig()
            title = f"Pixel_id {pxl_id}"
            plt.title(title)
            for f_idx in range(len(f_datas)):
                per_frame_data = f_datas[f_idx]
                data1 = per_frame_data[pxl_id].split("\t")
                data2 = list(map(int, data1[start_bin + start_index:end_bin + start_index]))

                data_np = np.array(data2)
                hdl, = plt.plot(data_np, label=f"{f_names[f_idx]}")

                # 折线图 label 标签显示
                handle.append(hdl)
                legend = plt.legend(handles=handle, prop=font1)

                if is_save:
                    # 对图片进行标记
                    # /////////////////////////////////////////////////////
                    do_mark(data_np)
                    plt.savefig(f'..\\figs\\{title}.png', dpi=300)
                    plt.close()
    if not is_save:
        coor_show()
        plt.show()


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
    hist_img(cfg)


if __name__ == '__main__':

    fd_path = "..\第二次测试"
    file_list = SelfDefinedPackge.PubMethod.get_fp(fd_path=fd_path, mode=1, match_filter=".txt")

    config = {"dsp_mode": 0,
              "start_bin": 0,
              "end_bin": 1000,
              "pixel_sel": "0, 50, 100, 150, 191",
              "file_sel": file_list,
              "bin_start_index": 16,
              "save": 0
              }
    do_work(config)

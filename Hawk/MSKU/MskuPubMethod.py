import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# import matplotlib
#
# matplotlib.use('Agg')  # 该模式下绘图无法显示，plt.show()也无法作用
import matplotlib.animation as animation
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from SelfDefinedPackge import PubMethod
import numpy as np
import matplotlib.pyplot as plt
from Hawk.Common import HawkPubMethod
from SelfDefinedPackge import ArrayPubMethod
import os
from matplotlib.pyplot import MultipleLocator


def zone_config(sub_expotime, sub_idletime, expo_lasprd, expo_plswc, expo_plswf, tx_en, spad_en_in3rows, kernel):
    """ 根据传入参数生成每个分区的 Zone Config """
    if not (isinstance(kernel, list)):
        raise ValueError("Kernel is no list!")
    if len(kernel) != 8:
        raise ValueError("Kernel size error!")

    zone_cfg = [sub_expotime, sub_idletime, expo_lasprd, (int(expo_plswc << 5) + expo_plswf),
                (int(tx_en << 2) + spad_en_in3rows)]
    zone_cfg = zone_cfg + kernel
    return zone_cfg


def ZonesConfigGenerate(cfg):
    """ 调用zon_config方法生成所有分区的 Zone Config """
    kernel = []
    zone_mem = []

    for v_roll_cnt in range(0, cfg['V_ROLL_NUM'] + 1):
        if cfg['zone_cfg_sel'] != -1:
            zone_sel = "Zone{}".format(cfg['zone_cfg_sel'])
            kernel_sel = "Zone_{}_MF_KN".format(cfg['zone_cfg_sel'])
        else:
            zone_sel = "Zone{}".format(v_roll_cnt)
            kernel_sel = "Zone_{}_MF_KN".format(v_roll_cnt)

        if len(cfg['zone_cfg_def'][kernel_sel]) != 16:
            raise ValueError("Kernel:{} config Error！".format(kernel_sel))

        for i in range(0, 8):
            kernel.append(
                int(cfg['zone_cfg_def'][kernel_sel][i * 2 + 1] << 8) + cfg['zone_cfg_def'][kernel_sel][i * 2])

        try:
            per_zone_mem = zone_config(sub_expotime=cfg['zone_cfg_def']['SUB_EXPOTIME'][zone_sel],
                                       sub_idletime=cfg['zone_cfg_def']['SUB_IDLETIME'][zone_sel],
                                       expo_lasprd=cfg['zone_cfg_def']['EXPO_LASPRD'][zone_sel],
                                       expo_plswc=cfg['zone_cfg_def']['EXPO_PLSWC'][zone_sel],
                                       expo_plswf=cfg['zone_cfg_def']['EXPO_PLSWF'][zone_sel],
                                       tx_en=cfg['zone_cfg_def']['TX_EN'][zone_sel],
                                       spad_en_in3rows=cfg['zone_cfg_def']['SPADEN_IN3ROWS'][zone_sel],
                                       kernel=kernel)
            kernel = []
        except BaseException as msg:
            raise ValueError("{} configuration may be missing or incorrect! Log: {}".format(zone_sel, msg))
        zone_mem.append(per_zone_mem)
    return zone_mem


def do_mark(info, fontsize=5):
    (x, y, text) = info
    plt.text(x + 5, y + 3, text, fontdict={
        'family': 'Times New Roman',  # 标注文本字体
        'fontsize': fontsize,  # 文本大小
        'fontweight': 'bold',  # 字体粗细
        # 'fontstyle': 'italic',  # 字体风格
        'color': 'white',  # 文本颜色
        'backgroundcolor': 'blue',  # 背景颜色
        'bbox': {
            'boxstyle': 'round',  # 椭圆外框
            'edgecolor': 'white',  # 线框颜色
            'linewidth': 0
        }
    })

    # plt.annotate(s, xy=(x, y), xytext=(x-30, y+3),
    #              arrowprops={
    #                  'headwidth': 12,  # 箭头头部的宽度
    #                  'headlength': 8,  # 箭头头部的长度
    #                  'width': 3,  # 箭头尾部的宽度
    #                  'facecolor': 'w',  # 箭头的颜色
    #                  'shrink': 0.1,  # 从箭尾到标注文本内容开始两端空隙长度
    #              },
    #              family='Times New Roman',  # 标注文本字体为Times New Roman
    #              fontsize=10,  # 文本大小为18
    #              fontweight='bold',  # 文本为粗体
    #              color='white',  # 文本颜色为红色
    #              backgroundcolor='black'
    #              # ha = 'center' # 水平居中
    #              )


def roi_data_save(f_name, data=None, fd_path=".", data_format=1):
    """ 保存 ROI 数据 """
    if data is None:
        return

    if not os.path.exists(fd_path):
        # 目录不存在，进行创建操作
        os.makedirs(fd_path)  # 使用os.makedirs()方法创建多层目录

    file = "{}\\{}".format(fd_path, f_name)

    with open(file=file, mode="w", encoding="utf-8") as f:
        for i in range(0, len(data)):
            roi_string = '{:0>4X}'.format(data[i])
            if data_format == 1:
                f.write(roi_string)
                if i < (len(data) - 1):
                    f.write('\n')
            else:
                f.write(roi_string[2:4])
                f.write('\n')
                f.write(roi_string[0:2])
                if i < (len(data) - 1):
                    f.write('\n')
    return


def roi_imag(msku_roi_data, cfg, fd_path='.', f_name='msku_imag'):
    """ 生成根据 Masking 数据生成ROI图片 """
    # spad_array = np.zeros((576, 768, 3))
    spad_array = np.zeros((576, 768))

    scan_mode = cfg["SCAN_MODE"]
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM']
    h_vld_seg = cfg['H_VLD_SEG']
    coor_info = []

    if scan_mode == 0:
        for vroll_cnt in range(v_roll_num + 1):
            per_rolling_data = msku_roi_data[vroll_cnt]
            dsp = (vroll_cnt * 2) % 16 + 10
            # for per_coor in per_rolling_data:
            for seg_cnt in range(len(per_rolling_data)):
                per_coor = per_rolling_data[seg_cnt]
                seg_num = per_coor >> 10
                spad_coor = per_coor % 1024
                # spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + 1) * 48, :] = np.arrays(
                #     [dsp, dsp, dsp])
                spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + 1) * 48] = dsp
                if seg_cnt == 0:
                    coor_info.append([seg_num * 48, spad_coor, "1D VROll_{}".format(vroll_cnt+1)])
    else:
        roll_cnt = 0
        for vroll_cnt in range(v_roll_num + 1):
            per_zone_data = msku_roi_data[vroll_cnt]
            for hroll_cnt in range(h_roll_num + 1):
                dsp = ((vroll_cnt * h_roll_num + hroll_cnt) * 2) % 32 + 10
                index = hroll_cnt * 6
                per_rolling_data = per_zone_data[index: index + 6]
                # for per_coor in per_rolling_data:
                for seg_cnt in range(len(per_rolling_data)):
                    per_coor = per_rolling_data[seg_cnt]
                    seg_num = per_coor >> 10
                    spad_coor = per_coor % 1024
                    spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + h_vld_seg + 1) * 48] = dsp
                    if seg_cnt == 0:
                        coor_info.append([seg_num * 48, spad_coor, "2D ROll_{}_{}".format(vroll_cnt+1, hroll_cnt+1)])
                roll_cnt += 1

    # spad_array = spad_array / spad_array.max()
    fig = plt.figure()
    ax = fig.gca()
    ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
    ax.yaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_major_locator(MultipleLocator(48))
    ax.imshow(spad_array, cmap="gray")
    # plt.show()
    for info in coor_info:
        do_mark(info)
    ArrayPubMethod.ArrayImageSave(fname=f_name, fd_path=fd_path)
    plt.close()
    # plt.show()
    # plt.imsave("{}/msku_imag.png".format(fd_path), spad_array, dpi=600)
    return


def ParseRoiMem(cfg, roi_file=None, f_path='figs'):
    """
    根据寄存器配置解析 ROI 数据
    Args:
        cfg (寄存器配置相关信息):
        roi_file (str): 指定 ROI 文件路径，为 None 时，从cfg中获取 roi_file
        f_path (str): 解析ROI后 masking 成图效果展示

    Returns:
        tuple: zone_roi_mem, msku_roi_mem
    """
    scan_mode = cfg["scan_mode"]
    v_roll_num = cfg["v_roll_num"]
    h_roll_num = cfg["h_roll_num"]
    h_vld_seg = cfg["h_vld_seg"]

    if roi_file is None:
        roi_file = cfg["roi_file"]
    roi_data = PubMethod.read_file(roi_file)

    zone_roi_mem = []
    msku_roi_mem = []

    roi_len = h_vld_seg + 1 if scan_mode == 0 else h_roll_num + 1
    zone_len = roi_len * 6 + 13

    if zone_len * (v_roll_num + 1) != len(roi_data):
        raise ValueError("解析ROI错误，请检查ROI或者v_roll_num、h_roll_num、h_vld_seg等配置!!!")

    for v_roll_cnt in range(v_roll_num + 1):
        seg_coor_st_index = v_roll_cnt * zone_len + 13

        zone_mem = roi_data[seg_coor_st_index - 13:seg_coor_st_index]

        for index in range(len(zone_mem)):
            zone_mem[index] = int(zone_mem[index], 16)

        zone_roi_mem.append(zone_mem)

        msku_mem = roi_data[seg_coor_st_index: seg_coor_st_index + zone_len - 13]

        # 转换为 int 数据类型
        for index in range(len(msku_mem)):
            msku_mem[index] = int(msku_mem[index], 16)

        msku_roi_mem.append(msku_mem)

    csru_cfg = {
        "SCAN_MODE": cfg["scan_mode"],
        "V_ROLL_NUM": cfg["v_roll_num"],
        "H_ROLL_NUM": cfg["h_roll_num"],
        "H_VLD_SEG": cfg["h_vld_seg"]
    }

    # 成图展示 masking 效果
    roi_imag(msku_roi_mem, csru_cfg, fd_path=f_path)

    return zone_roi_mem, msku_roi_mem


def PerRollingArrayCollect(msku_roi_data, cfg):
    """ 返回每次 rolling 的二维数组效果图，用于成图 """
    # spad_array = np.zeros((576, 768, 3))
    spad_array = np.zeros((576, 768))

    scan_mode = cfg["SCAN_MODE"]
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM']
    h_vld_seg = cfg['H_VLD_SEG']
    coor_info = []

    spad_array_collect = []

    if scan_mode == 0:
        for vroll_cnt in range(v_roll_num + 1):
            per_rolling_data = msku_roi_data[vroll_cnt]
            dsp = (vroll_cnt * 2) % 32 + 10
            # for per_coor in per_rolling_data:
            for seg_cnt in range(len(per_rolling_data)):
                per_coor = per_rolling_data[seg_cnt]
                seg_num = per_coor >> 10
                spad_coor = per_coor % 1024
                # spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + 1) * 48, :] = np.arrays(
                #     [dsp, dsp, dsp])
                spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + 1) * 48] = dsp
                if seg_cnt == 0:
                    coor_info.append([seg_num * 48, spad_coor, "1D VROll_{}".format(vroll_cnt+1)])
            spad_array_collect.append(spad_array)
            spad_array = np.zeros((576, 768))
    else:
        roll_cnt = 0
        for vroll_cnt in range(v_roll_num + 1):
            per_zone_data = msku_roi_data[vroll_cnt]
            for hroll_cnt in range(h_roll_num + 1):
                dsp = (hroll_cnt * 2) % 32 + 10
                index = hroll_cnt * 6
                per_rolling_data = per_zone_data[index: index + 6]
                # for per_coor in per_rolling_data:
                for seg_cnt in range(len(per_rolling_data)):
                    per_coor = per_rolling_data[seg_cnt]
                    seg_num = per_coor >> 10
                    spad_coor = per_coor % 1024
                    spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + h_vld_seg + 1) * 48] = dsp
                    if seg_cnt == 0:
                        coor_info.append([seg_num * 48, spad_coor, "2D ROll_{}_{}".format(vroll_cnt+1, hroll_cnt+1)])
                roll_cnt += 1
                spad_array_collect.append(spad_array)
                spad_array = np.zeros((576, 768))
    return spad_array_collect, coor_info


def animation_img(fig, msku_roi_data, cfg):
    # ax = plt.gca()
    # fig = plt.figure()
    arrays, info = PerRollingArrayCollect(msku_roi_data, cfg)

    fig.clf()
    ax = fig.add_subplot(111)

    # --------------------- 配置刻度 --------------------
    x_major_locator = MultipleLocator(48)
    # 把x轴的刻度间隔设置为 48，并存在变量里
    y_major_locator = MultipleLocator(50)
    # 把y轴的刻度间隔设置为 50，并存在变量里

    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

    # --------------------- 配置坐标轴属性刻度 --------------------
    ax.xaxis.tick_top()     # 设置x坐标轴位置在顶部
    ax.spines['top'].set_color('gray')
    ax.spines['top'].set_linewidth(5)
    ax.spines['left'].set_color('gray')
    ax.spines['left'].set_linewidth(5)
    # 将侧轴、顶部轴设置为None
    ax.spines['right'].set_color(None)
    ax.spines['bottom'].set_color(None)

    # im = ax.imshow(X=arrays[0], cmap="gray")

    # def init():
    #     im.set_data(arrays[0])
    #     return im

    def update(i):
        # im.set_data(arrays[i])
        imgs = ax.imshow(X=arrays[i], cmap="gray")

        x, y, s = info[i]
        title = ax.text(x + 5, y + 3, s, fontdict={
            'family': 'Times New Roman',  # 标注文本字体
            'fontsize': 10,  # 文本大小
            'fontweight': 'bold',  # 字体粗细
            # 'fontstyle': 'italic',  # 字体风格
            'color': 'white',  # 文本颜色
            'backgroundcolor': 'blue',  # 背景颜色
            'bbox': {
                'boxstyle': 'round',  # 椭圆外框
                'edgecolor': 'white',  # 线框颜色
                'linewidth': 0
            }
        })
        return [imgs] + [title]

    ani = animation.FuncAnimation(fig, update, range(len(arrays)), interval=700, blit=True)

    # plt.show()
    # plt.close()
    return ani

import logging
import re
import tkinter
from typing import Tuple, List, Any

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
from numpy import ndarray, dtype, floating, float_
from numpy._typing import _64Bit

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


def roi_data_save(f_name, data=None, fd_path=".", roi_data_format=1):
    """ 保存 ROI 数据 """
    if data is None:
        return

    if not os.path.exists(fd_path):
        # 目录不存在，进行创建操作
        os.makedirs(fd_path)  # 使用os.makedirs()方法创建多层目录

    file = "{}\\{}.txt".format(fd_path, f_name)

    with open(file=file, mode="w", encoding="utf-8") as f:
        for i in range(0, len(data)):
            roi_string = '{:0>4X}'.format(data[i])
            if roi_data_format == 1:
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


def ParseRoiMem(cfg, roi_file=None, f_path=None):
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
    if f_path is not None:
        RollingArrayCollect(msku_roi_data=msku_roi_mem, cfg=csru_cfg, is_save=1, fd_path=f_path)

    return zone_roi_mem, msku_roi_mem


def RollingArrayCollect(msku_roi_data, cfg, is_save=0, fd_path='.') -> tuple:
    """
    对 rolling 的数据生成二维数组用于成图, 包含:
        1. 单次rolling masking的二维数组;
        2. 所有rolling masking的叠加的二维数组(支持保存);
        3. 所有rolling masking叠加的深度二维数组(支持保存);
    """
    spad_array = np.zeros((576, 768), dtype=np.float32)

    scan_mode = cfg["SCAN_MODE"]
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM']
    h_vld_seg = cfg['H_VLD_SEG']
    coor_info = []

    spad_array_collect = []
    acc_spad_array = np.zeros((576, 768), dtype=np.float32)
    depth_spad_array = np.zeros((192, 256), dtype=np.float32)

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
                acc_spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + 1) * 48] = dsp
                try:
                    depth_spad_array[spad_coor // 3, seg_num * 16:(seg_num + 1) * 16] = dsp
                except:
                    continue
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
                    acc_spad_array[spad_coor:spad_coor + 3, seg_num * 48:(seg_num + h_vld_seg + 1) * 48] = dsp
                    try:
                        depth_spad_array[spad_coor // 3, seg_num * 16:(seg_num + h_vld_seg + 1) * 16] = dsp
                    except:
                        continue
                    if seg_cnt == 0:
                        coor_info.append([seg_num * 48, spad_coor, "2D ROll_{}_{}".format(vroll_cnt+1, hroll_cnt+1)])
                roll_cnt += 1
                spad_array_collect.append(spad_array)
                spad_array = np.zeros((576, 768))
    if is_save:
        # 对 acc_spad_array 和 depth_spad_array进行保存
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        ax.yaxis.set_major_locator(MultipleLocator(50))
        ax.xaxis.set_major_locator(MultipleLocator(48))
        # ax.imshow(spad_array, cmap="gray")
        ax.imshow(acc_spad_array)
        # plt.show()
        for info in coor_info:
            do_mark(info)
        ArrayPubMethod.ArrayImageSave(fname='imag_msku', fd_path=fd_path)
        plt.close()

        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.xaxis.set_major_locator(MultipleLocator(16))
        ax.imshow(depth_spad_array)
        # plt.show()
        ArrayPubMethod.ArrayImageSave(fname="imag_depth", fd_path=fd_path)
        plt.close()

        # plt.show()
        # plt.imsave("{}/msku_imag.png".format(fd_path), spad_array, dpi=600)
    return spad_array_collect, acc_spad_array, depth_spad_array, coor_info


def animation_img(fig, msku_roi_data, cfg):
    # ax = plt.gca()
    # fig = plt.figure()
    arrays, acc_spad_array, depth_spad_array, info = RollingArrayCollect(msku_roi_data, cfg)

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


def DirectAccessCaliData(cfg):
    """通过读取文件的形式获取 cali_data"""
    ini_cali_datas = PubMethod.read_file(cfg["gen_roi_file"])

    # 去除单行注释
    # /////////////////////////////////////////////////////////////////////
    cali_datas = []
    for line_cnt in range(len(ini_cali_datas)):
        _str = ini_cali_datas[line_cnt]
        if _str.strip() == '\n':
            continue
        elif _str.strip()[0:2] == '//':
            continue
        else:
            cali_datas.append([_str, line_cnt + 1])

    # 校验标定数量是否正确
    # /////////////////////////////////////////////////////////////////////
    num = (cfg['V_ROLL_NUM'] + 1) * (cfg['H_ROLL_NUM'] + 1) if cfg['SCAN_MODE'] == 1 else (cfg['V_ROLL_NUM'] + 1)
    if len(cali_datas) < num:  # 标定数量少于配置所需标定数时, 结束程序
        info = (f"Preview failed! Log：Based on the configuration information of V_ROLL_NUM & H_ROLL_NUM, "
                f"{num} cali data are required, but only {len(cali_datas)} cali data are available.")
        raise ValueError(info)
    elif len(cali_datas) > num:  # 标定数量多余所需标定数时, 打印提示信息, 提示配置信息与标定信息不匹配
        logging.warning(f"Be careful! The calibration data may not match the register configuration.")

    def _split_cali_data(index):
        [data, lines] = cali_datas[index]
        data = re.split(',|;|，|；|//', data)
        # if len(data) < 2:
        #     raise ValueError(f"Calibration data format error.\n"
        #                      f"line{lines}: {data}")
        try:
            _start_index = int(data[1])
            _seg_num = int(data[0]) // 48
        except:
            raise ValueError(f"Calibration data format error.\n"
                             f"line{lines}: {data}")
        if _seg_num > 15:
            raise ValueError(f"Calibration data error.\n"
                             f"line{lines}: {data}\n"
                             f"Error: {data[0]} beyond 767.")
        return _seg_num, _start_index

    img_roi_data = []
    per_img_roi_data = []  # 存储一张PCM灰度图获取的ROI数据

    frame_cnt = 0
    if cfg['SCAN_MODE'] == 0:
        for vroll_cnt in range(0, cfg['V_ROLL_NUM'] + 1):
            seg_num, start_index = _split_cali_data(frame_cnt)

            for seg_cnt in range(0, cfg['H_VLD_SEG'] + 1):
                per_img_roi_data.append([seg_num + seg_cnt, start_index])

            img_roi_data.append(per_img_roi_data)
            per_img_roi_data = []
            frame_cnt += 1
    else:
        for vroll_cnt in range(0, cfg['V_ROLL_NUM'] + 1):
            for hroll_cnt in range(0, cfg['H_ROLL_NUM'] + 1):
                seg_num, start_index = _split_cali_data(frame_cnt)
                per_img_roi_data.append([seg_num, start_index])

                img_roi_data.append(per_img_roi_data)
                per_img_roi_data = []
                frame_cnt += 1
    return img_roi_data

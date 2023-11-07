import tkinter

import re
from tkinter import filedialog
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MultipleLocator

from Hawk.MSKU import MskuPubMethod
from Hawk.MSKU.MSKU_Cali import ROICalibration
from Hawk.MSKU.MSKU_GEN import ROIGenerate
from Hawk.Common import HawkPubMethod
from SelfDefinedPackge import PubMethod
from Hawk.HawkGUI import Player
from Hawk.HawkGUI.HawkComponentStyle import *


def DirectAccessCaliData(file, cfg):
    """通过读取文件的形式获取 cali_data"""
    ini_cali_datas = PubMethod.read_file(file)

    # ---------------- 去除单行注释 ----------------------
    cali_datas = []
    for line_cnt in range(len(ini_cali_datas)):
        _str = ini_cali_datas[line_cnt]
        if _str.strip() == '\n':
            continue
        elif _str.strip()[0:2] == '//':
            continue
        else:
            cali_datas.append([_str, line_cnt + 1])

    # -------------------- 校验标定数量是否正确 ------------------------
    num = (cfg['V_ROLL_NUM'] + 1) * (cfg['H_ROLL_NUM'] + 1) if cfg['SCAN_MODE'] == 1 else (cfg['V_ROLL_NUM'] + 1)
    if len(cali_datas) < num:  # 标定数量少于配置所需标定数时, 结束程序
        info = (f"Preview failed! Log：Based on the configuration information of V_ROLL_NUM & H_ROLL_NUM, "
                f"{num} cali data are required, but only {len(cali_datas)} cali data are available.")
        raise ValueError(info)
    elif len(cali_datas) > num:  # 标定数量多余所需标定数时, 打印提示信息, 提示配置信息与标定信息不匹配
        info = f"Be careful! The calibration data may not match the register configuration."
    else:
        info = None

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
    return img_roi_data, info


def config_mapping(cfg: dict):
    """
    重映射寄存器配置，确保程序中的 key-value有值且正确
    """
    cfg['SYS_FREQ'] = "200M" if (cfg["TDC_BIN_W"] in [1.25, 2.50]) \
        else "250M" if (cfg["TDC_BIN_W"] in [1.00, 2.00]) \
        else "330M"
    cfg['UPSMP_MODE'] = 0b11 if (cfg["TDC_BIN_W"] in [0.75, 1.00, 1.25]) \
        else 0b00
    return


def MskuRoiGenerateForJsonConfig(cfg):
    """完全通过Json文件生成 MskuRoi"""
    msku_roi_mem = ROIGenerate.MskuRoiGenerate(cfg)
    return msku_roi_mem


def MskuRoiGenerateForCaliData(cali_data: list, cfg: dict) -> list:
    msku_roi_mem = ROICalibration.MskuRoiGenerate(cali_data, cfg)
    return msku_roi_mem


def RoiMemGenerate(cfg, msku_roi_mem):
    roi_data = []

    try:
        zone_mem = MskuPubMethod.ZonesConfigGenerate(cfg=cfg)
    except BaseException as msg:
        raise msg

    MskuPubMethod.roi_imag(msku_roi_mem, cfg, f_name=cfg['roi_name'], fd_path=cfg["fd_path"])

    for index in range(len(zone_mem)):
        per_zone_mem = zone_mem[index] + msku_roi_mem[index]
        roi_data = roi_data + per_zone_mem

    MskuPubMethod.roi_data_save(f_name=f"{cfg['roi_name']}.txt", data=roi_data, fd_path=cfg["fd_path"],
                                data_format=cfg['data_format'])
    return "ROI 生成完成！！！"


def msku_gui():
    # ===============================================================================================
    # 窗口显示属性配置
    # ===============================================================================================
    window = tkinter.Tk()
    # window.iconbitmap(r"C:\Users\honggang.li\OneDrive\图片\favicon1.ico")  # icon
    width = 1300
    height = 850
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)
    window.minsize(width, height)

    window.title("Hawk ROI Generate 1.2")  # 标题
    window.iconphoto(False, tkinter.PhotoImage(file=r".file/icon.png"))

    def _quit():
        window.quit()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", _quit)  # 关闭窗口，退出程序，防止后台程序持续占用

    # ===============================================================================================
    # 绘制动态图片相关方法
    # ===============================================================================================
    msku_roi_mem = []
    arrays = []
    info = []
    preview_triggered = False
    preview_update_symbol = False
    frame_cnt = 0

    def _preview_trigger():
        nonlocal arrays, info, preview_update_symbol, preview_triggered
        preview_triggered = True
        preview_update_symbol = True
        arrays, info = MskuPubMethod.PerRollingArrayCollect(msku_roi_mem, cfg)
        return

    def update(i):
        nonlocal preview_update_symbol, frame_cnt
        if preview_update_symbol is True:
            frame_cnt = i
            preview_update_symbol = False

        subframe_index = (i - frame_cnt) % len(arrays)

        # print(i, frame_cnt, subframe_index)

        ax.cla()
        # --------------------- 配置刻度 --------------------
        ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        ax.xaxis.set_major_locator(MultipleLocator(48))
        ax.yaxis.set_major_locator(MultipleLocator(50))

        imgs = ax.imshow(X=arrays[subframe_index])

        if not (subframe_index < len(info)):
            return [imgs]

        # ------------- title config -------------------
        x, y, s = info[subframe_index]
        _str = f"{s}({x}, {y})"
        x = x + 5 if x < 610 else 610
        y = y - 12 if y > 30 else y + 37
        y = y if y < 565 else 565
        title = ax.text(x, y, _str, fontdict={
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

    # ===============================================================================================
    # Window 主界面增加 3 个 frame, 分别用于不同用途
    # ===============================================================================================
    company_icons = tkinter.Frame(window, background='white')  # 左上添加 frame 控件用于展示公司图片
    frame_roi_img = tkinter.Frame(window)  # 左下添加 frame 控件用于展示动图
    frame_roi_cfg = tkinter.Frame(window)  # 右侧添加 frame 控件用于放置 配置、按钮、日志打印等内容

    # --------------------- company_图片 设置 -------------------
    imag = Image.open(r'.file/company_icon.png')
    photo = ImageTk.PhotoImage(imag)
    # photo = tkinter.PhotoImage(r'.file/company_icon.png')
    tkinter.Label(company_icons, image=photo, background='white').pack(fill=tkinter.BOTH)

    # ----------------- frame_roi_cfg 增加多个控件，显示不同交互内容 -------------------
    # register_config_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 寄存器配置控件
    # califile_select_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 文件选择控件
    # reg_roiram_file_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 文件选择控件
    # bottoms_operate_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 按钮操作控件
    # operation_print_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 操作日志打印控件
    configs_frame = tkinter.LabelFrame(frame_roi_cfg, text="Config")  # 寄存器配置控件
    f_input_frame = tkinter.LabelFrame(frame_roi_cfg, text="Input")  # 文件选择控件
    output__frame = tkinter.LabelFrame(frame_roi_cfg, text="Output")  # 文件输出控件
    operate_frame = tkinter.LabelFrame(frame_roi_cfg, text="Operate")  # 按钮操作控件
    logsout_frame = tkinter.LabelFrame(frame_roi_cfg, text="Log")  # 操作日志打印控件

    # logsout_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 操作日志打印控件

    # -------------------------- TDC_BIN_W ----------------------------------
    def _tdc_bin_width_update(event):
        tdc_bin_width = tdc_bin_width_cmp.get()
        cfg['SYS_FREQ'] = "200M" if (tdc_bin_width in ["1.25 ns", "2.50 ns"]) \
            else "250M" if (tdc_bin_width in ["1.00 ns", "2.00 ns"]) \
            else "330M"
        cfg['UPSMP_MODE'] = 0b11 if (tdc_bin_width in ["0.75 ns", "1.00 ns", "1.25 ns"]) \
            else 0b00  # No Upsampling

    bin_width_value = [0.75, 1.00, 1.25, 1.50, 2.00, 2.50]
    tdc_bin_width_cmp = ttk.Combobox(configs_frame, width=23)
    tdc_bin_width_cmp['value'] = ("0.75 ns", "1.00 ns", "1.25 ns", "1.50 ns", "2.00 ns", "2.50 ns")  # 设置下拉菜单中的值
    tdc_bin_width_cmp['state'] = "readonly"  # 设置下拉框只读
    tdc_bin_width_cmp.bind("<<ComboboxSelected>>", _tdc_bin_width_update)

    # -------------------------- WORK_MODE ----------------------------------
    def _work_mode_update(event):
        work_mode = work_mode_cfg_cmp.get()
        cfg['WORK_MODE'] = 3 if work_mode == 'Gray Scale Mode' \
            else 2 if work_mode == "Ranging Mode" \
            else 1 if work_mode == "Echo Mode" \
            else 0  # SPHR

    work_mode_cfg_cmp = ttk.Combobox(configs_frame, width=23)
    work_mode_cfg_cmp['value'] = ("Histogram Mode", "Echo Mode", "Ranging Mode", "Gray Scale Mode")  # 设置下拉菜单中的值
    work_mode_cfg_cmp['state'] = "readonly"  # 设置下拉框只读
    work_mode_cfg_cmp.bind("<<ComboboxSelected>>", _work_mode_update)

    # -------------------------- SCAN_MODE ----------------------------------
    def _scan_mode_update(event):
        scan_mode = scan_mode_cfg_cmp.get()
        cfg['SCAN_MODE'] = 0 if scan_mode == '1D SCAN_MODE' else 1

    scan_mode_cfg_cmp = ttk.Combobox(configs_frame, width=23)
    scan_mode_cfg_cmp['value'] = ('1D SCAN_MODE', '2D SCAN_MODE')  # 设置下拉菜单中的值
    scan_mode_cfg_cmp['state'] = "readonly"  # 设置下拉框只读
    scan_mode_cfg_cmp.bind("<<ComboboxSelected>>", _scan_mode_update)

    # -------------------------- MIPI_RATE ----------------------------------
    def _mipi_rate_update(event):
        mipi_rate = mipi_rate_cfg_cmp.get()
        cfg['MIPI_RATE'] = 0.8 if mipi_rate == "0.8 Gbps/Lane" \
            else 1.0 if mipi_rate == "1.0 Gbps/Lane" \
            else 1.2 if mipi_rate == "1.2 Gbps/Lane" \
            else 1.5

    mipi_rate_value = [0.8, 1.0, 1.2, 1.5]
    mipi_rate_cfg_cmp = ttk.Combobox(configs_frame, width=23)
    mipi_rate_cfg_cmp['value'] = ("0.8 Gbps/Lane", "1.0 Gbps/Lane", "1.2 Gbps/Lane", "1.5 Gbps/Lane")  # 设置下拉菜单中的值
    mipi_rate_cfg_cmp['state'] = "readonly"  # 设置下拉框只读
    mipi_rate_cfg_cmp.bind("<<ComboboxSelected>>", _mipi_rate_update)

    # -------------------------- 文件存储文件名配置 ---------------------------
    fname_for_cfg_cmp = tkinter.Entry(output__frame, relief="solid", width=26)
    fname_for_roi_cmp = tkinter.Entry(output__frame, relief="solid", width=26)

    # -------------------------- V_ROLL_NUM -------------------------------------------
    def _vroll_update(value):
        cfg['V_ROLL_NUM'] = int(value) - 1

    vroll_num_cfg_cmp = tkinter.Scale(configs_frame, Scale_style, from_=1, to=32, command=_vroll_update)

    # -------------------------- H_ROLL_NUM --------------------------------------------
    def _hroll_update(value):
        cfg['H_ROLL_NUM'] = int(value) - 1

    hroll_num_cfg_cmp = tkinter.Scale(configs_frame, Scale_style, from_=1, to=16, command=_hroll_update)

    # -------------------------- H_VLD_SEG --------------------------------------------
    def _h_vld_seg_update(value):
        cfg['H_VLD_SEG'] = int(value) - 1

    h_vld_seg_cfg_cmp = tkinter.Scale(configs_frame, Scale_style, from_=1, to=16, command=_h_vld_seg_update)

    # ---------------------------- 标定文件选择窗口 ----------------------
    file_sel_row = 0

    def _open_cali_file():
        try:
            filepath = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")],
                                                  initialdir=r'Input',
                                                  title='Cali Data Select')
            cali_filename.set(filepath)
        except Exception as e:
            # log_print_window.insert(tkinter.INSERT, "您没有选择任何文件:{}\n".format(e))
            _log_update(f"Preview failed! You have not selected any file.{e}", log_type=2)

    cali_filename = tkinter.StringVar()
    cali_file_sel_cmp = tkinter.Entry(f_input_frame, Entry_style, textvariable=cali_filename)
    cali_file_sel_cmp['state'] = "readonly"  # 设置文本展示框

    # ---------------------------- 基准配置脚本文件选择窗口 ----------------------
    def _open_config_file():
        try:
            filepath = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")],
                                                  initialdir=r'Input',
                                                  title='Coinfig File Select')
            config_filename.set(filepath)
        except Exception as e:
            # log_print_window.insert(tkinter.INSERT, "您没有选择任何文件:{}\n".format(e))
            _log_update(f"Preview failed! You have not selected any file.{e}", log_type=2)

    config_filename = tkinter.StringVar()
    cfgs_file_sel_cmp = tkinter.Entry(f_input_frame, Entry_style, textvariable=config_filename)
    cfgs_file_sel_cmp['state'] = "readonly"  # 设置文本展示框

    # ===============================================================================================
    # 添加功能按钮
    # ===============================================================================================
    # ------------------------ 预览按钮0: 通过 ROIConfig.json文件进行 rolling ------------------------
    def _preview_update0():
        nonlocal msku_roi_mem
        try:
            msku_roi_mem = MskuRoiGenerateForJsonConfig(cfg)
            _preview_trigger()
            _log_update(f"Displaying...", log_type=0)
        except BaseException as e:
            _log_update(f"Preview failed! Log：{e}", log_type=2)
            return

    # ------------------------ 预览按钮1: 通过标定文件进行 rolling ------------------------
    def _preview_update1():
        nonlocal msku_roi_mem
        try:
            if cali_filename.get() == '':
                # log_print_window.insert(tkinter.INSERT, "没有选取任何文件！！！\n")
                _log_update('Preview failed! You have not selected any file.', log_type=2)
                return
            cali_data, log = DirectAccessCaliData(cali_filename.get(), cfg)
            msku_roi_mem = MskuRoiGenerateForCaliData(cali_data, cfg)

            _preview_trigger()
            _log_update(f"Displaying...", log_type=0)

            if log is not None:  # 打印标定文件校验的日志信息
                _log_update(log, log_type=1)
            return
        except BaseException as e:
            _log_update(f"Preview failed! Log：{e}", log_type=2)
            return

    # ------------------------ 保存按钮 ------------------------
    def _do_save():
        # _log_update('Saving...', log_type=0)
        # if preview_triggered is False:
        #     _log_update('Error! You have not genetate ROI yet.', log_type=2)
        #     return
        # cfg['config_name'] = fname_for_cfg_cmp.get()  # 获取界面上配置的文件名
        # cfg['roi_name'] = fname_for_roi_cmp.get()  # 获取界面上配置的文件名
        # RoiMemGenerate(cfg, msku_roi_mem)
        # HawkPubMethod.GenerateHawkRegConfig(cfg)
        # _log_update(f"Hawk register config has been saved to: {cfg['fd_path']}/{cfg['config_name']}.txt", log_type=1)
        # _log_update(f"Hawk ROI data has been saved to: {cfg['fd_path']}/{cfg['roi_name']}.txt", log_type=1)
        # _log_update('Save successfully.', log_type=0)
        try:
            _log_update('Saving...', log_type=0)
            if preview_triggered is False:
                _log_update('Error! You have not genetate ROI yet.', log_type=2)
                return
            cfg['config_name'] = fname_for_cfg_cmp.get()  # 获取界面上配置的文件名
            cfg['roi_name'] = fname_for_roi_cmp.get()  # 获取界面上配置的文件名
            RoiMemGenerate(cfg, msku_roi_mem)
            HawkPubMethod.GenerateHawkRegConfig(cfg)
            _log_update(f"Hawk register config has been saved to: {cfg['fd_path']}/{cfg['config_name']}.txt", log_type=1)
            _log_update(f"Hawk ROI data has been saved to: {cfg['fd_path']}/{cfg['roi_name']}.txt", log_type=1)
            _log_update('Save successfully.', log_type=0)
            return
        except BaseException as e:
            _log_update(f"Save failure! Log：{e}", log_type=2)
            return

    # ------------------------ RELOAD按钮 ------------------------
    def _reload():
        nonlocal cfg
        # log_print_window.insert(tkinter.INSERT, '开始保存...\n')
        _log_update('Reload script...')
        try:
            cfg = PubMethod.ReadJsonFile('HawkConfig.json')
            config_mapping(cfg)
            _set_default_value()  # 根据配置值，重新配置界面值
            _log_update('Reload successfully.')
            return
        except BaseException as e:
            _log_update(f"Reload failure! Log：{e}")
            return

    # ------------------------ Log Clear ------------------------
    def _log_clr():
        """log_type=0: normal, 1: warning, 2: error"""
        log_print_cmp.configure(state='normal')
        log_print_cmp.delete('1.0', 'end')
        log_print_cmp.configure(state='disabled')
        # log_print_cmp.yview_moveto(1)
        # log_print_cmp.update()
        return

    # ------------------------ 日志输出界面 ------------------------
    def _log_update(log, log_type=0):
        """log_type=0: normal, 1: warning, 2: error"""
        log_print_cmp.configure(state='normal')
        if log_type == 1:
            warning = tkinter.END
            log_print_cmp.insert(warning, log, 'warning')
            log_print_cmp.tag_add('warning', warning)
            log_print_cmp.tag_config('warning', background='yellow')
        elif log_type == 2:
            error = tkinter.END
            log_print_cmp.insert(error, log, 'error')
            log_print_cmp.tag_add('error', error)
            log_print_cmp.tag_config('error', foreground='red')
        else:
            log_print_cmp.insert(tkinter.END, log)
        log_print_cmp.insert(tkinter.END, '\n')
        log_print_cmp.configure(state='disabled')
        log_print_cmp.yview_moveto(1)
        log_print_cmp.update()

    # log_windows_frame = tkinter.LabelFrame(logsout_frame, text='Log')
    # log_windows_frame.pack(fill=tkinter.BOTH)

    log_print_cmp = tkinter.Text(logsout_frame, width=30, height=30, undo=True, autoseparators=False, wrap='word')
    log_print_cmp.pack(fill=tkinter.BOTH)

    log_print_cmp.insert(tkinter.INSERT, 'Working!!!\n')
    log_print_cmp.configure(state='disabled')

    # -------------------------配置布局，以及默认值并打开窗口------------------------------
    rows = 0
    def get_row(ini=1):
        nonlocal rows
        rows = (rows + 1) if ini != 1 else 0
        return rows

    vcoor = 0
    def set_next_cmp_coor(height):
        nonlocal vcoor
        vcoor = height + vcoor + 0.005
        return height

    def _set_dsp():
        nonlocal vcoor
        # ------------------ window -> frame -----------------
        # vcoor = 0.005
        # company_icons.place(relx=0.005, rely=vcoor, relwidth=0.695, relheight=set_next_cmp_coor(0.100))
        # frame_roi_img.place(relx=0.005, rely=vcoor, relwidth=0.695, relheight=set_next_cmp_coor(0.885))
        # frame_roi_cfg.place(relx=0.700, rely=vcoor, relwidth=0.295, relheight=set_next_cmp_coor(0.990))
        company_icons.place(relx=0.005, rely=0.005, relwidth=0.695, relheight=0.100)
        frame_roi_img.place(relx=0.005, rely=0.110, relwidth=0.695, relheight=0.885)
        frame_roi_cfg.place(relx=0.700, rely=0.000, relwidth=0.295, relheight=0.990)
        # --------------------- frame_roi_cfg -------------------
        # vcoor = 0.000
        # configs_frame.place(relx=0.010, rely=vcoor, relwidth=0.990, relheight=set_next_cmp_coor(0.380))
        # f_input_frame.place(relx=0.010, rely=vcoor, relwidth=0.990, relheight=set_next_cmp_coor(0.130))
        # output__frame.place(relx=0.010, rely=vcoor, relwidth=0.990, relheight=set_next_cmp_coor(0.130))
        # operate_frame.place(relx=0.010, rely=vcoor, relwidth=0.990, relheight=set_next_cmp_coor(0.120))
        # logsout_frame.place(relx=0.010, rely=vcoor, relwidth=0.990, relheight=set_next_cmp_coor(0.240))
        configs_frame.place(relx=0.010, rely=0.000, relwidth=0.990, relheight=0.380)
        f_input_frame.place(relx=0.010, rely=0.385, relwidth=0.990, relheight=0.130)
        output__frame.place(relx=0.010, rely=0.520, relwidth=0.990, relheight=0.130)
        operate_frame.place(relx=0.010, rely=0.655, relwidth=0.990, relheight=0.120)
        logsout_frame.place(relx=0.010, rely=0.780, relwidth=0.990, relheight=0.240)

        # -------------- configs_frame -> Label -----------------
        # 放置输入框，并设置位置
        tkinter.Label(configs_frame, Lable_style, text="WORK_MODE    ").grid(Lable_grid, row=get_row(ini=1))
        tkinter.Label(configs_frame, Lable_style, text="TDC bin width").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="MIPI RATE    ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="SCAN_MODE    ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="V_ROLL_NUM   ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="H_ROLL_NUM   ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="H_VLD_SEG    ").grid(Lable_grid, row=get_row(ini=0))

        # -------------- configs_frame -> input cmp -----------------
        work_mode_cfg_cmp.grid(Entry_grid, row=get_row(ini=1), column=1)
        tdc_bin_width_cmp.grid(Entry_grid, row=get_row(ini=0), column=1)
        mipi_rate_cfg_cmp.grid(Entry_grid, row=get_row(ini=0), column=1)
        scan_mode_cfg_cmp.grid(Entry_grid, row=get_row(ini=0), column=1)
        vroll_num_cfg_cmp.grid(Scale_grid, row=get_row(ini=0), column=1)
        hroll_num_cfg_cmp.grid(Scale_grid, row=get_row(ini=0), column=1)
        h_vld_seg_cfg_cmp.grid(Scale_grid, row=get_row(ini=0), column=1)

        # -------------- input_frame -> input cmp -----------------
        cali_file_sel_cmp.grid(Entry_grid, row=get_row(ini=1), column=0, columnspan=2)
        cfgs_file_sel_cmp.grid(Entry_grid, row=get_row(ini=0), column=0, columnspan=2)

        cali_file_sel_btn = tkinter.Button(f_input_frame, Button_style, text='Load ROI file', command=_open_cali_file)
        cfgs_file_sel_btn = tkinter.Button(f_input_frame, Button_style, text='Sel Config file',
                                           command=_open_config_file)
        cali_file_sel_btn.grid(Button_grid, row=get_row(ini=1), column=2)
        cfgs_file_sel_btn.grid(Button_grid, row=get_row(ini=0), column=2)

        # -------------- output__frame -> input cmp -----------------
        tkinter.Label(output__frame, Lable_style, text="REG CFG File ").grid(Lable_grid, row=get_row(ini=1))
        tkinter.Label(output__frame, Lable_style, text="ROI SRAM File").grid(Lable_grid, row=get_row(ini=0))
        fname_for_cfg_cmp.grid(Entry_grid, row=get_row(ini=1), column=1, columnspan=1)
        fname_for_roi_cmp.grid(Entry_grid, row=get_row(ini=0), column=1, columnspan=1)

        # -------------- bottom_operate_frame -> button -----------------
        button_row = 0
        previw1_btn = tkinter.Button(operate_frame, Button_style, text="Preview", command=_preview_update1)
        save_dt_btn = tkinter.Button(operate_frame, Button_style, text="Save", command=_do_save)
        clr_log_btn = tkinter.Button(operate_frame, Button_style, text="Clear Log", command=_log_clr)

        previw1_btn.grid(Button_grid, row=button_row, column=0)
        save_dt_btn.grid(Button_grid, row=button_row, column=1)
        clr_log_btn.grid(Button_grid, row=button_row, column=2)

    # --------------- 隐藏按钮显示 ------------------
    def _hidden_btn(event):
        _log_update("The Debug operation button is displayed.")
        reload_btn = tkinter.Button(operate_frame, Button_style, text="RELOAD", command=_reload)
        preview0_btn = tkinter.Button(operate_frame, Button_style, text="Preview0", command=_preview_update0)

        reload_btn.grid(Button_grid, row=2, column=0)
        preview0_btn.grid(Button_grid, row=2, column=1)

    operate_frame.bind_all('<Control-e>', _hidden_btn)  # Control-e 显示 debug 按钮

    def _set_default_value():
        work_mode_cfg_cmp.current(cfg['WORK_MODE'])  # 通过 current() 设置下拉菜单选项的默认值
        scan_mode_cfg_cmp.current(cfg['SCAN_MODE'])  # 通过 current() 设置下拉菜单选项的默认值
        mipi_rate_cfg_cmp.current(mipi_rate_value.index(cfg['MIPI_RATE']))  # 通过 current() 设置下拉菜单选项的默认值
        tdc_bin_width_cmp.current(bin_width_value.index(cfg['TDC_BIN_W']))  # 通过 current() 设置下拉菜单选项的默认值
        vroll_num_cfg_cmp.set(cfg['V_ROLL_NUM'] + 1)
        hroll_num_cfg_cmp.set(cfg['H_ROLL_NUM'] + 1)
        h_vld_seg_cfg_cmp.set(cfg['H_VLD_SEG'] + 1)

        # 插入默认文本
        fname_for_cfg_cmp.delete(0, "end")
        fname_for_cfg_cmp.insert(0, cfg['config_name'])
        fname_for_roi_cmp.delete(0, "end")
        fname_for_roi_cmp.insert(0, cfg['roi_name'])

        config_filename.set(cfg['ref_cfg_file'])

    # ------------------ 启动初始化 -----------------------
    try:
        cfg = PubMethod.ReadJsonFile('HawkConfig.json')
        config_mapping(cfg)
        arrays = [np.zeros((576, 768))]
        # _msku_draw()
    except BaseException as e:
        raise ValueError(f"System initialization failed. Log: {e}")

    # ----------------------- 画图 -------------------
    fig = plt.figure()
    ax = fig.gca()
    # ani = animation.FuncAnimation(fig, update, range(len(arrays)), interval=700, blit=True)
    ani = Player.Player(fig, update, interval=700, blit=True, cache_frame_data=False, save_count=2, maxi=1000000)
    canvas = FigureCanvasTkAgg(fig, master=frame_roi_img)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    # plt.close(fig)

    # -------------- 左侧栏初始化 ----------------
    _set_dsp()
    _set_default_value()
    tkinter.mainloop()
    return


if __name__ == '__main__':
    msku_gui()

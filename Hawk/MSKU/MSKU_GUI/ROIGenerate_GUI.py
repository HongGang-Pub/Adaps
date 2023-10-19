import re
import tkinter
from tkinter import filedialog
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.ticker import MultipleLocator

from Hawk.MSKU import MskuPubMethod, Player
from Hawk.MSKU.MSKU_Cali import ROICalibration
from Hawk.MSKU.MSKU_GEN import ROIGenerate
from SelfDefinedPackge import PubMethod


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
        if len(data) < 2:
            raise ValueError(f"Calibration data format error.\n"
                             f"line{5}: {data}")

        _start_index = int(data[1])
        _seg_num = int(data[0]) // 48
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

    MskuPubMethod.roi_imag(msku_roi_mem, cfg, f_name=cfg['file_name'], fd_path=cfg["fd_path"])

    for index in range(len(zone_mem)):
        per_zone_mem = zone_mem[index] + msku_roi_mem[index]
        roi_data = roi_data + per_zone_mem

    file = "{}.txt".format(cfg['file_name'])
    MskuPubMethod.roi_data_save(f_name=file, data=roi_data, fd_path=cfg["fd_path"])
    return "ROI 生成完成！！！"


def msku_gui():
    # ===============================================================================================
    # 窗口显示属性配置
    # ===============================================================================================
    window = tkinter.Tk()
    window.title("Hawk ROI Generate 1.0")  # 标题
    # window.iconbitmap(r"C:\Users\honggang.li\OneDrive\图片\favicon1.ico")  # icon
    window.iconphoto(False, tkinter.PhotoImage(file=r".file\icon.png"))
    width = 1200
    height = 800
    window.minsize(width, height)
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)

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
        x = x+5 if x < 610 else 610
        y = y-12 if y > 30 else y+37
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
    company_icons = tkinter.Frame(window, background='white')    # 左上添加 frame 控件用于展示公司图片
    frame_roi_img = tkinter.Frame(window)                       # 左下添加 frame 控件用于展示动图
    frame_roi_cfg = tkinter.Frame(window)                       # 右侧添加 frame 控件用于放置 配置、按钮、日志打印等内容

    # --------------------- company_icon 设置 -------------------
    imag = Image.open(r'.file\company_icon.png')
    photo = ImageTk.PhotoImage(imag)
    tkinter.Label(company_icons, image=photo, background='white').pack(fill=tkinter.BOTH)

    # ----------------- frame_roi_cfg 增加多个控件，显示不同交互内容 -------------------
    register_config_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 寄存器配置控件
    califile_select_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 文件选择控件
    bottoms_operate_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 按钮操作控件
    operation_print_frame = tkinter.Frame(frame_roi_cfg, bg='white')  # 操作日志打印控件

    # -------------------------- SCAN_MODE ----------------------------------
    Entry_width = 20  # 输入框显示宽度

    def _scan_mode_update(event):
        scan_mode = scan_mode_cfg_cmp.get()
        cfg['SCAN_MODE'] = 0 if scan_mode == '1D SCAN_MODE' else 1

    scan_mode_cfg_cmp = ttk.Combobox(register_config_frame, width=Entry_width)
    scan_mode_cfg_cmp['value'] = ('1D SCAN_MODE', '2D SCAN_MODE')  # 设置下拉菜单中的值
    scan_mode_cfg_cmp['state'] = "readonly"  # 设置下拉框只读
    scan_mode_cfg_cmp.bind("<<ComboboxSelected>>", _scan_mode_update)

    # -------------------------- ROI相关文件存储文件名配置 ---------------------------
    fname_for_roi_cmp = tkinter.Entry(register_config_frame)

    # -------------------------- V_ROLL_NUM -------------------------------------------
    def _vroll_update(value):
        cfg['V_ROLL_NUM'] = int(value) - 1

    vroll_cfg_cmp = tkinter.Scale(register_config_frame,
                                  from_=1,
                                  to=32,
                                  command=_vroll_update,
                                  resolution=1,  # 设置 Scale 组件的分辨率（每点击一下移动的步长）
                                  length=180,
                                  sliderlength=20,
                                  tickinterval=8,  # 设置刻度滑动条的间隔
                                  orient=tkinter.HORIZONTAL  # 设置Scale控件平方向显示
                                  )

    # -------------------------- H_ROLL_NUM --------------------------------------------
    def _hroll_update(value):
        cfg['H_ROLL_NUM'] = int(value) - 1

    hroll_cfg_cmp = tkinter.Scale(register_config_frame,
                                  from_=1,
                                  to=16,
                                  command=_hroll_update,
                                  resolution=1,
                                  length=180,
                                  sliderlength=20,
                                  tickinterval=8,
                                  orient=tkinter.HORIZONTAL
                                  )

    # -------------------------- H_VLD_SEG --------------------------------------------
    def _h_vld_seg_update(value):
        cfg['H_VLD_SEG'] = int(value) - 1

    h_vld_seg_cfg_cmp = tkinter.Scale(register_config_frame,
                                      from_=1,
                                      to=16,
                                      command=_h_vld_seg_update,
                                      resolution=1,
                                      length=180,
                                      sliderlength=20,
                                      tickinterval=8,
                                      orient=tkinter.HORIZONTAL
                                      )

    # ---------------------------- 标定文件选择窗口 ----------------------
    file_sel_row = 0

    def _open_file():
        try:
            filepath = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")],
                                                  initialdir=r'Input',
                                                  title='Cali Data Select')
            filename.set(filepath)
        except Exception as e:
            # log_print_window.insert(tkinter.INSERT, "您没有选择任何文件:{}\n".format(e))
            _log_update(f"Preview failed! You have not selected any file.{e}", log_type=2)

    filename = tkinter.StringVar()
    cali_file_sel_cmp = tkinter.Entry(califile_select_frame, textvariable=filename, width=30)
    cali_file_sel_cmp.grid(row=file_sel_row, column=0, columnspan=2, padx=3, pady=5, ipady=5, sticky='W')
    cali_file_sel_cmp['state'] = "readonly"  # 设置文本展示框

    cali_file_sel_btn = tkinter.Button(califile_select_frame, text='Load ROI file', command=_open_file, width=12)
    cali_file_sel_btn.grid(row=file_sel_row, column=2, padx=3)

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
            if filename.get() == '':
                # log_print_window.insert(tkinter.INSERT, "没有选取任何文件！！！\n")
                _log_update('Preview failed! You have not selected any file.', log_type=2)
                return
            cali_data, log = DirectAccessCaliData(filename.get(), cfg)
            msku_roi_mem = MskuRoiGenerateForCaliData(cali_data, cfg)

            _preview_trigger()
            _log_update(f"Displaying...", log_type=0)

            if log is not None:     # 打印标定文件校验的日志信息
                _log_update(log, log_type=1)
            return
        except BaseException as e:
            _log_update(f"Preview failed! Log：{e}", log_type=2)
            return

    # ------------------------ 保存按钮 ------------------------
    def _do_save():
        try:
            _log_update('Saving...', log_type=0)
            if preview_triggered is False:
                _log_update('Error! You have not configured anything yet.', log_type=2)
                return
            cfg['file_name'] = fname_for_roi_cmp.get()  # 获取界面上配置的文件名
            RoiMemGenerate(cfg, msku_roi_mem)
            _log_update('Save successfully.', log_type=0)
            return
        except BaseException as e:
            _log_update(f"Save failure! Log：{e}", log_type=2)
            return
        # log_print_window.insert(tkinter.INSERT, '保存成功！\n')

    # ------------------------ RELOAD按钮 ------------------------
    def _reload():
        nonlocal cfg
        # log_print_window.insert(tkinter.INSERT, '开始保存...\n')
        _log_update('Reload script...')
        try:
            cfg = PubMethod.ReadJsonFile('ROIConfig.json')
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

    log_windows_frame = tkinter.LabelFrame(operation_print_frame, text='Log')
    log_windows_frame.pack(fill=tkinter.BOTH)

    log_print_cmp = tkinter.Text(log_windows_frame, width=30, height=30, undo=True, autoseparators=False, wrap='word')
    log_print_cmp.pack(fill=tkinter.BOTH)

    log_print_cmp.insert(tkinter.INSERT, 'Working!!!\n')
    log_print_cmp.configure(state='disabled')

    # -------------------------配置布局，以及默认值并打开窗口------------------------------
    def _set_dsp():
        # ------------------ window -> frame -----------------
        company_icons.place(relx=0.005, rely=0.005, relwidth=0.695, relheight=0.100)
        frame_roi_img.place(relx=0.005, rely=0.110, relwidth=0.695, relheight=0.885)
        frame_roi_cfg.place(relx=0.700, rely=0.000, relwidth=0.295, relheight=0.990)

        # --------------------- frame_roi_cfg -------------------
        register_config_frame.place(relx=0.010, rely=0.005, relwidth=0.990, relheight=0.400)
        califile_select_frame.place(relx=0.010, rely=0.410, relwidth=0.990, relheight=0.150)
        bottoms_operate_frame.place(relx=0.010, rely=0.565, relwidth=0.990, relheight=0.100)
        operation_print_frame.place(relx=0.010, rely=0.670, relwidth=0.990, relheight=0.330)

        # -------------- register_config_frame -> Label -----------------
        label_width = 15  # 文本显示宽度
        # 放置输入框，并设置位置
        (tkinter.Label(register_config_frame, anchor="w", width=label_width, text="Output File Name：").
         grid(row=0, sticky="w", padx=3))
        (tkinter.Label(register_config_frame, anchor="w", width=label_width, text="SCAN_MODE：").
         grid(row=1, sticky="w", padx=3))
        (tkinter.Label(register_config_frame, anchor="w", width=label_width, text="V_ROLL_NUM：").
         grid(row=2, sticky="w", padx=3))
        (tkinter.Label(register_config_frame, anchor="w", width=label_width, text="H_ROLL_NUM：").
         grid(row=3, sticky="w", padx=3))
        (tkinter.Label(register_config_frame, anchor="w", width=label_width, text="H_VLD_SEG：").
         grid(row=4, sticky="w", padx=3))

        # -------------- register_config_frame -> input cmp -----------------
        fname_for_roi_cmp.grid(row=0, column=1, columnspan=1, padx=10, pady=10, ipady=5, sticky='W')
        scan_mode_cfg_cmp.grid(row=1, column=1, padx=10, pady=5, sticky='W')
        vroll_cfg_cmp.grid(row=2, column=1, padx=10, pady=5, sticky='W')
        hroll_cfg_cmp.grid(row=3, column=1, padx=10, pady=5, sticky='W')
        h_vld_seg_cfg_cmp.grid(row=4, column=1, padx=10, pady=5, sticky='W')

        # -------------- bottom_operate_frame -> button -----------------
        button_row = 0
        preview_btn = tkinter.Button(bottoms_operate_frame, text="Preview", width=10, command=_preview_update1)
        preview_btn.grid(row=button_row, column=0, columnspan=1, sticky="w", padx=10, pady=5)

        save_btn = tkinter.Button(bottoms_operate_frame, text="Save", width=10, command=_do_save)
        save_btn.grid(row=button_row, column=1, columnspan=1, sticky="w", padx=10, pady=5)

        clr_btn = tkinter.Button(bottoms_operate_frame, text="Clear Log", width=10, command=_log_clr)
        clr_btn.grid(row=button_row, column=2, columnspan=1, sticky="w", padx=10, pady=5)

    # --------------- 隐藏按钮显示 ------------------
    def _hidden_btn(event):
        _log_update("The Debug operation button is displayed.")
        reload_btn = tkinter.Button(bottoms_operate_frame, text="RELOAD", width=10, command=_reload)
        reload_btn.grid(row=2, column=0, columnspan=1, sticky="w", padx=10, pady=5)

        preview0_btn = tkinter.Button(bottoms_operate_frame, text="Preview0", width=10, command=_preview_update0)
        preview0_btn.grid(row=2, column=1, columnspan=1, sticky="w", padx=10, pady=5)

    bottoms_operate_frame.bind_all('<Control-e>', _hidden_btn)  # Control-e 显示 debug 按钮

    def _set_default_value():
        scan_mode_cfg_cmp.current(cfg['SCAN_MODE'])  # 通过 current() 设置下拉菜单选项的默认值
        vroll_cfg_cmp.set(cfg['V_ROLL_NUM'] + 1)
        hroll_cfg_cmp.set(cfg['H_ROLL_NUM'] + 1)
        h_vld_seg_cfg_cmp.set(cfg['H_VLD_SEG'] + 1)

        # 插入默认文本
        fname_for_roi_cmp.delete(0, "end")
        fname_for_roi_cmp.insert(0, cfg['file_name'])

    # ------------------ 启动初始化 -----------------------
    try:
        cfg = PubMethod.ReadJsonFile('ROIConfig.json')
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

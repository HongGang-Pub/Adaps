import os
import sys

# sys.path.append(os.path.join(os.getcwd(), "../../SelfDefinedPackge"))
sys.path.append(r"D:\\Git\Adaps\\")
# print(os.getcwd())

import re
import tkinter
from tkinter import filedialog
from tkinter import ttk
from Sony.Script.TkComponentStyle import *
from SelfDefinedPackge import PubMethod
from Sony.Script import histogram
from matplotlib import pyplot as plt
from SelfDefinedPackge.JsonOperation import JsonFunction


def msku_gui():
    # ===============================================================================================
    # 窗口显示属性配置
    # ===============================================================================================
    window = tkinter.Tk()
    # window.iconbitmap(r"C:\Users\honggang.li\OneDrive\图片\favicon1.ico")  # icon
    width = 330
    height = 550
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)
    window.minsize(width, height)

    window.title("Sony Data Analysis")  # 标题

    def _quit():
        histogram.fig_close()
        configs.serialize()
        window.quit()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", _quit)  # 关闭窗口，退出程序，防止后台程序持续占用

    # ===============================================================================================
    # Window 主界面增加 3 个 frame, 分别用于不同用途
    # ===============================================================================================
    MainFrame = tkinter.Frame(window)  # 右侧添加 frame 控件用于放置 配置、按钮、日志打印等内容

    # ----------------- frame_roi_cfg 增加多个控件，显示不同交互内容 -------------------
    configs_frame = tkinter.LabelFrame(MainFrame, text="Config")  # 寄存器配置控件
    f_input_frame = tkinter.LabelFrame(MainFrame, text="Input")  # 文件选择控件
    operate_frame = tkinter.LabelFrame(MainFrame, text="Operate")  # 按钮操作控件
    logsout_frame = tkinter.LabelFrame(MainFrame, text="Log")  # 操作日志打印控件

    # -------------------------- DSP_MODE ----------------------------------
    def _dsp_mode(event):
        _dsp_mode = dsp_mode_cfg.get()
        cfg['dsp_mode'] = 0 if (_dsp_mode == "Display by frame") else 1

    dsp_mode_cfg = ttk.Combobox(configs_frame, width=23)
    dsp_mode_cfg['value'] = ("Display by frame", "Display by point")  # 设置下拉菜单中的值
    dsp_mode_cfg['state'] = "readonly"  # 设置下拉框只读
    dsp_mode_cfg.bind("<<ComboboxSelected>>", _dsp_mode)

    # -------------------------- BIN_FILE_MODE ----------------------------------
    # def binFileAnalysisModeSel():
    #     if var.get():
    #         cfg["binFileAnalysisMode"] = 1
    #     else:
    #         cfg["binFileAnalysisMode"] = 0
    #
    # var = tkinter.BooleanVar()
    # bin_file_dsp_mode = tkinter.Checkbutton(configs_frame, text="拆分Bin文件", variable=var, command=binFileAnalysisModeSel)

    # ---------------------------- 标定文件选择窗口 ----------------------
    def start_bin_validate_input(event):
        # 判断用户按下的键是否是数字或允许的字符（如退格键）
        if event.char.isdigit() or event.char == '\b':
            # 如果是数字或允许的字符，则继续输入
            pass
        else:
            # 如果不是数字或允许的字符，则禁止输入并弹出提示框
            # check_input(content)
            return "break"

    start_bin = tkinter.Entry(configs_frame, relief="solid", width=26)
    start_bin.bind("<Key>", start_bin_validate_input)

    def end_bin_validate_input(event):
        # 判断用户按下的键是否是数字或允许的字符（如退格键）
        if event.char.isdigit() or event.char == '\b':
            # 如果是数字或允许的字符，则继续输入
            pass
        else:
            # 如果不是数字或允许的字符，则禁止输入并弹出提示框
            # check_input(content)
            return "break"

    end_bin = tkinter.Entry(configs_frame, relief="solid", width=26)
    end_bin.bind("<Key>", end_bin_validate_input)

    def pixel_sel_validate_input(event):
        # 判断用户按下的键是否是数字或允许的字符（如退格键）
        if event.char.isdigit() or event.char in ['\b', ' ', ',']:
            # 如果是数字或允许的字符，则继续输入
            pass
        else:
            # 如果不是数字或允许的字符，则禁止输入并弹出提示框
            # check_input(content)
            # tkinter.messagebox.showwarning("警告", "请输入数字！")
            return "break"

    pixel_sel = tkinter.Entry(configs_frame, relief="solid", width=26)
    pixel_sel.bind("<Key>", pixel_sel_validate_input)

    def pixel_sel_validate_input(event):
        # 判断用户按下的键是否是数字或允许的字符（如退格键）
        if event.char.isdigit() or event.char in ['\b', ' ', ',']:
            # 如果是数字或允许的字符，则继续输入
            pass
        else:
            # 如果不是数字或允许的字符，则禁止输入并弹出提示框
            # check_input(content)
            # tkinter.messagebox.showwarning("警告", "请输入数字！")
            return "break"

    pixel_sel = tkinter.Entry(configs_frame, relief="solid", width=26)
    pixel_sel.bind("<Key>", pixel_sel_validate_input)


    def frame_sel_validate_input(event):
        # 判断用户按下的键是否是数字或允许的字符（如退格键）
        if event.char.isdigit() or event.char in ['\b', ' ', ',']:
            # 如果是数字或允许的字符，则继续输入
            pass
        else:
            # 如果不是数字或允许的字符，则禁止输入并弹出提示框
            # check_input(content)
            # tkinter.messagebox.showwarning("警告", "请输入数字！")
            return "break"

    frame_sel = tkinter.Entry(configs_frame, relief="solid", width=26)
    frame_sel.bind("<Key>", frame_sel_validate_input)

    def _get_config():
        cfg['start_bin'] = int(start_bin.get())
        cfg['end_bin'] = int(end_bin.get())
        cfg['pixel_sel'] = pixel_sel.get()
        cfg['frame_sel'] = frame_sel.get()

        if cfg["file_sel"] == '':
            _log_update("请先选择文件!!!", log_type=2)

        # 重新加载文件
        reload_configs = PubMethod.ReadJsonFile('config.json')
        cfg["DynamicLoading"] = reload_configs["DynamicLoading"]

    def _get_file():
        try:
            filepath = filedialog.askopenfilenames(filetypes=[("文本文件", "*.txt"), ("文本文件", "*.bin")],
                                                   # initialdir=r'.',
                                                   title='File Select')
            sel_filename.set(filepath[0])
            cfg["file_sel"] = filepath
            print(cfg["file_sel"])
        except Exception as e:
            # log_print_window.insert(tkinter.INSERT, "您没有选择任何文件:{}\n".format(e))
            _log_update(f"Preview failed! You have not selected any file.{e}", log_type=2)

    sel_filename = tkinter.StringVar()
    file_sel_cmp = tkinter.Entry(f_input_frame, Entry_style, textvariable=sel_filename)
    file_sel_cmp['state'] = "readonly"  # 设置文本展示框

    # ===============================================================================================
    # 添加功能按钮
    # ===============================================================================================
    def _view():
        _get_config()
        histogram.fig_close()
        # histogram.do_work(cfg)
        try:
            _log_update(f"作图中...", log_type=0)
            histogram.do_work(cfg)
            return
        except BaseException as e:
            _log_update(f"View failure! Log：{e}", log_type=2)
            return

    def _more_view():
        _get_config()
        # histogram.do_work(cfg)
        try:
            _log_update(f"作图中...", log_type=0)
            histogram.do_work(cfg)
            return
        except BaseException as e:
            _log_update(f"View failure! Log：{e}", log_type=2)
            return

    def _close_fig():
        try:
            histogram.fig_close()
            _log_update(f"图片全部关闭", log_type=0)
        except BaseException as e:
            _log_update(f"Close figure failure! Log：{e}", log_type=2)
            return

    def _save_fig():
        try:
            _log_update(f"保存中...", log_type=0)
            histogram.fig_save()
            _log_update(f"保存成功...", log_type=0)
        except BaseException as e:
            _log_update(f"Save figure failure! Log：{e}", log_type=2)
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

    log_print_cmp = tkinter.Text(logsout_frame, width=30, height=30, undo=True, autoseparators=False, wrap='word')
    log_print_cmp.pack(fill=tkinter.BOTH)

    # log_print_cmp.insert(tkinter.INSERT, 'Working!!!\n')
    log_print_cmp.configure(state='disabled')

    # -------------------------配置布局，以及默认值并打开窗口------------------------------
    rows = 0

    def get_row(ini=1):
        nonlocal rows
        if ini == 1:  # ini = 1: 进行初始化
            rows = 0
        elif ini == 0:  # ini = 0: 行自加1
            rows += 1
        else:  # ini = -1: 行不增不减
            pass
        return rows

    def _set_dsp():
        # ------------------ window -> frame -----------------
        MainFrame.place(relx=0.005, rely=0.000, relwidth=1.000, relheight=0.990)
        # --------------------- frame_roi_cfg -------------------
        configs_frame.place(relx=0.000, rely=0.000, relwidth=0.990, relheight=0.380)
        f_input_frame.place(relx=0.000, rely=0.385, relwidth=0.990, relheight=0.120)
        operate_frame.place(relx=0.000, rely=0.510, relwidth=0.990, relheight=0.200)
        logsout_frame.place(relx=0.000, rely=0.715, relwidth=0.990, relheight=0.290)

        # -------------- configs_frame -> Label -----------------
        # 放置输入框，并设置位置
        tkinter.Label(configs_frame, Lable_style, text="Meger Sel    ").grid(Lable_grid, row=get_row(ini=1))
        tkinter.Label(configs_frame, Lable_style, text="Start Bin    ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="End Bin      ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="Pixel Sel    ").grid(Lable_grid, row=get_row(ini=0))
        tkinter.Label(configs_frame, Lable_style, text="Frame Sel    ").grid(Lable_grid, row=get_row(ini=0))

        # -------------- configs_frame -> input cmp -----------------
        dsp_mode_cfg.grid(Entry_grid, row=get_row(ini=1), column=1, columnspan=1)
        start_bin.grid(Entry_grid, row=get_row(ini=0), column=1, columnspan=1)
        end_bin.grid(Entry_grid, row=get_row(ini=0), column=1, columnspan=1)
        pixel_sel.grid(Entry_grid, row=get_row(ini=0), column=1, columnspan=1)
        frame_sel.grid(Entry_grid, row=get_row(ini=0), column=1, columnspan=1)

        # Check box
        # bin_file_dsp_mode.grid(CheckButton_style, row=get_row(ini=0), column=0)

        file_sel_btn = tkinter.Button(f_input_frame, Button_style, text='选择文件', command=_get_file)
        file_sel_cmp.grid(Entry_grid, row=get_row(ini=1), column=0, columnspan=2)
        file_sel_btn.grid(Button_grid, row=get_row(ini=-1), column=2)

        # -------------- bottom_operate_frame -> button -----------------
        covr_view_btn = tkinter.Button(operate_frame, Button_style, text="View", command=_view)
        more_view_btn = tkinter.Button(operate_frame, Button_style, text="View+", command=_more_view)
        imag_save_btn = tkinter.Button(operate_frame, Button_style, text="Save", command=_save_fig)
        close_fig_btn = tkinter.Button(operate_frame, Button_style, text="Close", command=_close_fig)
        clear_log_btn = tkinter.Button(operate_frame, Button_style, text="Clear", command=_log_clr)

        covr_view_btn.grid(Button_grid, row=0, column=0)
        more_view_btn.grid(Button_grid, row=0, column=1)
        imag_save_btn.grid(Button_grid, row=0, column=2)
        close_fig_btn.grid(Button_grid, row=1, column=0)
        clear_log_btn.grid(Button_grid, row=1, column=1)

    # --------------- 隐藏按钮显示 ------------------
    def _hidden_btn(event):
        _log_update("The Debug operation button is displayed.")
        # reload_btn = tkinter.Button(operate_frame, Button_style, text="RELOAD", command=_reload)
        # preview0_btn = tkinter.Button(operate_frame, Button_style, text="Preview0", command=_preview_update0)
        #
        # reload_btn.grid(Button_grid, row=2, column=0)
        # preview0_btn.grid(Button_grid, row=2, column=1)

    operate_frame.bind_all('<Control-e>', _hidden_btn)  # Control-e 显示 debug 按钮

    def _set_default_value():
        dsp_mode_cfg.current(cfg['dsp_mode'])  # 通过 current() 设置下拉菜单选项的默认值
        start_bin.delete(0, "end")
        start_bin.insert(0, cfg['start_bin'])
        end_bin.delete(0, "end")
        end_bin.insert(0, cfg['end_bin'])
        pixel_sel.delete(0, "end")
        pixel_sel.insert(0, cfg['pixel_sel'])
        frame_sel.delete(0, "end")
        frame_sel.insert(0, cfg['frame_sel'])
        sel_filename.set(cfg["file_sel"][0])

        # if cfg["binFileAnalysisMode"] == 1:
        #     var.set(True)
        # else:
        #     var.set(False)

    # ------------------ 启动初始化 -----------------------
    try:
        # cfg = PubMethod.ReadJsonFile('config.json')
        configs = JsonFunction(file_path="config.json")
        cfg = configs.items
        # cfg = {"dsp_mode": True,
        #        "start_bin": 0,
        #        "end_bin": 1000,
        #        "pixel_sel": "0, 50, 100, 150, 192",
        #        "file_sel":""}
        # _msku_draw()
    except BaseException as e:
        raise ValueError(f"System initialization failed. Log: {e}")

    # -------------- 左侧栏初始化 ----------------
    _set_dsp()
    _set_default_value()
    tkinter.mainloop()


if __name__ == '__main__':
    msku_gui()

# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.uis.windows.main_window.ui_main import *
from PySide6.QtGui import QColor, QBrush, QTextCursor
from Hawk.HawkGUI_v002.HawkFunction.GlobalDef import MaskingValue
from Hawk.HawkGUI_v002.HawkFunction.Player import Player
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import numpy as np


# FUNCTIONS
class HawkFunctions:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Get config
        # ///////////////////////////////////////////////////////////////
        self.hawk_config = {}   # hawk general config
        self.gui_value_config = {}  # hawk UI function

    # gui initial
    # ///////////////////////////////////////////////////////////////
    def gui_initial(self):
        self.hawk_config['WORK_MODE'] = self.hawk_config['WORK_MODE'] if self.hawk_config['WORK_MODE'] <= 3 else 0
        self.hawk_config['SCAN_MODE'] = self.hawk_config['SCAN_MODE'] if self.hawk_config['SCAN_MODE'] <= 1 else 0
        self.hawk_config['MST_MODE'] = self.hawk_config['MST_MODE'] if self.hawk_config['MST_MODE'] <= 1 else 0
        self.hawk_config['TRG_I_EN'] = self.hawk_config['TRG_I_EN'] if self.hawk_config['TRG_I_EN'] <= 1 else 0
        self.hawk_config['V_ROLL_NUM'] = self.hawk_config['V_ROLL_NUM'] if self.hawk_config['V_ROLL_NUM'] <= 31 else 0
        self.hawk_config['H_ROLL_NUM'] = self.hawk_config['H_ROLL_NUM'] if self.hawk_config['H_ROLL_NUM'] <= 15 else 0
        self.hawk_config['H_VLD_SEG'] = self.hawk_config['H_VLD_SEG'] if self.hawk_config['H_VLD_SEG'] <= 15 else 0
        self.hawk_config['h_seg_shift'] = self.hawk_config['h_seg_shift'] if self.hawk_config['h_seg_shift'] <= 15 else 4

        try:
            MIPI_RATE_index = self.gui_value_config["MIPI_RATE"]["config"].index(self.hawk_config['MIPI_RATE'])
        except:
            self.hawk_config['MIPI_RATE'] = self.gui_value_config["MIPI_RATE"]["config"][0]
            MIPI_RATE_index = 0
        try:
            TDC_BIN_W_index = self.gui_value_config["TDC_BIN_W"]["config"].index(self.hawk_config['TDC_BIN_W'])
        except:
            self.hawk_config['TDC_BIN_W'] = self.gui_value_config["TDC_BIN_W"]["config"][0]
            TDC_BIN_W_index = 0

        # 下拉框设置初始值
        self.ui.load_pages.WORK_MODE_ComboBox.setCurrentIndex(self.hawk_config['WORK_MODE'])
        self.ui.load_pages.WORK_MODE_ComboBox_2.setCurrentIndex(self.hawk_config['WORK_MODE'])
        self.ui.load_pages.MIPI_RATE_ComboBox.setCurrentIndex(MIPI_RATE_index)
        self.ui.load_pages.MIPI_RATE_ComboBox_2.setCurrentIndex(MIPI_RATE_index)
        self.ui.load_pages.SCAN_MODE_ComboBox.setCurrentIndex(self.hawk_config['SCAN_MODE'])
        self.ui.load_pages.SCAN_MODE_ComboBox_2.setCurrentIndex(self.hawk_config['SCAN_MODE'])
        self.ui.load_pages.MST_MODE_ComboBox.setCurrentIndex(self.hawk_config['MST_MODE'])
        self.ui.load_pages.TRG_I_EN_ComboBox.setCurrentIndex(self.hawk_config['TRG_I_EN'])
        self.ui.load_pages.TDC_Bin_Width_ComboBox.setCurrentIndex(TDC_BIN_W_index)

        # 滚动条设置初始值
        self.ui.load_pages.V_ROLL_NUM_Slider.setValue(self.hawk_config['V_ROLL_NUM']+1)
        self.ui.load_pages.V_ROLL_NUM_Slider_2.setValue(self.hawk_config['V_ROLL_NUM']+1)
        self.ui.load_pages.H_ROLL_NUM_Slider.setValue(self.hawk_config['H_ROLL_NUM']+1)
        self.ui.load_pages.H_ROLL_NUM_Slider_2.setValue(self.hawk_config['H_ROLL_NUM']+1)
        self.ui.load_pages.H_VLD_SEG_Slider.setValue(self.hawk_config['H_VLD_SEG']+1)
        self.ui.load_pages.H_VLD_SEG_Slider_2.setValue(self.hawk_config['H_VLD_SEG']+1)
        self.ui.load_pages.H_SEG_Shift_Slider.setValue(self.hawk_config['h_seg_shift'])
        self.ui.load_pages.H_SEG_Shift_Slider_2.setValue(self.hawk_config['h_seg_shift'])

        # 文本框设置初始值
        self.ui.load_pages.Sel_Config_file_LineEdit.setText(self.hawk_config['ref_cfg_file'])
        self.ui.load_pages.REG_CFG_File_LineEdit.setText(self.hawk_config['config_name'])
        self.ui.load_pages.ROI_SRAM_File_LineEdit.setText(self.hawk_config['roi_name'])

        # 显示动图
        # self.fig = plt.figure()
        # self.ax = self.fig.gca()
        # ani = Player(self.fig, self.update, interval=700, blit=True, cache_frame_data=False, save_count=2, maxi=1000000)
        # # plt.show()
        # canvas = FigureCanvas(self.fig, master=MaskingValue.frame_roi_img)  # A tk.DrawingArea.
        # canvas.draw()
        return

    # 文件选择对话框
    # ///////////////////////////////////////////////////////////////
    def Sel_Config_file_func(self):
        file = QFileDialog.getOpenFileName(parent=None, caption='Config File Select', dir='Input',
                                           filter='file(*.txt) ;')
        if file[0] == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.Sel_Config_file_LineEdit.setText(file[0])
        self.hawk_config['ref_cfg_file'] = file[0]
        # print(self.hawk_config['ref_cfg_file'])

    def Load_ROI_file_func(self):
        file = QFileDialog.getOpenFileName(parent=None, caption='Cali Data Select', dir='Input',
                                           filter='file(*.txt) ;')
        if file[0] == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.Load_ROI_file_LineEdit.setText(file[0])
        self.hawk_config['cali_file'] = file[0]
        # print(self.hawk_config['cali_filename'])

    # 下拉框值更新
    # ///////////////////////////////////////////////////////////////
    def WORK_MODE_UPDATE(self, i):
        self.hawk_config['WORK_MODE'] = i
        print(self.hawk_config['WORK_MODE'])

    def SCAN_MODE_UPDATE(self, i):
        self.hawk_config['SCAN_MODE'] = i
        print(self.hawk_config['SCAN_MODE'])

    def MST_MODE_UPDATE(self, i):
        self.hawk_config['MST_MODE'] = i
        print(self.hawk_config['MST_MODE'])

    def TRG_I_EN_UPDATE(self, i):
        self.hawk_config['TRG_I_EN'] = i
        print(self.hawk_config['TRG_I_EN'])

    def MIPI_RATE_UPDATE(self, i):
        self.hawk_config['MIPI_RATE'] = self.gui_value_config["MIPI_RATE"]["config"][i]
        print(self.hawk_config['MIPI_RATE'])

    def TDC_BIN_W_UPDATE(self, i):
        self.hawk_config['TDC_BIN_W'] = self.gui_value_config["TDC_BIN_W"]["config"][i]
        print(self.hawk_config['TDC_BIN_W'])

    def V_ROLL_NUM_UPDATE(self, num):
        self.hawk_config['V_ROLL_NUM'] = num-1
        print(self.hawk_config['V_ROLL_NUM'])

    def H_ROLL_NUM_UPDATE(self, num):
        self.hawk_config['H_ROLL_NUM'] = num-1
        print(self.hawk_config['H_ROLL_NUM'])

    def H_VLD_SEG_UPDATE(self, num):
        self.hawk_config['H_VLD_SEG'] = num-1
        print(self.hawk_config['H_VLD_SEG'])

    def h_seg_shift_UPDATE(self, num):
        self.hawk_config['h_seg_shift'] = num
        print(self.hawk_config['h_seg_shift'])

    def get_input_text(self):
        self.hawk_config['config_name'] = self.ui.load_pages.REG_CFG_File_LineEdit.text()
        self.hawk_config['roi_name'] = self.ui.load_pages.ROI_SRAM_File_LineEdit.text()
        print(self.hawk_config['config_name'], self.hawk_config['roi_name'])

    def log_print(self, log, log_type):
        if self.settings["theme_name"] == "dark":
            theme = ["#DFE1E2", "yellow", "red"]
        else:
            theme = ["#9DA9B5", "blue", "red"]
        color = theme[log_type]
        logTextEdit = self.ui.load_pages.LogPrintWindow
        cursor = logTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)

        text_format = logTextEdit.currentCharFormat()  # 创建TextCharFormat对象 获取当前字文本的字符串格式
        text_format.setForeground(QBrush(QColor(color)))  # 设置字体颜色
        cursor.mergeCharFormat(text_format)  # 追加格式到原有文本
        cursor.insertText(f"{log}")
        logTextEdit.setTextCursor(cursor)
        logTextEdit.ensureCursorVisible()
        cursor.insertText(f"\n")

    def update(self, i):
        """ 动态图片更新函数 """
        if MaskingValue.preview_update_symbol is True:
            MaskingValue.frame_cnt = i
            preview_update_symbol = False

        subframe_index = (i - MaskingValue.frame_cnt) % len(MaskingValue.arrays)

        # print(i, frame_cnt, subframe_index)

        self.ax.cla()
        # --------------------- 配置刻度 --------------------
        self.ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        self.ax.xaxis.set_major_locator(MultipleLocator(48))
        self.ax.yaxis.set_major_locator(MultipleLocator(50))

        imgs = self.ax.imshow(X=MaskingValue.arrays[subframe_index])

        if not (subframe_index < len(MaskingValue.info)):
            return [imgs]

        # ------------- title config -------------------
        x, y, s = MaskingValue.info[subframe_index]
        _str = f"{s}({x}, {y})"
        x = x + 5 if x < 610 else 610
        y = y - 12 if y > 30 else y + 37
        y = y if y < 565 else 565
        title = self.ax.text(x, y, _str, fontdict={
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

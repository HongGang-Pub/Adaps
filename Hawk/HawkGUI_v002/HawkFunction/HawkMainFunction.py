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


# FUNCTIONS
class HawkFunctions:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.hawk_config = {}
        self.gui_value_config = {}
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

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
        self.ui.load_pages.MIPI_RATE_ComboBox.setCurrentIndex(MIPI_RATE_index)
        self.ui.load_pages.SCAN_MODE_ComboBox.setCurrentIndex(self.hawk_config['SCAN_MODE'])
        self.ui.load_pages.MST_MODE_ComboBox.setCurrentIndex(self.hawk_config['MST_MODE'])
        self.ui.load_pages.TRG_I_EN_ComboBox.setCurrentIndex(self.hawk_config['TRG_I_EN'])
        self.ui.load_pages.TDC_Bin_Width_ComboBox.setCurrentIndex(TDC_BIN_W_index)

        # 滚动条设置初始值
        self.ui.load_pages.V_ROLL_NUM_Slider.setValue(self.hawk_config['V_ROLL_NUM']+1)
        self.ui.load_pages.H_ROLL_NUM_Slider.setValue(self.hawk_config['H_ROLL_NUM']+1)
        self.ui.load_pages.H_VLD_SEG_Slider.setValue(self.hawk_config['H_VLD_SEG']+1)
        self.ui.load_pages.H_SEG_Shift_Slider.setValue(self.hawk_config['h_seg_shift']+1)

        # 文本框设置初始值
        self.ui.load_pages.Load_ROI_file_LineEdit.setText(self.hawk_config['ref_cfg_file'])
        self.ui.load_pages.REG_CFG_File_LineEdit.setText(self.hawk_config['config_name'])
        self.ui.load_pages.ROI_SRAM_File_LineEdit.setText(self.hawk_config['roi_name'])
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

import logging

from Hawk.HawkGUI_v002.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.uis.windows.main_window.ui_main import *
from Hawk.HawkGUI_v002.HawkFunction.ROIZoneConfig import ROIZoneConfigWin
from functools import partial


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
    def setup_gui(self):
        # Instans ROI_Zone_Config Win
        self.ui_zone_config_win = ROIZoneConfigWin(self.qssStyle)

        # 配置下拉选项
        self.ui.load_pages.REF_CLK_Config_ComboBox.addItems(self.gui_value_config["REF_CLK"]["show_gui"])
        self.ui.load_pages.SYS_CLK_Config_ComboBox.addItems(self.gui_value_config["SYS_CLK"]["show_gui"])
        self.ui.load_pages.MST_MODE_ComboBox.addItems(self.gui_value_config["MST_MODE"]["show_gui"])
        self.ui.load_pages.TRG_I_EN_ComboBox.addItems(self.gui_value_config["TRG_I_EN"]["show_gui"])
        self.ui.load_pages.WORK_MODE_ComboBox.add_items(self.gui_value_config["WORK_MODE"]["show_gui"])
        self.ui.load_pages.TDC_Bin_Width_ComboBox.addItems(self.gui_value_config["TDC_BIN_W"]["show_gui"])
        self.ui.load_pages.MIPI_RATE_ComboBox.add_items(self.gui_value_config["MIPI_RATE"]["show_gui"])
        self.ui.load_pages.SCAN_MODE_ComboBox.addItems(self.gui_value_config["SCAN_MODE"]["show_gui"])

        REF_CLK_index = self.gui_value_config["REF_CLK"]["config"].index(self.hawk_config['FREF_CLK'])
        MST_MODE_index = self.gui_value_config["MST_MODE"]["config"].index(self.hawk_config['MST_MODE'])
        TRG_I_EN_index = self.gui_value_config["TRG_I_EN"]["config"].index(self.hawk_config['TRG_I_EN'])
        TDC_BIN_W_index = self.gui_value_config["TDC_BIN_W"]["config"].index(self.hawk_config['TDC_BIN_W'])
        SYS_CLK_index = 2 - TDC_BIN_W_index % 3
        SCAN_MODE_index = self.gui_value_config["SCAN_MODE"]["config"].index(self.hawk_config['SCAN_MODE'])
        WORK_MODE_indexs = [self.gui_value_config["WORK_MODE"]["config"].index(config) for config in self.hawk_config['WORK_MODE']]
        MIPI_RATE_indexs = [self.gui_value_config["MIPI_RATE"]["config"].index(config) for config in self.hawk_config['MIPI_RATE']]

        # 下拉框设置初始值
        self.ui.load_pages.REF_CLK_Config_ComboBox.setCurrentIndex(REF_CLK_index)
        self.ui.load_pages.MST_MODE_ComboBox.setCurrentIndex(MST_MODE_index)
        self.ui.load_pages.TRG_I_EN_ComboBox.setCurrentIndex(TRG_I_EN_index)
        self.ui.load_pages.TDC_Bin_Width_ComboBox.setCurrentIndex(TDC_BIN_W_index)
        self.ui.load_pages.SYS_CLK_Config_ComboBox.setCurrentIndex(SYS_CLK_index)
        self.ui.load_pages.SCAN_MODE_ComboBox.setCurrentIndex(SCAN_MODE_index)
        self.ui.load_pages.WORK_MODE_ComboBox.select_indexs(WORK_MODE_indexs)
        self.ui.load_pages.MIPI_RATE_ComboBox.select_indexs(MIPI_RATE_indexs)

        # 滚动条设置初始值
        self.ui.load_pages.V_ROLL_NUM_Slider.setValue(self.hawk_config['V_ROLL_NUM']+1)
        self.ui.load_pages.H_ROLL_NUM_Slider.setValue(self.hawk_config['H_ROLL_NUM']+1)
        self.ui.load_pages.H_VLD_SEG_Slider.setValue(self.hawk_config['H_VLD_SEG']+1)

        # 文本框设置初始值
        self.ui.load_pages.Sel_Config_file_LineEdit.setText(self.hawk_config['ref_cfg_file'])
        self.ui.load_pages.REG_CFG_File_LineEdit.setText(self.hawk_config['config_name'])
        self.ui.load_pages.ROI_SRAM_File_LineEdit.setText(self.hawk_config['roi_name'])

        # 按钮绑定
        self.ui.load_pages.Sel_Config_file_Button.clicked.connect(partial(HawkFunctions.Sel_Config_file_func, self))
        self.ui.load_pages.Load_ROI_file_Button.clicked.connect(partial(HawkFunctions.Load_ROI_file_func, self))
        self.ui.load_pages.Save.clicked.connect(partial(HawkFunctions.get_input_text, self))

        self.ui.load_pages.WORK_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.WORK_MODE_UPDATE, self))
        self.ui.load_pages.SCAN_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.SCAN_MODE_UPDATE, self))
        self.ui.load_pages.MIPI_RATE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.MIPI_RATE_UPDATE, self))
        self.ui.load_pages.MST_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.MST_MODE_UPDATE, self))
        self.ui.load_pages.TRG_I_EN_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.TRG_I_EN_UPDATE, self))
        self.ui.load_pages.TDC_Bin_Width_ComboBox.currentIndexChanged.connect(
            partial(HawkFunctions.TDC_BIN_W_UPDATE, self))
        self.ui.load_pages.V_ROLL_NUM_Slider.valueChanged.connect(partial(HawkFunctions.V_ROLL_NUM_UPDATE, self))
        self.ui.load_pages.H_ROLL_NUM_Slider.valueChanged.connect(partial(HawkFunctions.H_ROLL_NUM_UPDATE, self))
        self.ui.load_pages.H_VLD_SEG_Slider.valueChanged.connect(partial(HawkFunctions.H_VLD_SEG_UPDATE, self))
        self.ui.load_pages.ROIZoneConfig.linkActivated.connect(partial(HawkFunctions.OpenROIZoneConfigWin, self))
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

    def OpenROIZoneConfigWin(self, url):
        logging.info("Open ROI zone config window...")
        self.ui_zone_config_win.setModal(True)
        self.ui_zone_config_win.show(self.hawkzoneconfig)

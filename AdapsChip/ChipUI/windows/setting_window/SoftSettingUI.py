import copy
import logging
import gc

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.windows.main_window.ui_main import UI_MainWindow

# from AdapsChip.ChipUI.gui.uis.windows.main_window.ui_main import *
from AdapsChip.Hawk01.Common.ScriptRegConfig import *
from functools import partial


# FUNCTIONS
class SoftMainUI:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()

        # Get config
        # ///////////////////////////////////////////////////////////////
        self.soft_config = {}

    # ///////////////////////////////////////////////////////////////
    # gui initial
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        """调用各个界面的 setup_gui, 完成界面初始化"""
        SoftMainUI.general_setting_gui(self)
        return

    # ///////////////////////////////////////////////////////////////
    # Script config window function
    # ///////////////////////////////////////////////////////////////
    def general_setting_gui(self):
        # 下拉框设置初始值
        self.ui.load_pages.roi_image_save_ComboBox.setCurrentIndex(self.soft_config["roi_image_save"])
        self.ui.load_pages.roi_data_fromat_ComboBox.setCurrentIndex(self.soft_config["roi_data_format"])

        # 操作绑定
        self.ui.load_pages.roi_image_save_ComboBox.currentIndexChanged.connect(
            partial(SoftMainUI.UPDATE_ROI_IMG_SAVE, self))
        self.ui.load_pages.roi_data_fromat_ComboBox.currentIndexChanged.connect(
            partial(SoftMainUI.UPDATE_ROI_DATA_FORMAT, self))
        return

    # 下拉框值更新
    # ///////////////////////////////////////////////////////////////
    def UPDATE_ROI_IMG_SAVE(self, i):
        self.soft_config["roi_image_save"] = i

    def UPDATE_ROI_DATA_FORMAT(self, i):
        self.soft_config["roi_data_format"] = i

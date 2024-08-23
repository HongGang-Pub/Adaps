# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.windows.main_window.ui_main import UI_MainWindow
from functools import partial
from SelfDefinedPackge.JsonOperation import JsonFunction


# FUNCTIONS
class SoftMainUI:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ///////////////////////////////////////////////////////////////
    # gui initial
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # Load Soft Config
        # ///////////////////////////////////////////////////////////////
        self.SoftConfig = JsonFunction(file_path="./SoftConfig.json")
        self.soft_config = self.SoftConfig.items
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

    def closeEvent(self):
        self.SoftConfig.serialize()
        pass
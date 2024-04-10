import os
import sys
sys.path.append(os.path.join(os.getcwd(), "../../"))

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
from functools import partial
from SelfDefinedPackge.JsonOperation import JsonFunction

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.qt_core import *

# IMPORT SETTINGSpy
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT HawkFunction
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.HawkFunction.HawkMainFunction import HawkFunctions
from Hawk.HawkGUI_v002.HawkFunction.MaskingWindow import MaskingWindow


# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
# os.environ["QT_FONT_DPI"] = "96"

# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD HawkConfig.json
        # ///////////////////////////////////////////////////////////////
        gui_value_config = JsonFunction(file_path=".HawkConfig/HawkGuiConfig.json")
        self.gui_value_config = gui_value_config.items

        hawk_config = JsonFunction(file_path=".HawkConfig/HawkConfig.json")
        self.hawk_config = hawk_config.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.masking_win = MaskingWindow()
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)
        HawkFunctions.gui_initial(self)

        # Connect Function
        # ///////////////////////////////////////////////////////////////
        # self.ui.load_pages.Sel_Config_file_Button.clicked.connect(partial(HawkFunctions.Sel_Config_file_func, self))
        # self.ui.load_pages.Load_ROI_file_Button.clicked.connect(partial(HawkFunctions.Load_ROI_file_func, self))
        # self.ui.load_pages.Save.clicked.connect(partial(HawkFunctions.get_input_text, self))
        # self.ui.load_pages.Preview.clicked.connect(partial(HawkFunctions.log_print, self, "11111111111111", 0))
        # self.ui.load_pages.Save.clicked.connect(partial(HawkFunctions.log_print, self, "222222222222222", 1))
        # self.ui.load_pages.ClearLog.clicked.connect(partial(HawkFunctions.log_print, self, "333333333333", 2))
        #
        # self.ui.load_pages.WORK_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.WORK_MODE_UPDATE, self))
        # self.ui.load_pages.SCAN_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.SCAN_MODE_UPDATE, self))
        # self.ui.load_pages.MIPI_RATE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.MIPI_RATE_UPDATE, self))
        # self.ui.load_pages.MST_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.MST_MODE_UPDATE, self))
        # self.ui.load_pages.TRG_I_EN_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.TRG_I_EN_UPDATE, self))
        # self.ui.load_pages.TDC_Bin_Width_ComboBox.currentIndexChanged.connect(
        #     partial(HawkFunctions.TDC_BIN_W_UPDATE, self))
        # self.ui.load_pages.V_ROLL_NUM_Slider.valueChanged.connect(partial(HawkFunctions.V_ROLL_NUM_UPDATE, self))
        # self.ui.load_pages.H_ROLL_NUM_Slider.valueChanged.connect(partial(HawkFunctions.H_ROLL_NUM_UPDATE, self))
        # self.ui.load_pages.H_VLD_SEG_Slider.valueChanged.connect(partial(HawkFunctions.H_VLD_SEG_UPDATE, self))
        # self.ui.load_pages.H_SEG_Shift_Slider.valueChanged.connect(partial(HawkFunctions.h_seg_shift_UPDATE, self))

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            GuiMainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        elif btn.objectName() == "btn_more_config":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            GuiMainFunctions.set_page(self, self.ui.load_pages.page_2)

        # LOAD USER PAGE
        elif btn.objectName() == "btn_settings":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3
            GuiMainFunctions.set_page(self, self.ui.load_pages.page_3)

        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("gui/icon.ico"))

    # SHOW MAIN WINDOW
    # ///////////////////////////////////////////////////////////////
    window = MainWindow()
    window.show()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())

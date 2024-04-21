import logging
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
from Hawk.HawkGUI_v002.HawkToolFunction.HawkToolbox import HawkToolbox
from SelfDefinedPackge import MatplotExtension
from SelfDefinedPackge.LogerPubMethod import *


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
        if self.settings["theme_name"] == "dark":
            styleFile = r"gui/themes/page_themes/dark/darkstyle.qss"
        else:
            styleFile = r"gui/themes/page_themes/light/lightstyle.qss"
        try:
            with open(styleFile, 'r') as f:
                self.qssStyle = f.read()
        except:
            logging.warning("No theme profile found...")
            self.qssStyle = None

        # LOAD Data
        # ///////////////////////////////////////////////////////////////
        self.GuiValueConfig = JsonFunction(file_path=".HawkConfig/HawkGuiConfig.json")
        self.HawkConfig = JsonFunction(file_path=".HawkConfig/HawkConfig.json")
        self.HawkROIGenConfig = JsonFunction(file_path=".HawkConfig/HawkROIGenConfig.json")
        self.HawkToolConfig = JsonFunction(file_path=".HawkConfig/HawkToolConfig.json")

        self.gui_value_config = self.GuiValueConfig.items
        self.hawk_config = self.HawkConfig.items
        self.hawk_roi_gen_config = self.HawkROIGenConfig.items
        self.hawk_tool_config = self.HawkToolConfig.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        # self.masking_win = MaskingWindow()
        self.hide_grips = True  # Show/Hide resize grips

        self.generate_logger()
        SetupMainWindow.setup_gui(self)
        HawkFunctions.setup_gui(self)
        HawkToolbox.setup_gui(self)


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

    def generate_logger(self):
        self.logger = LogerForMultithreading()
        self.timer = QTimer()
        self.timer.timeout.connect(partial(self.logger.update_log_for_qplaintextedit,
                                           self.ui.LogPrintWindow,
                                           self.settings["theme_name"]))
        self.timer.start(200)

    def closeEvent(self, event):
        self.HawkConfig.serialize()
        self.HawkToolConfig.serialize()
        MatplotExtension.fig_close()


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

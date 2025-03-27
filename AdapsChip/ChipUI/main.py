import os
import sys

import PySide6.QtCore

# sys.path.append(os.path.join(os.getcwd(), "../../"))
os.chdir(os.path.dirname(__file__))
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# from windows.main_window.main_window_setup import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes

# IMPORT HawkFunction
# ///////////////////////////////////////////////////////////////
# from SelfDefinedPackge import MatplotExtension
from windows.main_window.ui_main import UI_MainWindow
# from windows.main_window.main_window_functions import MainFunctions
from windows.main_window.main_window_setup import SetupMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QStyleFactory
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtCore import QUrl


# from PySide6.QtCore import QTimer


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        self.DEBUG = self.settings["DEBUG"]

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        if self.settings["theme_name"] == "dark":
            styleFile = r"gui/themes/page_themes/dark/darkstyle.qss"
        else:
            styleFile = r"gui/themes/page_themes/light/lightstyle.qss"
        try:
            with open(styleFile, 'r') as f:
                self.qssStyle = f.read()
        except:
            self.qssStyle = None

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # def excute():
        #     # SETUP MAIN WINDOW
        #     # ///////////////////////////////////////////////////////////////
        #     from windows.main_window.main_window_setup import SetupMainWindow
        #     SetupMainWindow.setup_gui(self)
        #     pass
        # QTimer.singleShot(100, excute)

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        from windows.main_window.main_window_setup import SetupMainWindow
        from windows.main_window.main_window_functions import MainFunctions
        btn = SetupMainWindow.setup_btns(self)

        # HOME BTN
        if btn.objectName() == "btn_hawk01":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.Hawk01)
            self.ui.log_group.setHidden(False)

        # WIDGETS BTN
        elif btn.objectName() == "btn_toolbox":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.Toolbox)
            self.ui.log_group.setHidden(False)

        # LOAD USER PAGE
        elif btn.objectName() == "btn_settings":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3
            MainFunctions.set_page(self, self.ui.load_pages.Settings)
            self.ui.log_group.setHidden(True)

        elif btn.objectName() == "btn_help":
            url = "./Doc/README.html"
            QDesktopServices.openUrl(QUrl.fromLocalFile(url))
            pass
        # print(f"Button {btn.objectName()}, clicked!")

    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        from windows.main_window.main_window_setup import SetupMainWindow
        btn = SetupMainWindow.setup_btns(self)

    def closeEvent(self, event):  # TODO: 这里退出时需要清理其他附属界面
        from windows.main_window.main_window_setup import SetupMainWindow
        from SelfDefinedPackge import MatplotExtension
        SetupMainWindow.closeEvent(self)
        MatplotExtension.fig_close()
        event.accept()


def main():
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("gui/icon.ico"))
    app.setStyle(QStyleFactory.create('windowsvista'))


    # SHOW MAIN WINDOW
    # ///////////////////////////////////////////////////////////////
    window = MainWindow()
    # window = Main
    # Window()
    window.show()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # import cProfile
    # cProfile.run("main()", sort="cumulative")
    main()

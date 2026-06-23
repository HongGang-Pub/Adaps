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
from windows.Swan01.swan01_window_setup import Swan01MainUI
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

        # DEFER HEAVY UI RENDER TO ALLOW WINDOW FRAME TO SHOW INSTANTLY
        from PySide6.QtCore import QTimer
        QTimer.singleShot(10, self.deferred_setup)

    def deferred_setup(self):
        # 1. Render the 4400-line center content UI tree
        self.ui.setup_ui_content()
        # 2. Setup left menus, signals, and chip specific GUIs
        from windows.main_window.main_window_setup import SetupMainWindow
        SetupMainWindow.setup_gui(self)

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        from windows.main_window.main_window_setup import SetupMainWindow
        from windows.main_window.main_window_functions import MainFunctions
        btn = SetupMainWindow.setup_btns(self)

        # Hawk01 BTN
        if btn.objectName() == "btn_hawk01":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.Hawk01)
            self.ui.log_group.setHidden(False)

        # Swan01 BTN
        elif btn.objectName() == "btn_swan01":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.Swan01)
            Swan01MainUI.setup_chip_gui(self, gui_type="Swan01")
            self.ui.log_group.setHidden(False)

        # Crane01 BTN
        elif btn.objectName() == "btn_crane01":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.Swan01)
            Swan01MainUI.setup_chip_gui(self, gui_type="Crane01")
            self.ui.log_group.setHidden(False)

        # Toolbox BTN
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

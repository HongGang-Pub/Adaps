import os
import sys

sys.path.append(os.path.join(os.getcwd(), "../../"))

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from windows.main_window.functions_main_window import *
from windows.main_window.setup_main_window import *


# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from AdapsChip.ChipUI.windows.main_window import *

# IMPORT HawkFunction
# ///////////////////////////////////////////////////////////////
from SelfDefinedPackge import MatplotExtension

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

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
            logging.warning("No theme profile found...")
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

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        elif btn.objectName() == "btn_app_store":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # LOAD USER PAGE
        elif btn.objectName() == "btn_settings":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        # 设置日志打印控件在设置界面隐藏
        if btn.objectName() == "btn_settings":
            self.ui.log_group.setHidden(True)
        else:
            self.ui.log_group.setHidden(False)
        # print(f"Button {btn.objectName()}, clicked!")

    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

    def closeEvent(self, event):  # TODO
        SetupMainWindow.closeEvent(self)
        MatplotExtension.fig_close()
        event.accept()


class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Open...")
        self.setFixedSize(300, 100)
        # self.setGeometry(300, 300, 300, 100)
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2 - 50
            # print(x, y)
            self.move(x, y)

        layout = QVBoxLayout()

        self.label = QLabel("Loading...")
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # QTimer.singleShot(0, self.start_loading)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(10, self.load_main_window)

    def load_main_window(self):
        # self.label.setText("Loading...")
        # self.main_window = MainWindow()
        QTimer.singleShot(100, self.open_main_window)

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


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
    window = InitialWindow()
    # window = Main
    # Window()
    window.show()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())

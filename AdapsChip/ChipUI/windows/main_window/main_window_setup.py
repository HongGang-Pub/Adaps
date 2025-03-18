# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from SelfDefinedPackge.LogerPubMethod import *
from functools import partial

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .ui_main import UI_MainWindow
from AdapsChip.ChipUI.windows.Hawk01.hawk01_window_setup import Hawk01MainUI
from AdapsChip.ChipUI.windows.HawkToolFunction.HawkToolbox import HawkToolbox
from AdapsChip.ChipUI.windows.SoftSettingFunction.SoftSettingUI import SoftMainUI


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_hawk01",
            "btn_text": "Hawk01",
            "btn_tooltip": "Hawk01",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_workbench.svg",
            "btn_id": "btn_toolbox",
            "btn_text": "Toolbox",
            "btn_tooltip": "Toolbox",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_help",
            "btn_text": "Help",
            "btn_tooltip": "Get instructions for use",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        # {
        #     "btn_icon" : "icon_search.svg",
        #     "btn_id" : "btn_search",
        #     "btn_tooltip" : "Search",
        #     "is_active" : False
        # }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.left_menu.sender() is not None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() is not None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        if not self.settings["TOOL_BOX"]:
            del SetupMainWindow.add_left_menus[1]
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        # self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        # self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        # self.ui.title_bar.clicked.connect(self.btn_clicked)
        # self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        self.ui.title_bar.set_title("We create eyes for the smart future")

        # ///////////////////////////////////////////////////////////////
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # Logger
        # ///////////////////////////////////////////////////////////////
        SetupMainWindow.generate_logger(self)

        # PAGES
        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - ADD LOGO TO MAIN PAGE
        Hawk01MainUI.setup_gui(self)

        # PAGE 2
        HawkToolbox.setup_gui(self)

        # PAGE 3
        SoftMainUI.setup_gui(self)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    # Logger Setting update automatic
    # ///////////////////////////////////////////////////////////////
    def generate_logger(self):
        """创建日志记录器"""
        # self.logger = LogerForMultithreading(themes=self.themes, font="Microsoft YaHei UI")
        #
        # # 创建定时器, 连接日志输出函数
        # self.timer = QTimer()
        # self.timer.timeout.connect(partial(self.logger.update_log_from_logger,
        #                                    self.ui.LogPrintWindow))
        # self.timer.start(200)
        # 文本超链接操作绑定
        setup_logging(self.ui.LogPrintWindow)
        self.ui.LogPrintWindow.anchorClicked.connect(open_folder)

    def closeEvent(self):
        Hawk01MainUI.closeEvent(self)
        HawkToolbox.closeEvent(self)
        SoftMainUI.closeEvent(self)

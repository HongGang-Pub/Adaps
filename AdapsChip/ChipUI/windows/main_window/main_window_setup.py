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
    app_chip_list = {
        "Hawk01": {
            "btn_icon": "Hawk01.svg",
            "btn_id": "btn_hawk01",
            "btn_text": "Hawk01",
            "btn_tooltip": "Hawk01",
            "show_top": True,
            "is_active": False
        },
        "Swan01": {
            "btn_icon": "Swan01.svg",
            "btn_id": "btn_swan01",
            "btn_text": "Swan01",
            "btn_tooltip": "Swan01",
            "show_top": True,
            "is_active": False
        },
        "Crane01": {
            "btn_icon": "Crane01.svg",
            "btn_id": "btn_crane01",
            "btn_text": "Crane01",
            "btn_tooltip": "Crane01",
            "show_top": True,
            "is_active": False
        },
        "Toolbox": {
            "btn_icon": "icon_workbench.svg",
            "btn_id": "btn_toolbox",
            "btn_text": "Toolbox",
            "btn_tooltip": "Toolbox",
            "show_top": True,
            "is_active": False
        }
    }

    add_left_menus = [
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
        # ADD MENUS, 仅显示需要开启的 chip
        chip_id = self.settings["chip_id"]
        while(chip_id):
            try:
                SetupMainWindow.add_left_menus.insert(0, SetupMainWindow.app_chip_list[chip_id.pop()])
            except:
                pass
        SetupMainWindow.add_left_menus[0]["is_active"] = True

        navigation_bar = self.settings["navigation_bar"]
        navigation_bar_len = len(navigation_bar)
        for idx in range(navigation_bar_len):
            if navigation_bar[idx] != "" and idx < len(SetupMainWindow.add_left_menus):
                SetupMainWindow.add_left_menus[idx]["btn_text"] = navigation_bar[idx]
                SetupMainWindow.add_left_menus[idx]["btn_tooltip"] = navigation_bar[idx]

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
        # Hawk01 / Swan01 / Toolbox 页面延迟加载，首次点击时初始化（减少启动时间）
        # PAGE 3 - 始终加载（无重型依赖）
        SoftMainUI.setup_gui(self)

        self.ui.left_menu.first_menus.click()

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
        self.logger = LogerForMultithreading(themes=self.themes, font="Microsoft YaHei UI")

        # 创建定时器, 连接日志输出函数
        self.timer = QTimer()
        self.timer.timeout.connect(partial(self.logger.update_log_from_logger,
                                           self.ui.LogPrintWindow))
        self.timer.start(200)
        # setup_logging(self.ui.LogPrintWindow)
        # 文本超链接操作绑定
        self.ui.LogPrintWindow.anchorClicked.connect(open_folder)

    def closeEvent(self):
        try:
            from AdapsChip.ChipUI.windows.Hawk01.hawk01_window_setup import Hawk01MainUI
            Hawk01MainUI.closeEvent(self)
        except Exception:
            pass
        try:
            from AdapsChip.ChipUI.windows.HawkToolFunction.HawkToolbox import HawkToolbox
            HawkToolbox.closeEvent(self)
        except Exception:
            pass
        SoftMainUI.closeEvent(self)
        try:
            from AdapsChip.ChipUI.windows.Swan01.swan01_window_setup import Swan01MainUI
            Swan01MainUI.closeEvent(self)
        except Exception:
            pass

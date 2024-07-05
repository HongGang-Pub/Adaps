# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.core.functions import Functions

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.widgets import *

# IMPORT SETUP MAIN WINDOW
# ///////////////////////////////////////////////////////////////
from .setup_main_window import *

# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.uis.pages.ui_main_pages import Ui_MainPages

# RIGHT COLUMN
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.uis.columns.ui_right_column import Ui_RightColumn

# CREDITS
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.widgets.py_credits_bar.py_credits import PyCredits


# PY WINDOW
# ///////////////////////////////////////////////////////////////


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        if self.settings["theme_name"] == "dark":
            styleFile = r"gui/themes/page_themes/dark/darkstyle.qss"
        else:
            styleFile = r"gui/themes/page_themes/light/lightstyle.qss"
        with open(styleFile, 'r') as f:
            qssStyle = f.read()


        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SET INITIAL PARAMETERS
        parent.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        parent.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # SET CENTRAL WIDGET
        # Add central widget to app
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(f'''
            font: {self.settings["font"]["text_size"]}pt {self.settings["font"]["family"]};
            color: {self.themes["app_color"]["text_foreground"]};
        ''')
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)

        # LOAD PY WINDOW CUSTOM WIDGET
        # Add inside PyWindow "layout" all Widgets
        # ///////////////////////////////////////////////////////////////
        window_font = f"""{self.settings["font"]["text_size"]}pt {self.settings["font"]["family"]}"""
        self.window = PyWindow(
            parent,
            bg_color=self.themes["app_color"]["bg_one"],
            border_color=self.themes["app_color"]["bg_two"],
            text_font=window_font,
            text_color=self.themes["app_color"]["text_foreground"]
        )

        # If disable custom title bar
        self.window.set_stylesheet(border_radius=0, border_size=0)

        # ADD PY WINDOW TO CENTRAL WIDGET
        self.central_widget_layout.addWidget(self.window)

        # ADD FRAME LEFT MENU
        # Add here the custom left menu bar
        # ///////////////////////////////////////////////////////////////
        left_menu_margin = self.settings["left_menu_content_margins"]
        left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setMaximumSize(left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)
        # self.left_menu_frame.resize(QSize(self.settings["lef_menu_size"]["maximum"] + (left_menu_margin * 10), 0))

        # LEFT MENU LAYOUT
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(
            left_menu_margin,
            left_menu_margin,
            left_menu_margin,
            left_menu_margin
        )

        # ADD LEFT MENU
        # Add custom left menu here
        # ///////////////////////////////////////////////////////////////
        self.left_menu = PyLeftMenu(
            parent=self.left_menu_frame,
            app_parent=self.central_widget,  # For tooltip parent
            dark_one=self.themes["app_color"]["dark_one"],
            dark_three=self.themes["app_color"]["dark_three"],
            dark_four=self.themes["app_color"]["dark_four"],
            bg_one=self.themes["app_color"]["dark_two"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            text_active=self.themes["app_color"]["text_active"],
            minimum_width=self.settings["lef_menu_size"]["minimum"],
            maximum_width=self.settings["lef_menu_size"]["maximum"],
            title_tips_size=self.settings["font"]["title_tips_size"],
            family=self.settings["font"]["family"],
            tips_minimum=self.settings["lef_menu_size"]["minimum"]
        )
        self.left_menu_layout.addWidget(self.left_menu)

        # ADD RIGHT WIDGETS
        # Add here the right widgets
        # ///////////////////////////////////////////////////////////////
        self.right_app_frame = QFrame()

        # ADD RIGHT APP LAYOUT
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(4)

        # ADD TITLE BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM TITLE BAR TO LAYOUT
        self.title_bar = PyTitleBar(
            parent,
            logo_width=100,
            app_parent=self.central_widget,
            logo_image="logo_top.svg",
            bg_color=self.themes["app_color"]["bg_two"],
            div_color=self.themes["app_color"]["bg_three"],
            btn_bg_color=self.themes["app_color"]["bg_two"],
            btn_bg_color_hover=self.themes["app_color"]["bg_three"],
            btn_bg_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            radius=8,
            font_family=self.settings["font"]["family"],
            title_size=self.settings["font"]["title_size"]
        )
        self.title_bar_layout.addWidget(self.title_bar)

        # ADD CONTENT AREA
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()
        # self.content_area_frame.setStyleSheet(f"background-color: self.themes['app_color']['bg_two']; border-radius: 0px;")

        # CREATE LAYOUT
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        # LEFT CONTENT
        self.content_main_pages = QFrame()

        # IMPORT MAIN PAGES TO CONTENT AREA
        self.load_pages = Ui_MainPages()
        self.load_pages.setupUi(self.content_main_pages)
        self.load_pages.pages.setStyleSheet(qssStyle)

        # ADD TO LAYOUTS
        self.content_area_layout.addWidget(self.content_main_pages)

        # Log Print Window
        # ///////////////////////////////////////////////////////////////
        self.log_group = QWidget()
        # self.log_group.setTitle(u"Log")
        # self.log_group.setObjectName(u"Layout3")
        self.log_group.setMinimumSize(QSize(0, 250))
        self.log_group.setMaximumSize(QSize(16777215, 250))

        self.log_group_layout = QVBoxLayout(self.log_group)
        self.log_group_layout.setContentsMargins(9, 9, 9, 9)

        # self.LogPrintWindow = QPlainTextEdit()
        self.LogPrintWindow = QTextBrowser()
        self.LogPrintWindow.setOpenLinks(False)
        # self.LogPrintWindow.setReadOnly(False)
        self.log_group_layout.addWidget(self.LogPrintWindow)
        self.log_group.setStyleSheet(qssStyle)

        # CREDITS / BOTTOM APP FRAME
        # ///////////////////////////////////////////////////////////////
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # CREATE LAYOUT
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM WIDGET CREDITS
        self.credits = PyCredits(
            bg_two=self.themes["app_color"]["bg_two"],
            copyright=self.settings["copyright"],
            version=self.settings["version"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            text_description_color=self.themes["app_color"]["text_description"]
        )

        #  ADD TO LAYOUT
        self.credits_layout.addWidget(self.credits)

        # ADD WIDGETS TO RIGHT LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(self.log_group)
        self.right_app_layout.addWidget(self.credits_frame)

        # ADD WIDGETS TO "PyWindow"
        # Add here your custom widgets or default widgets
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.left_menu_frame)
        # self.window.layout.addWidget(self.left_column_frame)
        self.window.layout.addWidget(self.right_app_frame)

        # ADD CENTRAL WIDGET AND SET CONTENT MARGINS
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)

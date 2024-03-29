import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidget
from Hawk.HawkGUI_v002.gui.uis.pages.ui_ROI_OthersConfig import Ui_Dialog
from PySide6.QtWidgets import *
from Hawk.HawkGUI_v002.gui.widgets.py_table_widget import PyTableWidget
from PySide6.QtCore import *
from Hawk.HawkGUI_v002.gui.widgets import *

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # 这是类函数的名称
        self.ui.setupUi(self)  # 运行类函数里的setupUi
        self.styleFile = styleFile
        with open(self.styleFile, 'r') as f:
            qssStyle = f.read()
        self.setStyleSheet(qssStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = r"../gui/themes/page_themes/light/lightstyle.qss"
    win = MainWindow()

    win.show()  # 显示窗口
    sys.exit(app.exec())
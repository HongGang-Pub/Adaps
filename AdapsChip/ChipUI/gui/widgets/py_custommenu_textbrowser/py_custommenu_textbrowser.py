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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *


class CustomMenuTextBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event):
        # 获取默认右键菜单
        menu = self.createStandardContextMenu()

        # 添加新的自定义选项
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear)
        menu.addAction(clear_action)  # 将新选项添加到菜单中

        # 显示菜单
        menu.exec(event.globalPos())

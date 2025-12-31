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

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *
import os


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化设置
        # self.setReadOnly(True)  # 设为只读
        # self.setCursor(Qt.PointingHandCursor)  # 鼠标悬停变小手
        # self.setToolTip("双击以打开此文件")
        self.setContextMenuPolicy(Qt.DefaultContextMenu)  # 确保启用默认菜单事件

    # def mouseDoubleClickEvent(self, event):
    #     """重写双击事件"""
    #     if event.button() == Qt.LeftButton:
    #         self.open_file_logic()

    def contextMenuEvent(self, event):
        """每次点击右键时都会执行此函数"""
        # 1. 获取当前路径并判断文件是否存在
        current_path = self.text().strip()
        abs_path = os.path.abspath(current_path)
        # 只有路径不为空且文件确实存在时，才标记为可打开
        file_exists = current_path != "" and os.path.exists(abs_path)
        """重写右键菜单事件"""
        # 1. 获取默认右键菜单
        menu = self.createStandardContextMenu()

        # 2. 添加自定义动作
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file_logic)

        # 3. 动态添加“打开文件”菜单项
        menu.addSeparator()  # 分割线

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file_logic)
        open_action.setEnabled(file_exists)
        menu.addAction(open_action)

        # 可选：如果文件存在，增加一个“打开所在文件夹”的选项也很实用
        open_folder_action = QAction("Reveal in File Explorer", self)
        open_folder_action.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl.fromLocalFile(os.path.dirname(abs_path))
        ))
        open_folder_action.setEnabled(file_exists)
        menu.addAction(open_folder_action)

        # if file_exists:
        #     menu.addSeparator()  # 分割线
        #
        #     open_action = QAction("Open", self)
        #     open_action.triggered.connect(self.open_file_logic)
        #     menu.addAction(open_action)
        #
        #     # 可选：如果文件存在，增加一个“打开所在文件夹”的选项也很实用
        #     open_folder_action = QAction("Reveal in File Explorer", self)
        #     open_folder_action.triggered.connect(lambda: QDesktopServices.openUrl(
        #         QUrl.fromLocalFile(os.path.dirname(abs_path))
        #     ))
        #     menu.addAction(open_folder_action)
        #
        # else:
        #     # 如果文件不存在，可以不添加“打开”菜单，或者添加一个置灰的提示
        #     # 如果你希望完全不显示，就什么都不写
        #     # 也可以加一个置灰提示：
        #     # none_action = QAction("❌ 文件路径无效", self)
        #     # none_action.setEnabled(False)
        #     # menu.addAction(none_action)
        #     # menu.addSeparator()
        #     pass

        # 4. 在鼠标点击的位置弹出菜单
        menu.exec(event.globalPos())

    def open_file_logic(self):
        """通用的打开文件逻辑"""
        file_path = self.text().strip()
        if not file_path:
            return

        abs_path = os.path.abspath(file_path)
        if os.path.exists(abs_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(abs_path))
        else:
            QMessageBox.warning(self, "Error", f"The file cannot be found:\n{abs_path}")

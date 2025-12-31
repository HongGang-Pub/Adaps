import os
from PySide6.QtWidgets import QLineEdit, QMenu, QMessageBox
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QAction


class FileOpenLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setCursor(Qt.PointingHandCursor)

    def open_file_logic(self):
        """打开文件的核心逻辑"""
        path = self.text().strip()
        if path:
            abs_path = os.path.abspath(path)
            QDesktopServices.openUrl(QUrl.fromLocalFile(abs_path))

    def contextMenuEvent(self, event):
        """每次点击右键时都会执行此函数"""
        # 1. 获取当前路径并判断文件是否存在
        current_path = self.text().strip()
        abs_path = os.path.abspath(current_path)
        # 只有路径不为空且文件确实存在时，才标记为可打开
        file_exists = current_path != "" and os.path.exists(abs_path)

        # 2. 创建菜单
        menu = QMenu(self)

        # 3. 动态添加“打开文件”菜单项
        if file_exists:
            open_action = QAction("📂 打开文件 (Open)", self)
            open_action.triggered.connect(self.open_file_logic)
            menu.addAction(open_action)

            # 可选：如果文件存在，增加一个“打开所在文件夹”的选项也很实用
            open_folder_action = QAction("📁 打开所在文件夹", self)
            open_folder_action.triggered.connect(lambda: QDesktopServices.openUrl(
                QUrl.fromLocalFile(os.path.dirname(abs_path))
            ))
            menu.addAction(open_folder_action)

            menu.addSeparator()  # 分割线
        else:
            # 如果文件不存在，可以不添加“打开”菜单，或者添加一个置灰的提示
            # 如果你希望完全不显示，就什么都不写
            # 也可以加一个置灰提示：
            none_action = QAction("❌ 文件路径无效", self)
            none_action.setEnabled(False)
            menu.addAction(none_action)
            menu.addSeparator()

        # 4. 无论如何都显示的通用功能（如复制路径）
        copy_action = QAction("📋 复制路径 (Copy Path)", self)
        copy_action.triggered.connect(lambda: self.copy())
        menu.addAction(copy_action)

        # 5. 在鼠标位置弹出菜单
        menu.exec(event.globalPos())
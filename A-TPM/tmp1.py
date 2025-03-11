from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QCheckBox, QVBoxLayout, QWidget, QListView
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个 ComboBox
        self.combo_box = QComboBox(self)

        # 创建自定义的 QListView
        self.combo_box.setView(QListView())

        # 创建多选的 QCheckBox 项
        self.combo_box.addItem("选项1")
        self.combo_box.addItem("选项2")
        self.combo_box.addItem("选项3")

        # 创建一个布局
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)

        # 创建一个 QWidget 并设置为窗口的中央部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 设置窗口标题
        self.setWindowTitle("下拉多选示例")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

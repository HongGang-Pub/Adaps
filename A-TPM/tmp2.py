import sys
import gc
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from memory_profiler import profile

class LauncherWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 创建一个按钮，用于打开绘图窗口
        self.open_plot_button = QPushButton("打开绘图窗口")
        self.open_plot_button.clicked.connect(self.open_plot_window)

        layout = QVBoxLayout()
        layout.addWidget(self.open_plot_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.plot_window = None  # 初始化绘图窗口为None

        self.setWindowTitle("启动器窗口")
        self.show()

    @profile
    def open_plot_window(self):
        if self.plot_window is None:
            # 导入包含绘图逻辑的 MainWindow 类
            from tmp1 import MainWindow
            # 创建 MainWindow 的实例
            self.plot_window = MainWindow()
            self.plot_window.setAttribute(Qt.WA_DeleteOnClose)  # 确保关闭时删除对象
            self.plot_window.show()
            # 连接关闭事件以清除引用
            self.plot_window.destroyed.connect(self.on_plot_window_closed)

    @profile
    def on_plot_window_closed(self):
        print(1111)
        self.plot_window = None  # 清除引用，以便垃圾回收
        gc.collect()  # 强制垃圾回收

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = LauncherWindow()
    app.exec_()

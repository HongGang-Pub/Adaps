from PySide6.QtWidgets import QWidget
from PySide6 import QtCore
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)  # 用户界面后端渲染，用来以绘图的形式输出
from PySide6.QtWidgets import QVBoxLayout, QApplication
from PySide6 import QtWidgets
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure  # 图表类
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
from Hawk.HawkGUI_v002.HawkFunction import Player


class MaskingCanvas(FigureCanvas):
    """
    创建一个画板类，并把画布放到容器（画板上）FigureCanvasQTAgg，再创建一个画图区
    """

    def __init__(self):
        # 创建一个Figure,该Figure为matplotlib下的Figure，不是matplotlib.pyplot下面的Figure
        self.figs = plt.figure()
        super(MaskingCanvas, self).__init__(self.figs)
        # self.figs.patch.set_facecolor('#01386a')  # 设置绘图区域颜色
        self.axes = self.figs.add_subplot(111)

        # Masking Data
        # ///////////////////////////////////////////////////////////////
        self.arrays = []
        self.info = []

        for i in range(5):
            # arr = np.zeros((576, 768))
            arr = np.random.rand(576, 768)
            self.arrays.append(arr)
        self.plot_tick()

    def initial(self):
        """
        初始化设置函数
        """
        self.axes.cla()
        # --------------------- 配置刻度 --------------------
        self.axes.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        self.axes.xaxis.set_major_locator(MultipleLocator(48))
        self.axes.yaxis.set_major_locator(MultipleLocator(50))

        # self.axes.patch.set_facecolor("#01386a")  # 设置ax区域背景颜色
        # self.axes.patch.set_alpha(0.5)  # 设置ax区域背景颜色透明度
        #
        # # self.axes.spines['top'].set_color('#01386a')
        # self.axes.spines['top'].set_visible(False)  # 顶边界不可见
        # self.axes.spines['right'].set_visible(False)  # 右边界不可见
        #
        # self.axes.xaxis.set_ticks_position('bottom')  # 设置ticks（刻度）的位置为下方
        # self.axes.yaxis.set_ticks_position('left')  # 设置ticks（刻度） 的位置为左侧
        # # 设置左、下边界在（0，0）处相交
        # # self.axes.spines['bottom'].set_position(('data', 0))  # 设置x轴线再Y轴0位置
        # self.axes.spines['left'].set_position(('data', 0))  # 设置y轴在x轴0位置
        # self.plot_line, = self.axes.plot([], [], 'r-', linewidth=1)  # 注意‘,’不可省略

    def plot_tick(self):
        def update(i):
            """ 动态图片更新函数 """
            print(i)

            subframe_index = i % len(self.arrays)

            # print(i, frame_cnt, subframe_index)

            self.axes.cla()
            # --------------------- 配置刻度 --------------------
            self.axes.xaxis.tick_top()  # 设置x坐标轴位置在顶部
            self.axes.xaxis.set_major_locator(MultipleLocator(48))
            self.axes.yaxis.set_major_locator(MultipleLocator(50))

            imgs = self.axes.imshow(X=self.arrays[subframe_index])

            if not (subframe_index < len(self.info)):
                return [imgs]

            # ------------- title config -------------------
            x, y, s = self.info[subframe_index]
            _str = f"{s}({x}, {y})"
            x = x + 5 if x < 610 else 610
            y = y - 12 if y > 30 else y + 37
            y = y if y < 565 else 565
            title = self.axes.text(x, y, _str, fontdict={
                'family': 'Times New Roman',  # 标注文本字体
                'fontsize': 10,  # 文本大小
                'fontweight': 'bold',  # 字体粗细
                # 'fontstyle': 'italic',  # 字体风格
                'color': 'white',  # 文本颜色
                'backgroundcolor': 'blue',  # 背景颜色
                'bbox': {
                    'boxstyle': 'round',  # 椭圆外框
                    'edgecolor': 'white',  # 线框颜色
                    'linewidth': 0
                }
            })
            return [imgs] + [title]

        # ani = FuncAnimation(self.figs, update, blit=True, repeat=False)
        self.ani = Player.Player(self.figs, update, interval=700, blit=True, cache_frame_data=False, save_count=2, maxi=10000)

        self.figs.canvas.draw()


class MainDialogImgBW(QtWidgets.QWidget):
    def __init__(self):
        super(MainDialogImgBW, self).__init__()
        self.setWindowTitle("显示matplotlib")
        self.setObjectName("widget")
        self.resize(800, 600)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.canvas = MaskingCanvas()
        # self.plotcos()
        self.hboxlayout = QtWidgets.QVBoxLayout(self)
        self.hboxlayout.addWidget(self.canvas)

        self.btn_start = QtWidgets.QPushButton("start")
        self.btn_pause = QtWidgets.QPushButton("pause")
        self.btn_back = QtWidgets.QPushButton("back")
        self.btn_forward = QtWidgets.QPushButton("forward")
        self.bnt_initial = QtWidgets.QPushButton("initial")

        self.btn_start.clicked.connect(self.canvas.ani.start)
        self.btn_pause.clicked.connect(self.canvas.ani.stop)
        self.btn_back.clicked.connect(self.canvas.ani.onebackward)
        self.btn_forward.clicked.connect(self.canvas.ani.oneforward)
        self.bnt_initial.clicked.connect(self.canvas.ani.reset)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(self.btn_start)
        hlayout.addWidget(self.btn_pause)
        hlayout.addWidget(self.btn_back)
        hlayout.addWidget(self.btn_forward)
        hlayout.addWidget(self.bnt_initial)
        self.hboxlayout.addLayout(hlayout)

    def plotcos(self):
        self.canvas.initial()
        self.canvas.plot_tick()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    # main.canvas.ani.stop()
    sys.exit(app.exec())

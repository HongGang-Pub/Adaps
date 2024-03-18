"""GUI 界面增加画布"""
import sys

from PySide6.QtGui import QIcon
import numpy as np

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from Hawk.HawkGUI_v002.HawkFunction import Player
from matplotlib.ticker import MultipleLocator
from Hawk.HawkGUI_v002.gui.qt_core import *
from Hawk.HawkGUI_v002.gui.core.functions import Functions
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout
from matplotlib.animation import FuncAnimation
from PySide6.QtCore import QTimer, Slot, QThread


class Myplot(FigureCanvas):
    def __init__(self, parent=None, width=10, height=6, dpi=120):
        # normalized for 中文显示和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.subplots_adjust(top=0.95, bottom=0, left=0.05, right=1, hspace=1, wspace=1)
        # new figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # self.fig = Figure()
        self.fig.set_facecolor('#f5f5f5')

        # activate figure window
        # super(Plot_dynamic,self).__init__(self.fig)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # self.fig.canvas.mpl_connect('button_press_event', self)
        # subplot by self.axes
        self.axes = self.fig.add_subplot(111)
        # initial figure
        self.compute_initial_figure()

        # size policy
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


# class for plotting a specific figure static or dynamic
class DynamicFig(Myplot):
    def __init__(self, *args, **kwargs):
        Myplot.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        arr = np.zeros((576, 768))
        # --------------------- 配置刻度 --------------------
        self.axes.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        self.axes.xaxis.set_major_locator(MultipleLocator(48))
        self.axes.yaxis.set_major_locator(MultipleLocator(50))
        self.axes.imshow(arr)


class MaskingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("matplotlib embeded in Python Qt with figure toolbar")

        # Masking Data
        # ///////////////////////////////////////////////////////////////
        self.arrays = []
        self.info = []
        self.is_playing = False
        self.index = -1
        self._timer = QTimer(self)

        for i in range(5):
            # arr = np.zeros((576, 768))
            arr = np.random.rand(576, 768)
            self.arrays.append(arr)

        self.initUI()
        self.Operate_bar()

    def initUI(self):
        self.canvas = DynamicFig()
        self.canvas.figure.set_facecolor('#f5f5f5')

        # Control bar
        self.control_bar_frame = QFrame()   # 动图操作控制添加到窗口布局中
        self.control_bar_hlayout = QHBoxLayout(self.control_bar_frame)

        # Toolbar
        # self.figtoolbar = NavigationToolbar(self.canvas, self)  # 创建figure工具栏

        # Display
        self.win_vlayout = QVBoxLayout(self)
        self.win_vlayout.addWidget(self.canvas, 15)  # 画布添加到窗口布局中
        self.win_vlayout.addWidget(self.control_bar_frame, 1)
        # self.win_vlayout.addWidget(self.figtoolbar)  # 工具栏添加到窗口布局中

    def update_fig(self):
        if self.is_playing:
            self.index += 1
        self.canvas.axes.cla()
        # --------------------- 配置刻度 --------------------
        self.canvas.axes.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        self.canvas.axes.xaxis.set_major_locator(MultipleLocator(48))
        self.canvas.axes.yaxis.set_major_locator(MultipleLocator(50))

        print(self.index)
        self.canvas.axes.imshow(self.arrays[self.index % 5])
        self.canvas.draw()


    def Play_plot(self):
        print('Play_plot')
        self._timer.timeout.connect(self.update_fig)
        self._timer.start(700)  # plot after 1s delay

    def Pause_plot(self):
        print('Pause_plot')
        self._timer.timeout.disconnect(self.update_fig)

    def Oneforward_plot(self):
        # print('Oneforward_plot')
        self.index += 1
        self.update_fig()

    def Oneback_plot(self):
        # print('Oneback_plot')
        self.index = self.index-1 if self.index > 0 else 0
        self.update_fig()

    def Replay_plog(self):
        # print('Replay_plog')
        self.index = -1

    def PlaySwitch_plot(self):
        if self.is_playing:
            self.is_playing = False
            self.Pause_plot()
            # self.pushButton.setText('暂停')
            print("stop")
            icon = QIcon(Functions.set_svg_icon("icon_play.svg"))
            self.btn_playControl.setIcon(icon)
        elif not self.is_playing:
            self.is_playing = True
            self.Play_plot()
            # self.pushButton.setText('运行')
            print("play")
            icon = QIcon(Functions.set_svg_icon("icon_stop.svg"))
            self.btn_playControl.setIcon(icon)

    def Operate_bar(self):
        self.control_bar_frame.setStyleSheet(
            """
            QPushButton {
              background-color: #e9e9e9;
              color: #19232D;
              width: 40px;
              height: 40px;
              border-radius: 20px;
              padding: 0px;
              outline: none;
              border: none;
              qproperty-iconSize:40px;
            }""")

        # Play Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_playControl = QPushButton()
        icon_play = QIcon(Functions.set_svg_icon("icon_play.svg"))
        self.btn_playControl.setIcon(icon_play)
        # Back Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_oneback = QPushButton()
        icon_oneback = QIcon(Functions.set_svg_icon("icon_oneback.svg"))
        self.btn_oneback.setIcon(icon_oneback)

        # Forward Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_oneforward = QPushButton()
        icon_oneforward = QIcon(Functions.set_svg_icon("icon_oneforward.svg"))
        self.btn_oneforward.setIcon(icon_oneforward)

        # Replay Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_replay = QPushButton()
        icon_replay = QIcon(Functions.set_svg_icon("icon_replay.svg"))
        self.btn_replay.setIcon(icon_replay)

        # self.bnt_initial.setFixedSize(100, 100)
        # self.bnt_initial.setIconSize(QtCore.QSize(80, 80))

        # Button connect
        # ////////////////////////////////////////////////////////////////////////
        self.btn_oneback.clicked.connect(self.Oneback_plot)
        self.btn_playControl.clicked.connect(self.PlaySwitch_plot)
        self.btn_oneforward.clicked.connect(self.Oneforward_plot)
        self.btn_replay.clicked.connect(self.Replay_plog)

        # self.btn_test = QPushButton("test")
        # self.btn_test.clicked.connect(self.ani.stop)

        self.control_bar_hlayout.addWidget(self.btn_oneback)
        self.control_bar_hlayout.addWidget(self.btn_playControl)
        self.control_bar_hlayout.addWidget(self.btn_oneforward)
        self.control_bar_hlayout.addWidget(self.btn_replay)
        # self.control_bar_hlayout.addWidget(self.btn_test)
        return

    # def resizeEvent(self, event):
    #     self.is_playing = True
    #     icon_play = QIcon(Functions.set_svg_icon("icon_stop.svg"))
    #     self.btn_playControl.setIcon(icon_play)
    #     self.ani.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MaskingWindow()
    win.show()
    sys.exit(app.exec())

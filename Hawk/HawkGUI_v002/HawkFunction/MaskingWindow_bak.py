"""GUI 界面增加画布"""
import sys

from PySide6.QtGui import QIcon
import numpy as np

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from Hawk.HawkGUI_v002.HawkFunction import Player
from matplotlib.ticker import MultipleLocator
from Hawk.HawkGUI_v002.gui.qt_core import *
from Hawk.HawkGUI_v002.gui.core.functions import Functions
from matplotlib.animation import FuncAnimation


class MaskingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("matplotlib embeded in Python Qt with figure toolbar")

        # Masking Data
        # ///////////////////////////////////////////////////////////////
        self.arrays = []
        self.info = []
        self.is_pause = True

        for i in range(5):
            # arr = np.zeros((576, 768))
            arr = np.random.rand(576, 768)
            self.arrays.append(arr)

        self.initUI()
        self.plotfig()
        # self.Operate_bar()

    def initUI(self):
        # Initial Window and setting
        plt.subplots_adjust(top=0.95, bottom=0, left=0.05, right=1, hspace=1, wspace=1)
        self.figs = plt.figure()  # 创建figure对象
        self.figs.set_facecolor('#f5f5f5')
        self.axes = self.figs.subplots()
        # plt.margins(0, 0)

        # Masking show
        self.canvas = FigureCanvasQTAgg(self.figs)  # 创建figure画布

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

    def plotfig(self):
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

        # ani = FuncAnimation(self.figs, update, blit=True, repeat=False, cache_frame_data=False)
        self.ani = Player.Player(self.figs, update, interval=700, blit=True, cache_frame_data=False,
                                 save_count=2, maxi=10000)
        # plt.imshow(self.arrays[0])
        # plt.show()
        self.figs.canvas.draw()

    def playSwitch(self):
        if self.is_pause:
            self.is_pause = False
            self.ani.stop()
            # self.pushButton.setText('暂停')
            print("stop")
            icon = QIcon(Functions.set_svg_icon("icon_play.svg"))
            self.btn_playControl.setIcon(icon)
        elif (not self.is_pause):
            self.is_pause = True
            self.ani.start()
            # self.pushButton.setText('运行')
            print("play")
            icon = QIcon(Functions.set_svg_icon("icon_stop.svg"))
            self.btn_playControl.setIcon(icon)

    def ani_control(self):
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
        icon_play = QIcon(Functions.set_svg_icon("icon_stop.svg"))
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

        self.btn_oneback.clicked.connect(self.ani.onebackward)
        self.btn_playControl.clicked.connect(self.playSwitch)
        self.btn_oneforward.clicked.connect(self.ani.oneforward)
        self.btn_replay.clicked.connect(self.ani.reset)

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

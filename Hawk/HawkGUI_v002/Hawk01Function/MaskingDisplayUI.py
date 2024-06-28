"""GUI 界面增加画布"""
import logging
import sys
from threading import Thread

from PySide6.QtGui import QIcon, QCursor
import numpy as np

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame
# from PySide6.QtGui import QIcon, QScreen, QAction
import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from Hawk.HawkGUI_v002.gui.qt_core import *
from Hawk.HawkGUI_v002.gui.core.functions import Functions
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QApplication
from PySide6.QtCore import QTimer
from Hawk.HawkGUI_v002.gui.Signal import MySignals
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from Hawk.HawkGUI_v002.Hawk01Function import Hawk01Function


class CustomToolbar(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None):
        super(CustomToolbar, self).__init__(canvas, parent)

        # Set custom icons
        # self._update_icons()

        # Add custom action
        # self._add_custom_action()

    def _update_icons(self):
        icon_mapping = {
            'Home': 'path/to/your/custom/home.png',
            'Back': 'path/to/your/custom/back.png',
            'Forward': 'path/to/your/custom/forward.png',
            'Pan': 'path/to/your/custom/pan.png',
            'Zoom': 'path/to/your/custom/zoom.png',
            'Save': 'path/to/your/custom/save.png'
        }

        for action in self.actions():
            if action.text() in icon_mapping:
                action.setIcon(QIcon(icon_mapping[action.text()]))

    def _add_custom_action(self):
        # Create a custom action with an icon
        custom_action = QAction(QIcon('path/to/your/custom/icon.png'), 'Custom Action', self)
        custom_action.triggered.connect(self.custom_function)
        self.addAction(custom_action)

    def custom_function(self):
        # print("Custom action triggered!")
        return


class DynamicFig(FigureCanvas):
    def __init__(self, parent=None, ini_img=None):
        # normalized for 中文显示和负号
        # plt.subplots_adjust(top=0.95, bottom=0, left=0.05, right=1, hspace=0, wspace=0)
        # plt.subplots_adjust(top=1.00, bottom=0, left=0.00, right=1, hspace=0, wspace=0)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.fig = Figure()
        self.fig.set_facecolor('#f5f5f5')
        self.ini_img = ini_img

        # activate figure window
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
        # FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        # --------------------- 配置刻度 --------------------
        self.axes.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        self.axes.xaxis.set_major_locator(MultipleLocator(48))
        self.axes.yaxis.set_major_locator(MultipleLocator(50))
        # ------------------ 给定初始图片 --------------------
        self.fig.tight_layout()
        try:
            self.axes.imshow(self.ini_img)
        except:
            pass
        return


class MaskingWindow(QMainWindow):
    def __init__(self, title="ROI SHOW", ID=0, roi_data_pkg=None, hawk_config=None):
        super().__init__()
        matplotlib.use('agg')
        self.setWindowTitle(title)
        self.ID = ID
        self.roi_data_pkg = roi_data_pkg
        self.hawk_config = hawk_config

        try:
            self.arrays = self.roi_data_pkg["arrays"]
            if self.roi_data_pkg["roi_gen_type"] == 3:
                self.arrays.append(self.roi_data_pkg["fusion_image"])
                self.arrays.append(self.roi_data_pkg["spad_array_3D"])
        except:
            self.arrays = []
            for i in range(5):
                # arr = np.zeros((576, 768))
                arr = np.random.rand(576, 768, 3)
                self.arrays.append(arr)

        # Sync Signal
        # ///////////////////////////////////////////////////////////////
        self.win_signal_sync = MySignals()
        self.win_signal_sync.text_signal_1.connect(self.bnt_save_release)

        # Masking Data
        # ///////////////////////////////////////////////////////////////
        self.is_playing = False
        self.index = 0
        self._timer = QTimer(self)



        self.initUI()
        self.Operate_bar()
        self.PlaySwitch_plot()

    def initUI(self):
        # 设置界面位置,确保多张图叠加显示位置不同
        # self.setGeometry(100, 100, 658, 602)
        self.setFixedSize(658, 602)
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2 + 20 * (self.ID % 10)
            y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2 + 20 * (self.ID % 10)
            # print(x, y)
            self.move(x, y)

        # 添加界面内容
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.win_vlayout = QVBoxLayout(self.central_widget)

        # Canvas
        self.canvas = DynamicFig(ini_img=self.arrays[0])

        # Control bar
        self.control_bar_frame = QFrame()  # 动图操作控制添加到窗口布局中
        self.control_bar_hlayout = QHBoxLayout(self.control_bar_frame)

        # Toolbar
        # self.figtoolbar = NavigationToolbar(self.canvas, self)  # 创建figure工具栏
        self.toolbar = CustomToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("")
        # self.addToolBar(self.toolbar)

        # Display
        self.win_vlayout.addWidget(self.toolbar, 1)  # 画布添加到窗口布局中
        self.win_vlayout.addWidget(self.canvas, 15)  # 画布添加到窗口布局中
        self.win_vlayout.addWidget(self.control_bar_frame, 1)
        # self.win_vlayout.addWidget(self.figtoolbar)  # 工具栏添加到窗口布局中

    def update_fig(self):
        self.canvas.axes.cla()
        # --------------------- 配置刻度 --------------------
        # self.canvas.fig.tight_layout()
        # self.canvas.axes.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        self.canvas.axes.xaxis.set_major_locator(MultipleLocator(48))
        self.canvas.axes.yaxis.set_major_locator(MultipleLocator(50))

        # print(self.index % len(self.arrays))
        self.canvas.axes.imshow(self.arrays[self.index % len(self.arrays)])
        self.canvas.draw()

    def dynamic_fig(self):
        if self.is_playing:
            self.index += 1
        self.update_fig()

    def Play_plot(self):
        # print('Play_plot')
        self._timer.timeout.connect(self.dynamic_fig)
        self._timer.start(700)  # plot after 1s delay

    def Pause_plot(self):
        # print('Pause_plot')
        self._timer.timeout.disconnect(self.update_fig)

    def Oneforward_plot(self):
        # print('Oneforward_plot')
        self.index += 1
        self.update_fig()

    def Oneback_plot(self):
        # print('Oneback_plot')
        self.index = self.index - 1 if self.index > 0 else 0
        self.update_fig()

    def Replay_plog(self):
        # print('Replay_plog')
        self.index = 0
        self.update_fig()

    def roi_data_save(self):
        logging.info("标定数据保存中....")
        self.btn_save.setEnabled(False)
        def threadFunc():
            try:
                Hawk01Function.ROIDataPackageSave(self.roi_data_pkg, self.hawk_config, save_sel=1)
                self.win_signal_sync.text_signal_1.emit("数据保存完成...")
            except Exception as e:
                self.win_signal_sync.text_signal_1.emit(e)
        thread = Thread(target=threadFunc)
        thread.start()
        return

    def bnt_save_release(self, info):
        logging.info(info)
        self.btn_save.setEnabled(True)
        return

    def PlaySwitch_plot(self):
        if self.is_playing:
            self.is_playing = False
            self.Pause_plot()
            # self.pushButton.setText('暂停')
            # print("stop")
            icon = QIcon(Functions.set_svg_icon("icon_play.svg"))
            self.btn_playControl.setIcon(icon)
        elif not self.is_playing:
            self.is_playing = True
            self.Play_plot()
            # self.pushButton.setText('运行')
            # print("play")
            icon = QIcon(Functions.set_svg_icon("icon_stop.svg"))
            self.btn_playControl.setIcon(icon)

    def closeEvent(self, event):
        # self._timer.stop()
        # self.arrays = []  # 清理内存
        self.win_signal_sync.int_signal_1.emit(self.ID) # 同步到主界面, 进行内存释放
        event.accept()

    def Operate_bar(self):
        self.control_bar_frame.setStyleSheet(
            """
            QPushButton {
              width: 40px;
              height: 40px;
              border-radius: 20px;
              padding: 0px;
              qproperty-iconSize:40px;
            }
            """)

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

        # Save Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_save = QPushButton()
        # icon_save = QIcon(Functions.set_svg_icon("icon_save.svg", folder="../gui/images/svg_icons/"))
        icon_save = QIcon(Functions.set_svg_icon("icon_save.svg"))
        self.btn_save.setIcon(icon_save)
        # self.bnt_initial.setFixedSize(100, 100)
        # self.bnt_initial.setIconSize(QtCore.QSize(80, 80))

        # Button connect
        # ////////////////////////////////////////////////////////////////////////
        self.btn_oneback.clicked.connect(self.Oneback_plot)
        self.btn_playControl.clicked.connect(self.PlaySwitch_plot)
        self.btn_oneforward.clicked.connect(self.Oneforward_plot)
        self.btn_replay.clicked.connect(self.Replay_plog)
        self.btn_save.clicked.connect(self.roi_data_save)

        # self.btn_test = QPushButton("test")
        # self.btn_test.clicked.connect(self.ani.stop)

        self.control_bar_hlayout.addWidget(self.btn_oneback)
        self.control_bar_hlayout.addWidget(self.btn_playControl)
        self.control_bar_hlayout.addWidget(self.btn_oneforward)
        self.control_bar_hlayout.addWidget(self.btn_replay)
        self.control_bar_hlayout.addWidget(self.btn_save)
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

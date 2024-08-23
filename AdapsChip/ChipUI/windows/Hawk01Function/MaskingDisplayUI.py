"""GUI 界面增加画布"""
import gc
import logging
import sys
from threading import Thread

import numpy as np

from PySide6.QtWidgets import QFrame
# from PySide6.QtGui import QIcon, QScreen, QAction
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator, MaxNLocator
from AdapsChip.ChipUI.gui.core.functions import Functions
from PySide6 import QtWidgets
from AdapsChip.ChipUI.gui.Signal import MySignals
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from AdapsChip.ChipUI.windows.Hawk01Function import Hawk01Function

from memory_profiler import profile


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
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # normalized for 中文显示和负号
        # plt.subplots_adjust(top=0.95, bottom=0, left=0.05, right=1, hspace=0, wspace=0)
        # plt.subplots_adjust(top=1.00, bottom=0, left=0.00, right=1, hspace=0, wspace=0)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_facecolor('#f5f5f5')
        super(DynamicFig, self).__init__(self.fig)
        # self.fig.tight_layout()

        self.axes = self.fig.add_subplot(111)
        self.axes.xaxis.tick_top()

        self.image = None  # Store reference to the image object
        self.title = None
        self.xlabel = None
        self.ylabel = None
        self.texts = []

        # size policy
        # FigureCanvas.setSizePolicy(self,
        #                            QtWidgets.QSizePolicy.Expanding,
        #                            QtWidgets.QSizePolicy.Expanding)

    def plot_image(self, data, x_ticks_interval=None, y_ticks_interval=None, xlim=None, ylim=None, title=None, xlabel=None, ylabel=None,
                   text_annotations=None):
        if self.image is None:
            # First time plotting, create the image
            self.image = self.axes.imshow(data, cmap='viridis')
            # self.fig.tight_layout()
        else:
            # Update the existing image data
            self.image.set_data(data)
            self.image.set_extent([0, data.shape[1], data.shape[0], 0])

        # Adjust the aspect ratio and limits based on the image size
        self.axes.set_aspect('auto')  # Set the aspect ratio to auto to accommodate different image sizes
        self.axes.relim()  # Recompute the limits based on the new data
        self.axes.autoscale_view()  # Automatically scale the view to fit the new limits

        # Set the x-axis tick interval
        self.axes.xaxis.set_major_locator(MultipleLocator(x_ticks_interval))
        self.axes.yaxis.set_major_locator(MultipleLocator(y_ticks_interval))

        if xlim is not None:
            self.axes.set_xlim(xlim)
        if ylim is not None:
            self.axes.set_ylim(ylim)

        # Update the title
        if title is not None:
            self.axes.set_title(title)

        # Update axis labels
        if xlabel is not None:
            self.axes.set_xlabel(xlabel)
        if ylabel is not None:
            self.axes.set_ylabel(ylabel)

        # Clear previous text_annotations annotations
        for text in self.texts:
            text.remove()
        self.texts.clear()
        # Update or add text_annotations
        if text_annotations is not None:
            for text_annotation in text_annotations:
                text_obj = self.axes.text(
                    text_annotation['x'],
                    text_annotation['y'],
                    text_annotation['text_annotations'],
                    fontdict={
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
                    }
                )
                self.texts.append(text_obj)
        # self.fig.tight_layout()
        self.draw()  # Redraw the canvas

    def clear_image(self):
        self.axes.clear()  # Clear the axes
        # self.image = None  # Reset the image reference
        self.draw()  # Redraw the canvas


class MaskingWindow(QMainWindow):
    def __init__(self, title="ROI SHOW", roi_data_pkg=None, hawk_config=None, soft_config=None):
        super().__init__()
        self.setWindowTitle(title)
        self.DEBUG = False
        self.roi_data_pkg = roi_data_pkg
        self.hawk_config = hawk_config
        self.soft_config = soft_config
        if self.roi_data_pkg is not None:
            self.icon_fd = "gui/images/svg_icons/"
            # self.arrays = self.roi_data_pkg["arrays"]
            self.img_type = ["Masking", "PCM Image", "PTM Image", "Cali fusion Image"] \
                if self.roi_data_pkg["roi_gen_type"] == 3 \
                else ["Masking", "PCM Image", "PTM Image"]
        else:
            self.DEBUG = True
            self.icon_fd = "../../gui/images/svg_icons/"
            arrays = []
            self.img_type = ["Masking"]
            for i in range(10):
                arr = np.random.rand(576, 768)
                arrays.append(arr)
                self.roi_data_pkg = {}
                self.roi_data_pkg["arrays"] = arrays

        # Sync Signal
        # ///////////////////////////////////////////////////////////////
        self.win_signal_sync = MySignals()

        # Masking Data
        # ///////////////////////////////////////////////////////////////
        self.is_playing = False
        self.index = 0
        self._timer = QTimer(self)

        self.initUI()
        self.Operate_bar()
        self.PlaySwitch_plot()
        self.update_fig()

    def initUI(self):
        # 设置界面位置,确保多张图叠加显示位置不同
        # self.setGeometry(100, 100, 658, 602)
        self.setFixedSize(724, 662)
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            # x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2 + 20 * (self.ID % 10)
            # y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2 + 20 * (self.ID % 10)
            x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2
            # print(x, y)
            self.move(x, y)

        # 添加界面内容
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.win_vlayout = QVBoxLayout(self.central_widget)

        # Canvas
        self.canvas = DynamicFig()

        # Control bar
        self.control_bar_frame = QFrame()  # 动图操作控制添加到窗口布局中
        self.control_bar_hlayout = QHBoxLayout(self.control_bar_frame)

        # Toolbar
        self.toolbar = QFrame()
        self.toolbar_hlayout = QHBoxLayout(self.toolbar)

        self.img_toolbar = CustomToolbar(self.canvas, self)
        self.img_sel_ComboBox = QComboBox()

        self.img_sel_ComboBox.addItems(self.img_type)
        self.img_sel_ComboBox.setCurrentIndex(0)
        self.img_sel_ComboBox.currentIndexChanged.connect(self.update_fig)

        self.toolbar.setStyleSheet("")
        self.toolbar_hlayout.addWidget(self.img_toolbar)
        self.toolbar_hlayout.addWidget(self.img_sel_ComboBox)
        # self.addToolBar(self.toolbar)

        # Display
        self.win_vlayout.addWidget(self.toolbar, 1)  # 画布添加到窗口布局中
        self.win_vlayout.addWidget(self.canvas, 15)  # 画布添加到窗口布局中
        self.win_vlayout.addWidget(self.control_bar_frame, 1)
        # self.win_vlayout.addWidget(self.figtoolbar)  # 工具栏添加到窗口布局中

    # @profile
    def update_fig(self):
        if self.img_sel_ComboBox.currentIndex() == 0:   # 动态展示 masking 图片
            idx = self.index % len(self.roi_data_pkg["arrays"])
            if not self.DEBUG:
                x, y, s = self.roi_data_pkg["coor_info"][idx]
                _str = f"{s}({x}, {y})"
                x = x + 5 if x < 610 else 610
                y = y - 12 if y > 30 else y + 37
                y = y if y < 565 else 565
                text = [{"x": x, "y": y, "text_annotations": _str}]
            else:
                text = None
            self.canvas.plot_image(data=self.roi_data_pkg["arrays"][idx],
                                   x_ticks_interval=48,
                                   y_ticks_interval=50,
                                   text_annotations=text,
                                   # title="Masking"
                                   )
        elif self.img_sel_ComboBox.currentIndex() == 1:   # 动态展示 masking 图片
            self.canvas.plot_image(data=self.roi_data_pkg["acc_spad_array"],
                                   x_ticks_interval=48,
                                   y_ticks_interval=50,
                                   # title="PCM"
                                   )
        elif self.img_sel_ComboBox.currentIndex() == 2:   # 动态展示 masking 图片
            self.canvas.plot_image(data=self.roi_data_pkg["depth_spad_array"],
                                   x_ticks_interval=16,
                                   y_ticks_interval=20
                                   )
        elif self.img_sel_ComboBox.currentIndex() == 3:   # 动态展示 masking 图片
            # --------------------- 配置刻度 --------------------
            # self.canvas.axes.xaxis.set_major_locator(MultipleLocator(48))
            # self.canvas.axes.yaxis.set_major_locator(MultipleLocator(50))
            self.canvas.plot_image(data=self.roi_data_pkg["fusion_image"],
                                   x_ticks_interval=48,
                                   y_ticks_interval=50
                                   )
        else:
            return

    def dynamic_fig(self):
        if self.is_playing and self.img_sel_ComboBox.currentIndex() == 0:
            self.index += 1
            # logging.error(f"index:{self.index}")
            self.update_fig()

    def Play_plot(self):
        # print('Play_plot')
        self._timer.timeout.connect(self.dynamic_fig)
        self._timer.start(700)  # plot after 1s delay

    def Pause_plot(self):
        # print('Pause_plot')
        self._timer.timeout.disconnect(self.dynamic_fig)

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
        """"
        调用方法保存ROI数据, 由于数据量较大，需要使用多线程执行
        """
        dir_path = QFileDialog.getExistingDirectory(self, "请选择保存的文件路径", "", QFileDialog.ShowDirsOnly)
        if dir_path == "":
            return
        self.hawk_config["fd_path"] = dir_path
        self.hawk_config["roi_name"] = "roi_mem"
        logging.info("标定数据保存中....")
        self.btn_save.setEnabled(False)

        def threadFunc():
            try:
                Hawk01Function.ROIDataPackageSave(roi_data_pkg=self.roi_data_pkg,
                                                  cfg=self.hawk_config,
                                                  save_sel=self.soft_config["roi_image_save"],
                                                  roi_data_format=self.soft_config["roi_data_format"])
            except Exception as e:
                logging.fatal(e)
            self.win_signal_sync.Obj_signal_0.emit(self.btn_save)
        thread = Thread(target=threadFunc)
        thread.start()
        return

    def bnt_save_release(self, Obj: QPushButton):
        Obj.setEnabled(True)
        return

    def PlaySwitch_plot(self):
        if self.is_playing:
            self.is_playing = False
            self.Pause_plot()
            # self.pushButton.setText('暂停')
            # print("stop")
            icon = QIcon(Functions.set_svg_icon("icon_play.svg", folder=self.icon_fd))
            self.btn_playControl.setIcon(icon)
        elif not self.is_playing:
            self.is_playing = True
            self.Play_plot()
            # self.pushButton.setText('运行')
            # print("play")
            icon = QIcon(Functions.set_svg_icon("icon_stop.svg", folder=self.icon_fd))
            self.btn_playControl.setIcon(icon)

    def closeEvent(self, event):
        # self._timer.stop()
        # self.arrays = []  # 清理内存
        # self.win_signal_sync.int_signal_1.emit(self.ID)     # 同步到主界面, 进行内存释放
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
        icon_play = QIcon(Functions.set_svg_icon("icon_play.svg", folder=self.icon_fd))
        self.btn_playControl.setIcon(icon_play)
        # Back Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_oneback = QPushButton()
        icon_oneback = QIcon(Functions.set_svg_icon("icon_oneback.svg", folder=self.icon_fd))
        self.btn_oneback.setIcon(icon_oneback)

        # Forward Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_oneforward = QPushButton()
        icon_oneforward = QIcon(Functions.set_svg_icon("icon_oneforward.svg", folder=self.icon_fd))
        self.btn_oneforward.setIcon(icon_oneforward)

        # Replay Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_replay = QPushButton()
        icon_replay = QIcon(Functions.set_svg_icon("icon_replay.svg", folder=self.icon_fd))
        self.btn_replay.setIcon(icon_replay)

        # Save Button
        # ////////////////////////////////////////////////////////////////////////
        self.btn_save = QPushButton()
        # icon_save = QIcon(Functions.set_svg_icon("icon_save.svg", folder="../gui/images/svg_icons/"))
        icon_save = QIcon(Functions.set_svg_icon("icon_save.svg", folder=self.icon_fd))
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
        self.win_signal_sync.Obj_signal_0.connect(self.bnt_save_release)


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

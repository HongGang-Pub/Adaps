import copy
import logging
import gc
import subprocess

from Hawk.HawkGUI_v002.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from SelfDefinedPackge import PubMethod
from Hawk.HawkGUI_v002.gui.uis.windows.main_window.ui_main import *
from Hawk.HawkGUI_v002.Hawk01Function.ROIZoneConfigUI import ROIZoneConfigWin
from Hawk.HawkGUI_v002.Hawk01Function.MaskingDisplayUI import MaskingWindow
from Hawk.HawkGUI_v002.Hawk01Function import Hawk01Function
from SelfDefinedPackge import MatplotExtension
from functools import partial
from threading import Thread
from Hawk.HawkGUI_v002.gui.Signal import MySignals

import objgraph
from memory_profiler import profile


# FUNCTIONS
class Hawk01MainUI:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.win_signal_sync = MySignals()

        # Get config
        # ///////////////////////////////////////////////////////////////
        self.hawk01_config = {}  # hawk01 general config
        self.hawk01_gui_config = {}  # hawk01 UI config
        self.hawk01_zone_config = {}  # hawk01 Zone config
        self.hawk01_roi_gen_config = {}  # hawk01 ROI config
        self.hawk01_register_config = {}  # PubMethod.ReadJsonFile('./.Hawk01Config/Hawk01ScriptRegConfig.json')

    # ///////////////////////////////////////////////////////////////
    # gui initial
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        """调用各个界面的 setup_gui, 完成界面初始化"""
        Hawk01MainUI.setup_script_gui(self)
        Hawk01MainUI.setup_roi_gui(self)
        Hawk01MainUI.setup_zone_gui(self)
        Hawk01MainUI.setup_file_gui(self)
        return

    # ///////////////////////////////////////////////////////////////
    # Script config window function
    # ///////////////////////////////////////////////////////////////
    def setup_script_gui(self):
        """寄存器相关的主界面配置"""
        # 配置下拉选项
        self.ui.load_pages.REF_CLK_ComboBox.addItems(self.hawk01_gui_config["REF_CLK"]["show_gui"])
        self.ui.load_pages.SYS_CLK_ComboBox.addItems(self.hawk01_gui_config["SYS_CLK"]["show_gui"])
        self.ui.load_pages.MST_MODE_ComboBox.addItems(self.hawk01_gui_config["MST_MODE"]["show_gui"])
        self.ui.load_pages.TRG_I_EN_ComboBox.addItems(self.hawk01_gui_config["TRG_I_EN"]["show_gui"])
        self.ui.load_pages.WORK_MODE_ComboBox.add_items(self.hawk01_gui_config["WORK_MODE"]["show_gui"])
        self.ui.load_pages.TDC_Bin_Width_ComboBox.addItems(self.hawk01_gui_config["TDC_BIN_W"]["show_gui"])
        self.ui.load_pages.MIPI_RATE_ComboBox.addItems(self.hawk01_gui_config["MIPI_RATE"]["show_gui"])
        self.ui.load_pages.SCAN_MODE_ComboBox.addItems(self.hawk01_gui_config["SCAN_MODE"]["show_gui"])

        REF_CLK_index = self.hawk01_gui_config["REF_CLK"]["config"].index(self.hawk01_config['REF_CLK'])
        MST_MODE_index = self.hawk01_gui_config["MST_MODE"]["config"].index(self.hawk01_config['MST_MODE'])
        TRG_I_EN_index = self.hawk01_gui_config["TRG_I_EN"]["config"].index(self.hawk01_config['TRG_I_EN'])
        TDC_BIN_W_index = self.hawk01_gui_config["TDC_BIN_W"]["config"].index(self.hawk01_config['TDC_BIN_W'])
        SYS_CLK_index = 2 - TDC_BIN_W_index % 3
        SCAN_MODE_index = self.hawk01_gui_config["SCAN_MODE"]["config"].index(self.hawk01_config['SCAN_MODE'])
        MIPI_RATE_indexs = self.hawk01_gui_config["MIPI_RATE"]["config"].index(self.hawk01_config['MIPI_RATE'])
        WORK_MODE_indexs = [self.hawk01_gui_config["WORK_MODE"]["config"].index(config) for config in
                            self.hawk01_config['WORK_MODE']]

        # 下拉框设置初始值
        self.ui.load_pages.REF_CLK_ComboBox.setCurrentIndex(REF_CLK_index)
        self.ui.load_pages.MST_MODE_ComboBox.setCurrentIndex(MST_MODE_index)
        self.ui.load_pages.TRG_I_EN_ComboBox.setCurrentIndex(TRG_I_EN_index)
        self.ui.load_pages.TDC_Bin_Width_ComboBox.setCurrentIndex(TDC_BIN_W_index)
        self.ui.load_pages.SYS_CLK_ComboBox.setCurrentIndex(SYS_CLK_index)
        self.ui.load_pages.SCAN_MODE_ComboBox.setCurrentIndex(SCAN_MODE_index)
        self.ui.load_pages.WORK_MODE_ComboBox.select_indexs(WORK_MODE_indexs)
        self.ui.load_pages.MIPI_RATE_ComboBox.setCurrentIndex(MIPI_RATE_indexs)

        # 滚动条设置初始值
        self.ui.load_pages.V_ROLL_NUM_Slider.setValue(self.hawk01_config['V_ROLL_NUM'] + 1)
        self.ui.load_pages.H_ROLL_NUM_Slider.setValue(self.hawk01_config['H_ROLL_NUM'] + 1)
        self.ui.load_pages.H_VLD_SEG_Slider.setValue(self.hawk01_config['H_VLD_SEG'] + 1)

        # 操作绑定
        self.ui.load_pages.REF_CLK_ComboBox.currentIndexChanged.connect(partial(Hawk01MainUI.UPDATE_REF_CLK, self))
        self.ui.load_pages.MST_MODE_ComboBox.currentIndexChanged.connect(partial(Hawk01MainUI.UPDATE_MST_MODE, self))
        self.ui.load_pages.TRG_I_EN_ComboBox.currentIndexChanged.connect(partial(Hawk01MainUI.UPDATE_TRG_I_EN, self))
        self.ui.load_pages.WORK_MODE_ComboBox.activated.connect(partial(Hawk01MainUI.UPDATE_WORK_MODE, self))
        self.ui.load_pages.MIPI_RATE_ComboBox.activated.connect(partial(Hawk01MainUI.UPDATE_MIPI_RATE, self))
        self.ui.load_pages.TDC_Bin_Width_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.UPDATE_TDC_BIN_W, self))
        self.ui.load_pages.SCAN_MODE_ComboBox.currentIndexChanged.connect(partial(Hawk01MainUI.UPDATE_SCAN_MODE, self))
        self.ui.load_pages.V_ROLL_NUM_Slider.valueChanged.connect(partial(Hawk01MainUI.UPDATE_V_ROLL_NUM, self))
        self.ui.load_pages.H_ROLL_NUM_Slider.valueChanged.connect(partial(Hawk01MainUI.UPDATE_H_ROLL_NUM, self))
        self.ui.load_pages.H_VLD_SEG_Slider.valueChanged.connect(partial(Hawk01MainUI.UPDATE_H_VLD_SEG, self))
        return

    # 下拉框值更新
    # ///////////////////////////////////////////////////////////////
    def UPDATE_REF_CLK(self, i):
        self.hawk01_config['REF_CLK'] = self.hawk01_gui_config["REF_CLK"]["config"][i]
        return

    def UPDATE_WORK_MODE(self, i):
        self.hawk01_config['WORK_MODE'] = self.ui.load_pages.WORK_MODE_ComboBox.get_selected_index()

    def UPDATE_SCAN_MODE(self, i):
        self.hawk01_config['SCAN_MODE'] = i

    def UPDATE_MST_MODE(self, i):
        self.hawk01_config['MST_MODE'] = i

    def UPDATE_TRG_I_EN(self, i):
        self.hawk01_config['TRG_I_EN'] = i

    def UPDATE_MIPI_RATE(self, i):
        self.hawk01_config['MIPI_RATE'] = self.hawk01_gui_config["MIPI_RATE"]["config"][i]

    def UPDATE_TDC_BIN_W(self, i):
        SYS_CLK_index = 2 - i % 3
        self.hawk01_config['TDC_BIN_W'] = self.hawk01_gui_config["TDC_BIN_W"]["config"][i]
        self.hawk01_config['SYS_CLK'] = self.hawk01_gui_config["SYS_CLK"]["config"][SYS_CLK_index]
        self.hawk01_config['UPSMP_MODE'] = 0b11 if i < 3 else 0b00
        self.ui.load_pages.SYS_CLK_ComboBox.setCurrentIndex(SYS_CLK_index)

    def UPDATE_V_ROLL_NUM(self, num):
        self.hawk01_config['V_ROLL_NUM'] = num - 1

    def UPDATE_H_ROLL_NUM(self, num):
        self.hawk01_config['H_ROLL_NUM'] = num - 1

    def UPDATE_H_VLD_SEG(self, num):
        self.hawk01_config['H_VLD_SEG'] = num - 1

    # ///////////////////////////////////////////////////////////////
    # ROI config window function
    # ///////////////////////////////////////////////////////////////
    def setup_roi_gui(self):
        """roi相关的主界面配置"""
        self.ui.load_pages.ROIConfig.setCurrentIndex(self.hawk01_config["Default_ROI_GEN_TYPE"])

        # Gen ROI for GUI
        self.ui.load_pages.seg_hs_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['seg_hs'])
        self.ui.load_pages.spad_vs_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['spad_vs'])
        self.ui.load_pages.light_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['light_shift'])
        self.ui.load_pages.sublight_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['sublight_shift'])
        self.ui.load_pages.ROI_Shape_ComboBox.setCurrentIndex(self.hawk01_roi_gen_config['ROIGenByJson']['roi_shape'])
        self.ui.load_pages.v_spad_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['v_spad_shift'])
        self.ui.load_pages.h_seg_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['h_seg_shift'])

        # Gen ROI for cali txt
        self.ui.load_pages.ROI_File_Load_LineEdit.setText(self.hawk01_roi_gen_config['ROIGenByFile']['gen_roi_file'])
        self.ui.load_pages.ROI_File_Load_Button.clicked.connect(partial(Hawk01MainUI.func_roi_load_file, self))

        # Gen ROI for Base ROI
        self.ui.load_pages.base_roi_file_LineEdit.setText(
            self.hawk01_roi_gen_config['ROIGenByBase']['base_roi_file'])
        self.ui.load_pages.start_rolling_SpinBox.setValue(
            self.hawk01_roi_gen_config['ROIGenByBase']['start_roll'] + 1)
        self.ui.load_pages.End_rolling_SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByBase']['end_roll'] + 1)
        self.ui.load_pages.base_roi_file_Button.clicked.connect(partial(Hawk01MainUI.func_base_roi_file, self))

        # Gen ROI for cali data
        self.ui.load_pages.cali_file_path_LineEdit.setText(self.hawk01_roi_gen_config['ROIGenByCali']['cali_file'])
        self.ui.load_pages.cali_order_ComboBox.setCurrentIndex(self.hawk01_roi_gen_config['ROIGenByCali']['is_reverse'])
        self.ui.load_pages.img_mirror_ComboBox.setCurrentIndex(
            self.hawk01_roi_gen_config['ROIGenByCali']['img_reverse'])
        self.ui.load_pages.cali_frm_num__SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByCali']['cali_frm_num'])
        self.ui.load_pages.remove_noise_ComboBox.setCurrentIndex(
            self.hawk01_roi_gen_config['ROIGenByCali']['remove_noise'])
        self.ui.load_pages.light_smooth_ComboBox.setCurrentIndex(
            self.hawk01_roi_gen_config['ROIGenByCali']['light_smooth'])
        self.ui.load_pages.ref_segment_SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByCali']['ref_segment'] + 1)
        self.ui.load_pages.curvature_SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByCali']['curvature'])
        self.ui.load_pages.correct_thres_SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByCali']['correct_thres'])
        self.ui.load_pages.mode_2D_ComboBox.setCurrentIndex(self.hawk01_roi_gen_config['ROIGenByCali']['mode2D'])
        self.ui.load_pages.cali_file_path_Button.clicked.connect(partial(Hawk01MainUI.func_roi_cali_folder, self))

        # 底部操作绑定
        self.ui.load_pages.ROIView.clicked.connect(partial(Hawk01MainUI.func_roi_view, self))
        self.win_signal_sync.sync_signal_0.connect(partial(Hawk01MainUI.func_open_roi_win, self))
        # self.ui.load_pages.ROISave.clicked.connect(partial(Hawk01MainUI.func_roi_save, self))  #TODO

        # ROI data刷新判断初始化
        self.ui_masking_win = {}  # 存储masking_window对象, 便于后续内存销毁
        self.MaskingWindowID = 0  # masking_window 标志位,
        self.__pre_roi_gen_type__ = -1  # 上一个bak数据,避免重复执行
        self.__pre_hawk01_config__ = {}  # 上一个配置数据,避免重复执行代码
        return

    def func_roi_load_file(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='ROI Coor Select', dir='',
                                              filter='file(*.txt) ;')
        if file == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.ROI_File_Load_LineEdit.setText(file)
        self.hawk01_roi_gen_config['ROIGenByFile']['gen_roi_file'] = file
        return

    def func_base_roi_file(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base ROI Select', dir='',
                                              filter='file(*.txt) ;')
        if file == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.base_roi_file_LineEdit.setText(file)
        self.hawk01_roi_gen_config['ROIGenByBase']['base_roi_file'] = file
        return

    def func_roi_cali_folder(self):
        fd = QFileDialog.getExistingDirectory(self, "Select Cali File", "")
        if fd == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.cali_file_path_LineEdit.setText(fd)
        self.hawk01_roi_gen_config['ROIGenByCali']['cali_file'] = fd
        return

    def func_get_roi_config(self):
        """获取 ROI GEN CONFIG(仅获取当前 GEN 类型的配置信息)"""
        self.roi_gen_type = self.ui.load_pages.ROIConfig.currentIndex()
        self.hawk01_config["Default_ROI_GEN_TYPE"] = self.roi_gen_type
        if self.roi_gen_type == 0:  # Gen ROI for GUI
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByJson']['seg_hs'] = self.ui.load_pages.seg_hs_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson']['spad_vs'] = self.ui.load_pages.spad_vs_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson']['light_shift'] = self.ui.load_pages.light_shift_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson'][
                'sublight_shift'] = self.ui.load_pages.sublight_shift_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson'][
                'roi_shape'] = self.ui.load_pages.ROI_Shape_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByJson']['v_spad_shift'] = self.ui.load_pages.v_spad_shift_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson']['h_seg_shift'] = self.ui.load_pages.h_seg_shift_spinBox.value()

        elif self.roi_gen_type == 1:  # Gen ROI for cali txt
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByFile'][
                'gen_roi_file'] = self.ui.load_pages.ROI_File_Load_LineEdit.text()

        elif self.roi_gen_type == 2:  # Gen ROI for Base ROI
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByBase'][
                'base_roi_file'] = self.ui.load_pages.base_roi_file_LineEdit.text()
            self.hawk01_roi_gen_config['ROIGenByBase'][
                'start_roll'] = self.ui.load_pages.start_rolling_SpinBox.value() - 1
            self.hawk01_roi_gen_config['ROIGenByBase']['end_roll'] = self.ui.load_pages.End_rolling_SpinBox.value() - 1
        else:
            # elif self.roi_gen_type == 3: # Gen ROI for cali data
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByCali']['cali_file'] = self.ui.load_pages.cali_file_path_LineEdit.text()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'is_reverse'] = self.ui.load_pages.cali_order_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'img_reverse'] = self.ui.load_pages.img_mirror_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'cali_frm_num'] = self.ui.load_pages.cali_frm_num__SpinBox.value()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'remove_noise'] = self.ui.load_pages.remove_noise_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'light_smooth'] = self.ui.load_pages.light_smooth_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'ref_segment'] = self.ui.load_pages.ref_segment_SpinBox.value() - 1
            self.hawk01_roi_gen_config['ROIGenByCali']['curvature'] = self.ui.load_pages.curvature_SpinBox.value()
            self.hawk01_roi_gen_config['ROIGenByCali'][
                'correct_thres'] = self.ui.load_pages.correct_thres_SpinBox.value()
            self.hawk01_roi_gen_config['ROIGenByCali']['mode2D'] = self.ui.load_pages.mode_2D_ComboBox.currentIndex()
        return

    def func_merge_hawk_config(self):
        """
        根据配置将界面上的config合并起来, 便于后续根据配置生成ROI等内容
        __hawk01_config__: 用于生成 脚本配置&ROI 的总的 config
        """
        __hawk01_zone_config__ = copy.deepcopy(self.hawk01_zone_config)

        def traverse_dict(d, parent_key=''):
            for key, value in d.items():
                full_key = f"{parent_key}.{key}" if parent_key else key
                if isinstance(value, dict):
                    traverse_dict(value, full_key)
                else:
                    try:
                        if isinstance(value, str):
                            d[key] = eval(value)
                        elif isinstance(value, list):
                            d[key] = [eval(s) for s in value]
                    except:
                        pass
        traverse_dict(d=__hawk01_zone_config__, parent_key='')  # 将zone_config的配置值全部转换为数字类型
        self.__hawk01_config__ = \
            {**self.hawk01_config, **self.hawk01_roi_gen_config['ROIGenByJson'],
             **__hawk01_zone_config__} if self.roi_gen_type == 0 else \
                {**self.hawk01_config, **self.hawk01_roi_gen_config['ROIGenByFile'],
                 **__hawk01_zone_config__} if self.roi_gen_type == 1 else \
                    {**self.hawk01_config, **self.hawk01_roi_gen_config['ROIGenByBase'],
                     **__hawk01_zone_config__} if self.roi_gen_type == 2 else \
                        {**self.hawk01_config, **self.hawk01_roi_gen_config['ROIGenByCali'],
                         **__hawk01_zone_config__}
        return

    # @profile
    def func_get_roi_data_pkg(self):
        """
        根据 ROI 界面配置生成 roi_data_pkg, 用于后续数据保存和成图展示
        由于标定较为缓慢, 可能占用主进程, 建议使用子进程进行调用
        roi_data_pkg["roi_gen_type"] = 3
        roi_data_pkg["roi_data_pkg"] = roi_data
        roi_data_pkg["arrays"] = arrays
        roi_data_pkg["fusion_image"] = fusion_image
        roi_data_pkg["spad_array_3D"] = spad_array_3D
        roi_data_pkg["acc_spad_array"] = acc_spad_array
        roi_data_pkg["depth_spad_array"] = depth_spad_array
        roi_data_pkg["coor_info"] = coor_info
        """
        # 获取 ROI_DATA_PKG, # 如果界面没有更新, 则无需再次执行代码
        # //////////////////////////////////////
        if self.roi_gen_type != self.__pre_roi_gen_type__ or self.__hawk01_config__ != self.__pre_hawk01_config__:
            logging.info("Get the latest ROI config...")
            self.__roi_data_pkg__ = \
                Hawk01Function.MskuRoiGenerateByJson(self.__hawk01_config__) if self.roi_gen_type == 0 else \
                    Hawk01Function.MskuRoiGenerateByFile(self.__hawk01_config__) if self.roi_gen_type == 1 else \
                        Hawk01Function.MskuRoiGenerateByBase(self.__hawk01_config__) if self.roi_gen_type == 2 else \
                            Hawk01Function.MskuRoiGenerateByCali(self.__hawk01_config__)
            self.__pre_roi_gen_type__ = self.roi_gen_type
            self.__pre_hawk01_config__ = self.__hawk01_config__
        return

    def func_refresh_hawk_config(self):
        """从 ROI ZONE config界面获取最新的配置"""
        logging.info("Get the latest ROI Zone config...")
        self.Hawk01ZoneConfig.serialize()

    # @profile
    def func_masking_date_mem_free(self, MaskingWindowID=None):
        """图像界面关闭或者销毁时, 释放masking内存"""
        # logging.info(f"Masking Window {MaskingWindowID} free...")
        try:
            del self.ui_masking_win[MaskingWindowID]
        except:
            pass
        if self.ui_masking_win == {}:
            del self.__roi_data_pkg__
            self.__pre_roi_gen_type__ = -1
            self.__pre_hawk01_config__ = {}
        gc.collect()
        return

    # @profile()
    def func_roi_view(self):
        """此函数调用子线程生成 roi_data_pkg, 然后 emit func_open_roi_win"""

        def threadFunc():
            try:
                # 获取界面配置并 merge 所有配置
                # ///////////////////////////////////////////
                Hawk01MainUI.func_get_roi_config(self)
                Hawk01MainUI.func_merge_hawk_config(self)
                # 获取 ROI_DATA_PKG
                Hawk01MainUI.func_get_roi_data_pkg(self)
                self.win_signal_sync.sync_signal_0.emit()
            except BaseException as e:
                logging.fatal(e)

        thread = Thread(target=threadFunc)
        thread.start()
        return

    def func_open_roi_win(self):
        """
        打开 ROI masking展示界面
        1. 最多支持展示 5 张图片, 若超出5张图片, 自动销毁最早的一张, 并进行内存释放
        """
        logging.info("ROI Masking display...")
        self.MaskingWindowID = 0 if self.ui_masking_win == {} else self.MaskingWindowID + 1
        if len(self.ui_masking_win) == 5:
            min_MaskingWindowID = min(self.ui_masking_win.keys())
            Hawk01MainUI.func_masking_date_mem_free(self, min_MaskingWindowID)
        self.ui_masking_win[self.MaskingWindowID] = MaskingWindow(title=f"ROI SHOW {self.MaskingWindowID + 1}",
                                                                  ID=self.MaskingWindowID,
                                                                  roi_data_pkg=self.__roi_data_pkg__,
                                                                  hawk_config=self.__hawk01_config__)
        self.ui_masking_win[self.MaskingWindowID].setStyleSheet(self.qssStyle)
        self.ui_masking_win[self.MaskingWindowID].win_signal_sync.int_signal_1.connect(
            partial(Hawk01MainUI.func_masking_date_mem_free, self))
        self.ui_masking_win[self.MaskingWindowID].show()
        return

    def func_roi_save(self):
        """
        此函数主要是保存 ROI 数据, 由于数据保存会占用主线程, 建议使用子进程执行
        """
        Hawk01MainUI.func_get_roi_data_pkg(self)
        Hawk01Function.ROIDataPackageSave(self.__roi_data_pkg__, self.__hawk01_config__, 1)
        Hawk01MainUI.func_masking_date_mem_free(self)
        return

    # ///////////////////////////////////////////////////////////////
    # ZONE config window function
    # ///////////////////////////////////////////////////////////////
    def setup_zone_gui(self):
        # Instans ROI_Zone_Config Win
        self.ui_zone_config_win = ROIZoneConfigWin(self.hawk01_zone_config, self.qssStyle)
        self.ui.load_pages.ROIZoneConfig.linkActivated.connect(partial(Hawk01MainUI.func_open_roizone_config_win, self))
        self.ui_zone_config_win.return_config_signal.sync_signal_0.connect(
            partial(Hawk01MainUI.func_refresh_hawk_config, self))
        return

    def func_open_roizone_config_win(self, url):
        """打开 ROI Zone config 界面"""
        logging.info("Open ROI zone config window...")
        self.ui_zone_config_win.setModal(True)
        self.ui_zone_config_win.hawk01_SYS_CLK = self.hawk01_config["SYS_CLK"]
        self.ui_zone_config_win.hawk01_PLL1_OD = eval(
            self.hawk01_register_config["FREQ_Config"][self.hawk01_config['REF_CLK']]["PLL1"][
                self.hawk01_config['SYS_CLK']]["OD"])
        self.ui_zone_config_win.show(self.hawk01_zone_config)

    # ///////////////////////////////////////////////////////////////
    # FILE config window function
    # ///////////////////////////////////////////////////////////////
    def setup_file_gui(self):
        """ FILE config 界面GUI配置"""
        self.ui.load_pages.reference_script_LineEdit.setText(self.hawk01_config['ref_cfg_file'])
        self.ui.load_pages.file_save_dir_LineEdit.setText(self.hawk01_config['fd_path'])
        self.ui.load_pages.reg_script_name_LineEdit.setText(self.hawk01_config['reg_name'])
        self.ui.load_pages.roi_sram_name_LineEdit.setText(self.hawk01_config['roi_name'])
        self.ui.load_pages.roi_sram_name_CheckBox.setChecked(self.hawk01_config['ROI_SRAM_Include'])
        self.ui.load_pages.SPADISS_Integration_CheckBox.setChecked(self.hawk01_config['SPADISS_Integration'])

        self.ui.load_pages.roi_sram_name_CheckBox.stateChanged.connect(
            partial(Hawk01MainUI.func_file_gui_checkBoxChange, self))
        self.ui.load_pages.SPADISS_Integration_CheckBox.stateChanged.connect(
            partial(Hawk01MainUI.func_file_gui_checkBoxChange, self))
        # 按钮绑定
        self.ui.load_pages.reference_script_Button.clicked.connect(
            partial(Hawk01MainUI.func_reference_script_file_sel, self))
        self.ui.load_pages.file_save_dir_Button.clicked.connect(partial(Hawk01MainUI.func_file_save_dir_sel, self))
        self.ui.load_pages.Save.clicked.connect(partial(Hawk01MainUI.func_mainUI_save, self))  # Save按钮连接保存操作
        self.win_signal_sync.Obj_signal_0.connect(partial(Hawk01MainUI.func_btn_release, self))  # 完成保存后, 释放Save按钮
        self.ui.load_pages.Test.clicked.connect(partial(Hawk01MainUI.open_folder, self))
        return

    def func_file_gui_checkBoxChange(self, state):
        self.hawk01_config['ROI_SRAM_Include'] = self.ui.load_pages.roi_sram_name_CheckBox.isChecked()
        self.hawk01_config['SPADISS_Integration'] = self.ui.load_pages.SPADISS_Integration_CheckBox.isChecked()
        return

    def func_reference_script_file_sel(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='Input',
                                              filter='file(*.txt) ;')
        if file:
            # 选择后缀为.txt
            self.ui.load_pages.reference_script_LineEdit.setText(file)
            self.hawk01_config['ref_cfg_file'] = file
            logging.info(self.hawk01_config['ref_cfg_file'])

    def func_file_save_dir_sel(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择保存的文件路径", "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.ui.load_pages.file_save_dir_LineEdit.setText(dir_path)
            self.hawk01_config['fd_path'] = dir_path
            logging.info(self.hawk01_config['fd_path'])

    def func_mainUI_save(self):
        """
        主界面的保存按钮保存数据: 包含 ROI 数据, Script 数据
            1. 使用子线程调用保存, 不占用主线程
        """
        self.ui.load_pages.Save.setEnabled(False)

        def threadFunc():
            try:
                # 获取界面配置并 merge 所有配置
                # ///////////////////////////////////////////
                Hawk01MainUI.func_get_MainUI_config(self)
                Hawk01MainUI.func_get_roi_config(self)
                Hawk01MainUI.func_merge_hawk_config(self)
                if self.hawk01_config["ROI_SRAM_Include"] == 1:
                    Hawk01MainUI.func_roi_save(self)
                Hawk01Function.ScriptDataSave(self.hawk01_config, self.hawk01_register_config)
            except Exception as e:
                logging.fatal(e)
            self.win_signal_sync.Obj_signal_0.emit(self.ui.load_pages.Save)

        thread = Thread(target=threadFunc)
        thread.start()

    def func_btn_release(self, Obj: QPushButton):
        Obj.setEnabled(True)
        return

    def open_folder(self):
        # 获取用户选择的文件夹路径
        folder_path = self.hawk01_config['fd_path']
        if folder_path:
            # 打开文件夹
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))

    def func_get_MainUI_config(self):
        self.hawk01_config['ref_cfg_file'] = self.ui.load_pages.reference_script_LineEdit.text()
        self.hawk01_config['reg_name'] = self.ui.load_pages.reg_script_name_LineEdit.text()
        self.hawk01_config['roi_name'] = self.ui.load_pages.roi_sram_name_LineEdit.text()
        self.hawk01_config['fd_path'] = self.ui.load_pages.file_save_dir_LineEdit.text()

    # ///////////////////////////////////////////////////////////////
    # 通用函数
    # ///////////////////////////////////////////////////////////////
    # 文件选择对话框
    # ///////////////////////////////////////////////////////////////

    def saveImage(self):  # 保存图片到本地
        fd, type = QFileDialog.getSaveFileName(self, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        logging.info(fd)

    def openDirectory(self):  # 打开文件夹（目录）
        fd = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        logging.info(fd)

    def openTextFile(self):  # 选择文本文件上传
        fd, fp = QFileDialog.getOpenFileName(self, "选择文件", "", "*.txt;;All Files(*)")
        logging.info(fd)

    def saveTextFile(self):  # 保存文本文件
        fd, fp = QFileDialog.getSaveFileName(self, "保存文件", "", "*.txt;;All Files(*)")
        logging.info(fd)
        logging.info(fp)

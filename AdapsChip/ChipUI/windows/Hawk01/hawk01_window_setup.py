import copy
import logging
import gc

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.windows.main_window.ui_main import UI_MainWindow

from AdapsChip.ChipUI.windows.Hawk01.roi_zone_config_setup import ROIZoneConfigWin
from AdapsChip.ChipUI.windows.Hawk01.masking_display_setup import MaskingWindow
from AdapsChip.ChipUI.windows.Hawk01 import hawk01_window_functions
from AdapsChip.Hawk01.Hawk01RegConfig import *
from functools import partial
from threading import Thread
from AdapsChip.ChipUI.gui.Signal import MySignals
from SelfDefinedPackge.JsonOperation import JsonFunction
from SelfDefinedPackge.PubMethod import invoking_function

class Hawk01MainUI:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ///////////////////////////////////////////////////////////////
    # gui initial
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # Load Hawk01 Config
        # ///////////////////////////////////////////////////////////////
        self.Hawk01Config = JsonFunction(file_path=".Hawk01Config/Hawk01Config.json")
        # self.Hawk01GuiConfig = JsonFunction(file_path=".Hawk01Config/Hawk01GuiConfig.json")
        self.Hawk01ZoneConfig = JsonFunction(file_path=".Hawk01Config/Hawk01ZoneConfig.json")
        self.Hawk01ROIGenConfig = JsonFunction(file_path=".Hawk01Config/Hawk01ROIGenConfig.json")
        # self.Hawk01RegisterConfig = JsonFunction('.Hawk01Config/Hawk01ScriptRegConfig_Invalid.json')

        self.hawk01_config = self.Hawk01Config.items
        # self.hawk01_gui_config = self.Hawk01GuiConfig.items
        self.hawk01_zone_config = self.Hawk01ZoneConfig.items
        self.hawk01_roi_gen_config = self.Hawk01ROIGenConfig.items
        self.soft_config = {}
        # self.hawk01_register_config = self.Hawk01RegisterConfig.items

        # All GUI signal sync
        # ///////////////////////////////////////////////////////////////
        self.hawk01_main_ui_signal_sync = MySignals()

        # 调用各个界面的 setup_gui, 完成界面初始化
        # ///////////////////////////////////////////////////////////////
        Hawk01MainUI.setup_script_gui(self)
        Hawk01MainUI.setup_roi_gui(self)
        Hawk01MainUI.setup_zone_gui(self)
        Hawk01MainUI.setup_file_gui(self)
        return

    # ///////////////////////////////////////////////////////////////
    # Script config window function
    # ///////////////////////////////////////////////////////////////
    def setup_script_gui(self):
        # ///////////////////////////////////////////////////////////////
        # 配置初始化, 如果配置文件没有此配置，需要初始化配置文件
        # ///////////////////////////////////////////////////////////////
        CONFIG_KEYS = ["XCLK", "MST_MODE", "WORK_MODE", "MIPI_RATE", "SYS_CLK", "TDC_BIN_W",
                       "V_PXL_OUT_NUM", "TRG_I_EN", "MINBIN_THRS", "MAXBIN_THRS", "OUT_BIN_NUM",
                       "PKS_ECHO_NUM", "SCAN_MODE", "V_ROLL_NUM", "H_ROLL_NUM", "H_VLD_SEG"]
        for key in CONFIG_KEYS:
            if not (key in self.hawk01_config):
                if key == 'WORK_MODE':  # list
                    self.hawk01_config[key] = [3]  # PCM MODE
                else:
                    self.hawk01_config[key] = 0
        # ///////////////////////////////////////////////////////////////
        # WORK_MODE: 针对多选下拉项组件, 需要根据原始数据重新刷新下拉选项
        # ///////////////////////////////////////////////////////////////
        work_mode_items_num = self.ui.load_pages.WORK_MODE_ComboBox.count()
        work_mode_items = []
        for index in range(work_mode_items_num):
            item_text = self.ui.load_pages.WORK_MODE_ComboBox.itemText(index)
            work_mode_items.append(item_text)
        self.ui.load_pages.WORK_MODE_ComboBox.clear_items()
        self.ui.load_pages.WORK_MODE_ComboBox.add_items(work_mode_items)

        # ///////////////////////////////////////////////////////////////
        # 设置初始值
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.XCLK_ComboBox.setCurrentIndex(self.hawk01_config['XCLK'])
        self.ui.load_pages.MST_MODE_ComboBox.setCurrentIndex(self.hawk01_config['MST_MODE'])
        self.ui.load_pages.WORK_MODE_ComboBox.select_indexs(self.hawk01_config['WORK_MODE'])
        self.ui.load_pages.MIPI_RATE_ComboBox.setCurrentIndex(self.hawk01_config['MIPI_RATE'])

        self.ui.load_pages.SYS_CLK_ComboBox.setCurrentIndex(self.hawk01_config['SYS_CLK'])
        self.ui.load_pages.TDC_BIN_W_ComboBox.setCurrentIndex(self.hawk01_config['TDC_BIN_W'])
        self.ui.load_pages.V_PXL_OUT_NUM_ComboBox.setCurrentIndex(self.hawk01_config['V_PXL_OUT_NUM'])
        self.ui.load_pages.TRG_I_EN_ComboBox.setCurrentIndex(self.hawk01_config['TRG_I_EN'])
        self.ui.load_pages.MINBIN_THRS_spinBox.setValue(self.hawk01_config['MINBIN_THRS'])
        self.ui.load_pages.MAXBIN_THRS_spinBox.setValue(self.hawk01_config['MAXBIN_THRS'])
        Hawk01MainUI.bin_thrs_uptate(self, 0)  # 设置 BIN_NUMBER
        self.ui.load_pages.OUT_BIN_NUM_ComboBox.setCurrentIndex(self.hawk01_config['OUT_BIN_NUM'])
        self.ui.load_pages.PKS_ECHO_NUM_ComboBox.setCurrentIndex(self.hawk01_config['PKS_ECHO_NUM'])

        self.ui.load_pages.SCAN_MODE_ComboBox.setCurrentIndex(self.hawk01_config['SCAN_MODE'])
        Hawk01MainUI.scan_mode_windows_change(self, self.hawk01_config['SCAN_MODE'])  # 控件隐藏及显示控制
        self.ui.load_pages.V_ROLL_NUM_Slider.setValue(self.hawk01_config['V_ROLL_NUM'] + 1)
        self.ui.load_pages.H_ROLL_NUM_Slider.setValue(self.hawk01_config['H_ROLL_NUM'] + 1)
        self.ui.load_pages.H_VLD_SEG_Slider.setValue(self.hawk01_config['H_VLD_SEG'] + 1)

        # 操作绑定
        self.ui.load_pages.XCLK_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "XCLK"))
        self.ui.load_pages.MST_MODE_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "MST_MODE"))
        self.ui.load_pages.WORK_MODE_ComboBox.activated.connect(partial(Hawk01MainUI.work_mode_update, self))
        self.ui.load_pages.MIPI_RATE_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "MIPI_RATE"))

        self.ui.load_pages.TDC_BIN_W_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "TDC_BIN_W"))
        self.ui.load_pages.V_PXL_OUT_NUM_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "V_PXL_OUT_NUM"))
        self.ui.load_pages.TRG_I_EN_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "TRG_I_EN"))
        self.ui.load_pages.MINBIN_THRS_spinBox.valueChanged.connect(partial(Hawk01MainUI.bin_thrs_uptate, self))
        self.ui.load_pages.MAXBIN_THRS_spinBox.valueChanged.connect(partial(Hawk01MainUI.bin_thrs_uptate, self))
        self.ui.load_pages.OUT_BIN_NUM_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "OUT_BIN_NUM"))
        self.ui.load_pages.PKS_ECHO_NUM_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "PKS_ECHO_NUM"))

        self.ui.load_pages.SCAN_MODE_ComboBox.currentIndexChanged.connect(
            partial(Hawk01MainUI.combobox_data_update, self, "SCAN_MODE"))
        self.ui.load_pages.V_ROLL_NUM_Slider.valueChanged.connect(partial(Hawk01MainUI.v_roll_num_update, self))
        self.ui.load_pages.H_ROLL_NUM_Slider.valueChanged.connect(partial(Hawk01MainUI.h_roll_num_update, self))
        self.ui.load_pages.H_VLD_SEG_Slider.valueChanged.connect(partial(Hawk01MainUI.h_vld_seg_update, self))
        return

    # 下拉框值更新
    # ///////////////////////////////////////////////////////////////
    def combobox_data_update(self, key, index):
        # logging.info(f"{key} {index}")
        self.hawk01_config[key] = index
        if key == "TDC_BIN_W":
            SYS_CLK_index = 2 - index % 3
            self.hawk01_config["SYS_CLK"] = SYS_CLK_index
            self.hawk01_config["UPSMP_MODE"] = 0b11 if index < 3 else 0b00
            self.ui.load_pages.SYS_CLK_ComboBox.setCurrentIndex(SYS_CLK_index)
        elif key == "SCAN_MODE":
            Hawk01MainUI.scan_mode_windows_change(self, index)
        return

    def work_mode_update(self, index):
        self.hawk01_config['WORK_MODE'] = self.ui.load_pages.WORK_MODE_ComboBox.get_selected_index()

    def bin_thrs_uptate(self, value):
        minbin_thrs = self.ui.load_pages.MINBIN_THRS_spinBox.value()
        maxbin_thrs = self.ui.load_pages.MAXBIN_THRS_spinBox.value()

        self.ui.load_pages.MINBIN_THRS_spinBox.setMaximum(maxbin_thrs)
        self.ui.load_pages.MAXBIN_THRS_spinBox.setMinimum(max(minbin_thrs, 1))  # MAXBIN_THRS can't 0

        self.hawk01_config["MINBIN_THRS"] = minbin_thrs
        self.hawk01_config["MAXBIN_THRS"] = maxbin_thrs
        bin_number = ((maxbin_thrs + 1) * 2 - minbin_thrs) * 2
        self.ui.load_pages.BIN_NUMBER_Value.setNum(bin_number)

    def v_roll_num_update(self, value):
        self.hawk01_config['V_ROLL_NUM'] = value - 1

    def h_roll_num_update(self, value):
        self.hawk01_config['H_ROLL_NUM'] = value - 1

    def h_vld_seg_update(self, value):
        self.hawk01_config['H_VLD_SEG'] = value - 1

    def scan_mode_windows_change(self, index):
        hidden = True if (index == 0) else False
        self.ui.load_pages.H_ROLL_NUM_Label.setHidden(hidden)
        self.ui.load_pages.H_ROLL_NUM_Frame.setHidden(hidden)
        self.ui.load_pages.h_seg_shift_Label.setHidden(hidden)
        self.ui.load_pages.h_seg_shift_spinBox.setHidden(hidden)
        self.ui.load_pages.mode_2D_Label.setHidden(hidden)
        self.ui.load_pages.mode_2D_ComboBox.setHidden(hidden)
        pass

    def debug_shortcut_windows_change(self, hidden: bool):
        self.ui.load_pages.cali_order_Label.setHidden(hidden)
        self.ui.load_pages.cali_order_ComboBox.setHidden(hidden)
        self.ui.load_pages.cali_frm_num_Label.setHidden(hidden)
        self.ui.load_pages.cali_frm_num__SpinBox.setHidden(hidden)
        self.ui.load_pages.ref_segment_Label.setHidden(hidden)
        self.ui.load_pages.ref_segment_SpinBox.setHidden(hidden)
        pass

    # ///////////////////////////////////////////////////////////////
    # ROI config window function
    # ///////////////////////////////////////////////////////////////
    def setup_roi_gui(self):
        """roi相关的主界面配置"""
        self.ui.load_pages.ROIConfig.setCurrentIndex(self.hawk01_config["Default_ROI_GEN_TYPE"])

        tab_bar = self.ui.load_pages.ROIConfig.tabBar()
        # 隐藏特定索引的标签页标签
        # tab_bar.setTabVisible(2, False)

        # Gen ROI for GUI
        self.ui.load_pages.seg_hs_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['seg_hs'] + 1)
        self.ui.load_pages.h_seg_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['h_seg_shift'])
        self.ui.load_pages.spad_vs_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['spad_vs'] + 1)
        self.ui.load_pages.light_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['light_shift'])
        self.ui.load_pages.sublight_group_LineEdit.setText(self.hawk01_roi_gen_config['ROIGenByJson']['sublight_group'])
        self.ui.load_pages.sublight_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['sublight_shift'])
        self.ui.load_pages.ROI_Shape_ComboBox.setCurrentIndex(self.hawk01_roi_gen_config['ROIGenByJson']['roi_shape'])
        self.ui.load_pages.ROI_Retrace_ComboBox.setCurrentIndex(self.hawk01_roi_gen_config['ROIGenByJson']['roi_retrace'])
        self.ui.load_pages.v_spad_shift_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByJson']['v_spad_shift'])

        # Gen ROI for cali txt
        self.ui.load_pages.Cali_File_Load_LineEdit.setText(self.hawk01_roi_gen_config['ROIGenByFile']['cali_file'])
        self.ui.load_pages.Excel_Sheet_sel_spinBox.setValue(self.hawk01_roi_gen_config['ROIGenByFile']['sheet_sel'] + 1)
        self.ui.load_pages.Cali_File_Load_Button.clicked.connect(partial(Hawk01MainUI.cali_file_select, self))

        # Gen ROI for Base ROI
        self.ui.load_pages.ROI_File_LineEdit.setText(self.hawk01_roi_gen_config['ROIGenByBase']['roi_file'])
        self.ui.load_pages.Start_Rolling_SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByBase']['start_roll'] + 1)
        self.ui.load_pages.End_Rolling_SpinBox.setValue(self.hawk01_roi_gen_config['ROIGenByBase']['end_roll'] + 1)
        self.ui.load_pages.ROI_File_Button.clicked.connect(partial(Hawk01MainUI.roi_file_select, self))

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
        self.ui.load_pages.cali_file_path_Button.clicked.connect(partial(Hawk01MainUI.roi_cali_folder_select, self))
        Hawk01MainUI.debug_shortcut_windows_change(self, True)  # 默认隐藏相关字段

        # 底部操作绑定
        self.ui.load_pages.ROIView.clicked.connect(partial(Hawk01MainUI.roi_view, self))
        self.hawk01_main_ui_signal_sync.sync_signal_0.connect(partial(Hawk01MainUI.open_roi_win, self))
        self.ui.load_pages.ROISave.clicked.connect(partial(Hawk01MainUI.roiUI_roi_save, self))

        # 创建 Ctrl+E 的快捷键, 控制显示隐藏字段
        debug_shortcut = QShortcut(QKeySequence("Ctrl+E"), self)
        debug_shortcut.activated.connect(partial(Hawk01MainUI.debug_shortcut_windows_change, self, False))

        # 特殊字段限制输入格式
        reg = QRegularExpression('[0-9, ]+$')
        validator = QRegularExpressionValidator(reg)
        self.ui.load_pages.sublight_group_LineEdit.setValidator(validator)

        # ROI data刷新判断初始化
        self.ui_masking_win = None  # 存储masking_window对象, 便于后续内存销毁
        # self.MaskingWindowID = 0  # masking_window 标志位,
        self.__pre_roi_gen_type__ = -1  # 上一个bak数据,避免重复执行
        self.__pre_hawk01_config__ = {}  # 上一个配置数据,避免重复执行代码
        return

    def cali_file_select(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='ROI cali data select', dir='',
                                              filter='file(*.txt *.csv *.xls *.xlsx) ;')
        if file == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.Cali_File_Load_LineEdit.setText(file)
        self.hawk01_roi_gen_config['ROIGenByFile']['cali_file'] = file
        return

    def roi_file_select(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='ROI select', dir='',
                                              filter='file(*.txt) ;')
        if file == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.ROI_File_LineEdit.setText(file)
        self.hawk01_roi_gen_config['ROIGenByBase']['roi_file'] = file
        return

    def roi_cali_folder_select(self):
        fd = QFileDialog.getExistingDirectory(self, "Select Cali File", "")
        if fd == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.cali_file_path_LineEdit.setText(fd)
        self.hawk01_roi_gen_config['ROIGenByCali']['cali_file'] = fd
        return

    def get_roi_gui_config(self):
        """获取 ROI GEN CONFIG(仅获取当前 GEN 类型的配置信息)"""
        self.roi_gen_type = self.ui.load_pages.ROIConfig.currentIndex()
        self.hawk01_config["Default_ROI_GEN_TYPE"] = self.roi_gen_type
        if self.roi_gen_type == 0:  # Gen ROI for GUI
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByJson']['seg_hs'] = self.ui.load_pages.seg_hs_spinBox.value() - 1
            self.hawk01_roi_gen_config['ROIGenByJson']['spad_vs'] = self.ui.load_pages.spad_vs_spinBox.value() - 1
            self.hawk01_roi_gen_config['ROIGenByJson']['light_shift'] = self.ui.load_pages.light_shift_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson'][
                'sublight_group'] = self.ui.load_pages.sublight_group_LineEdit.text()
            self.hawk01_roi_gen_config['ROIGenByJson'][
                'sublight_shift'] = self.ui.load_pages.sublight_shift_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson'][
                'roi_shape'] = self.ui.load_pages.ROI_Shape_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByJson'][
                'roi_retrace'] = self.ui.load_pages.ROI_Retrace_ComboBox.currentIndex()
            self.hawk01_roi_gen_config['ROIGenByJson']['v_spad_shift'] = self.ui.load_pages.v_spad_shift_spinBox.value()
            self.hawk01_roi_gen_config['ROIGenByJson']['h_seg_shift'] = self.ui.load_pages.h_seg_shift_spinBox.value()

        elif self.roi_gen_type == 1:  # Gen ROI for cali txt
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByFile']['cali_file'] = self.ui.load_pages.Cali_File_Load_LineEdit.text()
            self.hawk01_roi_gen_config['ROIGenByFile'][
                'sheet_sel'] = self.ui.load_pages.Excel_Sheet_sel_spinBox.value() - 1

        elif self.roi_gen_type == 2:  # Gen ROI for Base ROI
            # 获取配置
            self.hawk01_roi_gen_config['ROIGenByBase']['roi_file'] = self.ui.load_pages.ROI_File_LineEdit.text()
            self.hawk01_roi_gen_config['ROIGenByBase'][
                'start_roll'] = self.ui.load_pages.Start_Rolling_SpinBox.value() - 1
            self.hawk01_roi_gen_config['ROIGenByBase']['end_roll'] = self.ui.load_pages.End_Rolling_SpinBox.value() - 1
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

    # @memory_profiler.profile
    def merge_hawk_config(self):
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
            {**self.hawk01_config,
             **self.hawk01_roi_gen_config['ROIGenByJson'], **__hawk01_zone_config__} if self.roi_gen_type == 0 \
                else {**self.hawk01_config,
                      **self.hawk01_roi_gen_config['ROIGenByFile'], **__hawk01_zone_config__} if self.roi_gen_type == 1 \
                else {**self.hawk01_config,
                      **self.hawk01_roi_gen_config['ROIGenByBase'], **__hawk01_zone_config__} if self.roi_gen_type == 2 \
                else {**self.hawk01_config,
                      **self.hawk01_roi_gen_config['ROIGenByCali'], **__hawk01_zone_config__}
        return

    def get_roi_data_pkg(self):
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
        # 如果 ROI_DATA 根据文件生成, 则有可能是文件改变, 需要再次执行代码
        # //////////////////////////////////////
        if self.roi_gen_type != self.__pre_roi_gen_type__ or self.__hawk01_config__ != self.__pre_hawk01_config__ \
                or self.roi_gen_type == 1:
            # logging.info("Get the latest ROI config...")
            self.__roi_data_pkg__ = \
                hawk01_window_functions.MskuRoiGenerateByJson(self.__hawk01_config__) if self.roi_gen_type == 0 \
                    else hawk01_window_functions.MskuRoiGenerateByFile(self.__hawk01_config__) if self.roi_gen_type == 1 \
                    else hawk01_window_functions.MskuRoiGenerateByROIMEM(
                    self.__hawk01_config__) if self.roi_gen_type == 2 \
                    else hawk01_window_functions.MskuRoiGenerateByCali(self.__hawk01_config__)
            self.__pre_roi_gen_type__ = self.roi_gen_type
            self.__pre_hawk01_config__ = self.__hawk01_config__
            # logging.warning(f"Haw01MainUI:self.__roi_data_pkg__:{asizeof.asizeof(self.__roi_data_pkg__)/(1023**2):0.2f}M")
        return

    def refresh_hawk_config(self):
        """从 ROI ZONE config界面获取最新的配置"""
        # logging.info("Get the latest ROI Zone config...")
        self.Hawk01ZoneConfig.serialize()

    # @memory_profiler.profile
    def masking_data_mem_free(self):
        """图像界面关闭或者销毁时, 释放masking内存"""
        if self.ui_masking_win is None:
            self.__roi_data_pkg__ = None
            self.__pre_roi_gen_type__ = -1
            self.__pre_hawk01_config__ = {}
        gc.collect()
        return

    # @memory_profiler.profile
    def roi_win_free(self):
        """图像界面关闭或者销毁时, 释放masking内存"""
        self.ui_masking_win = None
        Hawk01MainUI.masking_data_mem_free(self)
        return

    def roi_view(self):
        """此函数调用子线程生成 roi_data_pkg, 然后 emit open_roi_win"""

        def excute():
            # 获取界面配置并 merge 所有配置
            # ///////////////////////////////////////////
            Hawk01MainUI.get_roi_gui_config(self)
            Hawk01MainUI.merge_hawk_config(self)
            # 获取 ROI_DATA_PKG
            Hawk01MainUI.get_roi_data_pkg(self)
            self.hawk01_main_ui_signal_sync.sync_signal_0.emit()

        def threadFunc():
            invoking_function(self.DEBUG, excute)

        thread = Thread(target=threadFunc)
        thread.start()
        return

    # @memory_profiler.profile
    def open_roi_win(self):
        """
        打开 ROI masking展示界面
        """
        # logging.info("ROI Masking display...")
        # arrays = []
        # for index in range(32):
        #     arr = np.random.rand(576, 768)
        #     arrays.append(arr)
        # self.__roi_data_pkg__["masking_arrays"] = arrays
        if self.ui_masking_win is None:
            self.ui_masking_win = MaskingWindow(title=f"Hawk01 roi show",
                                                roi_data_pkg=self.__roi_data_pkg__,
                                                hawk_config=self.__hawk01_config__,
                                                soft_config=self.soft_config,
                                                DEBUG=self.DEBUG)
            self.ui_masking_win.setStyleSheet(self.qssStyle)
            # self.ui_masking_win.setAttribute(Qt.WA_DeleteOnClose)
            self.ui_masking_win.destroyed.connect(partial(Hawk01MainUI.roi_win_free, self))
            self.ui_masking_win.show()
        else:
            # 如果窗口没有关闭, 则刷新最新的 ROI 数据到窗口, 重新展示
            self.ui_masking_win.roi_data_pkg = self.__roi_data_pkg__
            self.ui_masking_win.hawk_config = self.__hawk01_config__
            self.ui_masking_win.soft_config = self.soft_config
            self.ui_masking_win.roi_data_sync()
            self.ui_masking_win.activateWindow()
            self.ui_masking_win.Replay_plog()
        return

    def roi_save(self):
        """
        此函数主要是保存 ROI 数据, 由于数据保存会占用主线程, 建议使用子进程执行
        """
        Hawk01MainUI.get_roi_data_pkg(self)
        hawk01_window_functions.ROIDataPackageSave(roi_data_pkg=self.__roi_data_pkg__,
                                                   hawk01_config=self.__hawk01_config__,
                                                   save_sel=self.soft_config["roi_image_save"],
                                                   roi_data_format=self.soft_config["roi_data_format"])
        Hawk01MainUI.masking_data_mem_free(self)
        return

    # ///////////////////////////////////////////////////////////////
    # ZONE config window function
    # ///////////////////////////////////////////////////////////////
    def setup_zone_gui(self):
        # Instans ROI_Zone_Config Win
        self.ui_zone_config_win = ROIZoneConfigWin(self.hawk01_zone_config, self.qssStyle)
        self.ui.load_pages.ROIZoneConfig.linkActivated.connect(partial(Hawk01MainUI.open_roizone_config_win, self))
        self.ui_zone_config_win.return_config_signal.sync_signal_0.connect(
            partial(Hawk01MainUI.refresh_hawk_config, self))
        return

    def open_roizone_config_win(self, url):
        """打开 ROI Zone config 界面"""
        logging.info("Open ROI zone config window...")
        self.ui_zone_config_win.setModal(True)
        self.ui_zone_config_win.hawk01_SYS_CLK = self.hawk01_config["SYS_CLK"]
        self.ui_zone_config_win.hawk01_PLL1_OD = FREQ_Config[self.hawk01_config['XCLK']]["PLL1"] \
            [self.hawk01_config['SYS_CLK']]["OD"]
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
        # self.ui.load_pages.SPADISS_Integration_CheckBox.setChecked(self.hawk01_config['SPADISS_Integration'])

        self.ui.load_pages.roi_sram_name_CheckBox.stateChanged.connect(
            partial(Hawk01MainUI.file_gui_checkBoxChange, self))
        # self.ui.load_pages.SPADISS_Integration_CheckBox.stateChanged.connect(
        #     partial(Hawk01MainUI.file_gui_checkBoxChange, self))
        # 按钮绑定
        self.ui.load_pages.reference_script_sel_Button.clicked.connect(partial(Hawk01MainUI.reference_script_file_sel, self))
        self.ui.load_pages.reference_script_parse_Button.clicked.connect(partial(Hawk01MainUI.script_parse, self))
        self.ui.load_pages.file_save_dir_Button.clicked.connect(partial(Hawk01MainUI.file_save_dir_sel, self))
        self.ui.load_pages.Save.clicked.connect(partial(Hawk01MainUI.mainUI_save, self))  # Save按钮连接保存操作
        self.hawk01_main_ui_signal_sync.Obj_signal_0.connect(partial(Hawk01MainUI.func_btn_release, self))  # 完成保存后, 释放Save按钮
        self.ui.load_pages.Open.clicked.connect(partial(Hawk01MainUI.open_folder, self))
        return

    def file_gui_checkBoxChange(self, state):
        self.hawk01_config['ROI_SRAM_Include'] = self.ui.load_pages.roi_sram_name_CheckBox.isChecked()
        # self.hawk01_config['SPADISS_Integration'] = self.ui.load_pages.SPADISS_Integration_CheckBox.isChecked()
        return

    def reference_script_file_sel(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='',
                                              filter='file(*.txt) ;')
        if file:
            # 选择后缀为.txt
            self.ui.load_pages.reference_script_LineEdit.setText(file)
            self.hawk01_config['ref_cfg_file'] = file
            logging.info(self.hawk01_config['ref_cfg_file'])

    def script_parse(self):
        # Hawk01MainUI.merge_hawk_config(self)
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='',
                                              filter='file(*.txt) ;')

        def excute():
            hawk01_window_functions.ScriptParse(self.hawk01_config, file)
        invoking_function(self.DEBUG, excute)

    def file_save_dir_sel(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择保存的文件路径", "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.ui.load_pages.file_save_dir_LineEdit.setText(dir_path)
            self.hawk01_config['fd_path'] = dir_path
            logging.info(self.hawk01_config['fd_path'])

    def roiUI_roi_save(self):
        """
        ROI界面的保存按钮保存数据: 包含 ROI 数据
            1. 使用子线程调用保存, 不占用主线程
        """

        def excute():
            # 获取界面配置并 merge 所有配置
            # ///////////////////////////////////////////
            Hawk01MainUI.get_mainUI_config(self)
            Hawk01MainUI.get_roi_gui_config(self)
            Hawk01MainUI.merge_hawk_config(self)
            Hawk01MainUI.roi_save(self)

        self.ui.load_pages.ROISave.setEnabled(False)

        def threadFunc():
            invoking_function(self.DEBUG, excute)
            self.hawk01_main_ui_signal_sync.Obj_signal_0.emit(self.ui.load_pages.ROISave)

        thread = Thread(target=threadFunc)
        thread.start()

    def mainUI_save(self):
        """
        主界面的保存按钮保存数据: 包含 ROI 数据, Script 数据
            1. 使用子线程调用保存, 不占用主线程
        """

        def excute():
            # 获取界面配置并 merge 所有配置
            # ///////////////////////////////////////////
            Hawk01MainUI.get_mainUI_config(self)
            Hawk01MainUI.get_roi_gui_config(self)
            Hawk01MainUI.merge_hawk_config(self)
            if self.hawk01_config["ROI_SRAM_Include"] == 1:
                Hawk01MainUI.roi_save(self)
            hawk01_window_functions.ScriptDataSave(self.hawk01_config)
            logging.info("Data save complete...")

        self.ui.load_pages.Save.setEnabled(False)

        def threadFunc():
            invoking_function(self.DEBUG, excute)
            self.hawk01_main_ui_signal_sync.Obj_signal_0.emit(self.ui.load_pages.Save)

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

    def get_mainUI_config(self):
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

    def closeEvent(self):
        self.Hawk01Config.serialize()
        self.Hawk01ROIGenConfig.serialize()
        try:
            self.ui_masking_win.close()
        except:
            pass
        pass

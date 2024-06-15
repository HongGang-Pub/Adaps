import logging

import Hawk.HawkGUI_v002.HawkFunction.MaskingWindow
from Hawk.HawkGUI_v002.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.uis.windows.main_window.ui_main import *
from Hawk.HawkGUI_v002.HawkFunction.ROIZoneConfig import ROIZoneConfigWin
from Hawk.HawkGUI_v002.HawkFunction.MaskingWindow import MaskingWindow
from functools import partial


# FUNCTIONS
class HawkFunctions:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Get config
        # ///////////////////////////////////////////////////////////////
        self.hawk_config = {}  # hawk general config
        self.gui_value_config = {}  # hawk UI function

    # gui initial
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        HawkFunctions.setup_script_gui(self)
        HawkFunctions.setup_roi_gui(self)
        HawkFunctions.setup_masking_gui(self)
        HawkFunctions.setup_zone_gui(self)
        return

    def setup_script_gui(self):
        # 配置下拉选项
        self.ui.load_pages.REF_CLK_Config_ComboBox.addItems(self.gui_value_config["REF_CLK"]["show_gui"])
        self.ui.load_pages.SYS_CLK_Config_ComboBox.addItems(self.gui_value_config["SYS_CLK"]["show_gui"])
        self.ui.load_pages.MST_MODE_ComboBox.addItems(self.gui_value_config["MST_MODE"]["show_gui"])
        self.ui.load_pages.TRG_I_EN_ComboBox.addItems(self.gui_value_config["TRG_I_EN"]["show_gui"])
        self.ui.load_pages.WORK_MODE_ComboBox.add_items(self.gui_value_config["WORK_MODE"]["show_gui"])
        self.ui.load_pages.TDC_Bin_Width_ComboBox.addItems(self.gui_value_config["TDC_BIN_W"]["show_gui"])
        self.ui.load_pages.MIPI_RATE_ComboBox.add_items(self.gui_value_config["MIPI_RATE"]["show_gui"])
        self.ui.load_pages.SCAN_MODE_ComboBox.addItems(self.gui_value_config["SCAN_MODE"]["show_gui"])

        REF_CLK_index = self.gui_value_config["REF_CLK"]["config"].index(self.hawk_config['FREF_CLK'])
        MST_MODE_index = self.gui_value_config["MST_MODE"]["config"].index(self.hawk_config['MST_MODE'])
        TRG_I_EN_index = self.gui_value_config["TRG_I_EN"]["config"].index(self.hawk_config['TRG_I_EN'])
        TDC_BIN_W_index = self.gui_value_config["TDC_BIN_W"]["config"].index(self.hawk_config['TDC_BIN_W'])
        SYS_CLK_index = 2 - TDC_BIN_W_index % 3
        SCAN_MODE_index = self.gui_value_config["SCAN_MODE"]["config"].index(self.hawk_config['SCAN_MODE'])

        WORK_MODE_indexs = [self.gui_value_config["WORK_MODE"]["config"].index(config) for config in
                            self.hawk_config['WORK_MODE']]
        MIPI_RATE_indexs = [self.gui_value_config["MIPI_RATE"]["config"].index(config) for config in
                            self.hawk_config['MIPI_RATE']]

        # 下拉框设置初始值
        self.ui.load_pages.REF_CLK_Config_ComboBox.setCurrentIndex(REF_CLK_index)
        self.ui.load_pages.MST_MODE_ComboBox.setCurrentIndex(MST_MODE_index)
        self.ui.load_pages.TRG_I_EN_ComboBox.setCurrentIndex(TRG_I_EN_index)
        self.ui.load_pages.TDC_Bin_Width_ComboBox.setCurrentIndex(TDC_BIN_W_index)
        self.ui.load_pages.SYS_CLK_Config_ComboBox.setCurrentIndex(SYS_CLK_index)
        self.ui.load_pages.SCAN_MODE_ComboBox.setCurrentIndex(SCAN_MODE_index)

        self.ui.load_pages.WORK_MODE_ComboBox.select_indexs(WORK_MODE_indexs)
        self.ui.load_pages.MIPI_RATE_ComboBox.select_indexs(MIPI_RATE_indexs)

        # 滚动条设置初始值
        self.ui.load_pages.V_ROLL_NUM_Slider.setValue(self.hawk_config['V_ROLL_NUM'] + 1)
        self.ui.load_pages.H_ROLL_NUM_Slider.setValue(self.hawk_config['H_ROLL_NUM'] + 1)
        self.ui.load_pages.H_VLD_SEG_Slider.setValue(self.hawk_config['H_VLD_SEG'] + 1)

        # 文本框设置初始值
        self.ui.load_pages.base_script_LineEdit.setText(self.hawk_config['ref_cfg_file'])
        self.ui.load_pages.file_save_dir_LineEdit.setText(self.hawk_config['fd_path'])
        self.ui.load_pages.REG_CFG_File_LineEdit.setText(self.hawk_config['config_name'])
        self.ui.load_pages.ROI_SRAM_File_LineEdit.setText(self.hawk_config['roi_name'])

        self.ui.load_pages.WORK_MODE_ComboBox.activated.connect(partial(HawkFunctions.WORK_MODE_UPDATE, self))
        self.ui.load_pages.SCAN_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.SCAN_MODE_UPDATE, self))
        self.ui.load_pages.MIPI_RATE_ComboBox.activated.connect(partial(HawkFunctions.MIPI_RATE_UPDATE, self))
        self.ui.load_pages.MST_MODE_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.MST_MODE_UPDATE, self))
        self.ui.load_pages.TRG_I_EN_ComboBox.currentIndexChanged.connect(partial(HawkFunctions.TRG_I_EN_UPDATE, self))
        self.ui.load_pages.TDC_Bin_Width_ComboBox.currentIndexChanged.connect(
            partial(HawkFunctions.TDC_BIN_W_UPDATE, self))
        self.ui.load_pages.V_ROLL_NUM_Slider.valueChanged.connect(partial(HawkFunctions.V_ROLL_NUM_UPDATE, self))
        self.ui.load_pages.H_ROLL_NUM_Slider.valueChanged.connect(partial(HawkFunctions.H_ROLL_NUM_UPDATE, self))
        self.ui.load_pages.H_VLD_SEG_Slider.valueChanged.connect(partial(HawkFunctions.H_VLD_SEG_UPDATE, self))

        # 按钮绑定
        self.ui.load_pages.base_script_Button.clicked.connect(partial(HawkFunctions.base_script_file_sel_func, self))
        self.ui.load_pages.file_save_dir_Button.clicked.connect(partial(HawkFunctions.file_save_dir_sel_func, self))
        self.ui.load_pages.Save.clicked.connect(partial(HawkFunctions.get_script_config, self))
        self.ui.load_pages.ROIView.clicked.connect(partial(HawkFunctions.open_roi_masking_win, self))
        return

    def setup_roi_gui(self):
        # Gen ROI for GUI
        self.ui.load_pages.seg_hs_spinBox.setValue(self.hawk_roi_gen_config['ROIGenDirect']['seg_hs'])
        self.ui.load_pages.spad_vs_spinBox.setValue(self.hawk_roi_gen_config['ROIGenDirect']['spad_vs'])
        self.ui.load_pages.light_shift_spinBox.setValue(self.hawk_roi_gen_config['ROIGenDirect']['light_shift'])
        self.ui.load_pages.sublight_shift_spinBox.setValue(self.hawk_roi_gen_config['ROIGenDirect']['sublight_shift'])
        self.ui.load_pages.ROI_Shape_ComboBox.setCurrentIndex(self.hawk_roi_gen_config['ROIGenDirect']['roi_shape'])
        self.ui.load_pages.v_spad_shift_spinBox.setValue(self.hawk_roi_gen_config['ROIGenDirect']['v_spad_shift'])
        self.ui.load_pages.h_seg_shift_spinBox.setValue(self.hawk_roi_gen_config['ROIGenDirect']['h_seg_shift'])

        # Gen ROI for cali txt
        self.ui.load_pages.ROI_File_Load_LineEdit.setText(self.hawk_roi_gen_config['ROIGenByFile']['gen_roi_file'])
        self.ui.load_pages.ROI_File_Load_Button.clicked.connect(partial(HawkFunctions.roi_load_file_func, self))

        # Gen ROI for Base ROI
        self.ui.load_pages.base_roi_file_LineEdit.setText(self.hawk_roi_gen_config['ROIGenByBaseROI']['base_roi_file'])
        self.ui.load_pages.start_rolling_SpinBox.setValue(self.hawk_roi_gen_config['ROIGenByBaseROI']['start_roll'] + 1)
        self.ui.load_pages.End_rolling_SpinBox.setValue(self.hawk_roi_gen_config['ROIGenByBaseROI']['end_roll'] + 1)

        self.ui.load_pages.ROI_File_Load_Button.clicked.connect(partial(HawkFunctions.base_roi_file_func, self))

        # Gen ROI for cali data
        self.ui.load_pages.cali_order_ComboBox.setCurrentIndex(
            self.hawk_roi_gen_config['ROIGenByROICali']['is_reverse'])
        self.ui.load_pages.img_mirror_ComboBox.setCurrentIndex(
            self.hawk_roi_gen_config['ROIGenByROICali']['img_reverse'])
        self.ui.load_pages.cali_frm_num__SpinBox.setValue(self.hawk_roi_gen_config['ROIGenByROICali']['cali_frm_num'])
        self.ui.load_pages.remove_noise_ComboBox.setCurrentIndex(
            self.hawk_roi_gen_config['ROIGenByROICali']['remove_noise'])
        self.ui.load_pages.light_smooth_ComboBox.setCurrentIndex(
            self.hawk_roi_gen_config['ROIGenByROICali']['light_smooth'])
        self.ui.load_pages.ref_segment_SpinBox.setValue(self.hawk_roi_gen_config['ROIGenByROICali']['cali_frm_num'])
        self.ui.load_pages.curvature_SpinBox.setValue(self.hawk_roi_gen_config['ROIGenByROICali']['curvature'])
        self.ui.load_pages.roi_correct_ComboBox.setCurrentIndex(
            self.hawk_roi_gen_config['ROIGenByROICali']['roi_correct'])
        self.ui.load_pages.correct_thres_SpinBox.setValue(self.hawk_roi_gen_config['ROIGenByROICali']['correct_thres'])
        self.ui.load_pages.mode_2D_ComboBox.setCurrentIndex(self.hawk_roi_gen_config['ROIGenByROICali']['mode2D'])

    def setup_zone_gui(self):
        # Instans ROI_Zone_Config Win
        self.ui_zone_config_win = ROIZoneConfigWin(self.hawk_config, self.qssStyle)
        self.ui.load_pages.ROIZoneConfig.linkActivated.connect(partial(HawkFunctions.open_roizone_config_win, self))
        self.ui_zone_config_win.return_config_signal.sync_signal.connect(
            partial(HawkFunctions.refresh_hawk_config, self))


    def setup_masking_gui(self):
        # Instans ROI_Zone_Config Win
        self.ui_masking_win = {}
        self.masking_index = 0
        return

    # 文件选择对话框
    # ///////////////////////////////////////////////////////////////
    def base_script_file_sel_func(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='Input',
                                              filter='file(*.txt) ;')
        if file:
            # 选择后缀为.txt
            self.ui.load_pages.base_script_LineEdit.setText(file)
            self.hawk_config['ref_cfg_file'] = file
            logging.info(self.hawk_config['ref_cfg_file'])

    def file_save_dir_sel_func(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择保存的文件路径", "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.ui.load_pages.file_save_dir_LineEdit.setText(dir_path)
            self.hawk_config['ref_cfg_file'] = dir_path
            logging.info(self.hawk_config['ref_cfg_file'])

    def roi_load_file_func(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Cali Data Select', dir='Input',
                                              filter='file(*.txt) ;')
        if file == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.Load_ROI_file_LineEdit.setText(file)
        self.hawk_roi_gen_config['ROIGenByFile']['gen_roi_file'] = file
        # logging.info(self.hawk_config['cali_filename'])

    def base_roi_file_func(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Cali Data Select', dir='Input',
                                              filter='file(*.txt) ;')
        if file == "":
            return
        # 选择后缀为.txt
        self.ui.load_pages.base_roi_file_LineEdit.setText(file)
        self.hawk_roi_gen_config['ROIGenByBaseROI']['base_roi_file'] = file
        # logging.info(self.hawk_config['cali_filename'])

    # 下拉框值更新
    # ///////////////////////////////////////////////////////////////
    def WORK_MODE_UPDATE(self, i):
        self.hawk_config['WORK_MODE'] = self.ui.load_pages.WORK_MODE_ComboBox.get_selected_index()
        # for item in (self.ui.load_pages.WORK_MODE_ComboBox.get_selected()):
        #     logging.info(item.text())
        logging.info(self.hawk_config['WORK_MODE'])

    def SCAN_MODE_UPDATE(self, i):
        self.hawk_config['SCAN_MODE'] = i
        logging.info(self.hawk_config['SCAN_MODE'])

    def MST_MODE_UPDATE(self, i):
        self.hawk_config['MST_MODE'] = i
        logging.info(self.hawk_config['MST_MODE'])

    def TRG_I_EN_UPDATE(self, i):
        self.hawk_config['TRG_I_EN'] = i
        logging.info(self.hawk_config['TRG_I_EN'])

    def MIPI_RATE_UPDATE(self, i):
        select_indexs = self.ui.load_pages.MIPI_RATE_ComboBox.get_selected_index()
        self.hawk_config['MIPI_RATE'] = list(map(lambda i: self.gui_value_config["MIPI_RATE"]["config"][i], select_indexs))
        logging.info(self.hawk_config['MIPI_RATE'])

    def TDC_BIN_W_UPDATE(self, i):
        self.hawk_config['TDC_BIN_W'] = self.gui_value_config["TDC_BIN_W"]["config"][i]
        logging.info(self.hawk_config['TDC_BIN_W'])

    def V_ROLL_NUM_UPDATE(self, num):
        self.hawk_config['V_ROLL_NUM'] = num - 1
        logging.info(self.hawk_config['V_ROLL_NUM'])

    def H_ROLL_NUM_UPDATE(self, num):
        self.hawk_config['H_ROLL_NUM'] = num - 1
        logging.info(self.hawk_config['H_ROLL_NUM'])

    def H_VLD_SEG_UPDATE(self, num):
        self.hawk_config['H_VLD_SEG'] = num - 1
        logging.info(self.hawk_config['H_VLD_SEG'])

    def get_script_config(self):
        self.hawk_config['config_name'] = self.ui.load_pages.REG_CFG_File_LineEdit.text()
        self.hawk_config['roi_name'] = self.ui.load_pages.ROI_SRAM_File_LineEdit.text()
        logging.info(f"{self.hawk_config['config_name']}, {self.hawk_config['roi_name']}")

    def open_roizone_config_win(self, url):
        logging.info("Open ROI zone config window...")
        self.ui_zone_config_win.setModal(True)
        self.ui_zone_config_win.show(self.hawk_config)

    def open_roi_masking_win(self):
        logging.info("ROI Masking display...")
        self.ui_masking_win[self.masking_index] = MaskingWindow()   #TODO：initial need parameter
        self.ui_masking_win[self.masking_index].show()
        self.masking_index = (self.masking_index + 1) % 5

    def refresh_hawk_config(self):
        """从 ROI ZONE config界面获取最新的配置"""
        logging.info("Get the latest configuration")
        self.hawk_config = self.ui_zone_config_win.get_hawk_config()

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

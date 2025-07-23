import copy
import gc

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.windows.main_window.ui_main import UI_MainWindow

from AdapsChip.ChipUI.windows.Swan01 import swan01_window_functions
from AdapsChip.Swan01.Swan01RegConfig import *
from functools import partial
from threading import Thread
from AdapsChip.ChipUI.gui.Signal import MySignals
from SelfDefinedPackge.JsonOperation import JsonFunction
from SelfDefinedPackge.PubMethod import func_exec


class Swan01MainUI:
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
        # Load Swan01 Config
        # ///////////////////////////////////////////////////////////////
        self.Swan01Config = JsonFunction(file_path=".Swan01Config/Swan01Config.json")

        self.swan01_config = self.Swan01Config.items
        self.soft_config = {}

        # All GUI signal sync
        # ///////////////////////////////////////////////////////////////
        self.swan01_main_ui_signal_sync = MySignals()

        # 调用各个界面的 setup_gui, 完成界面初始化
        # ///////////////////////////////////////////////////////////////
        Swan01MainUI.setup_script_gui(self)
        Swan01MainUI.setup_roi_sram_generate_gui(self)
        Swan01MainUI.setup_file_gui(self)
        return

    # ///////////////////////////////////////////////////////////////
    # Script config window function
    # ///////////////////////////////////////////////////////////////
    def setup_script_gui(self):
        # ///////////////////////////////////////////////////////////////
        # 配置初始化, 如果配置文件没有此配置, 需要初始化配置文件
        # ///////////////////////////////////////////////////////////////
        CONFIG_KEYS = []
        for key in CONFIG_KEYS:
            if not (key in self.swan01_config):
                if key == 'WORK_MODE':  # list
                    self.swan01_config[key] = [3]  # PCM MODE
                else:
                    self.swan01_config[key] = 0

        # ///////////////////////////////////////////////////////////////
        # Swan01_ANGLE_GRPx_SLOT_NUM_spinBox 不显示箭头
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.ui.load_pages.Swan01_NS_MAXBIN_THRS_spinBox.setButtonSymbols(QSpinBox.NoButtons)

        # ///////////////////////////////////////////////////////////////
        # WORK_MODE: 针对多选下拉项组件, 需要根据原始数据重新刷新下拉选项
        # ///////////////////////////////////////////////////////////////
        work_mode_items_num = self.ui.load_pages.Swan01_WORK_MODE_ComboBox.count()
        work_mode_items = []
        for index in range(work_mode_items_num):
            item_text = self.ui.load_pages.Swan01_WORK_MODE_ComboBox.itemText(index)
            work_mode_items.append(item_text)
        self.ui.load_pages.Swan01_WORK_MODE_ComboBox.clear_items()
        self.ui.load_pages.Swan01_WORK_MODE_ComboBox.add_items(work_mode_items)

        # ///////////////////////////////////////////////////////////////
        # 设置初始值
        # ///////////////////////////////////////////////////////////////
        # -------------------------------------------
        # SYSC
        # -------------------------------------------
        self.ui.load_pages.Swan01_XCLK_ComboBox.setCurrentIndex(self.swan01_config['XCLK'])
        self.ui.load_pages.Swan01_SYS_CLK_ComboBox.setCurrentIndex(self.swan01_config['SYS_CLK'])
        self.ui.load_pages.Swan01_WORK_MODE_ComboBox.select_indexs(self.swan01_config['WORK_MODE'])
        self.ui.load_pages.Swan01_MIPI_RATE_ComboBox.setCurrentIndex(self.swan01_config['MIPI_RATE'])
        self.ui.load_pages.Swan01_MST_MODE_ComboBox.setCurrentIndex(self.swan01_config['MST_MODE'])
        self.ui.load_pages.Swan01_SYNC_POL_ComboBox.setCurrentIndex(self.swan01_config['SYNC_POL'])
        self.ui.load_pages.Swan01_FRM_SLOT_NUM_spinBox.setValue(self.swan01_config['FRM_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_SEG_NUM_Slider.setValue(self.swan01_config['SEG_NUM'])

        self.ui.load_pages.Swan01_ANGLE_GRP_SW_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP_SW_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP0_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP1_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP2_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP3_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP4_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP5_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP6_SLOT_NUM']+1)
        self.ui.load_pages.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setValue(self.swan01_config['ANGLE_GRP7_SLOT_NUM']+1)

        # -------------------------------------------
        # TRIG
        # -------------------------------------------
        self.ui.load_pages.Swan01_TRG_I_EN_ComboBox.setCurrentIndex(self.swan01_config['TRG_I_EN'])
        self.ui.load_pages.Swan01_FLEX_SHOT_EN_ComboBox.setCurrentIndex(self.swan01_config['FLEX_SHOT_EN'])
        self.ui.load_pages.Swan01_DRV_CHSWTME_spinBox.setValue(self.swan01_config['DRV_CHSWTME'])
        self.ui.load_pages.Swan01_ULR_EN_ComboBox.setCurrentIndex(self.swan01_config['ULR_EN'])
        self.ui.load_pages.Swan01_LSPRD_HOP_EN_ComboBox.setCurrentIndex(self.swan01_config['LSPRD_HOP_EN'])
        self.ui.load_pages.Swan01_LSPRD_HOP_STEP_spinBox.setValue(self.swan01_config['LSPRD_HOP_STEP'])
        self.ui.load_pages.Swan01_LSPRD_HOP_CNTS_spinBox.setValue(self.swan01_config['LSPRD_HOP_CNTS']+1)
        # -------------------------------------------
        # HIST
        # -------------------------------------------
        self.ui.load_pages.Swan01_HIST_MINBIN_THRS_spinBox.setValue(self.swan01_config['HIST_MINBIN_THRS'])
        self.ui.load_pages.Swan01_HIST_MAXBIN_THRS_spinBox.setValue(self.swan01_config['HIST_MAXBIN_THRS'])
        self.ui.load_pages.Swan01_NS_MINBIN_THRS_spinBox.setValue(self.swan01_config['NS_MINBIN_THRS'])
        self.ui.load_pages.Swan01_NS_MAXBIN_THRS_spinBox.setValue(self.swan01_config['NS_MAXBIN_THRS'])
        self.ui.load_pages.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setValue(
            (self.swan01_config['NS_MAXBIN_THRS']-self.swan01_config['NS_MINBIN_THRS']+1)//32)
        self.ui.load_pages.Swan01_HIST_BINFULL_THRS_spinBox.setValue(self.swan01_config['HIST_BINFULL_THRS'])
        self.ui.load_pages.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setValue(self.swan01_config['SPOT_MON_MINBIN_THRS'])

        self.ui.load_pages.Swan01_INTF_DET_EN_ComboBox.setCurrentIndex(self.swan01_config['INTF_DET_EN'])
        self.ui.load_pages.Swan01_INTF_HIST_MODE_ComboBox.setCurrentIndex(self.swan01_config['INTF_HIST_MODE'])
        self.ui.load_pages.Swan01_BIN_WIDTH_SEL_ComboBox.setCurrentIndex(self.swan01_config['BIN_WIDTH_SEL'])
        self.ui.load_pages.Swan01_BIN_WIDTH_MODE_ComboBox.setCurrentIndex(self.swan01_config['BIN_WIDTH_MODE'])

        Swan01MainUI.hist_info_update(self, 0)  # 设置 BIN_NUMBER

        # -------------------------------------------
        # DSP
        # -------------------------------------------
        self.ui.load_pages.Swan01_OUT_NUMBIN_MODE_ComboBox.setCurrentIndex(self.swan01_config['OUT_NUMBIN_MODE'])
        self.ui.load_pages.Swan01_OUT_TOTALBIN_NUM_spinBox.setValue(self.swan01_config['OUT_TOTALBIN_NUM'])
        self.ui.load_pages.Swan01_OUT_ECHO_NUM_ComboBox.setCurrentIndex(self.swan01_config['OUT_ECHO_NUM'])
        self.ui.load_pages.Swan01_OUT_ECHOBIN_NUM_spinBox.setValue(self.swan01_config['OUT_ECHOBIN_NUM'])

        self.ui.load_pages.Swan01_OUT_FIR_RAW_SEL_ComboBox.setCurrentIndex(self.swan01_config['OUT_FIR_RAW_SEL'])
        self.ui.load_pages.Swan01_OUT_INTF_HIST_SEL_ComboBox.setCurrentIndex(self.swan01_config['OUT_INTF_HIST_SEL'])
        self.ui.load_pages.Swan01_OUT_ECHOBIN_MODE_ComboBox.setCurrentIndex(self.swan01_config['OUT_ECHOBIN_MODE'])
        self.ui.load_pages.Swan01_OUT_OVFL_FLAT_EN_ComboBox.setCurrentIndex(self.swan01_config['OUT_OVFL_FLAT_EN'])

        self.ui.load_pages.Swan01_FWHM_HALF_COEF_spinBox.setValue(self.swan01_config['FWHM_HALF_COEF'])
        self.ui.load_pages.Swan01_FWHM_SEARCH_NUM_spinBox.setValue(self.swan01_config['FWHM_SEARCH_NUM'])
        self.ui.load_pages.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setValue(self.swan01_config['ECHO_ORDER_NEAR_NUM'])

        Swan01MainUI.out_totalbin_num_windows_change(self, self.swan01_config['OUT_NUMBIN_MODE'])  # 控件隐藏及显示控制
        Swan01MainUI.out_fir_raw_sel_windows_change(self, self.swan01_config['OUT_FIR_RAW_SEL'])
        Swan01MainUI.dsp_info_update(self, 0)

        # -------------------------------------------
        # TXU
        # -------------------------------------------
        self.ui.load_pages.Swan01_TX_FRM_MODE_ComboBox.setCurrentIndex(self.swan01_config['TX_FRM_MODE'])
        self.ui.load_pages.Swan01_ONE_DT_MODE_ComboBox.setCurrentIndex(self.swan01_config['ONE_DT_MODE'])
        self.ui.load_pages.Swan01_DATA_WIDTH_SEL_ComboBox.setCurrentIndex(self.swan01_config['DATA_WIDTH_SEL'])
        self.ui.load_pages.Swan01_PKT_CHKSUM_EN_ComboBox.setCurrentIndex(self.swan01_config['PKT_CHKSUM_EN'])
        self.ui.load_pages.Swan01_PXL_BINN_SEL_ComboBox.setCurrentIndex(self.swan01_config['PXL_BINN_SEL'])
        self.ui.load_pages.Swan01_PXL_PACK_SEL_ComboBox.setCurrentIndex(self.swan01_config['PXL_PACK_SEL'])

        # -------------------------------------------
        # User define config
        # -------------------------------------------
        self.ui.load_pages.Swan01_user_define_enable_CheckBox.setChecked(self.swan01_config['USER_DEFINE_CONIFG']["USER_DEFINE_CONIFG_ENABLE"])
        self.ui.load_pages.Swan01_user_define_sys_clk_spinBox.setValue(self.swan01_config['USER_DEFINE_CONIFG']["SYS_CLK"])
        self.ui.load_pages.Swan01_user_define_mipi_rate_spinBox.setValue(self.swan01_config['USER_DEFINE_CONIFG']["MIPI_RATE"])
        self.ui.load_pages.Swan01_user_define_mipi_lane_number_spinBox.setValue(self.swan01_config['USER_DEFINE_CONIFG']["MIPI_LANE_NUM"])
        self.ui.load_pages.Swan01_user_define_mipi_pkt_intv_spinBox.setValue(self.swan01_config['USER_DEFINE_CONIFG']["MIPI_PKT_INTV"])
        self.ui.load_pages.Swan01_user_define_mipi_fifo_size_spinBox.setValue(self.swan01_config['USER_DEFINE_CONIFG']["MIPI_FIFO_SIZE"])
        self.ui.load_pages.Swan01_user_define_mipi_pkt_intv_margin_spinBox.setValue(self.swan01_config['USER_DEFINE_CONIFG']["MIPI_PKT_INTV_MARGIN"])

        # ///////////////////////////////////////////////////////////////
        # 操作绑定
        # ///////////////////////////////////////////////////////////////
        # -------------------------------------------
        # SYSC
        # -------------------------------------------
        self.ui.load_pages.Swan01_XCLK_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'XCLK'))
        self.ui.load_pages.Swan01_SYS_CLK_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'SYS_CLK'))
        self.ui.load_pages.Swan01_WORK_MODE_ComboBox.activated.connect(partial(Swan01MainUI.work_mode_update, self))
        self.ui.load_pages.Swan01_MIPI_RATE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'MIPI_RATE'))
        self.ui.load_pages.Swan01_MST_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'MST_MODE'))
        self.ui.load_pages.Swan01_SYNC_POL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'SYNC_POL'))
        self.ui.load_pages.Swan01_SEG_NUM_Slider.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'SEG_NUM', 0))

        self.ui.load_pages.Swan01_ANGLE_GRP_SW_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP_SW_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP0_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP1_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP2_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP3_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP4_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP5_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP6_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ANGLE_GRP7_SLOT_NUM', -1))

        # -------------------------------------------
        # TRIG
        # -------------------------------------------
        self.ui.load_pages.Swan01_TRG_I_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'TRG_I_EN'))
        self.ui.load_pages.Swan01_FLEX_SHOT_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'FLEX_SHOT_EN'))
        self.ui.load_pages.Swan01_DRV_CHSWTME_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "DRV_CHSWTME", 0))
        self.ui.load_pages.Swan01_ULR_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "ULR_EN"))
        self.ui.load_pages.Swan01_LSPRD_HOP_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "LSPRD_HOP_EN"))
        self.ui.load_pages.Swan01_LSPRD_HOP_STEP_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "LSPRD_HOP_STEP", 0))
        self.ui.load_pages.Swan01_LSPRD_HOP_CNTS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "LSPRD_HOP_CNTS", -1))

        # -------------------------------------------
        # HIST
        # -------------------------------------------
        self.ui.load_pages.Swan01_HIST_MINBIN_THRS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "HIST_MINBIN_THRS", 0))
        self.ui.load_pages.Swan01_HIST_MAXBIN_THRS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "HIST_MAXBIN_THRS", 0))
        self.ui.load_pages.Swan01_NS_MINBIN_THRS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "NS_MINBIN_THRS", 0))
        # self.ui.load_pages.Swan01_NS_MAXBIN_THRS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "NS_MAXBIN_THRS", 0))
        self.ui.load_pages.Swan01_NS_CAL_SEG_NUM_SET_spinBox.valueChanged.connect(partial(Swan01MainUI.hist_info_update, self))
        self.ui.load_pages.Swan01_HIST_BINFULL_THRS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "HIST_BINFULL_THRS", 0))
        self.ui.load_pages.Swan01_SPOT_MON_MINBIN_THRS_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "SPOT_MON_MINBIN_THRS", 0))

        self.ui.load_pages.Swan01_INTF_DET_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'INTF_DET_EN'))
        self.ui.load_pages.Swan01_INTF_HIST_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'INTF_HIST_MODE'))
        self.ui.load_pages.Swan01_BIN_WIDTH_SEL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'BIN_WIDTH_SEL'))
        self.ui.load_pages.Swan01_BIN_WIDTH_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'BIN_WIDTH_MODE'))

        # -------------------------------------------
        # DSP
        # -------------------------------------------
        self.ui.load_pages.Swan01_OUT_NUMBIN_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "OUT_NUMBIN_MODE"))
        self.ui.load_pages.Swan01_OUT_TOTALBIN_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "OUT_TOTALBIN_NUM", 0))
        self.ui.load_pages.Swan01_OUT_ECHO_NUM_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "OUT_ECHO_NUM"))
        self.ui.load_pages.Swan01_OUT_ECHOBIN_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "OUT_ECHOBIN_NUM", 0))

        self.ui.load_pages.Swan01_OUT_FIR_RAW_SEL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'OUT_FIR_RAW_SEL'))
        self.ui.load_pages.Swan01_OUT_INTF_HIST_SEL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'OUT_INTF_HIST_SEL'))
        self.ui.load_pages.Swan01_OUT_ECHOBIN_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'OUT_ECHOBIN_MODE'))
        self.ui.load_pages.Swan01_OUT_OVFL_FLAT_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'OUT_OVFL_FLAT_EN'))

        self.ui.load_pages.Swan01_FWHM_HALF_COEF_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'FWHM_HALF_COEF', 0))
        self.ui.load_pages.Swan01_FWHM_SEARCH_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, "FWHM_SEARCH_NUM", 0))
        self.ui.load_pages.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'ECHO_ORDER_NEAR_NUM', 0))

        # -------------------------------------------
        # TXU
        # -------------------------------------------
        self.ui.load_pages.Swan01_TX_FRM_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "TX_FRM_MODE"))
        self.ui.load_pages.Swan01_FRM_SLOT_NUM_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'FRM_SLOT_NUM', -1))
        self.ui.load_pages.Swan01_ONE_DT_MODE_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "ONE_DT_MODE"))
        self.ui.load_pages.Swan01_DATA_WIDTH_SEL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "DATA_WIDTH_SEL"))
        self.ui.load_pages.Swan01_PKT_CHKSUM_EN_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "PKT_CHKSUM_EN"))
        self.ui.load_pages.Swan01_PXL_BINN_SEL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "PXL_BINN_SEL"))
        self.ui.load_pages.Swan01_PXL_PACK_SEL_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, "PXL_PACK_SEL"))

        # -------------------------------------------
        # User define
        # -------------------------------------------
        self.ui.load_pages.Swan01_user_define_enable_CheckBox.stateChanged.connect(partial(Swan01MainUI.switch_user_define_UI, self))
        self.ui.load_pages.Swan01_user_define_sys_clk_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update_user_define, self, "SYS_CLK", 0))
        self.ui.load_pages.Swan01_user_define_mipi_rate_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update_user_define, self, "MIPI_RATE", 0))
        self.ui.load_pages.Swan01_user_define_mipi_lane_number_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update_user_define, self, "MIPI_LANE_NUM", 0))
        self.ui.load_pages.Swan01_user_define_mipi_pkt_intv_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update_user_define, self, "MIPI_PKT_INTV", 0))
        self.ui.load_pages.Swan01_user_define_mipi_fifo_size_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update_user_define, self, "MIPI_FIFO_SIZE", 0))
        self.ui.load_pages.Swan01_user_define_mipi_pkt_intv_margin_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update_user_define, self, "MIPI_PKT_INTV_MARGIN", 0))

        # -------------------------------------------
        # ROI SRAM generate
        # -------------------------------------------
        self.ui.load_pages.Swan01_ScriptGenerateSel.setChecked(True)
        self.ui.load_pages.Swan01_ROIConfig.setHidden(True)
        Swan01MainUI.switch_user_define_UI(self, False)
        return

    # 下拉框值更新
    # ///////////////////////////////////////////////////////////////
    def combobox_data_update(self, key, index):
        self.swan01_config[key] = index
        # print(f"{key}: {self.swan01_config[key]}")
        if key == "OUT_NUMBIN_MODE":
            Swan01MainUI.out_totalbin_num_windows_change(self, index)
        elif key == "OUT_FIR_RAW_SEL":
            Swan01MainUI.out_fir_raw_sel_windows_change(self, index)
        elif key == "PXL_PACK_SEL":
            Swan01MainUI.pxl_pack_sel_windows_change(self, index)
        elif key == "roi_generate_by":
            Swan01MainUI.roi_generate_by_windows_change(self, index)
        # print(self.swan01_config[key])
        return

    # Spinbox & Slider值更新
    # ///////////////////////////////////////////////////////////////
    def value_data_update(self, key, value_shift, value):
        self.swan01_config[key] = value + value_shift
        # print(f"{key}: {self.swan01_config[key]}")

        if key in ["OUT_TOTALBIN_NUM", "OUT_ECHOBIN_NUM", "FWHM_SEARCH_NUM"]:
            Swan01MainUI.dsp_info_update(self, value)
        elif key in ["HIST_MINBIN_THRS", "HIST_MAXBIN_THRS", "NS_MINBIN_THRS", "NS_MAXBIN_THRS", "SPOT_MON_MINBIN_THRS"]:
            Swan01MainUI.hist_info_update(self, value)
        return

    def value_data_update_user_define(self, key, value_shift, value):
        self.swan01_config["USER_DEFINE_CONIFG"][key] = value + value_shift
        # print(f"{key}: {self.swan01_config["USER_DEFINE_CONIFG"][key]}")
        return

    def switch_user_define_UI(self, state):
        state = self.ui.load_pages.Swan01_user_define_enable_CheckBox.isChecked()
        self.swan01_config['USER_DEFINE_CONIFG']["USER_DEFINE_CONIFG_ENABLE"] = state
        self.ui.load_pages.Swan01_user_define_sys_clk_spinBox.setEnabled(state)
        self.ui.load_pages.Swan01_user_define_mipi_rate_spinBox.setEnabled(state)
        self.ui.load_pages.Swan01_user_define_mipi_lane_number_spinBox.setEnabled(state)
        self.ui.load_pages.Swan01_user_define_mipi_pkt_intv_spinBox.setEnabled(state)
        self.ui.load_pages.Swan01_user_define_mipi_fifo_size_spinBox.setEnabled(state)
        self.ui.load_pages.Swan01_user_define_mipi_pkt_intv_margin_spinBox.setEnabled(not state)
        return

    def work_mode_update(self, index):
        self.swan01_config['WORK_MODE'] = self.ui.load_pages.Swan01_WORK_MODE_ComboBox.get_selected_index()
        # print(f"WORK_MODE: {self.swan01_config['WORK_MODE']}")

    def hist_info_update(self, value):
        hist_minbin_thrs = self.swan01_config["HIST_MINBIN_THRS"]
        hist_maxbin_thrs = self.swan01_config["HIST_MAXBIN_THRS"]
        ns_minbin_thrs = self.swan01_config["NS_MINBIN_THRS"]
        ns_cal_seg_num = self.ui.load_pages.Swan01_NS_CAL_SEG_NUM_SET_spinBox.value()

        # bin_number 最小值为 256
        hist_maxbin_min_value = hist_minbin_thrs + 32 - 1   # hist_maxbin_thrs 的最小值
        hist_minbin_max_value = hist_maxbin_thrs - 32 + 1   # hist_minbin_thrs 的最大值

        ns_minbin_thrs_min_value = hist_minbin_thrs         # ns_minbin_thrs 的最小值
        ns_minbin_thrs_max_value = hist_minbin_max_value    # ns_minbin_thrs 的最大值
        ns_minbin_thrs = min(ns_minbin_thrs, hist_minbin_max_value)

        bin_number = (hist_maxbin_thrs - hist_minbin_thrs + 1) * 8      # 计算BIN_NUMBER
        ns_bin_number = (hist_maxbin_thrs - ns_minbin_thrs + 1) * 8     # 计算 Noise BIN_NUMBER

        ns_cal_seg_num_max_value = ns_bin_number // 256     # 计算 Noise 计算可以设置的最大段数

        ns_cal_seg_num = min(ns_cal_seg_num, ns_cal_seg_num_max_value)
        ns_maxbin_thrs = 32 * ns_cal_seg_num + ns_minbin_thrs - 1

        # 设置 HIST_MINBIN_THRS, HIST_MAXBIN_THRS 的交互
        self.ui.load_pages.Swan01_HIST_MINBIN_THRS_spinBox.setMaximum(hist_minbin_max_value)
        self.ui.load_pages.Swan01_HIST_MAXBIN_THRS_spinBox.setMinimum(hist_maxbin_min_value)  # MAXBIN_THRS can't 0

        # 设置 NS_MINBIN_THRS, NS_MAXBIN_THRS 的交互
        self.ui.load_pages.Swan01_NS_MINBIN_THRS_spinBox.setMinimum(ns_minbin_thrs_min_value)
        self.ui.load_pages.Swan01_NS_MINBIN_THRS_spinBox.setMaximum(ns_minbin_thrs_max_value)
        self.ui.load_pages.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setMaximum(ns_cal_seg_num_max_value)

        # 更新 bin_number
        self.ui.load_pages.Swan01_BIN_NUMBER_Value.setNum(bin_number)

        # 更新 NS_MAXBIN_THRS (此值不通过 SpinBox 进行设置, 后端自行计算后填值)
        self.ui.load_pages.Swan01_NS_MAXBIN_THRS_spinBox.setValue(ns_maxbin_thrs)
        self.swan01_config["NS_MAXBIN_THRS"] = ns_maxbin_thrs
        return

    def dsp_info_update(self, value):
        out_totalbin_num = self.swan01_config["OUT_TOTALBIN_NUM"]
        out_echobin_num = self.swan01_config["OUT_ECHOBIN_NUM"]
        fwhm_search_num = self.swan01_config["FWHM_SEARCH_NUM"]

        total_bin_number = out_totalbin_num * 2
        echobin_num = out_echobin_num * 2
        fwhm_search_num_act = (fwhm_search_num+1) * 2
        self.ui.load_pages.Swan01_OUT_TOTALBIN_NUM_Value.setNum(total_bin_number)
        self.ui.load_pages.Swan01_OUT_ECHOBIN_NUM_Value.setNum(echobin_num)
        self.ui.load_pages.Swan01_FWHM_SEARCH_NUM_Value.setNum(fwhm_search_num_act)
        return

    def out_totalbin_num_windows_change(self, index):
        Enable = True if (index == 0) else False
        self.ui.load_pages.Swan01_OUT_TOTALBIN_NUM_spinBox.setEnabled(Enable)
        self.ui.load_pages.Swan01_OUT_ECHO_NUM_ComboBox.setEnabled(not Enable)
        self.ui.load_pages.Swan01_OUT_ECHOBIN_NUM_spinBox.setEnabled(not Enable)
        pass

    def out_fir_raw_sel_windows_change(self, index):
        Enable = True if (index == 0) else False
        self.ui.load_pages.Swan01_OUT_INTF_HIST_SEL_ComboBox.setEnabled(Enable)

        if not Enable:
            self.ui.load_pages.Swan01_OUT_INTF_HIST_SEL_ComboBox.setCurrentIndex(0)
        pass

    def pxl_pack_sel_windows_change(self, index):
        pack_keys = [
            "PACK_2PXL_EN",
            "PACK_4PXL_EN",
            "PACK_8PXL_EN",
            "PACK_16PXL_EN",
            "PACK_16PXL_NUM"
        ]
        for key in pack_keys:
            self.swan01_config[key] = 0

        self.swan01_config["PACK_16PXL_NUM"] = max(0, index-4)
        index = min(4, index)   # 仅更新到 PACK_16PXL_EN
        for i in range(index):
            self.swan01_config[pack_keys[i]] = 1
        pass

    # ///////////////////////////////////////////////////////////////
    # ROI SRAM generate UI
    # ///////////////////////////////////////////////////////////////
    def setup_roi_sram_generate_gui(self):
        # ///////////////////////////////////////////////////////////////
        # 界面初始化
        # ///////////////////////////////////////////////////////////////
        # -------------------------------------------
        # ROI SRAM generate
        # -------------------------------------------
        self.ui.load_pages.Swan01_roi_generate_by_ComboBox.setCurrentIndex(self.swan01_config['roi_generate_by'])
        self.ui.load_pages.Swan01_roi_generate_script_file_sel_LineEdit.setText(self.swan01_config['roi_generate_script_file'])
        self.ui.load_pages.Swan01_roi_generate_excel_sel_LineEdit.setText(self.swan01_config['roi_generate_excel_file'])
        self.ui.load_pages.Swan01_roi_generate_excel_sheet_sel_spinBox.setValue(self.swan01_config["roi_generate_excel_sheet"]+1)
        self.ui.load_pages.Swan01_roi_generate_slot_time_set_enable_CheckBox.setChecked(self.swan01_config["roi_generate_slot_time_set_enable"])
        self.ui.load_pages.Swan01_roi_generate_slot_time_set_spinBox.setValue(self.swan01_config["roi_generate_slot_time_set"])
        self.ui.load_pages.Swan01_roi_save_dir_LineEdit.setText(self.swan01_config['roi_fd_path'])
        self.ui.load_pages.Swan01_roi_sram_name_LineEdit.setText(self.swan01_config['roi_name'])
        # ///////////////////////////////////////////////////////////////
        # 操作绑定
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.Swan01_roi_generate_by_ComboBox.currentIndexChanged.connect(partial(Swan01MainUI.combobox_data_update, self, 'roi_generate_by'))
        self.ui.load_pages.Swan01_roi_generate_excel_sheet_sel_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'roi_generate_excel_sheet', -1))
        self.ui.load_pages.Swan01_roi_generate_slot_time_set_enable_CheckBox.stateChanged.connect(partial(Swan01MainUI.slot_time_set_enable_UI, self))
        self.ui.load_pages.Swan01_roi_generate_slot_time_set_spinBox.valueChanged.connect(partial(Swan01MainUI.value_data_update, self, 'roi_generate_slot_time_set', 0))

        # 按钮绑定
        self.ui.load_pages.Swan01_roi_generate_script_file_sel_Button.clicked.connect(partial(Swan01MainUI.roi_generate_script_file_sel, self))
        self.ui.load_pages.Swan01_roi_generate_excel_sel_Button.clicked.connect(partial(Swan01MainUI.roi_generate_excel_sel, self))
        self.ui.load_pages.Swan01_roi_save_dir_Button.clicked.connect(partial(Swan01MainUI.roi_file_save_dir_sel, self))
        self.ui.load_pages.Swan01_ROI_Save.clicked.connect(partial(Swan01MainUI.roi_sram_Save, self))
        self.ui.load_pages.Swan01_ROI_Open.clicked.connect(partial(Swan01MainUI.open_folder, self, 'roi_fd_path'))

        # -------------------------------------------
        # 界面初始化
        # -------------------------------------------
        Swan01MainUI.roi_generate_by_windows_change(self, self.swan01_config['roi_generate_by'])
        Swan01MainUI.slot_time_set_enable_UI(self, False)
        return

    # ///////////////////////////////////////////////////////////////
    # ROI SRAM generate Function
    # ///////////////////////////////////////////////////////////////
    def roi_generate_script_file_sel(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='',
                                              filter='file(*.txt) ;')
        if file:
            # 选择后缀为.txt
            self.ui.load_pages.Swan01_roi_generate_script_file_sel_LineEdit.setText(file)
            self.swan01_config['roi_generate_script_file'] = file
            print(self.swan01_config['roi_generate_script_file'])

    def roi_generate_excel_sel(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='ROI cali data select', dir='',
                                              filter='file(*.csv *.xls *.xlsx) ;')
        if file:
            # 选择后缀为.txt
            self.ui.load_pages.Swan01_roi_generate_excel_sel_LineEdit.setText(file)
            self.swan01_config['roi_generate_excel_file'] = file
            print(self.swan01_config['roi_generate_excel_file'])

    def roi_file_save_dir_sel(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择保存的文件路径", "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.ui.load_pages.Swan01_roi_save_dir_LineEdit.setText(dir_path)
            self.swan01_config['roi_fd_path'] = dir_path
            # print(self.swan01_config['fd_path'])

    def roi_generate_by_windows_change(self, index):
        Enable = True if (index == 1) else False
        self.ui.load_pages.Swan01_roi_generate_script_file_sel_Button.setEnabled(Enable)
        pass

    def slot_time_set_enable_UI(self, state):
        state = self.ui.load_pages.Swan01_roi_generate_slot_time_set_enable_CheckBox.isChecked()
        self.swan01_config['roi_generate_slot_time_set_enable'] = state
        self.ui.load_pages.Swan01_roi_generate_slot_time_set_spinBox.setEnabled(state)

    def roi_sram_Save(self):
        """
        主界面的保存按钮保存数据, 计算帧率时间
            1. 使用子线程调用保存, 不占用主线程
        """

        def excute():
            # 获取界面配置并 merge 所有配置
            # ///////////////////////////////////////////
            Swan01MainUI.get_roi_generate_file_config(self)
            self.swan01_config["roi_data_format"] = self.soft_config["roi_data_format"]
            swan01_window_functions.ROISramConfigOperation(self.swan01_config)

        self.ui.load_pages.Swan01_ROI_Save.setEnabled(False)

        def threadFunc():
            func_exec(self.DEBUG, excute)
            self.swan01_main_ui_signal_sync.Obj_signal_0.emit(self.ui.load_pages.Swan01_ROI_Save)

        thread = Thread(target=threadFunc)
        thread.start()
        return

    # ///////////////////////////////////////////////////////////////
    # FILE config window function
    # ///////////////////////////////////////////////////////////////
    def setup_file_gui(self):
        """ FILE config 界面GUI配置"""
        self.ui.load_pages.Swan01_reference_script_LineEdit.setText(self.swan01_config['ref_cfg_file'])
        self.ui.load_pages.Swan01_file_save_dir_LineEdit.setText(self.swan01_config['fd_path'])
        self.ui.load_pages.Swan01_reg_script_name_LineEdit.setText(self.swan01_config['reg_name'])

        # 按钮绑定
        self.ui.load_pages.Swan01_reference_script_sel_Button.clicked.connect(partial(Swan01MainUI.reference_script_file_sel, self))
        self.ui.load_pages.Swan01_script_parse_Button.clicked.connect(partial(Swan01MainUI.script_parse, self))
        self.ui.load_pages.Swan01_file_save_dir_Button.clicked.connect(partial(Swan01MainUI.file_save_dir_sel, self))
        self.ui.load_pages.Swan01_slot_read_time_cal_Button.clicked.connect(partial(Swan01MainUI.slot_read_time_cal, self))  # Save按钮连接保存操作
        self.ui.load_pages.Swan01_script_Save.clicked.connect(partial(Swan01MainUI.script_save, self))  # Save按钮连接保存操作
        self.swan01_main_ui_signal_sync.Obj_signal_0.connect(partial(Swan01MainUI.func_btn_release, self))  # 完成保存后, 释放Save按钮
        self.ui.load_pages.Swan01_Open.clicked.connect(partial(Swan01MainUI.open_folder, self, 'fd_path'))
        return

    def reference_script_file_sel(self):
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='',
                                              filter='file(*.txt) ;')
        if file:
            # 选择后缀为.txt
            self.ui.load_pages.Swan01_reference_script_LineEdit.setText(file)
            self.swan01_config['ref_cfg_file'] = file
            print(self.swan01_config['ref_cfg_file'])

    def script_parse(self):
        # Swan01MainUI.merge_swan_config(self)
        file, _ = QFileDialog.getOpenFileName(parent=None, caption='Base script file select', dir='',
                                              filter='file(*.txt) ;')

        def excute():
            swan01_window_functions.ScriptParse(self.swan01_config, file)
        func_exec(self.DEBUG, excute)

    def file_save_dir_sel(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择保存的文件路径", "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.ui.load_pages.Swan01_file_save_dir_LineEdit.setText(dir_path)
            self.swan01_config['fd_path'] = dir_path
            # print(self.swan01_config['fd_path'])

    def script_save(self):
        """
        主界面的保存按钮保存数据: 包含 ROI 数据, Script 数据
            1. 使用子线程调用保存, 不占用主线程
        """

        def excute():
            # 获取界面配置并 merge 所有配置
            # ///////////////////////////////////////////
            Swan01MainUI.get_script_file_config(self)
            swan01_window_functions.ScriptUICoinfigOperate(self.swan01_config, operate=0b010)
            print("Data save complete...")

        self.ui.load_pages.Swan01_script_Save.setEnabled(False)

        def threadFunc():
            func_exec(self.DEBUG, excute)
            self.swan01_main_ui_signal_sync.Obj_signal_0.emit(self.ui.load_pages.Swan01_script_Save)

        thread = Thread(target=threadFunc)
        thread.start()

    def slot_read_time_cal(self):
        """
        主界面的保存按钮保存数据, 计算帧率时间
            1. 使用子线程调用保存, 不占用主线程
        """

        def excute():
            # 获取界面配置并 merge 所有配置
            # ///////////////////////////////////////////
            Swan01MainUI.get_script_file_config(self)
            swan01_window_functions.ScriptUICoinfigOperate(self.swan01_config, operate=0b001)

        self.ui.load_pages.Swan01_slot_read_time_cal_Button.setEnabled(False)

        def threadFunc():
            func_exec(self.DEBUG, excute)
            self.swan01_main_ui_signal_sync.Obj_signal_0.emit(self.ui.load_pages.Swan01_slot_read_time_cal_Button)

        thread = Thread(target=threadFunc)
        thread.start()

    def func_btn_release(self, Obj: QPushButton):
        Obj.setEnabled(True)
        return

    def open_folder(self, T: str):
        folder_path = self.swan01_config[T]
        # 获取用户选择的文件夹路径
        if folder_path:
            # 打开文件夹
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))

    def get_script_file_config(self):
        self.swan01_config['ref_cfg_file'] = self.ui.load_pages.Swan01_reference_script_LineEdit.text()
        self.swan01_config['reg_name'] = self.ui.load_pages.Swan01_reg_script_name_LineEdit.text()
        self.swan01_config['fd_path'] = self.ui.load_pages.Swan01_file_save_dir_LineEdit.text()

    def get_roi_generate_file_config(self):
        self.swan01_config['roi_generate_script_file'] = self.ui.load_pages.Swan01_roi_generate_script_file_sel_LineEdit.text()
        self.swan01_config['roi_generate_excel_file'] = self.ui.load_pages.Swan01_roi_generate_excel_sel_LineEdit.text()
        self.swan01_config['roi_fd_path'] = self.ui.load_pages.Swan01_roi_save_dir_LineEdit.text()
        self.swan01_config['roi_name'] = self.ui.load_pages.Swan01_roi_sram_name_LineEdit.text()

    # ///////////////////////////////////////////////////////////////
    # 通用函数
    # ///////////////////////////////////////////////////////////////
    # 文件选择对话框
    # ///////////////////////////////////////////////////////////////

    def saveImage(self):  # 保存图片到本地
        fd, type = QFileDialog.getSaveFileName(self, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        print(fd)

    def openDirectory(self):  # 打开文件夹（目录）
        fd = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        print(fd)

    def openTextFile(self):  # 选择文本文件上传
        fd, fp = QFileDialog.getOpenFileName(self, "选择文件", "", "*.txt;;All Files(*)")
        print(fd)

    def saveTextFile(self):  # 保存文本文件
        fd, fp = QFileDialog.getSaveFileName(self, "保存文件", "", "*.txt;;All Files(*)")
        print(fd)
        print(fp)

    def closeEvent(self):
        self.Swan01Config.serialize()
        pass

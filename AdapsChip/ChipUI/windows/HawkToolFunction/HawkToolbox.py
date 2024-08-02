import SelfDefinedPackge.ArrayPubMethod
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

from SelfDefinedPackge.MyThread import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.windows.main_window.ui_main import UI_MainWindow
from functools import partial

from AdapsChip.Hawk01.PCM import PcmMipiDataDecode
from AdapsChip.ToolBox import SpadisAppPCMRead
from AdapsChip.ChipUI.gui.Signal import MySignals
import logging


# FUNCTIONS
class HawkToolbox:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()

        # Get config
        # ///////////////////////////////////////////////////////////////
        self.hawk_tool_config = {}

    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        self.dothink_signal = MySignals()

        # set Hawk Toobbox gui
        HawkToolbox.gui_initial(self)
        HawkToolbox.operate_bounding(self)

        # Start initialization
        # ///////////////////////////////////////////////////////////////
        HawkToolbox.FunctionSelect(self, self.hawk_tool_config["func_sel"])
        return

    def gui_initial(self):
        self.ui.load_pages.General_Config.setVisible(False)
        self.ui.load_pages.select_group_01.setVisible(False)
        self.ui.load_pages.select_group_02.setVisible(False)
        self.ui.load_pages.select_group_03.setVisible(False)
        self.ui.load_pages.general_group_01.setVisible(False)
        self.ui.load_pages.general_group_02.setVisible(False)
        self.ui.load_pages.general_group_03.setVisible(False)
        self.ui.load_pages.general_group_04.setVisible(False)
        self.ui.load_pages.file_group_01.setVisible(False)
        self.ui.load_pages.file_group_02.setVisible(False)
        self.ui.load_pages.file_group_03.setVisible(False)
        self.ui.load_pages.file_group_04.setVisible(False)
        self.ui.load_pages.general_operate_Button_01.setVisible(False)
        self.ui.load_pages.general_operate_Button_02.setVisible(False)
        self.ui.load_pages.general_operate_Button_03.setVisible(False)
        self.ui.load_pages.general_operate_Button_04.setVisible(False)
        self.ui.load_pages.general_operate_Button_05.setVisible(False)
        self.ui.load_pages.general_operate_Button_06.setVisible(False)

    def operate_bounding(self):
        self.ui.load_pages.FunctionSelectGroup.buttonClicked.connect(partial(HawkToolbox.FunctionSelectTrigger, self))
        self.ui.load_pages.file_sel_Button_01.clicked.connect(partial(HawkToolbox.file_sel_Button_01_func, self))
        self.ui.load_pages.file_sel_Button_02.clicked.connect(partial(HawkToolbox.file_sel_Button_02_func, self))
        self.ui.load_pages.file_sel_Button_03.clicked.connect(partial(HawkToolbox.file_sel_Button_03_func, self))
        self.ui.load_pages.general_operate_Button_01.clicked.connect(
            partial(HawkToolbox.general_operate_Button_01_func, self))
        self.ui.load_pages.general_operate_Button_02.clicked.connect(
            partial(HawkToolbox.general_operate_Button_02_func, self))
        self.ui.load_pages.general_operate_Button_03.clicked.connect(
            partial(HawkToolbox.general_operate_Button_03_func, self))
        self.ui.load_pages.general_operate_Button_04.clicked.connect(
            partial(HawkToolbox.general_operate_Button_04_func, self))
        self.ui.load_pages.general_operate_Button_05.clicked.connect(
            partial(HawkToolbox.general_operate_Button_05_func, self))
        self.ui.load_pages.general_operate_Button_06.clicked.connect(
            partial(HawkToolbox.general_operate_Button_06_func, self))
        self.dothink_signal.sync_signal_0.connect(
            partial(HawkToolbox.dothink_pcm_imag_array_image, self))

    # QRadioButton bounding function
    # ///////////////////////////////////////////////////////////////
    def FunctionSelectTrigger(self, btn):
        HawkToolbox.FunctionSelect(self, btn.text())

    def FunctionSelect(self, func_name):
        if func_name == "Dothink PCM Imag":
            HawkToolbox.dothink_pcm_imag_setup_gui(self)
            self.ui.load_pages.DothinkPCMImag.setChecked(True)
            # print("Do Dothink PCM Imag")
        elif func_name == "Spadis App PCM READ":
            # print("Do Spadis App PCM READ")
            HawkToolbox.spadis_app_pcm_read_setup_gui(self)
            self.ui.load_pages.SpadisAppPCMREAD.setChecked(True)
        self.hawk_tool_config["func_sel"] = func_name

    def file_sel_Button_01_func(self):
        if self.hawk_tool_config["func_sel"] == "Dothink PCM Imag":
            file = HawkToolbox.Select_single_file(self, title="Script File", ftype="(*.txt)")
            self.ui.load_pages.file_sel_LineEdit_01.setText(file)
        else:
            pass

    def file_sel_Button_02_func(self):
        if self.hawk_tool_config["func_sel"] == "Dothink PCM Imag":
            file = HawkToolbox.Select_single_directory(self, title="Mipi File")
            self.ui.load_pages.file_sel_LineEdit_02.setText(file)
        else:
            pass

    def file_sel_Button_03_func(self):
        if self.hawk_tool_config["func_sel"] == "Dothink PCM Imag":
            file = HawkToolbox.Select_single_directory(self, title="Sramdata Path")
            self.ui.load_pages.file_sel_LineEdit_03.setText(file)
        else:
            pass

    def general_operate_Button_01_func(self):
        if self.hawk_tool_config["func_sel"] == "Dothink PCM Imag":
            HawkToolbox.dothink_pcm_imag_get_array(self)
            # t = threading.Thread(target=HawkToolbox.dothink_pcm_imag_get_array, args=(self, ))
            # t.start()
        elif self.hawk_tool_config["func_sel"] == "Spadis App PCM READ":
            HawkToolbox.spadis_app_pcm_read_operation(self)
        else:
            pass

    def general_operate_Button_02_func(self):
        pass

    def general_operate_Button_03_func(self):
        pass

    def general_operate_Button_04_func(self):
        pass

    def general_operate_Button_05_func(self):
        pass

    def general_operate_Button_06_func(self):
        pass

    # Dothink PCM Imag Function
    # ///////////////////////////////////////////////////////////////
    def dothink_pcm_imag_setup_gui(self):
        HawkToolbox.gui_initial(self)
        self.ui.load_pages.General_Config.setVisible(True)
        self.ui.load_pages.general_group_01.setVisible(True)
        self.ui.load_pages.general_group_02.setVisible(True)
        self.ui.load_pages.file_group_01.setVisible(True)
        self.ui.load_pages.file_group_02.setVisible(True)
        self.ui.load_pages.file_group_03.setVisible(True)
        self.ui.load_pages.general_operate_Button_01.setVisible(True)

        self.ui.load_pages.general_Label_01.setText("Image title")
        self.ui.load_pages.general_Label_02.setText("Color Bar")

        reg = QRegularExpression('[0-9, ]+$')
        validator = QRegularExpressionValidator(reg)
        self.ui.load_pages.general_LineEdit_02.setValidator(validator)

        self.ui.load_pages.file_sel_Label_01.setText("Script File")
        self.ui.load_pages.file_sel_Label_02.setText("Mipi File")
        self.ui.load_pages.file_sel_Label_03.setText("Sramdata Path")

        self.ui.load_pages.general_LineEdit_01.setText(self.hawk_tool_config["DothinkPCMImagValue"]["image_title"])
        self.ui.load_pages.general_LineEdit_02.setText(self.hawk_tool_config["DothinkPCMImagValue"]["color_bar"])
        self.ui.load_pages.file_sel_LineEdit_01.setText(self.hawk_tool_config["DothinkPCMImagValue"]["script_file"])
        self.ui.load_pages.file_sel_LineEdit_02.setText(self.hawk_tool_config["DothinkPCMImagValue"]["mipi_file"])
        self.ui.load_pages.file_sel_LineEdit_03.setText(self.hawk_tool_config["DothinkPCMImagValue"]["sramdata_path"])

        self.ui.load_pages.general_operate_Button_01.setText("Pcm Image")

    def dothink_pcm_imag_get_array(self):
        self.hawk_tool_config["DothinkPCMImagValue"]["image_title"] = self.ui.load_pages.general_LineEdit_01.text()
        self.hawk_tool_config["DothinkPCMImagValue"]["color_bar"] = self.ui.load_pages.general_LineEdit_02.text()
        self.hawk_tool_config["DothinkPCMImagValue"]["script_file"] = self.ui.load_pages.file_sel_LineEdit_01.text()
        self.hawk_tool_config["DothinkPCMImagValue"]["mipi_file"] = self.ui.load_pages.file_sel_LineEdit_02.text()
        self.hawk_tool_config["DothinkPCMImagValue"]["sramdata_path"] = self.ui.load_pages.file_sel_LineEdit_03.text()

        # self.hawk_tool_config["DothinkPCMImagValue"]["array"] = PcmMipiDataDecode.get_pcm_array(
        #     script_file=self.hawk_tool_config["DothinkPCMImagValue"]["script_file"],
        #     mipi_file=self.hawk_tool_config["DothinkPCMImagValue"]["mipi_file"],
        #     sramdata_path=self.hawk_tool_config["DothinkPCMImagValue"]["sramdata_path"]
        # )

        def get_pcm_array():
            try:
                self.pcm_array = PcmMipiDataDecode.get_pcm_array(
                    script_file=self.hawk_tool_config["DothinkPCMImagValue"]["script_file"],
                    mipi_file=self.hawk_tool_config["DothinkPCMImagValue"]["mipi_file"],
                    sramdata_path=self.hawk_tool_config["DothinkPCMImagValue"]["sramdata_path"]
                )
                self.dothink_signal.sync_signal_0.emit()
            except BaseException as msg:
                logging.error(f"解析PCM数据错误: {msg}")

        t = MyThread(get_pcm_array)
        t.start()
        # thread = MyThread(func=PcmMipiDataDecode.get_pcm_array, args=(
        #     self.hawk_tool_config["DothinkPCMImagValue"]["script_file"],
        #     self.hawk_tool_config["DothinkPCMImagValue"]["mipi_file"],
        #     self.hawk_tool_config["DothinkPCMImagValue"]["sramdata_path"]
        # ))
        # thread.start()
        # thread.join()

        # self.hawk_tool_config["DothinkPCMImagValue"]["array"] = thread.get_result()

        # self.hawk_tool_config["DothinkPCMImagValue"]["array"] = np.zeros((100, 100))

    def dothink_pcm_imag_array_image(self):
        title = self.hawk_tool_config["DothinkPCMImagValue"]["image_title"]

        try:
            color_bar = self.hawk_tool_config["DothinkPCMImagValue"]["color_bar"].split(",")
            [vmin, vmax] = list(map(int, color_bar))
        except:
            vmin = None
            vmax = None
        SelfDefinedPackge.ArrayPubMethod.ArrayImage(array_lst=[self.pcm_array], title_list=[title],
                                                    vmin=vmin, vmax=vmax)

    # Spadis App PCM READ Function
    # ///////////////////////////////////////////////////////////////
    def spadis_app_pcm_read_setup_gui(self):
        HawkToolbox.gui_initial(self)
        # self.ui.load_pages.file_group_01.setVisible(True)
        self.ui.load_pages.general_operate_Button_01.setVisible(True)

        # self.ui.load_pages.general_operate_Button_01.setText("File Select")
        self.ui.load_pages.general_operate_Button_01.setText("RAW Image")

    def spadis_app_pcm_read_operation(self):
        raw_file = HawkToolbox.Select_single_file(self, title="Script File", ftype="(*.raw)")
        SpadisAppPCMRead.do_work(raw_file)
        pass

    # File Select function
    # ///////////////////////////////////////////////////////////////
    def Select_single_file(self, title: str, ftype="All Files (*)"):
        file_path, _ = QFileDialog.getOpenFileName(self, title, "", filter=ftype)
        if file_path:
            print(file_path)
        return file_path

    # 选择多个文件
    def Select_multiple_files(self, title: str, ftype="All Files (*)"):
        file_paths, _ = QFileDialog.getOpenFileNames(self, title, "", filter=ftype)
        if file_paths:
            print(file_paths)
        return file_paths

    def Select_single_directory(self, title: str):
        dir_path = QFileDialog.getExistingDirectory(self, title, "", QFileDialog.ShowDirsOnly)
        if dir_path:
            print("选择的目录路径：", dir_path)
        return dir_path

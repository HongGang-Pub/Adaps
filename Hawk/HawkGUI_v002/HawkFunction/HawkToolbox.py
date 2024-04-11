# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys

import SelfDefinedPackge.ArrayPubMethod
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from Hawk.HawkGUI_v002.gui.uis.windows.main_window.ui_main import *
from PySide6.QtGui import QColor, QBrush, QTextCursor
from functools import partial

from Hawk.PCM import PcmMipiDataDecode


# FUNCTIONS
class HawkToolbox:
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
        self.DothinkPCMImagValue = {}

    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # set Hawk Toobbox gui
        self.ui.load_pages.DothinkPCMImag.setChecked(True)
        self.DothinkPCMImagValue = {
            "script_file": "",
            "mipi_file": "",
            "sramdata_path": "",
            "color_bar": "",
            "image_title": "",
            "redraw": True
        }

        HawkToolbox.dothink_pcm_imag(self)
        return

    # QRadioButton bounding function
    # ///////////////////////////////////////////////////////////////
    def FunctionSelect(self, btn):
        if btn.text() == "Dothink PCM Imag":
            HawkToolbox.dothink_pcm_imag(self)
            print("Do Dothink PCM Imag")
        elif btn.text() == "Spadis App PCM READ":
            print("Do Spadis App PCM READ")

    # Dothink PCM Imag Function
    # ///////////////////////////////////////////////////////////////
    def dothink_pcm_imag(self):
        self.ui.load_pages.general_Label_01.setText("Image title")
        self.ui.load_pages.general_Label_02.setText("Color Bar")

        self.ui.load_pages.file_sel_Label_01.setText("Script File")
        self.ui.load_pages.file_sel_Label_02.setText("Mipi File")
        self.ui.load_pages.file_sel_Label_03.setText("Sramdata Path")

        self.ui.load_pages.file_sel_Button_01.clicked.connect(partial(HawkToolbox.dothink_script_file_sel, self))
        self.ui.load_pages.file_sel_Button_02.clicked.connect(partial(HawkToolbox.dothink_mipi_file_sel, self))
        self.ui.load_pages.file_sel_Button_03.clicked.connect(partial(HawkToolbox.dothink_sramdata_file_sel, self))

        self.ui.load_pages.general_operate_Button_01.setText("Pcm Image")

        self.ui.load_pages.general_operate_Button_01.clicked.connect(
            partial(HawkToolbox.dothink_pcm_imag_btn, self))
        pass

    def dothink_script_file_sel(self):
        file = HawkToolbox.Select_single_file(self, title="Script File")
        self.ui.load_pages.file_sel_LineEdit_01.setText(file)
        pass

    def dothink_mipi_file_sel(self):
        file = HawkToolbox.Select_single_directory(self, title="Mipi File")
        self.ui.load_pages.file_sel_LineEdit_02.setText(file)
        pass

    def dothink_sramdata_file_sel(self):
        file = HawkToolbox.Select_single_directory(self, title="Sramdata Path")
        self.ui.load_pages.file_sel_LineEdit_03.setText(file)
        pass

    def dothink_pcm_imag_btn(self):
        def get_input_text():
            self.DothinkPCMImagValue["image_title"] = self.ui.load_pages.general_LineEdit_01.text()
            self.DothinkPCMImagValue["color_bar"] = self.ui.load_pages.general_LineEdit_02.text()

            script_file = self.ui.load_pages.file_sel_LineEdit_01.text()
            mipi_file = self.ui.load_pages.file_sel_LineEdit_02.text()
            sramdata_path = self.ui.load_pages.file_sel_LineEdit_03.text()
            if (script_file != self.DothinkPCMImagValue["script_file"]
                    or self.DothinkPCMImagValue["mipi_file"] != mipi_file
                    or self.DothinkPCMImagValue["sramdata_path"] != sramdata_path):
                self.DothinkPCMImagValue["redraw"] = True
            else:
                self.DothinkPCMImagValue["redraw"] = False
            self.DothinkPCMImagValue["script_file"] = script_file
            self.DothinkPCMImagValue["mipi_file"] = mipi_file
            self.DothinkPCMImagValue["sramdata_path"] = sramdata_path


        get_input_text()

        if self.DothinkPCMImagValue["redraw"] is True:
            self.DothinkPCMImagValue["array"] = PcmMipiDataDecode.get_pcm_array(
                script_file=self.DothinkPCMImagValue["script_file"],
                mipi_file=self.DothinkPCMImagValue["mipi_file"],
                sramdata_path=self.DothinkPCMImagValue["sramdata_path"]
            )
        title = self.DothinkPCMImagValue["image_title"]
        try:
            color_bar = self.DothinkPCMImagValue["color_bar"].split(",")
            [vmin, vmax] = list(map(int, color_bar))
            print(vmin, vmax)
        except:
            vmin = None
            vmax = None

        SelfDefinedPackge.ArrayPubMethod.ArrayImage(array_lst=[self.DothinkPCMImagValue["array"]], title_list=[title], vmin=vmin, vmax=vmax)

    def Select_single_file(self, title: str):
        file_path, _ = QFileDialog.getOpenFileName(self, title, "", filter="All Files (*)")
        if file_path:
            print(file_path)
        return file_path

    # 选择多个文件
    def Select_multiple_files(self, title: str):
        file_paths, _ = QFileDialog.getOpenFileNames(self, title, "", "All Files (*)")
        if file_paths:
            print(file_paths)
        return file_paths

    def Select_single_directory(self, title: str):
        dir_path = QFileDialog.getExistingDirectory(self, title, "", QFileDialog.ShowDirsOnly)
        if dir_path:
            print("选择的目录路径：", dir_path)
        return dir_path

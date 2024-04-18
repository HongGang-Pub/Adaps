import logging
import re
import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from functools import partial
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QSpinBox, QMessageBox, QHeaderView
from Hawk.HawkGUI_v002.gui.uis.pages.ui_roi_zone_config import Ui_ROIZoneConfig
from SelfDefinedPackge.PubMethod import *


class CustomQSB(QSpinBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()

class ROIZoneConfigWin(QDialog, Ui_ROIZoneConfig):
    def __init__(self, qssStyle=None):
        super().__init__()
        self.setupUi(self)  # 运行类函数里的setupUi
        self.setStyleSheet(qssStyle)
        self.ZoneConfigInputTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.zone_config = {
            "SUB_EXPOTIME": {},
            "SUB_IDLETIME": {},
            "EXPO_LASPRD": {},
            "EXPO_PLSWC": {},
            "EXPO_PLSWF": {},
            "TX_EN": {},
            "SPADEN_IN3ROWS": {}
        }

        self.row_type = ("SUB_EXPOTIME", "SUB_IDLETIME", "EXPO_LASPRD", "EXPO_PLSWC", "EXPO_PLSWF",
                         "TX_EN", "SPADEN_IN3ROWS", "MF Kernel")
        self.row_bit_width = (12, 12, 12, 6, 5, 4, 2, 8)

        self.ZoneConfigSel_CheckBox.stateChanged.connect(self.switch_zone_config_sel)
        self.ZoneConfigSel_SpinBox.valueChanged.connect(self.switch_zone_config_sel)
        self.buttonBox.accepted.connect(self.get_zone_config)
        self.setup_gui()

    def setup_gui(self):
        for row in range(23):
            for col in range(32):
                cell = QLineEdit()
                bit_width = self.row_bit_width[row] if row < 7 else self.row_bit_width[7]
                regex_hex = hex_regex_str(bit_width)
                validator = QRegularExpressionValidator(QRegularExpression(regex_hex))
                cell.setValidator(validator)
                cell.setAlignment(Qt.AlignCenter)
                if row == 2:    # 重频周期控制
                    pass
                elif row == 3 or row == 4:    # 曝光时间控制
                    cell.textChanged.connect(partial(self.cal_expotime, col))
                self.ZoneConfigInputTable.setCellWidget(row, col, cell)  # 利用table widget可以装其他组件的方式来实现
                pass

    def gui_initial(self, zone_config):
        self.zone_config = zone_config
        zone_config_sel = self.zone_config["zone_cfg_sel"]
        if zone_config_sel == -1:
            self.ZoneConfigSel_CheckBox.setChecked(True)
            self.ZoneConfigSel_SpinBox.setEnabled(False)
        else:
            self.ZoneConfigSel_CheckBox.setChecked(False)
            self.ZoneConfigSel_SpinBox.setEnabled(True)
            self.ZoneConfigSel_SpinBox.setValue(zone_config_sel+1)
            for col in range(32):
                self.ZoneConfigInputTable.setColumnHidden(col, True)
            self.ZoneConfigInputTable.setColumnHidden(zone_config_sel, False)
        for row in range(23):
            for col in range(32):
                if row >= 7:  # MF_KERNEL config
                    config = self.zone_config[f"Zone_{col}_MF_KN"][row-7]
                else:
                    config = self.zone_config[f"{self.row_type[row]}"][f"Zone{col}"]
                config_hex = hex(config)[2:]
                self.ZoneConfigInputTable.cellWidget(row, col).setText(config_hex)

    def switch_zone_config_sel(self):
        if self.ZoneConfigSel_CheckBox.isChecked():
            self.ZoneConfigSel_SpinBox.setEnabled(False)
            for col in range(32):
                self.ZoneConfigInputTable.setColumnHidden(col, False)
        else:
            self.ZoneConfigSel_SpinBox.setEnabled(True)
            zone_config_sel = self.ZoneConfigSel_SpinBox.value() - 1
            for col in range(32):
                self.ZoneConfigInputTable.setColumnHidden(col, True)
            self.ZoneConfigInputTable.setColumnHidden(zone_config_sel, False)

    def get_zone_config(self):
        if self.ZoneConfigSel_CheckBox.isChecked():
            for row in range(23):
                for col in range(32):
                    _str = self.ZoneConfigInputTable.cellWidget(row, col).text()
                    if _str == "":
                        value = 0
                    else:
                        value = int(self.ZoneConfigInputTable.cellWidget(row, col).text(), 16)
                    if row < 7:
                        self.zone_config[f"{self.row_type[row]}"][f"Zone{col}"] = value
                    else:
                        self.zone_config[f"Zone_{row-7}_MF_KN"][row] = value
            print(self.zone_config)
        pass

    def cal_expotime(self, col, value):
        EXPO_PLSWC = self.ZoneConfigInputTable.cellWidget(3, col).text()
        EXPO_PLSWF = self.ZoneConfigInputTable.cellWidget(4, col).text()
        self.Expotime_Value.setText(f"{EXPO_PLSWC}-{EXPO_PLSWF} ns")

    def show(self, zone_config = None):
        if zone_config is not None:
            self.gui_initial(zone_config)
        super(ROIZoneConfigWin, self).show()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape or event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            event.ignore()
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm', "Are you sure exit this screen?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = r"../gui/themes/page_themes/light/lightstyle.qss"
    with open(styleFile, 'r') as f:
        qssStyle = f.read()
    win = ROIZoneConfigWin(qssStyle)

    win.show()  # 显示窗口
    sys.exit(app.exec())

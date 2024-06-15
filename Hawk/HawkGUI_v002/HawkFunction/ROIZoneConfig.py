import logging
import re
import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from functools import partial
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QSpinBox, QMessageBox, QHeaderView

from Hawk.HawkGUI_v002.gui.uis.pages.ui_roi_zone_config import Ui_ROIZoneConfig
from SelfDefinedPackge.PubMethod import *
from SelfDefinedPackge.JsonOperation import JsonFunction
from Hawk.HawkGUI_v002.gui.Signal import MySignals


class CustomQSB(QSpinBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()


class ROIZoneConfigWin(QDialog, Ui_ROIZoneConfig):
    def __init__(self, hawk_config, qssStyle=None):
        super().__init__()
        self.setupUi(self)  # 运行类函数里的setupUi
        self.setStyleSheet(qssStyle)
        self.is_edit = False
        self.return_config_signal = MySignals()

        self.table_row = self.ZoneConfigInputTable.rowCount()
        self.table_col = self.ZoneConfigInputTable.columnCount()

        # self.ZoneConfigInputTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ZoneConfigInputTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.hawk_config = hawk_config
        self.row_type = ("SUB_EXPOTIME", "SUB_IDLETIME", "EXPO_LASPRD", "EXPO_PLSWC", "EXPO_PLSWF",
                         "TX_EN", "SPADEN_IN3ROWS", "MF Kernel")

        self.ZoneConfigSel_CheckBox.stateChanged.connect(self.switch_zone_config_sel)
        self.ZoneConfigSel_SpinBox.valueChanged.connect(self.switch_zone_config_sel)
        self.EditZoneConifg_Button.clicked.connect(self.zone_config_edit)

        self.ZoneConfigInputTable.cellClicked[int, int].connect(partial(self.oncellClicked))

        self.ZoneConfigInputTable.currentCellChanged.connect(
            partial(self.oncurrentCellChanged))

        # self.OKButton.clicked.connect(self.get_zone_config)
        self.accepted.connect(self.get_zone_config)
        self.setup_gui()

    def setup_gui(self):
        """ 向table中添加控件"""
        row_bit_width = (12, 12, 12, 6, 5, 4, 2, 8)
        for row in range(self.table_row):
            for col in range(self.table_col):
                cell = QLineEdit()
                bit_width = row_bit_width[row] if row < 7 else row_bit_width[7]
                regex_hex = hex_regex_str(bit_width)
                validator = QRegularExpressionValidator(QRegularExpression(regex_hex))
                if row in [2, 3, 4]:    # 重频周期 & 曝光时间控制
                    cell.textChanged.connect(partial(self.cal_expose_value, col))
                cell.setValidator(validator)
                cell.setAlignment(Qt.AlignCenter)
                self.ZoneConfigInputTable.setCellWidget(row, col, cell)  # 利用table widget可以装其他组件的方式来实现
        pass

    def gui_initial(self):
        """初始化显示 GUI"""
        zone_config_sel = self.hawk_config["zone_cfg_sel"]
        if zone_config_sel == -1:
            self.ZoneConfigSel_CheckBox.setChecked(True)
        else:
            self.ZoneConfigSel_CheckBox.setChecked(False)
        self.switch_zone_config_sel()

    def value_initial(self):
        """舒适化显示默认值"""
        for row in range(self.table_row):
            for col in range(self.table_col):
                if row < 7:
                    config = self.hawk_config["zone_cfg_def"][f"{self.row_type[row]}"][f"Zone{col}"]
                else:   # MF_KERNEL config
                    config = self.hawk_config["zone_cfg_def"][f"Zone_{col}_MF_KN"][row - 7]
                config_hex = hex(config)[2:]
                self.ZoneConfigInputTable.cellWidget(row, col).setText(config_hex)

    def switch_zone_config_sel(self):
        if self.ZoneConfigSel_CheckBox.isChecked():
            # 每个zone单独配置UI设置
            self.ZoneConfigSel_SpinBox.setEnabled(False)
            self.hawk_config["zone_cfg_sel"] = -1
            self.cal_expose_value()
            is_enable = True if self.is_edit is True else False
            for col in range(self.table_col):
                self.ZoneConfigInputTable.setColumnWidth(col, 60)
                for row in range(self.table_row):
                    cell = self.ZoneConfigInputTable.cellWidget(row, col)
                    cell.setEnabled(is_enable)
        else:
            # 选择某一个zone配置 UI 设置
            self.ZoneConfigSel_SpinBox.setEnabled(True)
            self.hawk_config["zone_cfg_sel"] = self.ZoneConfigSel_SpinBox.value() - 1
            for col in range(self.table_col):
                # 除了选择列, 其他列设置折叠并不可编辑
                width = 400 if col == self.hawk_config["zone_cfg_sel"] else 10
                isEnable = False if (self.is_edit is False or col!=self.hawk_config["zone_cfg_sel"]) else True

                self.ZoneConfigInputTable.setColumnWidth(col, width)
                for row in range(self.table_row):
                    cell = self.ZoneConfigInputTable.cellWidget(row, col)
                    cell.setEnabled(isEnable)
            self.cal_expose_value(self.hawk_config["zone_cfg_sel"])

    def zone_config_edit(self):
        if self.EditZoneConifg_Button.text() == "Edit":
            self.EditZoneConifg_Button.setText("Lock")
            self.is_edit = True
        else:
            self.EditZoneConifg_Button.setText("Edit")
            self.is_edit = False
        self.switch_zone_config_sel()
        pass

    def oncellClicked(self, row, column):
        # _str = f'row:{row},column:{column},触发信号:{type}'
        # print(_str)
        print("oncellClicked")
        if self.hawk_config["zone_cfg_sel"] != -1:
            column = self.hawk_config["zone_cfg_sel"]
        self.cal_expose_value(col=column)

    def oncurrentCellChanged(self, row, col, pre_row, pre_col):
        print("oncurrentCellChanged")
        self.cal_expose_value(col)

    def get_zone_config(self):
        zone_config_sel = self.hawk_config["zone_cfg_sel"]
        (col_lower, col_upper) = (0, self.table_col) if zone_config_sel == -1 else (zone_config_sel, zone_config_sel+1)
        for row in range(self.table_row):
            for col in range(col_lower, col_upper):
                print("获取数据：", row, col)
                _str = self.ZoneConfigInputTable.cellWidget(row, col).text()
                if _str == "":
                    value = 0
                else:
                    value = int(self.ZoneConfigInputTable.cellWidget(row, col).text(), 16)
                if row < 7:
                    self.hawk_config["zone_cfg_def"][f"{self.row_type[row]}"][f"Zone{col}"] = value
                else:
                    self.hawk_config["zone_cfg_def"][f"Zone_{col}_MF_KN"][row-7] = value
        # print(self.hawk_config)
        self.return_config_signal.sync_signal.emit()
        self.close()
        pass

    def cal_expose_value(self, col=0, value=""):
        EXPO_LASPRD = self.ZoneConfigInputTable.cellWidget(2, col).text()
        EXPO_PLSWC = self.ZoneConfigInputTable.cellWidget(3, col).text()
        EXPO_PLSWF = self.ZoneConfigInputTable.cellWidget(4, col).text()
        self.Expoperiod_Value.setText(f"{col}:{EXPO_LASPRD} ns")
        self.Expotime_Value.setText(f"{col}:{EXPO_PLSWC}-{EXPO_PLSWF} ns")

    def get_hawk_config(self):
        return self.hawk_config

    def show(self, hawk_config=None):
        if hawk_config is not None:
            self.hawk_config = hawk_config
        self.gui_initial()
        self.value_initial()
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

    HawkConfig = JsonFunction(file_path="../.Hawk01Config/HawkConfig.json")
    hawk_config = HawkConfig.items

    win = ROIZoneConfigWin(hawk_config, qssStyle)

    win.show()  # 显示窗口
    sys.exit(app.exec())

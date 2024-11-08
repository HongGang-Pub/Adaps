import logging
import sys
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *

from functools import partial
from AdapsChip.ChipUI.gui.uis.pages.ui_roi_zone_config import Ui_ROIZoneConfig
from SelfDefinedPackge.PubMethod import hex_regex_str
from SelfDefinedPackge.JsonOperation import JsonFunction
from AdapsChip.ChipUI.gui.Signal import MySignals

class ROIZoneConfigWin(QDialog, Ui_ROIZoneConfig):
    def __init__(self, hawk01_zone_config, qssStyle=None):
        super().__init__()
        self.setupUi(self)  # 运行类函数里的setupUi
        self.setWindowTitle("Hawk01 zone config")
        self.setStyleSheet(qssStyle)

        self.return_config_signal = MySignals()

        self.hawk01_SYS_CLK = None
        self.hawk01_PLL1_OD = None

        self.table_row = self.ZoneConfigInputTable.rowCount()
        self.table_col = self.ZoneConfigInputTable.columnCount()

        # 默认可边界, 隐藏编辑/锁定按钮
        self.is_edit = True
        self.EditZoneConifg_Button.hide()
        # self.ZoneConfigInputTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ZoneConfigInputTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.hawk01_zone_config = hawk01_zone_config
        self.zone_cfg_sel = 0
        self.row_type = ("SUB_EXPOTIME", "SUB_IDLETIME", "EXPO_LASPRD", "EXPO_PLSWC", "EXPO_PLSWF",
                         "TX_EN", "SPADEN_IN3ROWS", "MF Kernel")
        self.row_thres = (2 ** 12 - 1, 2 ** 12 - 1, 2 ** 12 - 1, 2 ** 6 - 1, 16, 2 ** 4 - 1, 2 ** 2 - 1, 2 ** 8 - 1)

        self.ZoneConfigSel_CheckBox.stateChanged.connect(self.switch_zone_config_sel)
        self.ZoneConfigSel_SpinBox.valueChanged.connect(self.switch_zone_config_sel)
        self.EditZoneConifg_Button.clicked.connect(self.zone_config_edit)

        # self.ZoneConfigInputTable.cellClicked[int, int].connect(partial(self.oncellClicked))
        self.ZoneConfigInputTable.itemClicked.connect(partial(self.oncellClicked))

        # self.ZoneConfigInputTable.currentCellChanged.connect(partial(self.oncurrentCellChanged))
        self.ZoneConfigInputTable.itemChanged.connect(partial(self.oncurrentCellChanged))
        self.handling_item_change = False  # 初始化处理标志
        self.ui_initial = False

        # self.OKButton.clicked.connect(self.get_zone_config)
        self.accepted.connect(self.get_zone_config)
        # self.setup_gui()

    def setup_gui(self):
        """ 向table中添加控件"""
        row_bit_width = (12, 12, 12, 6, 5, 4, 2, 8)
        for row in range(self.table_row):
            for col in range(self.table_col):
                cell = QLineEdit()
                bit_width = row_bit_width[row] if row < 7 else row_bit_width[7]
                regex_hex = hex_regex_str(bit_width)
                validator = QRegularExpressionValidator(QRegularExpression(regex_hex))
                if row in [2, 3, 4]:  # 重频周期 & 曝光时间控制
                    cell.textChanged.connect(partial(self.cal_expose_value, col))
                cell.setValidator(validator)
                cell.setAlignment(Qt.AlignCenter)
                self.ZoneConfigInputTable.setCellWidget(row, col, cell)  # 利用table widget可以装其他组件的方式来实现
        pass

    def gui_initial(self):
        """初始化显示 GUI"""
        self.zone_cfg_sel = self.hawk01_zone_config["zone_cfg_sel"]
        if self.zone_cfg_sel == -1:
            self.ZoneConfigSel_CheckBox.setChecked(True)  # 独立配置每个分区
        else:
            self.ZoneConfigSel_CheckBox.setChecked(False)  # 使用一个分区的配置配置所有分区
            self.ZoneConfigSel_SpinBox.setValue(self.zone_cfg_sel + 1)
        self.switch_zone_config_sel()

    def value_initial(self):
        """初始化显示默认值"""
        for row in range(self.table_row):
            for col in range(self.table_col):
                self.set_cell_value(row, col)
        self.ui_initial = True

    def set_cell_value(self, row, col):
        if row < 7:
            config = self.hawk01_zone_config["zone_cfg_def"][f"{self.row_type[row]}"][f"Zone{col}"]
        else:  # MF_KERNEL config
            config = self.hawk01_zone_config["zone_cfg_def"][f"Zone_{col}_MF_KN"][row - 7]
        item = QTableWidgetItem(config)
        item.setTextAlignment(Qt.AlignCenter)
        self.ZoneConfigInputTable.setItem(row, col, item)

    def switch_zone_config_sel(self):
        """根据配置动态切换Zone config界面"""
        if self.ZoneConfigSel_CheckBox.isChecked():
            # 每个zone单独配置UI设置
            self.ZoneConfigSel_SpinBox.setEnabled(False)
            self.zone_cfg_sel = -1
            self.cal_expose_value()
            # is_enable = True if self.is_edit is True else False
            for col in range(self.table_col):
                self.ZoneConfigInputTable.setColumnWidth(col, 60)
                for row in range(self.table_row):
                    item = self.ZoneConfigInputTable.item(row, col)
                    if item is None:
                        continue
                    item.setTextAlignment(Qt.AlignCenter)  # 设置居中对齐
                    if not self.is_edit:
                        # item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    else:
                        item.setFlags(item.flags() | Qt.ItemIsEditable)
                    # self.ZoneConfigInputTable.setItem(row, col, item)
                    # cell = self.ZoneConfigInputTable.cellWidget(row, col)
                    # cell.setEnabled(is_enable)
            self.cal_expose_value(0)
        else:
            # 选择某一个zone配置 UI 设置
            self.ZoneConfigSel_SpinBox.setEnabled(True)
            self.zone_cfg_sel = self.ZoneConfigSel_SpinBox.value() - 1
            for col in range(self.table_col):
                # 除了选择列, 其他列设置折叠并不可编辑
                width = 700 if col == self.zone_cfg_sel else 0
                # isEnable = False if (self.is_edit is False or col != self.zone_cfg_sel) else True

                self.ZoneConfigInputTable.setColumnWidth(col, width)
                for row in range(self.table_row):
                    item = self.ZoneConfigInputTable.item(row, col)
                    if item is None:
                        continue
                    item.setTextAlignment(Qt.AlignCenter)  # 设置居中对齐
                    if self.is_edit is False or col != self.zone_cfg_sel:
                        # item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    else:
                        item.setFlags(item.flags() | Qt.ItemIsEditable)
                    # cell = self.ZoneConfigInputTable.cellWidget(row, col)
                    # cell.setEnabled(isEnable)
            self.cal_expose_value(self.zone_cfg_sel)

    def zone_config_edit(self):
        if self.EditZoneConifg_Button.text() == "Edit":
            self.EditZoneConifg_Button.setText("Lock")
            self.is_edit = True
        else:
            self.EditZoneConifg_Button.setText("Edit")
            self.is_edit = False
        self.switch_zone_config_sel()
        pass

    def oncellClicked(self, item):
        """cell 被点击时, 动态计算曝光信息"""
        # print("oncellClicked")
        # print(f"cell_info: row: {item.row()} ,col: {item.column()}")
        col = self.zone_cfg_sel if self.zone_cfg_sel != -1 else item.column()
        self.cal_expose_value(col=col)

    def oncurrentCellChanged(self, item):
        """cell 值改变时, 动态计算曝光信息"""
        # print("oncurrentCellChanged")
        # print(f"cell_info: row: {item.row()} ,col: {item.column()}")
        if self.handling_item_change:  # 检查是否正在处理信号
            return
        self.handling_item_change = True  # 设置处理标志

        row = item.row()
        col = item.column()
        try:
            value = eval(item.text())
            # item.setBackground(Qt.white)  # 如果校验通过，设置背景为白色
            register_thres = self.row_thres[row] if row < 7 else self.row_thres[7]
            if value > register_thres:
                self.set_cell_value(row, col)  # 输入值错误, 回滚到上一个有效值
                QMessageBox.warning(self, "Invalid Input", f"The entered value {value} exceeds the threshold {register_thres}.\n "
                                                           "Please enter it again!!!")
        except BaseException:
            # item.setBackground(Qt.red)  # 如果校验失败，设置背景为红色
            self.set_cell_value(row, col)  # 输入值错误, 回滚到上一个有效值
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number:\n"
                                                       "  1. Decimal Please enter a number directly, such as 100.\n"
                                                       "  2. The binary format is 0b??, such as 0b1001.\n"
                                                       "  3. Thr octal input format is 0o??,such as 0o10.\n"
                                                       "  4. The hexadecimal format is 0x??, such as 0xFF.\n")

        self.handling_item_change = False  # 重置处理标志
        self.cal_expose_value(col)

    def get_zone_config(self):
        """获取界面配置值"""
        self.hawk01_zone_config["zone_cfg_sel"] = self.zone_cfg_sel
        (col_lower, col_upper) = (0, self.table_col) if self.zone_cfg_sel == -1 else (
            self.zone_cfg_sel, self.zone_cfg_sel + 1)
        for row in range(self.table_row):
            for col in range(col_lower, col_upper):
                # print("获取数据：", row, col)
                _str = self.ZoneConfigInputTable.item(row, col).text()
                if row < 7:
                    self.hawk01_zone_config["zone_cfg_def"][f"{self.row_type[row]}"][f"Zone{col}"] = _str
                else:
                    self.hawk01_zone_config["zone_cfg_def"][f"Zone_{col}_MF_KN"][row - 7] = _str
        # print(self.hawk01_config)
        self.return_config_signal.sync_signal_0.emit()
        self.close()
        pass

    def cal_expose_value(self, col=0, value=""):
        try:
            if not self.ui_initial:
                return
            T_sys_clk = 5 if self.hawk01_SYS_CLK == "200M" \
                else 4 if self.hawk01_SYS_CLK == "250M" \
                else 3.03
            T_vco = T_sys_clk / (2 ** (self.hawk01_PLL1_OD + 1))
            EXPO_LASPRD = eval(self.ZoneConfigInputTable.item(2, col).text())
            EXPO_PLSWC = eval(self.ZoneConfigInputTable.item(3, col).text())
            EXPO_PLSWF = eval(self.ZoneConfigInputTable.item(4, col).text())
            # print(EXPO_LASPRD)
            # print(EXPO_PLSWC)
            laser_period = (EXPO_LASPRD + 1) * T_sys_clk
            laser_pluse_width = (EXPO_PLSWC + 1) * T_sys_clk - EXPO_PLSWF * (T_vco / 8)

            self.Laser_Period_Value.setText(f"{laser_period:.2f} ns")
            self.Laser_Pluse_Width_Value.setText(f"{laser_pluse_width:.2f} ns")
        except BaseException as e:
            logging.fatal(f"Error in calculating exposure information: {e}")

    def get_hawk_config(self):
        return self.hawk01_zone_config

    def show(self, hawk_zone_config=None):
        if hawk_zone_config is not None:
            self.hawk01_zone_config = hawk_zone_config
        self.value_initial()
        self.gui_initial()
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

    HawkConfig = JsonFunction(file_path="../../.Hawk01Config/Hawk01Config.json")
    hawk_config = HawkConfig.items

    win = ROIZoneConfigWin(hawk_config, qssStyle)

    win.show()  # 显示窗口
    sys.exit(app.exec())

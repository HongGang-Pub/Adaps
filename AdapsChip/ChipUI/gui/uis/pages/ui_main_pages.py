# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagescgdSUE.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)

from AdapsChip.ChipUI.gui.widgets.py_combo_check_box.py_combo_check import ComboCheckBox
from AdapsChip.ChipUI.gui.widgets.py_nowheel_combobox.py_nowheel_combobox import NoWheelComboBox
from AdapsChip.ChipUI.gui.widgets.py_nowheel_spinbox.py_nowheel_spinbox import NoWheelSpinBox

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(896, 725)
        MainPages.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(MainPages)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        self.pages.setFont(font)
        self.pages.setStyleSheet(u"")
        self.Hawk01 = QWidget()
        self.Hawk01.setObjectName(u"Hawk01")
        self.Hawk01.setFont(font)
        self.Hawk01.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.Hawk01)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 0)
        self.ScriptConfig = QGroupBox(self.Hawk01)
        self.ScriptConfig.setObjectName(u"ScriptConfig")
        self.horizontalLayout_2 = QHBoxLayout(self.ScriptConfig)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.RegisterConfig = QGroupBox(self.ScriptConfig)
        self.RegisterConfig.setObjectName(u"RegisterConfig")
        self.RegisterConfig.setMinimumSize(QSize(0, 0))
        self.RegisterConfig.setMaximumSize(QSize(600, 16777215))
        self.formLayout_2 = QFormLayout(self.RegisterConfig)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(8)
        self.formLayout_2.setContentsMargins(3, 6, 3, 3)
        self.XCLK_Label = QLabel(self.RegisterConfig)
        self.XCLK_Label.setObjectName(u"XCLK_Label")
        self.XCLK_Label.setMinimumSize(QSize(90, 0))
        self.XCLK_Label.setFont(font)
        self.XCLK_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.XCLK_Label)

        self.XCLK_ComboBox = QComboBox(self.RegisterConfig)
        self.XCLK_ComboBox.addItem("")
        self.XCLK_ComboBox.addItem("")
        self.XCLK_ComboBox.setObjectName(u"XCLK_ComboBox")
        self.XCLK_ComboBox.setMinimumSize(QSize(150, 0))
        self.XCLK_ComboBox.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.XCLK_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.XCLK_ComboBox)

        self.MST_MODE_Label = QLabel(self.RegisterConfig)
        self.MST_MODE_Label.setObjectName(u"MST_MODE_Label")
        self.MST_MODE_Label.setMinimumSize(QSize(90, 0))
        self.MST_MODE_Label.setMaximumSize(QSize(85, 16777215))
        self.MST_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.MST_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.MST_MODE_Label)

        self.MST_MODE_ComboBox = QComboBox(self.RegisterConfig)
        self.MST_MODE_ComboBox.addItem("")
        self.MST_MODE_ComboBox.addItem("")
        self.MST_MODE_ComboBox.setObjectName(u"MST_MODE_ComboBox")
        self.MST_MODE_ComboBox.setMaximumSize(QSize(350, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.MST_MODE_ComboBox)

        self.WORK_MODE_Label = QLabel(self.RegisterConfig)
        self.WORK_MODE_Label.setObjectName(u"WORK_MODE_Label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WORK_MODE_Label.sizePolicy().hasHeightForWidth())
        self.WORK_MODE_Label.setSizePolicy(sizePolicy)
        self.WORK_MODE_Label.setMinimumSize(QSize(90, 0))
        self.WORK_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.WORK_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.WORK_MODE_Label.setFrameShadow(QFrame.Raised)
        self.WORK_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.WORK_MODE_Label)

        self.WORK_MODE_ComboBox = ComboCheckBox(self.RegisterConfig)
        self.WORK_MODE_ComboBox.addItem("")
        self.WORK_MODE_ComboBox.addItem("")
        self.WORK_MODE_ComboBox.addItem("")
        self.WORK_MODE_ComboBox.addItem("")
        self.WORK_MODE_ComboBox.setObjectName(u"WORK_MODE_ComboBox")
        self.WORK_MODE_ComboBox.setMaximumSize(QSize(350, 16777215))
        self.WORK_MODE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.WORK_MODE_ComboBox)

        self.MIPI_RATE_Label = QLabel(self.RegisterConfig)
        self.MIPI_RATE_Label.setObjectName(u"MIPI_RATE_Label")
        sizePolicy.setHeightForWidth(self.MIPI_RATE_Label.sizePolicy().hasHeightForWidth())
        self.MIPI_RATE_Label.setSizePolicy(sizePolicy)
        self.MIPI_RATE_Label.setMinimumSize(QSize(90, 0))
        self.MIPI_RATE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.MIPI_RATE_Label.setFont(font1)
        self.MIPI_RATE_Label.setFrameShape(QFrame.StyledPanel)
        self.MIPI_RATE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.MIPI_RATE_Label)

        self.MIPI_RATE_ComboBox = QComboBox(self.RegisterConfig)
        self.MIPI_RATE_ComboBox.addItem("")
        self.MIPI_RATE_ComboBox.addItem("")
        self.MIPI_RATE_ComboBox.addItem("")
        self.MIPI_RATE_ComboBox.addItem("")
        self.MIPI_RATE_ComboBox.setObjectName(u"MIPI_RATE_ComboBox")
        self.MIPI_RATE_ComboBox.setMaximumSize(QSize(350, 16777215))
        self.MIPI_RATE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.MIPI_RATE_ComboBox)

        self.MoreConfiguration = QGroupBox(self.RegisterConfig)
        self.MoreConfiguration.setObjectName(u"MoreConfiguration")
        self.MoreConfiguration.setMinimumSize(QSize(438, 180))
        self.MoreConfiguration.setMaximumSize(QSize(445, 16777215))
        self.MoreConfiguration.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.MoreConfiguration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 3, -1)
        self.V_PXL_OUT_NUM_ComboBox = QComboBox(self.MoreConfiguration)
        self.V_PXL_OUT_NUM_ComboBox.addItem("")
        self.V_PXL_OUT_NUM_ComboBox.addItem("")
        self.V_PXL_OUT_NUM_ComboBox.setObjectName(u"V_PXL_OUT_NUM_ComboBox")

        self.gridLayout.addWidget(self.V_PXL_OUT_NUM_ComboBox, 1, 1, 1, 1)

        self.TRG_I_EN_Label = QLabel(self.MoreConfiguration)
        self.TRG_I_EN_Label.setObjectName(u"TRG_I_EN_Label")
        self.TRG_I_EN_Label.setMinimumSize(QSize(100, 0))
        self.TRG_I_EN_Label.setMaximumSize(QSize(85, 16777215))
        self.TRG_I_EN_Label.setFont(font)
        self.TRG_I_EN_Label.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.TRG_I_EN_Label, 1, 3, 1, 1)

        self.OUT_BIN_NUM_Lable = QLabel(self.MoreConfiguration)
        self.OUT_BIN_NUM_Lable.setObjectName(u"OUT_BIN_NUM_Lable")
        self.OUT_BIN_NUM_Lable.setMinimumSize(QSize(100, 0))
        self.OUT_BIN_NUM_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.OUT_BIN_NUM_Lable.setFont(font)
        self.OUT_BIN_NUM_Lable.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.OUT_BIN_NUM_Lable, 3, 0, 1, 1)

        self.SYS_CLK_Label = QLabel(self.MoreConfiguration)
        self.SYS_CLK_Label.setObjectName(u"SYS_CLK_Label")
        self.SYS_CLK_Label.setMinimumSize(QSize(100, 0))
        self.SYS_CLK_Label.setFont(font)
        self.SYS_CLK_Label.setFrameShape(QFrame.StyledPanel)
        self.SYS_CLK_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.SYS_CLK_Label, 0, 0, 1, 1)

        self.TDC_BIN_W_Label = QLabel(self.MoreConfiguration)
        self.TDC_BIN_W_Label.setObjectName(u"TDC_BIN_W_Label")
        self.TDC_BIN_W_Label.setMinimumSize(QSize(100, 0))
        self.TDC_BIN_W_Label.setMaximumSize(QSize(16777215, 16777215))
        self.TDC_BIN_W_Label.setFont(font)
        self.TDC_BIN_W_Label.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.TDC_BIN_W_Label, 0, 3, 1, 1)

        self.PKS_ECHO_NUM_Lable = QLabel(self.MoreConfiguration)
        self.PKS_ECHO_NUM_Lable.setObjectName(u"PKS_ECHO_NUM_Lable")
        self.PKS_ECHO_NUM_Lable.setMinimumSize(QSize(100, 0))
        self.PKS_ECHO_NUM_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.PKS_ECHO_NUM_Lable.setFont(font)
        self.PKS_ECHO_NUM_Lable.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.PKS_ECHO_NUM_Lable, 3, 3, 1, 1)

        self.MINBIN_THRS_Lable = QLabel(self.MoreConfiguration)
        self.MINBIN_THRS_Lable.setObjectName(u"MINBIN_THRS_Lable")
        self.MINBIN_THRS_Lable.setMinimumSize(QSize(100, 0))
        self.MINBIN_THRS_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.MINBIN_THRS_Lable.setFont(font)
        self.MINBIN_THRS_Lable.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.MINBIN_THRS_Lable, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.PKS_ECHO_NUM_ComboBox = QComboBox(self.MoreConfiguration)
        self.PKS_ECHO_NUM_ComboBox.addItem("")
        self.PKS_ECHO_NUM_ComboBox.addItem("")
        self.PKS_ECHO_NUM_ComboBox.addItem("")
        self.PKS_ECHO_NUM_ComboBox.addItem("")
        self.PKS_ECHO_NUM_ComboBox.addItem("")
        self.PKS_ECHO_NUM_ComboBox.setObjectName(u"PKS_ECHO_NUM_ComboBox")

        self.gridLayout.addWidget(self.PKS_ECHO_NUM_ComboBox, 3, 5, 1, 1)

        self.TDC_BIN_W_ComboBox = QComboBox(self.MoreConfiguration)
        self.TDC_BIN_W_ComboBox.addItem("")
        self.TDC_BIN_W_ComboBox.addItem("")
        self.TDC_BIN_W_ComboBox.addItem("")
        self.TDC_BIN_W_ComboBox.addItem("")
        self.TDC_BIN_W_ComboBox.addItem("")
        self.TDC_BIN_W_ComboBox.addItem("")
        self.TDC_BIN_W_ComboBox.setObjectName(u"TDC_BIN_W_ComboBox")

        self.gridLayout.addWidget(self.TDC_BIN_W_ComboBox, 0, 5, 1, 1)

        self.MAXBIN_THRS_spinBox = QSpinBox(self.MoreConfiguration)
        self.MAXBIN_THRS_spinBox.setObjectName(u"MAXBIN_THRS_spinBox")
        self.MAXBIN_THRS_spinBox.setMinimumSize(QSize(60, 0))
        self.MAXBIN_THRS_spinBox.setMinimum(1)
        self.MAXBIN_THRS_spinBox.setMaximum(167)
        self.MAXBIN_THRS_spinBox.setValue(167)

        self.gridLayout.addWidget(self.MAXBIN_THRS_spinBox, 2, 5, 1, 1)

        self.MAXBIN_THRS_Lable_ = QLabel(self.MoreConfiguration)
        self.MAXBIN_THRS_Lable_.setObjectName(u"MAXBIN_THRS_Lable_")
        self.MAXBIN_THRS_Lable_.setMinimumSize(QSize(100, 0))
        self.MAXBIN_THRS_Lable_.setMaximumSize(QSize(16777215, 16777215))
        self.MAXBIN_THRS_Lable_.setFont(font)
        self.MAXBIN_THRS_Lable_.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.MAXBIN_THRS_Lable_, 2, 3, 1, 1)

        self.V_PXL_OUT_NUM_Label = QLabel(self.MoreConfiguration)
        self.V_PXL_OUT_NUM_Label.setObjectName(u"V_PXL_OUT_NUM_Label")
        self.V_PXL_OUT_NUM_Label.setMinimumSize(QSize(100, 0))
        self.V_PXL_OUT_NUM_Label.setMaximumSize(QSize(85, 16777215))
        self.V_PXL_OUT_NUM_Label.setFont(font)
        self.V_PXL_OUT_NUM_Label.setFrameShape(QFrame.StyledPanel)

        self.gridLayout.addWidget(self.V_PXL_OUT_NUM_Label, 1, 0, 1, 1)

        self.SYS_CLK_ComboBox = QComboBox(self.MoreConfiguration)
        self.SYS_CLK_ComboBox.addItem("")
        self.SYS_CLK_ComboBox.addItem("")
        self.SYS_CLK_ComboBox.addItem("")
        self.SYS_CLK_ComboBox.setObjectName(u"SYS_CLK_ComboBox")
        self.SYS_CLK_ComboBox.setEnabled(False)
        self.SYS_CLK_ComboBox.setMinimumSize(QSize(10, 0))
        self.SYS_CLK_ComboBox.setFont(font1)
        self.SYS_CLK_ComboBox.setEditable(False)

        self.gridLayout.addWidget(self.SYS_CLK_ComboBox, 0, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_24, 1, 2, 1, 1)

        self.TRG_I_EN_ComboBox = QComboBox(self.MoreConfiguration)
        self.TRG_I_EN_ComboBox.addItem("")
        self.TRG_I_EN_ComboBox.addItem("")
        self.TRG_I_EN_ComboBox.setObjectName(u"TRG_I_EN_ComboBox")

        self.gridLayout.addWidget(self.TRG_I_EN_ComboBox, 1, 5, 1, 1)

        self.MINBIN_THRS_spinBox = QSpinBox(self.MoreConfiguration)
        self.MINBIN_THRS_spinBox.setObjectName(u"MINBIN_THRS_spinBox")
        self.MINBIN_THRS_spinBox.setEnabled(True)
        self.MINBIN_THRS_spinBox.setMinimumSize(QSize(60, 0))
        self.MINBIN_THRS_spinBox.setMinimum(0)
        self.MINBIN_THRS_spinBox.setMaximum(255)
        self.MINBIN_THRS_spinBox.setValue(0)

        self.gridLayout.addWidget(self.MINBIN_THRS_spinBox, 2, 1, 1, 1)

        self.OUT_BIN_NUM_ComboBox = QComboBox(self.MoreConfiguration)
        self.OUT_BIN_NUM_ComboBox.addItem("")
        self.OUT_BIN_NUM_ComboBox.addItem("")
        self.OUT_BIN_NUM_ComboBox.setObjectName(u"OUT_BIN_NUM_ComboBox")

        self.gridLayout.addWidget(self.OUT_BIN_NUM_ComboBox, 3, 1, 1, 1)

        self.BIN_NUMBER_Value = QLabel(self.MoreConfiguration)
        self.BIN_NUMBER_Value.setObjectName(u"BIN_NUMBER_Value")
        self.BIN_NUMBER_Value.setMinimumSize(QSize(25, 25))
        self.BIN_NUMBER_Value.setMaximumSize(QSize(20, 16777215))
        self.BIN_NUMBER_Value.setFont(font1)
        self.BIN_NUMBER_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.BIN_NUMBER_Value.setWordWrap(True)
        self.BIN_NUMBER_Value.setMargin(0)

        self.gridLayout.addWidget(self.BIN_NUMBER_Value, 2, 6, 1, 1)


        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.MoreConfiguration)


        self.horizontalLayout_2.addWidget(self.RegisterConfig)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.ROIConfigGroup = QGroupBox(self.ScriptConfig)
        self.ROIConfigGroup.setObjectName(u"ROIConfigGroup")
        self.ROIConfigGroup.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.ROIConfigGroup)
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 6, 3, 0)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(8)
        self.formLayout_3.setContentsMargins(9, 0, 9, 9)
        self.SCAN_MODE_Label = QLabel(self.ROIConfigGroup)
        self.SCAN_MODE_Label.setObjectName(u"SCAN_MODE_Label")
        self.SCAN_MODE_Label.setMinimumSize(QSize(90, 0))
        self.SCAN_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.SCAN_MODE_Label.setFont(font1)
        self.SCAN_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.SCAN_MODE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.SCAN_MODE_Label)

        self.SCAN_MODE_ComboBox = QComboBox(self.ROIConfigGroup)
        self.SCAN_MODE_ComboBox.addItem("")
        self.SCAN_MODE_ComboBox.addItem("")
        self.SCAN_MODE_ComboBox.setObjectName(u"SCAN_MODE_ComboBox")
        self.SCAN_MODE_ComboBox.setMinimumSize(QSize(150, 0))
        self.SCAN_MODE_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.SCAN_MODE_ComboBox.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.SCAN_MODE_ComboBox)

        self.V_ROLL_NUM_Label = QLabel(self.ROIConfigGroup)
        self.V_ROLL_NUM_Label.setObjectName(u"V_ROLL_NUM_Label")
        self.V_ROLL_NUM_Label.setMinimumSize(QSize(90, 0))
        self.V_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.V_ROLL_NUM_Label.setFont(font1)
        self.V_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.V_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.V_ROLL_NUM_Label)

        self.H_ROLL_NUM_Label = QLabel(self.ROIConfigGroup)
        self.H_ROLL_NUM_Label.setObjectName(u"H_ROLL_NUM_Label")
        self.H_ROLL_NUM_Label.setMinimumSize(QSize(90, 0))
        self.H_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_ROLL_NUM_Label.setFont(font1)
        self.H_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.H_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.H_ROLL_NUM_Label)

        self.H_VLD_SEG_Label = QLabel(self.ROIConfigGroup)
        self.H_VLD_SEG_Label.setObjectName(u"H_VLD_SEG_Label")
        self.H_VLD_SEG_Label.setMinimumSize(QSize(90, 0))
        self.H_VLD_SEG_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_VLD_SEG_Label.setFont(font1)
        self.H_VLD_SEG_Label.setFrameShape(QFrame.StyledPanel)
        self.H_VLD_SEG_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.H_VLD_SEG_Label)

        self.H_ROLL_NUM_Frame = QFrame(self.ROIConfigGroup)
        self.H_ROLL_NUM_Frame.setObjectName(u"H_ROLL_NUM_Frame")
        self.H_ROLL_CMP = QHBoxLayout(self.H_ROLL_NUM_Frame)
        self.H_ROLL_CMP.setSpacing(0)
        self.H_ROLL_CMP.setObjectName(u"H_ROLL_CMP")
        self.H_ROLL_CMP.setContentsMargins(0, 0, 0, 0)
        self.H_ROLL_NUM_Slider = QSlider(self.H_ROLL_NUM_Frame)
        self.H_ROLL_NUM_Slider.setObjectName(u"H_ROLL_NUM_Slider")
        self.H_ROLL_NUM_Slider.setEnabled(True)
        self.H_ROLL_NUM_Slider.setMinimum(1)
        self.H_ROLL_NUM_Slider.setMaximum(16)
        self.H_ROLL_NUM_Slider.setPageStep(1)
        self.H_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Slider)

        self.H_ROLL_NUM_Value = QLabel(self.H_ROLL_NUM_Frame)
        self.H_ROLL_NUM_Value.setObjectName(u"H_ROLL_NUM_Value")
        self.H_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.H_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.H_ROLL_NUM_Value.setFont(font1)
        self.H_ROLL_NUM_Value.setMidLineWidth(0)
        self.H_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_ROLL_NUM_Value.setMargin(0)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Value)


        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.H_ROLL_NUM_Frame)

        self.V_ROLL_NUM_Frame = QFrame(self.ROIConfigGroup)
        self.V_ROLL_NUM_Frame.setObjectName(u"V_ROLL_NUM_Frame")
        self.V_ROLL_NUM_CMP = QHBoxLayout(self.V_ROLL_NUM_Frame)
        self.V_ROLL_NUM_CMP.setSpacing(0)
        self.V_ROLL_NUM_CMP.setObjectName(u"V_ROLL_NUM_CMP")
        self.V_ROLL_NUM_CMP.setContentsMargins(0, 0, 0, 0)
        self.V_ROLL_NUM_Slider = QSlider(self.V_ROLL_NUM_Frame)
        self.V_ROLL_NUM_Slider.setObjectName(u"V_ROLL_NUM_Slider")
        self.V_ROLL_NUM_Slider.setMouseTracking(False)
        self.V_ROLL_NUM_Slider.setMinimum(1)
        self.V_ROLL_NUM_Slider.setMaximum(32)
        self.V_ROLL_NUM_Slider.setPageStep(1)
        self.V_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Slider)

        self.V_ROLL_NUM_Value = QLabel(self.V_ROLL_NUM_Frame)
        self.V_ROLL_NUM_Value.setObjectName(u"V_ROLL_NUM_Value")
        self.V_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.V_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.V_ROLL_NUM_Value.setFont(font1)
        self.V_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.V_ROLL_NUM_Value.setWordWrap(True)
        self.V_ROLL_NUM_Value.setMargin(0)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Value)


        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.V_ROLL_NUM_Frame)

        self.H_VLD_SEG_Frame = QFrame(self.ROIConfigGroup)
        self.H_VLD_SEG_Frame.setObjectName(u"H_VLD_SEG_Frame")
        self.H_VLD_SEG_CMP = QHBoxLayout(self.H_VLD_SEG_Frame)
        self.H_VLD_SEG_CMP.setSpacing(0)
        self.H_VLD_SEG_CMP.setObjectName(u"H_VLD_SEG_CMP")
        self.H_VLD_SEG_CMP.setContentsMargins(0, 0, 0, 0)
        self.H_VLD_SEG_Slider = QSlider(self.H_VLD_SEG_Frame)
        self.H_VLD_SEG_Slider.setObjectName(u"H_VLD_SEG_Slider")
        self.H_VLD_SEG_Slider.setMinimum(1)
        self.H_VLD_SEG_Slider.setMaximum(16)
        self.H_VLD_SEG_Slider.setPageStep(1)
        self.H_VLD_SEG_Slider.setOrientation(Qt.Horizontal)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Slider)

        self.H_VLD_SEG_Value = QLabel(self.H_VLD_SEG_Frame)
        self.H_VLD_SEG_Value.setObjectName(u"H_VLD_SEG_Value")
        self.H_VLD_SEG_Value.setMinimumSize(QSize(20, 25))
        self.H_VLD_SEG_Value.setMaximumSize(QSize(20, 16777215))
        self.H_VLD_SEG_Value.setFont(font1)
        self.H_VLD_SEG_Value.setTextFormat(Qt.MarkdownText)
        self.H_VLD_SEG_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_VLD_SEG_Value.setMargin(0)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Value)


        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.H_VLD_SEG_Frame)


        self.verticalLayout_11.addLayout(self.formLayout_3)

        self.ROIConfig = QTabWidget(self.ROIConfigGroup)
        self.ROIConfig.setObjectName(u"ROIConfig")
        self.ROIConfig.setMinimumSize(QSize(0, 0))
        self.ROIConfig.setMaximumSize(QSize(16777215, 16777215))
        self.ROIConfig.setFont(font1)
        self.ROIConfig.setStyleSheet(u"")
        self.ROIConfig.setIconSize(QSize(0, 0))
        self.Config1byGUI = QWidget()
        self.Config1byGUI.setObjectName(u"Config1byGUI")
        self.verticalLayout_3 = QVBoxLayout(self.Config1byGUI)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.scrollArea = QScrollArea(self.Config1byGUI)
        self.scrollArea.setObjectName(u"scrollArea")
        palette = QPalette()
        brush = QBrush(QColor(0, 120, 215, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 332, 322))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 20, 0)
        self.seg_hs_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.seg_hs_Label.setObjectName(u"seg_hs_Label")
        self.seg_hs_Label.setMinimumSize(QSize(100, 0))
        self.seg_hs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.seg_hs_Label.setFont(font1)
        self.seg_hs_Label.setFrameShape(QFrame.StyledPanel)
        self.seg_hs_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.seg_hs_Label)

        self.seg_hs_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_2)
        self.seg_hs_spinBox.setObjectName(u"seg_hs_spinBox")
        self.seg_hs_spinBox.setMinimum(1)
        self.seg_hs_spinBox.setMaximum(16)
        self.seg_hs_spinBox.setValue(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.seg_hs_spinBox)

        self.spad_vs_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.spad_vs_Label.setObjectName(u"spad_vs_Label")
        self.spad_vs_Label.setMinimumSize(QSize(100, 0))
        self.spad_vs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.spad_vs_Label.setFont(font1)
        self.spad_vs_Label.setFrameShape(QFrame.StyledPanel)
        self.spad_vs_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.spad_vs_Label)

        self.spad_vs_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_2)
        self.spad_vs_spinBox.setObjectName(u"spad_vs_spinBox")
        self.spad_vs_spinBox.setMinimum(1)
        self.spad_vs_spinBox.setMaximum(576)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spad_vs_spinBox)

        self.light_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.light_shift_Label.setObjectName(u"light_shift_Label")
        self.light_shift_Label.setMinimumSize(QSize(100, 0))
        self.light_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.light_shift_Label.setFont(font1)
        self.light_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.light_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.light_shift_Label)

        self.light_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_2)
        self.light_shift_spinBox.setObjectName(u"light_shift_spinBox")
        self.light_shift_spinBox.setMinimum(-576)
        self.light_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.light_shift_spinBox)

        self.sublight_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.sublight_shift_Label.setObjectName(u"sublight_shift_Label")
        self.sublight_shift_Label.setMinimumSize(QSize(100, 0))
        self.sublight_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.sublight_shift_Label.setFont(font1)
        self.sublight_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.sublight_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sublight_shift_Label)

        self.sublight_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_2)
        self.sublight_shift_spinBox.setObjectName(u"sublight_shift_spinBox")
        self.sublight_shift_spinBox.setMinimum(-576)
        self.sublight_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sublight_shift_spinBox)

        self.ROI_Shape_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.ROI_Shape_Label.setObjectName(u"ROI_Shape_Label")
        self.ROI_Shape_Label.setMinimumSize(QSize(100, 0))
        self.ROI_Shape_Label.setMaximumSize(QSize(16777215, 16777215))
        self.ROI_Shape_Label.setFont(font1)
        self.ROI_Shape_Label.setFrameShape(QFrame.StyledPanel)
        self.ROI_Shape_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.ROI_Shape_Label)

        self.ROI_Shape_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_2)
        self.ROI_Shape_ComboBox.addItem("")
        self.ROI_Shape_ComboBox.addItem("")
        self.ROI_Shape_ComboBox.setObjectName(u"ROI_Shape_ComboBox")
        self.ROI_Shape_ComboBox.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ROI_Shape_ComboBox)

        self.v_spad_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.v_spad_shift_Label.setObjectName(u"v_spad_shift_Label")
        self.v_spad_shift_Label.setMinimumSize(QSize(100, 0))
        self.v_spad_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.v_spad_shift_Label.setFont(font1)
        self.v_spad_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.v_spad_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.v_spad_shift_Label)

        self.v_spad_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_2)
        self.v_spad_shift_spinBox.setObjectName(u"v_spad_shift_spinBox")
        self.v_spad_shift_spinBox.setMinimum(-576)
        self.v_spad_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.v_spad_shift_spinBox)

        self.h_seg_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.h_seg_shift_Label.setObjectName(u"h_seg_shift_Label")
        self.h_seg_shift_Label.setMinimumSize(QSize(100, 0))
        self.h_seg_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.h_seg_shift_Label.setFont(font1)
        self.h_seg_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.h_seg_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.h_seg_shift_Label)

        self.h_seg_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_2)
        self.h_seg_shift_spinBox.setObjectName(u"h_seg_shift_spinBox")
        self.h_seg_shift_spinBox.setMinimum(0)
        self.h_seg_shift_spinBox.setMaximum(15)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.h_seg_shift_spinBox)

        self.ROI_Retrace_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.ROI_Retrace_Label.setObjectName(u"ROI_Retrace_Label")
        self.ROI_Retrace_Label.setMinimumSize(QSize(100, 0))
        self.ROI_Retrace_Label.setMaximumSize(QSize(16777215, 16777215))
        self.ROI_Retrace_Label.setFont(font1)
        self.ROI_Retrace_Label.setFrameShape(QFrame.StyledPanel)
        self.ROI_Retrace_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.ROI_Retrace_Label)

        self.ROI_Retrace_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_2)
        self.ROI_Retrace_ComboBox.addItem("")
        self.ROI_Retrace_ComboBox.addItem("")
        self.ROI_Retrace_ComboBox.setObjectName(u"ROI_Retrace_ComboBox")
        self.ROI_Retrace_ComboBox.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ROI_Retrace_ComboBox)

        self.sublight_group_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.sublight_group_Label.setObjectName(u"sublight_group_Label")
        self.sublight_group_Label.setMinimumSize(QSize(100, 0))
        self.sublight_group_Label.setMaximumSize(QSize(16777215, 16777215))
        self.sublight_group_Label.setFont(font1)
        self.sublight_group_Label.setFrameShape(QFrame.StyledPanel)
        self.sublight_group_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.sublight_group_Label)

        self.sublight_group_LineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.sublight_group_LineEdit.setObjectName(u"sublight_group_LineEdit")
        self.sublight_group_LineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sublight_group_LineEdit.sizePolicy().hasHeightForWidth())
        self.sublight_group_LineEdit.setSizePolicy(sizePolicy1)
        self.sublight_group_LineEdit.setMinimumSize(QSize(0, 0))
        self.sublight_group_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.sublight_group_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.sublight_group_LineEdit.setReadOnly(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sublight_group_LineEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.ROIConfig.addTab(self.Config1byGUI, "")
        self.Config2byCOOR = QWidget()
        self.Config2byCOOR.setObjectName(u"Config2byCOOR")
        self.verticalLayout_4 = QVBoxLayout(self.Config2byCOOR)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, 0)
        self.scrollArea_2 = QScrollArea(self.Config2byCOOR)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 332, 322))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 20, 0)
        self.Cali_File_Load_Label = QLabel(self.scrollAreaWidgetContents_3)
        self.Cali_File_Load_Label.setObjectName(u"Cali_File_Load_Label")
        self.Cali_File_Load_Label.setMinimumSize(QSize(100, 0))
        self.Cali_File_Load_Label.setFont(font1)
        self.Cali_File_Load_Label.setFrameShape(QFrame.StyledPanel)
        self.Cali_File_Load_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.Cali_File_Load_Label)

        self.Cali_File_Load_Layout = QHBoxLayout()
        self.Cali_File_Load_Layout.setSpacing(9)
        self.Cali_File_Load_Layout.setObjectName(u"Cali_File_Load_Layout")
        self.Cali_File_Load_LineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Cali_File_Load_LineEdit.setObjectName(u"Cali_File_Load_LineEdit")
        self.Cali_File_Load_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Cali_File_Load_LineEdit.sizePolicy().hasHeightForWidth())
        self.Cali_File_Load_LineEdit.setSizePolicy(sizePolicy1)
        self.Cali_File_Load_LineEdit.setMinimumSize(QSize(0, 0))
        self.Cali_File_Load_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Cali_File_Load_LineEdit.setReadOnly(True)

        self.Cali_File_Load_Layout.addWidget(self.Cali_File_Load_LineEdit)

        self.Cali_File_Load_Button = QPushButton(self.scrollAreaWidgetContents_3)
        self.Cali_File_Load_Button.setObjectName(u"Cali_File_Load_Button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Cali_File_Load_Button.sizePolicy().hasHeightForWidth())
        self.Cali_File_Load_Button.setSizePolicy(sizePolicy2)
        self.Cali_File_Load_Button.setFocusPolicy(Qt.WheelFocus)

        self.Cali_File_Load_Layout.addWidget(self.Cali_File_Load_Button)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.Cali_File_Load_Layout)

        self.Excel_Sheet_sel_Label = QLabel(self.scrollAreaWidgetContents_3)
        self.Excel_Sheet_sel_Label.setObjectName(u"Excel_Sheet_sel_Label")
        self.Excel_Sheet_sel_Label.setMinimumSize(QSize(100, 0))
        self.Excel_Sheet_sel_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Excel_Sheet_sel_Label.setFont(font1)
        self.Excel_Sheet_sel_Label.setFrameShape(QFrame.StyledPanel)
        self.Excel_Sheet_sel_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.Excel_Sheet_sel_Label)

        self.Excel_Sheet_sel_spinBox = QSpinBox(self.scrollAreaWidgetContents_3)
        self.Excel_Sheet_sel_spinBox.setObjectName(u"Excel_Sheet_sel_spinBox")
        self.Excel_Sheet_sel_spinBox.setMinimum(1)
        self.Excel_Sheet_sel_spinBox.setMaximum(100)
        self.Excel_Sheet_sel_spinBox.setValue(1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.Excel_Sheet_sel_spinBox)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.ROIConfig.addTab(self.Config2byCOOR, "")
        self.Config3ROIEdit = QWidget()
        self.Config3ROIEdit.setObjectName(u"Config3ROIEdit")
        self.verticalLayout_5 = QVBoxLayout(self.Config3ROIEdit)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.scrollArea_3 = QScrollArea(self.Config3ROIEdit)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 332, 322))
        self.formLayout_5 = QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(10)
        self.formLayout_5.setVerticalSpacing(6)
        self.formLayout_5.setContentsMargins(0, 0, 20, 0)
        self.ROI_File_Label = QLabel(self.scrollAreaWidgetContents_4)
        self.ROI_File_Label.setObjectName(u"ROI_File_Label")
        self.ROI_File_Label.setMinimumSize(QSize(100, 0))
        self.ROI_File_Label.setFont(font1)
        self.ROI_File_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.ROI_File_Label)

        self.ROI_File_Layout = QHBoxLayout()
        self.ROI_File_Layout.setSpacing(9)
        self.ROI_File_Layout.setObjectName(u"ROI_File_Layout")
        self.ROI_File_LineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.ROI_File_LineEdit.setObjectName(u"ROI_File_LineEdit")
        self.ROI_File_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ROI_File_LineEdit.sizePolicy().hasHeightForWidth())
        self.ROI_File_LineEdit.setSizePolicy(sizePolicy1)
        self.ROI_File_LineEdit.setMinimumSize(QSize(0, 0))
        self.ROI_File_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.ROI_File_LineEdit.setReadOnly(True)

        self.ROI_File_Layout.addWidget(self.ROI_File_LineEdit)

        self.ROI_File_Button = QPushButton(self.scrollAreaWidgetContents_4)
        self.ROI_File_Button.setObjectName(u"ROI_File_Button")
        sizePolicy2.setHeightForWidth(self.ROI_File_Button.sizePolicy().hasHeightForWidth())
        self.ROI_File_Button.setSizePolicy(sizePolicy2)
        self.ROI_File_Button.setFocusPolicy(Qt.WheelFocus)

        self.ROI_File_Layout.addWidget(self.ROI_File_Button)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.ROI_File_Layout)

        self.Start_Rolling_Label = QLabel(self.scrollAreaWidgetContents_4)
        self.Start_Rolling_Label.setObjectName(u"Start_Rolling_Label")
        self.Start_Rolling_Label.setMinimumSize(QSize(100, 0))
        self.Start_Rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Start_Rolling_Label.setFont(font1)
        self.Start_Rolling_Label.setFrameShape(QFrame.StyledPanel)
        self.Start_Rolling_Label.setFrameShadow(QFrame.Raised)
        self.Start_Rolling_Label.setTextFormat(Qt.PlainText)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.Start_Rolling_Label)

        self.End_Rolling_Label = QLabel(self.scrollAreaWidgetContents_4)
        self.End_Rolling_Label.setObjectName(u"End_Rolling_Label")
        self.End_Rolling_Label.setMinimumSize(QSize(100, 0))
        self.End_Rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.End_Rolling_Label.setFont(font1)
        self.End_Rolling_Label.setFrameShape(QFrame.StyledPanel)
        self.End_Rolling_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.End_Rolling_Label)

        self.End_Rolling_SpinBox = QSpinBox(self.scrollAreaWidgetContents_4)
        self.End_Rolling_SpinBox.setObjectName(u"End_Rolling_SpinBox")
        self.End_Rolling_SpinBox.setMinimum(1)
        self.End_Rolling_SpinBox.setMaximum(32)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.End_Rolling_SpinBox)

        self.Start_Rolling_SpinBox = QSpinBox(self.scrollAreaWidgetContents_4)
        self.Start_Rolling_SpinBox.setObjectName(u"Start_Rolling_SpinBox")
        self.Start_Rolling_SpinBox.setMinimum(1)
        self.Start_Rolling_SpinBox.setMaximum(32)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.Start_Rolling_SpinBox)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.scrollArea_3)

        self.ROIConfig.addTab(self.Config3ROIEdit, "")
        self.Config4ROICali = QWidget()
        self.Config4ROICali.setObjectName(u"Config4ROICali")
        self.verticalLayout_2 = QVBoxLayout(self.Config4ROICali)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_5 = QScrollArea(self.Config4ROICali)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"")
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 332, 313))
        self.formLayout_7 = QFormLayout(self.scrollAreaWidgetContents_6)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(10)
        self.formLayout_7.setVerticalSpacing(6)
        self.formLayout_7.setContentsMargins(0, 0, 20, 0)
        self.cali_file_path_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.cali_file_path_Label.setObjectName(u"cali_file_path_Label")
        self.cali_file_path_Label.setMinimumSize(QSize(100, 0))
        self.cali_file_path_Label.setFont(font1)
        self.cali_file_path_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.cali_file_path_Label)

        self.cali_file_path_Layout = QHBoxLayout()
        self.cali_file_path_Layout.setSpacing(9)
        self.cali_file_path_Layout.setObjectName(u"cali_file_path_Layout")
        self.cali_file_path_LineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.cali_file_path_LineEdit.setObjectName(u"cali_file_path_LineEdit")
        self.cali_file_path_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cali_file_path_LineEdit.sizePolicy().hasHeightForWidth())
        self.cali_file_path_LineEdit.setSizePolicy(sizePolicy1)
        self.cali_file_path_LineEdit.setMinimumSize(QSize(0, 0))
        self.cali_file_path_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.cali_file_path_LineEdit.setReadOnly(True)

        self.cali_file_path_Layout.addWidget(self.cali_file_path_LineEdit)

        self.cali_file_path_Button = QPushButton(self.scrollAreaWidgetContents_6)
        self.cali_file_path_Button.setObjectName(u"cali_file_path_Button")
        sizePolicy2.setHeightForWidth(self.cali_file_path_Button.sizePolicy().hasHeightForWidth())
        self.cali_file_path_Button.setSizePolicy(sizePolicy2)
        self.cali_file_path_Button.setFocusPolicy(Qt.WheelFocus)

        self.cali_file_path_Layout.addWidget(self.cali_file_path_Button)


        self.formLayout_7.setLayout(0, QFormLayout.FieldRole, self.cali_file_path_Layout)

        self.img_mirror_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.img_mirror_Label.setObjectName(u"img_mirror_Label")
        self.img_mirror_Label.setMinimumSize(QSize(100, 0))
        self.img_mirror_Label.setFont(font1)
        self.img_mirror_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.img_mirror_Label)

        self.img_mirror_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_6)
        self.img_mirror_ComboBox.addItem("")
        self.img_mirror_ComboBox.addItem("")
        self.img_mirror_ComboBox.addItem("")
        self.img_mirror_ComboBox.addItem("")
        self.img_mirror_ComboBox.setObjectName(u"img_mirror_ComboBox")
        self.img_mirror_ComboBox.setMinimumSize(QSize(150, 0))
        self.img_mirror_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.img_mirror_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.img_mirror_ComboBox)

        self.remove_noise_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.remove_noise_Label.setObjectName(u"remove_noise_Label")
        self.remove_noise_Label.setMinimumSize(QSize(100, 0))
        self.remove_noise_Label.setFont(font1)
        self.remove_noise_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.remove_noise_Label)

        self.remove_noise_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_6)
        self.remove_noise_ComboBox.addItem("")
        self.remove_noise_ComboBox.addItem("")
        self.remove_noise_ComboBox.setObjectName(u"remove_noise_ComboBox")
        self.remove_noise_ComboBox.setMinimumSize(QSize(150, 0))
        self.remove_noise_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.remove_noise_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.remove_noise_ComboBox)

        self.light_smooth_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.light_smooth_Label.setObjectName(u"light_smooth_Label")
        self.light_smooth_Label.setMinimumSize(QSize(100, 0))
        self.light_smooth_Label.setFont(font1)
        self.light_smooth_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.light_smooth_Label)

        self.light_smooth_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_6)
        self.light_smooth_ComboBox.addItem("")
        self.light_smooth_ComboBox.addItem("")
        self.light_smooth_ComboBox.setObjectName(u"light_smooth_ComboBox")
        self.light_smooth_ComboBox.setMinimumSize(QSize(150, 0))
        self.light_smooth_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.light_smooth_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.light_smooth_ComboBox)

        self.curvature_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.curvature_Label.setObjectName(u"curvature_Label")
        self.curvature_Label.setMinimumSize(QSize(100, 0))
        self.curvature_Label.setFont(font1)
        self.curvature_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.curvature_Label)

        self.curvature_SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_6)
        self.curvature_SpinBox.setObjectName(u"curvature_SpinBox")
        self.curvature_SpinBox.setMinimum(0)
        self.curvature_SpinBox.setMaximum(1000)
        self.curvature_SpinBox.setValue(2)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.curvature_SpinBox)

        self.correct_thres_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.correct_thres_Label.setObjectName(u"correct_thres_Label")
        self.correct_thres_Label.setMinimumSize(QSize(100, 0))
        self.correct_thres_Label.setFont(font1)
        self.correct_thres_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.correct_thres_Label)

        self.correct_thres_SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_6)
        self.correct_thres_SpinBox.setObjectName(u"correct_thres_SpinBox")
        self.correct_thres_SpinBox.setMinimum(0)
        self.correct_thres_SpinBox.setMaximum(100)
        self.correct_thres_SpinBox.setValue(1)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.correct_thres_SpinBox)

        self.cali_order_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.cali_order_Label.setObjectName(u"cali_order_Label")
        self.cali_order_Label.setMinimumSize(QSize(100, 0))
        self.cali_order_Label.setFont(font1)
        self.cali_order_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.cali_order_Label)

        self.cali_order_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_6)
        self.cali_order_ComboBox.addItem("")
        self.cali_order_ComboBox.addItem("")
        self.cali_order_ComboBox.setObjectName(u"cali_order_ComboBox")
        self.cali_order_ComboBox.setMinimumSize(QSize(150, 0))
        self.cali_order_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.cali_order_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.cali_order_ComboBox)

        self.cali_frm_num_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.cali_frm_num_Label.setObjectName(u"cali_frm_num_Label")
        self.cali_frm_num_Label.setMinimumSize(QSize(100, 0))
        self.cali_frm_num_Label.setFont(font1)
        self.cali_frm_num_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.cali_frm_num_Label)

        self.cali_frm_num__SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_6)
        self.cali_frm_num__SpinBox.setObjectName(u"cali_frm_num__SpinBox")
        self.cali_frm_num__SpinBox.setMinimum(1)
        self.cali_frm_num__SpinBox.setMaximum(10000)

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.cali_frm_num__SpinBox)

        self.ref_segment_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.ref_segment_Label.setObjectName(u"ref_segment_Label")
        self.ref_segment_Label.setMinimumSize(QSize(100, 0))
        self.ref_segment_Label.setFont(font1)
        self.ref_segment_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.ref_segment_Label)

        self.ref_segment_SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_6)
        self.ref_segment_SpinBox.setObjectName(u"ref_segment_SpinBox")
        self.ref_segment_SpinBox.setMinimum(0)
        self.ref_segment_SpinBox.setMaximum(16)
        self.ref_segment_SpinBox.setValue(0)

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.ref_segment_SpinBox)

        self.mode_2D_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.mode_2D_Label.setObjectName(u"mode_2D_Label")
        self.mode_2D_Label.setMinimumSize(QSize(100, 0))
        self.mode_2D_Label.setFont(font1)
        self.mode_2D_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.mode_2D_Label)

        self.mode_2D_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_6)
        self.mode_2D_ComboBox.addItem("")
        self.mode_2D_ComboBox.addItem("")
        self.mode_2D_ComboBox.setObjectName(u"mode_2D_ComboBox")
        self.mode_2D_ComboBox.setMinimumSize(QSize(150, 0))
        self.mode_2D_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.mode_2D_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(9, QFormLayout.FieldRole, self.mode_2D_ComboBox)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_2.addWidget(self.scrollArea_5)

        self.ROIConfig.addTab(self.Config4ROICali, "")

        self.verticalLayout_11.addWidget(self.ROIConfig)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, 3)
        self.ROIZoneConfig = QLabel(self.ROIConfigGroup)
        self.ROIZoneConfig.setObjectName(u"ROIZoneConfig")
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush1)
        self.ROIZoneConfig.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.ROIZoneConfig.setFont(font2)
        self.ROIZoneConfig.setStyleSheet(u"QLabel {\n"
"font: 700 9pt \"Consolas\";\n"
"}")
        self.ROIZoneConfig.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ROIZoneConfig.setMargin(0)
        self.ROIZoneConfig.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.ROIZoneConfig)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_18)

        self.ROIView = QPushButton(self.ROIConfigGroup)
        self.ROIView.setObjectName(u"ROIView")
        self.ROIView.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.ROIView)

        self.ROISave = QPushButton(self.ROIConfigGroup)
        self.ROISave.setObjectName(u"ROISave")
        self.ROISave.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.ROISave)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.ROIConfigGroup)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_12.addWidget(self.ScriptConfig)

        self.FileConifg = QGroupBox(self.Hawk01)
        self.FileConifg.setObjectName(u"FileConifg")
        self.FileConifg.setMinimumSize(QSize(300, 0))
        self.FileConifg.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_6 = QGridLayout(self.FileConifg)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 9, 9, 1)
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 4, 4, 1, 1)

        self.roi_sram_name_Label = QLabel(self.FileConifg)
        self.roi_sram_name_Label.setObjectName(u"roi_sram_name_Label")
        self.roi_sram_name_Label.setFont(font)

        self.gridLayout_6.addWidget(self.roi_sram_name_Label, 4, 0, 1, 1)

        self.reg_script_name_LineEdit = QLineEdit(self.FileConifg)
        self.reg_script_name_LineEdit.setObjectName(u"reg_script_name_LineEdit")
        self.reg_script_name_LineEdit.setMinimumSize(QSize(0, 0))
        self.reg_script_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.reg_script_name_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.reg_script_name_LineEdit, 2, 1, 1, 1)

        self.file_save_dir_Label = QLabel(self.FileConifg)
        self.file_save_dir_Label.setObjectName(u"file_save_dir_Label")
        self.file_save_dir_Label.setMinimumSize(QSize(0, 0))
        self.file_save_dir_Label.setMaximumSize(QSize(16777215, 16777215))
        self.file_save_dir_Label.setFont(font1)
        self.file_save_dir_Label.setFrameShape(QFrame.NoFrame)
        self.file_save_dir_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.file_save_dir_Label, 6, 0, 1, 1)

        self.reference_script_sel_Button = QPushButton(self.FileConifg)
        self.reference_script_sel_Button.setObjectName(u"reference_script_sel_Button")
        sizePolicy2.setHeightForWidth(self.reference_script_sel_Button.sizePolicy().hasHeightForWidth())
        self.reference_script_sel_Button.setSizePolicy(sizePolicy2)
        self.reference_script_sel_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.reference_script_sel_Button, 1, 2, 1, 1)

        self.roi_sram_name_CheckBox = QCheckBox(self.FileConifg)
        self.roi_sram_name_CheckBox.setObjectName(u"roi_sram_name_CheckBox")

        self.gridLayout_6.addWidget(self.roi_sram_name_CheckBox, 4, 3, 1, 1)

        self.roi_sram_name_LineEdit = QLineEdit(self.FileConifg)
        self.roi_sram_name_LineEdit.setObjectName(u"roi_sram_name_LineEdit")
        self.roi_sram_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.roi_sram_name_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.roi_sram_name_LineEdit, 4, 1, 1, 1)

        self.reference_script_LineEdit = QLineEdit(self.FileConifg)
        self.reference_script_LineEdit.setObjectName(u"reference_script_LineEdit")
        self.reference_script_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.reference_script_LineEdit.sizePolicy().hasHeightForWidth())
        self.reference_script_LineEdit.setSizePolicy(sizePolicy1)
        self.reference_script_LineEdit.setMinimumSize(QSize(0, 0))
        self.reference_script_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.reference_script_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.reference_script_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.reference_script_LineEdit, 1, 1, 1, 1)

        self.horizontalFrame = QFrame(self.FileConifg)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 2, -1, -1)
        self.Save = QPushButton(self.horizontalFrame)
        self.Save.setObjectName(u"Save")
        sizePolicy1.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy1)
        self.Save.setMinimumSize(QSize(90, 0))
        self.Save.setFont(font)
        self.Save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.Save)

        self.Open = QPushButton(self.horizontalFrame)
        self.Open.setObjectName(u"Open")
        sizePolicy1.setHeightForWidth(self.Open.sizePolicy().hasHeightForWidth())
        self.Open.setSizePolicy(sizePolicy1)
        self.Open.setMinimumSize(QSize(90, 0))
        self.Open.setFont(font)
        self.Open.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.Open)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout_6.addWidget(self.horizontalFrame, 7, 0, 1, 5)

        self.reference_script_Label = QLabel(self.FileConifg)
        self.reference_script_Label.setObjectName(u"reference_script_Label")
        self.reference_script_Label.setMinimumSize(QSize(0, 0))
        self.reference_script_Label.setMaximumSize(QSize(16777215, 16777215))
        self.reference_script_Label.setFont(font1)
        self.reference_script_Label.setFrameShape(QFrame.NoFrame)
        self.reference_script_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.reference_script_Label, 1, 0, 1, 1)

        self.file_save_dir_LineEdit = QLineEdit(self.FileConifg)
        self.file_save_dir_LineEdit.setObjectName(u"file_save_dir_LineEdit")
        self.file_save_dir_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_save_dir_LineEdit.sizePolicy().hasHeightForWidth())
        self.file_save_dir_LineEdit.setSizePolicy(sizePolicy1)
        self.file_save_dir_LineEdit.setMinimumSize(QSize(350, 0))
        self.file_save_dir_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.file_save_dir_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.file_save_dir_LineEdit.setReadOnly(False)

        self.gridLayout_6.addWidget(self.file_save_dir_LineEdit, 6, 1, 1, 1)

        self.file_save_dir_Button = QPushButton(self.FileConifg)
        self.file_save_dir_Button.setObjectName(u"file_save_dir_Button")
        sizePolicy2.setHeightForWidth(self.file_save_dir_Button.sizePolicy().hasHeightForWidth())
        self.file_save_dir_Button.setSizePolicy(sizePolicy2)
        self.file_save_dir_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.file_save_dir_Button, 6, 2, 1, 1)

        self.reg_script_name_Label = QLabel(self.FileConifg)
        self.reg_script_name_Label.setObjectName(u"reg_script_name_Label")
        self.reg_script_name_Label.setFont(font)

        self.gridLayout_6.addWidget(self.reg_script_name_Label, 2, 0, 1, 1)

        self.reference_script_parse_Button = QPushButton(self.FileConifg)
        self.reference_script_parse_Button.setObjectName(u"reference_script_parse_Button")
        sizePolicy2.setHeightForWidth(self.reference_script_parse_Button.sizePolicy().hasHeightForWidth())
        self.reference_script_parse_Button.setSizePolicy(sizePolicy2)
        self.reference_script_parse_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.reference_script_parse_Button, 1, 3, 1, 1)


        self.verticalLayout_12.addWidget(self.FileConifg)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.pages.addWidget(self.Hawk01)
        self.Toolbox = QWidget()
        self.Toolbox.setObjectName(u"Toolbox")
        self.Toolbox.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.Toolbox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 0)
        self.title_label_2 = QLabel(self.Toolbox)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(16)
        self.title_label_2.setFont(font3)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.title_label_2)

        self.FunctionWindow = QGroupBox(self.Toolbox)
        self.FunctionWindow.setObjectName(u"FunctionWindow")
        self.verticalLayout_8 = QVBoxLayout(self.FunctionWindow)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.FunctionSelectWin = QGroupBox(self.FunctionWindow)
        self.FunctionSelectWin.setObjectName(u"FunctionSelectWin")
        self.FunctionSelectWin.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.FunctionSelectWin)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.SpadisAppPCMREAD = QRadioButton(self.FunctionSelectWin)
        self.FunctionSelectGroup = QButtonGroup(MainPages)
        self.FunctionSelectGroup.setObjectName(u"FunctionSelectGroup")
        self.FunctionSelectGroup.addButton(self.SpadisAppPCMREAD)
        self.SpadisAppPCMREAD.setObjectName(u"SpadisAppPCMREAD")

        self.gridLayout_2.addWidget(self.SpadisAppPCMREAD, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.DothinkPCMImag = QRadioButton(self.FunctionSelectWin)
        self.FunctionSelectGroup.addButton(self.DothinkPCMImag)
        self.DothinkPCMImag.setObjectName(u"DothinkPCMImag")

        self.gridLayout_2.addWidget(self.DothinkPCMImag, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.FunctionSelectWin)

        self.General_Config = QGroupBox(self.FunctionWindow)
        self.General_Config.setObjectName(u"General_Config")
        self.General_Config.setMinimumSize(QSize(0, 0))
        self.General_Config.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.General_Config)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.select_group_01 = QFrame(self.General_Config)
        self.select_group_01.setObjectName(u"select_group_01")
        self.select_group_01.setLayoutDirection(Qt.LeftToRight)
        self.select_group_01.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.select_group_01)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.select_Label_01 = QLabel(self.select_group_01)
        self.select_Label_01.setObjectName(u"select_Label_01")
        self.select_Label_01.setMinimumSize(QSize(100, 0))
        self.select_Label_01.setMaximumSize(QSize(100, 16777215))
        self.select_Label_01.setFont(font)
        self.select_Label_01.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.select_Label_01)

        self.select_ComboBox_01 = QComboBox(self.select_group_01)
        self.select_ComboBox_01.setObjectName(u"select_ComboBox_01")
        self.select_ComboBox_01.setMinimumSize(QSize(300, 0))
        self.select_ComboBox_01.setMaximumSize(QSize(300, 16777215))
        self.select_ComboBox_01.setFont(font1)

        self.horizontalLayout.addWidget(self.select_ComboBox_01)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.select_group_01)

        self.select_group_02 = QFrame(self.General_Config)
        self.select_group_02.setObjectName(u"select_group_02")
        self.horizontalLayout_6 = QHBoxLayout(self.select_group_02)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.select_Label_02 = QLabel(self.select_group_02)
        self.select_Label_02.setObjectName(u"select_Label_02")
        self.select_Label_02.setMinimumSize(QSize(100, 0))
        self.select_Label_02.setMaximumSize(QSize(100, 16777215))
        self.select_Label_02.setFont(font)
        self.select_Label_02.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_6.addWidget(self.select_Label_02)

        self.select_ComboBox_02 = QComboBox(self.select_group_02)
        self.select_ComboBox_02.setObjectName(u"select_ComboBox_02")
        self.select_ComboBox_02.setMinimumSize(QSize(300, 0))
        self.select_ComboBox_02.setMaximumSize(QSize(200, 16777215))
        self.select_ComboBox_02.setFont(font1)

        self.horizontalLayout_6.addWidget(self.select_ComboBox_02)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addWidget(self.select_group_02)

        self.select_group_03 = QFrame(self.General_Config)
        self.select_group_03.setObjectName(u"select_group_03")
        self.horizontalLayout_7 = QHBoxLayout(self.select_group_03)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.select_Label_03 = QLabel(self.select_group_03)
        self.select_Label_03.setObjectName(u"select_Label_03")
        self.select_Label_03.setMinimumSize(QSize(100, 0))
        self.select_Label_03.setMaximumSize(QSize(100, 16777215))
        self.select_Label_03.setFont(font)
        self.select_Label_03.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_7.addWidget(self.select_Label_03)

        self.select_ComboBox_03 = QComboBox(self.select_group_03)
        self.select_ComboBox_03.setObjectName(u"select_ComboBox_03")
        self.select_ComboBox_03.setMinimumSize(QSize(300, 0))
        self.select_ComboBox_03.setMaximumSize(QSize(200, 16777215))
        self.select_ComboBox_03.setFont(font1)

        self.horizontalLayout_7.addWidget(self.select_ComboBox_03)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addWidget(self.select_group_03)

        self.general_group_01 = QFrame(self.General_Config)
        self.general_group_01.setObjectName(u"general_group_01")
        self.horizontalLayout_8 = QHBoxLayout(self.general_group_01)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.general_Label_01 = QLabel(self.general_group_01)
        self.general_Label_01.setObjectName(u"general_Label_01")
        self.general_Label_01.setMinimumSize(QSize(100, 0))
        self.general_Label_01.setMaximumSize(QSize(100, 16777215))
        self.general_Label_01.setFont(font)

        self.horizontalLayout_8.addWidget(self.general_Label_01)

        self.general_LineEdit_01 = QLineEdit(self.general_group_01)
        self.general_LineEdit_01.setObjectName(u"general_LineEdit_01")
        self.general_LineEdit_01.setMinimumSize(QSize(300, 0))
        self.general_LineEdit_01.setMaximumSize(QSize(200, 16777215))
        self.general_LineEdit_01.setFont(font)

        self.horizontalLayout_8.addWidget(self.general_LineEdit_01)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addWidget(self.general_group_01)

        self.general_group_02 = QFrame(self.General_Config)
        self.general_group_02.setObjectName(u"general_group_02")
        self.horizontalLayout_9 = QHBoxLayout(self.general_group_02)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.general_Label_02 = QLabel(self.general_group_02)
        self.general_Label_02.setObjectName(u"general_Label_02")
        self.general_Label_02.setMinimumSize(QSize(100, 0))
        self.general_Label_02.setMaximumSize(QSize(100, 16777215))
        self.general_Label_02.setFont(font)

        self.horizontalLayout_9.addWidget(self.general_Label_02)

        self.general_LineEdit_02 = QLineEdit(self.general_group_02)
        self.general_LineEdit_02.setObjectName(u"general_LineEdit_02")
        self.general_LineEdit_02.setMinimumSize(QSize(300, 0))
        self.general_LineEdit_02.setMaximumSize(QSize(200, 16777215))
        self.general_LineEdit_02.setFont(font)

        self.horizontalLayout_9.addWidget(self.general_LineEdit_02)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addWidget(self.general_group_02)

        self.general_group_03 = QFrame(self.General_Config)
        self.general_group_03.setObjectName(u"general_group_03")
        self.horizontalLayout_10 = QHBoxLayout(self.general_group_03)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.general_Label_03 = QLabel(self.general_group_03)
        self.general_Label_03.setObjectName(u"general_Label_03")
        self.general_Label_03.setMinimumSize(QSize(100, 0))
        self.general_Label_03.setMaximumSize(QSize(100, 16777215))
        self.general_Label_03.setFont(font)

        self.horizontalLayout_10.addWidget(self.general_Label_03)

        self.general_LineEdit_03 = QLineEdit(self.general_group_03)
        self.general_LineEdit_03.setObjectName(u"general_LineEdit_03")
        self.general_LineEdit_03.setMinimumSize(QSize(300, 0))
        self.general_LineEdit_03.setMaximumSize(QSize(200, 16777215))
        self.general_LineEdit_03.setFont(font)

        self.horizontalLayout_10.addWidget(self.general_LineEdit_03)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addWidget(self.general_group_03)

        self.general_group_04 = QFrame(self.General_Config)
        self.general_group_04.setObjectName(u"general_group_04")
        self.horizontalLayout_11 = QHBoxLayout(self.general_group_04)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.general_Label_04 = QLabel(self.general_group_04)
        self.general_Label_04.setObjectName(u"general_Label_04")
        self.general_Label_04.setMinimumSize(QSize(100, 0))
        self.general_Label_04.setMaximumSize(QSize(100, 16777215))
        self.general_Label_04.setFont(font)

        self.horizontalLayout_11.addWidget(self.general_Label_04)

        self.general_LineEdit_04 = QLineEdit(self.general_group_04)
        self.general_LineEdit_04.setObjectName(u"general_LineEdit_04")
        self.general_LineEdit_04.setMinimumSize(QSize(300, 0))
        self.general_LineEdit_04.setMaximumSize(QSize(200, 16777215))
        self.general_LineEdit_04.setFont(font)

        self.horizontalLayout_11.addWidget(self.general_LineEdit_04)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addWidget(self.general_group_04)

        self.file_group_01 = QFrame(self.General_Config)
        self.file_group_01.setObjectName(u"file_group_01")
        self.horizontalLayout_16 = QHBoxLayout(self.file_group_01)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.file_sel_Label_01 = QLabel(self.file_group_01)
        self.file_sel_Label_01.setObjectName(u"file_sel_Label_01")
        self.file_sel_Label_01.setMinimumSize(QSize(100, 0))
        self.file_sel_Label_01.setMaximumSize(QSize(100, 16777215))
        self.file_sel_Label_01.setFont(font1)
        self.file_sel_Label_01.setFrameShape(QFrame.NoFrame)
        self.file_sel_Label_01.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.file_sel_Label_01)

        self.file_sel_LineEdit_01 = QLineEdit(self.file_group_01)
        self.file_sel_LineEdit_01.setObjectName(u"file_sel_LineEdit_01")
        self.file_sel_LineEdit_01.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_01.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_01.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_01.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_01.setFocusPolicy(Qt.StrongFocus)
        self.file_sel_LineEdit_01.setReadOnly(False)

        self.horizontalLayout_12.addWidget(self.file_sel_LineEdit_01)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_12)

        self.file_sel_Button_01 = QPushButton(self.file_group_01)
        self.file_sel_Button_01.setObjectName(u"file_sel_Button_01")
        sizePolicy2.setHeightForWidth(self.file_sel_Button_01.sizePolicy().hasHeightForWidth())
        self.file_sel_Button_01.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.file_sel_Button_01)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addWidget(self.file_group_01)

        self.file_group_02 = QFrame(self.General_Config)
        self.file_group_02.setObjectName(u"file_group_02")
        self.horizontalLayout_17 = QHBoxLayout(self.file_group_02)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.file_sel_Label_02 = QLabel(self.file_group_02)
        self.file_sel_Label_02.setObjectName(u"file_sel_Label_02")
        self.file_sel_Label_02.setMinimumSize(QSize(100, 0))
        self.file_sel_Label_02.setMaximumSize(QSize(100, 16777215))
        self.file_sel_Label_02.setFont(font1)
        self.file_sel_Label_02.setFrameShape(QFrame.NoFrame)
        self.file_sel_Label_02.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.file_sel_Label_02)

        self.file_sel_LineEdit_02 = QLineEdit(self.file_group_02)
        self.file_sel_LineEdit_02.setObjectName(u"file_sel_LineEdit_02")
        self.file_sel_LineEdit_02.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_02.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_02.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_02.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_02.setFocusPolicy(Qt.StrongFocus)
        self.file_sel_LineEdit_02.setReadOnly(False)

        self.horizontalLayout_13.addWidget(self.file_sel_LineEdit_02)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_13)

        self.file_sel_Button_02 = QPushButton(self.file_group_02)
        self.file_sel_Button_02.setObjectName(u"file_sel_Button_02")
        sizePolicy2.setHeightForWidth(self.file_sel_Button_02.sizePolicy().hasHeightForWidth())
        self.file_sel_Button_02.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.file_sel_Button_02)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)


        self.verticalLayout_7.addWidget(self.file_group_02)

        self.file_group_03 = QFrame(self.General_Config)
        self.file_group_03.setObjectName(u"file_group_03")
        self.horizontalLayout_18 = QHBoxLayout(self.file_group_03)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.file_sel_Label_03 = QLabel(self.file_group_03)
        self.file_sel_Label_03.setObjectName(u"file_sel_Label_03")
        self.file_sel_Label_03.setMinimumSize(QSize(100, 0))
        self.file_sel_Label_03.setMaximumSize(QSize(100, 16777215))
        self.file_sel_Label_03.setFont(font1)
        self.file_sel_Label_03.setFrameShape(QFrame.NoFrame)
        self.file_sel_Label_03.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.file_sel_Label_03)

        self.file_sel_LineEdit_03 = QLineEdit(self.file_group_03)
        self.file_sel_LineEdit_03.setObjectName(u"file_sel_LineEdit_03")
        self.file_sel_LineEdit_03.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_03.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_03.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_03.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_03.setFocusPolicy(Qt.StrongFocus)
        self.file_sel_LineEdit_03.setReadOnly(False)

        self.horizontalLayout_14.addWidget(self.file_sel_LineEdit_03)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_14)

        self.file_sel_Button_03 = QPushButton(self.file_group_03)
        self.file_sel_Button_03.setObjectName(u"file_sel_Button_03")
        sizePolicy2.setHeightForWidth(self.file_sel_Button_03.sizePolicy().hasHeightForWidth())
        self.file_sel_Button_03.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.file_sel_Button_03)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)


        self.verticalLayout_7.addWidget(self.file_group_03)

        self.file_group_04 = QFrame(self.General_Config)
        self.file_group_04.setObjectName(u"file_group_04")
        self.horizontalLayout_19 = QHBoxLayout(self.file_group_04)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.file_sel_Label_04 = QLabel(self.file_group_04)
        self.file_sel_Label_04.setObjectName(u"file_sel_Label_04")
        self.file_sel_Label_04.setMinimumSize(QSize(100, 0))
        self.file_sel_Label_04.setMaximumSize(QSize(100, 16777215))
        self.file_sel_Label_04.setFont(font1)
        self.file_sel_Label_04.setFrameShape(QFrame.NoFrame)
        self.file_sel_Label_04.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.file_sel_Label_04)

        self.file_sel_LineEdit_04 = QLineEdit(self.file_group_04)
        self.file_sel_LineEdit_04.setObjectName(u"file_sel_LineEdit_04")
        self.file_sel_LineEdit_04.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_04.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_04.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_04.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_04.setFocusPolicy(Qt.StrongFocus)
        self.file_sel_LineEdit_04.setReadOnly(False)

        self.horizontalLayout_15.addWidget(self.file_sel_LineEdit_04)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_15)

        self.file_sel_Button_04 = QPushButton(self.file_group_04)
        self.file_sel_Button_04.setObjectName(u"file_sel_Button_04")
        sizePolicy2.setHeightForWidth(self.file_sel_Button_04.sizePolicy().hasHeightForWidth())
        self.file_sel_Button_04.setSizePolicy(sizePolicy2)

        self.horizontalLayout_19.addWidget(self.file_sel_Button_04)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)


        self.verticalLayout_7.addWidget(self.file_group_04)


        self.verticalLayout_8.addWidget(self.General_Config)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.FunctionWindow)

        self.Operate_2 = QGroupBox(self.Toolbox)
        self.Operate_2.setObjectName(u"Operate_2")
        self.Operate_2.setMinimumSize(QSize(300, 0))
        self.Operate_2.setMaximumSize(QSize(16777215, 16777215))
        self.Operate_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.gridLayout_9 = QGridLayout(self.Operate_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(20, 10, 20, 10)
        self.general_operate_Button_04 = QPushButton(self.Operate_2)
        self.general_operate_Button_04.setObjectName(u"general_operate_Button_04")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_04.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_04.setSizePolicy(sizePolicy1)
        self.general_operate_Button_04.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_04.setFont(font)
        self.general_operate_Button_04.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_04, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 0, 6, 1, 1)

        self.general_operate_Button_02 = QPushButton(self.Operate_2)
        self.general_operate_Button_02.setObjectName(u"general_operate_Button_02")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_02.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_02.setSizePolicy(sizePolicy1)
        self.general_operate_Button_02.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_02.setFont(font)
        self.general_operate_Button_02.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_02, 0, 1, 1, 1)

        self.general_operate_Button_05 = QPushButton(self.Operate_2)
        self.general_operate_Button_05.setObjectName(u"general_operate_Button_05")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_05.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_05.setSizePolicy(sizePolicy1)
        self.general_operate_Button_05.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_05.setFont(font)
        self.general_operate_Button_05.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_05, 0, 4, 1, 1)

        self.general_operate_Button_01 = QPushButton(self.Operate_2)
        self.general_operate_Button_01.setObjectName(u"general_operate_Button_01")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_01.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_01.setSizePolicy(sizePolicy1)
        self.general_operate_Button_01.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_01.setFont(font)
        self.general_operate_Button_01.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_01, 0, 0, 1, 1)

        self.general_operate_Button_03 = QPushButton(self.Operate_2)
        self.general_operate_Button_03.setObjectName(u"general_operate_Button_03")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_03.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_03.setSizePolicy(sizePolicy1)
        self.general_operate_Button_03.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_03.setFont(font)
        self.general_operate_Button_03.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_03, 0, 2, 1, 1)

        self.general_operate_Button_06 = QPushButton(self.Operate_2)
        self.general_operate_Button_06.setObjectName(u"general_operate_Button_06")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_06.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_06.setSizePolicy(sizePolicy1)
        self.general_operate_Button_06.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_06.setFont(font)
        self.general_operate_Button_06.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_06, 0, 5, 1, 1)


        self.verticalLayout_6.addWidget(self.Operate_2)

        self.pages.addWidget(self.Toolbox)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.page_2_layout = QVBoxLayout(self.Settings)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 0)
        self.scroll_area = QScrollArea(self.Settings)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 886, 720))
        self.contents.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setItalic(False)
        self.title_label.setFont(font4)
        self.title_label.setStyleSheet(u"font: 24pt \"Microsoft YaHei UI\";")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.softsetting = QGroupBox(self.contents)
        self.softsetting.setObjectName(u"softsetting")
        self.softsetting.setMinimumSize(QSize(0, 0))
        self.softsetting.setMaximumSize(QSize(16777215, 16777215))
        self.softsetting.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        self.verticalLayout_9 = QVBoxLayout(self.softsetting)
        self.verticalLayout_9.setSpacing(24)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.chip_ID_Group = QFrame(self.softsetting)
        self.chip_ID_Group.setObjectName(u"chip_ID_Group")
        self.chip_ID_Group.setLayoutDirection(Qt.LeftToRight)
        self.chip_ID_Group.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(self.chip_ID_Group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chip_ID_Label = QLabel(self.chip_ID_Group)
        self.chip_ID_Label.setObjectName(u"chip_ID_Label")
        self.chip_ID_Label.setMinimumSize(QSize(100, 0))
        self.chip_ID_Label.setMaximumSize(QSize(100, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.chip_ID_Label.setFont(font5)
        self.chip_ID_Label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_3.addWidget(self.chip_ID_Label)

        self.chip_ID_ComboBox = QComboBox(self.chip_ID_Group)
        self.chip_ID_ComboBox.addItem("")
        self.chip_ID_ComboBox.setObjectName(u"chip_ID_ComboBox")
        self.chip_ID_ComboBox.setEnabled(False)
        self.chip_ID_ComboBox.setMinimumSize(QSize(300, 0))
        self.chip_ID_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.chip_ID_ComboBox.setFont(font5)

        self.horizontalLayout_3.addWidget(self.chip_ID_ComboBox)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)


        self.verticalLayout_9.addWidget(self.chip_ID_Group)

        self.thems_select_Group = QFrame(self.softsetting)
        self.thems_select_Group.setObjectName(u"thems_select_Group")
        self.thems_select_Group.setEnabled(False)
        self.horizontalLayout_21 = QHBoxLayout(self.thems_select_Group)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.themes_select_Label = QLabel(self.thems_select_Group)
        self.themes_select_Label.setObjectName(u"themes_select_Label")
        self.themes_select_Label.setMinimumSize(QSize(100, 0))
        self.themes_select_Label.setMaximumSize(QSize(100, 16777215))
        self.themes_select_Label.setFont(font5)
        self.themes_select_Label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_21.addWidget(self.themes_select_Label)

        self.themes_select_ComboBox = QComboBox(self.thems_select_Group)
        self.themes_select_ComboBox.addItem("")
        self.themes_select_ComboBox.addItem("")
        self.themes_select_ComboBox.setObjectName(u"themes_select_ComboBox")
        self.themes_select_ComboBox.setMinimumSize(QSize(300, 0))
        self.themes_select_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.themes_select_ComboBox.setFont(font5)

        self.horizontalLayout_21.addWidget(self.themes_select_ComboBox)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)


        self.verticalLayout_9.addWidget(self.thems_select_Group)

        self.roi_image_save = QFrame(self.softsetting)
        self.roi_image_save.setObjectName(u"roi_image_save")
        self.horizontalLayout_22 = QHBoxLayout(self.roi_image_save)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.roi_image_save_Label = QLabel(self.roi_image_save)
        self.roi_image_save_Label.setObjectName(u"roi_image_save_Label")
        self.roi_image_save_Label.setMinimumSize(QSize(100, 0))
        self.roi_image_save_Label.setMaximumSize(QSize(100, 16777215))
        self.roi_image_save_Label.setFont(font5)
        self.roi_image_save_Label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_22.addWidget(self.roi_image_save_Label)

        self.roi_image_save_ComboBox = QComboBox(self.roi_image_save)
        self.roi_image_save_ComboBox.addItem("")
        self.roi_image_save_ComboBox.addItem("")
        self.roi_image_save_ComboBox.setObjectName(u"roi_image_save_ComboBox")
        self.roi_image_save_ComboBox.setMinimumSize(QSize(300, 0))
        self.roi_image_save_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.roi_image_save_ComboBox.setFont(font5)

        self.horizontalLayout_22.addWidget(self.roi_image_save_ComboBox)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_22)


        self.verticalLayout_9.addWidget(self.roi_image_save)

        self.roi_data_format_Group = QFrame(self.softsetting)
        self.roi_data_format_Group.setObjectName(u"roi_data_format_Group")
        self.horizontalLayout_20 = QHBoxLayout(self.roi_data_format_Group)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.roi_data_format_Label = QLabel(self.roi_data_format_Group)
        self.roi_data_format_Label.setObjectName(u"roi_data_format_Label")
        self.roi_data_format_Label.setMinimumSize(QSize(100, 0))
        self.roi_data_format_Label.setMaximumSize(QSize(100, 16777215))
        self.roi_data_format_Label.setFont(font5)
        self.roi_data_format_Label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_20.addWidget(self.roi_data_format_Label)

        self.roi_data_fromat_ComboBox = QComboBox(self.roi_data_format_Group)
        self.roi_data_fromat_ComboBox.addItem("")
        self.roi_data_fromat_ComboBox.addItem("")
        self.roi_data_fromat_ComboBox.setObjectName(u"roi_data_fromat_ComboBox")
        self.roi_data_fromat_ComboBox.setMinimumSize(QSize(300, 0))
        self.roi_data_fromat_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.roi_data_fromat_ComboBox.setFont(font5)

        self.horizontalLayout_20.addWidget(self.roi_data_fromat_ComboBox)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)


        self.verticalLayout_9.addWidget(self.roi_data_format_Group)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.softsetting)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.Settings)

        self.verticalLayout_10.addWidget(self.pages)

#if QT_CONFIG(shortcut)
        self.title_label.setBuddy(self.select_group_01)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainPages)
        self.V_ROLL_NUM_Slider.valueChanged.connect(self.V_ROLL_NUM_Value.setNum)
        self.H_ROLL_NUM_Slider.valueChanged.connect(self.H_ROLL_NUM_Value.setNum)
        self.H_VLD_SEG_Slider.valueChanged.connect(self.H_VLD_SEG_Value.setNum)

        self.pages.setCurrentIndex(0)
        self.ROIConfig.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.XCLK_Label.setText(QCoreApplication.translate("MainPages", u"XCLK", None))
        self.XCLK_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"24 M", None))
        self.XCLK_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"25 M", None))

        self.MST_MODE_Label.setText(QCoreApplication.translate("MainPages", u"MST_MODE", None))
        self.MST_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Slave Mode", None))
        self.MST_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Master Mode", None))

        self.WORK_MODE_Label.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.WORK_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Ranging Mode", None))
        self.WORK_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Echo Mode", None))
        self.WORK_MODE_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"Histogram Mode", None))
        self.WORK_MODE_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"Gray Scale Mode", None))

        self.MIPI_RATE_Label.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
        self.MIPI_RATE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"0.8 Gbps/Lane", None))
        self.MIPI_RATE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"1.0 Gbps/Lane", None))
        self.MIPI_RATE_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"1.2 Gbps/Lane", None))
        self.MIPI_RATE_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"1.5 Gbps/Lane", None))

        self.MoreConfiguration.setTitle("")
        self.V_PXL_OUT_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 Pixel", None))
        self.V_PXL_OUT_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"6 Pixel", None))

        self.TRG_I_EN_Label.setText(QCoreApplication.translate("MainPages", u"TRG_I_EN", None))
        self.OUT_BIN_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_BIN_NUM", None))
        self.SYS_CLK_Label.setText(QCoreApplication.translate("MainPages", u"SYS CLK", None))
        self.TDC_BIN_W_Label.setText(QCoreApplication.translate("MainPages", u"TDC bin width", None))
        self.PKS_ECHO_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"PKS_ECHO_NUM", None))
        self.MINBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
        self.PKS_ECHO_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 Echo", None))
        self.PKS_ECHO_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2 Echo", None))
        self.PKS_ECHO_NUM_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"3 Echo", None))
        self.PKS_ECHO_NUM_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"4 Echo", None))
        self.PKS_ECHO_NUM_ComboBox.setItemText(4, QCoreApplication.translate("MainPages", u"5 Echo", None))

        self.TDC_BIN_W_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"0.75 ns", None))
        self.TDC_BIN_W_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"1.00 ns", None))
        self.TDC_BIN_W_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"1.25 ns", None))
        self.TDC_BIN_W_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"1.50 ns", None))
        self.TDC_BIN_W_ComboBox.setItemText(4, QCoreApplication.translate("MainPages", u"2.00 ns", None))
        self.TDC_BIN_W_ComboBox.setItemText(5, QCoreApplication.translate("MainPages", u"2.50 ns", None))

#if QT_CONFIG(tooltip)
        self.MAXBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.MAXBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.MAXBIN_THRS_Lable_.setText(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
        self.V_PXL_OUT_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_PXL_NUM", None))
        self.SYS_CLK_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"200 M", None))
        self.SYS_CLK_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"250 M", None))
        self.SYS_CLK_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"330 M", None))

        self.TRG_I_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Disable", None))
        self.TRG_I_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Enable", None))

#if QT_CONFIG(tooltip)
        self.MINBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.MINBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.OUT_BIN_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"36 Bin", None))
        self.OUT_BIN_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"60 Bin", None))

        self.BIN_NUMBER_Value.setText(QCoreApplication.translate("MainPages", u"672", None))
        self.SCAN_MODE_Label.setText(QCoreApplication.translate("MainPages", u"SCAN_MODE", None))
        self.SCAN_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1D SCAN_MODE", None))
        self.SCAN_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2D SCAN_MODE", None))

        self.V_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_ROLL_NUM", None))
        self.H_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"H_ROLL_NUM", None))
        self.H_VLD_SEG_Label.setText(QCoreApplication.translate("MainPages", u"H_VLD_SEG", None))
        self.H_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.V_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.H_VLD_SEG_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.seg_hs_Label.setText(QCoreApplication.translate("MainPages", u"seg_hs", None))
#if QT_CONFIG(whatsthis)
        self.seg_hs_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.spad_vs_Label.setText(QCoreApplication.translate("MainPages", u"spad_vs", None))
        self.light_shift_Label.setText(QCoreApplication.translate("MainPages", u"light shift", None))
        self.sublight_shift_Label.setText(QCoreApplication.translate("MainPages", u"sublight shift", None))
        self.ROI_Shape_Label.setText(QCoreApplication.translate("MainPages", u"ROI shape", None))
        self.ROI_Shape_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Straight", None))
        self.ROI_Shape_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Curve", None))

        self.v_spad_shift_Label.setText(QCoreApplication.translate("MainPages", u"v_spad_shift", None))
        self.h_seg_shift_Label.setText(QCoreApplication.translate("MainPages", u"h_seg_shift", None))
        self.ROI_Retrace_Label.setText(QCoreApplication.translate("MainPages", u"ROI retrace", None))
        self.ROI_Retrace_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.ROI_Retrace_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.sublight_group_Label.setText(QCoreApplication.translate("MainPages", u"sublight group", None))
        self.sublight_group_LineEdit.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.sublight_group_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"6\u884cpixel\u5206\u7ec4\u65b9\u5f0f", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config1byGUI), QCoreApplication.translate("MainPages", u"ROI GUI", None))
        self.Cali_File_Load_Label.setText(QCoreApplication.translate("MainPages", u"Cali File", None))
        self.Cali_File_Load_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u5750\u6807\u6587\u4ef6\uff0c\u652f\u6301 .txt, .csv, .xls, .xlsx", None))
        self.Cali_File_Load_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Excel_Sheet_sel_Label.setText(QCoreApplication.translate("MainPages", u"Sheet Sel", None))
#if QT_CONFIG(whatsthis)
        self.Excel_Sheet_sel_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config2byCOOR), QCoreApplication.translate("MainPages", u"ROI COOR", None))
        self.ROI_File_Label.setText(QCoreApplication.translate("MainPages", u"ROI File", None))
        self.ROI_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u7f16\u8f91\u7684ROI\u6587\u4ef6", None))
        self.ROI_File_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Start_Rolling_Label.setText(QCoreApplication.translate("MainPages", u"Start Rolling", None))
        self.End_Rolling_Label.setText(QCoreApplication.translate("MainPages", u"End Rolling", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config3ROIEdit), QCoreApplication.translate("MainPages", u"ROI Edit", None))
        self.cali_file_path_Label.setText(QCoreApplication.translate("MainPages", u"Cali File", None))
        self.cali_file_path_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u6807\u5b9a\u7684ROI\u6587\u4ef6", None))
        self.cali_file_path_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.img_mirror_Label.setText(QCoreApplication.translate("MainPages", u"Img Mirror ", None))
        self.img_mirror_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No mirror", None))
        self.img_mirror_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"X-axis mirror", None))
        self.img_mirror_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"Y-axis mirror", None))
        self.img_mirror_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"X-axis and Y-axis mirror", None))

        self.remove_noise_Label.setText(QCoreApplication.translate("MainPages", u"remove noise", None))
        self.remove_noise_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.remove_noise_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.light_smooth_Label.setText(QCoreApplication.translate("MainPages", u"light smooth", None))
        self.light_smooth_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.light_smooth_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.curvature_Label.setText(QCoreApplication.translate("MainPages", u"curvature", None))
        self.correct_thres_Label.setText(QCoreApplication.translate("MainPages", u"correct thres", None))
        self.cali_order_Label.setText(QCoreApplication.translate("MainPages", u"Cali Order", None))
        self.cali_order_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"From small to large", None))
        self.cali_order_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"From large to small", None))

        self.cali_frm_num_Label.setText(QCoreApplication.translate("MainPages", u"cali frm num", None))
        self.ref_segment_Label.setText(QCoreApplication.translate("MainPages", u"ref segment", None))
        self.mode_2D_Label.setText(QCoreApplication.translate("MainPages", u"mode 2D", None))
        self.mode_2D_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Light strip energy is preferred", None))
        self.mode_2D_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"The number of covered photons is preferred", None))

        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config4ROICali), QCoreApplication.translate("MainPages", u"ROI Cali", None))
        self.ROIZoneConfig.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><a href=\"https://www.example.com\"><span style=\" text-decoration: underline; color:#0078d7;\">ZONE INFO</span></a></p></body></html>", None))
        self.ROIView.setText(QCoreApplication.translate("MainPages", u"View", None))
        self.ROISave.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.roi_sram_name_Label.setText(QCoreApplication.translate("MainPages", u"ROI SRAM Name", None))
        self.reg_script_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.file_save_dir_Label.setText(QCoreApplication.translate("MainPages", u"File Save Path", None))
        self.reference_script_sel_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.roi_sram_name_CheckBox.setText(QCoreApplication.translate("MainPages", u"Include", None))
        self.roi_sram_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.reference_script_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.Save.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Open.setText(QCoreApplication.translate("MainPages", u"Open", None))
        self.reference_script_Label.setText(QCoreApplication.translate("MainPages", u"Reference Script", None))
        self.file_save_dir_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u6307\u5b9aSpadisApp\u8f6f\u4ef6\u8def\u5f84", None))
        self.file_save_dir_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.reg_script_name_Label.setText(QCoreApplication.translate("MainPages", u"Reg Script Name", None))
        self.reference_script_parse_Button.setText(QCoreApplication.translate("MainPages", u"Parse", None))
        self.title_label_2.setText(QCoreApplication.translate("MainPages", u"Hawk Toolbox", None))
        self.FunctionWindow.setTitle("")
        self.FunctionSelectWin.setTitle(QCoreApplication.translate("MainPages", u"Function Select", None))
        self.SpadisAppPCMREAD.setText(QCoreApplication.translate("MainPages", u"Spadis App PCM READ", None))
        self.DothinkPCMImag.setText(QCoreApplication.translate("MainPages", u"Dothink PCM Imag", None))
        self.select_Label_01.setText(QCoreApplication.translate("MainPages", u"Select1", None))
        self.select_Label_02.setText(QCoreApplication.translate("MainPages", u"Select1", None))
        self.select_Label_03.setText(QCoreApplication.translate("MainPages", u"Select1", None))
        self.general_Label_01.setText(QCoreApplication.translate("MainPages", u"Input1", None))
        self.general_LineEdit_01.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u5185\u5bb9", None))
        self.general_Label_02.setText(QCoreApplication.translate("MainPages", u"Input2", None))
        self.general_LineEdit_02.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u5185\u5bb9", None))
        self.general_Label_03.setText(QCoreApplication.translate("MainPages", u"Input3", None))
        self.general_LineEdit_03.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u5185\u5bb9", None))
        self.general_Label_04.setText(QCoreApplication.translate("MainPages", u"Input4", None))
        self.general_LineEdit_04.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u5185\u5bb9", None))
        self.file_sel_Label_01.setText(QCoreApplication.translate("MainPages", u"File sel", None))
        self.file_sel_LineEdit_01.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.file_sel_Button_01.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.file_sel_Label_02.setText(QCoreApplication.translate("MainPages", u"File sel", None))
        self.file_sel_LineEdit_02.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.file_sel_Button_02.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.file_sel_Label_03.setText(QCoreApplication.translate("MainPages", u"File sel", None))
        self.file_sel_LineEdit_03.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.file_sel_Button_03.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.file_sel_Label_04.setText(QCoreApplication.translate("MainPages", u"File sel", None))
        self.file_sel_LineEdit_04.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.file_sel_Button_04.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Operate_2.setTitle(QCoreApplication.translate("MainPages", u"Operate", None))
        self.general_operate_Button_04.setText(QCoreApplication.translate("MainPages", u"button", None))
        self.general_operate_Button_02.setText(QCoreApplication.translate("MainPages", u"button", None))
        self.general_operate_Button_05.setText(QCoreApplication.translate("MainPages", u"button", None))
        self.general_operate_Button_01.setText(QCoreApplication.translate("MainPages", u"button", None))
        self.general_operate_Button_03.setText(QCoreApplication.translate("MainPages", u"button", None))
        self.general_operate_Button_06.setText(QCoreApplication.translate("MainPages", u"button", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Setting", None))
        self.chip_ID_Label.setText(QCoreApplication.translate("MainPages", u"Chip ID", None))
        self.chip_ID_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Hawk01", None))

#if QT_CONFIG(tooltip)
        self.thems_select_Group.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.themes_select_Label.setText(QCoreApplication.translate("MainPages", u"Themes", None))
        self.themes_select_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"light", None))
        self.themes_select_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"dark", None))

#if QT_CONFIG(tooltip)
        self.themes_select_ComboBox.setToolTip(QCoreApplication.translate("MainPages", u"Coming soon!", None))
#endif // QT_CONFIG(tooltip)
        self.roi_image_save_Label.setText(QCoreApplication.translate("MainPages", u"ROI Image", None))
        self.roi_image_save_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Discard", None))
        self.roi_image_save_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Save", None))

        self.roi_data_format_Label.setText(QCoreApplication.translate("MainPages", u"ROI Format", None))
        self.roi_data_fromat_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Byte", None))
        self.roi_data_fromat_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Half-word", None))

    # retranslateUi


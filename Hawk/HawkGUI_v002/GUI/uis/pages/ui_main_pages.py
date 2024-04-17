# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesNjEbyo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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

from Hawk.HawkGUI_v002.gui.widgets.py_combo_check_box.py_combo_check import QComboCheckBox

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(844, 649)
        MainPages.setStyleSheet(u"")
        self.horizontalLayout_23 = QHBoxLayout(MainPages)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        self.pages.setFont(font)
        self.pages.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setFont(font)
        self.page_1.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.page_1)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 0)
        self.Layout1 = QGroupBox(self.page_1)
        self.Layout1.setObjectName(u"Layout1")
        self.horizontalLayout_2 = QHBoxLayout(self.Layout1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RegisterConfig = QFrame(self.Layout1)
        self.RegisterConfig.setObjectName(u"RegisterConfig")
        self.RegisterConfig.setMinimumSize(QSize(0, 0))
        self.RegisterConfig.setMaximumSize(QSize(400, 16777215))
        self.formLayout_2 = QFormLayout(self.RegisterConfig)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(9, 9, 9, 9)
        self.REF_CLK_Config_Label = QLabel(self.RegisterConfig)
        self.REF_CLK_Config_Label.setObjectName(u"REF_CLK_Config_Label")
        self.REF_CLK_Config_Label.setFont(font)
        self.REF_CLK_Config_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.REF_CLK_Config_Label)

        self.REF_CLK_Config_ComboBox = QComboBox(self.RegisterConfig)
        self.REF_CLK_Config_ComboBox.setObjectName(u"REF_CLK_Config_ComboBox")
        self.REF_CLK_Config_ComboBox.setMinimumSize(QSize(150, 0))
        self.REF_CLK_Config_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.REF_CLK_Config_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.REF_CLK_Config_ComboBox)

        self.SYS_CLK_Config_Label = QLabel(self.RegisterConfig)
        self.SYS_CLK_Config_Label.setObjectName(u"SYS_CLK_Config_Label")
        self.SYS_CLK_Config_Label.setFont(font)
        self.SYS_CLK_Config_Label.setFrameShape(QFrame.StyledPanel)
        self.SYS_CLK_Config_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.SYS_CLK_Config_Label)

        self.SYS_CLK_Config_ComboBox = QComboBox(self.RegisterConfig)
        self.SYS_CLK_Config_ComboBox.setObjectName(u"SYS_CLK_Config_ComboBox")
        self.SYS_CLK_Config_ComboBox.setMinimumSize(QSize(100, 0))
        self.SYS_CLK_Config_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.SYS_CLK_Config_ComboBox)

        self.MST_MODE_Label = QLabel(self.RegisterConfig)
        self.MST_MODE_Label.setObjectName(u"MST_MODE_Label")
        self.MST_MODE_Label.setMinimumSize(QSize(85, 0))
        self.MST_MODE_Label.setMaximumSize(QSize(85, 16777215))
        self.MST_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.MST_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.MST_MODE_Label)

        self.MST_MODE_ComboBox = QComboBox(self.RegisterConfig)
        self.MST_MODE_ComboBox.setObjectName(u"MST_MODE_ComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.MST_MODE_ComboBox)

        self.TRG_I_EN_Label = QLabel(self.RegisterConfig)
        self.TRG_I_EN_Label.setObjectName(u"TRG_I_EN_Label")
        self.TRG_I_EN_Label.setMinimumSize(QSize(85, 0))
        self.TRG_I_EN_Label.setMaximumSize(QSize(85, 16777215))
        self.TRG_I_EN_Label.setFont(font)
        self.TRG_I_EN_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.TRG_I_EN_Label)

        self.TRG_I_EN_ComboBox = QComboBox(self.RegisterConfig)
        self.TRG_I_EN_ComboBox.setObjectName(u"TRG_I_EN_ComboBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.TRG_I_EN_ComboBox)

        self.WORK_MODE_Label = QLabel(self.RegisterConfig)
        self.WORK_MODE_Label.setObjectName(u"WORK_MODE_Label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WORK_MODE_Label.sizePolicy().hasHeightForWidth())
        self.WORK_MODE_Label.setSizePolicy(sizePolicy)
        self.WORK_MODE_Label.setMinimumSize(QSize(0, 0))
        self.WORK_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.WORK_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.WORK_MODE_Label.setFrameShadow(QFrame.Raised)
        self.WORK_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.WORK_MODE_Label)

        self.WORK_MODE_ComboBox = QComboCheckBox(self.RegisterConfig)
        self.WORK_MODE_ComboBox.setObjectName(u"WORK_MODE_ComboBox")
        self.WORK_MODE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.WORK_MODE_ComboBox)

        self.MIPI_RATE_Label = QLabel(self.RegisterConfig)
        self.MIPI_RATE_Label.setObjectName(u"MIPI_RATE_Label")
        sizePolicy.setHeightForWidth(self.MIPI_RATE_Label.sizePolicy().hasHeightForWidth())
        self.MIPI_RATE_Label.setSizePolicy(sizePolicy)
        self.MIPI_RATE_Label.setMinimumSize(QSize(0, 0))
        self.MIPI_RATE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.MIPI_RATE_Label.setFont(font1)
        self.MIPI_RATE_Label.setFrameShape(QFrame.StyledPanel)
        self.MIPI_RATE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.MIPI_RATE_Label)

        self.MIPI_RATE_ComboBox = QComboCheckBox(self.RegisterConfig)
        self.MIPI_RATE_ComboBox.setObjectName(u"MIPI_RATE_ComboBox")
        self.MIPI_RATE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.MIPI_RATE_ComboBox)

        self.TDC_Bin_Width_Label = QLabel(self.RegisterConfig)
        self.TDC_Bin_Width_Label.setObjectName(u"TDC_Bin_Width_Label")
        self.TDC_Bin_Width_Label.setMinimumSize(QSize(0, 0))
        self.TDC_Bin_Width_Label.setMaximumSize(QSize(16777215, 16777215))
        self.TDC_Bin_Width_Label.setFont(font)
        self.TDC_Bin_Width_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.TDC_Bin_Width_Label)

        self.TDC_Bin_Width_ComboBox = QComboBox(self.RegisterConfig)
        self.TDC_Bin_Width_ComboBox.setObjectName(u"TDC_Bin_Width_ComboBox")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.TDC_Bin_Width_ComboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.RegisterConfig)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.ROIConfigGroup = QFrame(self.Layout1)
        self.ROIConfigGroup.setObjectName(u"ROIConfigGroup")
        self.ROIConfigGroup.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.ROIConfigGroup)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 9, -1, -1)
        self.SubROIConfig = QFrame(self.ROIConfigGroup)
        self.SubROIConfig.setObjectName(u"SubROIConfig")
        self.formLayout_3 = QFormLayout(self.SubROIConfig)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(1, 1, -1, -1)
        self.SCAN_MODE_Label = QLabel(self.SubROIConfig)
        self.SCAN_MODE_Label.setObjectName(u"SCAN_MODE_Label")
        self.SCAN_MODE_Label.setMinimumSize(QSize(0, 0))
        self.SCAN_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.SCAN_MODE_Label.setFont(font1)
        self.SCAN_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.SCAN_MODE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.SCAN_MODE_Label)

        self.SCAN_MODE_ComboBox = QComboBox(self.SubROIConfig)
        self.SCAN_MODE_ComboBox.setObjectName(u"SCAN_MODE_ComboBox")
        self.SCAN_MODE_ComboBox.setMinimumSize(QSize(150, 0))
        self.SCAN_MODE_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.SCAN_MODE_ComboBox.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.SCAN_MODE_ComboBox)

        self.V_ROLL_NUM_Label = QLabel(self.SubROIConfig)
        self.V_ROLL_NUM_Label.setObjectName(u"V_ROLL_NUM_Label")
        self.V_ROLL_NUM_Label.setMinimumSize(QSize(0, 0))
        self.V_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.V_ROLL_NUM_Label.setFont(font1)
        self.V_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.V_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.V_ROLL_NUM_Label)

        self.V_ROLL_NUM_CMP = QHBoxLayout()
        self.V_ROLL_NUM_CMP.setSpacing(0)
        self.V_ROLL_NUM_CMP.setObjectName(u"V_ROLL_NUM_CMP")
        self.V_ROLL_NUM_CMP.setContentsMargins(0, -1, 0, -1)
        self.V_ROLL_NUM_Slider = QSlider(self.SubROIConfig)
        self.V_ROLL_NUM_Slider.setObjectName(u"V_ROLL_NUM_Slider")
        self.V_ROLL_NUM_Slider.setMouseTracking(False)
        self.V_ROLL_NUM_Slider.setMinimum(1)
        self.V_ROLL_NUM_Slider.setMaximum(32)
        self.V_ROLL_NUM_Slider.setPageStep(1)
        self.V_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Slider)

        self.V_ROLL_NUM_Value = QLabel(self.SubROIConfig)
        self.V_ROLL_NUM_Value.setObjectName(u"V_ROLL_NUM_Value")
        self.V_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.V_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.V_ROLL_NUM_Value.setFont(font1)
        self.V_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.V_ROLL_NUM_Value.setWordWrap(True)
        self.V_ROLL_NUM_Value.setMargin(0)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Value)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.V_ROLL_NUM_CMP)

        self.H_ROLL_NUM_Label = QLabel(self.SubROIConfig)
        self.H_ROLL_NUM_Label.setObjectName(u"H_ROLL_NUM_Label")
        self.H_ROLL_NUM_Label.setMinimumSize(QSize(0, 0))
        self.H_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_ROLL_NUM_Label.setFont(font1)
        self.H_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.H_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.H_ROLL_NUM_Label)

        self.H_ROLL_CMP = QHBoxLayout()
        self.H_ROLL_CMP.setSpacing(0)
        self.H_ROLL_CMP.setObjectName(u"H_ROLL_CMP")
        self.H_ROLL_CMP.setContentsMargins(0, -1, -1, -1)
        self.H_ROLL_NUM_Slider = QSlider(self.SubROIConfig)
        self.H_ROLL_NUM_Slider.setObjectName(u"H_ROLL_NUM_Slider")
        self.H_ROLL_NUM_Slider.setEnabled(True)
        self.H_ROLL_NUM_Slider.setMinimum(1)
        self.H_ROLL_NUM_Slider.setMaximum(16)
        self.H_ROLL_NUM_Slider.setPageStep(1)
        self.H_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Slider)

        self.H_ROLL_NUM_Value = QLabel(self.SubROIConfig)
        self.H_ROLL_NUM_Value.setObjectName(u"H_ROLL_NUM_Value")
        self.H_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.H_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.H_ROLL_NUM_Value.setFont(font1)
        self.H_ROLL_NUM_Value.setMidLineWidth(0)
        self.H_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_ROLL_NUM_Value.setMargin(0)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Value)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.H_ROLL_CMP)

        self.H_VLD_SEG_Label = QLabel(self.SubROIConfig)
        self.H_VLD_SEG_Label.setObjectName(u"H_VLD_SEG_Label")
        self.H_VLD_SEG_Label.setMinimumSize(QSize(0, 0))
        self.H_VLD_SEG_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_VLD_SEG_Label.setFont(font1)
        self.H_VLD_SEG_Label.setFrameShape(QFrame.StyledPanel)
        self.H_VLD_SEG_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.H_VLD_SEG_Label)

        self.H_VLD_SEG_CMP = QHBoxLayout()
        self.H_VLD_SEG_CMP.setSpacing(0)
        self.H_VLD_SEG_CMP.setObjectName(u"H_VLD_SEG_CMP")
        self.H_VLD_SEG_CMP.setContentsMargins(0, -1, -1, -1)
        self.H_VLD_SEG_Slider = QSlider(self.SubROIConfig)
        self.H_VLD_SEG_Slider.setObjectName(u"H_VLD_SEG_Slider")
        self.H_VLD_SEG_Slider.setMinimum(1)
        self.H_VLD_SEG_Slider.setMaximum(16)
        self.H_VLD_SEG_Slider.setPageStep(1)
        self.H_VLD_SEG_Slider.setOrientation(Qt.Horizontal)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Slider)

        self.H_VLD_SEG_Value = QLabel(self.SubROIConfig)
        self.H_VLD_SEG_Value.setObjectName(u"H_VLD_SEG_Value")
        self.H_VLD_SEG_Value.setMinimumSize(QSize(20, 25))
        self.H_VLD_SEG_Value.setMaximumSize(QSize(20, 16777215))
        self.H_VLD_SEG_Value.setFont(font1)
        self.H_VLD_SEG_Value.setTextFormat(Qt.MarkdownText)
        self.H_VLD_SEG_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_VLD_SEG_Value.setMargin(0)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Value)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.H_VLD_SEG_CMP)


        self.verticalLayout_11.addWidget(self.SubROIConfig)

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
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.scrollArea = QScrollArea(self.Config1byGUI)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 325, 184))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 20, 0)
        self.ROI_Shape_Light = QLabel(self.scrollAreaWidgetContents_2)
        self.ROI_Shape_Light.setObjectName(u"ROI_Shape_Light")
        self.ROI_Shape_Light.setMinimumSize(QSize(0, 0))
        self.ROI_Shape_Light.setMaximumSize(QSize(16777215, 16777215))
        self.ROI_Shape_Light.setFont(font1)
        self.ROI_Shape_Light.setFrameShape(QFrame.StyledPanel)
        self.ROI_Shape_Light.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.ROI_Shape_Light)

        self.ROI_Shape_ComboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.ROI_Shape_ComboBox.setObjectName(u"ROI_Shape_ComboBox")
        self.ROI_Shape_ComboBox.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ROI_Shape_ComboBox)

        self.seg_hs_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.seg_hs_Label.setObjectName(u"seg_hs_Label")
        self.seg_hs_Label.setMinimumSize(QSize(0, 0))
        self.seg_hs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.seg_hs_Label.setFont(font1)
        self.seg_hs_Label.setFrameShape(QFrame.StyledPanel)
        self.seg_hs_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.seg_hs_Label)

        self.seg_hs_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.seg_hs_spinBox.setObjectName(u"seg_hs_spinBox")
        self.seg_hs_spinBox.setMinimum(1)
        self.seg_hs_spinBox.setMaximum(16)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.seg_hs_spinBox)

        self.spad_vs_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.spad_vs_Label.setObjectName(u"spad_vs_Label")
        self.spad_vs_Label.setMinimumSize(QSize(0, 0))
        self.spad_vs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.spad_vs_Label.setFont(font1)
        self.spad_vs_Label.setFrameShape(QFrame.StyledPanel)
        self.spad_vs_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.spad_vs_Label)

        self.spad_vs_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spad_vs_spinBox.setObjectName(u"spad_vs_spinBox")
        self.spad_vs_spinBox.setMinimum(-575)
        self.spad_vs_spinBox.setMaximum(576)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spad_vs_spinBox)

        self.light_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.light_shift_Label.setObjectName(u"light_shift_Label")
        self.light_shift_Label.setMinimumSize(QSize(0, 0))
        self.light_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.light_shift_Label.setFont(font1)
        self.light_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.light_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.light_shift_Label)

        self.light_shift_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.light_shift_spinBox.setObjectName(u"light_shift_spinBox")
        self.light_shift_spinBox.setMinimum(-576)
        self.light_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.light_shift_spinBox)

        self.sublight_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.sublight_shift_Label.setObjectName(u"sublight_shift_Label")
        self.sublight_shift_Label.setMinimumSize(QSize(0, 0))
        self.sublight_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.sublight_shift_Label.setFont(font1)
        self.sublight_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.sublight_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.sublight_shift_Label)

        self.sublight_shift_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.sublight_shift_spinBox.setObjectName(u"sublight_shift_spinBox")
        self.sublight_shift_spinBox.setMinimum(-576)
        self.sublight_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sublight_shift_spinBox)

        self.v_spad_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.v_spad_shift_Label.setObjectName(u"v_spad_shift_Label")
        self.v_spad_shift_Label.setMinimumSize(QSize(0, 0))
        self.v_spad_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.v_spad_shift_Label.setFont(font1)
        self.v_spad_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.v_spad_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.v_spad_shift_Label)

        self.v_spad_shift_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.v_spad_shift_spinBox.setObjectName(u"v_spad_shift_spinBox")
        self.v_spad_shift_spinBox.setMinimum(-576)
        self.v_spad_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.v_spad_shift_spinBox)

        self.h_seg_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.h_seg_shift_Label.setObjectName(u"h_seg_shift_Label")
        self.h_seg_shift_Label.setMinimumSize(QSize(0, 0))
        self.h_seg_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.h_seg_shift_Label.setFont(font1)
        self.h_seg_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.h_seg_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.h_seg_shift_Label)

        self.h_seg_shift_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.h_seg_shift_spinBox.setObjectName(u"h_seg_shift_spinBox")
        self.h_seg_shift_spinBox.setMinimum(0)
        self.h_seg_shift_spinBox.setMaximum(15)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.h_seg_shift_spinBox)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 325, 184))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 20, 0)
        self.ROI_SRAM_File_Label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.ROI_SRAM_File_Label_3.setObjectName(u"ROI_SRAM_File_Label_3")
        self.ROI_SRAM_File_Label_3.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.ROI_SRAM_File_Label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Load_ROI_file_LineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.Load_ROI_file_LineEdit.setObjectName(u"Load_ROI_file_LineEdit")
        self.Load_ROI_file_LineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Load_ROI_file_LineEdit.sizePolicy().hasHeightForWidth())
        self.Load_ROI_file_LineEdit.setSizePolicy(sizePolicy1)
        self.Load_ROI_file_LineEdit.setMinimumSize(QSize(0, 0))
        self.Load_ROI_file_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Load_ROI_file_LineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.Load_ROI_file_LineEdit)

        self.Load_ROI_file_Button = QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_ROI_file_Button.setObjectName(u"Load_ROI_file_Button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Load_ROI_file_Button.sizePolicy().hasHeightForWidth())
        self.Load_ROI_file_Button.setSizePolicy(sizePolicy2)
        self.Load_ROI_file_Button.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_3.addWidget(self.Load_ROI_file_Button)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 325, 184))
        self.formLayout_5 = QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(10)
        self.formLayout_5.setVerticalSpacing(6)
        self.formLayout_5.setContentsMargins(0, 0, 20, 0)
        self.ROI_SRAM_File_Label_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.ROI_SRAM_File_Label_4.setObjectName(u"ROI_SRAM_File_Label_4")
        self.ROI_SRAM_File_Label_4.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.ROI_SRAM_File_Label_4)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(9)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.Load_ROI_file_LineEdit_2 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.Load_ROI_file_LineEdit_2.setObjectName(u"Load_ROI_file_LineEdit_2")
        self.Load_ROI_file_LineEdit_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Load_ROI_file_LineEdit_2.sizePolicy().hasHeightForWidth())
        self.Load_ROI_file_LineEdit_2.setSizePolicy(sizePolicy1)
        self.Load_ROI_file_LineEdit_2.setMinimumSize(QSize(0, 0))
        self.Load_ROI_file_LineEdit_2.setFocusPolicy(Qt.StrongFocus)
        self.Load_ROI_file_LineEdit_2.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.Load_ROI_file_LineEdit_2)

        self.Load_ROI_file_Button_2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.Load_ROI_file_Button_2.setObjectName(u"Load_ROI_file_Button_2")
        sizePolicy2.setHeightForWidth(self.Load_ROI_file_Button_2.sizePolicy().hasHeightForWidth())
        self.Load_ROI_file_Button_2.setSizePolicy(sizePolicy2)
        self.Load_ROI_file_Button_2.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_20.addWidget(self.Load_ROI_file_Button_2)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.seg_hs_Label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.seg_hs_Label_2.setObjectName(u"seg_hs_Label_2")
        self.seg_hs_Label_2.setMinimumSize(QSize(0, 0))
        self.seg_hs_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.seg_hs_Label_2.setFont(font1)
        self.seg_hs_Label_2.setFrameShape(QFrame.StyledPanel)
        self.seg_hs_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.seg_hs_Label_2)

        self.seg_hs_spinBox_2 = QSpinBox(self.scrollAreaWidgetContents_4)
        self.seg_hs_spinBox_2.setObjectName(u"seg_hs_spinBox_2")
        self.seg_hs_spinBox_2.setMinimum(1)
        self.seg_hs_spinBox_2.setMaximum(16)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.seg_hs_spinBox_2)

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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 325, 175))
        self.formLayout_7 = QFormLayout(self.scrollAreaWidgetContents_6)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(10)
        self.formLayout_7.setVerticalSpacing(6)
        self.formLayout_7.setContentsMargins(0, 0, 20, 0)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_2.addWidget(self.scrollArea_5)

        self.ROIConfig.addTab(self.Config4ROICali, "")

        self.verticalLayout_11.addWidget(self.ROIConfig)

        self.ROIZoneConfig = QLabel(self.ROIConfigGroup)
        self.ROIZoneConfig.setObjectName(u"ROIZoneConfig")
        self.ROIZoneConfig.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.ROIZoneConfig.setMargin(0)
        self.ROIZoneConfig.setOpenExternalLinks(False)

        self.verticalLayout_11.addWidget(self.ROIZoneConfig)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_18)

        self.ROISave = QPushButton(self.ROIConfigGroup)
        self.ROISave.setObjectName(u"ROISave")

        self.horizontalLayout_4.addWidget(self.ROISave)

        self.ROIView = QPushButton(self.ROIConfigGroup)
        self.ROIView.setObjectName(u"ROIView")

        self.horizontalLayout_4.addWidget(self.ROIView)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.ROIConfigGroup)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_12.addWidget(self.Layout1)

        self.Layout2 = QGroupBox(self.page_1)
        self.Layout2.setObjectName(u"Layout2")
        self.horizontalLayout_5 = QHBoxLayout(self.Layout2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FileConifg = QFrame(self.Layout2)
        self.FileConifg.setObjectName(u"FileConifg")
        self.FileConifg.setMinimumSize(QSize(300, 0))
        self.FileConifg.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_6 = QGridLayout(self.FileConifg)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 9, 9, 9)
        self.ROI_SRAM_File_LineEdit = QLineEdit(self.FileConifg)
        self.ROI_SRAM_File_LineEdit.setObjectName(u"ROI_SRAM_File_LineEdit")
        self.ROI_SRAM_File_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.ROI_SRAM_File_LineEdit, 3, 1, 1, 1)

        self.Sel_Config_file_LineEdit = QLineEdit(self.FileConifg)
        self.Sel_Config_file_LineEdit.setObjectName(u"Sel_Config_file_LineEdit")
        self.Sel_Config_file_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Sel_Config_file_LineEdit.sizePolicy().hasHeightForWidth())
        self.Sel_Config_file_LineEdit.setSizePolicy(sizePolicy1)
        self.Sel_Config_file_LineEdit.setMinimumSize(QSize(0, 0))
        self.Sel_Config_file_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Sel_Config_file_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.Sel_Config_file_LineEdit, 4, 1, 1, 1)

        self.ROI_SRAM_File_Label = QLabel(self.FileConifg)
        self.ROI_SRAM_File_Label.setObjectName(u"ROI_SRAM_File_Label")
        self.ROI_SRAM_File_Label.setFont(font)

        self.gridLayout_6.addWidget(self.ROI_SRAM_File_Label, 3, 0, 1, 1)

        self.ROI_Sram_File_CheckBox = QCheckBox(self.FileConifg)
        self.ROI_Sram_File_CheckBox.setObjectName(u"ROI_Sram_File_CheckBox")

        self.gridLayout_6.addWidget(self.ROI_Sram_File_CheckBox, 3, 3, 1, 1)

        self.SPadisApp_Path_Sel_Label = QLabel(self.FileConifg)
        self.SPadisApp_Path_Sel_Label.setObjectName(u"SPadisApp_Path_Sel_Label")
        self.SPadisApp_Path_Sel_Label.setMinimumSize(QSize(0, 0))
        self.SPadisApp_Path_Sel_Label.setMaximumSize(QSize(16777215, 16777215))
        self.SPadisApp_Path_Sel_Label.setFont(font1)
        self.SPadisApp_Path_Sel_Label.setFrameShape(QFrame.NoFrame)
        self.SPadisApp_Path_Sel_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.SPadisApp_Path_Sel_Label, 5, 0, 1, 1)

        self.REG_CFG_File_Label = QLabel(self.FileConifg)
        self.REG_CFG_File_Label.setObjectName(u"REG_CFG_File_Label")
        self.REG_CFG_File_Label.setFont(font)

        self.gridLayout_6.addWidget(self.REG_CFG_File_Label, 1, 0, 1, 1)

        self.ROI_Zone_Sel_CheckBox = QCheckBox(self.FileConifg)
        self.ROI_Zone_Sel_CheckBox.setObjectName(u"ROI_Zone_Sel_CheckBox")

        self.gridLayout_6.addWidget(self.ROI_Zone_Sel_CheckBox, 5, 3, 1, 1)

        self.Sel_Config_file_Label = QLabel(self.FileConifg)
        self.Sel_Config_file_Label.setObjectName(u"Sel_Config_file_Label")
        self.Sel_Config_file_Label.setMinimumSize(QSize(0, 0))
        self.Sel_Config_file_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Sel_Config_file_Label.setFont(font1)
        self.Sel_Config_file_Label.setFrameShape(QFrame.NoFrame)
        self.Sel_Config_file_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.Sel_Config_file_Label, 4, 0, 1, 1)

        self.SPadisApp_Path_Sel_Button = QPushButton(self.FileConifg)
        self.SPadisApp_Path_Sel_Button.setObjectName(u"SPadisApp_Path_Sel_Button")
        sizePolicy2.setHeightForWidth(self.SPadisApp_Path_Sel_Button.sizePolicy().hasHeightForWidth())
        self.SPadisApp_Path_Sel_Button.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.SPadisApp_Path_Sel_Button, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.Sel_Config_file_Button = QPushButton(self.FileConifg)
        self.Sel_Config_file_Button.setObjectName(u"Sel_Config_file_Button")
        sizePolicy2.setHeightForWidth(self.Sel_Config_file_Button.sizePolicy().hasHeightForWidth())
        self.Sel_Config_file_Button.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.Sel_Config_file_Button, 4, 2, 1, 1)

        self.REG_CFG_File_LineEdit = QLineEdit(self.FileConifg)
        self.REG_CFG_File_LineEdit.setObjectName(u"REG_CFG_File_LineEdit")
        self.REG_CFG_File_LineEdit.setMinimumSize(QSize(0, 0))
        self.REG_CFG_File_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.REG_CFG_File_LineEdit, 1, 1, 1, 1)

        self.SPadisApp_Path_Sel__LineEdit = QLineEdit(self.FileConifg)
        self.SPadisApp_Path_Sel__LineEdit.setObjectName(u"SPadisApp_Path_Sel__LineEdit")
        self.SPadisApp_Path_Sel__LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.SPadisApp_Path_Sel__LineEdit.sizePolicy().hasHeightForWidth())
        self.SPadisApp_Path_Sel__LineEdit.setSizePolicy(sizePolicy1)
        self.SPadisApp_Path_Sel__LineEdit.setMinimumSize(QSize(300, 0))
        self.SPadisApp_Path_Sel__LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.SPadisApp_Path_Sel__LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.SPadisApp_Path_Sel__LineEdit, 5, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 5, 4, 1, 1)


        self.horizontalLayout_5.addWidget(self.FileConifg)

        self.Operate = QWidget(self.Layout2)
        self.Operate.setObjectName(u"Operate")
        self.Operate.setMinimumSize(QSize(0, 0))
        self.Operate.setMaximumSize(QSize(16777215, 16777215))
        self.Operate.setCursor(QCursor(Qt.ArrowCursor))
        self.Operate.setLayoutDirection(Qt.LeftToRight)
        self.Operate.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.Operate)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, 9, 9)
        self.Save = QPushButton(self.Operate)
        self.Save.setObjectName(u"Save")
        sizePolicy1.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy1)
        self.Save.setFont(font)
        self.Save.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Save, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.horizontalLayout_5.addWidget(self.Operate)

        self.horizontalLayout_5.setStretch(0, 4)

        self.verticalLayout_12.addWidget(self.Layout2)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 0)
        self.title_label_2 = QLabel(self.page_2)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(16)
        self.title_label_2.setFont(font2)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.title_label_2)

        self.FunctionWindow = QGroupBox(self.page_2)
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)


        self.verticalLayout_7.addWidget(self.file_group_04)


        self.verticalLayout_8.addWidget(self.General_Config)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.FunctionWindow)

        self.Operate_2 = QGroupBox(self.page_2)
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
        self.general_operate_Button_04.setFont(font)
        self.general_operate_Button_04.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_04, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 0, 6, 1, 1)

        self.general_operate_Button_02 = QPushButton(self.Operate_2)
        self.general_operate_Button_02.setObjectName(u"general_operate_Button_02")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_02.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_02.setSizePolicy(sizePolicy1)
        self.general_operate_Button_02.setFont(font)
        self.general_operate_Button_02.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_02, 0, 1, 1, 1)

        self.general_operate_Button_05 = QPushButton(self.Operate_2)
        self.general_operate_Button_05.setObjectName(u"general_operate_Button_05")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_05.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_05.setSizePolicy(sizePolicy1)
        self.general_operate_Button_05.setFont(font)
        self.general_operate_Button_05.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_05, 0, 4, 1, 1)

        self.general_operate_Button_01 = QPushButton(self.Operate_2)
        self.general_operate_Button_01.setObjectName(u"general_operate_Button_01")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_01.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_01.setSizePolicy(sizePolicy1)
        self.general_operate_Button_01.setFont(font)
        self.general_operate_Button_01.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_01, 0, 0, 1, 1)

        self.general_operate_Button_03 = QPushButton(self.Operate_2)
        self.general_operate_Button_03.setObjectName(u"general_operate_Button_03")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_03.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_03.setSizePolicy(sizePolicy1)
        self.general_operate_Button_03.setFont(font)
        self.general_operate_Button_03.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_03, 0, 2, 1, 1)

        self.general_operate_Button_06 = QPushButton(self.Operate_2)
        self.general_operate_Button_06.setObjectName(u"general_operate_Button_06")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_06.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_06.setSizePolicy(sizePolicy1)
        self.general_operate_Button_06.setFont(font)
        self.general_operate_Button_06.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_06, 0, 5, 1, 1)


        self.verticalLayout_6.addWidget(self.Operate_2)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_2_layout = QVBoxLayout(self.page_3)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 0)
        self.scroll_area = QScrollArea(self.page_3)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 746, 522))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(16)
        self.title_label.setFont(font3)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_3)

        self.horizontalLayout_23.addWidget(self.pages)

#if QT_CONFIG(shortcut)
        self.title_label.setBuddy(self.select_group_01)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)
        self.ROIConfig.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.REF_CLK_Config_Label.setText(QCoreApplication.translate("MainPages", u"REF CLK", None))
        self.SYS_CLK_Config_Label.setText(QCoreApplication.translate("MainPages", u"SYS CLK", None))
        self.MST_MODE_Label.setText(QCoreApplication.translate("MainPages", u"MST_MODE", None))
        self.TRG_I_EN_Label.setText(QCoreApplication.translate("MainPages", u"TRG_I_EN", None))
        self.WORK_MODE_Label.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.MIPI_RATE_Label.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
        self.TDC_Bin_Width_Label.setText(QCoreApplication.translate("MainPages", u"TDC bin width", None))
        self.SCAN_MODE_Label.setText(QCoreApplication.translate("MainPages", u"SCAN_MODE", None))
        self.V_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_ROLL_NUM", None))
        self.V_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"32", None))
        self.H_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"H_ROLL_NUM", None))
        self.H_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.H_VLD_SEG_Label.setText(QCoreApplication.translate("MainPages", u"H_VLD_SEG", None))
        self.H_VLD_SEG_Value.setText(QCoreApplication.translate("MainPages", u"16", None))
        self.ROI_Shape_Light.setText(QCoreApplication.translate("MainPages", u"ROI shape", None))
        self.seg_hs_Label.setText(QCoreApplication.translate("MainPages", u"seg_hs", None))
        self.spad_vs_Label.setText(QCoreApplication.translate("MainPages", u"spad_vs", None))
        self.light_shift_Label.setText(QCoreApplication.translate("MainPages", u"light shift", None))
        self.sublight_shift_Label.setText(QCoreApplication.translate("MainPages", u"sublight shift", None))
        self.v_spad_shift_Label.setText(QCoreApplication.translate("MainPages", u"v_spad_shift", None))
        self.h_seg_shift_Label.setText(QCoreApplication.translate("MainPages", u"h_seg_shift", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config1byGUI), QCoreApplication.translate("MainPages", u"ROI_GUI", None))
        self.ROI_SRAM_File_Label_3.setText(QCoreApplication.translate("MainPages", u"ROI Coor", None))
        self.Load_ROI_file_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u6807\u5b9a\u6587\u4ef6", None))
        self.Load_ROI_file_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config2byCOOR), QCoreApplication.translate("MainPages", u"ROI_COOR", None))
        self.ROI_SRAM_File_Label_4.setText(QCoreApplication.translate("MainPages", u"Base ROI", None))
        self.Load_ROI_file_LineEdit_2.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u6807\u5b9a\u6587\u4ef6", None))
        self.Load_ROI_file_Button_2.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.seg_hs_Label_2.setText(QCoreApplication.translate("MainPages", u"Start Rolling", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config3ROIEdit), QCoreApplication.translate("MainPages", u"ROI Edit", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config4ROICali), QCoreApplication.translate("MainPages", u"ROI Cali", None))
        self.ROIZoneConfig.setText(QCoreApplication.translate("MainPages", u"<a href=\"https://www.example.com\">Others Config</a>", None))
        self.ROISave.setText(QCoreApplication.translate("MainPages", u"View", None))
        self.ROIView.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Layout2.setTitle("")
        self.ROI_SRAM_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.Sel_Config_file_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.ROI_SRAM_File_Label.setText(QCoreApplication.translate("MainPages", u"ROI SRAM File", None))
        self.ROI_Sram_File_CheckBox.setText(QCoreApplication.translate("MainPages", u"Include", None))
        self.SPadisApp_Path_Sel_Label.setText(QCoreApplication.translate("MainPages", u"SpadisApp", None))
        self.REG_CFG_File_Label.setText(QCoreApplication.translate("MainPages", u"REG CFG File", None))
        self.ROI_Zone_Sel_CheckBox.setText(QCoreApplication.translate("MainPages", u"Integration", None))
        self.Sel_Config_file_Label.setText(QCoreApplication.translate("MainPages", u"Base Script", None))
        self.SPadisApp_Path_Sel_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Sel_Config_file_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.REG_CFG_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.SPadisApp_Path_Sel__LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u6307\u5b9aSpadisApp\u8f6f\u4ef6\u8def\u5f84", None))
        self.Save.setText(QCoreApplication.translate("MainPages", u"Save", None))
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
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pageseRadgM.ui'
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
        MainPages.resize(776, 652)
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
        self.ScriptConfig = QGroupBox(self.page_1)
        self.ScriptConfig.setObjectName(u"ScriptConfig")
        self.horizontalLayout_2 = QHBoxLayout(self.ScriptConfig)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RegisterConfig = QFrame(self.ScriptConfig)
        self.RegisterConfig.setObjectName(u"RegisterConfig")
        self.RegisterConfig.setMinimumSize(QSize(0, 0))
        self.RegisterConfig.setMaximumSize(QSize(400, 16777215))
        self.formLayout_2 = QFormLayout(self.RegisterConfig)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(8)
        self.formLayout_2.setContentsMargins(9, 9, 9, 9)
        self.REF_CLK_Label = QLabel(self.RegisterConfig)
        self.REF_CLK_Label.setObjectName(u"REF_CLK_Label")
        self.REF_CLK_Label.setFont(font)
        self.REF_CLK_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.REF_CLK_Label)

        self.REF_CLK_ComboBox = QComboBox(self.RegisterConfig)
        self.REF_CLK_ComboBox.setObjectName(u"REF_CLK_ComboBox")
        self.REF_CLK_ComboBox.setMinimumSize(QSize(150, 0))
        self.REF_CLK_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.REF_CLK_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.REF_CLK_ComboBox)

        self.SYS_CLK_Label = QLabel(self.RegisterConfig)
        self.SYS_CLK_Label.setObjectName(u"SYS_CLK_Label")
        self.SYS_CLK_Label.setFont(font)
        self.SYS_CLK_Label.setFrameShape(QFrame.StyledPanel)
        self.SYS_CLK_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.SYS_CLK_Label)

        self.SYS_CLK_ComboBox = QComboBox(self.RegisterConfig)
        self.SYS_CLK_ComboBox.setObjectName(u"SYS_CLK_ComboBox")
        self.SYS_CLK_ComboBox.setEnabled(False)
        self.SYS_CLK_ComboBox.setMinimumSize(QSize(100, 0))
        self.SYS_CLK_ComboBox.setFont(font1)
        self.SYS_CLK_ComboBox.setEditable(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.SYS_CLK_ComboBox)

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

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.WORK_MODE_Label)

        self.WORK_MODE_ComboBox = QComboCheckBox(self.RegisterConfig)
        self.WORK_MODE_ComboBox.setObjectName(u"WORK_MODE_ComboBox")
        self.WORK_MODE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.WORK_MODE_ComboBox)

        self.TRG_I_EN_Label = QLabel(self.RegisterConfig)
        self.TRG_I_EN_Label.setObjectName(u"TRG_I_EN_Label")
        self.TRG_I_EN_Label.setMinimumSize(QSize(85, 0))
        self.TRG_I_EN_Label.setMaximumSize(QSize(85, 16777215))
        self.TRG_I_EN_Label.setFont(font)
        self.TRG_I_EN_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.TRG_I_EN_Label)

        self.TRG_I_EN_ComboBox = QComboBox(self.RegisterConfig)
        self.TRG_I_EN_ComboBox.setObjectName(u"TRG_I_EN_ComboBox")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.TRG_I_EN_ComboBox)

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

        self.MIPI_RATE_ComboBox = QComboBox(self.RegisterConfig)
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

        self.SCAN_MODE_Label = QLabel(self.RegisterConfig)
        self.SCAN_MODE_Label.setObjectName(u"SCAN_MODE_Label")
        self.SCAN_MODE_Label.setMinimumSize(QSize(0, 0))
        self.SCAN_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.SCAN_MODE_Label.setFont(font1)
        self.SCAN_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.SCAN_MODE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.SCAN_MODE_Label)

        self.SCAN_MODE_ComboBox = QComboBox(self.RegisterConfig)
        self.SCAN_MODE_ComboBox.setObjectName(u"SCAN_MODE_ComboBox")
        self.SCAN_MODE_ComboBox.setMinimumSize(QSize(150, 0))
        self.SCAN_MODE_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.SCAN_MODE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.SCAN_MODE_ComboBox)

        self.V_ROLL_NUM_Label = QLabel(self.RegisterConfig)
        self.V_ROLL_NUM_Label.setObjectName(u"V_ROLL_NUM_Label")
        self.V_ROLL_NUM_Label.setMinimumSize(QSize(0, 0))
        self.V_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.V_ROLL_NUM_Label.setFont(font1)
        self.V_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.V_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.V_ROLL_NUM_Label)

        self.V_ROLL_NUM_CMP = QHBoxLayout()
        self.V_ROLL_NUM_CMP.setSpacing(0)
        self.V_ROLL_NUM_CMP.setObjectName(u"V_ROLL_NUM_CMP")
        self.V_ROLL_NUM_CMP.setContentsMargins(0, -1, 0, -1)
        self.V_ROLL_NUM_Slider = QSlider(self.RegisterConfig)
        self.V_ROLL_NUM_Slider.setObjectName(u"V_ROLL_NUM_Slider")
        self.V_ROLL_NUM_Slider.setMouseTracking(False)
        self.V_ROLL_NUM_Slider.setMinimum(1)
        self.V_ROLL_NUM_Slider.setMaximum(32)
        self.V_ROLL_NUM_Slider.setPageStep(1)
        self.V_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Slider)

        self.V_ROLL_NUM_Value = QLabel(self.RegisterConfig)
        self.V_ROLL_NUM_Value.setObjectName(u"V_ROLL_NUM_Value")
        self.V_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.V_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.V_ROLL_NUM_Value.setFont(font1)
        self.V_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.V_ROLL_NUM_Value.setWordWrap(True)
        self.V_ROLL_NUM_Value.setMargin(0)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Value)


        self.formLayout_2.setLayout(8, QFormLayout.FieldRole, self.V_ROLL_NUM_CMP)

        self.H_ROLL_NUM_Label = QLabel(self.RegisterConfig)
        self.H_ROLL_NUM_Label.setObjectName(u"H_ROLL_NUM_Label")
        self.H_ROLL_NUM_Label.setMinimumSize(QSize(0, 0))
        self.H_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_ROLL_NUM_Label.setFont(font1)
        self.H_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.H_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.H_ROLL_NUM_Label)

        self.H_ROLL_CMP = QHBoxLayout()
        self.H_ROLL_CMP.setSpacing(0)
        self.H_ROLL_CMP.setObjectName(u"H_ROLL_CMP")
        self.H_ROLL_CMP.setContentsMargins(0, -1, -1, -1)
        self.H_ROLL_NUM_Slider = QSlider(self.RegisterConfig)
        self.H_ROLL_NUM_Slider.setObjectName(u"H_ROLL_NUM_Slider")
        self.H_ROLL_NUM_Slider.setEnabled(True)
        self.H_ROLL_NUM_Slider.setMinimum(1)
        self.H_ROLL_NUM_Slider.setMaximum(16)
        self.H_ROLL_NUM_Slider.setPageStep(1)
        self.H_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Slider)

        self.H_ROLL_NUM_Value = QLabel(self.RegisterConfig)
        self.H_ROLL_NUM_Value.setObjectName(u"H_ROLL_NUM_Value")
        self.H_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.H_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.H_ROLL_NUM_Value.setFont(font1)
        self.H_ROLL_NUM_Value.setMidLineWidth(0)
        self.H_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_ROLL_NUM_Value.setMargin(0)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Value)


        self.formLayout_2.setLayout(9, QFormLayout.FieldRole, self.H_ROLL_CMP)

        self.H_VLD_SEG_Label = QLabel(self.RegisterConfig)
        self.H_VLD_SEG_Label.setObjectName(u"H_VLD_SEG_Label")
        self.H_VLD_SEG_Label.setMinimumSize(QSize(0, 0))
        self.H_VLD_SEG_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_VLD_SEG_Label.setFont(font1)
        self.H_VLD_SEG_Label.setFrameShape(QFrame.StyledPanel)
        self.H_VLD_SEG_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.H_VLD_SEG_Label)

        self.H_VLD_SEG_CMP = QHBoxLayout()
        self.H_VLD_SEG_CMP.setSpacing(0)
        self.H_VLD_SEG_CMP.setObjectName(u"H_VLD_SEG_CMP")
        self.H_VLD_SEG_CMP.setContentsMargins(0, -1, -1, -1)
        self.H_VLD_SEG_Slider = QSlider(self.RegisterConfig)
        self.H_VLD_SEG_Slider.setObjectName(u"H_VLD_SEG_Slider")
        self.H_VLD_SEG_Slider.setMinimum(1)
        self.H_VLD_SEG_Slider.setMaximum(16)
        self.H_VLD_SEG_Slider.setPageStep(1)
        self.H_VLD_SEG_Slider.setOrientation(Qt.Horizontal)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Slider)

        self.H_VLD_SEG_Value = QLabel(self.RegisterConfig)
        self.H_VLD_SEG_Value.setObjectName(u"H_VLD_SEG_Value")
        self.H_VLD_SEG_Value.setMinimumSize(QSize(20, 25))
        self.H_VLD_SEG_Value.setMaximumSize(QSize(20, 16777215))
        self.H_VLD_SEG_Value.setFont(font1)
        self.H_VLD_SEG_Value.setTextFormat(Qt.MarkdownText)
        self.H_VLD_SEG_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_VLD_SEG_Value.setMargin(0)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Value)


        self.formLayout_2.setLayout(10, QFormLayout.FieldRole, self.H_VLD_SEG_CMP)


        self.horizontalLayout_2.addWidget(self.RegisterConfig)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.ROIConfigGroup = QGroupBox(self.ScriptConfig)
        self.ROIConfigGroup.setObjectName(u"ROIConfigGroup")
        self.ROIConfigGroup.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.ROIConfigGroup)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 6)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 307, 382))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 20, 0)
        self.seg_hs_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.seg_hs_Label.setObjectName(u"seg_hs_Label")
        self.seg_hs_Label.setMinimumSize(QSize(0, 0))
        self.seg_hs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.seg_hs_Label.setFont(font1)
        self.seg_hs_Label.setFrameShape(QFrame.StyledPanel)
        self.seg_hs_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.seg_hs_Label)

        self.seg_hs_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.seg_hs_spinBox.setObjectName(u"seg_hs_spinBox")
        self.seg_hs_spinBox.setMinimum(0)
        self.seg_hs_spinBox.setMaximum(15)
        self.seg_hs_spinBox.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.seg_hs_spinBox)

        self.spad_vs_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.spad_vs_Label.setObjectName(u"spad_vs_Label")
        self.spad_vs_Label.setMinimumSize(QSize(0, 0))
        self.spad_vs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.spad_vs_Label.setFont(font1)
        self.spad_vs_Label.setFrameShape(QFrame.StyledPanel)
        self.spad_vs_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.spad_vs_Label)

        self.spad_vs_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spad_vs_spinBox.setObjectName(u"spad_vs_spinBox")
        self.spad_vs_spinBox.setMinimum(0)
        self.spad_vs_spinBox.setMaximum(575)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spad_vs_spinBox)

        self.light_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.light_shift_Label.setObjectName(u"light_shift_Label")
        self.light_shift_Label.setMinimumSize(QSize(0, 0))
        self.light_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.light_shift_Label.setFont(font1)
        self.light_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.light_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.light_shift_Label)

        self.light_shift_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.light_shift_spinBox.setObjectName(u"light_shift_spinBox")
        self.light_shift_spinBox.setMinimum(-576)
        self.light_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.light_shift_spinBox)

        self.sublight_shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.sublight_shift_Label.setObjectName(u"sublight_shift_Label")
        self.sublight_shift_Label.setMinimumSize(QSize(0, 0))
        self.sublight_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.sublight_shift_Label.setFont(font1)
        self.sublight_shift_Label.setFrameShape(QFrame.StyledPanel)
        self.sublight_shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sublight_shift_Label)

        self.sublight_shift_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.sublight_shift_spinBox.setObjectName(u"sublight_shift_spinBox")
        self.sublight_shift_spinBox.setMinimum(-576)
        self.sublight_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sublight_shift_spinBox)

        self.ROI_Shape_Light = QLabel(self.scrollAreaWidgetContents_2)
        self.ROI_Shape_Light.setObjectName(u"ROI_Shape_Light")
        self.ROI_Shape_Light.setMinimumSize(QSize(0, 0))
        self.ROI_Shape_Light.setMaximumSize(QSize(16777215, 16777215))
        self.ROI_Shape_Light.setFont(font1)
        self.ROI_Shape_Light.setFrameShape(QFrame.StyledPanel)
        self.ROI_Shape_Light.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.ROI_Shape_Light)

        self.ROI_Shape_ComboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.ROI_Shape_ComboBox.addItem("")
        self.ROI_Shape_ComboBox.addItem("")
        self.ROI_Shape_ComboBox.setObjectName(u"ROI_Shape_ComboBox")
        self.ROI_Shape_ComboBox.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ROI_Shape_ComboBox)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 307, 382))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 20, 0)
        self.ROI_File_Load_Label = QLabel(self.scrollAreaWidgetContents_3)
        self.ROI_File_Load_Label.setObjectName(u"ROI_File_Load_Label")
        self.ROI_File_Load_Label.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.ROI_File_Load_Label)

        self.ROI_File_Load_Layout = QHBoxLayout()
        self.ROI_File_Load_Layout.setSpacing(9)
        self.ROI_File_Load_Layout.setObjectName(u"ROI_File_Load_Layout")
        self.ROI_File_Load_LineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ROI_File_Load_LineEdit.setObjectName(u"ROI_File_Load_LineEdit")
        self.ROI_File_Load_LineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ROI_File_Load_LineEdit.sizePolicy().hasHeightForWidth())
        self.ROI_File_Load_LineEdit.setSizePolicy(sizePolicy1)
        self.ROI_File_Load_LineEdit.setMinimumSize(QSize(0, 0))
        self.ROI_File_Load_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.ROI_File_Load_LineEdit.setReadOnly(True)

        self.ROI_File_Load_Layout.addWidget(self.ROI_File_Load_LineEdit)

        self.ROI_File_Load_Button = QPushButton(self.scrollAreaWidgetContents_3)
        self.ROI_File_Load_Button.setObjectName(u"ROI_File_Load_Button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ROI_File_Load_Button.sizePolicy().hasHeightForWidth())
        self.ROI_File_Load_Button.setSizePolicy(sizePolicy2)
        self.ROI_File_Load_Button.setFocusPolicy(Qt.WheelFocus)

        self.ROI_File_Load_Layout.addWidget(self.ROI_File_Load_Button)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.ROI_File_Load_Layout)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 307, 382))
        self.formLayout_5 = QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(10)
        self.formLayout_5.setVerticalSpacing(6)
        self.formLayout_5.setContentsMargins(0, 0, 20, 0)
        self.base_roi_file_Label = QLabel(self.scrollAreaWidgetContents_4)
        self.base_roi_file_Label.setObjectName(u"base_roi_file_Label")
        self.base_roi_file_Label.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.base_roi_file_Label)

        self.base_roi_file_Layout = QHBoxLayout()
        self.base_roi_file_Layout.setSpacing(9)
        self.base_roi_file_Layout.setObjectName(u"base_roi_file_Layout")
        self.base_roi_file_LineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.base_roi_file_LineEdit.setObjectName(u"base_roi_file_LineEdit")
        self.base_roi_file_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.base_roi_file_LineEdit.sizePolicy().hasHeightForWidth())
        self.base_roi_file_LineEdit.setSizePolicy(sizePolicy1)
        self.base_roi_file_LineEdit.setMinimumSize(QSize(0, 0))
        self.base_roi_file_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.base_roi_file_LineEdit.setReadOnly(True)

        self.base_roi_file_Layout.addWidget(self.base_roi_file_LineEdit)

        self.base_roi_file_Button = QPushButton(self.scrollAreaWidgetContents_4)
        self.base_roi_file_Button.setObjectName(u"base_roi_file_Button")
        sizePolicy2.setHeightForWidth(self.base_roi_file_Button.sizePolicy().hasHeightForWidth())
        self.base_roi_file_Button.setSizePolicy(sizePolicy2)
        self.base_roi_file_Button.setFocusPolicy(Qt.WheelFocus)

        self.base_roi_file_Layout.addWidget(self.base_roi_file_Button)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.base_roi_file_Layout)

        self.start_rolling_Label = QLabel(self.scrollAreaWidgetContents_4)
        self.start_rolling_Label.setObjectName(u"start_rolling_Label")
        self.start_rolling_Label.setMinimumSize(QSize(0, 0))
        self.start_rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.start_rolling_Label.setFont(font1)
        self.start_rolling_Label.setFrameShape(QFrame.NoFrame)
        self.start_rolling_Label.setFrameShadow(QFrame.Raised)
        self.start_rolling_Label.setTextFormat(Qt.PlainText)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.start_rolling_Label)

        self.End_rolling_Label = QLabel(self.scrollAreaWidgetContents_4)
        self.End_rolling_Label.setObjectName(u"End_rolling_Label")
        self.End_rolling_Label.setMinimumSize(QSize(0, 0))
        self.End_rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.End_rolling_Label.setFont(font1)
        self.End_rolling_Label.setFrameShape(QFrame.NoFrame)
        self.End_rolling_Label.setFrameShadow(QFrame.Raised)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.End_rolling_Label)

        self.End_rolling_SpinBox = QSpinBox(self.scrollAreaWidgetContents_4)
        self.End_rolling_SpinBox.setObjectName(u"End_rolling_SpinBox")
        self.End_rolling_SpinBox.setMinimum(1)
        self.End_rolling_SpinBox.setMaximum(32)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.End_rolling_SpinBox)

        self.start_rolling_SpinBox = QSpinBox(self.scrollAreaWidgetContents_4)
        self.start_rolling_SpinBox.setObjectName(u"start_rolling_SpinBox")
        self.start_rolling_SpinBox.setMinimum(1)
        self.start_rolling_SpinBox.setMaximum(32)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.start_rolling_SpinBox)

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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 307, 373))
        self.formLayout_7 = QFormLayout(self.scrollAreaWidgetContents_6)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(10)
        self.formLayout_7.setVerticalSpacing(6)
        self.formLayout_7.setContentsMargins(0, 0, 20, 0)
        self.cali_file_path_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.cali_file_path_Label.setObjectName(u"cali_file_path_Label")
        self.cali_file_path_Label.setFont(font1)
        self.cali_file_path_Label.setFrameShape(QFrame.NoFrame)

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
        self.img_mirror_Label.setFont(font1)
        self.img_mirror_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.img_mirror_Label)

        self.img_mirror_ComboBox = QComboBox(self.scrollAreaWidgetContents_6)
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
        self.remove_noise_Label.setFont(font1)
        self.remove_noise_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.remove_noise_Label)

        self.remove_noise_ComboBox = QComboBox(self.scrollAreaWidgetContents_6)
        self.remove_noise_ComboBox.addItem("")
        self.remove_noise_ComboBox.addItem("")
        self.remove_noise_ComboBox.setObjectName(u"remove_noise_ComboBox")
        self.remove_noise_ComboBox.setMinimumSize(QSize(150, 0))
        self.remove_noise_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.remove_noise_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.remove_noise_ComboBox)

        self.light_smooth_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.light_smooth_Label.setObjectName(u"light_smooth_Label")
        self.light_smooth_Label.setFont(font1)
        self.light_smooth_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.light_smooth_Label)

        self.light_smooth_ComboBox = QComboBox(self.scrollAreaWidgetContents_6)
        self.light_smooth_ComboBox.addItem("")
        self.light_smooth_ComboBox.addItem("")
        self.light_smooth_ComboBox.setObjectName(u"light_smooth_ComboBox")
        self.light_smooth_ComboBox.setMinimumSize(QSize(150, 0))
        self.light_smooth_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.light_smooth_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.light_smooth_ComboBox)

        self.curvature_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.curvature_Label.setObjectName(u"curvature_Label")
        self.curvature_Label.setFont(font1)
        self.curvature_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.curvature_Label)

        self.curvature_SpinBox = QSpinBox(self.scrollAreaWidgetContents_6)
        self.curvature_SpinBox.setObjectName(u"curvature_SpinBox")
        self.curvature_SpinBox.setMinimum(0)
        self.curvature_SpinBox.setMaximum(1000)
        self.curvature_SpinBox.setValue(2)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.curvature_SpinBox)

        self.correct_thres_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.correct_thres_Label.setObjectName(u"correct_thres_Label")
        self.correct_thres_Label.setFont(font1)
        self.correct_thres_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.correct_thres_Label)

        self.correct_thres_SpinBox = QSpinBox(self.scrollAreaWidgetContents_6)
        self.correct_thres_SpinBox.setObjectName(u"correct_thres_SpinBox")
        self.correct_thres_SpinBox.setMinimum(0)
        self.correct_thres_SpinBox.setMaximum(100)
        self.correct_thres_SpinBox.setValue(1)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.correct_thres_SpinBox)

        self.cali_order_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.cali_order_Label.setObjectName(u"cali_order_Label")
        self.cali_order_Label.setFont(font1)
        self.cali_order_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.cali_order_Label)

        self.cali_order_ComboBox = QComboBox(self.scrollAreaWidgetContents_6)
        self.cali_order_ComboBox.addItem("")
        self.cali_order_ComboBox.addItem("")
        self.cali_order_ComboBox.setObjectName(u"cali_order_ComboBox")
        self.cali_order_ComboBox.setMinimumSize(QSize(150, 0))
        self.cali_order_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.cali_order_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.cali_order_ComboBox)

        self.cali_frm_num_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.cali_frm_num_Label.setObjectName(u"cali_frm_num_Label")
        self.cali_frm_num_Label.setFont(font1)
        self.cali_frm_num_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.cali_frm_num_Label)

        self.cali_frm_num__SpinBox = QSpinBox(self.scrollAreaWidgetContents_6)
        self.cali_frm_num__SpinBox.setObjectName(u"cali_frm_num__SpinBox")
        self.cali_frm_num__SpinBox.setMinimum(1)
        self.cali_frm_num__SpinBox.setMaximum(10000)

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.cali_frm_num__SpinBox)

        self.ref_segment_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.ref_segment_Label.setObjectName(u"ref_segment_Label")
        self.ref_segment_Label.setFont(font1)
        self.ref_segment_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.ref_segment_Label)

        self.ref_segment_SpinBox = QSpinBox(self.scrollAreaWidgetContents_6)
        self.ref_segment_SpinBox.setObjectName(u"ref_segment_SpinBox")
        self.ref_segment_SpinBox.setMinimum(0)
        self.ref_segment_SpinBox.setMaximum(16)
        self.ref_segment_SpinBox.setValue(0)

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.ref_segment_SpinBox)

        self.mode_2D_Label = QLabel(self.scrollAreaWidgetContents_6)
        self.mode_2D_Label.setObjectName(u"mode_2D_Label")
        self.mode_2D_Label.setFont(font1)
        self.mode_2D_Label.setFrameShape(QFrame.NoFrame)

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.mode_2D_Label)

        self.mode_2D_ComboBox = QComboBox(self.scrollAreaWidgetContents_6)
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
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, -1)
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

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_12.addWidget(self.ScriptConfig)

        self.FileConifg = QGroupBox(self.page_1)
        self.FileConifg.setObjectName(u"FileConifg")
        self.FileConifg.setMinimumSize(QSize(300, 0))
        self.FileConifg.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_6 = QGridLayout(self.FileConifg)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 9, 9, 9)
        self.roi_sram_name_Label = QLabel(self.FileConifg)
        self.roi_sram_name_Label.setObjectName(u"roi_sram_name_Label")
        self.roi_sram_name_Label.setFont(font)

        self.gridLayout_6.addWidget(self.roi_sram_name_Label, 4, 0, 1, 1)

        self.file_save_dir_Label = QLabel(self.FileConifg)
        self.file_save_dir_Label.setObjectName(u"file_save_dir_Label")
        self.file_save_dir_Label.setMinimumSize(QSize(0, 0))
        self.file_save_dir_Label.setMaximumSize(QSize(16777215, 16777215))
        self.file_save_dir_Label.setFont(font1)
        self.file_save_dir_Label.setFrameShape(QFrame.NoFrame)
        self.file_save_dir_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.file_save_dir_Label, 6, 0, 1, 1)

        self.roi_sram_name_LineEdit = QLineEdit(self.FileConifg)
        self.roi_sram_name_LineEdit.setObjectName(u"roi_sram_name_LineEdit")
        self.roi_sram_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.roi_sram_name_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.roi_sram_name_LineEdit, 4, 1, 1, 1)

        self.roi_sram_name_CheckBox = QCheckBox(self.FileConifg)
        self.roi_sram_name_CheckBox.setObjectName(u"roi_sram_name_CheckBox")

        self.gridLayout_6.addWidget(self.roi_sram_name_CheckBox, 4, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 6, 4, 1, 1)

        self.file_save_dir_Button = QPushButton(self.FileConifg)
        self.file_save_dir_Button.setObjectName(u"file_save_dir_Button")
        sizePolicy2.setHeightForWidth(self.file_save_dir_Button.sizePolicy().hasHeightForWidth())
        self.file_save_dir_Button.setSizePolicy(sizePolicy2)
        self.file_save_dir_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.file_save_dir_Button, 6, 2, 1, 1)

        self.SPADISS_Integration_CheckBox = QCheckBox(self.FileConifg)
        self.SPADISS_Integration_CheckBox.setObjectName(u"SPADISS_Integration_CheckBox")

        self.gridLayout_6.addWidget(self.SPADISS_Integration_CheckBox, 6, 3, 1, 1)

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

        self.reg_script_name_Label = QLabel(self.FileConifg)
        self.reg_script_name_Label.setObjectName(u"reg_script_name_Label")
        self.reg_script_name_Label.setFont(font)

        self.gridLayout_6.addWidget(self.reg_script_name_Label, 2, 0, 1, 1)

        self.reg_script_name_LineEdit = QLineEdit(self.FileConifg)
        self.reg_script_name_LineEdit.setObjectName(u"reg_script_name_LineEdit")
        self.reg_script_name_LineEdit.setMinimumSize(QSize(0, 0))
        self.reg_script_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.reg_script_name_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.reg_script_name_LineEdit, 2, 1, 1, 1)

        self.reference_script_Label = QLabel(self.FileConifg)
        self.reference_script_Label.setObjectName(u"reference_script_Label")
        self.reference_script_Label.setMinimumSize(QSize(0, 0))
        self.reference_script_Label.setMaximumSize(QSize(16777215, 16777215))
        self.reference_script_Label.setFont(font1)
        self.reference_script_Label.setFrameShape(QFrame.NoFrame)
        self.reference_script_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.reference_script_Label, 1, 0, 1, 1)

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

        self.reference_script_Button = QPushButton(self.FileConifg)
        self.reference_script_Button.setObjectName(u"reference_script_Button")
        sizePolicy2.setHeightForWidth(self.reference_script_Button.sizePolicy().hasHeightForWidth())
        self.reference_script_Button.setSizePolicy(sizePolicy2)
        self.reference_script_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.reference_script_Button, 1, 2, 1, 1)


        self.verticalLayout_12.addWidget(self.FileConifg)

        self.Operate = QGroupBox(self.page_1)
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
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.Save = QPushButton(self.Operate)
        self.Save.setObjectName(u"Save")
        sizePolicy1.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy1)
        self.Save.setMinimumSize(QSize(90, 0))
        self.Save.setFont(font)
        self.Save.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Save, 0, 0, 1, 1)

        self.Test = QPushButton(self.Operate)
        self.Test.setObjectName(u"Test")
        sizePolicy1.setHeightForWidth(self.Test.sizePolicy().hasHeightForWidth())
        self.Test.setSizePolicy(sizePolicy1)
        self.Test.setMinimumSize(QSize(90, 0))
        self.Test.setFont(font)
        self.Test.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Test, 0, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.Operate)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.verticalLayout_12.addItem(self.verticalSpacer)

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
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(16)
        self.title_label_2.setFont(font3)
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
        self.general_operate_Button_04.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_04.setFont(font)
        self.general_operate_Button_04.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_04, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.contents.setGeometry(QRect(0, 0, 233, 256))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(16)
        self.title_label.setFont(font4)
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
        self.H_ROLL_NUM_Slider.valueChanged.connect(self.H_ROLL_NUM_Value.setNum)
        self.H_VLD_SEG_Slider.valueChanged.connect(self.H_VLD_SEG_Value.setNum)
        self.V_ROLL_NUM_Slider.valueChanged.connect(self.V_ROLL_NUM_Value.setNum)

        self.pages.setCurrentIndex(0)
        self.ROIConfig.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.REF_CLK_Label.setText(QCoreApplication.translate("MainPages", u"REF CLK", None))
        self.SYS_CLK_Label.setText(QCoreApplication.translate("MainPages", u"SYS CLK", None))
        self.MST_MODE_Label.setText(QCoreApplication.translate("MainPages", u"MST_MODE", None))
        self.WORK_MODE_Label.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.TRG_I_EN_Label.setText(QCoreApplication.translate("MainPages", u"TRG_I_EN", None))
        self.MIPI_RATE_Label.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
        self.TDC_Bin_Width_Label.setText(QCoreApplication.translate("MainPages", u"TDC bin width", None))
        self.SCAN_MODE_Label.setText(QCoreApplication.translate("MainPages", u"SCAN_MODE", None))
        self.V_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_ROLL_NUM", None))
        self.V_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"32", None))
        self.H_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"H_ROLL_NUM", None))
        self.H_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.H_VLD_SEG_Label.setText(QCoreApplication.translate("MainPages", u"H_VLD_SEG", None))
        self.H_VLD_SEG_Value.setText(QCoreApplication.translate("MainPages", u"16", None))
        self.seg_hs_Label.setText(QCoreApplication.translate("MainPages", u"seg_hs", None))
        self.spad_vs_Label.setText(QCoreApplication.translate("MainPages", u"spad_vs", None))
        self.light_shift_Label.setText(QCoreApplication.translate("MainPages", u"light shift", None))
        self.sublight_shift_Label.setText(QCoreApplication.translate("MainPages", u"sublight shift", None))
        self.ROI_Shape_Light.setText(QCoreApplication.translate("MainPages", u"ROI shape", None))
        self.ROI_Shape_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Straight", None))
        self.ROI_Shape_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Curve", None))

        self.v_spad_shift_Label.setText(QCoreApplication.translate("MainPages", u"v_spad_shift", None))
        self.h_seg_shift_Label.setText(QCoreApplication.translate("MainPages", u"h_seg_shift", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config1byGUI), QCoreApplication.translate("MainPages", u"ROI GUI", None))
        self.ROI_File_Load_Label.setText(QCoreApplication.translate("MainPages", u"ROI File", None))
        self.ROI_File_Load_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u6807\u5b9a\u6587\u4ef6", None))
        self.ROI_File_Load_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config2byCOOR), QCoreApplication.translate("MainPages", u"ROI COOR", None))
        self.base_roi_file_Label.setText(QCoreApplication.translate("MainPages", u"Base ROI", None))
        self.base_roi_file_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u4fee\u6539\u7684ROI\u6587\u4ef6", None))
        self.base_roi_file_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.start_rolling_Label.setText(QCoreApplication.translate("MainPages", u"Start Rolling", None))
        self.End_rolling_Label.setText(QCoreApplication.translate("MainPages", u"End Rolling", None))
        self.ROIConfig.setTabText(self.ROIConfig.indexOf(self.Config3ROIEdit), QCoreApplication.translate("MainPages", u"ROI Edit", None))
        self.cali_file_path_Label.setText(QCoreApplication.translate("MainPages", u"Cali Filer", None))
        self.cali_file_path_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u6807\u5b9a\u7684ROI\u6587\u4ef6", None))
        self.cali_file_path_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.img_mirror_Label.setText(QCoreApplication.translate("MainPages", u"Img Mirror ", None))
        self.img_mirror_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No mirror", None))
        self.img_mirror_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"X-axis mirror", None))
        self.img_mirror_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"Y-axis mirror", None))
        self.img_mirror_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"X-axis and Y-axis mirror", None))

        self.remove_noise_Label.setText(QCoreApplication.translate("MainPages", u"remove noise", None))
        self.remove_noise_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Yes", None))
        self.remove_noise_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"No", None))

        self.light_smooth_Label.setText(QCoreApplication.translate("MainPages", u"light smooth", None))
        self.light_smooth_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Yes", None))
        self.light_smooth_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"No", None))

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
        self.file_save_dir_Label.setText(QCoreApplication.translate("MainPages", u"File Save Path", None))
        self.roi_sram_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.roi_sram_name_CheckBox.setText(QCoreApplication.translate("MainPages", u"Include", None))
        self.file_save_dir_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.SPADISS_Integration_CheckBox.setText(QCoreApplication.translate("MainPages", u"Integration", None))
        self.file_save_dir_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u6307\u5b9aSpadisApp\u8f6f\u4ef6\u8def\u5f84", None))
        self.reg_script_name_Label.setText(QCoreApplication.translate("MainPages", u"Reg Script Name", None))
        self.reg_script_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.reference_script_Label.setText(QCoreApplication.translate("MainPages", u"Reference Script", None))
        self.reference_script_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.reference_script_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Save.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Test.setText(QCoreApplication.translate("MainPages", u"Test", None))
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


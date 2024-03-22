# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesyJiYgV.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(875, 668)
        MainPages.setStyleSheet(u"")
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.MainPage = QHBoxLayout()
        self.MainPage.setObjectName(u"MainPage")
        self.ShowPage = QVBoxLayout()
        self.ShowPage.setObjectName(u"ShowPage")
        self.ShowPage.setContentsMargins(-1, 7, -1, -1)

        self.MainPage.addLayout(self.ShowPage)

        self.OperateFrame = QFrame(self.page_1)
        self.OperateFrame.setObjectName(u"OperateFrame")
        self.OperateFrame.setMaximumSize(QSize(420, 16777215))
        self.OperateFrame.setStyleSheet(u"")
        self.OperateFrame.setFrameShape(QFrame.NoFrame)
        self.OperatePage = QVBoxLayout(self.OperateFrame)
        self.OperatePage.setSpacing(6)
        self.OperatePage.setObjectName(u"OperatePage")
        self.OperatePage.setContentsMargins(0, 0, 0, 0)
        self.Config = QGroupBox(self.OperateFrame)
        self.Config.setObjectName(u"Config")
        self.Config.setMinimumSize(QSize(0, 0))
        self.Config.setMaximumSize(QSize(500, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.Config.setFont(font1)
        self.Config.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.Config)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.Config)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 220, 207))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.WORK_MODE_Label = QLabel(self.scrollAreaWidgetContents_2)
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

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.WORK_MODE_Label)

        self.WORK_MODE_ComboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.WORK_MODE_ComboBox.setObjectName(u"WORK_MODE_ComboBox")
        self.WORK_MODE_ComboBox.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.WORK_MODE_ComboBox)

        self.MIPI_RATE_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.MIPI_RATE_Label.setObjectName(u"MIPI_RATE_Label")
        sizePolicy.setHeightForWidth(self.MIPI_RATE_Label.sizePolicy().hasHeightForWidth())
        self.MIPI_RATE_Label.setSizePolicy(sizePolicy)
        self.MIPI_RATE_Label.setMinimumSize(QSize(0, 0))
        self.MIPI_RATE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.MIPI_RATE_Label.setFont(font1)
        self.MIPI_RATE_Label.setFrameShape(QFrame.StyledPanel)
        self.MIPI_RATE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.MIPI_RATE_Label)

        self.MIPI_RATE_ComboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.MIPI_RATE_ComboBox.setObjectName(u"MIPI_RATE_ComboBox")
        self.MIPI_RATE_ComboBox.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.MIPI_RATE_ComboBox)

        self.SCAN_MODE_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.SCAN_MODE_Label.setObjectName(u"SCAN_MODE_Label")
        self.SCAN_MODE_Label.setMinimumSize(QSize(0, 0))
        self.SCAN_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.SCAN_MODE_Label.setFont(font1)
        self.SCAN_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.SCAN_MODE_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.SCAN_MODE_Label)

        self.SCAN_MODE_ComboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.SCAN_MODE_ComboBox.setObjectName(u"SCAN_MODE_ComboBox")
        self.SCAN_MODE_ComboBox.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.SCAN_MODE_ComboBox)

        self.V_ROLL_NUM_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.V_ROLL_NUM_Label.setObjectName(u"V_ROLL_NUM_Label")
        self.V_ROLL_NUM_Label.setMinimumSize(QSize(0, 0))
        self.V_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.V_ROLL_NUM_Label.setFont(font1)
        self.V_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.V_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.V_ROLL_NUM_Label)

        self.H_ROLL_NUM_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.H_ROLL_NUM_Label.setObjectName(u"H_ROLL_NUM_Label")
        self.H_ROLL_NUM_Label.setMinimumSize(QSize(0, 0))
        self.H_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_ROLL_NUM_Label.setFont(font1)
        self.H_ROLL_NUM_Label.setFrameShape(QFrame.StyledPanel)
        self.H_ROLL_NUM_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.H_ROLL_NUM_Label)

        self.H_VLD_SEG_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.H_VLD_SEG_Label.setObjectName(u"H_VLD_SEG_Label")
        self.H_VLD_SEG_Label.setMinimumSize(QSize(0, 0))
        self.H_VLD_SEG_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_VLD_SEG_Label.setFont(font1)
        self.H_VLD_SEG_Label.setFrameShape(QFrame.StyledPanel)
        self.H_VLD_SEG_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.H_VLD_SEG_Label)

        self.H_SEG_Shift_Label = QLabel(self.scrollAreaWidgetContents_2)
        self.H_SEG_Shift_Label.setObjectName(u"H_SEG_Shift_Label")
        self.H_SEG_Shift_Label.setMinimumSize(QSize(0, 0))
        self.H_SEG_Shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.H_SEG_Shift_Label.setFont(font1)
        self.H_SEG_Shift_Label.setFrameShape(QFrame.StyledPanel)
        self.H_SEG_Shift_Label.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.H_SEG_Shift_Label)

        self.V_ROLL_NUM_CMP = QHBoxLayout()
        self.V_ROLL_NUM_CMP.setSpacing(0)
        self.V_ROLL_NUM_CMP.setObjectName(u"V_ROLL_NUM_CMP")
        self.V_ROLL_NUM_CMP.setContentsMargins(0, -1, 0, -1)
        self.V_ROLL_NUM_Slider = QSlider(self.scrollAreaWidgetContents_2)
        self.V_ROLL_NUM_Slider.setObjectName(u"V_ROLL_NUM_Slider")
        self.V_ROLL_NUM_Slider.setMouseTracking(False)
        self.V_ROLL_NUM_Slider.setMinimum(1)
        self.V_ROLL_NUM_Slider.setMaximum(32)
        self.V_ROLL_NUM_Slider.setPageStep(1)
        self.V_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Slider)

        self.V_ROLL_NUM_Value = QLabel(self.scrollAreaWidgetContents_2)
        self.V_ROLL_NUM_Value.setObjectName(u"V_ROLL_NUM_Value")
        self.V_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.V_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.V_ROLL_NUM_Value.setFont(font1)
        self.V_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.V_ROLL_NUM_Value.setWordWrap(True)
        self.V_ROLL_NUM_Value.setMargin(0)

        self.V_ROLL_NUM_CMP.addWidget(self.V_ROLL_NUM_Value)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.V_ROLL_NUM_CMP)

        self.H_ROLL_CMP = QHBoxLayout()
        self.H_ROLL_CMP.setSpacing(0)
        self.H_ROLL_CMP.setObjectName(u"H_ROLL_CMP")
        self.H_ROLL_CMP.setContentsMargins(0, -1, -1, -1)
        self.H_ROLL_NUM_Slider = QSlider(self.scrollAreaWidgetContents_2)
        self.H_ROLL_NUM_Slider.setObjectName(u"H_ROLL_NUM_Slider")
        self.H_ROLL_NUM_Slider.setEnabled(True)
        self.H_ROLL_NUM_Slider.setMinimum(1)
        self.H_ROLL_NUM_Slider.setMaximum(16)
        self.H_ROLL_NUM_Slider.setPageStep(1)
        self.H_ROLL_NUM_Slider.setOrientation(Qt.Horizontal)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Slider)

        self.H_ROLL_NUM_Value = QLabel(self.scrollAreaWidgetContents_2)
        self.H_ROLL_NUM_Value.setObjectName(u"H_ROLL_NUM_Value")
        self.H_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.H_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.H_ROLL_NUM_Value.setFont(font1)
        self.H_ROLL_NUM_Value.setMidLineWidth(0)
        self.H_ROLL_NUM_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_ROLL_NUM_Value.setMargin(0)

        self.H_ROLL_CMP.addWidget(self.H_ROLL_NUM_Value)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.H_ROLL_CMP)

        self.H_VLD_SEG_CMP = QHBoxLayout()
        self.H_VLD_SEG_CMP.setSpacing(0)
        self.H_VLD_SEG_CMP.setObjectName(u"H_VLD_SEG_CMP")
        self.H_VLD_SEG_CMP.setContentsMargins(0, -1, -1, -1)
        self.H_VLD_SEG_Slider = QSlider(self.scrollAreaWidgetContents_2)
        self.H_VLD_SEG_Slider.setObjectName(u"H_VLD_SEG_Slider")
        self.H_VLD_SEG_Slider.setMinimum(1)
        self.H_VLD_SEG_Slider.setMaximum(16)
        self.H_VLD_SEG_Slider.setPageStep(1)
        self.H_VLD_SEG_Slider.setOrientation(Qt.Horizontal)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Slider)

        self.H_VLD_SEG_Value = QLabel(self.scrollAreaWidgetContents_2)
        self.H_VLD_SEG_Value.setObjectName(u"H_VLD_SEG_Value")
        self.H_VLD_SEG_Value.setMinimumSize(QSize(20, 25))
        self.H_VLD_SEG_Value.setMaximumSize(QSize(20, 16777215))
        self.H_VLD_SEG_Value.setFont(font1)
        self.H_VLD_SEG_Value.setTextFormat(Qt.MarkdownText)
        self.H_VLD_SEG_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_VLD_SEG_Value.setMargin(0)

        self.H_VLD_SEG_CMP.addWidget(self.H_VLD_SEG_Value)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.H_VLD_SEG_CMP)

        self.H_SEG_Shift_CMP = QHBoxLayout()
        self.H_SEG_Shift_CMP.setSpacing(0)
        self.H_SEG_Shift_CMP.setObjectName(u"H_SEG_Shift_CMP")
        self.H_SEG_Shift_CMP.setContentsMargins(0, -1, 0, -1)
        self.H_SEG_Shift_Slider = QSlider(self.scrollAreaWidgetContents_2)
        self.H_SEG_Shift_Slider.setObjectName(u"H_SEG_Shift_Slider")
        self.H_SEG_Shift_Slider.setEnabled(True)
        self.H_SEG_Shift_Slider.setMinimum(0)
        self.H_SEG_Shift_Slider.setMaximum(15)
        self.H_SEG_Shift_Slider.setSingleStep(1)
        self.H_SEG_Shift_Slider.setPageStep(1)
        self.H_SEG_Shift_Slider.setValue(0)
        self.H_SEG_Shift_Slider.setSliderPosition(0)
        self.H_SEG_Shift_Slider.setOrientation(Qt.Horizontal)

        self.H_SEG_Shift_CMP.addWidget(self.H_SEG_Shift_Slider)

        self.H_SEG_Shift_Value = QLabel(self.scrollAreaWidgetContents_2)
        self.H_SEG_Shift_Value.setObjectName(u"H_SEG_Shift_Value")
        self.H_SEG_Shift_Value.setMinimumSize(QSize(20, 25))
        self.H_SEG_Shift_Value.setMaximumSize(QSize(20, 16777215))
        self.H_SEG_Shift_Value.setFont(font1)
        self.H_SEG_Shift_Value.setTextFormat(Qt.MarkdownText)
        self.H_SEG_Shift_Value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_SEG_Shift_Value.setMargin(0)

        self.H_SEG_Shift_CMP.addWidget(self.H_SEG_Shift_Value)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.H_SEG_Shift_CMP)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.OperatePage.addWidget(self.Config)

        self.Input = QGroupBox(self.OperateFrame)
        self.Input.setObjectName(u"Input")
        self.Input.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setMaximumSize(QSize(500, 16777215))
        self.Input.setStyleSheet(u"QPushButton {	\n"
"	width:90px;\n"
"}")
        self.Input.setTitle(u"Input")
        self.verticalLayout_2 = QVBoxLayout(self.Input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Sel_Config_file_LineEdit = QLineEdit(self.Input)
        self.Sel_Config_file_LineEdit.setObjectName(u"Sel_Config_file_LineEdit")
        self.Sel_Config_file_LineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Sel_Config_file_LineEdit.sizePolicy().hasHeightForWidth())
        self.Sel_Config_file_LineEdit.setSizePolicy(sizePolicy1)
        self.Sel_Config_file_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Sel_Config_file_LineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.Sel_Config_file_LineEdit)

        self.Sel_Config_file_Button = QPushButton(self.Input)
        self.Sel_Config_file_Button.setObjectName(u"Sel_Config_file_Button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Sel_Config_file_Button.sizePolicy().hasHeightForWidth())
        self.Sel_Config_file_Button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.Sel_Config_file_Button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Load_ROI_file_LineEdit = QLineEdit(self.Input)
        self.Load_ROI_file_LineEdit.setObjectName(u"Load_ROI_file_LineEdit")
        self.Load_ROI_file_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Load_ROI_file_LineEdit.sizePolicy().hasHeightForWidth())
        self.Load_ROI_file_LineEdit.setSizePolicy(sizePolicy1)
        self.Load_ROI_file_LineEdit.setMinimumSize(QSize(0, 0))
        self.Load_ROI_file_LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Load_ROI_file_LineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.Load_ROI_file_LineEdit)

        self.Load_ROI_file_Button = QPushButton(self.Input)
        self.Load_ROI_file_Button.setObjectName(u"Load_ROI_file_Button")
        sizePolicy2.setHeightForWidth(self.Load_ROI_file_Button.sizePolicy().hasHeightForWidth())
        self.Load_ROI_file_Button.setSizePolicy(sizePolicy2)
        self.Load_ROI_file_Button.setFocusPolicy(Qt.WheelFocus)

        self.horizontalLayout_3.addWidget(self.Load_ROI_file_Button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.OperatePage.addWidget(self.Input)

        self.Output = QGroupBox(self.OperateFrame)
        self.Output.setObjectName(u"Output")
        self.Output.setMaximumSize(QSize(500, 16777215))
        self.Output.setTitle(u"Output")
        self.FileSaveRename_Layout_2 = QFormLayout(self.Output)
        self.FileSaveRename_Layout_2.setObjectName(u"FileSaveRename_Layout_2")
        self.REG_CFG_File_Label = QLabel(self.Output)
        self.REG_CFG_File_Label.setObjectName(u"REG_CFG_File_Label")
        self.REG_CFG_File_Label.setFont(font)

        self.FileSaveRename_Layout_2.setWidget(0, QFormLayout.LabelRole, self.REG_CFG_File_Label)

        self.REG_CFG_File_LineEdit = QLineEdit(self.Output)
        self.REG_CFG_File_LineEdit.setObjectName(u"REG_CFG_File_LineEdit")
        self.REG_CFG_File_LineEdit.setFont(font)

        self.FileSaveRename_Layout_2.setWidget(0, QFormLayout.FieldRole, self.REG_CFG_File_LineEdit)

        self.ROI_SRAM_File_Label = QLabel(self.Output)
        self.ROI_SRAM_File_Label.setObjectName(u"ROI_SRAM_File_Label")
        self.ROI_SRAM_File_Label.setFont(font)

        self.FileSaveRename_Layout_2.setWidget(1, QFormLayout.LabelRole, self.ROI_SRAM_File_Label)

        self.ROI_SRAM_File_LineEdit = QLineEdit(self.Output)
        self.ROI_SRAM_File_LineEdit.setObjectName(u"ROI_SRAM_File_LineEdit")
        self.ROI_SRAM_File_LineEdit.setFont(font)

        self.FileSaveRename_Layout_2.setWidget(1, QFormLayout.FieldRole, self.ROI_SRAM_File_LineEdit)


        self.OperatePage.addWidget(self.Output)

        self.Operate = QGroupBox(self.OperateFrame)
        self.Operate.setObjectName(u"Operate")
        self.Operate.setMinimumSize(QSize(100, 0))
        self.Operate.setMaximumSize(QSize(500, 16777215))
        self.gridLayout = QGridLayout(self.Operate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(6)
        self.Save = QPushButton(self.Operate)
        self.Save.setObjectName(u"Save")
        sizePolicy1.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy1)
        self.Save.setFont(font)

        self.gridLayout.addWidget(self.Save, 0, 1, 1, 1)

        self.Preview = QPushButton(self.Operate)
        self.Preview.setObjectName(u"Preview")
        self.Preview.setMinimumSize(QSize(0, 0))
        self.Preview.setFont(font)

        self.gridLayout.addWidget(self.Preview, 0, 0, 1, 1)

        self.ClearLog = QPushButton(self.Operate)
        self.ClearLog.setObjectName(u"ClearLog")
        self.ClearLog.setFont(font)

        self.gridLayout.addWidget(self.ClearLog, 0, 2, 1, 1)

        self.Reload = QPushButton(self.Operate)
        self.Reload.setObjectName(u"Reload")
        self.Reload.setFont(font)

        self.gridLayout.addWidget(self.Reload, 1, 1, 1, 1)

        self.Preview0 = QPushButton(self.Operate)
        self.Preview0.setObjectName(u"Preview0")
        self.Preview0.setFont(font)

        self.gridLayout.addWidget(self.Preview0, 1, 0, 1, 1)


        self.OperatePage.addWidget(self.Operate)

        self.Log = QGroupBox(self.OperateFrame)
        self.Log.setObjectName(u"Log")
        self.Log.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_15 = QHBoxLayout(self.Log)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 9, 0, 1)
        self.LogPrintWindow = QPlainTextEdit(self.Log)
        self.LogPrintWindow.setObjectName(u"LogPrintWindow")
        self.LogPrintWindow.setEnabled(True)
        self.LogPrintWindow.setFont(font)
        self.LogPrintWindow.setFocusPolicy(Qt.StrongFocus)
        self.LogPrintWindow.setFrameShape(QFrame.NoFrame)
        self.LogPrintWindow.setFrameShadow(QFrame.Plain)
        self.LogPrintWindow.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.LogPrintWindow)


        self.OperatePage.addWidget(self.Log)

        self.OperatePage.setStretch(0, 7)
        self.OperatePage.setStretch(1, 2)
        self.OperatePage.setStretch(2, 2)
        self.OperatePage.setStretch(3, 2)
        self.OperatePage.setStretch(4, 5)

        self.MainPage.addWidget(self.OperateFrame)

        self.MainPage.setStretch(0, 7)
        self.MainPage.setStretch(1, 3)

        self.horizontalLayout.addLayout(self.MainPage)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.page_3_layout = QVBoxLayout(self.page_2)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 9, 9)
        self.MST_MODE_Label = QLabel(self.groupBox)
        self.MST_MODE_Label.setObjectName(u"MST_MODE_Label")
        self.MST_MODE_Label.setMinimumSize(QSize(85, 0))
        self.MST_MODE_Label.setMaximumSize(QSize(85, 16777215))
        self.MST_MODE_Label.setFrameShape(QFrame.StyledPanel)
        self.MST_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.MST_MODE_Label)

        self.MST_MODE_ComboBox = QComboBox(self.groupBox)
        self.MST_MODE_ComboBox.setObjectName(u"MST_MODE_ComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.MST_MODE_ComboBox)

        self.TRG_I_EN_Label = QLabel(self.groupBox)
        self.TRG_I_EN_Label.setObjectName(u"TRG_I_EN_Label")
        self.TRG_I_EN_Label.setMinimumSize(QSize(85, 0))
        self.TRG_I_EN_Label.setMaximumSize(QSize(85, 16777215))
        self.TRG_I_EN_Label.setFont(font)
        self.TRG_I_EN_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.TRG_I_EN_Label)

        self.TRG_I_EN_ComboBox = QComboBox(self.groupBox)
        self.TRG_I_EN_ComboBox.setObjectName(u"TRG_I_EN_ComboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.TRG_I_EN_ComboBox)

        self.TDC_Bin_Width_Label = QLabel(self.groupBox)
        self.TDC_Bin_Width_Label.setObjectName(u"TDC_Bin_Width_Label")
        self.TDC_Bin_Width_Label.setMinimumSize(QSize(0, 0))
        self.TDC_Bin_Width_Label.setMaximumSize(QSize(16777215, 16777215))
        self.TDC_Bin_Width_Label.setFont(font)
        self.TDC_Bin_Width_Label.setFrameShape(QFrame.StyledPanel)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.TDC_Bin_Width_Label)

        self.TDC_Bin_Width_ComboBox = QComboBox(self.groupBox)
        self.TDC_Bin_Width_ComboBox.setObjectName(u"TDC_Bin_Width_ComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.TDC_Bin_Width_ComboBox)

        self.WORK_MODE_Label_2 = QLabel(self.groupBox)
        self.WORK_MODE_Label_2.setObjectName(u"WORK_MODE_Label_2")
        sizePolicy.setHeightForWidth(self.WORK_MODE_Label_2.sizePolicy().hasHeightForWidth())
        self.WORK_MODE_Label_2.setSizePolicy(sizePolicy)
        self.WORK_MODE_Label_2.setMinimumSize(QSize(0, 0))
        self.WORK_MODE_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.WORK_MODE_Label_2.setFrameShape(QFrame.StyledPanel)
        self.WORK_MODE_Label_2.setFrameShadow(QFrame.Raised)
        self.WORK_MODE_Label_2.setMargin(0)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.WORK_MODE_Label_2)

        self.WORK_MODE_ComboBox_2 = QComboBox(self.groupBox)
        self.WORK_MODE_ComboBox_2.setObjectName(u"WORK_MODE_ComboBox_2")
        self.WORK_MODE_ComboBox_2.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.WORK_MODE_ComboBox_2)

        self.MIPI_RATE_Label_2 = QLabel(self.groupBox)
        self.MIPI_RATE_Label_2.setObjectName(u"MIPI_RATE_Label_2")
        sizePolicy.setHeightForWidth(self.MIPI_RATE_Label_2.sizePolicy().hasHeightForWidth())
        self.MIPI_RATE_Label_2.setSizePolicy(sizePolicy)
        self.MIPI_RATE_Label_2.setMinimumSize(QSize(0, 0))
        self.MIPI_RATE_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.MIPI_RATE_Label_2.setFont(font1)
        self.MIPI_RATE_Label_2.setFrameShape(QFrame.StyledPanel)
        self.MIPI_RATE_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.MIPI_RATE_Label_2)

        self.MIPI_RATE_ComboBox_2 = QComboBox(self.groupBox)
        self.MIPI_RATE_ComboBox_2.setObjectName(u"MIPI_RATE_ComboBox_2")
        self.MIPI_RATE_ComboBox_2.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.MIPI_RATE_ComboBox_2)

        self.SCAN_MODE_Label_2 = QLabel(self.groupBox)
        self.SCAN_MODE_Label_2.setObjectName(u"SCAN_MODE_Label_2")
        self.SCAN_MODE_Label_2.setMinimumSize(QSize(0, 0))
        self.SCAN_MODE_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.SCAN_MODE_Label_2.setFont(font1)
        self.SCAN_MODE_Label_2.setFrameShape(QFrame.StyledPanel)
        self.SCAN_MODE_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.SCAN_MODE_Label_2)

        self.SCAN_MODE_ComboBox_2 = QComboBox(self.groupBox)
        self.SCAN_MODE_ComboBox_2.setObjectName(u"SCAN_MODE_ComboBox_2")
        self.SCAN_MODE_ComboBox_2.setFont(font1)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.SCAN_MODE_ComboBox_2)

        self.V_ROLL_NUM_Label_2 = QLabel(self.groupBox)
        self.V_ROLL_NUM_Label_2.setObjectName(u"V_ROLL_NUM_Label_2")
        self.V_ROLL_NUM_Label_2.setMinimumSize(QSize(0, 0))
        self.V_ROLL_NUM_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.V_ROLL_NUM_Label_2.setFont(font1)
        self.V_ROLL_NUM_Label_2.setFrameShape(QFrame.StyledPanel)
        self.V_ROLL_NUM_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.V_ROLL_NUM_Label_2)

        self.V_ROLL_NUM_CMP_2 = QHBoxLayout()
        self.V_ROLL_NUM_CMP_2.setSpacing(0)
        self.V_ROLL_NUM_CMP_2.setObjectName(u"V_ROLL_NUM_CMP_2")
        self.V_ROLL_NUM_CMP_2.setContentsMargins(0, -1, 0, -1)
        self.V_ROLL_NUM_Slider_2 = QSlider(self.groupBox)
        self.V_ROLL_NUM_Slider_2.setObjectName(u"V_ROLL_NUM_Slider_2")
        self.V_ROLL_NUM_Slider_2.setMouseTracking(False)
        self.V_ROLL_NUM_Slider_2.setMinimum(1)
        self.V_ROLL_NUM_Slider_2.setMaximum(32)
        self.V_ROLL_NUM_Slider_2.setPageStep(1)
        self.V_ROLL_NUM_Slider_2.setOrientation(Qt.Horizontal)

        self.V_ROLL_NUM_CMP_2.addWidget(self.V_ROLL_NUM_Slider_2)

        self.V_ROLL_NUM_Value_2 = QLabel(self.groupBox)
        self.V_ROLL_NUM_Value_2.setObjectName(u"V_ROLL_NUM_Value_2")
        self.V_ROLL_NUM_Value_2.setMinimumSize(QSize(20, 25))
        self.V_ROLL_NUM_Value_2.setMaximumSize(QSize(20, 16777215))
        self.V_ROLL_NUM_Value_2.setFont(font1)
        self.V_ROLL_NUM_Value_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.V_ROLL_NUM_Value_2.setWordWrap(True)
        self.V_ROLL_NUM_Value_2.setMargin(0)

        self.V_ROLL_NUM_CMP_2.addWidget(self.V_ROLL_NUM_Value_2)


        self.formLayout_2.setLayout(6, QFormLayout.FieldRole, self.V_ROLL_NUM_CMP_2)

        self.H_ROLL_NUM_Label_2 = QLabel(self.groupBox)
        self.H_ROLL_NUM_Label_2.setObjectName(u"H_ROLL_NUM_Label_2")
        self.H_ROLL_NUM_Label_2.setMinimumSize(QSize(0, 0))
        self.H_ROLL_NUM_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.H_ROLL_NUM_Label_2.setFont(font1)
        self.H_ROLL_NUM_Label_2.setFrameShape(QFrame.StyledPanel)
        self.H_ROLL_NUM_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.H_ROLL_NUM_Label_2)

        self.H_ROLL_CMP_2 = QHBoxLayout()
        self.H_ROLL_CMP_2.setSpacing(0)
        self.H_ROLL_CMP_2.setObjectName(u"H_ROLL_CMP_2")
        self.H_ROLL_CMP_2.setContentsMargins(0, -1, -1, -1)
        self.H_ROLL_NUM_Slider_2 = QSlider(self.groupBox)
        self.H_ROLL_NUM_Slider_2.setObjectName(u"H_ROLL_NUM_Slider_2")
        self.H_ROLL_NUM_Slider_2.setEnabled(True)
        self.H_ROLL_NUM_Slider_2.setMinimum(1)
        self.H_ROLL_NUM_Slider_2.setMaximum(16)
        self.H_ROLL_NUM_Slider_2.setPageStep(1)
        self.H_ROLL_NUM_Slider_2.setOrientation(Qt.Horizontal)

        self.H_ROLL_CMP_2.addWidget(self.H_ROLL_NUM_Slider_2)

        self.H_ROLL_NUM_Value_2 = QLabel(self.groupBox)
        self.H_ROLL_NUM_Value_2.setObjectName(u"H_ROLL_NUM_Value_2")
        self.H_ROLL_NUM_Value_2.setMinimumSize(QSize(20, 25))
        self.H_ROLL_NUM_Value_2.setMaximumSize(QSize(20, 16777215))
        self.H_ROLL_NUM_Value_2.setFont(font1)
        self.H_ROLL_NUM_Value_2.setMidLineWidth(0)
        self.H_ROLL_NUM_Value_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_ROLL_NUM_Value_2.setMargin(0)

        self.H_ROLL_CMP_2.addWidget(self.H_ROLL_NUM_Value_2)


        self.formLayout_2.setLayout(7, QFormLayout.FieldRole, self.H_ROLL_CMP_2)

        self.H_VLD_SEG_Label_2 = QLabel(self.groupBox)
        self.H_VLD_SEG_Label_2.setObjectName(u"H_VLD_SEG_Label_2")
        self.H_VLD_SEG_Label_2.setMinimumSize(QSize(0, 0))
        self.H_VLD_SEG_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.H_VLD_SEG_Label_2.setFont(font1)
        self.H_VLD_SEG_Label_2.setFrameShape(QFrame.StyledPanel)
        self.H_VLD_SEG_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.H_VLD_SEG_Label_2)

        self.H_VLD_SEG_CMP_2 = QHBoxLayout()
        self.H_VLD_SEG_CMP_2.setSpacing(0)
        self.H_VLD_SEG_CMP_2.setObjectName(u"H_VLD_SEG_CMP_2")
        self.H_VLD_SEG_CMP_2.setContentsMargins(0, -1, -1, -1)
        self.H_VLD_SEG_Slider_2 = QSlider(self.groupBox)
        self.H_VLD_SEG_Slider_2.setObjectName(u"H_VLD_SEG_Slider_2")
        self.H_VLD_SEG_Slider_2.setMinimum(1)
        self.H_VLD_SEG_Slider_2.setMaximum(16)
        self.H_VLD_SEG_Slider_2.setPageStep(1)
        self.H_VLD_SEG_Slider_2.setOrientation(Qt.Horizontal)

        self.H_VLD_SEG_CMP_2.addWidget(self.H_VLD_SEG_Slider_2)

        self.H_VLD_SEG_Value_2 = QLabel(self.groupBox)
        self.H_VLD_SEG_Value_2.setObjectName(u"H_VLD_SEG_Value_2")
        self.H_VLD_SEG_Value_2.setMinimumSize(QSize(20, 25))
        self.H_VLD_SEG_Value_2.setMaximumSize(QSize(20, 16777215))
        self.H_VLD_SEG_Value_2.setFont(font1)
        self.H_VLD_SEG_Value_2.setTextFormat(Qt.MarkdownText)
        self.H_VLD_SEG_Value_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_VLD_SEG_Value_2.setMargin(0)

        self.H_VLD_SEG_CMP_2.addWidget(self.H_VLD_SEG_Value_2)


        self.formLayout_2.setLayout(8, QFormLayout.FieldRole, self.H_VLD_SEG_CMP_2)

        self.H_SEG_Shift_Label_2 = QLabel(self.groupBox)
        self.H_SEG_Shift_Label_2.setObjectName(u"H_SEG_Shift_Label_2")
        self.H_SEG_Shift_Label_2.setMinimumSize(QSize(0, 0))
        self.H_SEG_Shift_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.H_SEG_Shift_Label_2.setFont(font1)
        self.H_SEG_Shift_Label_2.setFrameShape(QFrame.StyledPanel)
        self.H_SEG_Shift_Label_2.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.H_SEG_Shift_Label_2)

        self.H_SEG_Shift_CMP_2 = QHBoxLayout()
        self.H_SEG_Shift_CMP_2.setSpacing(0)
        self.H_SEG_Shift_CMP_2.setObjectName(u"H_SEG_Shift_CMP_2")
        self.H_SEG_Shift_CMP_2.setContentsMargins(0, -1, 0, -1)
        self.H_SEG_Shift_Slider_2 = QSlider(self.groupBox)
        self.H_SEG_Shift_Slider_2.setObjectName(u"H_SEG_Shift_Slider_2")
        self.H_SEG_Shift_Slider_2.setEnabled(True)
        self.H_SEG_Shift_Slider_2.setMinimum(0)
        self.H_SEG_Shift_Slider_2.setMaximum(15)
        self.H_SEG_Shift_Slider_2.setSingleStep(1)
        self.H_SEG_Shift_Slider_2.setPageStep(1)
        self.H_SEG_Shift_Slider_2.setValue(0)
        self.H_SEG_Shift_Slider_2.setSliderPosition(0)
        self.H_SEG_Shift_Slider_2.setOrientation(Qt.Horizontal)

        self.H_SEG_Shift_CMP_2.addWidget(self.H_SEG_Shift_Slider_2)

        self.H_SEG_Shift_Value_2 = QLabel(self.groupBox)
        self.H_SEG_Shift_Value_2.setObjectName(u"H_SEG_Shift_Value_2")
        self.H_SEG_Shift_Value_2.setMinimumSize(QSize(20, 25))
        self.H_SEG_Shift_Value_2.setMaximumSize(QSize(20, 16777215))
        self.H_SEG_Shift_Value_2.setFont(font1)
        self.H_SEG_Shift_Value_2.setTextFormat(Qt.MarkdownText)
        self.H_SEG_Shift_Value_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.H_SEG_Shift_Value_2.setMargin(0)

        self.H_SEG_Shift_CMP_2.addWidget(self.H_SEG_Shift_Value_2)


        self.formLayout_2.setLayout(9, QFormLayout.FieldRole, self.H_SEG_Shift_CMP_2)


        self.horizontalLayout_4.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")

        self.horizontalLayout_4.addLayout(self.formLayout_3)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")

        self.horizontalLayout_4.addLayout(self.formLayout_5)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.Sel_Config_file_Label_2 = QLabel(self.groupBox)
        self.Sel_Config_file_Label_2.setObjectName(u"Sel_Config_file_Label_2")
        self.Sel_Config_file_Label_2.setMinimumSize(QSize(0, 0))
        self.Sel_Config_file_Label_2.setMaximumSize(QSize(16777215, 16777215))
        self.Sel_Config_file_Label_2.setFont(font1)
        self.Sel_Config_file_Label_2.setFrameShape(QFrame.NoFrame)
        self.Sel_Config_file_Label_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.Sel_Config_file_Label_2, 4, 0, 1, 1)

        self.ROI_SRAM_File_Label_2 = QLabel(self.groupBox)
        self.ROI_SRAM_File_Label_2.setObjectName(u"ROI_SRAM_File_Label_2")
        self.ROI_SRAM_File_Label_2.setFont(font)

        self.gridLayout_2.addWidget(self.ROI_SRAM_File_Label_2, 3, 0, 1, 1)

        self.SPadisApp_Path_Sel_Button = QPushButton(self.groupBox)
        self.SPadisApp_Path_Sel_Button.setObjectName(u"SPadisApp_Path_Sel_Button")
        sizePolicy2.setHeightForWidth(self.SPadisApp_Path_Sel_Button.sizePolicy().hasHeightForWidth())
        self.SPadisApp_Path_Sel_Button.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.SPadisApp_Path_Sel_Button, 5, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)

        self.ROI_SRAM_File_LineEdit_2 = QLineEdit(self.groupBox)
        self.ROI_SRAM_File_LineEdit_2.setObjectName(u"ROI_SRAM_File_LineEdit_2")
        self.ROI_SRAM_File_LineEdit_2.setFont(font)

        self.gridLayout_2.addWidget(self.ROI_SRAM_File_LineEdit_2, 3, 1, 1, 1)

        self.REG_CFG_File_Label_2 = QLabel(self.groupBox)
        self.REG_CFG_File_Label_2.setObjectName(u"REG_CFG_File_Label_2")
        self.REG_CFG_File_Label_2.setFont(font)

        self.gridLayout_2.addWidget(self.REG_CFG_File_Label_2, 1, 0, 1, 1)

        self.REG_CFG_File_LineEdit_2 = QLineEdit(self.groupBox)
        self.REG_CFG_File_LineEdit_2.setObjectName(u"REG_CFG_File_LineEdit_2")
        self.REG_CFG_File_LineEdit_2.setFont(font)

        self.gridLayout_2.addWidget(self.REG_CFG_File_LineEdit_2, 1, 1, 1, 1)

        self.SPadisApp_Path_Sel_Label = QLabel(self.groupBox)
        self.SPadisApp_Path_Sel_Label.setObjectName(u"SPadisApp_Path_Sel_Label")
        self.SPadisApp_Path_Sel_Label.setMinimumSize(QSize(0, 0))
        self.SPadisApp_Path_Sel_Label.setMaximumSize(QSize(16777215, 16777215))
        self.SPadisApp_Path_Sel_Label.setFont(font1)
        self.SPadisApp_Path_Sel_Label.setFrameShape(QFrame.NoFrame)
        self.SPadisApp_Path_Sel_Label.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.SPadisApp_Path_Sel_Label, 5, 0, 1, 1)

        self.SPadisApp_Path_Sel__LineEdit = QLineEdit(self.groupBox)
        self.SPadisApp_Path_Sel__LineEdit.setObjectName(u"SPadisApp_Path_Sel__LineEdit")
        self.SPadisApp_Path_Sel__LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.SPadisApp_Path_Sel__LineEdit.sizePolicy().hasHeightForWidth())
        self.SPadisApp_Path_Sel__LineEdit.setSizePolicy(sizePolicy1)
        self.SPadisApp_Path_Sel__LineEdit.setFocusPolicy(Qt.StrongFocus)
        self.SPadisApp_Path_Sel__LineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.SPadisApp_Path_Sel__LineEdit, 5, 1, 1, 1)

        self.Sel_Config_file_LineEdit_2 = QLineEdit(self.groupBox)
        self.Sel_Config_file_LineEdit_2.setObjectName(u"Sel_Config_file_LineEdit_2")
        self.Sel_Config_file_LineEdit_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Sel_Config_file_LineEdit_2.sizePolicy().hasHeightForWidth())
        self.Sel_Config_file_LineEdit_2.setSizePolicy(sizePolicy1)
        self.Sel_Config_file_LineEdit_2.setFocusPolicy(Qt.StrongFocus)
        self.Sel_Config_file_LineEdit_2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Sel_Config_file_LineEdit_2, 4, 1, 1, 1)

        self.Sel_Config_file_Button_2 = QPushButton(self.groupBox)
        self.Sel_Config_file_Button_2.setObjectName(u"Sel_Config_file_Button_2")
        sizePolicy2.setHeightForWidth(self.Sel_Config_file_Button_2.sizePolicy().hasHeightForWidth())
        self.Sel_Config_file_Button_2.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.Sel_Config_file_Button_2, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.verticalLayout_5.setStretch(0, 3)

        self.page_3_layout.addWidget(self.groupBox)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.page_3_layout.addLayout(self.verticalLayout_6)

        self.MoreConfig = QVBoxLayout()
        self.MoreConfig.setObjectName(u"MoreConfig")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.MoreConfig.addWidget(self.frame)


        self.page_3_layout.addLayout(self.MoreConfig)

        self.page_3_layout.setStretch(2, 2)
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_2_layout = QVBoxLayout(self.page_3)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_3)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 865, 658))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(16)
        self.title_label.setFont(font2)
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

        self.main_pages_layout.addWidget(self.pages)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainPages)
        self.V_ROLL_NUM_Slider.valueChanged.connect(self.V_ROLL_NUM_Value.setNum)
        self.H_ROLL_NUM_Slider.valueChanged.connect(self.H_ROLL_NUM_Value.setNum)
        self.H_SEG_Shift_Slider.valueChanged.connect(self.H_SEG_Shift_Value.setNum)
        self.H_VLD_SEG_Slider.valueChanged.connect(self.H_VLD_SEG_Value.setNum)
        self.H_SEG_Shift_Slider_2.valueChanged.connect(self.H_SEG_Shift_Value_2.setNum)
        self.H_ROLL_NUM_Slider_2.valueChanged.connect(self.H_ROLL_NUM_Slider.setValue)
        self.H_VLD_SEG_Slider_2.valueChanged.connect(self.H_VLD_SEG_Slider.setValue)
        self.WORK_MODE_ComboBox.activated.connect(self.WORK_MODE_ComboBox_2.setCurrentIndex)
        self.H_SEG_Shift_Slider_2.valueChanged.connect(self.H_SEG_Shift_Slider.setValue)
        self.V_ROLL_NUM_Slider_2.valueChanged.connect(self.V_ROLL_NUM_Slider.setValue)
        self.SCAN_MODE_ComboBox_2.activated.connect(self.SCAN_MODE_ComboBox.setCurrentIndex)
        self.H_VLD_SEG_Slider_2.valueChanged.connect(self.H_VLD_SEG_Value_2.setNum)
        self.SCAN_MODE_ComboBox.activated.connect(self.SCAN_MODE_ComboBox_2.setCurrentIndex)
        self.V_ROLL_NUM_Slider_2.valueChanged.connect(self.V_ROLL_NUM_Value_2.setNum)
        self.V_ROLL_NUM_Slider.valueChanged.connect(self.V_ROLL_NUM_Slider_2.setValue)
        self.H_ROLL_NUM_Slider.valueChanged.connect(self.H_ROLL_NUM_Slider_2.setValue)
        self.WORK_MODE_ComboBox_2.activated.connect(self.WORK_MODE_ComboBox.setCurrentIndex)
        self.MIPI_RATE_ComboBox.activated.connect(self.MIPI_RATE_ComboBox_2.setCurrentIndex)
        self.MIPI_RATE_ComboBox_2.activated.connect(self.MIPI_RATE_ComboBox.setCurrentIndex)
        self.H_SEG_Shift_Slider.valueChanged.connect(self.H_SEG_Shift_Slider_2.setValue)
        self.H_VLD_SEG_Slider.valueChanged.connect(self.H_VLD_SEG_Slider_2.setValue)
        self.H_ROLL_NUM_Slider_2.valueChanged.connect(self.H_ROLL_NUM_Value_2.setNum)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.Config.setTitle(QCoreApplication.translate("MainPages", u"Config", None))
        self.WORK_MODE_Label.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.MIPI_RATE_Label.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
        self.SCAN_MODE_Label.setText(QCoreApplication.translate("MainPages", u"SCAN_MODE", None))
        self.V_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_ROLL_NUM", None))
        self.H_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"H_ROLL_NUM", None))
        self.H_VLD_SEG_Label.setText(QCoreApplication.translate("MainPages", u"H_VLD_SEG", None))
        self.H_SEG_Shift_Label.setText(QCoreApplication.translate("MainPages", u"H_SEG_Shift", None))
        self.V_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"32", None))
        self.H_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.H_VLD_SEG_Value.setText(QCoreApplication.translate("MainPages", u"16", None))
        self.H_SEG_Shift_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Sel_Config_file_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.Sel_Config_file_Button.setText(QCoreApplication.translate("MainPages", u"Sel Config file", None))
        self.Load_ROI_file_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u6807\u5b9a\u6587\u4ef6", None))
        self.Load_ROI_file_Button.setText(QCoreApplication.translate("MainPages", u"Load ROI file", None))
        self.REG_CFG_File_Label.setText(QCoreApplication.translate("MainPages", u"REG CFG File", None))
        self.REG_CFG_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.ROI_SRAM_File_Label.setText(QCoreApplication.translate("MainPages", u"ROI SRAM File", None))
        self.ROI_SRAM_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.Operate.setTitle(QCoreApplication.translate("MainPages", u"Operete", None))
        self.Save.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Preview.setText(QCoreApplication.translate("MainPages", u"Preview", None))
        self.ClearLog.setText(QCoreApplication.translate("MainPages", u"Clear Log", None))
        self.Reload.setText(QCoreApplication.translate("MainPages", u"Reload", None))
        self.Preview0.setText(QCoreApplication.translate("MainPages", u"Preveiw0", None))
        self.Log.setTitle(QCoreApplication.translate("MainPages", u"Log", None))
        self.LogPrintWindow.setPlainText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainPages", u"Config", None))
        self.MST_MODE_Label.setText(QCoreApplication.translate("MainPages", u"MST_MODE", None))
        self.TRG_I_EN_Label.setText(QCoreApplication.translate("MainPages", u"TRG_I_EN", None))
        self.TDC_Bin_Width_Label.setText(QCoreApplication.translate("MainPages", u"TDC bin width", None))
        self.WORK_MODE_Label_2.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.MIPI_RATE_Label_2.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
        self.SCAN_MODE_Label_2.setText(QCoreApplication.translate("MainPages", u"SCAN_MODE", None))
        self.V_ROLL_NUM_Label_2.setText(QCoreApplication.translate("MainPages", u"V_ROLL_NUM", None))
        self.V_ROLL_NUM_Value_2.setText(QCoreApplication.translate("MainPages", u"32", None))
        self.H_ROLL_NUM_Label_2.setText(QCoreApplication.translate("MainPages", u"H_ROLL_NUM", None))
        self.H_ROLL_NUM_Value_2.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.H_VLD_SEG_Label_2.setText(QCoreApplication.translate("MainPages", u"H_VLD_SEG", None))
        self.H_VLD_SEG_Value_2.setText(QCoreApplication.translate("MainPages", u"16", None))
        self.H_SEG_Shift_Label_2.setText(QCoreApplication.translate("MainPages", u"H_SEG_Shift", None))
        self.H_SEG_Shift_Value_2.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Sel_Config_file_Label_2.setText(QCoreApplication.translate("MainPages", u"Base Script", None))
        self.ROI_SRAM_File_Label_2.setText(QCoreApplication.translate("MainPages", u"ROI SRAM File", None))
        self.SPadisApp_Path_Sel_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.ROI_SRAM_File_LineEdit_2.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.REG_CFG_File_Label_2.setText(QCoreApplication.translate("MainPages", u"REG CFG File", None))
        self.REG_CFG_File_LineEdit_2.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.SPadisApp_Path_Sel_Label.setText(QCoreApplication.translate("MainPages", u"SpadisApp", None))
        self.SPadisApp_Path_Sel__LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u6307\u5b9aSpadisApp\u8f6f\u4ef6\u8def\u5f84", None))
        self.Sel_Config_file_LineEdit_2.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.Sel_Config_file_Button_2.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pageswExmSq.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
        MainPages.resize(1031, 774)
        MainPages.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(MainPages)
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
        self.Hawk01_ScriptConfig = QGroupBox(self.Hawk01)
        self.Hawk01_ScriptConfig.setObjectName(u"Hawk01_ScriptConfig")
        self.horizontalLayout_2 = QHBoxLayout(self.Hawk01_ScriptConfig)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.Hawk01_RegisterConfig = QWidget(self.Hawk01_ScriptConfig)
        self.Hawk01_RegisterConfig.setObjectName(u"Hawk01_RegisterConfig")
        self.Hawk01_RegisterConfig.setMinimumSize(QSize(0, 0))
        self.Hawk01_RegisterConfig.setMaximumSize(QSize(600, 16777215))
        self.formLayout_2 = QFormLayout(self.Hawk01_RegisterConfig)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(8)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Hawk01_XCLK_Label = QLabel(self.Hawk01_RegisterConfig)
        self.Hawk01_XCLK_Label.setObjectName(u"Hawk01_XCLK_Label")
        self.Hawk01_XCLK_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_XCLK_Label.setFont(font)
        self.Hawk01_XCLK_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Hawk01_XCLK_Label)

        self.Hawk01_XCLK_ComboBox = QComboBox(self.Hawk01_RegisterConfig)
        self.Hawk01_XCLK_ComboBox.addItem("")
        self.Hawk01_XCLK_ComboBox.addItem("")
        self.Hawk01_XCLK_ComboBox.setObjectName(u"Hawk01_XCLK_ComboBox")
        self.Hawk01_XCLK_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_XCLK_ComboBox.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.Hawk01_XCLK_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.Hawk01_XCLK_ComboBox)

        self.Hawk01_MST_MODE_Label = QLabel(self.Hawk01_RegisterConfig)
        self.Hawk01_MST_MODE_Label.setObjectName(u"Hawk01_MST_MODE_Label")
        self.Hawk01_MST_MODE_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_MST_MODE_Label.setMaximumSize(QSize(85, 16777215))
        self.Hawk01_MST_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_MST_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Hawk01_MST_MODE_Label)

        self.Hawk01_MST_MODE_ComboBox = QComboBox(self.Hawk01_RegisterConfig)
        self.Hawk01_MST_MODE_ComboBox.addItem("")
        self.Hawk01_MST_MODE_ComboBox.addItem("")
        self.Hawk01_MST_MODE_ComboBox.setObjectName(u"Hawk01_MST_MODE_ComboBox")
        self.Hawk01_MST_MODE_ComboBox.setMaximumSize(QSize(350, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.Hawk01_MST_MODE_ComboBox)

        self.Hawk01_WORK_MODE_Label = QLabel(self.Hawk01_RegisterConfig)
        self.Hawk01_WORK_MODE_Label.setObjectName(u"Hawk01_WORK_MODE_Label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hawk01_WORK_MODE_Label.sizePolicy().hasHeightForWidth())
        self.Hawk01_WORK_MODE_Label.setSizePolicy(sizePolicy)
        self.Hawk01_WORK_MODE_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_WORK_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_WORK_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_WORK_MODE_Label.setFrameShadow(QFrame.Shadow.Raised)
        self.Hawk01_WORK_MODE_Label.setMargin(0)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.Hawk01_WORK_MODE_Label)

        self.Hawk01_WORK_MODE_ComboBox = ComboCheckBox(self.Hawk01_RegisterConfig)
        self.Hawk01_WORK_MODE_ComboBox.addItem("")
        self.Hawk01_WORK_MODE_ComboBox.addItem("")
        self.Hawk01_WORK_MODE_ComboBox.addItem("")
        self.Hawk01_WORK_MODE_ComboBox.addItem("")
        self.Hawk01_WORK_MODE_ComboBox.setObjectName(u"Hawk01_WORK_MODE_ComboBox")
        self.Hawk01_WORK_MODE_ComboBox.setMaximumSize(QSize(350, 16777215))
        self.Hawk01_WORK_MODE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.Hawk01_WORK_MODE_ComboBox)

        self.Hawk01_MIPI_RATE_Label = QLabel(self.Hawk01_RegisterConfig)
        self.Hawk01_MIPI_RATE_Label.setObjectName(u"Hawk01_MIPI_RATE_Label")
        sizePolicy.setHeightForWidth(self.Hawk01_MIPI_RATE_Label.sizePolicy().hasHeightForWidth())
        self.Hawk01_MIPI_RATE_Label.setSizePolicy(sizePolicy)
        self.Hawk01_MIPI_RATE_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_MIPI_RATE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_MIPI_RATE_Label.setFont(font1)
        self.Hawk01_MIPI_RATE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_MIPI_RATE_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.Hawk01_MIPI_RATE_Label)

        self.Hawk01_MIPI_RATE_ComboBox = QComboBox(self.Hawk01_RegisterConfig)
        self.Hawk01_MIPI_RATE_ComboBox.addItem("")
        self.Hawk01_MIPI_RATE_ComboBox.addItem("")
        self.Hawk01_MIPI_RATE_ComboBox.addItem("")
        self.Hawk01_MIPI_RATE_ComboBox.addItem("")
        self.Hawk01_MIPI_RATE_ComboBox.setObjectName(u"Hawk01_MIPI_RATE_ComboBox")
        self.Hawk01_MIPI_RATE_ComboBox.setMaximumSize(QSize(350, 16777215))
        self.Hawk01_MIPI_RATE_ComboBox.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.Hawk01_MIPI_RATE_ComboBox)

        self.Hawk01_MoreConfiguration = QGroupBox(self.Hawk01_RegisterConfig)
        self.Hawk01_MoreConfiguration.setObjectName(u"Hawk01_MoreConfiguration")
        self.Hawk01_MoreConfiguration.setMinimumSize(QSize(438, 180))
        self.Hawk01_MoreConfiguration.setMaximumSize(QSize(445, 16777215))
        self.Hawk01_MoreConfiguration.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.Hawk01_MoreConfiguration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, -1, 3, -1)
        self.Hawk01_TRG_I_EN_Label = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_TRG_I_EN_Label.setObjectName(u"Hawk01_TRG_I_EN_Label")
        self.Hawk01_TRG_I_EN_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_TRG_I_EN_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_TRG_I_EN_Label.setFont(font)
        self.Hawk01_TRG_I_EN_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_TRG_I_EN_Label, 2, 3, 1, 1)

        self.Hawk01_MINBIN_THRS_Lable = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_MINBIN_THRS_Lable.setObjectName(u"Hawk01_MINBIN_THRS_Lable")
        self.Hawk01_MINBIN_THRS_Lable.setMinimumSize(QSize(100, 0))
        self.Hawk01_MINBIN_THRS_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_MINBIN_THRS_Lable.setFont(font)
        self.Hawk01_MINBIN_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_MINBIN_THRS_Lable, 3, 0, 1, 1)

        self.Hawk01_MAXBIN_THRS_spinBox = QSpinBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_MAXBIN_THRS_spinBox.setObjectName(u"Hawk01_MAXBIN_THRS_spinBox")
        self.Hawk01_MAXBIN_THRS_spinBox.setMinimumSize(QSize(60, 0))
        self.Hawk01_MAXBIN_THRS_spinBox.setMinimum(1)
        self.Hawk01_MAXBIN_THRS_spinBox.setMaximum(167)
        self.Hawk01_MAXBIN_THRS_spinBox.setValue(167)

        self.gridLayout.addWidget(self.Hawk01_MAXBIN_THRS_spinBox, 3, 5, 1, 1)

        self.Hawk01_V_PXL_OUT_NUM_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_V_PXL_OUT_NUM_ComboBox.addItem("")
        self.Hawk01_V_PXL_OUT_NUM_ComboBox.addItem("")
        self.Hawk01_V_PXL_OUT_NUM_ComboBox.setObjectName(u"Hawk01_V_PXL_OUT_NUM_ComboBox")

        self.gridLayout.addWidget(self.Hawk01_V_PXL_OUT_NUM_ComboBox, 2, 1, 1, 1)

        self.Hawk01_PKS_ECHO_NUM_Lable = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_PKS_ECHO_NUM_Lable.setObjectName(u"Hawk01_PKS_ECHO_NUM_Lable")
        self.Hawk01_PKS_ECHO_NUM_Lable.setMinimumSize(QSize(100, 0))
        self.Hawk01_PKS_ECHO_NUM_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_PKS_ECHO_NUM_Lable.setFont(font)
        self.Hawk01_PKS_ECHO_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_PKS_ECHO_NUM_Lable, 4, 3, 1, 1)

        self.Hawk01_V_PXL_OUT_NUM_Label = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_V_PXL_OUT_NUM_Label.setObjectName(u"Hawk01_V_PXL_OUT_NUM_Label")
        self.Hawk01_V_PXL_OUT_NUM_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_V_PXL_OUT_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_V_PXL_OUT_NUM_Label.setFont(font)
        self.Hawk01_V_PXL_OUT_NUM_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_V_PXL_OUT_NUM_Label, 2, 0, 1, 1)

        self.Hawk01_TDC_BIN_W_Label = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_TDC_BIN_W_Label.setObjectName(u"Hawk01_TDC_BIN_W_Label")
        self.Hawk01_TDC_BIN_W_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_TDC_BIN_W_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_TDC_BIN_W_Label.setFont(font)
        self.Hawk01_TDC_BIN_W_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_TDC_BIN_W_Label, 0, 3, 1, 1)

        self.Hawk01_BIN_NUMBER_Value = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_BIN_NUMBER_Value.setObjectName(u"Hawk01_BIN_NUMBER_Value")
        self.Hawk01_BIN_NUMBER_Value.setMinimumSize(QSize(28, 25))
        self.Hawk01_BIN_NUMBER_Value.setMaximumSize(QSize(20, 16777215))
        self.Hawk01_BIN_NUMBER_Value.setFont(font1)
        self.Hawk01_BIN_NUMBER_Value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Hawk01_BIN_NUMBER_Value.setWordWrap(True)
        self.Hawk01_BIN_NUMBER_Value.setMargin(0)

        self.gridLayout.addWidget(self.Hawk01_BIN_NUMBER_Value, 3, 6, 1, 1)

        self.Hawk01_OUT_BIN_NUM_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_OUT_BIN_NUM_ComboBox.addItem("")
        self.Hawk01_OUT_BIN_NUM_ComboBox.addItem("")
        self.Hawk01_OUT_BIN_NUM_ComboBox.setObjectName(u"Hawk01_OUT_BIN_NUM_ComboBox")

        self.gridLayout.addWidget(self.Hawk01_OUT_BIN_NUM_ComboBox, 4, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 1, 1, 1)

        self.Hawk01_TDC_BIN_W_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_TDC_BIN_W_ComboBox.addItem("")
        self.Hawk01_TDC_BIN_W_ComboBox.addItem("")
        self.Hawk01_TDC_BIN_W_ComboBox.addItem("")
        self.Hawk01_TDC_BIN_W_ComboBox.addItem("")
        self.Hawk01_TDC_BIN_W_ComboBox.addItem("")
        self.Hawk01_TDC_BIN_W_ComboBox.addItem("")
        self.Hawk01_TDC_BIN_W_ComboBox.setObjectName(u"Hawk01_TDC_BIN_W_ComboBox")

        self.gridLayout.addWidget(self.Hawk01_TDC_BIN_W_ComboBox, 0, 5, 1, 1)

        self.Hawk01_MAXBIN_THRS_Lable_ = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_MAXBIN_THRS_Lable_.setObjectName(u"Hawk01_MAXBIN_THRS_Lable_")
        self.Hawk01_MAXBIN_THRS_Lable_.setMinimumSize(QSize(100, 0))
        self.Hawk01_MAXBIN_THRS_Lable_.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_MAXBIN_THRS_Lable_.setFont(font)
        self.Hawk01_MAXBIN_THRS_Lable_.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_MAXBIN_THRS_Lable_, 3, 3, 1, 1)

        self.Hawk01_MINBIN_THRS_spinBox = QSpinBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_MINBIN_THRS_spinBox.setObjectName(u"Hawk01_MINBIN_THRS_spinBox")
        self.Hawk01_MINBIN_THRS_spinBox.setEnabled(True)
        self.Hawk01_MINBIN_THRS_spinBox.setMinimumSize(QSize(60, 0))
        self.Hawk01_MINBIN_THRS_spinBox.setMinimum(0)
        self.Hawk01_MINBIN_THRS_spinBox.setMaximum(255)
        self.Hawk01_MINBIN_THRS_spinBox.setValue(0)

        self.gridLayout.addWidget(self.Hawk01_MINBIN_THRS_spinBox, 3, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_24, 2, 2, 1, 1)

        self.Hawk01_OUT_BIN_NUM_Lable = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_OUT_BIN_NUM_Lable.setObjectName(u"Hawk01_OUT_BIN_NUM_Lable")
        self.Hawk01_OUT_BIN_NUM_Lable.setMinimumSize(QSize(100, 0))
        self.Hawk01_OUT_BIN_NUM_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_OUT_BIN_NUM_Lable.setFont(font)
        self.Hawk01_OUT_BIN_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.Hawk01_OUT_BIN_NUM_Lable, 4, 0, 1, 1)

        self.Hawk01_PKS_ECHO_NUM_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_PKS_ECHO_NUM_ComboBox.addItem("")
        self.Hawk01_PKS_ECHO_NUM_ComboBox.addItem("")
        self.Hawk01_PKS_ECHO_NUM_ComboBox.addItem("")
        self.Hawk01_PKS_ECHO_NUM_ComboBox.addItem("")
        self.Hawk01_PKS_ECHO_NUM_ComboBox.addItem("")
        self.Hawk01_PKS_ECHO_NUM_ComboBox.setObjectName(u"Hawk01_PKS_ECHO_NUM_ComboBox")

        self.gridLayout.addWidget(self.Hawk01_PKS_ECHO_NUM_ComboBox, 4, 5, 1, 1)

        self.Hawk01_SYS_CLK_Label = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_SYS_CLK_Label.setObjectName(u"Hawk01_SYS_CLK_Label")
        self.Hawk01_SYS_CLK_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_SYS_CLK_Label.setFont(font)
        self.Hawk01_SYS_CLK_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_SYS_CLK_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Hawk01_SYS_CLK_Label, 0, 0, 1, 1)

        self.Hawk01_SYS_CLK_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_SYS_CLK_ComboBox.addItem("")
        self.Hawk01_SYS_CLK_ComboBox.addItem("")
        self.Hawk01_SYS_CLK_ComboBox.addItem("")
        self.Hawk01_SYS_CLK_ComboBox.setObjectName(u"Hawk01_SYS_CLK_ComboBox")
        self.Hawk01_SYS_CLK_ComboBox.setEnabled(False)
        self.Hawk01_SYS_CLK_ComboBox.setMinimumSize(QSize(10, 0))
        self.Hawk01_SYS_CLK_ComboBox.setFont(font1)
        self.Hawk01_SYS_CLK_ComboBox.setEditable(False)

        self.gridLayout.addWidget(self.Hawk01_SYS_CLK_ComboBox, 0, 1, 1, 1)

        self.Hawk01_TRG_I_EN_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_TRG_I_EN_ComboBox.addItem("")
        self.Hawk01_TRG_I_EN_ComboBox.addItem("")
        self.Hawk01_TRG_I_EN_ComboBox.setObjectName(u"Hawk01_TRG_I_EN_ComboBox")

        self.gridLayout.addWidget(self.Hawk01_TRG_I_EN_ComboBox, 2, 5, 1, 1)

        self.Hawk01_TX_FRM_MODE_Label = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_TX_FRM_MODE_Label.setObjectName(u"Hawk01_TX_FRM_MODE_Label")
        self.Hawk01_TX_FRM_MODE_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_TX_FRM_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_TX_FRM_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_TX_FRM_MODE_Label.setMargin(0)

        self.gridLayout.addWidget(self.Hawk01_TX_FRM_MODE_Label, 1, 0, 1, 1)

        self.Hawk01_TX_FRM_MODE_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_TX_FRM_MODE_ComboBox.addItem("")
        self.Hawk01_TX_FRM_MODE_ComboBox.addItem("")
        self.Hawk01_TX_FRM_MODE_ComboBox.setObjectName(u"Hawk01_TX_FRM_MODE_ComboBox")
        self.Hawk01_TX_FRM_MODE_ComboBox.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.Hawk01_TX_FRM_MODE_ComboBox, 1, 1, 1, 1)

        self.Hawk01_ONE_DT_MODE_Label = QLabel(self.Hawk01_MoreConfiguration)
        self.Hawk01_ONE_DT_MODE_Label.setObjectName(u"Hawk01_ONE_DT_MODE_Label")
        self.Hawk01_ONE_DT_MODE_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_ONE_DT_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_ONE_DT_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_ONE_DT_MODE_Label.setMargin(0)

        self.gridLayout.addWidget(self.Hawk01_ONE_DT_MODE_Label, 1, 3, 1, 1)

        self.Hawk01_ONE_DT_MODE_ComboBox = QComboBox(self.Hawk01_MoreConfiguration)
        self.Hawk01_ONE_DT_MODE_ComboBox.addItem("")
        self.Hawk01_ONE_DT_MODE_ComboBox.addItem("")
        self.Hawk01_ONE_DT_MODE_ComboBox.setObjectName(u"Hawk01_ONE_DT_MODE_ComboBox")
        self.Hawk01_ONE_DT_MODE_ComboBox.setMaximumSize(QSize(350, 16777215))

        self.gridLayout.addWidget(self.Hawk01_ONE_DT_MODE_ComboBox, 1, 5, 1, 1)


        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.Hawk01_MoreConfiguration)


        self.horizontalLayout_2.addWidget(self.Hawk01_RegisterConfig)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.Hawk01_ROIConfigGroup = QGroupBox(self.Hawk01_ScriptConfig)
        self.Hawk01_ROIConfigGroup.setObjectName(u"Hawk01_ROIConfigGroup")
        self.Hawk01_ROIConfigGroup.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.Hawk01_ROIConfigGroup)
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 6, 3, 0)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(8)
        self.formLayout_3.setContentsMargins(9, 0, 9, 9)
        self.Hawk01_SCAN_MODE_Label = QLabel(self.Hawk01_ROIConfigGroup)
        self.Hawk01_SCAN_MODE_Label.setObjectName(u"Hawk01_SCAN_MODE_Label")
        self.Hawk01_SCAN_MODE_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_SCAN_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_SCAN_MODE_Label.setFont(font1)
        self.Hawk01_SCAN_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_SCAN_MODE_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Hawk01_SCAN_MODE_Label)

        self.Hawk01_SCAN_MODE_ComboBox = QComboBox(self.Hawk01_ROIConfigGroup)
        self.Hawk01_SCAN_MODE_ComboBox.addItem("")
        self.Hawk01_SCAN_MODE_ComboBox.addItem("")
        self.Hawk01_SCAN_MODE_ComboBox.setObjectName(u"Hawk01_SCAN_MODE_ComboBox")
        self.Hawk01_SCAN_MODE_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_SCAN_MODE_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.Hawk01_SCAN_MODE_ComboBox.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.Hawk01_SCAN_MODE_ComboBox)

        self.Hawk01_V_ROLL_NUM_Label = QLabel(self.Hawk01_ROIConfigGroup)
        self.Hawk01_V_ROLL_NUM_Label.setObjectName(u"Hawk01_V_ROLL_NUM_Label")
        self.Hawk01_V_ROLL_NUM_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_V_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_V_ROLL_NUM_Label.setFont(font1)
        self.Hawk01_V_ROLL_NUM_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_V_ROLL_NUM_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Hawk01_V_ROLL_NUM_Label)

        self.Hawk01_H_ROLL_NUM_Label = QLabel(self.Hawk01_ROIConfigGroup)
        self.Hawk01_H_ROLL_NUM_Label.setObjectName(u"Hawk01_H_ROLL_NUM_Label")
        self.Hawk01_H_ROLL_NUM_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_H_ROLL_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_H_ROLL_NUM_Label.setFont(font1)
        self.Hawk01_H_ROLL_NUM_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_H_ROLL_NUM_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Hawk01_H_ROLL_NUM_Label)

        self.Hawk01_H_VLD_SEG_Label = QLabel(self.Hawk01_ROIConfigGroup)
        self.Hawk01_H_VLD_SEG_Label.setObjectName(u"Hawk01_H_VLD_SEG_Label")
        self.Hawk01_H_VLD_SEG_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_H_VLD_SEG_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_H_VLD_SEG_Label.setFont(font1)
        self.Hawk01_H_VLD_SEG_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_H_VLD_SEG_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.Hawk01_H_VLD_SEG_Label)

        self.Hawk01_H_ROLL_NUM_Frame = QFrame(self.Hawk01_ROIConfigGroup)
        self.Hawk01_H_ROLL_NUM_Frame.setObjectName(u"Hawk01_H_ROLL_NUM_Frame")
        self.H_ROLL_CMP = QHBoxLayout(self.Hawk01_H_ROLL_NUM_Frame)
        self.H_ROLL_CMP.setSpacing(0)
        self.H_ROLL_CMP.setObjectName(u"H_ROLL_CMP")
        self.H_ROLL_CMP.setContentsMargins(0, 0, 0, 0)
        self.Hawk01_H_ROLL_NUM_Slider = QSlider(self.Hawk01_H_ROLL_NUM_Frame)
        self.Hawk01_H_ROLL_NUM_Slider.setObjectName(u"Hawk01_H_ROLL_NUM_Slider")
        self.Hawk01_H_ROLL_NUM_Slider.setEnabled(True)
        self.Hawk01_H_ROLL_NUM_Slider.setMinimum(1)
        self.Hawk01_H_ROLL_NUM_Slider.setMaximum(16)
        self.Hawk01_H_ROLL_NUM_Slider.setPageStep(1)
        self.Hawk01_H_ROLL_NUM_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.H_ROLL_CMP.addWidget(self.Hawk01_H_ROLL_NUM_Slider)

        self.Hawk01_H_ROLL_NUM_Value = QLabel(self.Hawk01_H_ROLL_NUM_Frame)
        self.Hawk01_H_ROLL_NUM_Value.setObjectName(u"Hawk01_H_ROLL_NUM_Value")
        self.Hawk01_H_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.Hawk01_H_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.Hawk01_H_ROLL_NUM_Value.setFont(font1)
        self.Hawk01_H_ROLL_NUM_Value.setMidLineWidth(0)
        self.Hawk01_H_ROLL_NUM_Value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Hawk01_H_ROLL_NUM_Value.setMargin(0)

        self.H_ROLL_CMP.addWidget(self.Hawk01_H_ROLL_NUM_Value)


        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.Hawk01_H_ROLL_NUM_Frame)

        self.Hawk01_V_ROLL_NUM_Frame = QFrame(self.Hawk01_ROIConfigGroup)
        self.Hawk01_V_ROLL_NUM_Frame.setObjectName(u"Hawk01_V_ROLL_NUM_Frame")
        self.V_ROLL_NUM_CMP = QHBoxLayout(self.Hawk01_V_ROLL_NUM_Frame)
        self.V_ROLL_NUM_CMP.setSpacing(0)
        self.V_ROLL_NUM_CMP.setObjectName(u"V_ROLL_NUM_CMP")
        self.V_ROLL_NUM_CMP.setContentsMargins(0, 0, 0, 0)
        self.Hawk01_V_ROLL_NUM_Slider = QSlider(self.Hawk01_V_ROLL_NUM_Frame)
        self.Hawk01_V_ROLL_NUM_Slider.setObjectName(u"Hawk01_V_ROLL_NUM_Slider")
        self.Hawk01_V_ROLL_NUM_Slider.setMouseTracking(True)
        self.Hawk01_V_ROLL_NUM_Slider.setMinimum(1)
        self.Hawk01_V_ROLL_NUM_Slider.setMaximum(32)
        self.Hawk01_V_ROLL_NUM_Slider.setPageStep(1)
        self.Hawk01_V_ROLL_NUM_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.V_ROLL_NUM_CMP.addWidget(self.Hawk01_V_ROLL_NUM_Slider)

        self.Hawk01_V_ROLL_NUM_Value = QLabel(self.Hawk01_V_ROLL_NUM_Frame)
        self.Hawk01_V_ROLL_NUM_Value.setObjectName(u"Hawk01_V_ROLL_NUM_Value")
        self.Hawk01_V_ROLL_NUM_Value.setMinimumSize(QSize(20, 25))
        self.Hawk01_V_ROLL_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.Hawk01_V_ROLL_NUM_Value.setFont(font1)
        self.Hawk01_V_ROLL_NUM_Value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Hawk01_V_ROLL_NUM_Value.setWordWrap(True)
        self.Hawk01_V_ROLL_NUM_Value.setMargin(0)

        self.V_ROLL_NUM_CMP.addWidget(self.Hawk01_V_ROLL_NUM_Value)


        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.Hawk01_V_ROLL_NUM_Frame)

        self.Hawk01_H_VLD_SEG_Frame = QFrame(self.Hawk01_ROIConfigGroup)
        self.Hawk01_H_VLD_SEG_Frame.setObjectName(u"Hawk01_H_VLD_SEG_Frame")
        self.H_VLD_SEG_CMP = QHBoxLayout(self.Hawk01_H_VLD_SEG_Frame)
        self.H_VLD_SEG_CMP.setSpacing(0)
        self.H_VLD_SEG_CMP.setObjectName(u"H_VLD_SEG_CMP")
        self.H_VLD_SEG_CMP.setContentsMargins(0, 0, 0, 0)
        self.Hawk01_H_VLD_SEG_Slider = QSlider(self.Hawk01_H_VLD_SEG_Frame)
        self.Hawk01_H_VLD_SEG_Slider.setObjectName(u"Hawk01_H_VLD_SEG_Slider")
        self.Hawk01_H_VLD_SEG_Slider.setMinimum(1)
        self.Hawk01_H_VLD_SEG_Slider.setMaximum(16)
        self.Hawk01_H_VLD_SEG_Slider.setPageStep(1)
        self.Hawk01_H_VLD_SEG_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.H_VLD_SEG_CMP.addWidget(self.Hawk01_H_VLD_SEG_Slider)

        self.Hawk01_H_VLD_SEG_Value = QLabel(self.Hawk01_H_VLD_SEG_Frame)
        self.Hawk01_H_VLD_SEG_Value.setObjectName(u"Hawk01_H_VLD_SEG_Value")
        self.Hawk01_H_VLD_SEG_Value.setMinimumSize(QSize(20, 25))
        self.Hawk01_H_VLD_SEG_Value.setMaximumSize(QSize(20, 16777215))
        self.Hawk01_H_VLD_SEG_Value.setFont(font1)
        self.Hawk01_H_VLD_SEG_Value.setTextFormat(Qt.TextFormat.MarkdownText)
        self.Hawk01_H_VLD_SEG_Value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Hawk01_H_VLD_SEG_Value.setMargin(0)

        self.H_VLD_SEG_CMP.addWidget(self.Hawk01_H_VLD_SEG_Value)


        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.Hawk01_H_VLD_SEG_Frame)


        self.verticalLayout_11.addLayout(self.formLayout_3)

        self.Hawk01_ROIConfig = QTabWidget(self.Hawk01_ROIConfigGroup)
        self.Hawk01_ROIConfig.setObjectName(u"Hawk01_ROIConfig")
        self.Hawk01_ROIConfig.setMinimumSize(QSize(0, 0))
        self.Hawk01_ROIConfig.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_ROIConfig.setFont(font1)
        self.Hawk01_ROIConfig.setStyleSheet(u"")
        self.Hawk01_ROIConfig.setIconSize(QSize(0, 0))
        self.Hawk01_Config1byGUI = QWidget()
        self.Hawk01_Config1byGUI.setObjectName(u"Hawk01_Config1byGUI")
        self.verticalLayout_3 = QVBoxLayout(self.Hawk01_Config1byGUI)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.Hawk01_Config1byGUI_1 = QScrollArea(self.Hawk01_Config1byGUI)
        self.Hawk01_Config1byGUI_1.setObjectName(u"Hawk01_Config1byGUI_1")
        palette = QPalette()
        brush = QBrush(QColor(0, 120, 215, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        self.Hawk01_Config1byGUI_1.setPalette(palette)
        self.Hawk01_Config1byGUI_1.setStyleSheet(u"")
        self.Hawk01_Config1byGUI_1.setFrameShape(QFrame.Shape.NoFrame)
        self.Hawk01_Config1byGUI_1.setFrameShadow(QFrame.Shadow.Plain)
        self.Hawk01_Config1byGUI_1.setWidgetResizable(True)
        self.Hawk01_Config1byGUI_2 = QWidget()
        self.Hawk01_Config1byGUI_2.setObjectName(u"Hawk01_Config1byGUI_2")
        self.Hawk01_Config1byGUI_2.setGeometry(QRect(0, 0, 368, 375))
        self.formLayout = QFormLayout(self.Hawk01_Config1byGUI_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 20, 0)
        self.Hawk01_seg_hs_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_seg_hs_Label.setObjectName(u"Hawk01_seg_hs_Label")
        self.Hawk01_seg_hs_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_seg_hs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_seg_hs_Label.setFont(font1)
        self.Hawk01_seg_hs_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_seg_hs_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Hawk01_seg_hs_Label)

        self.Hawk01_seg_hs_spinBox = NoWheelSpinBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_seg_hs_spinBox.setObjectName(u"Hawk01_seg_hs_spinBox")
        self.Hawk01_seg_hs_spinBox.setMinimum(1)
        self.Hawk01_seg_hs_spinBox.setMaximum(16)
        self.Hawk01_seg_hs_spinBox.setValue(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Hawk01_seg_hs_spinBox)

        self.Hawk01_spad_vs_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_spad_vs_Label.setObjectName(u"Hawk01_spad_vs_Label")
        self.Hawk01_spad_vs_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_spad_vs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_spad_vs_Label.setFont(font1)
        self.Hawk01_spad_vs_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_spad_vs_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Hawk01_spad_vs_Label)

        self.Hawk01_spad_vs_spinBox = NoWheelSpinBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_spad_vs_spinBox.setObjectName(u"Hawk01_spad_vs_spinBox")
        self.Hawk01_spad_vs_spinBox.setMinimum(1)
        self.Hawk01_spad_vs_spinBox.setMaximum(576)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Hawk01_spad_vs_spinBox)

        self.Hawk01_light_shift_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_light_shift_Label.setObjectName(u"Hawk01_light_shift_Label")
        self.Hawk01_light_shift_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_light_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_light_shift_Label.setFont(font1)
        self.Hawk01_light_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_light_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Hawk01_light_shift_Label)

        self.Hawk01_light_shift_spinBox = NoWheelSpinBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_light_shift_spinBox.setObjectName(u"Hawk01_light_shift_spinBox")
        self.Hawk01_light_shift_spinBox.setMinimum(-576)
        self.Hawk01_light_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Hawk01_light_shift_spinBox)

        self.Hawk01_sublight_shift_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_sublight_shift_Label.setObjectName(u"Hawk01_sublight_shift_Label")
        self.Hawk01_sublight_shift_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_sublight_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_sublight_shift_Label.setFont(font1)
        self.Hawk01_sublight_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_sublight_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.Hawk01_sublight_shift_Label)

        self.Hawk01_sublight_shift_spinBox = NoWheelSpinBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_sublight_shift_spinBox.setObjectName(u"Hawk01_sublight_shift_spinBox")
        self.Hawk01_sublight_shift_spinBox.setMinimum(-576)
        self.Hawk01_sublight_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Hawk01_sublight_shift_spinBox)

        self.Hawk01_ROI_Shape_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_ROI_Shape_Label.setObjectName(u"Hawk01_ROI_Shape_Label")
        self.Hawk01_ROI_Shape_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_ROI_Shape_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_ROI_Shape_Label.setFont(font1)
        self.Hawk01_ROI_Shape_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_ROI_Shape_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.Hawk01_ROI_Shape_Label)

        self.Hawk01_ROI_Shape_ComboBox = NoWheelComboBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_ROI_Shape_ComboBox.addItem("")
        self.Hawk01_ROI_Shape_ComboBox.addItem("")
        self.Hawk01_ROI_Shape_ComboBox.setObjectName(u"Hawk01_ROI_Shape_ComboBox")
        self.Hawk01_ROI_Shape_ComboBox.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.Hawk01_ROI_Shape_ComboBox)

        self.Hawk01_v_spad_shift_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_v_spad_shift_Label.setObjectName(u"Hawk01_v_spad_shift_Label")
        self.Hawk01_v_spad_shift_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_v_spad_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_v_spad_shift_Label.setFont(font1)
        self.Hawk01_v_spad_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_v_spad_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.Hawk01_v_spad_shift_Label)

        self.Hawk01_v_spad_shift_spinBox = NoWheelSpinBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_v_spad_shift_spinBox.setObjectName(u"Hawk01_v_spad_shift_spinBox")
        self.Hawk01_v_spad_shift_spinBox.setMinimum(-576)
        self.Hawk01_v_spad_shift_spinBox.setMaximum(576)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.Hawk01_v_spad_shift_spinBox)

        self.Hawk01_h_seg_shift_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_h_seg_shift_Label.setObjectName(u"Hawk01_h_seg_shift_Label")
        self.Hawk01_h_seg_shift_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_h_seg_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_h_seg_shift_Label.setFont(font1)
        self.Hawk01_h_seg_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_h_seg_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Hawk01_h_seg_shift_Label)

        self.Hawk01_h_seg_shift_spinBox = NoWheelSpinBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_h_seg_shift_spinBox.setObjectName(u"Hawk01_h_seg_shift_spinBox")
        self.Hawk01_h_seg_shift_spinBox.setMinimum(0)
        self.Hawk01_h_seg_shift_spinBox.setMaximum(15)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Hawk01_h_seg_shift_spinBox)

        self.Hawk01_ROI_Retrace_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_ROI_Retrace_Label.setObjectName(u"Hawk01_ROI_Retrace_Label")
        self.Hawk01_ROI_Retrace_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_ROI_Retrace_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_ROI_Retrace_Label.setFont(font1)
        self.Hawk01_ROI_Retrace_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_ROI_Retrace_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.Hawk01_ROI_Retrace_Label)

        self.Hawk01_ROI_Retrace_ComboBox = NoWheelComboBox(self.Hawk01_Config1byGUI_2)
        self.Hawk01_ROI_Retrace_ComboBox.addItem("")
        self.Hawk01_ROI_Retrace_ComboBox.addItem("")
        self.Hawk01_ROI_Retrace_ComboBox.setObjectName(u"Hawk01_ROI_Retrace_ComboBox")
        self.Hawk01_ROI_Retrace_ComboBox.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.Hawk01_ROI_Retrace_ComboBox)

        self.Hawk01_sublight_group_Label = QLabel(self.Hawk01_Config1byGUI_2)
        self.Hawk01_sublight_group_Label.setObjectName(u"Hawk01_sublight_group_Label")
        self.Hawk01_sublight_group_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_sublight_group_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_sublight_group_Label.setFont(font1)
        self.Hawk01_sublight_group_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_sublight_group_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.Hawk01_sublight_group_Label)

        self.Hawk01_sublight_group_LineEdit = QLineEdit(self.Hawk01_Config1byGUI_2)
        self.Hawk01_sublight_group_LineEdit.setObjectName(u"Hawk01_sublight_group_LineEdit")
        self.Hawk01_sublight_group_LineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Hawk01_sublight_group_LineEdit.sizePolicy().hasHeightForWidth())
        self.Hawk01_sublight_group_LineEdit.setSizePolicy(sizePolicy1)
        self.Hawk01_sublight_group_LineEdit.setMinimumSize(QSize(0, 0))
        self.Hawk01_sublight_group_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Hawk01_sublight_group_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Hawk01_sublight_group_LineEdit.setReadOnly(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Hawk01_sublight_group_LineEdit)

        self.Hawk01_Config1byGUI_1.setWidget(self.Hawk01_Config1byGUI_2)

        self.verticalLayout_3.addWidget(self.Hawk01_Config1byGUI_1)

        self.Hawk01_ROIConfig.addTab(self.Hawk01_Config1byGUI, "")
        self.Hawk01_Config2byCOOR = QWidget()
        self.Hawk01_Config2byCOOR.setObjectName(u"Hawk01_Config2byCOOR")
        self.verticalLayout_4 = QVBoxLayout(self.Hawk01_Config2byCOOR)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, 0)
        self.Hawk01_Config2byCOOR_1 = QScrollArea(self.Hawk01_Config2byCOOR)
        self.Hawk01_Config2byCOOR_1.setObjectName(u"Hawk01_Config2byCOOR_1")
        self.Hawk01_Config2byCOOR_1.setStyleSheet(u"")
        self.Hawk01_Config2byCOOR_1.setFrameShape(QFrame.Shape.NoFrame)
        self.Hawk01_Config2byCOOR_1.setFrameShadow(QFrame.Shadow.Plain)
        self.Hawk01_Config2byCOOR_1.setWidgetResizable(True)
        self.Hawk01_Config2byCOOR_2 = QWidget()
        self.Hawk01_Config2byCOOR_2.setObjectName(u"Hawk01_Config2byCOOR_2")
        self.Hawk01_Config2byCOOR_2.setGeometry(QRect(0, 0, 368, 375))
        self.formLayout_4 = QFormLayout(self.Hawk01_Config2byCOOR_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 20, 0)
        self.Hawk01_Cali_File_Load_Label = QLabel(self.Hawk01_Config2byCOOR_2)
        self.Hawk01_Cali_File_Load_Label.setObjectName(u"Hawk01_Cali_File_Load_Label")
        self.Hawk01_Cali_File_Load_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_Cali_File_Load_Label.setFont(font1)
        self.Hawk01_Cali_File_Load_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_Cali_File_Load_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.Hawk01_Cali_File_Load_Label)

        self.Hawk01_Cali_File_Load_Layout = QHBoxLayout()
        self.Hawk01_Cali_File_Load_Layout.setSpacing(9)
        self.Hawk01_Cali_File_Load_Layout.setObjectName(u"Hawk01_Cali_File_Load_Layout")
        self.Hawk01_Cali_File_Load_LineEdit = QLineEdit(self.Hawk01_Config2byCOOR_2)
        self.Hawk01_Cali_File_Load_LineEdit.setObjectName(u"Hawk01_Cali_File_Load_LineEdit")
        self.Hawk01_Cali_File_Load_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Hawk01_Cali_File_Load_LineEdit.sizePolicy().hasHeightForWidth())
        self.Hawk01_Cali_File_Load_LineEdit.setSizePolicy(sizePolicy1)
        self.Hawk01_Cali_File_Load_LineEdit.setMinimumSize(QSize(0, 0))
        self.Hawk01_Cali_File_Load_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Hawk01_Cali_File_Load_LineEdit.setReadOnly(True)

        self.Hawk01_Cali_File_Load_Layout.addWidget(self.Hawk01_Cali_File_Load_LineEdit)

        self.Hawk01_Cali_File_Load_Button = QPushButton(self.Hawk01_Config2byCOOR_2)
        self.Hawk01_Cali_File_Load_Button.setObjectName(u"Hawk01_Cali_File_Load_Button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Hawk01_Cali_File_Load_Button.sizePolicy().hasHeightForWidth())
        self.Hawk01_Cali_File_Load_Button.setSizePolicy(sizePolicy2)
        self.Hawk01_Cali_File_Load_Button.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.Hawk01_Cali_File_Load_Layout.addWidget(self.Hawk01_Cali_File_Load_Button)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.Hawk01_Cali_File_Load_Layout)

        self.Hawk01_Excel_Sheet_sel_Label = QLabel(self.Hawk01_Config2byCOOR_2)
        self.Hawk01_Excel_Sheet_sel_Label.setObjectName(u"Hawk01_Excel_Sheet_sel_Label")
        self.Hawk01_Excel_Sheet_sel_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_Excel_Sheet_sel_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_Excel_Sheet_sel_Label.setFont(font1)
        self.Hawk01_Excel_Sheet_sel_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_Excel_Sheet_sel_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.Hawk01_Excel_Sheet_sel_Label)

        self.Hawk01_Excel_Sheet_sel_spinBox = QSpinBox(self.Hawk01_Config2byCOOR_2)
        self.Hawk01_Excel_Sheet_sel_spinBox.setObjectName(u"Hawk01_Excel_Sheet_sel_spinBox")
        self.Hawk01_Excel_Sheet_sel_spinBox.setMinimum(1)
        self.Hawk01_Excel_Sheet_sel_spinBox.setMaximum(100)
        self.Hawk01_Excel_Sheet_sel_spinBox.setValue(1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.Hawk01_Excel_Sheet_sel_spinBox)

        self.Hawk01_Config2byCOOR_1.setWidget(self.Hawk01_Config2byCOOR_2)

        self.verticalLayout_4.addWidget(self.Hawk01_Config2byCOOR_1)

        self.Hawk01_ROIConfig.addTab(self.Hawk01_Config2byCOOR, "")
        self.Hawk01_Config3ROIEdit = QWidget()
        self.Hawk01_Config3ROIEdit.setObjectName(u"Hawk01_Config3ROIEdit")
        self.verticalLayout_5 = QVBoxLayout(self.Hawk01_Config3ROIEdit)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.Hawk01_Config3ROIEdit_1 = QScrollArea(self.Hawk01_Config3ROIEdit)
        self.Hawk01_Config3ROIEdit_1.setObjectName(u"Hawk01_Config3ROIEdit_1")
        self.Hawk01_Config3ROIEdit_1.setStyleSheet(u"")
        self.Hawk01_Config3ROIEdit_1.setFrameShape(QFrame.Shape.NoFrame)
        self.Hawk01_Config3ROIEdit_1.setFrameShadow(QFrame.Shadow.Plain)
        self.Hawk01_Config3ROIEdit_1.setWidgetResizable(True)
        self.Hawk01_Config3ROIEdit_2 = QWidget()
        self.Hawk01_Config3ROIEdit_2.setObjectName(u"Hawk01_Config3ROIEdit_2")
        self.Hawk01_Config3ROIEdit_2.setGeometry(QRect(0, 0, 368, 375))
        self.formLayout_5 = QFormLayout(self.Hawk01_Config3ROIEdit_2)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(10)
        self.formLayout_5.setVerticalSpacing(6)
        self.formLayout_5.setContentsMargins(0, 0, 20, 0)
        self.Hawk01_ROI_File_Label = QLabel(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_ROI_File_Label.setObjectName(u"Hawk01_ROI_File_Label")
        self.Hawk01_ROI_File_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_ROI_File_Label.setFont(font1)
        self.Hawk01_ROI_File_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.Hawk01_ROI_File_Label)

        self.Hawk01_ROI_File_Layout = QHBoxLayout()
        self.Hawk01_ROI_File_Layout.setSpacing(9)
        self.Hawk01_ROI_File_Layout.setObjectName(u"Hawk01_ROI_File_Layout")
        self.Hawk01_ROI_File_LineEdit = QLineEdit(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_ROI_File_LineEdit.setObjectName(u"Hawk01_ROI_File_LineEdit")
        self.Hawk01_ROI_File_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Hawk01_ROI_File_LineEdit.sizePolicy().hasHeightForWidth())
        self.Hawk01_ROI_File_LineEdit.setSizePolicy(sizePolicy1)
        self.Hawk01_ROI_File_LineEdit.setMinimumSize(QSize(0, 0))
        self.Hawk01_ROI_File_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Hawk01_ROI_File_LineEdit.setReadOnly(True)

        self.Hawk01_ROI_File_Layout.addWidget(self.Hawk01_ROI_File_LineEdit)

        self.Hawk01_ROI_File_Button = QPushButton(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_ROI_File_Button.setObjectName(u"Hawk01_ROI_File_Button")
        sizePolicy2.setHeightForWidth(self.Hawk01_ROI_File_Button.sizePolicy().hasHeightForWidth())
        self.Hawk01_ROI_File_Button.setSizePolicy(sizePolicy2)
        self.Hawk01_ROI_File_Button.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.Hawk01_ROI_File_Layout.addWidget(self.Hawk01_ROI_File_Button)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.Hawk01_ROI_File_Layout)

        self.Hawk01_Start_Rolling_Label = QLabel(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_Start_Rolling_Label.setObjectName(u"Hawk01_Start_Rolling_Label")
        self.Hawk01_Start_Rolling_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_Start_Rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_Start_Rolling_Label.setFont(font1)
        self.Hawk01_Start_Rolling_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_Start_Rolling_Label.setFrameShadow(QFrame.Shadow.Raised)
        self.Hawk01_Start_Rolling_Label.setTextFormat(Qt.TextFormat.PlainText)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.Hawk01_Start_Rolling_Label)

        self.Hawk01_End_Rolling_Label = QLabel(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_End_Rolling_Label.setObjectName(u"Hawk01_End_Rolling_Label")
        self.Hawk01_End_Rolling_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_End_Rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_End_Rolling_Label.setFont(font1)
        self.Hawk01_End_Rolling_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Hawk01_End_Rolling_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.Hawk01_End_Rolling_Label)

        self.Hawk01_End_Rolling_SpinBox = QSpinBox(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_End_Rolling_SpinBox.setObjectName(u"Hawk01_End_Rolling_SpinBox")
        self.Hawk01_End_Rolling_SpinBox.setMinimum(1)
        self.Hawk01_End_Rolling_SpinBox.setMaximum(32)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.Hawk01_End_Rolling_SpinBox)

        self.Hawk01_Start_Rolling_SpinBox = QSpinBox(self.Hawk01_Config3ROIEdit_2)
        self.Hawk01_Start_Rolling_SpinBox.setObjectName(u"Hawk01_Start_Rolling_SpinBox")
        self.Hawk01_Start_Rolling_SpinBox.setMinimum(1)
        self.Hawk01_Start_Rolling_SpinBox.setMaximum(32)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.Hawk01_Start_Rolling_SpinBox)

        self.Hawk01_Config3ROIEdit_1.setWidget(self.Hawk01_Config3ROIEdit_2)

        self.verticalLayout_5.addWidget(self.Hawk01_Config3ROIEdit_1)

        self.Hawk01_ROIConfig.addTab(self.Hawk01_Config3ROIEdit, "")
        self.Hawk01_Config4ROICali = QWidget()
        self.Hawk01_Config4ROICali.setObjectName(u"Hawk01_Config4ROICali")
        self.verticalLayout_2 = QVBoxLayout(self.Hawk01_Config4ROICali)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Hawk01_Config4ROICali_1 = QScrollArea(self.Hawk01_Config4ROICali)
        self.Hawk01_Config4ROICali_1.setObjectName(u"Hawk01_Config4ROICali_1")
        self.Hawk01_Config4ROICali_1.setStyleSheet(u"")
        self.Hawk01_Config4ROICali_1.setFrameShape(QFrame.Shape.NoFrame)
        self.Hawk01_Config4ROICali_1.setFrameShadow(QFrame.Shadow.Plain)
        self.Hawk01_Config4ROICali_1.setWidgetResizable(True)
        self.Hawk01_Config4ROICali_2 = QWidget()
        self.Hawk01_Config4ROICali_2.setObjectName(u"Hawk01_Config4ROICali_2")
        self.Hawk01_Config4ROICali_2.setGeometry(QRect(0, 0, 368, 366))
        self.formLayout_7 = QFormLayout(self.Hawk01_Config4ROICali_2)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(10)
        self.formLayout_7.setVerticalSpacing(6)
        self.formLayout_7.setContentsMargins(0, 0, 20, 0)
        self.Hawk01_cali_file_path_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_file_path_Label.setObjectName(u"Hawk01_cali_file_path_Label")
        self.Hawk01_cali_file_path_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_cali_file_path_Label.setFont(font1)
        self.Hawk01_cali_file_path_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.Hawk01_cali_file_path_Label)

        self.Hawk01_cali_file_path_Layout = QHBoxLayout()
        self.Hawk01_cali_file_path_Layout.setSpacing(9)
        self.Hawk01_cali_file_path_Layout.setObjectName(u"Hawk01_cali_file_path_Layout")
        self.Hawk01_cali_file_path_LineEdit = QLineEdit(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_file_path_LineEdit.setObjectName(u"Hawk01_cali_file_path_LineEdit")
        self.Hawk01_cali_file_path_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Hawk01_cali_file_path_LineEdit.sizePolicy().hasHeightForWidth())
        self.Hawk01_cali_file_path_LineEdit.setSizePolicy(sizePolicy1)
        self.Hawk01_cali_file_path_LineEdit.setMinimumSize(QSize(0, 0))
        self.Hawk01_cali_file_path_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Hawk01_cali_file_path_LineEdit.setReadOnly(True)

        self.Hawk01_cali_file_path_Layout.addWidget(self.Hawk01_cali_file_path_LineEdit)

        self.Hawk01_cali_file_path_Button = QPushButton(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_file_path_Button.setObjectName(u"Hawk01_cali_file_path_Button")
        sizePolicy2.setHeightForWidth(self.Hawk01_cali_file_path_Button.sizePolicy().hasHeightForWidth())
        self.Hawk01_cali_file_path_Button.setSizePolicy(sizePolicy2)
        self.Hawk01_cali_file_path_Button.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.Hawk01_cali_file_path_Layout.addWidget(self.Hawk01_cali_file_path_Button)


        self.formLayout_7.setLayout(0, QFormLayout.FieldRole, self.Hawk01_cali_file_path_Layout)

        self.Hawk01_img_mirror_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_img_mirror_Label.setObjectName(u"Hawk01_img_mirror_Label")
        self.Hawk01_img_mirror_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_img_mirror_Label.setFont(font1)
        self.Hawk01_img_mirror_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.Hawk01_img_mirror_Label)

        self.Hawk01_img_mirror_ComboBox = NoWheelComboBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_img_mirror_ComboBox.addItem("")
        self.Hawk01_img_mirror_ComboBox.addItem("")
        self.Hawk01_img_mirror_ComboBox.addItem("")
        self.Hawk01_img_mirror_ComboBox.addItem("")
        self.Hawk01_img_mirror_ComboBox.setObjectName(u"Hawk01_img_mirror_ComboBox")
        self.Hawk01_img_mirror_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_img_mirror_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_img_mirror_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.Hawk01_img_mirror_ComboBox)

        self.Hawk01_remove_noise_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_remove_noise_Label.setObjectName(u"Hawk01_remove_noise_Label")
        self.Hawk01_remove_noise_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_remove_noise_Label.setFont(font1)
        self.Hawk01_remove_noise_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.Hawk01_remove_noise_Label)

        self.Hawk01_remove_noise_ComboBox = NoWheelComboBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_remove_noise_ComboBox.addItem("")
        self.Hawk01_remove_noise_ComboBox.addItem("")
        self.Hawk01_remove_noise_ComboBox.setObjectName(u"Hawk01_remove_noise_ComboBox")
        self.Hawk01_remove_noise_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_remove_noise_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_remove_noise_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.Hawk01_remove_noise_ComboBox)

        self.Hawk01_light_smooth_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_light_smooth_Label.setObjectName(u"Hawk01_light_smooth_Label")
        self.Hawk01_light_smooth_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_light_smooth_Label.setFont(font1)
        self.Hawk01_light_smooth_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.Hawk01_light_smooth_Label)

        self.Hawk01_light_smooth_ComboBox = NoWheelComboBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_light_smooth_ComboBox.addItem("")
        self.Hawk01_light_smooth_ComboBox.addItem("")
        self.Hawk01_light_smooth_ComboBox.setObjectName(u"Hawk01_light_smooth_ComboBox")
        self.Hawk01_light_smooth_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_light_smooth_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_light_smooth_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.Hawk01_light_smooth_ComboBox)

        self.Hawk01_curvature_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_curvature_Label.setObjectName(u"Hawk01_curvature_Label")
        self.Hawk01_curvature_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_curvature_Label.setFont(font1)
        self.Hawk01_curvature_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.Hawk01_curvature_Label)

        self.Hawk01_curvature_SpinBox = NoWheelSpinBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_curvature_SpinBox.setObjectName(u"Hawk01_curvature_SpinBox")
        self.Hawk01_curvature_SpinBox.setMinimum(0)
        self.Hawk01_curvature_SpinBox.setMaximum(1000)
        self.Hawk01_curvature_SpinBox.setValue(2)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.Hawk01_curvature_SpinBox)

        self.Hawk01_correct_thres_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_correct_thres_Label.setObjectName(u"Hawk01_correct_thres_Label")
        self.Hawk01_correct_thres_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_correct_thres_Label.setFont(font1)
        self.Hawk01_correct_thres_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.Hawk01_correct_thres_Label)

        self.Hawk01_correct_thres_SpinBox = NoWheelSpinBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_correct_thres_SpinBox.setObjectName(u"Hawk01_correct_thres_SpinBox")
        self.Hawk01_correct_thres_SpinBox.setMinimum(0)
        self.Hawk01_correct_thres_SpinBox.setMaximum(100)
        self.Hawk01_correct_thres_SpinBox.setValue(1)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.Hawk01_correct_thres_SpinBox)

        self.Hawk01_cali_order_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_order_Label.setObjectName(u"Hawk01_cali_order_Label")
        self.Hawk01_cali_order_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_cali_order_Label.setFont(font1)
        self.Hawk01_cali_order_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.Hawk01_cali_order_Label)

        self.Hawk01_cali_order_ComboBox = NoWheelComboBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_order_ComboBox.addItem("")
        self.Hawk01_cali_order_ComboBox.addItem("")
        self.Hawk01_cali_order_ComboBox.setObjectName(u"Hawk01_cali_order_ComboBox")
        self.Hawk01_cali_order_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_cali_order_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_cali_order_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.Hawk01_cali_order_ComboBox)

        self.Hawk01_cali_frm_num_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_frm_num_Label.setObjectName(u"Hawk01_cali_frm_num_Label")
        self.Hawk01_cali_frm_num_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_cali_frm_num_Label.setFont(font1)
        self.Hawk01_cali_frm_num_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.Hawk01_cali_frm_num_Label)

        self.Hawk01_cali_frm_num__SpinBox = NoWheelSpinBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_cali_frm_num__SpinBox.setObjectName(u"Hawk01_cali_frm_num__SpinBox")
        self.Hawk01_cali_frm_num__SpinBox.setMinimum(1)
        self.Hawk01_cali_frm_num__SpinBox.setMaximum(10000)

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.Hawk01_cali_frm_num__SpinBox)

        self.Hawk01_ref_segment_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_ref_segment_Label.setObjectName(u"Hawk01_ref_segment_Label")
        self.Hawk01_ref_segment_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_ref_segment_Label.setFont(font1)
        self.Hawk01_ref_segment_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.Hawk01_ref_segment_Label)

        self.Hawk01_ref_segment_SpinBox = NoWheelSpinBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_ref_segment_SpinBox.setObjectName(u"Hawk01_ref_segment_SpinBox")
        self.Hawk01_ref_segment_SpinBox.setMinimum(0)
        self.Hawk01_ref_segment_SpinBox.setMaximum(16)
        self.Hawk01_ref_segment_SpinBox.setValue(0)

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.Hawk01_ref_segment_SpinBox)

        self.Hawk01_mode_2D_Label = QLabel(self.Hawk01_Config4ROICali_2)
        self.Hawk01_mode_2D_Label.setObjectName(u"Hawk01_mode_2D_Label")
        self.Hawk01_mode_2D_Label.setMinimumSize(QSize(100, 0))
        self.Hawk01_mode_2D_Label.setFont(font1)
        self.Hawk01_mode_2D_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.Hawk01_mode_2D_Label)

        self.Hawk01_mode_2D_ComboBox = NoWheelComboBox(self.Hawk01_Config4ROICali_2)
        self.Hawk01_mode_2D_ComboBox.addItem("")
        self.Hawk01_mode_2D_ComboBox.addItem("")
        self.Hawk01_mode_2D_ComboBox.setObjectName(u"Hawk01_mode_2D_ComboBox")
        self.Hawk01_mode_2D_ComboBox.setMinimumSize(QSize(150, 0))
        self.Hawk01_mode_2D_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_mode_2D_ComboBox.setFont(font1)

        self.formLayout_7.setWidget(9, QFormLayout.FieldRole, self.Hawk01_mode_2D_ComboBox)

        self.Hawk01_Config4ROICali_1.setWidget(self.Hawk01_Config4ROICali_2)

        self.verticalLayout_2.addWidget(self.Hawk01_Config4ROICali_1)

        self.Hawk01_ROIConfig.addTab(self.Hawk01_Config4ROICali, "")

        self.verticalLayout_11.addWidget(self.Hawk01_ROIConfig)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, 3)
        self.Hawk01_ROIZoneConfig = QLabel(self.Hawk01_ROIConfigGroup)
        self.Hawk01_ROIZoneConfig.setObjectName(u"Hawk01_ROIZoneConfig")
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush1)
        self.Hawk01_ROIZoneConfig.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.Hawk01_ROIZoneConfig.setFont(font2)
        self.Hawk01_ROIZoneConfig.setStyleSheet(u"QLabel {\n"
"font: 700 9pt \"Consolas\";\n"
"}")
        self.Hawk01_ROIZoneConfig.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Hawk01_ROIZoneConfig.setMargin(0)
        self.Hawk01_ROIZoneConfig.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.Hawk01_ROIZoneConfig)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_18)

        self.Hawk01_ROIView = QPushButton(self.Hawk01_ROIConfigGroup)
        self.Hawk01_ROIView.setObjectName(u"Hawk01_ROIView")
        self.Hawk01_ROIView.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.Hawk01_ROIView)

        self.Hawk01_ROISave = QPushButton(self.Hawk01_ROIConfigGroup)
        self.Hawk01_ROISave.setObjectName(u"Hawk01_ROISave")
        self.Hawk01_ROISave.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.Hawk01_ROISave)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.Hawk01_ROIConfigGroup)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_12.addWidget(self.Hawk01_ScriptConfig)

        self.Hawk01_FileConifg = QGroupBox(self.Hawk01)
        self.Hawk01_FileConifg.setObjectName(u"Hawk01_FileConifg")
        self.Hawk01_FileConifg.setMinimumSize(QSize(300, 0))
        self.Hawk01_FileConifg.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_6 = QGridLayout(self.Hawk01_FileConifg)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 9, 9, 1)
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 4, 4, 1, 1)

        self.Hawk01_roi_sram_name_Label = QLabel(self.Hawk01_FileConifg)
        self.Hawk01_roi_sram_name_Label.setObjectName(u"Hawk01_roi_sram_name_Label")
        self.Hawk01_roi_sram_name_Label.setFont(font)

        self.gridLayout_6.addWidget(self.Hawk01_roi_sram_name_Label, 4, 0, 1, 1)

        self.Hawk01_reg_script_name_LineEdit = QLineEdit(self.Hawk01_FileConifg)
        self.Hawk01_reg_script_name_LineEdit.setObjectName(u"Hawk01_reg_script_name_LineEdit")
        self.Hawk01_reg_script_name_LineEdit.setMinimumSize(QSize(0, 0))
        self.Hawk01_reg_script_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Hawk01_reg_script_name_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.Hawk01_reg_script_name_LineEdit, 2, 1, 1, 1)

        self.Hawk01_file_save_dir_Label = QLabel(self.Hawk01_FileConifg)
        self.Hawk01_file_save_dir_Label.setObjectName(u"Hawk01_file_save_dir_Label")
        self.Hawk01_file_save_dir_Label.setMinimumSize(QSize(0, 0))
        self.Hawk01_file_save_dir_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_file_save_dir_Label.setFont(font1)
        self.Hawk01_file_save_dir_Label.setFrameShape(QFrame.Shape.NoFrame)
        self.Hawk01_file_save_dir_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_6.addWidget(self.Hawk01_file_save_dir_Label, 6, 0, 1, 1)

        self.Hawk01_reference_script_sel_Button = QPushButton(self.Hawk01_FileConifg)
        self.Hawk01_reference_script_sel_Button.setObjectName(u"Hawk01_reference_script_sel_Button")
        sizePolicy2.setHeightForWidth(self.Hawk01_reference_script_sel_Button.sizePolicy().hasHeightForWidth())
        self.Hawk01_reference_script_sel_Button.setSizePolicy(sizePolicy2)
        self.Hawk01_reference_script_sel_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.Hawk01_reference_script_sel_Button, 1, 2, 1, 1)

        self.Hawk01_roi_sram_name_CheckBox = QCheckBox(self.Hawk01_FileConifg)
        self.Hawk01_roi_sram_name_CheckBox.setObjectName(u"Hawk01_roi_sram_name_CheckBox")

        self.gridLayout_6.addWidget(self.Hawk01_roi_sram_name_CheckBox, 4, 3, 1, 1)

        self.Hawk01_roi_sram_name_LineEdit = QLineEdit(self.Hawk01_FileConifg)
        self.Hawk01_roi_sram_name_LineEdit.setObjectName(u"Hawk01_roi_sram_name_LineEdit")
        self.Hawk01_roi_sram_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Hawk01_roi_sram_name_LineEdit.setFont(font)

        self.gridLayout_6.addWidget(self.Hawk01_roi_sram_name_LineEdit, 4, 1, 1, 1)

        self.Hawk01_reference_script_LineEdit = QLineEdit(self.Hawk01_FileConifg)
        self.Hawk01_reference_script_LineEdit.setObjectName(u"Hawk01_reference_script_LineEdit")
        self.Hawk01_reference_script_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Hawk01_reference_script_LineEdit.sizePolicy().hasHeightForWidth())
        self.Hawk01_reference_script_LineEdit.setSizePolicy(sizePolicy1)
        self.Hawk01_reference_script_LineEdit.setMinimumSize(QSize(0, 0))
        self.Hawk01_reference_script_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Hawk01_reference_script_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Hawk01_reference_script_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.Hawk01_reference_script_LineEdit, 1, 1, 1, 1)

        self.Hawk01_ButtonCollectionFrame = QFrame(self.Hawk01_FileConifg)
        self.Hawk01_ButtonCollectionFrame.setObjectName(u"Hawk01_ButtonCollectionFrame")
        self.horizontalLayout_5 = QHBoxLayout(self.Hawk01_ButtonCollectionFrame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 2, -1, -1)
        self.Hawk01_Save = QPushButton(self.Hawk01_ButtonCollectionFrame)
        self.Hawk01_Save.setObjectName(u"Hawk01_Save")
        sizePolicy1.setHeightForWidth(self.Hawk01_Save.sizePolicy().hasHeightForWidth())
        self.Hawk01_Save.setSizePolicy(sizePolicy1)
        self.Hawk01_Save.setMinimumSize(QSize(90, 0))
        self.Hawk01_Save.setFont(font)
        self.Hawk01_Save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.Hawk01_Save)

        self.Hawk01_Open = QPushButton(self.Hawk01_ButtonCollectionFrame)
        self.Hawk01_Open.setObjectName(u"Hawk01_Open")
        sizePolicy1.setHeightForWidth(self.Hawk01_Open.sizePolicy().hasHeightForWidth())
        self.Hawk01_Open.setSizePolicy(sizePolicy1)
        self.Hawk01_Open.setMinimumSize(QSize(90, 0))
        self.Hawk01_Open.setFont(font)
        self.Hawk01_Open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.Hawk01_Open)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout_6.addWidget(self.Hawk01_ButtonCollectionFrame, 7, 0, 1, 5)

        self.Hawk01_reference_script_Label = QLabel(self.Hawk01_FileConifg)
        self.Hawk01_reference_script_Label.setObjectName(u"Hawk01_reference_script_Label")
        self.Hawk01_reference_script_Label.setMinimumSize(QSize(0, 0))
        self.Hawk01_reference_script_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Hawk01_reference_script_Label.setFont(font1)
        self.Hawk01_reference_script_Label.setFrameShape(QFrame.Shape.NoFrame)
        self.Hawk01_reference_script_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_6.addWidget(self.Hawk01_reference_script_Label, 1, 0, 1, 1)

        self.Hawk01_file_save_dir_LineEdit = QLineEdit(self.Hawk01_FileConifg)
        self.Hawk01_file_save_dir_LineEdit.setObjectName(u"Hawk01_file_save_dir_LineEdit")
        self.Hawk01_file_save_dir_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Hawk01_file_save_dir_LineEdit.sizePolicy().hasHeightForWidth())
        self.Hawk01_file_save_dir_LineEdit.setSizePolicy(sizePolicy1)
        self.Hawk01_file_save_dir_LineEdit.setMinimumSize(QSize(350, 0))
        self.Hawk01_file_save_dir_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Hawk01_file_save_dir_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Hawk01_file_save_dir_LineEdit.setReadOnly(False)

        self.gridLayout_6.addWidget(self.Hawk01_file_save_dir_LineEdit, 6, 1, 1, 1)

        self.Hawk01_file_save_dir_Button = QPushButton(self.Hawk01_FileConifg)
        self.Hawk01_file_save_dir_Button.setObjectName(u"Hawk01_file_save_dir_Button")
        sizePolicy2.setHeightForWidth(self.Hawk01_file_save_dir_Button.sizePolicy().hasHeightForWidth())
        self.Hawk01_file_save_dir_Button.setSizePolicy(sizePolicy2)
        self.Hawk01_file_save_dir_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.Hawk01_file_save_dir_Button, 6, 2, 1, 1)

        self.Hawk01_reg_script_name_Label = QLabel(self.Hawk01_FileConifg)
        self.Hawk01_reg_script_name_Label.setObjectName(u"Hawk01_reg_script_name_Label")
        self.Hawk01_reg_script_name_Label.setFont(font)

        self.gridLayout_6.addWidget(self.Hawk01_reg_script_name_Label, 2, 0, 1, 1)

        self.Hawk01_reference_script_parse_Button = QPushButton(self.Hawk01_FileConifg)
        self.Hawk01_reference_script_parse_Button.setObjectName(u"Hawk01_reference_script_parse_Button")
        sizePolicy2.setHeightForWidth(self.Hawk01_reference_script_parse_Button.sizePolicy().hasHeightForWidth())
        self.Hawk01_reference_script_parse_Button.setSizePolicy(sizePolicy2)
        self.Hawk01_reference_script_parse_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.Hawk01_reference_script_parse_Button, 1, 3, 1, 1)


        self.verticalLayout_12.addWidget(self.Hawk01_FileConifg)

        self.pages.addWidget(self.Hawk01)
        self.Swan01 = QWidget()
        self.Swan01.setObjectName(u"Swan01")
        self.verticalLayout_13 = QVBoxLayout(self.Swan01)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 0)
        self.Swan01_ScriptConfig = QGroupBox(self.Swan01)
        self.Swan01_ScriptConfig.setObjectName(u"Swan01_ScriptConfig")
        self.horizontalLayout_23 = QHBoxLayout(self.Swan01_ScriptConfig)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(3, 3, 3, 3)
        self.Swan01_RegisterConfig = QGroupBox(self.Swan01_ScriptConfig)
        self.Swan01_RegisterConfig.setObjectName(u"Swan01_RegisterConfig")
        self.Swan01_RegisterConfig.setMinimumSize(QSize(720, 0))
        self.verticalLayout_19 = QVBoxLayout(self.Swan01_RegisterConfig)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Swan01_RegisterConfig_1 = QScrollArea(self.Swan01_RegisterConfig)
        self.Swan01_RegisterConfig_1.setObjectName(u"Swan01_RegisterConfig_1")
        self.Swan01_RegisterConfig_1.setFrameShape(QFrame.Shape.NoFrame)
        self.Swan01_RegisterConfig_1.setWidgetResizable(True)
        self.Swan01_RegisterConfig_2 = QWidget()
        self.Swan01_RegisterConfig_2.setObjectName(u"Swan01_RegisterConfig_2")
        self.Swan01_RegisterConfig_2.setGeometry(QRect(0, -32, 706, 623))
        self.gridLayout_4 = QGridLayout(self.Swan01_RegisterConfig_2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.Swan01_INTF_DET_EN_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_INTF_DET_EN_ComboBox.addItem("")
        self.Swan01_INTF_DET_EN_ComboBox.addItem("")
        self.Swan01_INTF_DET_EN_ComboBox.setObjectName(u"Swan01_INTF_DET_EN_ComboBox")
        self.Swan01_INTF_DET_EN_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_INTF_DET_EN_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_INTF_DET_EN_ComboBox, 10, 1, 1, 1)

        self.Swan01_OUT_TOTALBIN_NUM_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_TOTALBIN_NUM_Lable.setObjectName(u"Swan01_OUT_TOTALBIN_NUM_Lable")
        self.Swan01_OUT_TOTALBIN_NUM_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_OUT_TOTALBIN_NUM_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_OUT_TOTALBIN_NUM_Lable.setFont(font)
        self.Swan01_OUT_TOTALBIN_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_TOTALBIN_NUM_Lable, 13, 3, 1, 1)

        self.Swan01_SYNC_POL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_SYNC_POL_ComboBox.addItem("")
        self.Swan01_SYNC_POL_ComboBox.addItem("")
        self.Swan01_SYNC_POL_ComboBox.setObjectName(u"Swan01_SYNC_POL_ComboBox")
        self.Swan01_SYNC_POL_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_SYNC_POL_ComboBox, 2, 4, 1, 1)

        self.Swan01_ANGLE_GRP_SW_NUM_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_ANGLE_GRP_SW_NUM_Label.setObjectName(u"Swan01_ANGLE_GRP_SW_NUM_Label")
        self.Swan01_ANGLE_GRP_SW_NUM_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_ANGLE_GRP_SW_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_ANGLE_GRP_SW_NUM_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_ANGLE_GRP_SW_NUM_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_ANGLE_GRP_SW_NUM_Label, 5, 0, 1, 1)

        self.Swan01_INTF_HIST_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_INTF_HIST_MODE_ComboBox.addItem("")
        self.Swan01_INTF_HIST_MODE_ComboBox.addItem("")
        self.Swan01_INTF_HIST_MODE_ComboBox.setObjectName(u"Swan01_INTF_HIST_MODE_ComboBox")
        self.Swan01_INTF_HIST_MODE_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_INTF_HIST_MODE_ComboBox, 10, 4, 1, 1)

        self.Swan01_OUT_FIR_RAW_SEL_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_FIR_RAW_SEL_Lable.setObjectName(u"Swan01_OUT_FIR_RAW_SEL_Lable")
        self.Swan01_OUT_FIR_RAW_SEL_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_OUT_FIR_RAW_SEL_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_OUT_FIR_RAW_SEL_Lable.setFont(font)
        self.Swan01_OUT_FIR_RAW_SEL_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_FIR_RAW_SEL_Lable, 16, 0, 1, 1)

        self.Swan01_MST_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_MST_MODE_ComboBox.addItem("")
        self.Swan01_MST_MODE_ComboBox.addItem("")
        self.Swan01_MST_MODE_ComboBox.setObjectName(u"Swan01_MST_MODE_ComboBox")
        self.Swan01_MST_MODE_ComboBox.setMinimumSize(QSize(165, 0))
        self.Swan01_MST_MODE_ComboBox.setMaximumSize(QSize(165, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_MST_MODE_ComboBox, 2, 1, 1, 1)

        self.Swan01_FWHM_SEARCH_NUM_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_FWHM_SEARCH_NUM_Lable.setObjectName(u"Swan01_FWHM_SEARCH_NUM_Lable")
        self.Swan01_FWHM_SEARCH_NUM_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_FWHM_SEARCH_NUM_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_FWHM_SEARCH_NUM_Lable.setFont(font)
        self.Swan01_FWHM_SEARCH_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_FWHM_SEARCH_NUM_Lable, 18, 3, 1, 1)

        self.Swan01_PXL_BINN_SEL_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_PXL_BINN_SEL_Label.setObjectName(u"Swan01_PXL_BINN_SEL_Label")
        self.Swan01_PXL_BINN_SEL_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_PXL_BINN_SEL_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_PXL_BINN_SEL_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_PXL_BINN_SEL_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_PXL_BINN_SEL_Label, 23, 0, 1, 1)

        self.Swan01_TX_FRM_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_TX_FRM_MODE_ComboBox.addItem("")
        self.Swan01_TX_FRM_MODE_ComboBox.addItem("")
        self.Swan01_TX_FRM_MODE_ComboBox.setObjectName(u"Swan01_TX_FRM_MODE_ComboBox")
        self.Swan01_TX_FRM_MODE_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_TX_FRM_MODE_ComboBox, 21, 1, 1, 1)

        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setObjectName(u"Swan01_ECHO_ORDER_NEAR_NUM_spinBox")
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setMinimumSize(QSize(0, 0))
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setMinimum(0)
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setMaximum(15)
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setSingleStep(1)
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setValue(0)

        self.gridLayout_4.addWidget(self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox, 19, 1, 1, 1)

        self.Swan01_OUT_ECHO_NUM_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHO_NUM_ComboBox.addItem("")
        self.Swan01_OUT_ECHO_NUM_ComboBox.addItem("")
        self.Swan01_OUT_ECHO_NUM_ComboBox.addItem("")
        self.Swan01_OUT_ECHO_NUM_ComboBox.addItem("")
        self.Swan01_OUT_ECHO_NUM_ComboBox.addItem("")
        self.Swan01_OUT_ECHO_NUM_ComboBox.addItem("")
        self.Swan01_OUT_ECHO_NUM_ComboBox.setObjectName(u"Swan01_OUT_ECHO_NUM_ComboBox")
        self.Swan01_OUT_ECHO_NUM_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHO_NUM_ComboBox, 15, 1, 1, 1)

        self.Swan01_HIST_MAXBIN_THRS_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_HIST_MAXBIN_THRS_Lable.setObjectName(u"Swan01_HIST_MAXBIN_THRS_Lable")
        self.Swan01_HIST_MAXBIN_THRS_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_HIST_MAXBIN_THRS_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_HIST_MAXBIN_THRS_Lable.setFont(font)
        self.Swan01_HIST_MAXBIN_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_HIST_MAXBIN_THRS_Lable, 7, 3, 1, 1)

        self.Swan01_MIPI_RATE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_MIPI_RATE_ComboBox.addItem("")
        self.Swan01_MIPI_RATE_ComboBox.addItem("")
        self.Swan01_MIPI_RATE_ComboBox.addItem("")
        self.Swan01_MIPI_RATE_ComboBox.addItem("")
        self.Swan01_MIPI_RATE_ComboBox.setObjectName(u"Swan01_MIPI_RATE_ComboBox")
        self.Swan01_MIPI_RATE_ComboBox.setMaximumSize(QSize(150, 16777215))
        self.Swan01_MIPI_RATE_ComboBox.setFont(font1)

        self.gridLayout_4.addWidget(self.Swan01_MIPI_RATE_ComboBox, 1, 4, 1, 1)

        self.Swan01_OUT_INTF_HIST_SEL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_INTF_HIST_SEL_ComboBox.addItem("")
        self.Swan01_OUT_INTF_HIST_SEL_ComboBox.addItem("")
        self.Swan01_OUT_INTF_HIST_SEL_ComboBox.setObjectName(u"Swan01_OUT_INTF_HIST_SEL_ComboBox")
        self.Swan01_OUT_INTF_HIST_SEL_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_OUT_INTF_HIST_SEL_ComboBox, 16, 4, 1, 1)

        self.Swan01_HIST_MAXBIN_THRS_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setObjectName(u"Swan01_HIST_MAXBIN_THRS_spinBox")
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setEnabled(True)
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setMinimumSize(QSize(150, 0))
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setMaximumSize(QSize(150, 16777215))
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setMinimum(1)
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setMaximum(255)
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setValue(1)

        self.gridLayout_4.addWidget(self.Swan01_HIST_MAXBIN_THRS_spinBox, 7, 4, 1, 1)

        self.Swan01_OUT_FIR_RAW_SEL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_FIR_RAW_SEL_ComboBox.addItem("")
        self.Swan01_OUT_FIR_RAW_SEL_ComboBox.addItem("")
        self.Swan01_OUT_FIR_RAW_SEL_ComboBox.setObjectName(u"Swan01_OUT_FIR_RAW_SEL_ComboBox")
        self.Swan01_OUT_FIR_RAW_SEL_ComboBox.setMaximumSize(QSize(165, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_OUT_FIR_RAW_SEL_ComboBox, 16, 1, 1, 1)

        self.Swan01_BIN_WIDTH_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_BIN_WIDTH_MODE_ComboBox.addItem("")
        self.Swan01_BIN_WIDTH_MODE_ComboBox.addItem("")
        self.Swan01_BIN_WIDTH_MODE_ComboBox.setObjectName(u"Swan01_BIN_WIDTH_MODE_ComboBox")
        self.Swan01_BIN_WIDTH_MODE_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_BIN_WIDTH_MODE_ComboBox, 11, 4, 1, 1)

        self.Swan01_SPOT_MON_MINBIN_THRS_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setObjectName(u"Swan01_SPOT_MON_MINBIN_THRS_Lable")
        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setMinimumSize(QSize(145, 0))
        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setFont(font3)
        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setStyleSheet(u"font: 8pt \"Microsoft YaHei UI\";")
        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_SPOT_MON_MINBIN_THRS_Lable, 9, 3, 1, 1)

        self.Swan01_OUT_ECHOBIN_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHOBIN_MODE_ComboBox.addItem("")
        self.Swan01_OUT_ECHOBIN_MODE_ComboBox.addItem("")
        self.Swan01_OUT_ECHOBIN_MODE_ComboBox.setObjectName(u"Swan01_OUT_ECHOBIN_MODE_ComboBox")
        self.Swan01_OUT_ECHOBIN_MODE_ComboBox.setMaximumSize(QSize(165, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHOBIN_MODE_ComboBox, 17, 1, 1, 1)

        self.Swan01_TRG_I_EN_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_TRG_I_EN_Label.setObjectName(u"Swan01_TRG_I_EN_Label")
        self.Swan01_TRG_I_EN_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_TRG_I_EN_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_TRG_I_EN_Label.setFont(font)
        self.Swan01_TRG_I_EN_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_TRG_I_EN_Label, 4, 0, 1, 1)

        self.Swan01_OUT_ECHO_NUM_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHO_NUM_Lable.setObjectName(u"Swan01_OUT_ECHO_NUM_Lable")
        self.Swan01_OUT_ECHO_NUM_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_OUT_ECHO_NUM_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_OUT_ECHO_NUM_Lable.setFont(font)
        self.Swan01_OUT_ECHO_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHO_NUM_Lable, 15, 0, 1, 1)

        self.Swan01_HIST_MINBIN_THRS_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_HIST_MINBIN_THRS_spinBox.setObjectName(u"Swan01_HIST_MINBIN_THRS_spinBox")
        self.Swan01_HIST_MINBIN_THRS_spinBox.setEnabled(True)
        self.Swan01_HIST_MINBIN_THRS_spinBox.setMinimumSize(QSize(150, 0))
        self.Swan01_HIST_MINBIN_THRS_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_HIST_MINBIN_THRS_spinBox.setMinimum(0)
        self.Swan01_HIST_MINBIN_THRS_spinBox.setMaximum(255)
        self.Swan01_HIST_MINBIN_THRS_spinBox.setValue(0)

        self.gridLayout_4.addWidget(self.Swan01_HIST_MINBIN_THRS_spinBox, 7, 1, 1, 1)

        self.Swan01_BIN_WIDTH_MODE_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_BIN_WIDTH_MODE_Lable.setObjectName(u"Swan01_BIN_WIDTH_MODE_Lable")
        self.Swan01_BIN_WIDTH_MODE_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_BIN_WIDTH_MODE_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_BIN_WIDTH_MODE_Lable.setFont(font)
        self.Swan01_BIN_WIDTH_MODE_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_BIN_WIDTH_MODE_Lable, 11, 3, 1, 1)

        self.Swan01_DATA_WIDTH_SEL_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_DATA_WIDTH_SEL_Label.setObjectName(u"Swan01_DATA_WIDTH_SEL_Label")
        self.Swan01_DATA_WIDTH_SEL_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_DATA_WIDTH_SEL_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_DATA_WIDTH_SEL_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_DATA_WIDTH_SEL_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_DATA_WIDTH_SEL_Label, 22, 0, 1, 1)

        self.Swan01_DATA_WIDTH_SEL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_DATA_WIDTH_SEL_ComboBox.addItem("")
        self.Swan01_DATA_WIDTH_SEL_ComboBox.addItem("")
        self.Swan01_DATA_WIDTH_SEL_ComboBox.setObjectName(u"Swan01_DATA_WIDTH_SEL_ComboBox")
        self.Swan01_DATA_WIDTH_SEL_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_DATA_WIDTH_SEL_ComboBox, 22, 1, 1, 1)

        self.Swan01_FWHM_SEARCH_NUM_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setObjectName(u"Swan01_FWHM_SEARCH_NUM_spinBox")
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setMinimumSize(QSize(0, 0))
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setMaximumSize(QSize(150, 16777215))
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setMinimum(2)
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setMaximum(15)
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setSingleStep(1)
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setValue(2)

        self.gridLayout_4.addWidget(self.Swan01_FWHM_SEARCH_NUM_spinBox, 18, 4, 1, 1)

        self.Swan01_OUT_NUMBIN_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_NUMBIN_MODE_ComboBox.addItem("")
        self.Swan01_OUT_NUMBIN_MODE_ComboBox.addItem("")
        self.Swan01_OUT_NUMBIN_MODE_ComboBox.setObjectName(u"Swan01_OUT_NUMBIN_MODE_ComboBox")
        self.Swan01_OUT_NUMBIN_MODE_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_OUT_NUMBIN_MODE_ComboBox, 13, 1, 1, 1)

        self.Swan01_FRM_SLOT_NUM_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_FRM_SLOT_NUM_Label.setObjectName(u"Swan01_FRM_SLOT_NUM_Label")
        self.Swan01_FRM_SLOT_NUM_Label.setMinimumSize(QSize(150, 0))
        self.Swan01_FRM_SLOT_NUM_Label.setMaximumSize(QSize(150, 16777215))
        self.Swan01_FRM_SLOT_NUM_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_FRM_SLOT_NUM_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_FRM_SLOT_NUM_Label, 3, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_25, 1, 2, 1, 1)

        self.Swan01_BIN_WIDTH_SEL_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_BIN_WIDTH_SEL_Lable.setObjectName(u"Swan01_BIN_WIDTH_SEL_Lable")
        self.Swan01_BIN_WIDTH_SEL_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_BIN_WIDTH_SEL_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_BIN_WIDTH_SEL_Lable.setFont(font)
        self.Swan01_BIN_WIDTH_SEL_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_BIN_WIDTH_SEL_Lable, 11, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_30, 1, 6, 1, 1)

        self.Swan01_OUT_OVFL_FLAT_EN_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_OVFL_FLAT_EN_Lable.setObjectName(u"Swan01_OUT_OVFL_FLAT_EN_Lable")
        self.Swan01_OUT_OVFL_FLAT_EN_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_OUT_OVFL_FLAT_EN_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_OUT_OVFL_FLAT_EN_Lable.setFont(font)
        self.Swan01_OUT_OVFL_FLAT_EN_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_OVFL_FLAT_EN_Lable, 17, 3, 1, 1)

        self.Swan01_PXL_PACK_SEL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.addItem("")
        self.Swan01_PXL_PACK_SEL_ComboBox.setObjectName(u"Swan01_PXL_PACK_SEL_ComboBox")
        self.Swan01_PXL_PACK_SEL_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_PXL_PACK_SEL_ComboBox, 23, 4, 1, 1)

        self.Swan01_OUT_NUMBIN_MODE_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_NUMBIN_MODE_Lable.setObjectName(u"Swan01_OUT_NUMBIN_MODE_Lable")
        self.Swan01_OUT_NUMBIN_MODE_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_OUT_NUMBIN_MODE_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_OUT_NUMBIN_MODE_Lable.setFont(font)
        self.Swan01_OUT_NUMBIN_MODE_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_NUMBIN_MODE_Lable, 13, 0, 1, 1)

        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox.addItem("")
        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox.addItem("")
        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox.setObjectName(u"Swan01_OUT_OVFL_FLAT_EN_ComboBox")
        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_OUT_OVFL_FLAT_EN_ComboBox, 17, 4, 1, 1)

        self.Swan01_PKT_CHKSUM_EN_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_PKT_CHKSUM_EN_Label.setObjectName(u"Swan01_PKT_CHKSUM_EN_Label")
        self.Swan01_PKT_CHKSUM_EN_Label.setMinimumSize(QSize(150, 0))
        self.Swan01_PKT_CHKSUM_EN_Label.setMaximumSize(QSize(150, 16777215))
        self.Swan01_PKT_CHKSUM_EN_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_PKT_CHKSUM_EN_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_PKT_CHKSUM_EN_Label, 22, 3, 1, 1)

        self.Swan01_WORK_MODE_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_WORK_MODE_Label.setObjectName(u"Swan01_WORK_MODE_Label")
        sizePolicy.setHeightForWidth(self.Swan01_WORK_MODE_Label.sizePolicy().hasHeightForWidth())
        self.Swan01_WORK_MODE_Label.setSizePolicy(sizePolicy)
        self.Swan01_WORK_MODE_Label.setMinimumSize(QSize(125, 0))
        self.Swan01_WORK_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_WORK_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_WORK_MODE_Label.setFrameShadow(QFrame.Shadow.Raised)
        self.Swan01_WORK_MODE_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_WORK_MODE_Label, 1, 0, 1, 1)

        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setObjectName(u"Swan01_ECHO_ORDER_NEAR_NUM_Lable")
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setMinimumSize(QSize(145, 0))
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setMaximumSize(QSize(145, 16777215))
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setFont(font3)
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setStyleSheet(u"font: 8pt \"Microsoft YaHei UI\";")
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_ECHO_ORDER_NEAR_NUM_Lable, 19, 0, 1, 1)

        self.Swan01_XCLK_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_XCLK_Label.setObjectName(u"Swan01_XCLK_Label")
        self.Swan01_XCLK_Label.setMinimumSize(QSize(125, 0))
        self.Swan01_XCLK_Label.setFont(font)
        self.Swan01_XCLK_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_XCLK_Label, 0, 0, 1, 1)

        self.Swan01_FRM_SLOT_NUM_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_FRM_SLOT_NUM_spinBox.setObjectName(u"Swan01_FRM_SLOT_NUM_spinBox")
        self.Swan01_FRM_SLOT_NUM_spinBox.setEnabled(True)
        self.Swan01_FRM_SLOT_NUM_spinBox.setMinimumSize(QSize(150, 0))
        self.Swan01_FRM_SLOT_NUM_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_FRM_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_FRM_SLOT_NUM_spinBox.setMaximum(65536)
        self.Swan01_FRM_SLOT_NUM_spinBox.setValue(1)

        self.gridLayout_4.addWidget(self.Swan01_FRM_SLOT_NUM_spinBox, 3, 1, 1, 1)

        self.Swan01_ANGLE_GRP_SW_NUM_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP_SW_NUM_spinBox")
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setEnabled(True)
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setMinimumSize(QSize(150, 0))
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setMaximum(8)
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setValue(1)

        self.gridLayout_4.addWidget(self.Swan01_ANGLE_GRP_SW_NUM_spinBox, 5, 1, 1, 1)

        self.Swan01_HIST_BINFULL_THRS_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_HIST_BINFULL_THRS_spinBox.setObjectName(u"Swan01_HIST_BINFULL_THRS_spinBox")
        self.Swan01_HIST_BINFULL_THRS_spinBox.setEnabled(True)
        self.Swan01_HIST_BINFULL_THRS_spinBox.setMinimumSize(QSize(150, 0))
        self.Swan01_HIST_BINFULL_THRS_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_HIST_BINFULL_THRS_spinBox.setMinimum(0)
        self.Swan01_HIST_BINFULL_THRS_spinBox.setMaximum(1023)
        self.Swan01_HIST_BINFULL_THRS_spinBox.setValue(0)

        self.gridLayout_4.addWidget(self.Swan01_HIST_BINFULL_THRS_spinBox, 9, 1, 1, 1)

        self.Swan01_TX_FRM_MODE_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_TX_FRM_MODE_Label.setObjectName(u"Swan01_TX_FRM_MODE_Label")
        self.Swan01_TX_FRM_MODE_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_TX_FRM_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_TX_FRM_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_TX_FRM_MODE_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_TX_FRM_MODE_Label, 21, 0, 1, 1)

        self.line_1 = QFrame(self.Swan01_RegisterConfig_2)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_1.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_4.addWidget(self.line_1, 6, 0, 1, 5)

        self.Swan01_HIST_MINBIN_THRS_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_HIST_MINBIN_THRS_Lable.setObjectName(u"Swan01_HIST_MINBIN_THRS_Lable")
        self.Swan01_HIST_MINBIN_THRS_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_HIST_MINBIN_THRS_Lable.setMaximumSize(QSize(145, 16777215))
        self.Swan01_HIST_MINBIN_THRS_Lable.setFont(font)
        self.Swan01_HIST_MINBIN_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_HIST_MINBIN_THRS_Lable, 7, 0, 1, 1)

        self.Swan01_ONE_DT_MODE_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_ONE_DT_MODE_ComboBox.addItem("")
        self.Swan01_ONE_DT_MODE_ComboBox.addItem("")
        self.Swan01_ONE_DT_MODE_ComboBox.setObjectName(u"Swan01_ONE_DT_MODE_ComboBox")
        self.Swan01_ONE_DT_MODE_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_ONE_DT_MODE_ComboBox, 21, 4, 1, 1)

        self.Swan01_PXL_PACK_SEL_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_PXL_PACK_SEL_Label.setObjectName(u"Swan01_PXL_PACK_SEL_Label")
        self.Swan01_PXL_PACK_SEL_Label.setMinimumSize(QSize(150, 0))
        self.Swan01_PXL_PACK_SEL_Label.setMaximumSize(QSize(150, 16777215))
        self.Swan01_PXL_PACK_SEL_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_PXL_PACK_SEL_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_PXL_PACK_SEL_Label, 23, 3, 1, 1)

        self.Swan01_FWHM_SEARCH_NUM_Value = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_FWHM_SEARCH_NUM_Value.setObjectName(u"Swan01_FWHM_SEARCH_NUM_Value")
        self.Swan01_FWHM_SEARCH_NUM_Value.setMinimumSize(QSize(28, 25))
        self.Swan01_FWHM_SEARCH_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.Swan01_FWHM_SEARCH_NUM_Value.setFont(font1)
        self.Swan01_FWHM_SEARCH_NUM_Value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_FWHM_SEARCH_NUM_Value.setWordWrap(True)
        self.Swan01_FWHM_SEARCH_NUM_Value.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_FWHM_SEARCH_NUM_Value, 18, 5, 1, 1)

        self.Swan01_OUT_ECHOBIN_NUM_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setObjectName(u"Swan01_OUT_ECHOBIN_NUM_spinBox")
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setMinimumSize(QSize(0, 0))
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setMaximumSize(QSize(150, 16777215))
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setMinimum(1)
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setMaximum(127)
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setSingleStep(1)
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setValue(20)

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHOBIN_NUM_spinBox, 15, 4, 1, 1)

        self.Swan01_ONE_DT_MODE_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_ONE_DT_MODE_Label.setObjectName(u"Swan01_ONE_DT_MODE_Label")
        self.Swan01_ONE_DT_MODE_Label.setMinimumSize(QSize(150, 0))
        self.Swan01_ONE_DT_MODE_Label.setMaximumSize(QSize(150, 16777215))
        self.Swan01_ONE_DT_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_ONE_DT_MODE_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_ONE_DT_MODE_Label, 21, 3, 1, 1)

        self.Swan01_MIPI_RATE_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_MIPI_RATE_Label.setObjectName(u"Swan01_MIPI_RATE_Label")
        sizePolicy.setHeightForWidth(self.Swan01_MIPI_RATE_Label.sizePolicy().hasHeightForWidth())
        self.Swan01_MIPI_RATE_Label.setSizePolicy(sizePolicy)
        self.Swan01_MIPI_RATE_Label.setMinimumSize(QSize(145, 0))
        self.Swan01_MIPI_RATE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_MIPI_RATE_Label.setFont(font1)
        self.Swan01_MIPI_RATE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_MIPI_RATE_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.Swan01_MIPI_RATE_Label, 1, 3, 1, 1)

        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setObjectName(u"Swan01_SPOT_MON_MINBIN_THRS_spinBox")
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setEnabled(True)
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setMinimumSize(QSize(0, 0))
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setMaximumSize(QSize(150, 16777215))
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setMinimum(0)
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setMaximum(255)
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setValue(0)

        self.gridLayout_4.addWidget(self.Swan01_SPOT_MON_MINBIN_THRS_spinBox, 9, 4, 1, 1)

        self.Swan01_SEG_NUM_Value = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_SEG_NUM_Value.setObjectName(u"Swan01_SEG_NUM_Value")
        self.Swan01_SEG_NUM_Value.setMinimumSize(QSize(28, 25))
        self.Swan01_SEG_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.Swan01_SEG_NUM_Value.setFont(font1)
        self.Swan01_SEG_NUM_Value.setTextFormat(Qt.TextFormat.MarkdownText)
        self.Swan01_SEG_NUM_Value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_SEG_NUM_Value.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_SEG_NUM_Value, 3, 5, 1, 1)

        self.Swan01_PKT_CHKSUM_EN_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_PKT_CHKSUM_EN_ComboBox.addItem("")
        self.Swan01_PKT_CHKSUM_EN_ComboBox.addItem("")
        self.Swan01_PKT_CHKSUM_EN_ComboBox.setObjectName(u"Swan01_PKT_CHKSUM_EN_ComboBox")
        self.Swan01_PKT_CHKSUM_EN_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_PKT_CHKSUM_EN_ComboBox, 22, 4, 1, 1)

        self.Swan01_FLEX_SHOT_EN_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_FLEX_SHOT_EN_Label.setObjectName(u"Swan01_FLEX_SHOT_EN_Label")
        self.Swan01_FLEX_SHOT_EN_Label.setMinimumSize(QSize(150, 0))
        self.Swan01_FLEX_SHOT_EN_Label.setMaximumSize(QSize(150, 16777215))
        self.Swan01_FLEX_SHOT_EN_Label.setFont(font)
        self.Swan01_FLEX_SHOT_EN_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_FLEX_SHOT_EN_Label, 4, 3, 1, 1)

        self.Swan01_OUT_TOTALBIN_NUM_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setObjectName(u"Swan01_OUT_TOTALBIN_NUM_spinBox")
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setMinimumSize(QSize(0, 0))
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setMaximumSize(QSize(150, 16777215))
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setMinimum(1)
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setMaximum(255)
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setValue(100)

        self.gridLayout_4.addWidget(self.Swan01_OUT_TOTALBIN_NUM_spinBox, 13, 4, 1, 1)

        self.Swan01_FWHM_HALF_COEF_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_FWHM_HALF_COEF_spinBox.setObjectName(u"Swan01_FWHM_HALF_COEF_spinBox")
        self.Swan01_FWHM_HALF_COEF_spinBox.setMinimumSize(QSize(0, 0))
        self.Swan01_FWHM_HALF_COEF_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_FWHM_HALF_COEF_spinBox.setMinimum(0)
        self.Swan01_FWHM_HALF_COEF_spinBox.setMaximum(15)
        self.Swan01_FWHM_HALF_COEF_spinBox.setSingleStep(1)
        self.Swan01_FWHM_HALF_COEF_spinBox.setValue(0)
        self.Swan01_FWHM_HALF_COEF_spinBox.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.Swan01_FWHM_HALF_COEF_spinBox, 18, 1, 1, 1)

        self.Swan01_OUT_TOTALBIN_NUM_Value = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_TOTALBIN_NUM_Value.setObjectName(u"Swan01_OUT_TOTALBIN_NUM_Value")
        self.Swan01_OUT_TOTALBIN_NUM_Value.setMinimumSize(QSize(28, 25))
        self.Swan01_OUT_TOTALBIN_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.Swan01_OUT_TOTALBIN_NUM_Value.setFont(font1)
        self.Swan01_OUT_TOTALBIN_NUM_Value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_OUT_TOTALBIN_NUM_Value.setWordWrap(True)
        self.Swan01_OUT_TOTALBIN_NUM_Value.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_OUT_TOTALBIN_NUM_Value, 13, 5, 1, 1)

        self.Swan01_SYS_CLK_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_SYS_CLK_ComboBox.addItem("")
        self.Swan01_SYS_CLK_ComboBox.addItem("")
        self.Swan01_SYS_CLK_ComboBox.setObjectName(u"Swan01_SYS_CLK_ComboBox")
        self.Swan01_SYS_CLK_ComboBox.setEnabled(True)
        self.Swan01_SYS_CLK_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_SYS_CLK_ComboBox.setMaximumSize(QSize(165, 16777215))
        self.Swan01_SYS_CLK_ComboBox.setFont(font1)
        self.Swan01_SYS_CLK_ComboBox.setEditable(False)

        self.gridLayout_4.addWidget(self.Swan01_SYS_CLK_ComboBox, 0, 4, 1, 1)

        self.Swan01_NS_MINBIN_THRS_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_NS_MINBIN_THRS_Lable.setObjectName(u"Swan01_NS_MINBIN_THRS_Lable")
        self.Swan01_NS_MINBIN_THRS_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_NS_MINBIN_THRS_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_NS_MINBIN_THRS_Lable.setFont(font)
        self.Swan01_NS_MINBIN_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_NS_MINBIN_THRS_Lable, 8, 0, 1, 1)

        self.Swan01_OUT_ECHOBIN_MODE_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHOBIN_MODE_Lable.setObjectName(u"Swan01_OUT_ECHOBIN_MODE_Lable")
        self.Swan01_OUT_ECHOBIN_MODE_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_OUT_ECHOBIN_MODE_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_OUT_ECHOBIN_MODE_Lable.setFont(font)
        self.Swan01_OUT_ECHOBIN_MODE_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHOBIN_MODE_Lable, 17, 0, 1, 1)

        self.Swan01_INTF_DET_EN_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_INTF_DET_EN_Lable.setObjectName(u"Swan01_INTF_DET_EN_Lable")
        self.Swan01_INTF_DET_EN_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_INTF_DET_EN_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_INTF_DET_EN_Lable.setFont(font)
        self.Swan01_INTF_DET_EN_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_INTF_DET_EN_Lable, 10, 0, 1, 1)

        self.Swan01_SYS_CLK_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_SYS_CLK_Label.setObjectName(u"Swan01_SYS_CLK_Label")
        self.Swan01_SYS_CLK_Label.setMinimumSize(QSize(145, 0))
        self.Swan01_SYS_CLK_Label.setMaximumSize(QSize(145, 16777215))
        self.Swan01_SYS_CLK_Label.setFont(font)
        self.Swan01_SYS_CLK_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_SYS_CLK_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.Swan01_SYS_CLK_Label, 0, 3, 1, 1)

        self.Swan01_WORK_MODE_ComboBox = ComboCheckBox(self.Swan01_RegisterConfig_2)
        self.Swan01_WORK_MODE_ComboBox.addItem("")
        self.Swan01_WORK_MODE_ComboBox.addItem("")
        self.Swan01_WORK_MODE_ComboBox.addItem("")
        self.Swan01_WORK_MODE_ComboBox.addItem("")
        self.Swan01_WORK_MODE_ComboBox.setObjectName(u"Swan01_WORK_MODE_ComboBox")
        self.Swan01_WORK_MODE_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_WORK_MODE_ComboBox.setFont(font1)

        self.gridLayout_4.addWidget(self.Swan01_WORK_MODE_ComboBox, 1, 1, 1, 1)

        self.Swan01_HIST_BINFULL_THRS_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_HIST_BINFULL_THRS_Lable.setObjectName(u"Swan01_HIST_BINFULL_THRS_Lable")
        self.Swan01_HIST_BINFULL_THRS_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_HIST_BINFULL_THRS_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_HIST_BINFULL_THRS_Lable.setFont(font)
        self.Swan01_HIST_BINFULL_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_HIST_BINFULL_THRS_Lable, 9, 0, 1, 1)

        self.Swan01_SEG_NUM_Slider = QSlider(self.Swan01_RegisterConfig_2)
        self.Swan01_SEG_NUM_Slider.setObjectName(u"Swan01_SEG_NUM_Slider")
        self.Swan01_SEG_NUM_Slider.setMinimum(1)
        self.Swan01_SEG_NUM_Slider.setMaximum(16)
        self.Swan01_SEG_NUM_Slider.setPageStep(1)
        self.Swan01_SEG_NUM_Slider.setValue(16)
        self.Swan01_SEG_NUM_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.Swan01_SEG_NUM_Slider, 3, 4, 1, 1)

        self.Swan01_BIN_NUMBER_Value = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_BIN_NUMBER_Value.setObjectName(u"Swan01_BIN_NUMBER_Value")
        self.Swan01_BIN_NUMBER_Value.setMinimumSize(QSize(28, 25))
        self.Swan01_BIN_NUMBER_Value.setMaximumSize(QSize(20, 16777215))
        self.Swan01_BIN_NUMBER_Value.setFont(font1)
        self.Swan01_BIN_NUMBER_Value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_BIN_NUMBER_Value.setWordWrap(True)
        self.Swan01_BIN_NUMBER_Value.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_BIN_NUMBER_Value, 7, 5, 1, 1)

        self.Swan01_FWHM_HALF_COEF_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_FWHM_HALF_COEF_Lable.setObjectName(u"Swan01_FWHM_HALF_COEF_Lable")
        self.Swan01_FWHM_HALF_COEF_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_FWHM_HALF_COEF_Lable.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_FWHM_HALF_COEF_Lable.setFont(font)
        self.Swan01_FWHM_HALF_COEF_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_FWHM_HALF_COEF_Lable, 18, 0, 1, 1)

        self.Swan01_NS_MINBIN_THRS_spinBox = QSpinBox(self.Swan01_RegisterConfig_2)
        self.Swan01_NS_MINBIN_THRS_spinBox.setObjectName(u"Swan01_NS_MINBIN_THRS_spinBox")
        self.Swan01_NS_MINBIN_THRS_spinBox.setEnabled(True)
        self.Swan01_NS_MINBIN_THRS_spinBox.setMinimumSize(QSize(150, 0))
        self.Swan01_NS_MINBIN_THRS_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_NS_MINBIN_THRS_spinBox.setMinimum(0)
        self.Swan01_NS_MINBIN_THRS_spinBox.setMaximum(255)
        self.Swan01_NS_MINBIN_THRS_spinBox.setValue(0)

        self.gridLayout_4.addWidget(self.Swan01_NS_MINBIN_THRS_spinBox, 8, 1, 1, 1)

        self.Swan01_INTF_HIST_MODE_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_INTF_HIST_MODE_Lable.setObjectName(u"Swan01_INTF_HIST_MODE_Lable")
        self.Swan01_INTF_HIST_MODE_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_INTF_HIST_MODE_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_INTF_HIST_MODE_Lable.setFont(font)
        self.Swan01_INTF_HIST_MODE_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_INTF_HIST_MODE_Lable, 10, 3, 1, 1)

        self.Swan01_SPOT_MON_MINBIN_THRS_Value = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setObjectName(u"Swan01_SPOT_MON_MINBIN_THRS_Value")
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setMinimumSize(QSize(28, 25))
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setMaximumSize(QSize(20, 16777215))
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setFont(font1)
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setWordWrap(True)
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_SPOT_MON_MINBIN_THRS_Value, 9, 5, 1, 1)

        self.line_2 = QFrame(self.Swan01_RegisterConfig_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_4.addWidget(self.line_2, 12, 0, 1, 5)

        self.line_3 = QFrame(self.Swan01_RegisterConfig_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_4.addWidget(self.line_3, 20, 0, 1, 5)

        self.Swan01_OUT_ECHOBIN_NUM_Value = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHOBIN_NUM_Value.setObjectName(u"Swan01_OUT_ECHOBIN_NUM_Value")
        self.Swan01_OUT_ECHOBIN_NUM_Value.setMinimumSize(QSize(28, 25))
        self.Swan01_OUT_ECHOBIN_NUM_Value.setMaximumSize(QSize(20, 16777215))
        self.Swan01_OUT_ECHOBIN_NUM_Value.setFont(font1)
        self.Swan01_OUT_ECHOBIN_NUM_Value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_OUT_ECHOBIN_NUM_Value.setWordWrap(True)
        self.Swan01_OUT_ECHOBIN_NUM_Value.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHOBIN_NUM_Value, 15, 5, 1, 1)

        self.Swan01_TRG_I_EN_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_TRG_I_EN_ComboBox.addItem("")
        self.Swan01_TRG_I_EN_ComboBox.addItem("")
        self.Swan01_TRG_I_EN_ComboBox.setObjectName(u"Swan01_TRG_I_EN_ComboBox")
        self.Swan01_TRG_I_EN_ComboBox.setMinimumSize(QSize(165, 0))
        self.Swan01_TRG_I_EN_ComboBox.setMaximumSize(QSize(165, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_TRG_I_EN_ComboBox, 4, 1, 1, 1)

        self.Swan01_MST_MODE_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_MST_MODE_Label.setObjectName(u"Swan01_MST_MODE_Label")
        self.Swan01_MST_MODE_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_MST_MODE_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_MST_MODE_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_MST_MODE_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_MST_MODE_Label, 2, 0, 1, 1)

        self.Swan01_OUT_INTF_HIST_SEL_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_INTF_HIST_SEL_Lable.setObjectName(u"Swan01_OUT_INTF_HIST_SEL_Lable")
        self.Swan01_OUT_INTF_HIST_SEL_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_OUT_INTF_HIST_SEL_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_OUT_INTF_HIST_SEL_Lable.setFont(font)
        self.Swan01_OUT_INTF_HIST_SEL_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_INTF_HIST_SEL_Lable, 16, 3, 1, 1)

        self.Swan01_BIN_WIDTH_SEL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_BIN_WIDTH_SEL_ComboBox.addItem("")
        self.Swan01_BIN_WIDTH_SEL_ComboBox.addItem("")
        self.Swan01_BIN_WIDTH_SEL_ComboBox.setObjectName(u"Swan01_BIN_WIDTH_SEL_ComboBox")
        self.Swan01_BIN_WIDTH_SEL_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_BIN_WIDTH_SEL_ComboBox, 11, 1, 1, 1)

        self.Swan01_XCLK_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_XCLK_ComboBox.addItem("")
        self.Swan01_XCLK_ComboBox.addItem("")
        self.Swan01_XCLK_ComboBox.setObjectName(u"Swan01_XCLK_ComboBox")
        self.Swan01_XCLK_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_XCLK_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_XCLK_ComboBox.setFont(font1)

        self.gridLayout_4.addWidget(self.Swan01_XCLK_ComboBox, 0, 1, 1, 1)

        self.Swan01_SYNC_POL_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_SYNC_POL_Label.setObjectName(u"Swan01_SYNC_POL_Label")
        self.Swan01_SYNC_POL_Label.setMinimumSize(QSize(150, 0))
        self.Swan01_SYNC_POL_Label.setMaximumSize(QSize(150, 16777215))
        self.Swan01_SYNC_POL_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_SYNC_POL_Label.setMargin(0)

        self.gridLayout_4.addWidget(self.Swan01_SYNC_POL_Label, 2, 3, 1, 1)

        self.Swan01_OUT_ECHOBIN_NUM_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_OUT_ECHOBIN_NUM_Lable.setObjectName(u"Swan01_OUT_ECHOBIN_NUM_Lable")
        self.Swan01_OUT_ECHOBIN_NUM_Lable.setMinimumSize(QSize(150, 0))
        self.Swan01_OUT_ECHOBIN_NUM_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_OUT_ECHOBIN_NUM_Lable.setFont(font)
        self.Swan01_OUT_ECHOBIN_NUM_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_OUT_ECHOBIN_NUM_Lable, 15, 3, 1, 1)

        self.Swan01_PXL_BINN_SEL_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_PXL_BINN_SEL_ComboBox.addItem("")
        self.Swan01_PXL_BINN_SEL_ComboBox.addItem("")
        self.Swan01_PXL_BINN_SEL_ComboBox.addItem("")
        self.Swan01_PXL_BINN_SEL_ComboBox.addItem("")
        self.Swan01_PXL_BINN_SEL_ComboBox.setObjectName(u"Swan01_PXL_BINN_SEL_ComboBox")
        self.Swan01_PXL_BINN_SEL_ComboBox.setMinimumSize(QSize(0, 0))
        self.Swan01_PXL_BINN_SEL_ComboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_PXL_BINN_SEL_ComboBox, 23, 1, 1, 1)

        self.Swan01_FLEX_SHOT_EN_ComboBox = QComboBox(self.Swan01_RegisterConfig_2)
        self.Swan01_FLEX_SHOT_EN_ComboBox.addItem("")
        self.Swan01_FLEX_SHOT_EN_ComboBox.addItem("")
        self.Swan01_FLEX_SHOT_EN_ComboBox.setObjectName(u"Swan01_FLEX_SHOT_EN_ComboBox")
        self.Swan01_FLEX_SHOT_EN_ComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.Swan01_FLEX_SHOT_EN_ComboBox, 4, 4, 1, 1)

        self.Swan01_SEG_NUM_Label = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_SEG_NUM_Label.setObjectName(u"Swan01_SEG_NUM_Label")
        self.Swan01_SEG_NUM_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_SEG_NUM_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_SEG_NUM_Label.setFont(font1)
        self.Swan01_SEG_NUM_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_SEG_NUM_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.Swan01_SEG_NUM_Label, 3, 3, 1, 1)

        self.Swan01_NS_MAXBIN_THRS_groupBox = QGroupBox(self.Swan01_RegisterConfig_2)
        self.Swan01_NS_MAXBIN_THRS_groupBox.setObjectName(u"Swan01_NS_MAXBIN_THRS_groupBox")
        self.Swan01_NS_MAXBIN_THRS_groupBox.setMinimumSize(QSize(150, 0))
        self.Swan01_NS_MAXBIN_THRS_groupBox.setMaximumSize(QSize(150, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.Swan01_NS_MAXBIN_THRS_groupBox)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Swan01_NS_MAXBIN_THRS_spinBox = QSpinBox(self.Swan01_NS_MAXBIN_THRS_groupBox)
        self.Swan01_NS_MAXBIN_THRS_spinBox.setObjectName(u"Swan01_NS_MAXBIN_THRS_spinBox")
        self.Swan01_NS_MAXBIN_THRS_spinBox.setEnabled(False)
        self.Swan01_NS_MAXBIN_THRS_spinBox.setMinimumSize(QSize(80, 0))
        self.Swan01_NS_MAXBIN_THRS_spinBox.setMaximumSize(QSize(50, 16777215))
        self.Swan01_NS_MAXBIN_THRS_spinBox.setMinimum(1)
        self.Swan01_NS_MAXBIN_THRS_spinBox.setMaximum(255)
        self.Swan01_NS_MAXBIN_THRS_spinBox.setValue(1)

        self.horizontalLayout_27.addWidget(self.Swan01_NS_MAXBIN_THRS_spinBox)

        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox = QSpinBox(self.Swan01_NS_MAXBIN_THRS_groupBox)
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setObjectName(u"Swan01_NS_CAL_SEG_NUM_SET_spinBox")
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setEnabled(True)
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setMinimumSize(QSize(50, 0))
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setMaximumSize(QSize(50, 16777215))
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setMinimum(1)
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setMaximum(8)
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setValue(1)

        self.horizontalLayout_27.addWidget(self.Swan01_NS_CAL_SEG_NUM_SET_spinBox)


        self.gridLayout_4.addWidget(self.Swan01_NS_MAXBIN_THRS_groupBox, 8, 4, 1, 1)

        self.Swan01_NS_MAXBIN_THRS_Lable = QLabel(self.Swan01_RegisterConfig_2)
        self.Swan01_NS_MAXBIN_THRS_Lable.setObjectName(u"Swan01_NS_MAXBIN_THRS_Lable")
        self.Swan01_NS_MAXBIN_THRS_Lable.setMinimumSize(QSize(0, 0))
        self.Swan01_NS_MAXBIN_THRS_Lable.setMaximumSize(QSize(150, 16777215))
        self.Swan01_NS_MAXBIN_THRS_Lable.setFont(font)
        self.Swan01_NS_MAXBIN_THRS_Lable.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_4.addWidget(self.Swan01_NS_MAXBIN_THRS_Lable, 8, 3, 1, 1)

        self.Swan01_ANGLE_GRP_SLOT_NUM = QGroupBox(self.Swan01_RegisterConfig_2)
        self.Swan01_ANGLE_GRP_SLOT_NUM.setObjectName(u"Swan01_ANGLE_GRP_SLOT_NUM")
        self.Swan01_ANGLE_GRP_SLOT_NUM.setStyleSheet(u"")
        self.horizontalLayout_26 = QHBoxLayout(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.horizontalLayout_26.setSpacing(2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP0_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox)

        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP1_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox)

        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP2_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox)

        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP3_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_31)

        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP4_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox)

        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP5_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox)

        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP6_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox)

        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox = QSpinBox(self.Swan01_ANGLE_GRP_SLOT_NUM)
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setObjectName(u"Swan01_ANGLE_GRP7_SLOT_NUM_spinBox")
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setMinimumSize(QSize(35, 0))
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setMaximumSize(QSize(35, 16777215))
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setMinimum(1)
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setMaximum(256)
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setValue(255)

        self.horizontalLayout_26.addWidget(self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox)


        self.gridLayout_4.addWidget(self.Swan01_ANGLE_GRP_SLOT_NUM, 5, 3, 1, 2)

        self.Swan01_RegisterConfig_1.setWidget(self.Swan01_RegisterConfig_2)

        self.verticalLayout_19.addWidget(self.Swan01_RegisterConfig_1)


        self.horizontalLayout_23.addWidget(self.Swan01_RegisterConfig)

        self.horizontalSpacer_23 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)

        self.Swan01_ROIConfigGroup = QGroupBox(self.Swan01_ScriptConfig)
        self.Swan01_ROIConfigGroup.setObjectName(u"Swan01_ROIConfigGroup")
        self.Swan01_ROIConfigGroup.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.Swan01_ROIConfigGroup)
        self.verticalLayout_14.setSpacing(9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 6, 3, 0)
        self.Swan01_ROIConfig = QTabWidget(self.Swan01_ROIConfigGroup)
        self.Swan01_ROIConfig.setObjectName(u"Swan01_ROIConfig")
        self.Swan01_ROIConfig.setMinimumSize(QSize(0, 0))
        self.Swan01_ROIConfig.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_ROIConfig.setFont(font1)
        self.Swan01_ROIConfig.setStyleSheet(u"")
        self.Swan01_ROIConfig.setIconSize(QSize(0, 0))
        self.Swan01_Config1byGUI = QWidget()
        self.Swan01_Config1byGUI.setObjectName(u"Swan01_Config1byGUI")
        self.verticalLayout_15 = QVBoxLayout(self.Swan01_Config1byGUI)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 9, -1, 0)
        self.scrollArea_4 = QScrollArea(self.Swan01_Config1byGUI)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette2.setBrush(QPalette.Active, QPalette.Link, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Link, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Link, brush)
        self.scrollArea_4.setPalette(palette2)
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 243, 510))
        self.formLayout_9 = QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setHorizontalSpacing(10)
        self.formLayout_9.setVerticalSpacing(6)
        self.formLayout_9.setContentsMargins(0, 0, 20, 0)
        self.Swan01_seg_hs_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_seg_hs_Label.setObjectName(u"Swan01_seg_hs_Label")
        self.Swan01_seg_hs_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_seg_hs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_seg_hs_Label.setFont(font1)
        self.Swan01_seg_hs_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_seg_hs_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.Swan01_seg_hs_Label)

        self.Swan01_seg_hs_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_5)
        self.Swan01_seg_hs_spinBox.setObjectName(u"Swan01_seg_hs_spinBox")
        self.Swan01_seg_hs_spinBox.setMinimum(1)
        self.Swan01_seg_hs_spinBox.setMaximum(16)
        self.Swan01_seg_hs_spinBox.setValue(1)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.Swan01_seg_hs_spinBox)

        self.Swan01_h_seg_shift_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_h_seg_shift_Label.setObjectName(u"Swan01_h_seg_shift_Label")
        self.Swan01_h_seg_shift_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_h_seg_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_h_seg_shift_Label.setFont(font1)
        self.Swan01_h_seg_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_h_seg_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.Swan01_h_seg_shift_Label)

        self.Swan01_h_seg_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_5)
        self.Swan01_h_seg_shift_spinBox.setObjectName(u"Swan01_h_seg_shift_spinBox")
        self.Swan01_h_seg_shift_spinBox.setMinimum(0)
        self.Swan01_h_seg_shift_spinBox.setMaximum(15)

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.Swan01_h_seg_shift_spinBox)

        self.Swan01_spad_vs_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_spad_vs_Label.setObjectName(u"Swan01_spad_vs_Label")
        self.Swan01_spad_vs_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_spad_vs_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_spad_vs_Label.setFont(font1)
        self.Swan01_spad_vs_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_spad_vs_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.Swan01_spad_vs_Label)

        self.Swan01_spad_vs_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_5)
        self.Swan01_spad_vs_spinBox.setObjectName(u"Swan01_spad_vs_spinBox")
        self.Swan01_spad_vs_spinBox.setMinimum(1)
        self.Swan01_spad_vs_spinBox.setMaximum(576)

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.Swan01_spad_vs_spinBox)

        self.Swan01_light_shift_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_light_shift_Label.setObjectName(u"Swan01_light_shift_Label")
        self.Swan01_light_shift_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_light_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_light_shift_Label.setFont(font1)
        self.Swan01_light_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_light_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.Swan01_light_shift_Label)

        self.Swan01_light_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_5)
        self.Swan01_light_shift_spinBox.setObjectName(u"Swan01_light_shift_spinBox")
        self.Swan01_light_shift_spinBox.setMinimum(-576)
        self.Swan01_light_shift_spinBox.setMaximum(576)

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.Swan01_light_shift_spinBox)

        self.Swan01_sublight_group_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_sublight_group_Label.setObjectName(u"Swan01_sublight_group_Label")
        self.Swan01_sublight_group_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_sublight_group_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_sublight_group_Label.setFont(font1)
        self.Swan01_sublight_group_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_sublight_group_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(4, QFormLayout.LabelRole, self.Swan01_sublight_group_Label)

        self.Swan01_sublight_group_LineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.Swan01_sublight_group_LineEdit.setObjectName(u"Swan01_sublight_group_LineEdit")
        self.Swan01_sublight_group_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Swan01_sublight_group_LineEdit.sizePolicy().hasHeightForWidth())
        self.Swan01_sublight_group_LineEdit.setSizePolicy(sizePolicy1)
        self.Swan01_sublight_group_LineEdit.setMinimumSize(QSize(0, 0))
        self.Swan01_sublight_group_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Swan01_sublight_group_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Swan01_sublight_group_LineEdit.setReadOnly(False)

        self.formLayout_9.setWidget(4, QFormLayout.FieldRole, self.Swan01_sublight_group_LineEdit)

        self.Swan01_sublight_shift_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_sublight_shift_Label.setObjectName(u"Swan01_sublight_shift_Label")
        self.Swan01_sublight_shift_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_sublight_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_sublight_shift_Label.setFont(font1)
        self.Swan01_sublight_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_sublight_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(5, QFormLayout.LabelRole, self.Swan01_sublight_shift_Label)

        self.Swan01_sublight_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_5)
        self.Swan01_sublight_shift_spinBox.setObjectName(u"Swan01_sublight_shift_spinBox")
        self.Swan01_sublight_shift_spinBox.setMinimum(-576)
        self.Swan01_sublight_shift_spinBox.setMaximum(576)

        self.formLayout_9.setWidget(5, QFormLayout.FieldRole, self.Swan01_sublight_shift_spinBox)

        self.Swan01_ROI_Shape_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_ROI_Shape_Label.setObjectName(u"Swan01_ROI_Shape_Label")
        self.Swan01_ROI_Shape_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_ROI_Shape_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_ROI_Shape_Label.setFont(font1)
        self.Swan01_ROI_Shape_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_ROI_Shape_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(6, QFormLayout.LabelRole, self.Swan01_ROI_Shape_Label)

        self.Swan01_ROI_Shape_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_5)
        self.Swan01_ROI_Shape_ComboBox.addItem("")
        self.Swan01_ROI_Shape_ComboBox.addItem("")
        self.Swan01_ROI_Shape_ComboBox.setObjectName(u"Swan01_ROI_Shape_ComboBox")
        self.Swan01_ROI_Shape_ComboBox.setFont(font1)

        self.formLayout_9.setWidget(6, QFormLayout.FieldRole, self.Swan01_ROI_Shape_ComboBox)

        self.Swan01_ROI_Retrace_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_ROI_Retrace_Label.setObjectName(u"Swan01_ROI_Retrace_Label")
        self.Swan01_ROI_Retrace_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_ROI_Retrace_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_ROI_Retrace_Label.setFont(font1)
        self.Swan01_ROI_Retrace_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_ROI_Retrace_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(7, QFormLayout.LabelRole, self.Swan01_ROI_Retrace_Label)

        self.Swan01_ROI_Retrace_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_5)
        self.Swan01_ROI_Retrace_ComboBox.addItem("")
        self.Swan01_ROI_Retrace_ComboBox.addItem("")
        self.Swan01_ROI_Retrace_ComboBox.setObjectName(u"Swan01_ROI_Retrace_ComboBox")
        self.Swan01_ROI_Retrace_ComboBox.setFont(font1)

        self.formLayout_9.setWidget(7, QFormLayout.FieldRole, self.Swan01_ROI_Retrace_ComboBox)

        self.Swan01_v_spad_shift_Label = QLabel(self.scrollAreaWidgetContents_5)
        self.Swan01_v_spad_shift_Label.setObjectName(u"Swan01_v_spad_shift_Label")
        self.Swan01_v_spad_shift_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_v_spad_shift_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_v_spad_shift_Label.setFont(font1)
        self.Swan01_v_spad_shift_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_v_spad_shift_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_9.setWidget(8, QFormLayout.LabelRole, self.Swan01_v_spad_shift_Label)

        self.Swan01_v_spad_shift_spinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_5)
        self.Swan01_v_spad_shift_spinBox.setObjectName(u"Swan01_v_spad_shift_spinBox")
        self.Swan01_v_spad_shift_spinBox.setMinimum(-576)
        self.Swan01_v_spad_shift_spinBox.setMaximum(576)

        self.formLayout_9.setWidget(8, QFormLayout.FieldRole, self.Swan01_v_spad_shift_spinBox)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_15.addWidget(self.scrollArea_4)

        self.Swan01_ROIConfig.addTab(self.Swan01_Config1byGUI, "")
        self.Swan01_Config2byCOOR = QWidget()
        self.Swan01_Config2byCOOR.setObjectName(u"Swan01_Config2byCOOR")
        self.verticalLayout_16 = QVBoxLayout(self.Swan01_Config2byCOOR)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, 9, 0)
        self.scrollArea_6 = QScrollArea(self.Swan01_Config2byCOOR)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u"")
        self.scrollArea_6.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_6.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 263, 498))
        self.formLayout_10 = QFormLayout(self.scrollAreaWidgetContents_7)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(10)
        self.formLayout_10.setVerticalSpacing(6)
        self.formLayout_10.setContentsMargins(0, 0, 20, 0)
        self.Swan01_Cali_File_Load_Label = QLabel(self.scrollAreaWidgetContents_7)
        self.Swan01_Cali_File_Load_Label.setObjectName(u"Swan01_Cali_File_Load_Label")
        self.Swan01_Cali_File_Load_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_Cali_File_Load_Label.setFont(font1)
        self.Swan01_Cali_File_Load_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_Cali_File_Load_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.Swan01_Cali_File_Load_Label)

        self.Swan01_Cali_File_Load_Layout = QHBoxLayout()
        self.Swan01_Cali_File_Load_Layout.setSpacing(9)
        self.Swan01_Cali_File_Load_Layout.setObjectName(u"Swan01_Cali_File_Load_Layout")
        self.Swan01_Cali_File_Load_LineEdit = QLineEdit(self.scrollAreaWidgetContents_7)
        self.Swan01_Cali_File_Load_LineEdit.setObjectName(u"Swan01_Cali_File_Load_LineEdit")
        self.Swan01_Cali_File_Load_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Swan01_Cali_File_Load_LineEdit.sizePolicy().hasHeightForWidth())
        self.Swan01_Cali_File_Load_LineEdit.setSizePolicy(sizePolicy1)
        self.Swan01_Cali_File_Load_LineEdit.setMinimumSize(QSize(0, 0))
        self.Swan01_Cali_File_Load_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Swan01_Cali_File_Load_LineEdit.setReadOnly(True)

        self.Swan01_Cali_File_Load_Layout.addWidget(self.Swan01_Cali_File_Load_LineEdit)

        self.Swan01_Cali_File_Load_Button = QPushButton(self.scrollAreaWidgetContents_7)
        self.Swan01_Cali_File_Load_Button.setObjectName(u"Swan01_Cali_File_Load_Button")
        sizePolicy2.setHeightForWidth(self.Swan01_Cali_File_Load_Button.sizePolicy().hasHeightForWidth())
        self.Swan01_Cali_File_Load_Button.setSizePolicy(sizePolicy2)
        self.Swan01_Cali_File_Load_Button.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.Swan01_Cali_File_Load_Layout.addWidget(self.Swan01_Cali_File_Load_Button)


        self.formLayout_10.setLayout(0, QFormLayout.FieldRole, self.Swan01_Cali_File_Load_Layout)

        self.Swan01_Excel_Sheet_sel_Label = QLabel(self.scrollAreaWidgetContents_7)
        self.Swan01_Excel_Sheet_sel_Label.setObjectName(u"Swan01_Excel_Sheet_sel_Label")
        self.Swan01_Excel_Sheet_sel_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_Excel_Sheet_sel_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_Excel_Sheet_sel_Label.setFont(font1)
        self.Swan01_Excel_Sheet_sel_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_Excel_Sheet_sel_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.Swan01_Excel_Sheet_sel_Label)

        self.Swan01_Excel_Sheet_sel_spinBox = QSpinBox(self.scrollAreaWidgetContents_7)
        self.Swan01_Excel_Sheet_sel_spinBox.setObjectName(u"Swan01_Excel_Sheet_sel_spinBox")
        self.Swan01_Excel_Sheet_sel_spinBox.setMinimum(1)
        self.Swan01_Excel_Sheet_sel_spinBox.setMaximum(100)
        self.Swan01_Excel_Sheet_sel_spinBox.setValue(1)

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.Swan01_Excel_Sheet_sel_spinBox)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_16.addWidget(self.scrollArea_6)

        self.Swan01_ROIConfig.addTab(self.Swan01_Config2byCOOR, "")
        self.Swan01_Config3ROIEdit = QWidget()
        self.Swan01_Config3ROIEdit.setObjectName(u"Swan01_Config3ROIEdit")
        self.verticalLayout_17 = QVBoxLayout(self.Swan01_Config3ROIEdit)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.scrollArea_7 = QScrollArea(self.Swan01_Config3ROIEdit)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"")
        self.scrollArea_7.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_7.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 263, 498))
        self.formLayout_11 = QFormLayout(self.scrollAreaWidgetContents_8)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setHorizontalSpacing(10)
        self.formLayout_11.setVerticalSpacing(6)
        self.formLayout_11.setContentsMargins(0, 0, 20, 0)
        self.Swan01_ROI_File_Label = QLabel(self.scrollAreaWidgetContents_8)
        self.Swan01_ROI_File_Label.setObjectName(u"Swan01_ROI_File_Label")
        self.Swan01_ROI_File_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_ROI_File_Label.setFont(font1)
        self.Swan01_ROI_File_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.Swan01_ROI_File_Label)

        self.Swan01_ROI_File_Layout = QHBoxLayout()
        self.Swan01_ROI_File_Layout.setSpacing(9)
        self.Swan01_ROI_File_Layout.setObjectName(u"Swan01_ROI_File_Layout")
        self.Swan01_ROI_File_LineEdit = QLineEdit(self.scrollAreaWidgetContents_8)
        self.Swan01_ROI_File_LineEdit.setObjectName(u"Swan01_ROI_File_LineEdit")
        self.Swan01_ROI_File_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Swan01_ROI_File_LineEdit.sizePolicy().hasHeightForWidth())
        self.Swan01_ROI_File_LineEdit.setSizePolicy(sizePolicy1)
        self.Swan01_ROI_File_LineEdit.setMinimumSize(QSize(0, 0))
        self.Swan01_ROI_File_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Swan01_ROI_File_LineEdit.setReadOnly(True)

        self.Swan01_ROI_File_Layout.addWidget(self.Swan01_ROI_File_LineEdit)

        self.Swan01_ROI_File_Button = QPushButton(self.scrollAreaWidgetContents_8)
        self.Swan01_ROI_File_Button.setObjectName(u"Swan01_ROI_File_Button")
        sizePolicy2.setHeightForWidth(self.Swan01_ROI_File_Button.sizePolicy().hasHeightForWidth())
        self.Swan01_ROI_File_Button.setSizePolicy(sizePolicy2)
        self.Swan01_ROI_File_Button.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.Swan01_ROI_File_Layout.addWidget(self.Swan01_ROI_File_Button)


        self.formLayout_11.setLayout(0, QFormLayout.FieldRole, self.Swan01_ROI_File_Layout)

        self.Swan01_Start_Rolling_Label = QLabel(self.scrollAreaWidgetContents_8)
        self.Swan01_Start_Rolling_Label.setObjectName(u"Swan01_Start_Rolling_Label")
        self.Swan01_Start_Rolling_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_Start_Rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_Start_Rolling_Label.setFont(font1)
        self.Swan01_Start_Rolling_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_Start_Rolling_Label.setFrameShadow(QFrame.Shadow.Raised)
        self.Swan01_Start_Rolling_Label.setTextFormat(Qt.TextFormat.PlainText)

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.Swan01_Start_Rolling_Label)

        self.Swan01_End_Rolling_Label = QLabel(self.scrollAreaWidgetContents_8)
        self.Swan01_End_Rolling_Label.setObjectName(u"Swan01_End_Rolling_Label")
        self.Swan01_End_Rolling_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_End_Rolling_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_End_Rolling_Label.setFont(font1)
        self.Swan01_End_Rolling_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Swan01_End_Rolling_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_11.setWidget(2, QFormLayout.LabelRole, self.Swan01_End_Rolling_Label)

        self.Swan01_End_Rolling_SpinBox = QSpinBox(self.scrollAreaWidgetContents_8)
        self.Swan01_End_Rolling_SpinBox.setObjectName(u"Swan01_End_Rolling_SpinBox")
        self.Swan01_End_Rolling_SpinBox.setMinimum(1)
        self.Swan01_End_Rolling_SpinBox.setMaximum(32)

        self.formLayout_11.setWidget(2, QFormLayout.FieldRole, self.Swan01_End_Rolling_SpinBox)

        self.Swan01_Start_Rolling_SpinBox = QSpinBox(self.scrollAreaWidgetContents_8)
        self.Swan01_Start_Rolling_SpinBox.setObjectName(u"Swan01_Start_Rolling_SpinBox")
        self.Swan01_Start_Rolling_SpinBox.setMinimum(1)
        self.Swan01_Start_Rolling_SpinBox.setMaximum(32)

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.Swan01_Start_Rolling_SpinBox)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_17.addWidget(self.scrollArea_7)

        self.Swan01_ROIConfig.addTab(self.Swan01_Config3ROIEdit, "")
        self.Swan01_Config4ROICali = QWidget()
        self.Swan01_Config4ROICali.setObjectName(u"Swan01_Config4ROICali")
        self.verticalLayout_18 = QVBoxLayout(self.Swan01_Config4ROICali)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea_8 = QScrollArea(self.Swan01_Config4ROICali)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u"")
        self.scrollArea_8.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_8.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 280, 489))
        self.formLayout_12 = QFormLayout(self.scrollAreaWidgetContents_9)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setHorizontalSpacing(10)
        self.formLayout_12.setVerticalSpacing(6)
        self.formLayout_12.setContentsMargins(0, 0, 20, 0)
        self.Swan01_cali_file_path_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_file_path_Label.setObjectName(u"Swan01_cali_file_path_Label")
        self.Swan01_cali_file_path_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_cali_file_path_Label.setFont(font1)
        self.Swan01_cali_file_path_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.Swan01_cali_file_path_Label)

        self.Swan01_cali_file_path_Layout = QHBoxLayout()
        self.Swan01_cali_file_path_Layout.setSpacing(9)
        self.Swan01_cali_file_path_Layout.setObjectName(u"Swan01_cali_file_path_Layout")
        self.Swan01_cali_file_path_LineEdit = QLineEdit(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_file_path_LineEdit.setObjectName(u"Swan01_cali_file_path_LineEdit")
        self.Swan01_cali_file_path_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Swan01_cali_file_path_LineEdit.sizePolicy().hasHeightForWidth())
        self.Swan01_cali_file_path_LineEdit.setSizePolicy(sizePolicy1)
        self.Swan01_cali_file_path_LineEdit.setMinimumSize(QSize(0, 0))
        self.Swan01_cali_file_path_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Swan01_cali_file_path_LineEdit.setReadOnly(True)

        self.Swan01_cali_file_path_Layout.addWidget(self.Swan01_cali_file_path_LineEdit)

        self.Swan01_cali_file_path_Button = QPushButton(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_file_path_Button.setObjectName(u"Swan01_cali_file_path_Button")
        sizePolicy2.setHeightForWidth(self.Swan01_cali_file_path_Button.sizePolicy().hasHeightForWidth())
        self.Swan01_cali_file_path_Button.setSizePolicy(sizePolicy2)
        self.Swan01_cali_file_path_Button.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.Swan01_cali_file_path_Layout.addWidget(self.Swan01_cali_file_path_Button)


        self.formLayout_12.setLayout(0, QFormLayout.FieldRole, self.Swan01_cali_file_path_Layout)

        self.Swan01_img_mirror_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_img_mirror_Label.setObjectName(u"Swan01_img_mirror_Label")
        self.Swan01_img_mirror_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_img_mirror_Label.setFont(font1)
        self.Swan01_img_mirror_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.Swan01_img_mirror_Label)

        self.Swan01_img_mirror_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_9)
        self.Swan01_img_mirror_ComboBox.addItem("")
        self.Swan01_img_mirror_ComboBox.addItem("")
        self.Swan01_img_mirror_ComboBox.addItem("")
        self.Swan01_img_mirror_ComboBox.addItem("")
        self.Swan01_img_mirror_ComboBox.setObjectName(u"Swan01_img_mirror_ComboBox")
        self.Swan01_img_mirror_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_img_mirror_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_img_mirror_ComboBox.setFont(font1)

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.Swan01_img_mirror_ComboBox)

        self.Swan01_remove_noise_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_remove_noise_Label.setObjectName(u"Swan01_remove_noise_Label")
        self.Swan01_remove_noise_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_remove_noise_Label.setFont(font1)
        self.Swan01_remove_noise_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(2, QFormLayout.LabelRole, self.Swan01_remove_noise_Label)

        self.Swan01_remove_noise_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_9)
        self.Swan01_remove_noise_ComboBox.addItem("")
        self.Swan01_remove_noise_ComboBox.addItem("")
        self.Swan01_remove_noise_ComboBox.setObjectName(u"Swan01_remove_noise_ComboBox")
        self.Swan01_remove_noise_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_remove_noise_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_remove_noise_ComboBox.setFont(font1)

        self.formLayout_12.setWidget(2, QFormLayout.FieldRole, self.Swan01_remove_noise_ComboBox)

        self.Swan01_light_smooth_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_light_smooth_Label.setObjectName(u"Swan01_light_smooth_Label")
        self.Swan01_light_smooth_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_light_smooth_Label.setFont(font1)
        self.Swan01_light_smooth_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(3, QFormLayout.LabelRole, self.Swan01_light_smooth_Label)

        self.Swan01_light_smooth_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_9)
        self.Swan01_light_smooth_ComboBox.addItem("")
        self.Swan01_light_smooth_ComboBox.addItem("")
        self.Swan01_light_smooth_ComboBox.setObjectName(u"Swan01_light_smooth_ComboBox")
        self.Swan01_light_smooth_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_light_smooth_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_light_smooth_ComboBox.setFont(font1)

        self.formLayout_12.setWidget(3, QFormLayout.FieldRole, self.Swan01_light_smooth_ComboBox)

        self.Swan01_curvature_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_curvature_Label.setObjectName(u"Swan01_curvature_Label")
        self.Swan01_curvature_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_curvature_Label.setFont(font1)
        self.Swan01_curvature_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(4, QFormLayout.LabelRole, self.Swan01_curvature_Label)

        self.Swan01_curvature_SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_9)
        self.Swan01_curvature_SpinBox.setObjectName(u"Swan01_curvature_SpinBox")
        self.Swan01_curvature_SpinBox.setMinimum(0)
        self.Swan01_curvature_SpinBox.setMaximum(1000)
        self.Swan01_curvature_SpinBox.setValue(2)

        self.formLayout_12.setWidget(4, QFormLayout.FieldRole, self.Swan01_curvature_SpinBox)

        self.Swan01_correct_thres_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_correct_thres_Label.setObjectName(u"Swan01_correct_thres_Label")
        self.Swan01_correct_thres_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_correct_thres_Label.setFont(font1)
        self.Swan01_correct_thres_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(5, QFormLayout.LabelRole, self.Swan01_correct_thres_Label)

        self.Swan01_correct_thres_SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_9)
        self.Swan01_correct_thres_SpinBox.setObjectName(u"Swan01_correct_thres_SpinBox")
        self.Swan01_correct_thres_SpinBox.setMinimum(0)
        self.Swan01_correct_thres_SpinBox.setMaximum(100)
        self.Swan01_correct_thres_SpinBox.setValue(1)

        self.formLayout_12.setWidget(5, QFormLayout.FieldRole, self.Swan01_correct_thres_SpinBox)

        self.Swan01_cali_order_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_order_Label.setObjectName(u"Swan01_cali_order_Label")
        self.Swan01_cali_order_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_cali_order_Label.setFont(font1)
        self.Swan01_cali_order_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(6, QFormLayout.LabelRole, self.Swan01_cali_order_Label)

        self.Swan01_cali_order_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_order_ComboBox.addItem("")
        self.Swan01_cali_order_ComboBox.addItem("")
        self.Swan01_cali_order_ComboBox.setObjectName(u"Swan01_cali_order_ComboBox")
        self.Swan01_cali_order_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_cali_order_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_cali_order_ComboBox.setFont(font1)

        self.formLayout_12.setWidget(6, QFormLayout.FieldRole, self.Swan01_cali_order_ComboBox)

        self.Swan01_cali_frm_num_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_frm_num_Label.setObjectName(u"Swan01_cali_frm_num_Label")
        self.Swan01_cali_frm_num_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_cali_frm_num_Label.setFont(font1)
        self.Swan01_cali_frm_num_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(7, QFormLayout.LabelRole, self.Swan01_cali_frm_num_Label)

        self.Swan01_cali_frm_num__SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_9)
        self.Swan01_cali_frm_num__SpinBox.setObjectName(u"Swan01_cali_frm_num__SpinBox")
        self.Swan01_cali_frm_num__SpinBox.setMinimum(1)
        self.Swan01_cali_frm_num__SpinBox.setMaximum(10000)

        self.formLayout_12.setWidget(7, QFormLayout.FieldRole, self.Swan01_cali_frm_num__SpinBox)

        self.Swan01_ref_segment_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_ref_segment_Label.setObjectName(u"Swan01_ref_segment_Label")
        self.Swan01_ref_segment_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_ref_segment_Label.setFont(font1)
        self.Swan01_ref_segment_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(8, QFormLayout.LabelRole, self.Swan01_ref_segment_Label)

        self.Swan01_ref_segment_SpinBox = NoWheelSpinBox(self.scrollAreaWidgetContents_9)
        self.Swan01_ref_segment_SpinBox.setObjectName(u"Swan01_ref_segment_SpinBox")
        self.Swan01_ref_segment_SpinBox.setMinimum(0)
        self.Swan01_ref_segment_SpinBox.setMaximum(16)
        self.Swan01_ref_segment_SpinBox.setValue(0)

        self.formLayout_12.setWidget(8, QFormLayout.FieldRole, self.Swan01_ref_segment_SpinBox)

        self.Swan01_mode_2D_Label = QLabel(self.scrollAreaWidgetContents_9)
        self.Swan01_mode_2D_Label.setObjectName(u"Swan01_mode_2D_Label")
        self.Swan01_mode_2D_Label.setMinimumSize(QSize(100, 0))
        self.Swan01_mode_2D_Label.setFont(font1)
        self.Swan01_mode_2D_Label.setFrameShape(QFrame.Shape.StyledPanel)

        self.formLayout_12.setWidget(9, QFormLayout.LabelRole, self.Swan01_mode_2D_Label)

        self.Swan01_mode_2D_ComboBox = NoWheelComboBox(self.scrollAreaWidgetContents_9)
        self.Swan01_mode_2D_ComboBox.addItem("")
        self.Swan01_mode_2D_ComboBox.addItem("")
        self.Swan01_mode_2D_ComboBox.setObjectName(u"Swan01_mode_2D_ComboBox")
        self.Swan01_mode_2D_ComboBox.setMinimumSize(QSize(150, 0))
        self.Swan01_mode_2D_ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_mode_2D_ComboBox.setFont(font1)

        self.formLayout_12.setWidget(9, QFormLayout.FieldRole, self.Swan01_mode_2D_ComboBox)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_18.addWidget(self.scrollArea_8)

        self.Swan01_ROIConfig.addTab(self.Swan01_Config4ROICali, "")

        self.verticalLayout_14.addWidget(self.Swan01_ROIConfig)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(3, 0, 3, 3)
        self.Swan01_ROIZoneConfig = QLabel(self.Swan01_ROIConfigGroup)
        self.Swan01_ROIZoneConfig.setObjectName(u"Swan01_ROIZoneConfig")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Link, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Link, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Link, brush1)
        self.Swan01_ROIZoneConfig.setPalette(palette3)
        self.Swan01_ROIZoneConfig.setFont(font2)
        self.Swan01_ROIZoneConfig.setStyleSheet(u"QLabel {\n"
"font: 700 9pt \"Consolas\";\n"
"}")
        self.Swan01_ROIZoneConfig.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Swan01_ROIZoneConfig.setMargin(0)
        self.Swan01_ROIZoneConfig.setOpenExternalLinks(False)

        self.horizontalLayout_24.addWidget(self.Swan01_ROIZoneConfig)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_26)

        self.Swan01_ROIView = QPushButton(self.Swan01_ROIConfigGroup)
        self.Swan01_ROIView.setObjectName(u"Swan01_ROIView")
        self.Swan01_ROIView.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_24.addWidget(self.Swan01_ROIView)

        self.Swan01_ROISave = QPushButton(self.Swan01_ROIConfigGroup)
        self.Swan01_ROISave.setObjectName(u"Swan01_ROISave")
        self.Swan01_ROISave.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_24.addWidget(self.Swan01_ROISave)


        self.verticalLayout_14.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_23.addWidget(self.Swan01_ROIConfigGroup)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_27)


        self.verticalLayout_13.addWidget(self.Swan01_ScriptConfig)

        self.Swan01_FileConifg = QGroupBox(self.Swan01)
        self.Swan01_FileConifg.setObjectName(u"Swan01_FileConifg")
        self.Swan01_FileConifg.setMinimumSize(QSize(300, 0))
        self.Swan01_FileConifg.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.Swan01_FileConifg)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(9, 9, 9, 1)
        self.Swan01_roi_sram_name_LineEdit = QLineEdit(self.Swan01_FileConifg)
        self.Swan01_roi_sram_name_LineEdit.setObjectName(u"Swan01_roi_sram_name_LineEdit")
        self.Swan01_roi_sram_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Swan01_roi_sram_name_LineEdit.setFont(font)

        self.gridLayout_7.addWidget(self.Swan01_roi_sram_name_LineEdit, 4, 1, 1, 1)

        self.Swan01_file_save_dir_Label = QLabel(self.Swan01_FileConifg)
        self.Swan01_file_save_dir_Label.setObjectName(u"Swan01_file_save_dir_Label")
        self.Swan01_file_save_dir_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_file_save_dir_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_file_save_dir_Label.setFont(font1)
        self.Swan01_file_save_dir_Label.setFrameShape(QFrame.Shape.NoFrame)
        self.Swan01_file_save_dir_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_7.addWidget(self.Swan01_file_save_dir_Label, 6, 0, 1, 1)

        self.Swan01_reference_script_Label = QLabel(self.Swan01_FileConifg)
        self.Swan01_reference_script_Label.setObjectName(u"Swan01_reference_script_Label")
        self.Swan01_reference_script_Label.setMinimumSize(QSize(0, 0))
        self.Swan01_reference_script_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Swan01_reference_script_Label.setFont(font1)
        self.Swan01_reference_script_Label.setFrameShape(QFrame.Shape.NoFrame)
        self.Swan01_reference_script_Label.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_7.addWidget(self.Swan01_reference_script_Label, 1, 0, 1, 1)

        self.Swan01_reference_script_parse_Button = QPushButton(self.Swan01_FileConifg)
        self.Swan01_reference_script_parse_Button.setObjectName(u"Swan01_reference_script_parse_Button")
        sizePolicy2.setHeightForWidth(self.Swan01_reference_script_parse_Button.sizePolicy().hasHeightForWidth())
        self.Swan01_reference_script_parse_Button.setSizePolicy(sizePolicy2)
        self.Swan01_reference_script_parse_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_7.addWidget(self.Swan01_reference_script_parse_Button, 1, 3, 1, 1)

        self.Swan01_roi_sram_name_CheckBox = QCheckBox(self.Swan01_FileConifg)
        self.Swan01_roi_sram_name_CheckBox.setObjectName(u"Swan01_roi_sram_name_CheckBox")

        self.gridLayout_7.addWidget(self.Swan01_roi_sram_name_CheckBox, 4, 3, 1, 1)

        self.Swan01_ButtonCollectionFrame = QFrame(self.Swan01_FileConifg)
        self.Swan01_ButtonCollectionFrame.setObjectName(u"Swan01_ButtonCollectionFrame")
        self.horizontalLayout_25 = QHBoxLayout(self.Swan01_ButtonCollectionFrame)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 2, -1, -1)
        self.Swan01_Save = QPushButton(self.Swan01_ButtonCollectionFrame)
        self.Swan01_Save.setObjectName(u"Swan01_Save")
        sizePolicy1.setHeightForWidth(self.Swan01_Save.sizePolicy().hasHeightForWidth())
        self.Swan01_Save.setSizePolicy(sizePolicy1)
        self.Swan01_Save.setMinimumSize(QSize(90, 0))
        self.Swan01_Save.setFont(font)
        self.Swan01_Save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.Swan01_Save)

        self.Swan01_Open = QPushButton(self.Swan01_ButtonCollectionFrame)
        self.Swan01_Open.setObjectName(u"Swan01_Open")
        sizePolicy1.setHeightForWidth(self.Swan01_Open.sizePolicy().hasHeightForWidth())
        self.Swan01_Open.setSizePolicy(sizePolicy1)
        self.Swan01_Open.setMinimumSize(QSize(90, 0))
        self.Swan01_Open.setFont(font)
        self.Swan01_Open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.Swan01_Open)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_29)


        self.gridLayout_7.addWidget(self.Swan01_ButtonCollectionFrame, 7, 0, 1, 5)

        self.Swan01_reg_script_name_LineEdit = QLineEdit(self.Swan01_FileConifg)
        self.Swan01_reg_script_name_LineEdit.setObjectName(u"Swan01_reg_script_name_LineEdit")
        self.Swan01_reg_script_name_LineEdit.setMinimumSize(QSize(0, 0))
        self.Swan01_reg_script_name_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Swan01_reg_script_name_LineEdit.setFont(font)

        self.gridLayout_7.addWidget(self.Swan01_reg_script_name_LineEdit, 2, 1, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(30, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_28, 4, 4, 1, 1)

        self.Swan01_roi_sram_name_Label = QLabel(self.Swan01_FileConifg)
        self.Swan01_roi_sram_name_Label.setObjectName(u"Swan01_roi_sram_name_Label")
        self.Swan01_roi_sram_name_Label.setFont(font)

        self.gridLayout_7.addWidget(self.Swan01_roi_sram_name_Label, 4, 0, 1, 1)

        self.Swan01_reference_script_LineEdit = QLineEdit(self.Swan01_FileConifg)
        self.Swan01_reference_script_LineEdit.setObjectName(u"Swan01_reference_script_LineEdit")
        self.Swan01_reference_script_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Swan01_reference_script_LineEdit.sizePolicy().hasHeightForWidth())
        self.Swan01_reference_script_LineEdit.setSizePolicy(sizePolicy1)
        self.Swan01_reference_script_LineEdit.setMinimumSize(QSize(0, 0))
        self.Swan01_reference_script_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Swan01_reference_script_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Swan01_reference_script_LineEdit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.Swan01_reference_script_LineEdit, 1, 1, 1, 1)

        self.Swan01_reference_script_sel_Button = QPushButton(self.Swan01_FileConifg)
        self.Swan01_reference_script_sel_Button.setObjectName(u"Swan01_reference_script_sel_Button")
        sizePolicy2.setHeightForWidth(self.Swan01_reference_script_sel_Button.sizePolicy().hasHeightForWidth())
        self.Swan01_reference_script_sel_Button.setSizePolicy(sizePolicy2)
        self.Swan01_reference_script_sel_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_7.addWidget(self.Swan01_reference_script_sel_Button, 1, 2, 1, 1)

        self.Swan01_file_save_dir_LineEdit = QLineEdit(self.Swan01_FileConifg)
        self.Swan01_file_save_dir_LineEdit.setObjectName(u"Swan01_file_save_dir_LineEdit")
        self.Swan01_file_save_dir_LineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Swan01_file_save_dir_LineEdit.sizePolicy().hasHeightForWidth())
        self.Swan01_file_save_dir_LineEdit.setSizePolicy(sizePolicy1)
        self.Swan01_file_save_dir_LineEdit.setMinimumSize(QSize(350, 0))
        self.Swan01_file_save_dir_LineEdit.setMaximumSize(QSize(500, 16777215))
        self.Swan01_file_save_dir_LineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Swan01_file_save_dir_LineEdit.setReadOnly(False)

        self.gridLayout_7.addWidget(self.Swan01_file_save_dir_LineEdit, 6, 1, 1, 1)

        self.Swan01_reg_script_name_Label = QLabel(self.Swan01_FileConifg)
        self.Swan01_reg_script_name_Label.setObjectName(u"Swan01_reg_script_name_Label")
        self.Swan01_reg_script_name_Label.setFont(font)

        self.gridLayout_7.addWidget(self.Swan01_reg_script_name_Label, 2, 0, 1, 1)

        self.Swan01_file_save_dir_Button = QPushButton(self.Swan01_FileConifg)
        self.Swan01_file_save_dir_Button.setObjectName(u"Swan01_file_save_dir_Button")
        sizePolicy2.setHeightForWidth(self.Swan01_file_save_dir_Button.sizePolicy().hasHeightForWidth())
        self.Swan01_file_save_dir_Button.setSizePolicy(sizePolicy2)
        self.Swan01_file_save_dir_Button.setMinimumSize(QSize(90, 0))

        self.gridLayout_7.addWidget(self.Swan01_file_save_dir_Button, 6, 2, 1, 1)

        self.Swan01_MoreConfiguration = QFrame(self.Swan01_FileConifg)
        self.Swan01_MoreConfiguration.setObjectName(u"Swan01_MoreConfiguration")
        self.Swan01_MoreConfiguration.setMinimumSize(QSize(800, 0))
        self.Swan01_MoreConfiguration.setMaximumSize(QSize(800, 16777215))
        self.Swan01_MoreConfiguration.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.Swan01_MoreConfiguration)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.Swan01_MoreConfiguration, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.Swan01_FileConifg)

        self.pages.addWidget(self.Swan01)
        self.Toolbox = QWidget()
        self.Toolbox.setObjectName(u"Toolbox")
        self.Toolbox.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.Toolbox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 0)
        self.title_label_2 = QLabel(self.Toolbox)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(16)
        self.title_label_2.setFont(font4)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

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
        self.select_group_01.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.select_group_01.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.select_group_01)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.select_Label_01 = QLabel(self.select_group_01)
        self.select_Label_01.setObjectName(u"select_Label_01")
        self.select_Label_01.setMinimumSize(QSize(100, 0))
        self.select_Label_01.setMaximumSize(QSize(100, 16777215))
        self.select_Label_01.setFont(font)
        self.select_Label_01.setFrameShape(QFrame.Shape.NoFrame)

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
        self.select_Label_02.setFrameShape(QFrame.Shape.NoFrame)

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
        self.select_Label_03.setFrameShape(QFrame.Shape.NoFrame)

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
        self.file_sel_Label_01.setFrameShape(QFrame.Shape.NoFrame)
        self.file_sel_Label_01.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.file_sel_Label_01)

        self.file_sel_LineEdit_01 = QLineEdit(self.file_group_01)
        self.file_sel_LineEdit_01.setObjectName(u"file_sel_LineEdit_01")
        self.file_sel_LineEdit_01.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_01.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_01.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_01.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_01.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
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
        self.file_sel_Label_02.setFrameShape(QFrame.Shape.NoFrame)
        self.file_sel_Label_02.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.file_sel_Label_02)

        self.file_sel_LineEdit_02 = QLineEdit(self.file_group_02)
        self.file_sel_LineEdit_02.setObjectName(u"file_sel_LineEdit_02")
        self.file_sel_LineEdit_02.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_02.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_02.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_02.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_02.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
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
        self.file_sel_Label_03.setFrameShape(QFrame.Shape.NoFrame)
        self.file_sel_Label_03.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_14.addWidget(self.file_sel_Label_03)

        self.file_sel_LineEdit_03 = QLineEdit(self.file_group_03)
        self.file_sel_LineEdit_03.setObjectName(u"file_sel_LineEdit_03")
        self.file_sel_LineEdit_03.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_03.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_03.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_03.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_03.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
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
        self.file_sel_Label_04.setFrameShape(QFrame.Shape.NoFrame)
        self.file_sel_Label_04.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.file_sel_Label_04)

        self.file_sel_LineEdit_04 = QLineEdit(self.file_group_04)
        self.file_sel_LineEdit_04.setObjectName(u"file_sel_LineEdit_04")
        self.file_sel_LineEdit_04.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.file_sel_LineEdit_04.sizePolicy().hasHeightForWidth())
        self.file_sel_LineEdit_04.setSizePolicy(sizePolicy1)
        self.file_sel_LineEdit_04.setMinimumSize(QSize(500, 0))
        self.file_sel_LineEdit_04.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
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
        self.Operate_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.general_operate_Button_04.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_04, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 0, 6, 1, 1)

        self.general_operate_Button_02 = QPushButton(self.Operate_2)
        self.general_operate_Button_02.setObjectName(u"general_operate_Button_02")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_02.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_02.setSizePolicy(sizePolicy1)
        self.general_operate_Button_02.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_02.setFont(font)
        self.general_operate_Button_02.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_02, 0, 1, 1, 1)

        self.general_operate_Button_05 = QPushButton(self.Operate_2)
        self.general_operate_Button_05.setObjectName(u"general_operate_Button_05")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_05.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_05.setSizePolicy(sizePolicy1)
        self.general_operate_Button_05.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_05.setFont(font)
        self.general_operate_Button_05.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_05, 0, 4, 1, 1)

        self.general_operate_Button_01 = QPushButton(self.Operate_2)
        self.general_operate_Button_01.setObjectName(u"general_operate_Button_01")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_01.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_01.setSizePolicy(sizePolicy1)
        self.general_operate_Button_01.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_01.setFont(font)
        self.general_operate_Button_01.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_01, 0, 0, 1, 1)

        self.general_operate_Button_03 = QPushButton(self.Operate_2)
        self.general_operate_Button_03.setObjectName(u"general_operate_Button_03")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_03.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_03.setSizePolicy(sizePolicy1)
        self.general_operate_Button_03.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_03.setFont(font)
        self.general_operate_Button_03.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.general_operate_Button_03, 0, 2, 1, 1)

        self.general_operate_Button_06 = QPushButton(self.Operate_2)
        self.general_operate_Button_06.setObjectName(u"general_operate_Button_06")
        sizePolicy1.setHeightForWidth(self.general_operate_Button_06.sizePolicy().hasHeightForWidth())
        self.general_operate_Button_06.setSizePolicy(sizePolicy1)
        self.general_operate_Button_06.setMinimumSize(QSize(90, 0))
        self.general_operate_Button_06.setFont(font)
        self.general_operate_Button_06.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 442, 293))
        self.contents.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(24)
        font5.setBold(False)
        font5.setItalic(False)
        self.title_label.setFont(font5)
        self.title_label.setStyleSheet(u"font: 24pt \"Microsoft YaHei UI\";")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

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
        self.chip_ID_Group.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chip_ID_Group.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(self.chip_ID_Group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chip_ID_Label = QLabel(self.chip_ID_Group)
        self.chip_ID_Label.setObjectName(u"chip_ID_Label")
        self.chip_ID_Label.setMinimumSize(QSize(100, 0))
        self.chip_ID_Label.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei UI"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.chip_ID_Label.setFont(font6)
        self.chip_ID_Label.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_3.addWidget(self.chip_ID_Label)

        self.chip_ID_ComboBox = QComboBox(self.chip_ID_Group)
        self.chip_ID_ComboBox.addItem("")
        self.chip_ID_ComboBox.setObjectName(u"chip_ID_ComboBox")
        self.chip_ID_ComboBox.setEnabled(False)
        self.chip_ID_ComboBox.setMinimumSize(QSize(300, 0))
        self.chip_ID_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.chip_ID_ComboBox.setFont(font6)

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
        self.themes_select_Label.setFont(font6)
        self.themes_select_Label.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_21.addWidget(self.themes_select_Label)

        self.themes_select_ComboBox = QComboBox(self.thems_select_Group)
        self.themes_select_ComboBox.addItem("")
        self.themes_select_ComboBox.addItem("")
        self.themes_select_ComboBox.setObjectName(u"themes_select_ComboBox")
        self.themes_select_ComboBox.setMinimumSize(QSize(300, 0))
        self.themes_select_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.themes_select_ComboBox.setFont(font6)

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
        self.roi_image_save_Label.setFont(font6)
        self.roi_image_save_Label.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_22.addWidget(self.roi_image_save_Label)

        self.roi_image_save_ComboBox = QComboBox(self.roi_image_save)
        self.roi_image_save_ComboBox.addItem("")
        self.roi_image_save_ComboBox.addItem("")
        self.roi_image_save_ComboBox.setObjectName(u"roi_image_save_ComboBox")
        self.roi_image_save_ComboBox.setMinimumSize(QSize(300, 0))
        self.roi_image_save_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.roi_image_save_ComboBox.setFont(font6)

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
        self.roi_data_format_Label.setFont(font6)
        self.roi_data_format_Label.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_20.addWidget(self.roi_data_format_Label)

        self.roi_data_fromat_ComboBox = QComboBox(self.roi_data_format_Group)
        self.roi_data_fromat_ComboBox.addItem("")
        self.roi_data_fromat_ComboBox.addItem("")
        self.roi_data_fromat_ComboBox.setObjectName(u"roi_data_fromat_ComboBox")
        self.roi_data_fromat_ComboBox.setMinimumSize(QSize(300, 0))
        self.roi_data_fromat_ComboBox.setMaximumSize(QSize(300, 16777215))
        self.roi_data_fromat_ComboBox.setFont(font6)

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
        self.Hawk01_V_ROLL_NUM_Slider.valueChanged.connect(self.Hawk01_V_ROLL_NUM_Value.setNum)
        self.Hawk01_H_ROLL_NUM_Slider.valueChanged.connect(self.Hawk01_H_ROLL_NUM_Value.setNum)
        self.Hawk01_H_VLD_SEG_Slider.valueChanged.connect(self.Hawk01_H_VLD_SEG_Value.setNum)
        self.Swan01_SEG_NUM_Slider.valueChanged.connect(self.Swan01_SEG_NUM_Value.setNum)

        self.pages.setCurrentIndex(1)
        self.Hawk01_ROIConfig.setCurrentIndex(0)
        self.Swan01_ROIConfig.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.Hawk01_XCLK_Label.setText(QCoreApplication.translate("MainPages", u"XCLK", None))
        self.Hawk01_XCLK_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"24 M", None))
        self.Hawk01_XCLK_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"25 M", None))

        self.Hawk01_MST_MODE_Label.setText(QCoreApplication.translate("MainPages", u"MST_MODE", None))
        self.Hawk01_MST_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Slave Mode", None))
        self.Hawk01_MST_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Master Mode", None))

        self.Hawk01_WORK_MODE_Label.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.Hawk01_WORK_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Ranging Mode", None))
        self.Hawk01_WORK_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Echo Mode", None))
        self.Hawk01_WORK_MODE_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"Histogram Mode", None))
        self.Hawk01_WORK_MODE_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"Gray Scale Mode", None))

        self.Hawk01_MIPI_RATE_Label.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
        self.Hawk01_MIPI_RATE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"0.8 Gbps/Lane", None))
        self.Hawk01_MIPI_RATE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"1.0 Gbps/Lane", None))
        self.Hawk01_MIPI_RATE_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"1.2 Gbps/Lane", None))
        self.Hawk01_MIPI_RATE_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"1.5 Gbps/Lane", None))

        self.Hawk01_MoreConfiguration.setTitle("")
        self.Hawk01_TRG_I_EN_Label.setText(QCoreApplication.translate("MainPages", u"TRG_I_EN", None))
        self.Hawk01_MINBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#if QT_CONFIG(tooltip)
        self.Hawk01_MAXBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Hawk01_MAXBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Hawk01_V_PXL_OUT_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 Pixel", None))
        self.Hawk01_V_PXL_OUT_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"6 Pixel", None))

        self.Hawk01_PKS_ECHO_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"PKS_ECHO_NUM", None))
        self.Hawk01_V_PXL_OUT_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_PXL_NUM", None))
        self.Hawk01_TDC_BIN_W_Label.setText(QCoreApplication.translate("MainPages", u"TDC bin width", None))
        self.Hawk01_BIN_NUMBER_Value.setText(QCoreApplication.translate("MainPages", u"672", None))
        self.Hawk01_OUT_BIN_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"36 Bin", None))
        self.Hawk01_OUT_BIN_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"60 Bin", None))

        self.Hawk01_TDC_BIN_W_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"0.75 ns", None))
        self.Hawk01_TDC_BIN_W_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"1.00 ns", None))
        self.Hawk01_TDC_BIN_W_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"1.25 ns", None))
        self.Hawk01_TDC_BIN_W_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"1.50 ns", None))
        self.Hawk01_TDC_BIN_W_ComboBox.setItemText(4, QCoreApplication.translate("MainPages", u"2.00 ns", None))
        self.Hawk01_TDC_BIN_W_ComboBox.setItemText(5, QCoreApplication.translate("MainPages", u"2.50 ns", None))

        self.Hawk01_MAXBIN_THRS_Lable_.setText(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#if QT_CONFIG(tooltip)
        self.Hawk01_MINBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Hawk01_MINBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Hawk01_OUT_BIN_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_BIN_NUM", None))
        self.Hawk01_PKS_ECHO_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 Echo", None))
        self.Hawk01_PKS_ECHO_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2 Echo", None))
        self.Hawk01_PKS_ECHO_NUM_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"3 Echo", None))
        self.Hawk01_PKS_ECHO_NUM_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"4 Echo", None))
        self.Hawk01_PKS_ECHO_NUM_ComboBox.setItemText(4, QCoreApplication.translate("MainPages", u"5 Echo", None))

        self.Hawk01_SYS_CLK_Label.setText(QCoreApplication.translate("MainPages", u"SYS CLK", None))
        self.Hawk01_SYS_CLK_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"200 M", None))
        self.Hawk01_SYS_CLK_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"250 M", None))
        self.Hawk01_SYS_CLK_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"330 M", None))

        self.Hawk01_TRG_I_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Disable", None))
        self.Hawk01_TRG_I_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Enable", None))

        self.Hawk01_TX_FRM_MODE_Label.setText(QCoreApplication.translate("MainPages", u"TX_FRM_MODE", None))
        self.Hawk01_TX_FRM_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Sub-frame", None))
        self.Hawk01_TX_FRM_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Imag-frame", None))

        self.Hawk01_ONE_DT_MODE_Label.setText(QCoreApplication.translate("MainPages", u"ONE_DT_MODE", None))
        self.Hawk01_ONE_DT_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Hawk01_ONE_DT_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Hawk01_SCAN_MODE_Label.setText(QCoreApplication.translate("MainPages", u"SCAN_MODE", None))
        self.Hawk01_SCAN_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1D SCAN_MODE", None))
        self.Hawk01_SCAN_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2D SCAN_MODE", None))

        self.Hawk01_V_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"V_ROLL_NUM", None))
        self.Hawk01_H_ROLL_NUM_Label.setText(QCoreApplication.translate("MainPages", u"H_ROLL_NUM", None))
        self.Hawk01_H_VLD_SEG_Label.setText(QCoreApplication.translate("MainPages", u"H_VLD_SEG", None))
        self.Hawk01_H_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Hawk01_V_ROLL_NUM_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Hawk01_H_VLD_SEG_Value.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Hawk01_seg_hs_Label.setText(QCoreApplication.translate("MainPages", u"seg_hs", None))
#if QT_CONFIG(whatsthis)
        self.Hawk01_seg_hs_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Hawk01_spad_vs_Label.setText(QCoreApplication.translate("MainPages", u"spad_vs", None))
        self.Hawk01_light_shift_Label.setText(QCoreApplication.translate("MainPages", u"light shift", None))
        self.Hawk01_sublight_shift_Label.setText(QCoreApplication.translate("MainPages", u"sublight shift", None))
        self.Hawk01_ROI_Shape_Label.setText(QCoreApplication.translate("MainPages", u"ROI shape", None))
        self.Hawk01_ROI_Shape_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Straight", None))
        self.Hawk01_ROI_Shape_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Curve", None))

        self.Hawk01_v_spad_shift_Label.setText(QCoreApplication.translate("MainPages", u"v_spad_shift", None))
        self.Hawk01_h_seg_shift_Label.setText(QCoreApplication.translate("MainPages", u"h_seg_shift", None))
        self.Hawk01_ROI_Retrace_Label.setText(QCoreApplication.translate("MainPages", u"ROI retrace", None))
        self.Hawk01_ROI_Retrace_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Hawk01_ROI_Retrace_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Hawk01_sublight_group_Label.setText(QCoreApplication.translate("MainPages", u"sublight group", None))
        self.Hawk01_sublight_group_LineEdit.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Hawk01_sublight_group_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"6\u884cpixel\u5206\u7ec4\u65b9\u5f0f", None))
        self.Hawk01_ROIConfig.setTabText(self.Hawk01_ROIConfig.indexOf(self.Hawk01_Config1byGUI), QCoreApplication.translate("MainPages", u"ROI GUI", None))
        self.Hawk01_Cali_File_Load_Label.setText(QCoreApplication.translate("MainPages", u"Cali File", None))
        self.Hawk01_Cali_File_Load_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u5750\u6807\u6587\u4ef6\uff0c\u652f\u6301 .txt, .csv, .xls, .xlsx", None))
        self.Hawk01_Cali_File_Load_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Hawk01_Excel_Sheet_sel_Label.setText(QCoreApplication.translate("MainPages", u"Sheet Sel", None))
#if QT_CONFIG(whatsthis)
        self.Hawk01_Excel_Sheet_sel_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Hawk01_ROIConfig.setTabText(self.Hawk01_ROIConfig.indexOf(self.Hawk01_Config2byCOOR), QCoreApplication.translate("MainPages", u"ROI COOR", None))
        self.Hawk01_ROI_File_Label.setText(QCoreApplication.translate("MainPages", u"ROI File", None))
        self.Hawk01_ROI_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u7f16\u8f91\u7684ROI\u6587\u4ef6", None))
        self.Hawk01_ROI_File_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Hawk01_Start_Rolling_Label.setText(QCoreApplication.translate("MainPages", u"Start Rolling", None))
        self.Hawk01_End_Rolling_Label.setText(QCoreApplication.translate("MainPages", u"End Rolling", None))
        self.Hawk01_ROIConfig.setTabText(self.Hawk01_ROIConfig.indexOf(self.Hawk01_Config3ROIEdit), QCoreApplication.translate("MainPages", u"ROI Edit", None))
        self.Hawk01_cali_file_path_Label.setText(QCoreApplication.translate("MainPages", u"Cali File", None))
        self.Hawk01_cali_file_path_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u6807\u5b9a\u7684ROI\u6587\u4ef6", None))
        self.Hawk01_cali_file_path_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Hawk01_img_mirror_Label.setText(QCoreApplication.translate("MainPages", u"Img Mirror ", None))
        self.Hawk01_img_mirror_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No mirror", None))
        self.Hawk01_img_mirror_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"X-axis mirror", None))
        self.Hawk01_img_mirror_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"Y-axis mirror", None))
        self.Hawk01_img_mirror_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"X-axis and Y-axis mirror", None))

        self.Hawk01_remove_noise_Label.setText(QCoreApplication.translate("MainPages", u"remove noise", None))
        self.Hawk01_remove_noise_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Hawk01_remove_noise_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Hawk01_light_smooth_Label.setText(QCoreApplication.translate("MainPages", u"light smooth", None))
        self.Hawk01_light_smooth_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Hawk01_light_smooth_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Hawk01_curvature_Label.setText(QCoreApplication.translate("MainPages", u"curvature", None))
        self.Hawk01_correct_thres_Label.setText(QCoreApplication.translate("MainPages", u"correct thres", None))
        self.Hawk01_cali_order_Label.setText(QCoreApplication.translate("MainPages", u"Cali Order", None))
        self.Hawk01_cali_order_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"From small to large", None))
        self.Hawk01_cali_order_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"From large to small", None))

        self.Hawk01_cali_frm_num_Label.setText(QCoreApplication.translate("MainPages", u"cali frm num", None))
        self.Hawk01_ref_segment_Label.setText(QCoreApplication.translate("MainPages", u"ref segment", None))
        self.Hawk01_mode_2D_Label.setText(QCoreApplication.translate("MainPages", u"mode 2D", None))
        self.Hawk01_mode_2D_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Light strip energy is preferred", None))
        self.Hawk01_mode_2D_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"The number of covered photons is preferred", None))

        self.Hawk01_ROIConfig.setTabText(self.Hawk01_ROIConfig.indexOf(self.Hawk01_Config4ROICali), QCoreApplication.translate("MainPages", u"ROI Cali", None))
        self.Hawk01_ROIZoneConfig.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><a href=\"https://www.example.com\"><span style=\" text-decoration: underline; color:#0078d7;\">ZONE INFO</span></a></p></body></html>", None))
        self.Hawk01_ROIView.setText(QCoreApplication.translate("MainPages", u"View", None))
        self.Hawk01_ROISave.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Hawk01_roi_sram_name_Label.setText(QCoreApplication.translate("MainPages", u"ROI SRAM Name", None))
        self.Hawk01_reg_script_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.Hawk01_file_save_dir_Label.setText(QCoreApplication.translate("MainPages", u"File Save Path", None))
        self.Hawk01_reference_script_sel_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Hawk01_roi_sram_name_CheckBox.setText(QCoreApplication.translate("MainPages", u"Include", None))
        self.Hawk01_roi_sram_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.Hawk01_reference_script_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.Hawk01_Save.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Hawk01_Open.setText(QCoreApplication.translate("MainPages", u"Open", None))
        self.Hawk01_reference_script_Label.setText(QCoreApplication.translate("MainPages", u"Reference Script", None))
        self.Hawk01_file_save_dir_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u6307\u5b9aSpadisApp\u8f6f\u4ef6\u8def\u5f84", None))
        self.Hawk01_file_save_dir_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Hawk01_reg_script_name_Label.setText(QCoreApplication.translate("MainPages", u"Reg Script Name", None))
        self.Hawk01_reference_script_parse_Button.setText(QCoreApplication.translate("MainPages", u"Parse", None))
        self.Swan01_RegisterConfig.setTitle("")
        self.Swan01_INTF_DET_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Disable", None))
        self.Swan01_INTF_DET_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Enable", None))

        self.Swan01_OUT_TOTALBIN_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_TOTALBIN_NUM", None))
        self.Swan01_SYNC_POL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Active low", None))
        self.Swan01_SYNC_POL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Active high", None))

        self.Swan01_ANGLE_GRP_SW_NUM_Label.setText(QCoreApplication.translate("MainPages", u"ANGLE_GRP_SW_NUM", None))
        self.Swan01_INTF_HIST_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Mode 0", None))
        self.Swan01_INTF_HIST_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Mode 1", None))

        self.Swan01_OUT_FIR_RAW_SEL_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_FIR_RAW_SEL", None))
        self.Swan01_MST_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Slave Mode", None))
        self.Swan01_MST_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Master Mode", None))

        self.Swan01_FWHM_SEARCH_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"FWHM_SEARCH_NUM", None))
        self.Swan01_PXL_BINN_SEL_Label.setText(QCoreApplication.translate("MainPages", u"PXL_BINN_SEL", None))
        self.Swan01_TX_FRM_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Sub-frame", None))
        self.Swan01_TX_FRM_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Imag-frame", None))

#if QT_CONFIG(tooltip)
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ECHO_ORDER_NEAR_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_OUT_ECHO_NUM_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 Echo", None))
        self.Swan01_OUT_ECHO_NUM_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2 Echo", None))
        self.Swan01_OUT_ECHO_NUM_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"3 Echo", None))
        self.Swan01_OUT_ECHO_NUM_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"4 Echo", None))
        self.Swan01_OUT_ECHO_NUM_ComboBox.setItemText(4, QCoreApplication.translate("MainPages", u"5 Echo", None))
        self.Swan01_OUT_ECHO_NUM_ComboBox.setItemText(5, QCoreApplication.translate("MainPages", u"6 Echo", None))

        self.Swan01_HIST_MAXBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"HIST_MAXBIN_THRS", None))
        self.Swan01_MIPI_RATE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"0.8 Gbps/Lane", None))
        self.Swan01_MIPI_RATE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"1.0 Gbps/Lane", None))
        self.Swan01_MIPI_RATE_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"1.2 Gbps/Lane", None))
        self.Swan01_MIPI_RATE_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"1.5 Gbps/Lane", None))

        self.Swan01_OUT_INTF_HIST_SEL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"ACCU HIST_DATA", None))
        self.Swan01_OUT_INTF_HIST_SEL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"INTF HIST_Data", None))

#if QT_CONFIG(tooltip)
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_HIST_MAXBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_OUT_FIR_RAW_SEL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Raw Histogram data", None))
        self.Swan01_OUT_FIR_RAW_SEL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"FIR Histogram data", None))

        self.Swan01_BIN_WIDTH_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Mode 0", None))
        self.Swan01_BIN_WIDTH_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Mode 1", None))

        self.Swan01_SPOT_MON_MINBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"SPOT_MON_MINBIN_THRS", None))
        self.Swan01_OUT_ECHOBIN_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Peak point to Left-right", None))
        self.Swan01_OUT_ECHOBIN_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Start point to the right", None))

        self.Swan01_TRG_I_EN_Label.setText(QCoreApplication.translate("MainPages", u"TRG_I_EN", None))
        self.Swan01_OUT_ECHO_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_ECHO_NUM", None))
#if QT_CONFIG(tooltip)
        self.Swan01_HIST_MINBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_HIST_MINBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_BIN_WIDTH_MODE_Lable.setText(QCoreApplication.translate("MainPages", u"BIN_WIDTH_MODE", None))
        self.Swan01_DATA_WIDTH_SEL_Label.setText(QCoreApplication.translate("MainPages", u"DATA_WIDTH_SEL", None))
        self.Swan01_DATA_WIDTH_SEL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"8 bit", None))
        self.Swan01_DATA_WIDTH_SEL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"10 bit", None))

#if QT_CONFIG(tooltip)
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_FWHM_SEARCH_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_OUT_NUMBIN_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Total bin number", None))
        self.Swan01_OUT_NUMBIN_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Bin number per echo", None))

        self.Swan01_FRM_SLOT_NUM_Label.setText(QCoreApplication.translate("MainPages", u"FRM_SLOT_NUM", None))
        self.Swan01_BIN_WIDTH_SEL_Lable.setText(QCoreApplication.translate("MainPages", u"BIN_WIDTH_SEL", None))
        self.Swan01_OUT_OVFL_FLAT_EN_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_OVFL_FLAT_EN", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"4 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"8 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(4, QCoreApplication.translate("MainPages", u"16 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(5, QCoreApplication.translate("MainPages", u"32 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(6, QCoreApplication.translate("MainPages", u"48 pixel pack", None))
        self.Swan01_PXL_PACK_SEL_ComboBox.setItemText(7, QCoreApplication.translate("MainPages", u"64 pixel pack", None))

        self.Swan01_OUT_NUMBIN_MODE_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_NUMBIN_MODE", None))
        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Cut-off output", None))
        self.Swan01_OUT_OVFL_FLAT_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Flat-top output", None))

        self.Swan01_PKT_CHKSUM_EN_Label.setText(QCoreApplication.translate("MainPages", u"PKT_CHKSUM_EN", None))
        self.Swan01_WORK_MODE_Label.setText(QCoreApplication.translate("MainPages", u"WORK_MODE", None))
        self.Swan01_ECHO_ORDER_NEAR_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"ECHO_ORDER_NEAR_NUM", None))
        self.Swan01_XCLK_Label.setText(QCoreApplication.translate("MainPages", u"XCLK", None))
#if QT_CONFIG(tooltip)
        self.Swan01_FRM_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_FRM_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP_SW_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_HIST_BINFULL_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_HIST_BINFULL_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_TX_FRM_MODE_Label.setText(QCoreApplication.translate("MainPages", u"TX_FRM_MODE", None))
        self.Swan01_HIST_MINBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"HIST_MINBIN_THRS", None))
        self.Swan01_ONE_DT_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Swan01_ONE_DT_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Swan01_PXL_PACK_SEL_Label.setText(QCoreApplication.translate("MainPages", u"PXL_PACK_SEL", None))
        self.Swan01_FWHM_SEARCH_NUM_Value.setText(QCoreApplication.translate("MainPages", u"6", None))
#if QT_CONFIG(tooltip)
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_OUT_ECHOBIN_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_ONE_DT_MODE_Label.setText(QCoreApplication.translate("MainPages", u"ONE_DT_MODE", None))
        self.Swan01_MIPI_RATE_Label.setText(QCoreApplication.translate("MainPages", u"MIPI RATE", None))
#if QT_CONFIG(tooltip)
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_SPOT_MON_MINBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_SEG_NUM_Value.setText(QCoreApplication.translate("MainPages", u"16", None))
        self.Swan01_PKT_CHKSUM_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Swan01_PKT_CHKSUM_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Swan01_FLEX_SHOT_EN_Label.setText(QCoreApplication.translate("MainPages", u"FLEX_SHOT_EN", None))
#if QT_CONFIG(tooltip)
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_OUT_TOTALBIN_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_FWHM_HALF_COEF_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_FWHM_HALF_COEF_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_OUT_TOTALBIN_NUM_Value.setText(QCoreApplication.translate("MainPages", u"200", None))
        self.Swan01_SYS_CLK_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"330 M", None))
        self.Swan01_SYS_CLK_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"400 M", None))

        self.Swan01_NS_MINBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"NS_MINBIN_THRS", None))
        self.Swan01_OUT_ECHOBIN_MODE_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_ECHOBIN_MODE", None))
        self.Swan01_INTF_DET_EN_Lable.setText(QCoreApplication.translate("MainPages", u"INTF_DET_EN", None))
        self.Swan01_SYS_CLK_Label.setText(QCoreApplication.translate("MainPages", u"SYS CLK", None))
        self.Swan01_WORK_MODE_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"SPHR", None))
        self.Swan01_WORK_MODE_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"PHR", None))
        self.Swan01_WORK_MODE_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"FHR", None))
        self.Swan01_WORK_MODE_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"PCM", None))

        self.Swan01_HIST_BINFULL_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"HIST_BINFULL_THRS", None))
        self.Swan01_BIN_NUMBER_Value.setText(QCoreApplication.translate("MainPages", u"2048", None))
        self.Swan01_FWHM_HALF_COEF_Lable.setText(QCoreApplication.translate("MainPages", u"FWHM_HALF_COEF", None))
#if QT_CONFIG(tooltip)
        self.Swan01_NS_MINBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_NS_MINBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_INTF_HIST_MODE_Lable.setText(QCoreApplication.translate("MainPages", u"INTF_HIST_MODE", None))
        self.Swan01_SPOT_MON_MINBIN_THRS_Value.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.Swan01_OUT_ECHOBIN_NUM_Value.setText(QCoreApplication.translate("MainPages", u"40", None))
        self.Swan01_TRG_I_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Disable", None))
        self.Swan01_TRG_I_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Enable", None))

        self.Swan01_MST_MODE_Label.setText(QCoreApplication.translate("MainPages", u"MST_MODE", None))
        self.Swan01_OUT_INTF_HIST_SEL_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_INTF_HIST_SEL", None))
        self.Swan01_BIN_WIDTH_SEL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1 ns", None))
        self.Swan01_BIN_WIDTH_SEL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2 ns", None))

        self.Swan01_XCLK_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"24 M", None))
        self.Swan01_XCLK_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"25 M", None))

        self.Swan01_SYNC_POL_Label.setText(QCoreApplication.translate("MainPages", u"SYNC_POL", None))
        self.Swan01_OUT_ECHOBIN_NUM_Lable.setText(QCoreApplication.translate("MainPages", u"OUT_ECHOBIN_NUM", None))
        self.Swan01_PXL_BINN_SEL_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No pixel binning", None))
        self.Swan01_PXL_BINN_SEL_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"2 pixel binning", None))
        self.Swan01_PXL_BINN_SEL_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"4 pixel binning", None))
        self.Swan01_PXL_BINN_SEL_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"2 pixel slide binning", None))

        self.Swan01_FLEX_SHOT_EN_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Disable", None))
        self.Swan01_FLEX_SHOT_EN_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Enable", None))

        self.Swan01_SEG_NUM_Label.setText(QCoreApplication.translate("MainPages", u"SEG_NUM", None))
        self.Swan01_NS_MAXBIN_THRS_groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.Swan01_NS_MAXBIN_THRS_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_NS_MAXBIN_THRS_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MINBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_NS_CAL_SEG_NUM_SET_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_NS_MAXBIN_THRS_Lable.setText(QCoreApplication.translate("MainPages", u"NS_MAXBIN_THRS", None))
        self.Swan01_ANGLE_GRP_SLOT_NUM.setTitle("")
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP0_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP1_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP2_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP3_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP4_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP5_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP6_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setToolTip(QCoreApplication.translate("MainPages", u"MAXBIN_THRS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Swan01_ANGLE_GRP7_SLOT_NUM_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_seg_hs_Label.setText(QCoreApplication.translate("MainPages", u"seg_hs", None))
#if QT_CONFIG(whatsthis)
        self.Swan01_seg_hs_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_h_seg_shift_Label.setText(QCoreApplication.translate("MainPages", u"h_seg_shift", None))
        self.Swan01_spad_vs_Label.setText(QCoreApplication.translate("MainPages", u"spad_vs", None))
        self.Swan01_light_shift_Label.setText(QCoreApplication.translate("MainPages", u"light shift", None))
        self.Swan01_sublight_group_Label.setText(QCoreApplication.translate("MainPages", u"sublight group", None))
        self.Swan01_sublight_group_LineEdit.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.Swan01_sublight_group_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"6\u884cpixel\u5206\u7ec4\u65b9\u5f0f", None))
        self.Swan01_sublight_shift_Label.setText(QCoreApplication.translate("MainPages", u"sublight shift", None))
        self.Swan01_ROI_Shape_Label.setText(QCoreApplication.translate("MainPages", u"ROI shape", None))
        self.Swan01_ROI_Shape_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Straight", None))
        self.Swan01_ROI_Shape_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Curve", None))

        self.Swan01_ROI_Retrace_Label.setText(QCoreApplication.translate("MainPages", u"ROI retrace", None))
        self.Swan01_ROI_Retrace_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Swan01_ROI_Retrace_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Swan01_v_spad_shift_Label.setText(QCoreApplication.translate("MainPages", u"v_spad_shift", None))
        self.Swan01_ROIConfig.setTabText(self.Swan01_ROIConfig.indexOf(self.Swan01_Config1byGUI), QCoreApplication.translate("MainPages", u"ROI GUI", None))
        self.Swan01_Cali_File_Load_Label.setText(QCoreApplication.translate("MainPages", u"Cali File", None))
        self.Swan01_Cali_File_Load_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9ROI\u5750\u6807\u6587\u4ef6\uff0c\u652f\u6301 .txt, .csv, .xls, .xlsx", None))
        self.Swan01_Cali_File_Load_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Swan01_Excel_Sheet_sel_Label.setText(QCoreApplication.translate("MainPages", u"Sheet Sel", None))
#if QT_CONFIG(whatsthis)
        self.Swan01_Excel_Sheet_sel_spinBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Swan01_ROIConfig.setTabText(self.Swan01_ROIConfig.indexOf(self.Swan01_Config2byCOOR), QCoreApplication.translate("MainPages", u"ROI COOR", None))
        self.Swan01_ROI_File_Label.setText(QCoreApplication.translate("MainPages", u"ROI File", None))
        self.Swan01_ROI_File_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u7f16\u8f91\u7684ROI\u6587\u4ef6", None))
        self.Swan01_ROI_File_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Swan01_Start_Rolling_Label.setText(QCoreApplication.translate("MainPages", u"Start Rolling", None))
        self.Swan01_End_Rolling_Label.setText(QCoreApplication.translate("MainPages", u"End Rolling", None))
        self.Swan01_ROIConfig.setTabText(self.Swan01_ROIConfig.indexOf(self.Swan01_Config3ROIEdit), QCoreApplication.translate("MainPages", u"ROI Edit", None))
        self.Swan01_cali_file_path_Label.setText(QCoreApplication.translate("MainPages", u"Cali File", None))
        self.Swan01_cali_file_path_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u9700\u8981\u6807\u5b9a\u7684ROI\u6587\u4ef6", None))
        self.Swan01_cali_file_path_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Swan01_img_mirror_Label.setText(QCoreApplication.translate("MainPages", u"Img Mirror ", None))
        self.Swan01_img_mirror_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No mirror", None))
        self.Swan01_img_mirror_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"X-axis mirror", None))
        self.Swan01_img_mirror_ComboBox.setItemText(2, QCoreApplication.translate("MainPages", u"Y-axis mirror", None))
        self.Swan01_img_mirror_ComboBox.setItemText(3, QCoreApplication.translate("MainPages", u"X-axis and Y-axis mirror", None))

        self.Swan01_remove_noise_Label.setText(QCoreApplication.translate("MainPages", u"remove noise", None))
        self.Swan01_remove_noise_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Swan01_remove_noise_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Swan01_light_smooth_Label.setText(QCoreApplication.translate("MainPages", u"light smooth", None))
        self.Swan01_light_smooth_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"No", None))
        self.Swan01_light_smooth_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Yes", None))

        self.Swan01_curvature_Label.setText(QCoreApplication.translate("MainPages", u"curvature", None))
        self.Swan01_correct_thres_Label.setText(QCoreApplication.translate("MainPages", u"correct thres", None))
        self.Swan01_cali_order_Label.setText(QCoreApplication.translate("MainPages", u"Cali Order", None))
        self.Swan01_cali_order_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"From small to large", None))
        self.Swan01_cali_order_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"From large to small", None))

        self.Swan01_cali_frm_num_Label.setText(QCoreApplication.translate("MainPages", u"cali frm num", None))
        self.Swan01_ref_segment_Label.setText(QCoreApplication.translate("MainPages", u"ref segment", None))
        self.Swan01_mode_2D_Label.setText(QCoreApplication.translate("MainPages", u"mode 2D", None))
        self.Swan01_mode_2D_ComboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Light strip energy is preferred", None))
        self.Swan01_mode_2D_ComboBox.setItemText(1, QCoreApplication.translate("MainPages", u"The number of covered photons is preferred", None))

        self.Swan01_ROIConfig.setTabText(self.Swan01_ROIConfig.indexOf(self.Swan01_Config4ROICali), QCoreApplication.translate("MainPages", u"ROI Cali", None))
        self.Swan01_ROIZoneConfig.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><a href=\"https://www.example.com\"><span style=\" text-decoration: underline; color:#0078d7;\">ZONE INFO</span></a></p></body></html>", None))
        self.Swan01_ROIView.setText(QCoreApplication.translate("MainPages", u"View", None))
        self.Swan01_ROISave.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Swan01_roi_sram_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165ROI\u4fdd\u5b58\u7684\u6587\u4ef6\u540d", None))
        self.Swan01_file_save_dir_Label.setText(QCoreApplication.translate("MainPages", u"File Save Path", None))
        self.Swan01_reference_script_Label.setText(QCoreApplication.translate("MainPages", u"Reference Script", None))
        self.Swan01_reference_script_parse_Button.setText(QCoreApplication.translate("MainPages", u"Parse", None))
        self.Swan01_roi_sram_name_CheckBox.setText(QCoreApplication.translate("MainPages", u"Include", None))
        self.Swan01_Save.setText(QCoreApplication.translate("MainPages", u"Save", None))
        self.Swan01_Open.setText(QCoreApplication.translate("MainPages", u"Open", None))
        self.Swan01_reg_script_name_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u8f93\u5165\u4fdd\u5b58\u811a\u672c\u7684\u6587\u4ef6\u540d", None))
        self.Swan01_roi_sram_name_Label.setText(QCoreApplication.translate("MainPages", u"ROI SRAM Name", None))
        self.Swan01_reference_script_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u9009\u62e9\u57fa\u51c6\u914d\u7f6e\u6587\u4ef6", None))
        self.Swan01_reference_script_sel_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
        self.Swan01_file_save_dir_LineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u8bf7\u6307\u5b9aSpadisApp\u8f6f\u4ef6\u8def\u5f84", None))
        self.Swan01_reg_script_name_Label.setText(QCoreApplication.translate("MainPages", u"Reg Script Name", None))
        self.Swan01_file_save_dir_Button.setText(QCoreApplication.translate("MainPages", u"Select", None))
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


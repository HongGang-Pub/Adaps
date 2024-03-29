# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ROI_OthersConfigazSxuj.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(766, 490)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget = QWidget(Dialog)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.horizontalWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SYS_CLK_Config_ComboBox = QComboBox(self.horizontalWidget)
        self.SYS_CLK_Config_ComboBox.setObjectName(u"SYS_CLK_Config_ComboBox")
        self.SYS_CLK_Config_ComboBox.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        font.setBold(False)
        self.SYS_CLK_Config_ComboBox.setFont(font)

        self.gridLayout.addWidget(self.SYS_CLK_Config_ComboBox, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.SYS_CLK_Config_Label = QLabel(self.horizontalWidget)
        self.SYS_CLK_Config_Label.setObjectName(u"SYS_CLK_Config_Label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        self.SYS_CLK_Config_Label.setFont(font1)

        self.gridLayout.addWidget(self.SYS_CLK_Config_Label, 0, 3, 1, 1)

        self.REF_CLK_Config_Label = QLabel(self.horizontalWidget)
        self.REF_CLK_Config_Label.setObjectName(u"REF_CLK_Config_Label")
        self.REF_CLK_Config_Label.setFont(font1)

        self.gridLayout.addWidget(self.REF_CLK_Config_Label, 0, 0, 1, 1)

        self.REF_CLK_Config_ComboBox = QComboBox(self.horizontalWidget)
        self.REF_CLK_Config_ComboBox.setObjectName(u"REF_CLK_Config_ComboBox")
        self.REF_CLK_Config_ComboBox.setMinimumSize(QSize(100, 0))
        self.REF_CLK_Config_ComboBox.setFont(font)

        self.gridLayout.addWidget(self.REF_CLK_Config_ComboBox, 0, 1, 1, 1)

        self.ROI_Zone_Sel_CheckBox = QCheckBox(self.horizontalWidget)
        self.ROI_Zone_Sel_CheckBox.setObjectName(u"ROI_Zone_Sel_CheckBox")

        self.gridLayout.addWidget(self.ROI_Zone_Sel_CheckBox, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 7, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.horizontalWidget)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 8)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 33):
            self.tableWidget.setColumnCount(33)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(31, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(32, __qtablewidgetitem32)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem42)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(33)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.widget)

        self.verticalWidget = QWidget(Dialog)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.verticalWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.REG_CFG_File_LineEdit_2 = QLineEdit(self.verticalWidget)
        self.REG_CFG_File_LineEdit_2.setObjectName(u"REG_CFG_File_LineEdit_2")
        self.REG_CFG_File_LineEdit_2.setEnabled(False)
        self.REG_CFG_File_LineEdit_2.setMinimumSize(QSize(100, 0))
        self.REG_CFG_File_LineEdit_2.setMaximumSize(QSize(100, 16777215))
        self.REG_CFG_File_LineEdit_2.setFont(font1)

        self.gridLayout_3.addWidget(self.REG_CFG_File_LineEdit_2, 0, 1, 1, 1)

        self.REG_CFG_File_Label_2 = QLabel(self.verticalWidget)
        self.REG_CFG_File_Label_2.setObjectName(u"REG_CFG_File_Label_2")
        self.REG_CFG_File_Label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.REG_CFG_File_Label_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.verticalWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SYS_CLK_Config_Label.setText(QCoreApplication.translate("Dialog", u"SYS CLK", None))
        self.REF_CLK_Config_Label.setText(QCoreApplication.translate("Dialog", u"REF CLK", None))
        self.ROI_Zone_Sel_CheckBox.setText(QCoreApplication.translate("Dialog", u"Configure each Zone independently", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Zone", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Zone1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Zone2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Zone3", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Zone4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Zone5", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Zone6", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Zone7", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Zone8", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Zone9", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Zone10", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Zone11", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Zone12", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"Zone13", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"Zone14", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"Zone15", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"Zone16", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"Zone17", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"Zone18", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"Zone19", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"Zone20", None));
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"Zone21", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"Zone22", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"Zone23", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"Zone24", None));
        ___qtablewidgetitem25 = self.tableWidget.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"Zone25", None));
        ___qtablewidgetitem26 = self.tableWidget.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"Zone26", None));
        ___qtablewidgetitem27 = self.tableWidget.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"Zone27", None));
        ___qtablewidgetitem28 = self.tableWidget.horizontalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"Zone28", None));
        ___qtablewidgetitem29 = self.tableWidget.horizontalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"Zone29", None));
        ___qtablewidgetitem30 = self.tableWidget.horizontalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Dialog", u"Zone30", None));
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Dialog", u"Zone31", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(32)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Dialog", u"Zone32", None));
        ___qtablewidgetitem33 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Dialog", u"SUB_EXPOTIME", None));
        ___qtablewidgetitem34 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Dialog", u"SUB_IDLETIME", None));
        ___qtablewidgetitem35 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Dialog", u"EXPO_LASPRD", None));
        ___qtablewidgetitem36 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Dialog", u"EXPO_PLSWC", None));
        ___qtablewidgetitem37 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Dialog", u"EXPO_PLSWF", None));
        ___qtablewidgetitem38 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Dialog", u"TX_EN", None));
        ___qtablewidgetitem39 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Dialog", u"SPADEN_IN3ROWS", None));
        ___qtablewidgetitem40 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Dialog", u"MF Kernel", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.REG_CFG_File_LineEdit_2.setPlaceholderText("")
        self.REG_CFG_File_Label_2.setText(QCoreApplication.translate("Dialog", u"Expotime", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roi_zone_configraRzBm.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ROIZoneConfig(object):
    def setupUi(self, ROIZoneConfig):
        if not ROIZoneConfig.objectName():
            ROIZoneConfig.setObjectName(u"ROIZoneConfig")
        ROIZoneConfig.resize(966, 583)
        ROIZoneConfig.setSizeGripEnabled(True)
        ROIZoneConfig.setModal(False)
        self.verticalLayout = QVBoxLayout(ROIZoneConfig)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget = QWidget(ROIZoneConfig)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.horizontalWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ZoneConfigSel_Label = QLabel(self.horizontalWidget)
        self.ZoneConfigSel_Label.setObjectName(u"ZoneConfigSel_Label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        self.ZoneConfigSel_Label.setFont(font)

        self.gridLayout.addWidget(self.ZoneConfigSel_Label, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 10, 1, 1)

        self.ZoneConfigSel_CheckBox = QCheckBox(self.horizontalWidget)
        self.ZoneConfigSel_CheckBox.setObjectName(u"ZoneConfigSel_CheckBox")

        self.gridLayout.addWidget(self.ZoneConfigSel_CheckBox, 0, 9, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 8, 1, 1)

        self.ZoneConfigSel_SpinBox = QSpinBox(self.horizontalWidget)
        self.ZoneConfigSel_SpinBox.setObjectName(u"ZoneConfigSel_SpinBox")
        self.ZoneConfigSel_SpinBox.setMinimumSize(QSize(50, 0))
        self.ZoneConfigSel_SpinBox.setMinimum(1)
        self.ZoneConfigSel_SpinBox.setMaximum(32)

        self.gridLayout.addWidget(self.ZoneConfigSel_SpinBox, 0, 7, 1, 1)

        self.Expoperiod_Value = QLineEdit(self.horizontalWidget)
        self.Expoperiod_Value.setObjectName(u"Expoperiod_Value")
        self.Expoperiod_Value.setEnabled(False)
        self.Expoperiod_Value.setMinimumSize(QSize(100, 0))
        self.Expoperiod_Value.setMaximumSize(QSize(100, 16777215))
        self.Expoperiod_Value.setFont(font)

        self.gridLayout.addWidget(self.Expoperiod_Value, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.Expotime_Value = QLineEdit(self.horizontalWidget)
        self.Expotime_Value.setObjectName(u"Expotime_Value")
        self.Expotime_Value.setEnabled(False)
        self.Expotime_Value.setMinimumSize(QSize(100, 0))
        self.Expotime_Value.setMaximumSize(QSize(100, 16777215))
        self.Expotime_Value.setFont(font)

        self.gridLayout.addWidget(self.Expotime_Value, 0, 4, 1, 1)

        self.Expotime_Label = QLabel(self.horizontalWidget)
        self.Expotime_Label.setObjectName(u"Expotime_Label")
        self.Expotime_Label.setFont(font)

        self.gridLayout.addWidget(self.Expotime_Label, 0, 3, 1, 1)

        self.Expoperiod_Label = QLabel(self.horizontalWidget)
        self.Expoperiod_Label.setObjectName(u"Expoperiod_Label")
        self.Expoperiod_Label.setFont(font)

        self.gridLayout.addWidget(self.Expoperiod_Label, 0, 0, 1, 1)

        self.EditZoneConifg_Button = QPushButton(self.horizontalWidget)
        self.EditZoneConifg_Button.setObjectName(u"EditZoneConifg_Button")

        self.gridLayout.addWidget(self.EditZoneConifg_Button, 0, 11, 1, 1)


        self.verticalLayout.addWidget(self.horizontalWidget)

        self.widget = QWidget(ROIZoneConfig)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 8)
        self.ZoneConfigInputTable = QTableWidget(self.widget)
        if (self.ZoneConfigInputTable.columnCount() < 32):
            self.ZoneConfigInputTable.setColumnCount(32)
        __qtablewidgetitem = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.ZoneConfigInputTable.setHorizontalHeaderItem(31, __qtablewidgetitem31)
        if (self.ZoneConfigInputTable.rowCount() < 23):
            self.ZoneConfigInputTable.setRowCount(23)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(7, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(9, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(10, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(11, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(12, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(13, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(14, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(15, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(16, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(17, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(18, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(19, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(20, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(21, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.ZoneConfigInputTable.setVerticalHeaderItem(22, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.ZoneConfigInputTable.setItem(0, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.ZoneConfigInputTable.setItem(1, 0, __qtablewidgetitem56)
        self.ZoneConfigInputTable.setObjectName(u"ZoneConfigInputTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ZoneConfigInputTable.sizePolicy().hasHeightForWidth())
        self.ZoneConfigInputTable.setSizePolicy(sizePolicy1)
        self.ZoneConfigInputTable.setAutoScrollMargin(1)
        self.ZoneConfigInputTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ZoneConfigInputTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ZoneConfigInputTable.setShowGrid(True)
        self.ZoneConfigInputTable.setGridStyle(Qt.SolidLine)
        self.ZoneConfigInputTable.setSortingEnabled(False)
        self.ZoneConfigInputTable.setRowCount(23)
        self.ZoneConfigInputTable.setColumnCount(32)
        self.ZoneConfigInputTable.horizontalHeader().setVisible(True)
        self.ZoneConfigInputTable.horizontalHeader().setCascadingSectionResizes(False)
        self.ZoneConfigInputTable.horizontalHeader().setMinimumSectionSize(0)
        self.ZoneConfigInputTable.horizontalHeader().setDefaultSectionSize(60)
        self.ZoneConfigInputTable.horizontalHeader().setHighlightSections(True)
        self.ZoneConfigInputTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.ZoneConfigInputTable.verticalHeader().setVisible(True)
        self.ZoneConfigInputTable.verticalHeader().setHighlightSections(True)
        self.ZoneConfigInputTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.ZoneConfigInputTable)


        self.verticalLayout.addWidget(self.widget)

        self.verticalWidget = QWidget(ROIZoneConfig)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.verticalWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.verticalWidget)

        self.buttonBox = QDialogButtonBox(ROIZoneConfig)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ROIZoneConfig)
        self.buttonBox.accepted.connect(ROIZoneConfig.accept)
        self.buttonBox.rejected.connect(ROIZoneConfig.reject)

        QMetaObject.connectSlotsByName(ROIZoneConfig)
    # setupUi

    def retranslateUi(self, ROIZoneConfig):
        ROIZoneConfig.setWindowTitle(QCoreApplication.translate("ROIZoneConfig", u"Dialog", None))
        self.ZoneConfigSel_Label.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone Config Sel", None))
        self.ZoneConfigSel_CheckBox.setText(QCoreApplication.translate("ROIZoneConfig", u"Configure each Zone independently", None))
        self.Expoperiod_Value.setPlaceholderText("")
        self.Expotime_Value.setPlaceholderText("")
        self.Expotime_Label.setText(QCoreApplication.translate("ROIZoneConfig", u"Expotime", None))
        self.Expoperiod_Label.setText(QCoreApplication.translate("ROIZoneConfig", u"Expo Period", None))
        self.EditZoneConifg_Button.setText(QCoreApplication.translate("ROIZoneConfig", u"Edit", None))
        ___qtablewidgetitem = self.ZoneConfigInputTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone1", None));
        ___qtablewidgetitem1 = self.ZoneConfigInputTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone2", None));
        ___qtablewidgetitem2 = self.ZoneConfigInputTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone3", None));
        ___qtablewidgetitem3 = self.ZoneConfigInputTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone4", None));
        ___qtablewidgetitem4 = self.ZoneConfigInputTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone5", None));
        ___qtablewidgetitem5 = self.ZoneConfigInputTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone6", None));
        ___qtablewidgetitem6 = self.ZoneConfigInputTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone7", None));
        ___qtablewidgetitem7 = self.ZoneConfigInputTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone8", None));
        ___qtablewidgetitem8 = self.ZoneConfigInputTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone9", None));
        ___qtablewidgetitem9 = self.ZoneConfigInputTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone10", None));
        ___qtablewidgetitem10 = self.ZoneConfigInputTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone11", None));
        ___qtablewidgetitem11 = self.ZoneConfigInputTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone12", None));
        ___qtablewidgetitem12 = self.ZoneConfigInputTable.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone13", None));
        ___qtablewidgetitem13 = self.ZoneConfigInputTable.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone14", None));
        ___qtablewidgetitem14 = self.ZoneConfigInputTable.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone15", None));
        ___qtablewidgetitem15 = self.ZoneConfigInputTable.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone16", None));
        ___qtablewidgetitem16 = self.ZoneConfigInputTable.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone17", None));
        ___qtablewidgetitem17 = self.ZoneConfigInputTable.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone18", None));
        ___qtablewidgetitem18 = self.ZoneConfigInputTable.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone19", None));
        ___qtablewidgetitem19 = self.ZoneConfigInputTable.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone20", None));
        ___qtablewidgetitem20 = self.ZoneConfigInputTable.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone21", None));
        ___qtablewidgetitem21 = self.ZoneConfigInputTable.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone22", None));
        ___qtablewidgetitem22 = self.ZoneConfigInputTable.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone23", None));
        ___qtablewidgetitem23 = self.ZoneConfigInputTable.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone24", None));
        ___qtablewidgetitem24 = self.ZoneConfigInputTable.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone25", None));
        ___qtablewidgetitem25 = self.ZoneConfigInputTable.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone26", None));
        ___qtablewidgetitem26 = self.ZoneConfigInputTable.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone27", None));
        ___qtablewidgetitem27 = self.ZoneConfigInputTable.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone28", None));
        ___qtablewidgetitem28 = self.ZoneConfigInputTable.horizontalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone29", None));
        ___qtablewidgetitem29 = self.ZoneConfigInputTable.horizontalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone30", None));
        ___qtablewidgetitem30 = self.ZoneConfigInputTable.horizontalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone31", None));
        ___qtablewidgetitem31 = self.ZoneConfigInputTable.horizontalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("ROIZoneConfig", u"Zone32", None));
        ___qtablewidgetitem32 = self.ZoneConfigInputTable.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("ROIZoneConfig", u"SUB_EXPOTIME", None));
        ___qtablewidgetitem33 = self.ZoneConfigInputTable.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("ROIZoneConfig", u"SUB_IDLETIME", None));
        ___qtablewidgetitem34 = self.ZoneConfigInputTable.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("ROIZoneConfig", u"EXPO_LASPRD", None));
        ___qtablewidgetitem35 = self.ZoneConfigInputTable.verticalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("ROIZoneConfig", u"EXPO_PLSWC", None));
        ___qtablewidgetitem36 = self.ZoneConfigInputTable.verticalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("ROIZoneConfig", u"EXPO_PLSWF", None));
        ___qtablewidgetitem37 = self.ZoneConfigInputTable.verticalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("ROIZoneConfig", u"TX_EN", None));
        ___qtablewidgetitem38 = self.ZoneConfigInputTable.verticalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("ROIZoneConfig", u"SPADEN_IN3ROWS", None));
        ___qtablewidgetitem39 = self.ZoneConfigInputTable.verticalHeaderItem(7)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 1", None));
        ___qtablewidgetitem40 = self.ZoneConfigInputTable.verticalHeaderItem(8)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 2", None));
        ___qtablewidgetitem41 = self.ZoneConfigInputTable.verticalHeaderItem(9)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 3", None));
        ___qtablewidgetitem42 = self.ZoneConfigInputTable.verticalHeaderItem(10)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 4", None));
        ___qtablewidgetitem43 = self.ZoneConfigInputTable.verticalHeaderItem(11)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 5", None));
        ___qtablewidgetitem44 = self.ZoneConfigInputTable.verticalHeaderItem(12)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 6", None));
        ___qtablewidgetitem45 = self.ZoneConfigInputTable.verticalHeaderItem(13)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 7", None));
        ___qtablewidgetitem46 = self.ZoneConfigInputTable.verticalHeaderItem(14)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 8", None));
        ___qtablewidgetitem47 = self.ZoneConfigInputTable.verticalHeaderItem(15)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 9", None));
        ___qtablewidgetitem48 = self.ZoneConfigInputTable.verticalHeaderItem(16)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 10", None));
        ___qtablewidgetitem49 = self.ZoneConfigInputTable.verticalHeaderItem(17)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 11", None));
        ___qtablewidgetitem50 = self.ZoneConfigInputTable.verticalHeaderItem(18)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 12", None));
        ___qtablewidgetitem51 = self.ZoneConfigInputTable.verticalHeaderItem(19)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 13", None));
        ___qtablewidgetitem52 = self.ZoneConfigInputTable.verticalHeaderItem(20)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 14", None));
        ___qtablewidgetitem53 = self.ZoneConfigInputTable.verticalHeaderItem(21)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 15", None));
        ___qtablewidgetitem54 = self.ZoneConfigInputTable.verticalHeaderItem(22)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("ROIZoneConfig", u"MF Kernel 16", None));

        __sortingEnabled = self.ZoneConfigInputTable.isSortingEnabled()
        self.ZoneConfigInputTable.setSortingEnabled(False)
        self.ZoneConfigInputTable.setSortingEnabled(__sortingEnabled)

    # retranslateUi


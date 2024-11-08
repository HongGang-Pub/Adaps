# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# QT CORE
# Change for PySide Or PyQt
# ///////////////////////// WARNING: ////////////////////////////
# Remember that changing to PyQt too many modules will have 
# problems because some classes have different names like: 
# Property (pyqtProperty), Slot (pyqtSlot), Signal (pyqtSignal)
# among others.
# ///////////////////////////////////////////////////////////////
# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *

from PySide6.QtCore import QTimer, QThread, QSize, QRegularExpression, QEvent, QUrl, QPropertyAnimation, QEasingCurve
from PySide6.QtCore import QParallelAnimationGroup, QRect, QObject, Signal, QPoint, Property

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QGraphicsDropShadowEffect
from PySide6.QtWidgets import QFrame, QSpinBox, QDialog, QHeaderView, QLineEdit, QTableWidget, QMessageBox
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QFileDialog, QPushButton
from PySide6.QtWidgets import QListView, QSpacerItem, QSizePolicy, QTextBrowser, QSizeGrip, QSlider, QCheckBox

from PySide6.QtGui import QRegularExpressionValidator, Qt, QShortcut, QKeySequence, QDesktopServices, QIcon, QAction
from PySide6.QtGui import QCursor, QColor, QPainter, QFont, QPen, QMouseEvent, QStandardItemModel, QStandardItem
from PySide6.QtGui import QBrush, QPixmap

from PySide6.QtSvgWidgets import QSvgWidget

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from AdapsChip.ChipUI.gui.qt_core import *


class NoWheelSpinBox(QSpinBox):
    def wheelEvent(self, event):
        # 忽略滚轮事件
        event.ignore()

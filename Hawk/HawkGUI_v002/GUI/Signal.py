from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QPlainTextEdit


# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    sync_signal = Signal()
    int_signal1 = Signal(int)
    text_signal1 = Signal(str)
    text_signal2 = Signal(QPlainTextEdit, str)

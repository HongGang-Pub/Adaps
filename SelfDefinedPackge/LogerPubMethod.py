import PySide6
from PySide6.QtGui import QColor, QBrush, QTextCursor
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtCore import QObject, Signal
import logging
import logging.handlers
import queue


def LoggingForConsoleFormat():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


class LogerForMultithreading:
    """
    此方法仅支持向 QPlainTextEdit 中写入日志
    """

    def __init__(self, name=None, loglevel=logging.INFO):
        self.logger_name = name
        self.loglevel = loglevel

        # 创建一个日志器
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.loglevel)

        # 创建一个队列对象，用于存储日志消息
        self.log_queue = queue.Queue()
        self.queue_handler = logging.handlers.QueueHandler(self.log_queue)
        # self.console_handler = logging.StreamHandler()

        # 创建一个Formatter，用于设置日志的格式
        formatter = logging.Formatter(fmt="%(asctime)s: %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
        self.queue_handler.setFormatter(formatter)
        # self.console_handler.setFormatter(formatter)

        self.logger.addHandler(self.queue_handler)
        # self.logger.addHandler(self.console_handler)

    def update_log_for_qplaintextedit(self, log_weight: QPlainTextEdit = None, theme: str = "light"):
        while not self.log_queue.empty():
            log_theme_for_qplaintextedit = ["#DFE1E2", "yellow", "red"] if theme == "dark" else ["#9DA9B5", "blue", "red"]
            record = self.log_queue.get()
            message = record.message
            log_type = 2 if record.levelno >= 40 else 1 if record.levelno >= 30 else 0

            color = log_theme_for_qplaintextedit[log_type]

            cursor = log_weight.textCursor()
            cursor.movePosition(QTextCursor.End)

            text_format = log_weight.currentCharFormat()  # 创建TextCharFormat对象 获取当前字文本的字符串格式
            text_format.setForeground(QBrush(QColor(color)))  # 设置字体颜色
            cursor.mergeCharFormat(text_format)  # 追加格式到原有文本
            cursor.insertText(f"{message}")
            log_weight.setTextCursor(cursor)
            log_weight.ensureCursorVisible()
            cursor.insertText(f"\n")

import datetime
import sys

from PySide6.QtGui import QColor, QBrush, QTextCursor, QTextCharFormat, QDesktopServices, QTextBlockFormat
from PySide6.QtWidgets import QTextBrowser
import logging
import logging.handlers
import queue

# ///////////////////////////////////////////////////////////////
# 统一增加一个 INFO_PLUS 日志级别, 代码中识别后, 进行特殊处理
# ///////////////////////////////////////////////////////////////
# 定义新的日志级别
INFO_PLUS = 25  # 比 INFO 的值高，用于打印特殊的 INFO 信息
logging.addLevelName(INFO_PLUS, "INFO_PLUS")


def _INFO_PLUS(msg, *args, **kwargs):
    if logging.getLogger(__name__).isEnabledFor(INFO_PLUS):
        logging.log(INFO_PLUS, msg, *args, **kwargs)


logging.INFO_PLUS = _INFO_PLUS


# ///////////////////////////////////////////////////////////////
# 增加一个通用的日志格式化方法
# ///////////////////////////////////////////////////////////////
def LoggingForConsoleFormat():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


# ///////////////////////////////////////////////////////////////
# 超链接打开本地文件
# ///////////////////////////////////////////////////////////////
def open_folder(url):
    if url.isLocalFile():
        QDesktopServices.openUrl(url)


# ///////////////////////////////////////////////////////////////
# 创建 html 格式文件
# ///////////////////////////////////////////////////////////////
def create_file_hyperlink(url):
    """针对QTextCursor创建文件路径"""
    s = f'<a href="file:///{url}" style="color: blue; text-decoration: underline;">{url}</a>&#32;'
    return s


# ///////////////////////////////////////////////////////////////
# 创建等宽文件格式的文本内容
# ///////////////////////////////////////////////////////////////
def create_consolas_str(_str, color="#0076f6"):
    """针对QTextCursor创建文件路径"""
    s = f'<span style="font-family: Consolas; white-space: pre; color: {color}">{_str}</span>'
    # s = f'<p style="margin:0;"><span style="font-family: Consolas; white-space: pre; color: {color}">{_str}</span></p>'
    return s


class LogerForMultithreading:
    """
    此方法仅支持向 QTextBrowser 中写入日志
    """

    def __init__(self, name=None, loglevel=logging.INFO, themes=None, font="Microsoft YaHei UI"):
        self.logger_name = name
        self.font = font
        # 日志主题, 按顺序分别为  INFO:20, INFO_PLUS:25, WARNING:30, ERROR:40
        self.color_map = ["black", "yellow", "red"]
        if themes is not None:
            self.color_map = themes["app_color"]["logger"]

        self.loglevel = loglevel

        # 创建一个日志器
        self.root_logger = logging.getLogger(self.logger_name)
        self.root_logger.setLevel(self.loglevel)
        # 创建一个队列对象，用于存储日志消息

        # 1️⃣ 添加 GUI Handler
        self.LOG_QUEUE = queue.Queue()
        self.gui_handler = logging.handlers.QueueHandler(self.LOG_QUEUE)
        self.gui_handler.setLevel(logging.INFO)
        self.gui_handler.setFormatter(logging.Formatter(fmt="%(asctime)s: %(message)s", datefmt='%Y-%m-%d %H:%M:%S'))
        self.root_logger.addHandler(self.gui_handler)

        # 2️⃣ 添加文件 Handler
        self.LOG_FILE = f"application_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
        self.file_handler = logging.FileHandler(self.LOG_FILE, encoding="utf-8")
        self.file_handler.setLevel(logging.INFO)
        self.file_handler.setFormatter(logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
        self.root_logger.addHandler(self.file_handler)

        # 3️⃣ 重定向 stdout 和 stderr
        sys.stdout = LoggerStream(logging.INFO)
        sys.stderr = LoggerStream(logging.ERROR)

    def update_log_from_logger(self, log_widget: QTextBrowser = None):
        while not self.LOG_QUEUE.empty():
            record = self.LOG_QUEUE.get()
            # INFO:20, INFO_PLUS:25, WARNING:30, ERROR:40
            log_type = 2 if record.levelno >= 40 \
                else 1 if record.levelno >= 30 \
                else 0
            color = self.color_map[log_type]
            message = record.message[21:] if record.levelno == INFO_PLUS else record.message  # 如果是 info_pluse, 去除日志时间信息

            cursor = log_widget.textCursor()
            cursor.movePosition(QTextCursor.End)

            # text_format = log_widget.currentCharFormat()  # 创建TextCharFormat对象 获取当前字文本的字符串格式
            text_format = QTextCharFormat()
            text_format.setForeground(QBrush(QColor(color)))  # 设置字体颜色
            text_format.setFontFamily(self.font)
            cursor.mergeCharFormat(text_format)  # 追加格式到原有文本

            block_format = QTextBlockFormat()
            block_format.setLineHeight(120, 1)
            cursor.setBlockFormat(block_format)

            log_widget.setTextCursor(cursor)
            log_widget.append(message)
            log_widget.ensureCursorVisible()


# ==============================================================================

# 自定义 Handler，将日志输出到 QTextBrowser
class QTextBrowserHandler(logging.Handler):
    def __init__(self, text_browser: QTextBrowser, themes=None, font="Microsoft YaHei UI"):
        super().__init__()
        self.text_browser = text_browser
        self.font = font
        self.color_map = ["black", "orange", "red"]
        if themes is not None:
            self.color_map = themes["app_color"]["logger"]

    def emit(self, record):
        """日志输出到 GUI，并根据日志等级设置颜色"""
        # color_map = {
        #     logging.DEBUG: QColor("gray"),
        #     logging.INFO: QColor("black"),
        #     logging.WARNING: QColor("orange"),
        #     logging.ERROR: QColor("red"),
        #     logging.CRITICAL: QColor("darkred"),
        # }
        # color = color_map.get(record.levelno, QColor("black"))

        log_type = 2 if record.levelno >= 40 \
                else 1 if record.levelno >= 30 \
                else 0
        color = self.color_map[log_type]
        message = self.format(record)        # 格式化日志消息

        cursor = self.text_browser.textCursor()
        cursor.movePosition(QTextCursor.End)

        # text_format = log_widget.currentCharFormat()  # 创建TextCharFormat对象 获取当前字文本的字符串格式
        text_format = QTextCharFormat()
        text_format.setForeground(QColor(color))  # 设置字体颜色
        text_format.setFontFamily(self.font)
        cursor.mergeCharFormat(text_format)  # 追加格式到原有文本

        block_format = QTextBlockFormat()
        block_format.setLineHeight(120, 1)
        cursor.setBlockFormat(block_format)

        self.text_browser.setTextCursor(cursor)
        self.text_browser.append(message)
        self.text_browser.ensureCursorVisible()


# 🔹 全局日志配置（影响所有 `logging` 调用）
def setup_logging(text_browser: QTextBrowser):
    # 获取 root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # 设置全局日志级别

    # 1️⃣ 添加 GUI Handler
    gui_handler = QTextBrowserHandler(text_browser)
    gui_handler.setFormatter(logging.Formatter("%(asctime)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
    root_logger.addHandler(gui_handler)

    # 2️⃣ 添加文件 Handler
    LOG_FILE = f"application_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
    root_logger.addHandler(file_handler)

    # 3️⃣ 重定向 stdout 和 stderr
    sys.stdout = LoggerStream(logging.INFO)
    sys.stderr = LoggerStream(logging.ERROR)


# 兼容 stdout/stderr 的日志流
class LoggerStream:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        if message.strip():
            logging.log(self.level, message.strip())

    def flush(self):
        pass  # 兼容性方法，通常不需要操作

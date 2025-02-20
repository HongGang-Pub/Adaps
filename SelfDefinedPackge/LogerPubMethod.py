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
    s = f'<a href="file:///{url}" style="color: blue; text-decoration: underline;">{url}</a>\t'
    return s


class LogerForMultithreading:
    """
    此方法仅支持向 QTextBrowser 中写入日志
    """

    def __init__(self, name=None, loglevel=logging.INFO, themes=None, font="Microsoft YaHei UI"):
        self.logger_name = name
        self.font = font
        # 日志主题, 按顺序分别为  INFO:20, INFO_PLUS:25, WARNING:30, ERROR:40
        self.log_print_color = ["black", "blue", "yellow", "red"]
        if themes is not None:
            self.log_print_color = themes["app_color"]["log_output"]

        self.loglevel = loglevel

        # 创建一个日志器
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.loglevel)

        # 创建一个队列对象，用于存储日志消息
        self.log_queue = queue.Queue()
        self.queue_handler = logging.handlers.QueueHandler(self.log_queue)
        # self.console_handler = logging.StreamHandler()

        # 创建一个Formatter, 用于设置日志的格式
        formatter = logging.Formatter(fmt="%(asctime)s: %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
        self.queue_handler.setFormatter(formatter)
        # self.console_handler.setFormatter(formatter)

        self.logger.addHandler(self.queue_handler)
        # self.logger.addHandler(self.console_handler)

    def update_log_from_logger(self, log_widget: QTextBrowser = None):
        while not self.log_queue.empty():
            record = self.log_queue.get()
            # INFO:20, INFO_PLUS:25, WARNING:30, ERROR:40
            log_type = 2 if record.levelno >= 40 \
                else 1 if record.levelno >= 30 \
                else 0
            color = self.log_print_color[log_type]
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

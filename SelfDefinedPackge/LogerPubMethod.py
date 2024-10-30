from PySide6.QtGui import QColor, QBrush, QTextCursor, QTextCharFormat, QDesktopServices
import logging
import logging.handlers
import queue

# ///////////////////////////////////////////////////////////////
# 统一增加一个 INFO_PLUS 日志级别, 用于打印特殊的 INFO 日志
# ///////////////////////////////////////////////////////////////
# 定义新的日志级别
INFO_PLUS = 25  # 比 INFO 的值高，用于打印特殊的 INFO 信息
logging.addLevelName(INFO_PLUS, "INFO_PLUS")


def _INFO_PLUS(msg, *args, **kwargs):
    if logging.getLogger(__name__).isEnabledFor(INFO_PLUS):
        logging.log(INFO_PLUS, msg, *args, **kwargs)


logging.INFO_PLUS = _INFO_PLUS


def LoggingForConsoleFormat():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def open_folder(url):
    if url.isLocalFile():
        QDesktopServices.openUrl(url)


def create_file_hyperlink(file_type, url):
    """针对QTextCursor创建文件路径"""
    s = f'{file_type} has been save to <a href="file:///{url}" style="color: blue; text-decoration: underline;">{url}</a>\t'
    return s


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

    def update_log_from_logger(self, log_widget: QTextCursor = None, theme: str = "light"):
        while not self.log_queue.empty():
            log_theme_for_qplaintextedit = ["#DFE1E2", "#0078d7", "yellow", "red"] if theme == "dark" \
                else ["#9DA9B5", "#0078d7", "#b58900", "red"]
            record = self.log_queue.get()
            message = record.message
            # ERROR:40
            # WARNING:30
            # INFO_PLUS:25
            # INFO:20
            log_type = 3 if record.levelno >= 40 \
                else 2 if record.levelno >= 30 \
                else 1 if record.levelno >= 25 \
                else 0

            color = log_theme_for_qplaintextedit[log_type]

            cursor = log_widget.textCursor()
            cursor.movePosition(QTextCursor.End)

            # text_format = log_widget.currentCharFormat()  # 创建TextCharFormat对象 获取当前字文本的字符串格式
            text_format = QTextCharFormat()
            text_format.setForeground(QBrush(QColor(color)))  # 设置字体颜色
            cursor.mergeCharFormat(text_format)  # 追加格式到原有文本
            log_widget.setTextCursor(cursor)
            log_widget.append(message)
            log_widget.ensureCursorVisible()

import time

from PySide6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QPushButton, QVBoxLayout, QLabel, QPlainTextEdit, QHBoxLayout
from PySide6.QtCore import QTimer
import logging
import logging.handlers
import queue


def log_add():
    logger1 = logging.getLogger("gui1")
    logger2 = logging.getLogger("gui2")
    logger1.info(f"This is {time.time()} time")
    logger1.debug(f"This is {time.time()} time")
    logger2.error(f"This is {time.time()} time")
    # print(f"This is {time.time()} time")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(900, 400)

        self.label = QLabel(self)
        self.label.setGeometry(9, 9, 800, 300)
        self.vlaout = QHBoxLayout(self.label)

        self.text_browser = QPlainTextEdit()
        # self.text_browser.setReadOnly(True)

        self.btn = QPushButton()
        self.btn.setText("aaaa")

        self.vlaout.addWidget(self.text_browser)
        self.vlaout.addWidget(self.btn)

        self.logger1 = logging.getLogger("gui1")
        self.logger2 = logging.getLogger("gui2")
        self.logger1.setLevel('DEBUG')
        # self.logger.setLevel(logging.DEBUG)

        self.log_queue = queue.Queue()
        self.queue_handler = logging.handlers.QueueHandler(self.log_queue)
        # self.consle_handler1 = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        self.queue_handler.setFormatter(formatter)
        # self.consle_handler1.setFormatter(formatter)

        self.logger1.addHandler(self.queue_handler)
        # self.logger.addHandler(self.consle_handler1)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_log_messages)
        self.timer.start(200)

        self.btn.clicked.connect(log_add)

    def update_log_messages(self):
        while not self.log_queue.empty():
            record = self.log_queue.get()
            message = self.queue_handler.format(record)
            # self.text_browser.appendPlainText(message)
            self.text_browser.appendPlainText(record.message)


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()

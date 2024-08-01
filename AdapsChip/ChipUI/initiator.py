import os
import sys
from AdapsChip.ChipUI.gui.qt_core import *
# from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QVBoxLayout, QWidget
# from PySide6.QtGui import QCursor, QIcon
# from PySide6.QtCore import QTimer


class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Initial Window")
        self.setFixedSize(300, 100)
        # self.setGeometry(300, 300, 300, 100)
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2 - 50
            # print(x, y)
            self.move(x, y)

        layout = QVBoxLayout()

        self.label = QLabel("Loading...")
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # QTimer.singleShot(0, self.start_loading)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(10, self.load_main_window)

    def load_main_window(self):
        # self.label.setText("Loading...")
        # self.main_window = MainWindow()
        QTimer.singleShot(100, self.open_main_window)

    def open_main_window(self):
        self.close()
        os.system('main.exe')


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("gui/icon.ico"))

    # SHOW MAIN WINDOW
    # ///////////////////////////////////////////////////////////////
    window = InitialWindow()
    window.show()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
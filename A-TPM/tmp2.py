import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a menu item to trigger the creation of a new window
        new_win_action = QAction('New Window', self)
        new_win_action.triggered.connect(self.create_sub_window)

        # Create a menu bar and add the menu item
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_win_action)

        # Create a multiple document interface (MDI) area
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # Create a text editor widget to use in the sub windows
        self.text_edit = QTextEdit()

    def create_sub_window(self):
        # Create a new sub window
        sub_window = QMdiSubWindow()
        sub_window.setWidget(self.text_edit)
        sub_window.setWindowTitle('Sub Window')

        # Make the sub window resizable and maximizable
        sub_window.setWindowFlags(sub_window.windowFlags() | 
                                  Qt.WindowMaximizeButtonHint |
                                  Qt.WindowMinimizeButtonHint |
                                  Qt.WindowCloseButtonHint)

        # Add the sub window to the MDI area
        self.mdi.addSubWindow(sub_window)

        # Show the sub window
        sub_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


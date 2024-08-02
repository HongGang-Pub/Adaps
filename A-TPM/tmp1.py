import sys
from PySide6.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt, QObject, Signal, QEvent


class LineEditClickFilter(QObject):
    clicked = Signal()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.clicked.emit()
            return True
        return False


class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CustomComboBox, self).__init__(parent)
        self.setEditable(True)
        self.line_edit = self.lineEdit()
        self.line_edit.setReadOnly(True)  # 设置 QLineEdit 为只读

        self.click_filter = LineEditClickFilter()
        self.line_edit.installEventFilter(self.click_filter)
        self.click_filter.clicked.connect(self.togglePopup)

        self.popup_visible = False  # Track the visibility of the popup

    def showPopup(self):
        if not self.popup_visible:
            super(CustomComboBox, self).showPopup()
            self.popup_visible = True

    def hidePopup(self):
        if self.popup_visible:
            super(CustomComboBox, self).hidePopup()
            self.popup_visible = False

    def togglePopup(self):
        if self.popup_visible:
            self.hidePopup()
        else:
            self.showPopup()

    def setCurrentText(self, text):
        self.line_edit.setText(text)  # 设置只读 QLineEdit 的文本值
        super(CustomComboBox, self).setCurrentText(text)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        combo = CustomComboBox(self)
        combo.addItem("Option 1")
        combo.addItem("Option 2")
        combo.addItem("Option 3")

        # 手动设置 QComboBox 的显示值
        combo.setCurrentText("Option 212313213")

        layout.addWidget(combo)
        self.setLayout(layout)

        self.setWindowTitle('Custom ComboBox')
        self.setGeometry(300, 300, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

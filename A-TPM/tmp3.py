import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QScreen, QAction, QCursor
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT


class CustomToolbar(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None):
        super(CustomToolbar, self).__init__(canvas, parent)

        # Set custom icons
        self._update_icons()

        # Add custom action
        self._add_custom_action()

    def _update_icons(self):
        icon_mapping = {
            'Home': 'path/to/your/custom/home.png',
            'Back': 'path/to/your/custom/back.png',
            'Forward': 'path/to/your/custom/forward.png',
            'Pan': 'path/to/your/custom/pan.png',
            'Zoom': 'path/to/your/custom/zoom.png',
            'Save': 'path/to/your/custom/save.png'
        }

        for action in self.actions():
            if action.text() in icon_mapping:
                action.setIcon(QIcon(icon_mapping[action.text()]))

    def _add_custom_action(self):
        # Create a custom action with an icon
        custom_action = QAction(QIcon('path/to/your/custom/icon.png'), 'Custom Action', self)
        custom_action.triggered.connect(self.custom_function)
        self.addAction(custom_action)
        self.insertAction(self.actions()[0], custom_action)  # Insert at the beginning

    def custom_function(self):
        print("Custom action triggered!")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Custom Toolbar Example')
        self.setFixedSize(800, 600)  # Prevent window resizing

        fig, ax = plt.subplots()
        ax.plot([0, 1, 2], [0, 1, 0])

        # Use tight layout
        fig.tight_layout()

        canvas = FigureCanvas(fig)

        # Create a central widget and a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add the canvas and the toolbar to the layout
        layout.addWidget(canvas)

        toolbar = CustomToolbar(canvas, self)
        layout.addWidget(toolbar)  # Add toolbar to the bottom by adding it after the canvas

        # Move window to the center of the current screen
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2
            self.move(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

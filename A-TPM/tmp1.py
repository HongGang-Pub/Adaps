import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.image = None  # Store reference to the image object
        self.annotation = None
        self.texts = []  # List to store text objects

    def plot_image(self, data, xlim=None, ylim=None, title=None, xlabel=None, ylabel=None, annotation=None,
                   text_annotations=None, x_tick_interval=1):
        if self.image is None:
            # First time plotting, create the image
            self.image = self.axes.imshow(data, cmap='viridis')
        else:
            # Update the existing image data
            self.image.set_data(data)
            self.image.set_extent([0, data.shape[1], 0, data.shape[0]])

        # Adjust the aspect ratio and limits based on the image size
        self.axes.set_aspect('auto')  # Set the aspect ratio to auto to accommodate different image sizes
        self.axes.relim()  # Recompute the limits based on the new data
        self.axes.autoscale_view()  # Automatically scale the view to fit the new limits

        # Set the x-axis tick interval
        self.axes.xaxis.set_major_locator(MultipleLocator(x_tick_interval))

        # Set the limits if provided
        if xlim is not None:
            self.axes.set_xlim(xlim)
        if ylim is not None:
            self.axes.set_ylim(ylim)

        # Update the title
        if title is not None:
            self.axes.set_title(title)

        # Update axis labels
        if xlabel is not None:
            self.axes.set_xlabel(xlabel)
        if ylabel is not None:
            self.axes.set_ylabel(ylabel)

        # Update or add an annotation with an arrow
        if annotation is not None:
            if self.annotation is not None:
                # Remove the previous annotation
                self.annotation.remove()
            self.annotation = self.axes.annotate(
                annotation['text'],
                xy=annotation['xy'],
                xytext=annotation['xytext'],
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5)  # Arrow properties
            )

        # Clear previous text annotations
        for text in self.texts:
            text.remove()
        self.texts.clear()

        # Add new text annotations
        if text_annotations is not None:
            for text_annotation in text_annotations:
                text_obj = self.axes.text(
                    text_annotation['x'],
                    text_annotation['y'],
                    text_annotation['text'],
                    fontsize=text_annotation.get('fontsize', 12),
                    color=text_annotation.get('color', 'white')
                )
                self.texts.append(text_obj)

        self.draw()  # Redraw the canvas

    def clear_image(self):
        self.axes.clear()  # Clear the axes
        self.image = None  # Reset the image reference
        self.annotation = None  # Reset the annotation reference

        # Clear all text annotations
        for text in self.texts:
            text.remove()
        self.texts.clear()

        self.draw()  # Redraw the canvas


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Initial image plot
        initial_data = np.random.rand(10, 10)
        self.canvas.plot_image(
            initial_data,
            title="Initial Plot",
            xlabel="X Axis",
            ylabel="Y Axis",
            annotation={"text": "Start", "xy": (2, 2), "xytext": (4, 4)},
            text_annotations=[
                {"x": 1, "y": 1, "text": "Point A", "fontsize": 10, "color": "yellow"},
                {"x": 7, "y": 8, "text": "Point B", "fontsize": 10, "color": "yellow"}
            ],
            x_tick_interval=2  # Set x-axis tick interval to 2
        )

        # Button to update the image
        self.update_button = QPushButton("Update Image")
        self.update_button.clicked.connect(self.update_image)

        # Button to clear the image
        self.clear_button = QPushButton("Clear Image")
        self.clear_button.clicked.connect(self.clear_image)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.update_button)
        layout.addWidget(self.clear_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setWindowTitle("Matplotlib imshow with PySide6")
        self.show()

    def update_image(self):
        new_data = np.random.rand(15, 20)  # Different size image
        self.canvas.plot_image(
            new_data,
            xlim=[0, 19],
            ylim=[0, 14],
            title="Updated Plot",
            xlabel="Updated X Axis",
            ylabel="Updated Y Axis",
            annotation={"text": "Updated Point", "xy": (10, 7), "xytext": (15, 10)},
            text_annotations=[
                {"x": 2, "y": 3, "text": "Updated A", "fontsize": 12, "color": "red"},
                {"x": 12, "y": 8, "text": "Updated B", "fontsize": 12, "color": "red"}
            ],
            x_tick_interval=5  # Set x-axis tick interval to 5 for the updated image
        )

    def clear_image(self):
        self.canvas.clear_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

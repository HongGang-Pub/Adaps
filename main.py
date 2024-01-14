from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from qdarkstyle import LightPalette
from qt_material import apply_stylesheet
import qdarkstyle
import os
# os.environ["QT_FONT_DPI"] = "96"
class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(r'C:\Users\hongg\Documents\VsCode\TMP\GUI\PyOneDark_Qt_Widgets_Modern_GUI\gui\uis\pages\main_pages.ui')
        # self.ui = QUiLoader().load(r'Hawk/HawkGUI/.file/Hawk.ui')

        # self.ui.button.clicked.connect(self.handleCalc)
        print(self.ui.V_ROLL_NUM_Label.font())
    def handleCalc(self):
        return


app = QApplication([])
# apply_stylesheet(app, theme='light_purple.xml')

# val = qdarkstyle.load_stylesheet(qt_api='pyside6')
# # setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette()))
# print(qdarkstyle.load_stylesheet(qt_api='pyside6'))
print(os.environ)

stats = Stats()
stats.ui.show()
app.exec()

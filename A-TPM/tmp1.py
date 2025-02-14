from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon


app = QApplication([])

# 创建 QListWidget
list_widget = QListWidget()

# 添加带图标的 item
for i in range(5):
    # 创建 QListWidgetItem
    item = QListWidgetItem(f"Item {i + 1}")

    # 设置图标（这里使用示例路径）
    icon = QIcon(r"D:\Git\Adaps\AdapsChip\ChipUI\gui\images\svg_icons\icon_file.svg")  # 替换为你的图标路径
    item.setIcon(icon)

    # 将 item 添加到 QListWidget
    list_widget.addItem(item)

# 显示 QListWidget
list_widget.show()

app.exec()

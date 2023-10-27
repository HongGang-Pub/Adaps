import tkinter

# _Relief: TypeAlias = Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]  # manual page: Tk_GetRelief

Lable_style = {
    "anchor": "w",
    "width": 15,
    "relief": 'ridge'
}
Lable_grid = {
    "padx": 3,
    "pady": 2,
    "ipady": 3,
    "sticky": "w"
}

Scale_style = {
    "resolution": 1,  # 设置 Scale 组件的分辨率（每点击一下移动的步长）
    "length": 180,
    "bg": "#ffffff",  # 组件背景样式
    "relief": "flat",  # 组件边框样式
    "borderwidth": 1,
    "highlightbackground": "#ffffff",  # 外边框颜色
    "troughcolor": "#d7d5d4",  # 滑轨颜色
    "width": 10,  # 滑轨宽度
    "sliderlength": 13,  # 设置滑块长度
    "sliderrelief": "ridge",
    "activebackground": "black",  # 滑块点按时颜色
    # tickinterval=8,             # 设置刻度滑动条的间隔
    "orient": tkinter.HORIZONTAL  # 设置Scale控件平方向显示
}

Scale_grid = {
    "padx": 3,
    "pady": 3,
    "ipady": 0,
    "sticky": 'W'
}

Entry_style = {
    "width": 30,
    # "bd": 1,
    "relief": "solid"
}

Entry_grid = {
    "padx": 3,
    "pady": 2,
    "ipady": 3,
    "sticky": 'W'
}

Button_style = {
    "width": 12,
    "relief": "raised"
}

Button_grid = {
    'columnspan': 1,
    'sticky': "w",
    'padx': 5,
    'pady': 3,
    "ipady": 0
}

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("输入框数字限定")
win.geometry("300x150")

# 创建 Entry 框
entry = tk.Entry(win, width=20)
entry.pack(pady=20)

# 创建按钮
button = tk.Button(win, text="确定", command=lambda: tk.messagebox.showinfo("提示", f"您输入的数字为：{entry.get()}"))
button.pack()

# 绑定 Entry 框的键盘事件
def validate_input(event):
    # 获取当前输入框中实时的文本内容
    content = entry.get()

    # 判断用户按下的键是否是数字或允许的字符（如退格键）
    if event.char.isdigit() or event.char == '\b':
        # 如果是数字或允许的字符，则继续输入
        pass
    else:
        # 如果不是数字或允许的字符，则禁止输入并弹出提示框
        check_input(content)
        return "break"

entry.bind("<Key>", validate_input)

# 检查输入的是否数字
def check_input(content):
    # 这里的 content 是输入框中实时的文本内容
    if not content.isdigit():
        # 如果输入的不是数字，则删除最后一个字符并弹出提示框
        entry.delete(len(content) - 1, tk.END)
        tk.messagebox.showwarning("警告", "请输入数字！")

win.mainloop()
import os
import openpyxl
from tkinter import messagebox


def save_excel(fname: str, sheet_name: str, data_list: list, fd_path: str, note: str = None) -> str:
    """
    根据用户要求保存文件

    Args:
        fname(str): filename
        sheet_name(str): sheet name(如果指定的文件中存在同名的sheet_name，会删除后重新写入)
        data_list(list): 存储的信息内容
        fd_path(str): 文件存储路径，若指定文件夹不存在，则创建。若不指定，则默认为当前文件夹
        note(str): 便签，不为None时，打印日志 & 文件路径；否则不打印

    Returns:
        str: 返回保存的文件路径
    """

    file = "{}\\{}.xlsx".format(fd_path, fname)
    if not os.path.exists(fd_path):
        # 目录不存在，进行创建操作
        os.makedirs(fd_path)
    if os.path.exists(file):
        while state:
            try:
                workbook = openpyxl.load_workbook(file)
                break
            except BaseException as msg:
                state = messagebox.askretrycancel('弹窗', '文件无法读取，请关闭文件后再试?\n{}'.format(msg))
        # os.remove(fd_path)
        if not state:
            return
    else:
        workbook = openpyxl.Workbook()
        # sheet = workbook.active
        # sheet.title = 'SpadArray_{}'.format(coeff)
    if sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        workbook.remove(sheet)

    sheet = workbook.create_sheet(sheet_name, 0)
    for row in data_list:
        sheet.append(row)
    # alignment = openpyxl.styles.Alignment(horizontal="center", vertical="center", text_rotation=0, wrap_text=True)
    # cell = sheet["A1"]
    # cell.alignment = alignment
    # sheet["A1"].font = f1
    # sheet["A1"].fill = fill1

    while state:
        try:
            workbook.save(file)
            break
        except BaseException as msg:
            state = messagebox.askretrycancel('弹窗', '文件无法读取，请关闭文件后再试?\n{}'.format(msg))
    # os.remove(fd_path)
    if not state:
        return

    if note:
        print("{}，文件路径为:  {}".format(note, file))
    return file

    # data_statistics.append("{:>3}\t{:>3}".format(r, c))
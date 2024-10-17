import os
import re
import json


def ReadJsonFile(file):
    """ 获取 Json文件 """
    with open(file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except BaseException as msg:
            raise ValueError(f"The Json file does not exist or the Json format is incorrect! Log: {msg}")


def get_fp(fd_path: str, mode: int, match_filter: str, regression: int = 0, f_type: str = "No Define") -> list:
    """
    根据用户自定义的过滤条件，获取指定文件夹下所有符合过滤条件的文件

    Args:
        regression (int): 是否迭代获取当前目录下所有文件夹：0：仅查找当前目录；1：当前目录以及所有子目录
        fd_path(str): Folder_path
        mode(int): 0:根据文件名进行匹配; 1:根据文件类型进行匹配，如：.txt, .doc等
        match_filter(str): 需要匹配的文件名或则文件类型
        f_type(str): 指定获取文件类型，便于error时打印日志

    Returns:
        list: 返回指定路径下满足过滤条件的所有文件的绝对路径
    """

    file_list = []
    if not os.path.exists(fd_path):
        # log = "指定的文件夹不存在，请检查参数: fd_path"
        # print(log)
        # return file_list
        raise ValueError("[{}] 指定的文件夹不存在: {}".format(f_type, fd_path))

    # os.walk()
    if regression == 0:
        files_list = os.listdir(fd_path)
        for file in files_list:
            if re.search(match_filter, os.path.splitext(file)[mode]):
                file_list.append("{}\\{}".format(fd_path, file))
    else:
        for root, dirs, files in os.walk(fd_path):
            for file in files:
                if re.search(match_filter, os.path.splitext(file)[mode]):
                    file_list.append("{}\\{}".format(root, file))
    return file_list


def data_save(fname: str,
              data_list: list,
              split: str = '\n',
              is_cover: int = 1,
              fd_path: str = '.',
              note: str = None
              ) -> str:
    """
    根据用户要求保存文件

    Args:
        fname(str): filename
        data_list(list): 存储的信息内容
        split(str): 列表保存时，元素与元素之间的分隔符。可为：无、空格、制表符、换行符等任意字符串
        is_cover(int): 文件写入方式：0：追加写入；1：覆盖写入
        fd_path(str): 文件存储路径，若指定文件夹不存在，则创建。若不指定，则默认为当前文件夹
        note(str): 便签，不为None时，打印日志 & 文件路径；否则不打印

    Returns:
        str: 返回保存的文件路径
    """
    fname = fname.strip()
    if fname == "":
        raise ValueError("File name empty.")

    if not data_list:
        raise ValueError("The content written is empty.")

    try:
        if not os.path.exists(fd_path):
            # 目录不存在，进行创建操作
            os.makedirs(fd_path)  # 使用os.makedirs()方法创建多层目录
        #     print("目录新建成功：" + fd_path)
        # else:
        #     print("文件存储目录: " + fd_path)
    except BaseException as msg:
        raise msg

    mode = "w" if is_cover == 1 else "a+"
    file = "{}\\{}".format(fd_path, fname)

    with open(file=file, mode=mode, encoding="utf-8") as f:
        for i in range(0, len(data_list)):
            f.write(str(data_list[i]))
            # if i < (len(data_list) - 1):
            f.write(split)
        if split != "\n":
            f.write("\n")
    if note:
        print("{}，The file path is: {}".format(note, file))
    return file


def read_file(fname: str) -> list:
    """
    获取文件内容

    Args:
        fname(str): file name
    Returns:
        list: 返回列表，若文件不存在，范围空列表
    """
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            data = f.readlines()
        return data
    except FileNotFoundError as msg:
        raise msg


# def save_excel(fname: str, sheet_name: str, data_list: list, fd_path: str, note: str = None) -> str:
#     """
#     根据用户要求保存文件
#
#     Args:
#         fname(str): filename
#         sheet_name(str): sheet name(如果指定的文件中存在同名的sheet_name，会删除后重新写入)
#         data_list(list): 存储的信息内容
#         fd_path(str): 文件存储路径，若指定文件夹不存在，则创建。若不指定，则默认为当前文件夹
#         note(str): 便签，不为None时，打印日志 & 文件路径；否则不打印
#
#     Returns:
#         str: 返回保存的文件路径
#     """
#
#     file = "{}\\{}.xlsx".format(fd_path, fname)
#     if not os.path.exists(fd_path):
#         # 目录不存在，进行创建操作
#         os.makedirs(fd_path)
#     if os.path.exists(file):
#         while state:
#             try:
#                 workbook = openpyxl.load_workbook(file)
#                 break
#             except BaseException as msg:
#                 state = messagebox.askretrycancel('弹窗', '文件无法读取，请关闭文件后再试?\n{}'.format(msg))
#         # os.remove(fd_path)
#         if not state:
#             return
#     else:
#         workbook = openpyxl.Workbook()
#         # sheet = workbook.active
#         # sheet.title = 'SpadArray_{}'.format(coeff)
#     if sheet_name in workbook.sheetnames:
#         sheet = workbook[sheet_name]
#         workbook.remove(sheet)
#
#     sheet = workbook.create_sheet(sheet_name, 0)
#     for row in data_list:
#         sheet.append(row)
#     # alignment = openpyxl.styles.Alignment(horizontal="center", vertical="center", text_rotation=0, wrap_text=True)
#     # cell = sheet["A1"]
#     # cell.alignment = alignment
#     # sheet["A1"].font = f1
#     # sheet["A1"].fill = fill1
#
#     while state:
#         try:
#             workbook.save(file)
#             break
#         except BaseException as msg:
#             state = messagebox.askretrycancel('弹窗', '文件无法读取，请关闭文件后再试?\n{}'.format(msg))
#     # os.remove(fd_path)
#     if not state:
#         return
#
#     if note:
#         print("{}，文件路径为： {}".format(note, file))
#     return file
#
#     # data_statistics.append("{:>3}\t{:>3}".format(r, c))


if __name__ == '__main__':
    # try:
    #     data_save(fname="eee", data_list=[23], split="\n", note="nihao", fd_path="")
    # except BaseException as msg:
    #     print(msg)
    # try:
    #     save_excel(fname="test", sheet_name="111", data_list=[(1, 2), [2, 3]], fd_path=".")
    # except BaseException as msg:
    #     print(msg)
    print("None")

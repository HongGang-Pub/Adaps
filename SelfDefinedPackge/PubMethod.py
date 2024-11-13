import logging
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

    # Note
    # name = os.path.basename(file_i)   # 文件名 (包含后缀) ps: file_i 为文件绝对路径
    # name_all = os.path.splitext(name) # 分割文件名和后缀
    # name_0 = name_all[0]              # 或者文件名
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
            # if index < (len(data_list) - 1):
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


def gray2bin(n):
    """
    格雷码转换为二进制
    Args:
        n (int):

    Returns:
        str: str for binary
    """
    # n = int(n, 2)
    mask = n
    while mask:
        mask >>= 1
        n ^= mask
    return bin(n)[2:].zfill(4)


def hex_regex_str(bit_width=4):
    repeat_times = bit_width // 4
    regex_str = "[0-9A-Fa-f]{{0,{}}}".format(repeat_times)

    if bit_width % 4 != 0:
        _mod = bit_width % 4
        _str = f"[0-{(2 ** _mod) - 1}]"
        regex_str = f"({_str}{regex_str})|({regex_str})"
    return regex_str


def get_ordinal(n: int) -> str:
    # 打印序数词: Ordinal Numbers
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"


def invoking_function(DEBUG: bool, func) -> None:
    """
    是否将异常信息进行包裹
    Args:
        DEBUG (bool): DEBUG 情况下, 直接在终端打印信息
        func (函数): 调用函数

    Returns:
        None
    """
    if DEBUG is True:
        func()
    else:
        try:
            func()
        except Exception as e:
            logging.fatal(e)
    pass


if __name__ == '__main__':
    print("Hello world.")

"""
本文件主要通过读取软件存储的frame_id信息, 并check MIPI是否丢包

支持场景：
1)非多帧合一丢帧判断，多帧合一丢 sub帧 & 图像帧判断;
2)Function >>> frame_id_chk();

Frame_id获取方法：
1)见 Function >>> get_frame_id(), 本方法只对一行内容进行解析，获取frame_id;
2)若文件存储内容/格式发生改变，可仅修改此方法，确保返回的只为frame_id即可;
"""

from SelfDefinedPackge import PubMethod
import re


def get_frame_id(data):
    try:
        # frame_id = int(cali_data.split(" ")[-1].strip())
        __data__ = re.split("[,:]", data)
        frame_id = int(__data__[-5].strip())
        return frame_id
    except BaseException as msg:
        raise msg


def frame_id_chk(file_list, tx_frame_mode=0, roll_num=32):
    """
    读取frame_id判断MIPI是否丢包，并计算丢包率

    Args:
        file_list (list): 需要读取frame_id的文件列表
        tx_frame_mode (int): 是否多帧合一。0：否; 1 or others：是
        roll_num (int): 多帧合一时，每个image帧存在多少sub帧

    Returns:
        None: 无返回值
    """
    frame_id_list = []
    err_cnt = 0
    pkg_num = 0
    imag_num = 0
    for file in file_list:
        # with open(file, 'r', encoding='utf-8') as f_name:
        #     frame_id_datas = f_name.readlines()
        frame_id_datas = PubMethod.read_file(fname=file)
        if len(frame_id_datas) == 0:
            raise ValueError("[Param] 读取的文件内容为空，请检查。")

        for frame_id_data in frame_id_datas:
            pkg_num += 1
            try:
                frame_id = get_frame_id(frame_id_data)
            except BaseException as msg:
                print(msg)
                raise ValueError("获取frame_id失败。\n\t[file]：{}\n\t[cali_data]: {}".format(file, frame_id_data))

            if tx_frame_mode == 0:
                if pkg_num > 1 and pre_frame_id + 1 != frame_id:
                    print("FILE:{}: \033[1;31;40mLoss package: {} -> {}\033[0m".format(file, pre_frame_id, frame_id))
                    err_cnt += 1
                    pre_frame_id = -1 if frame_id == 65535 else frame_id
                else:
                    pre_frame_id = -1 if frame_id == 65535 else frame_id
            else:
                if pkg_num == 1:
                    pre_frame_id = frame_id

                if frame_id != pre_frame_id:
                    imag_num += 1
                    if imag_num > 1 and len(frame_id_list) != roll_num:
                        loss_pkg = roll_num - len(frame_id_list)
                        print("FILE:{}: \033[1;31;40mLoss img_pkg: {}: {}\033[0m".format(file, frame_id, loss_pkg))
                        err_cnt += loss_pkg

                    if pre_frame_id + 1 != frame_id:
                        print(
                            "FILE:{}: \033[1;31;40mLoss package: {} -> {}\033[0m".format(file, pre_frame_id, frame_id))
                        err_cnt += 1
                    pre_frame_id = -1 if frame_id == 65535 else frame_id
                    frame_id_list = []
                frame_id_list.append(frame_id)
                # else:
                #     pre_frame_id = -1 if frame_id == 65535 else frame_id
    print("imag_num: {}, pkg_num: {}, error_num: {}, Persent: {:.4}".format(imag_num, pkg_num, err_cnt,
                                                                            err_cnt / pkg_num))


def do_work():
    # 通过Function: get_fp()获取存储的frame_id的所有文件
    file_collect = PubMethod.get_fp(fd_path=r"D:\Software\DothinkTester",
                                    mode=0,
                                    match_filter="frame_info_log",
                                    f_type="frame_id_file")

    frame_id_chk(file_collect, tx_frame_mode=0)


if __name__ == '__main__':
    do_work()

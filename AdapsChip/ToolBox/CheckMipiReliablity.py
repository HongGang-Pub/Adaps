from AdapsChip.Hawk01 import Hawk01MipiPubMethod, Hawk01PubMethod


def do_work():
    file_dict = Hawk01PubMethod.GetMipiFile(fd_path=file_path)
    if not Hawk01MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=386):
        return
    else:
        print("检查完成！！！")


if __name__ == '__main__':
    file_path = r"D:\Program Files\Software\DothinkTester\MipiData"
    do_work()

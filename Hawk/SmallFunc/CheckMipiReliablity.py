from SelfDefinedPackge import PubMethod
from Hawk.Common import HawkPubMethod
from Hawk.Common import MipiPubMethod
import numpy as np
import os


def do_work():
    file_dict = HawkPubMethod.GetMipiFile(fd_path=file_path)
    if not MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=386):
        return
    else:
        print("检查完成！！！")


if __name__ == '__main__':
    file_path = r"D:\Program Files\Software\DothinkTester\MipiData"
    do_work()

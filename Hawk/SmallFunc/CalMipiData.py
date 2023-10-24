import numpy as np
from SelfDefinedPackge import ArrayPubMethod
from Hawk.Common import HawkPubMethod
from Hawk.Common import MipiPubMethod
from Hawk.MSKU import MskuPubMethod
from Hawk.PCM import PcmPubMethod


def do_work():
    # 获取寄存器配置
    csru_cfg = HawkPubMethod.GetCsruConfig(script_file, sramdata_path)

    wc = MipiPubMethod.cal_wc(csru_cfg)
    pkg_num = MipiPubMethod.cal_pkg_num(csru_cfg)
    print(wc, pkg_num)


if __name__ == '__main__':
    script_file = r"D:\Software\DothinkTester\Script\250mhz\test_ptm_fhr_2d_scan.txt"
    sramdata_path = r"D:\Software\DothinkTester\SramData"

    do_work()

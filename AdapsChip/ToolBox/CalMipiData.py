import AdapsChip.Hawk01.HawkPubMethod
import AdapsChip.Hawk01.MipiPubMethod


def do_work():
    # 获取寄存器配置
    csru_cfg = AdapsChip.Hawk01.MipiPubMethod.GetCsruAndROIConfig(script_file, sramdata_path)

    wc, flnr = AdapsChip.Hawk01.HawkPubMethod.CalMipiFlnrAndWC(csru_cfg)
    pkg_num = AdapsChip.Hawk01.HawkPubMethod.CalPkgNum(csru_cfg)
    print(wc, pkg_num)


if __name__ == '__main__':
    script_file = r"D:\Software\DothinkTester\Script\250mhz\test_ptm_fhr_2d_scan.txt"
    sramdata_path = r"D:\Software\DothinkTester\SramData"

    do_work()

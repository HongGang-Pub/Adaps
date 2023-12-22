import numpy as np

import Hawk.Common.MipiPubMethod
from SelfDefinedPackge import ArrayPubMethod
from Hawk.Common import HawkPubMethod
from Hawk.MSKU import MskuPubMethod
from Hawk.PCM import PcmPubMethod


def do_work(mipi_file, script_file, sramdata_path):
    # 获取寄存器配置
    csru_cfg = Hawk.Common.MipiPubMethod.GetCsruAndROIConfig(script_file, sramdata_path)

    # 获取 msku roi信息
    zone_roi_mem, msku_roi_mem = MskuPubMethod.ParseRoiMem(csru_cfg)

    # 获取 pcm spad arrays
    array, spad_data = PcmPubMethod.GetPcmDataFromDothinker(file_path=mipi_file,
                                                            cfg=csru_cfg,
                                                            msku_roi_mem=msku_roi_mem)

    # 成图展示 PCM 灰度图
    # ArrayImageSave(fname="arrays", fd_path="figs")
    title = "Image: max_bin:{}, min_bin:{}, median_bin:{}".format(
                    np.max(spad_data), np.min(spad_data), np.median(spad_data))

    ArrayPubMethod.ArrayImage(array_lst=[array], title_list=[title])


if __name__ == '__main__':
    mipi_file = r"C:\Users\honggang.li\Downloads\MipiData_shift2spad"
    # config_file=r"D:\Software\DothinkTester\Script\PCM.txt",
    script_file = r"C:\Users\honggang.li\Downloads\tmp\test_pcm_full_330mhz_adaps.txt"
    sramdata_path = r"C:\Users\honggang.li\Downloads\tmp"

    do_work(mipi_file, script_file, sramdata_path)

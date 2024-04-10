import os

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
    name = os.path.basename(script_file)   # 文件名 (包含后缀) ps: file_i 为文件绝对路径
    title = os.path.splitext(name)[0] # 分割文件名和后缀

    ArrayPubMethod.ArrayImage(array_lst=[array], title_list=[title], vmin=0, vmax=1)


if __name__ == '__main__':
    mipi_file = r"D:\Program Files\Software\DothinkTester\MipiData_darklight_masking_18_3"
    # config_file=r"D:\Software\DothinkTester\Script\PCM.txt",
    script_file = r"D:\Program Files\Software\DothinkTester\Script\PCMLightAnalysis\test_pcm_masking_18_3.txt"
    sramdata_path = r"D:\Program Files\Software\DothinkTester\SramData"

    do_work(mipi_file, script_file, sramdata_path)

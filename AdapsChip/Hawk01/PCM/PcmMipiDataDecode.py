import os

from AdapsChip.Hawk01 import Hawk01MipiPubMethod
from SelfDefinedPackge import ArrayPubMethod, LogerPubMethod
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from AdapsChip.Hawk01.PCM import PcmPubMethod


def get_pcm_array(script_file, mipi_file, sramdata_path):
    # 获取寄存器配置
    hawk01_config = Hawk01MipiPubMethod.GetCsruAndROIConfig(script_file, sramdata_path)

    # 获取 msku roi信息
    zone_roi_mem, msku_roi_mem = MskuPubMethod.ParseRoiMem(hawk01_config)

    # 获取 pcm spad arrays
    array, spad_data = PcmPubMethod.GetPcmDataFromDothinker(file_path=mipi_file,
                                                            hawk01_config=hawk01_config,
                                                            msku_roi_mem=msku_roi_mem)
    return array


def do_work(mipi_file, script_file, sramdata_path, vmin=0, vmax=100):
    array = get_pcm_array(mipi_file=mipi_file, script_file=script_file, sramdata_path=sramdata_path)

    # 成图展示 PCM 灰度图
    # ArrayImageSave(fname="arrays", fd_path="figs")
    name = os.path.basename(mipi_file)  # 文件名 (包含后缀) ps: file_i 为文件绝对路径
    title = os.path.splitext(name)[0]  # 分割文件名和后缀
    ArrayPubMethod.ArrayImage(array_lst=[array], title_list=[title], vmin=vmin, vmax=vmax)


if __name__ == '__main__':
    LogerPubMethod.LoggingForConsoleFormat()

    script_file = r"D:\Program Files\Software\DothinkTester\Script\PCMDarkSpotAnalysis\test_pcm_masking_7Seg.txt"
    script_file = r"D:\Program Files\Software\DothinkTester\Script\Gray_Scale_Mode_reg_config.txt"
    mipi_file = r"D:\Program Files\Software\DothinkTester\MipiData"
    sramdata_path = r"D:\Program Files\Software\DothinkTester\SramData"

    do_work(mipi_file, script_file, sramdata_path)

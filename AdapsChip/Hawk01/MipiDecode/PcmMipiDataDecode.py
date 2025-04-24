import os

from AdapsChip.Hawk01 import Hawk01MipiPubMethod
from SelfDefinedPackge import ArrayPubMethod, LogerPubMethod
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from AdapsChip.Hawk01.MipiDecode import PcmPubMethod


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
    ArrayPubMethod.ArrayImage(array_lst=[array], title_list=None, vmin=vmin, vmax=vmax)


if __name__ == '__main__':
    LogerPubMethod.LoggingForConsoleFormat()

    script_f = r"D:\Program Files\Software\DothinkTester\Script\PCMLightAnalysis\test_pcm_spad_test_mode0.txt"
    mipi_fp = r"D:\Program Files\Software\DothinkTester\MipiData"
    sramdata_fp = r"D:\Program Files\Software\DothinkTester\SramData"
    do_work(mipi_file=mipi_fp,
            script_file=script_f,
            sramdata_path=sramdata_fp,
            vmin=600,
            vmax=700)


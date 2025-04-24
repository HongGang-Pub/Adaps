import numpy as np
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from SelfDefinedPackge import ArrayPubMethod
from AdapsChip.Hawk01.MipiDecode import PcmPubMethod, MipiDecodePubMethod
from AdapsChip.Hawk01 import Hawk01MipiPubMethod
from AdapsChip.Hawk01.MipiDecode.DarkSpotAnalysis import DarkSpotAnalysisPubMethod as DarkMethod


def do_work():
    data = {
        "chip_numbers": [],
        "axis1": {},
        "base_number": {},
        "coefficients": coeff_list,
    }
    # 获取寄存器配置
    hawk01_config = Hawk01MipiPubMethod.GetCsruAndROIConfig(script_file, sramdata_path)

    fd_path = "FHR_15(35)_OUT_EN"
    excel_name = r'{}\Spad分析.xlsx'.format(fd_path)

    # 获取 FHR 数据
    for spad_en_cnt in range(9):
        chip_number = "OUT_EN{}".format(spad_en_cnt)
        data["chip_numbers"].append(chip_number)
        data["axis1"][chip_number] = axis1

        hawk01_config["PXL_SPAD_OUT_EN"] = 1 << spad_en_cnt
        mipi_file = r"D:\Software\DothinkTester\MipiData_FHR_Shift35_3_EN{}".format(spad_en_cnt)

        zone_roi_mem, msku_roi_mem = MskuPubMethod.ParseRoiMem(hawk01_config, f_path=fd_path)
        _array, _spad_data = FhrPubMethod.GetFhrDataFromDothinker(file_path=mipi_file,
                                                                  hawk01_config=hawk01_config,
                                                                  msku_roi_mem=msku_roi_mem)

        array = _array
        spad_data = _spad_data

        # 获取黑点
        data[chip_number], data["base_number"][chip_number] = DarkMethod.data_process(array_lst=[array],
                                                                                      coefficient_list=coeff_list,
                                                                                      ref_array_idx=0,
                                                                                      ref_array_lst=[spad_data])

        title = "Image: max_bin:{}, min_bin:{}, median_bin:{}".format(
            np.max(spad_data), np.min(spad_data), np.median(spad_data))
        ArrayPubMethod.ArrayImage(array_lst=[array], title_list=[title], fd_path=fd_path, fname="PHR{}".format(spad_en_cnt))
        # ArrayPubMethod.ArrayImage(array_lst=[arrays], title_list=[title])
    DarkMethod.write_excel(data, excel_name)

    print("数据处理完成!!!")
    return


if __name__ == '__main__':
    chip_number = 'S04'
    axis1 = [1.11]
    coeff_list = [0.9]

    # config_file=r"D:\Software\DothinkTester\Script\PCM.txt",
    script_file = r"D:\Software\DothinkTester\Script\FHR_15(35)_OUT_EN.txt"
    sramdata_path = r"D:\Software\DothinkTester\SramData"

    do_work()

    # cmp_data(0.95, 1.12, cali_data)

import numpy as np
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from SelfDefinedPackge import ArrayPubMethod
from AdapsChip.Hawk01.PCM import PcmPubMethod
from AdapsChip.Hawk01.PCM.DarkSpotAnalysis import DarkSpotAnalysisPubMethod as DarkMethod


def do_work():
    data = {
        "chip_numbers": [],
        "axis1": {},
        "base_number": {},
        "coefficients": coeff_list,
    }
    # 获取寄存器配置
    csru_cfg = Hawk.Common.MipiPubMethod.GetCsruAndROIConfig(script_file, sramdata_path)

    # 获取 msku roi 数据

    # 获取 FHR 数据
    for spad_en_cnt in range(9):
        chip_number = "OUT_EN{}".format(spad_en_cnt)
        data["chip_numbers"].append(chip_number)
        data["axis1"][chip_number] = axis1

        csru_cfg["pxl_spad_out_en"] = 1 << spad_en_cnt
        mipi_file = r"D:\Software\DothinkTester\MipiData_FHR_Shift35_3_EN{}".format(spad_en_cnt)

        fd_path = "FHR_15(35)_OUT_EN"
        excel_name = r'{}\Spad分析.xlsx'.format(fd_path)
        print(mipi_file)

        zone_roi_mem, msku_roi_mem = MskuPubMethod.ParseRoiMem(csru_cfg, f_path=fd_path)
        _array, _spad_data = PcmPubMethod.GetFhrDataFromDothinker(file_path=mipi_file,
                                                                  cfg=csru_cfg,
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

    print("数据处理完成！！！")
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

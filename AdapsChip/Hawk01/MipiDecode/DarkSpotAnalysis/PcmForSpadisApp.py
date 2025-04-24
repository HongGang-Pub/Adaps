import os
from AdapsChip.Hawk01.MipiDecode import PcmPubMethod
from AdapsChip.Hawk01.MipiDecode.DarkSpotAnalysis import DarkSpotAnalysisPubMethod as DarkMethod


def do_work(fd_path: str, chip_numbers, axis1, coeff_list, ref_ax: float = 0, ):
    files_list = os.listdir(fd_path)

    axis1.sort()
    try:
        ref_array_index = axis1.index(ref_ax)
    except:
        ref_array_index = 0

    data = {
        "chip_numbers": [],
        "axis1": {},
        "base_number": {},
        "coefficients": coeff_list
    }

    for chip_number in chip_numbers:
        array_lists = []
        for ax1 in axis1:
            file_name = "{}_{:.2f}".format(chip_number, ax1)
            if file_name in files_list:
                if not chip_number in data["chip_numbers"]:
                    data["chip_numbers"].append(chip_number)
                    data["axis1"][chip_number] = []
                data["axis1"][chip_number].append(ax1)

                # 按照文件为单位读取数据
                fp = os.path.join(fd_path, file_name)

                print("处理PCM数据: ", fp)
                # 获取 PCM 数据
                _array_ = PcmPubMethod.GetPcmDataFromSpadisApp(fp, frame_number=1)

                array_lists.append(_array_)

        if len(array_lists) > 0:
            # 获取不同模组的黑点数据
            data[chip_number], data["base_number"][chip_number] = DarkMethod.data_process(array_lists,
                                                                                          coefficient_list=coeff_list,
                                                                                          ref_array_idx=ref_array_index)

        DarkMethod.write_excel(data, excel_name)
        print("数据处理完成!!!")
    return


if __name__ == '__main__':
    chip_number_list = ['S04', 'S16', 'S17', 'S19']
    sv11_voltage_list = [1.00, 1.05, 1.10, 1.12, 1.14, 1.16, 1.18, 1.21]
    # coeff_lst = [0.6, 0.7, 0.8, 0.9]
    coeff_lst = [0.6]

    excel_name = 'Spad分析_0.6.xlsx'

    do_work(fd_path=r"D:\Program Files\SpadisApp\InternalRelease_SpadisApp_02\SavedImages",
            chip_numbers=chip_number_list,
            coeff_list=coeff_lst,
            axis1=sv11_voltage_list,
            ref_ax=1.10)

    # cmp_data(0.95, 1.12, cali_data)

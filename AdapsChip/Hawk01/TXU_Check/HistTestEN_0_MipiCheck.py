"""
本文件主要用于hist_test_en=0情况下，对MIPI数据进行模糊匹配。主要思路是：同一验证环境下，抓取完整图像帧数据，然后抓取
单次rolling的数据。将其与图像帧对应rolling的数据进行比对。

具体使用方法见 Function >>> pcm_decode()
"""
from AdapsChip.Hawk01.TXU_Check import TxuPubMethod
from AdapsChip.Hawk01.TXU_Check.Config import *


def do_work(script_file: str, mipidata_path: str, subframe_script_file: str, subframe_mipidata_path: str,
            sramdata_path: str, threshold: int, protocol: str):
    """
    hist_test_en=0情况下，对图像帧和子帧（暂只支持一帧）数据进行模糊匹配

    Args:
        script_file (str): 图像帧的脚本路径，用于和子帧进行比较
        mipidata_path (str): 图像帧的MIPI数据路径，用于和子帧进行比较
        subframe_script_file (str): 子帧的脚本路径，用于和图像帧进行比较
        subframe_mipidata_path (str): 子帧的MIPI数据路径，用于和子帧进行比较
        sramdata_path (str): SRAMDATA file path
        threshold (int): 图像帧和子帧进行 bin_num 比较的阈值
        protocol (str): 通讯协议："i2c" or "spi"

    Returns:
        None: 无返回值
    """
    image_csru_config = Hawk.Common.MipiPubMethod.GetCsruAndROIConfig(script_file=script_file,
                                                                      sramdata_path=sramdata_path,
                                                                      protocol=protocol)
    # 获取image的frame信息，用于查找单次rolling时需要参考的数据
    image_info = TxuPubMethod.do_chk(cfg=image_csru_config, mipi_fd_path=mipidata_path, golden_fp_list=["NoCheck"],
                                     file_path=result_folder)
    if image_info['flag'] == 0:
        print("获取用于作为基准数据比对的MIPI数据获取错误！！！")
        print(image_info["log"])
        return

    # 获取当前rolling对应的v_rolling
    subframe_csru_config = Hawk.Common.MipiPubMethod.GetCsruAndROIConfig(script_file=subframe_script_file,
                                                                         sramdata_path=sramdata_path,
                                                                         protocol=protocol)

    roi_file = subframe_csru_config['roi_file']
    vroll_num = roi_file.split("_")[1]
    # vroll_num = 0
    golden_file_path_list = []
    for info in image_info['subframe_info']:
        # 找到与当前单次rolling相匹配的rolling数据用作golden数据(pcm找到hroll为0的数据，模糊匹配时，9次子帧使用自加1进行匹配)
        if info['vroll_num'] == vroll_num and info['hroll_num'] == 0:
            onesubframe_hrolling_times = 9 if subframe_csru_config['work_mode'] == 3 else 1
            for i in range(onesubframe_hrolling_times):
                if (info['file_index'] + i) in image_info['file'].keys():
                    # 如果有丢包情况，获取的file_index可能错误
                    golden_file_path_list.append(image_info['file'][info['file_index'] + i])
                else:
                    print("用于比对的基准文件缺失，请检查！！！\ngolden_file_path_list：\n{}".format(
                        golden_file_path_list))
                    return
            break  # 找到符合条件的数据后，结束循环

    if len(golden_file_path_list) != onesubframe_hrolling_times:
        # for循环中每找到对应数据时，需要return
        print("脚本路径: ", subframe_script_file)
        print("\033[1;31;40m寄存器配置信息：\n{}\033[0m".format(subframe_csru_config))
        print("没有从Image MIPI Data中找到 v_roll_num={} 的基准数据:\n\t{}".format(vroll_num,
                                                                                   image_info['subframe_info']))
        return

    # print("golden_file_path_list：\n{}".format(golden_file_path_list))

    cmp_answer = TxuPubMethod.do_chk(cfg=subframe_csru_config,
                                     mipi_fd_path=subframe_mipidata_path,
                                     golden_fp_list=golden_file_path_list,
                                     hist_testen=0,
                                     threshold=threshold,
                                     file_path=subframe_result_folder)

    print("脚本路径: ", subframe_script_file)
    print("\033[1;31;40m寄存器配置信息：\n{}\033[0m".format(subframe_csru_config))
    print(cmp_answer["log"])
    return


if __name__ == '__main__':
    # work_mode = 0
    # tc_name = "1D_base"
    # config_file=get_script_path(work_mode, tc_name)

    do_work(script_file=script_file,
            mipidata_path=mipi_file_path,
            subframe_script_file=subframe_script_file,
            subframe_mipidata_path=subframe_mipidata_path,
            sramdata_path=sram_data_path,
            threshold=10,
            protocol="i2c")

"""
本文件主要用于hist_test_en=1情况下，对MIPI数据进行精准匹配
具体使用方法见 Function >>> pcm_decode()
"""

from Hawk.Common import HawkPubMethod
from Hawk.TXU_Check import TxuPubMethod
from Hawk.TXU_Check.Config import *


def get_script_path(work_mode, tc_name):
    _script_path = "D:\\Program Files\\DothinkTester\\Script\\TXU_script"
    if work_mode == 3:
        script_file = "test_pcm\\test_pcm_{}.txt".format(tc_name)
    elif work_mode == 2:
        script_file = "test_ptm_fhr\\test_ptm_fhr_{}.txt".format(tc_name)
    elif work_mode == 1:
        script_file = "test_ptm_phr\\test_ptm_phr_{}.txt".format(tc_name)
    else:
        script_file = "test_ptm_sphr\\test_ptm_sphr_{}.txt".format(tc_name)
    return "{}\\{}".format(_script_path, script_file)


def get_golden_data_file(work_mode, out_bin_num):
    base_path = r"D:\OneDrive - 深圳市灵明光子科技有限公司\Program Files\DothinkTester\Script\TXU_script"
    if work_mode == 0:
        if out_bin_num == 0:
            _file = r"{}\{}".format(base_path, r"test_ptm_sphr\sphr_golden_data_out_bin0.txt")
        else:
            _file = r"{}\{}".format(base_path, r"test_ptm_sphr\sphr_golden_data_out_bin1.txt")
    elif work_mode == 1:
        if out_bin_num == 0:
            _file = r"{}\{}".format(base_path, r"test_ptm_phr\phr_golden_data_out_bin0.txt")
        else:
            _file = r"{}\{}".format(base_path, r"test_ptm_phr\phr_golden_data_out_bin1.txt")
    elif work_mode == 2:
        _file = r"{}\{}".format(base_path, r"test_ptm_fhr\fhr_golden_data.txt")
    elif work_mode == 3:
        _file = r"{}\{}".format(base_path, r"test_pcm\pcm_golden_data.txt")
    else:
        _file = "None golden file ..."
    return _file


def do_work(script_file: str, gld_data_path: str, sramdata_path: str, mipidata_path: str, protocol: str):
    """
    hist_test_en=1情况下，对mipi数据进行精准匹配

    Args:
        script_file (str): Hawk脚本路径
        gld_data_path (str): 基准比对数据
            >> 如果不进行MIPI数据比对，请输入："NoCheck"
            >> 如果为："None"，会通过get_golden_data_file()获取golden file path
        sramdata_path (str): SramData所在文件夹
        mipidata_path (str): MipiData所在文件夹
        protocol (str): 通信协议 i2c or spi

    Returns:
        None: 无返回值
    """

    csru_config = HawkPubMethod.GetCsruConfig(script_file=script_file,
                                              sramdata_path=sramdata_path,
                                              protocol=protocol)

    if gld_data_path == "None":
        golden_fp = get_golden_data_file(work_mode=csru_config["work_mode"], out_bin_num=csru_config["out_bin_num"])
    else:
        golden_fp = gld_data_path

    cmp_answer = TxuPubMethod.do_chk(cfg=csru_config, mipi_fd_path=mipidata_path, golden_fp_list=[golden_fp],
                                     file_path=result_folder)

    print("脚本路径: ", script_file)
    print("\033[1;31;40m寄存器配置信息：\n{}\033[0m".format(csru_config))
    print(cmp_answer["log"])
    return


if __name__ == '__main__':
    do_work(script_file=script_file,
            gld_data_path=golden_data_path,
            sramdata_path=sram_data_path,
            mipidata_path=mipi_file_path,
            protocol="i2c")

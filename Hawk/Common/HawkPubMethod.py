import numpy as np

from SelfDefinedPackge.PubMethod import *


def GetMipiFile(fd_path):
    """
    针对 Dothinker 获取MIPI文件，并按index生成字典，使能顺序读取文件进行数据比对

    Args:
        fd_path: MIPI Data folder dir
    Returns:
        dict: f_dict[key=index, value=mipidata_path]
    """

    file_list = get_fp(fd_path=fd_path, mode=1, match_filter=".txt", f_type="Get MIPI File")
    if len(file_list) == 0:
        raise ValueError("未从指定目录下获取到MIPI文件！！！")

    file_dict = {}
    file_index_list = []
    for index in range(len(file_list)):
        sublist_file = file_list[index].split("-")
        # 针对度信抓包MIPI文件命名格式：mipidata-index-xxxxxxxxx.txt，字典格式为：{index: mipidata_path}
        if len(sublist_file) >= 3:
            file_index = int(file_list[index].split("-")[-2])
            file_dict[file_index] = file_list[index]
            file_index_list.append(file_index)
        else:
            continue

    return file_dict


def GetCsruConfig(script_file, sramdata_path=None, protocol="i2c") -> dict:
    """
    根据 Hawk 寄存器配置脚本，获取寄存器配置信息

    Args:
        script_file (str): 脚本路径
        sramdata_path (str): SRAMDATA存储路径，用于生成 ROI 文件的路径
        protocol (str): i2c or spi

    Returns:
        dict: 寄存相关配置
    """
    addr_index = 2 if protocol == "i2c" else 1
    min_lens = 4 if protocol == "i2c" else 3
    block_write = "I2C_Block_Write" if protocol == "i2c" else "SPI_Block_Write"

    csru_cfg = {
        "tx_frame_mode": 0,
        "v_pxl_out_num": 1,
        "scan_mode": 0,
        "work_mode": 0,
        "v_roll_num": 31,
        "h_roll_num": 0,
        "h_vld_seg": 15,
        "maxbin_thrs": 167,
        "minbin_thrs": 0,
        "one_dt_mode": 0,
        "out_bin_num": 0,
        "seg_hs": 0,
        "h_seg_shift": 0,
        "pxl_spad_out_en": 0x1FF,
        "roi_file": ""
    }

    # try:
    #     with open(script_file, 'r', encoding='utf-8') as f_name:
    #         all_data = f_name.readlines()
    # except BaseException as msg:
    #     print("文件不存在，请重新配置路径！！！", msg)
    #     return cfg

    csru_datas = read_file(fname=script_file)

    if len(csru_datas) == 0:
        raise ValueError("[Param] 读取的寄存器配置文件为空，请检查。")

    # 初始化部分变量
    PXL_SPAD_OUT_EN_L = 0xFF
    PXL_SPAD_OUT_EN_H = 0x01

    for sub_data in csru_datas:
        configs = re.split(",|//", sub_data)

        """get_csru_config"""
        if len(configs) > min_lens:
            addr = configs[addr_index].strip()
            # sys_ctrl
            if addr == "0004":
                _sys_ctrl = configs[addr_index + 1].strip()[0:3]
                sys_ctrl = int(_sys_ctrl, 16)
                csru_cfg["tx_frame_mode"] = sys_ctrl // 128
                csru_cfg["v_pxl_out_num"] = sys_ctrl // 64 % 2
                csru_cfg["scan_mode"] = sys_ctrl % 16 // 8
                csru_cfg["work_mode"] = sys_ctrl % 8 // 2
            # v_roll_num
            if addr == "000D":
                _v_roll_num = configs[addr_index + 1].strip()[0:3]
                v_roll_num = int(_v_roll_num, 16)
                csru_cfg["v_roll_num"] = v_roll_num
            # hroll_num
            if addr == "000E":
                _h_roll_num = configs[addr_index + 1].strip()[0:3]
                hroll_num = int(_h_roll_num, 16)
                csru_cfg["h_roll_num"] = hroll_num % 16
                csru_cfg["h_vld_seg"] = hroll_num // 16
            # minbin_thrs
            if addr == "0016":
                _maxbin_thrs = configs[addr_index + 1].strip()[0:3]
                maxbin_thrs = int(_maxbin_thrs, 16)
                csru_cfg["maxbin_thrs"] = maxbin_thrs
            # minbin_thrs
            if addr == "0017":
                _minbin_thrs = configs[addr_index + 1].strip()[0:3]
                minbin_thrs = int(_minbin_thrs, 16)
                csru_cfg["minbin_thrs"] = minbin_thrs
            # txu_cfg
            if addr == "001C":
                _txu_cfg = configs[addr_index + 1].strip()[0:3]
                txu_cfg = int(_txu_cfg, 16)
                csru_cfg["one_dt_mode"] = txu_cfg % 2
            # depthu_cfg1
            if addr == "001F":
                _depthu_cfg1 = configs[addr_index + 1].strip()[0:3]
                depthu_cfg1 = int(_depthu_cfg1, 16)
                csru_cfg["out_bin_num"] = depthu_cfg1 // 16 % 2
            # SPAD_CFG1
            if addr == "0055":
                _spad_cfg1 = configs[addr_index + 1].strip()[0:3]
                spad_cfg1 = int(_spad_cfg1, 16)
                PXL_SPAD_OUT_EN_L = spad_cfg1
                csru_cfg["pxl_spad_out_en"] = PXL_SPAD_OUT_EN_H * 256 + PXL_SPAD_OUT_EN_L

            # SPAD_CFG2
            if addr == "0056":
                _spad_cfg2 = configs[addr_index + 1].strip()[0:3]
                spad_cfg2 = int(_spad_cfg2, 16)
                PXL_SPAD_OUT_EN_H = spad_cfg2 >> 7
                csru_cfg["pxl_spad_out_en"] = PXL_SPAD_OUT_EN_H * 256 + PXL_SPAD_OUT_EN_L

        # seg_hs, h_seg_shift
        if sramdata_path is not None and configs[0] == block_write and len(configs) == min_lens + 1:
            roi_name = configs[min_lens].strip()
            roi_file = "{}\\{}.txt".format(sramdata_path, roi_name)
            csru_cfg["roi_file"] = roi_file
            with open(roi_file, 'r', encoding='utf-8') as f1:
                roi_data = f1.readlines()
                seg_hs = int(roi_data[13], 16) // 1024
                csru_cfg["seg_hs"] = seg_hs
                if csru_cfg["scan_mode"] == 1:
                    h_seg_shift = int(roi_data[19], 16) // 1024 - seg_hs
                else:
                    h_seg_shift = 0
                csru_cfg["h_seg_shift"] = h_seg_shift
    print("\033[1;31;40m寄存器配置信息：\n{}\033[0m".format(csru_cfg))
    return csru_cfg


def SpadOutEn(spad_out_en):
    spad_en_list = []
    for i in range(9):
        EN = 1 if spad_out_en & (1 << i) > 0 else 0
        spad_en_list.append(EN)
    OutEN = [spad_en_list[0:3], spad_en_list[3:6], spad_en_list[6:9]]

    spad_out_en_array = np.array(OutEN)
    return spad_out_en_array

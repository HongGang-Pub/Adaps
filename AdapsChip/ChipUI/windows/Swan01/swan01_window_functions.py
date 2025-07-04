import copy
import os

from AdapsChip.Swan01 import Swan01PubMethod
from AdapsChip.Swan01.MSKU.MSKU_Cali.ROICalibration import ROICalibration
from AdapsChip.Swan01.MSKU.MSKU_GEN import ROIGenerate
from AdapsChip.Swan01.MSKU import MskuPubMethod
import gc
import logging
from SelfDefinedPackge import LogerPubMethod


def MskuRoiGenerateByJson(Swan01_config: dict) -> dict:
    """完全通过Json文件生成 MskuRoi"""
    roi_data_pkg = {}
    msku_roi_mem = ROIGenerate.MskuRoiGenerate(Swan01_config)
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem,
                                                                                                Swan01_config,
                                                                                                is_save=0)
    roi_data = RoiMemGenerate(msku_roi_mem, Swan01_config)
    roi_data_pkg["roi_gen_type"] = 0
    roi_data_pkg["img_types"] = ["Masking", "PCM Image", "PTM Image"]
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["pcm_array"] = pcm_array
    roi_data_pkg["ptm_array"] = ptm_array
    roi_data_pkg["masking_arrays"] = masking_arrays
    roi_data_pkg["masking_coor_info"] = masking_coor_info
    return roi_data_pkg


def MskuRoiGenerateByFile(Swan01_config: dict) -> dict:
    """通过手动的标定坐标生成ROI"""
    roi_data_pkg = {}
    file = Swan01_config["cali_file"]
    file_name, file_ext = os.path.splitext(file)
    if file_ext == ".txt":
        cali_data = MskuPubMethod.DirectAccessCaliDataByTXT(Swan01_config)
    elif file_ext in [".csv", ".xls", ".xlsx"]:  # csv
        cali_data = MskuPubMethod.DirectAccessCaliDataByExcel(Swan01_config)
    else:
        raise ValueError("Incorrect file format, not supported for parsing...")
    msku_roi_mem = ROICalibration.MskuRoiGenerate(Swan01_cfg=Swan01_config, cali_data=cali_data)
    roi_data = RoiMemGenerate(msku_roi_mem, Swan01_config)
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem,
                                                                                                Swan01_config,
                                                                                                is_save=0)
    roi_data_pkg["roi_gen_type"] = 1
    roi_data_pkg["img_types"] = ["Masking", "PCM Image", "PTM Image"]
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["pcm_array"] = pcm_array
    roi_data_pkg["ptm_array"] = ptm_array
    roi_data_pkg["masking_arrays"] = masking_arrays
    roi_data_pkg["masking_coor_info"] = masking_coor_info
    gc.collect()
    return roi_data_pkg


def MskuRoiGenerateByROIMEM(Swan01_config: dict) -> dict:
    roi_file = Swan01_config["roi_file"]
    start_roll = Swan01_config["start_roll"]
    end_roll = Swan01_config["end_roll"]

    roi_data = []
    roi_data_pkg = {}
    zone_roi_mem, msku_roi_mem = MskuPubMethod.ParseRoiMem(Swan01_config, roi_file)
    for vroll_cnt in range(start_roll, end_roll + 1):
        per_zone_mem = zone_roi_mem[vroll_cnt] + msku_roi_mem[vroll_cnt]
        roi_data = roi_data + per_zone_mem
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem,
                                                                                                Swan01_config,
                                                                                                is_save=0)
    roi_data_pkg["roi_gen_type"] = 2
    roi_data_pkg["img_types"] = ["Masking", "PCM Image", "PTM Image"]
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["pcm_array"] = pcm_array
    roi_data_pkg["ptm_array"] = ptm_array
    roi_data_pkg["masking_arrays"] = masking_arrays
    roi_data_pkg["masking_coor_info"] = masking_coor_info
    return roi_data_pkg


# @profile
def MskuRoiGenerateByCali(Swan01_config: dict) -> dict:
    """通过直接标定PCM图片生成ROI"""
    roi_data_pkg = {}
    cali_run = ROICalibration()
    cali_data, light_imags = cali_run.GetCaliDataFromPCMImage(Swan01_config)
    msku_roi_mem = ROICalibration.MskuRoiGenerate(Swan01_cfg=Swan01_config, cali_data=cali_data)
    roi_data = RoiMemGenerate(msku_roi_mem, Swan01_config)
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem,
                                                                                                Swan01_config)
    masking_arrays, cali_fusion_image, fusion_image_cali_3D_image = cali_run.CaliResultDisplay(cali_data, light_imags,
                                                                                               Swan01_config, is_save=0)
    roi_data_pkg["roi_gen_type"] = 3
    roi_data_pkg["img_types"] = ["Masking", "PCM Image", "PTM Image", "Cali fusion Image"]
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["pcm_array"] = pcm_array
    roi_data_pkg["ptm_array"] = ptm_array
    roi_data_pkg["cali_fusion_image"] = cali_fusion_image
    roi_data_pkg["masking_arrays"] = masking_arrays
    roi_data_pkg["masking_coor_info"] = masking_coor_info
    del cali_run
    return roi_data_pkg


def RoiMemGenerate(msku_roi_mem, cfg):
    roi_data = []
    try:
        zones_config = MskuPubMethod.ZonesConfigGenerate(cfg=cfg)
    except BaseException as msg:
        raise msg

    for vroll_cnt in range(len(msku_roi_mem)):
        per_zone_mem = zones_config[vroll_cnt] + msku_roi_mem[vroll_cnt]
        roi_data = roi_data + per_zone_mem
    return roi_data


def ROIDataPackageSave(roi_data_pkg, Swan01_config, save_sel=0, roi_data_format=1):
    """
    保存ROI数据: 包含图片、ROI数据
    Args:
        roi_data_pkg (dict): 包含生成ROI的所有必要信息
        Swan01_config (dict): Swan 配置集合
        save_sel (int): 0: 仅保存ROI数据,1: 保存ROI数据和图片数据
        roi_data_format (int): ROI存储格式: 0: byte对齐, 1: half-word对齐

    Returns:

    """
    MskuPubMethod.roi_data_save(f_name=Swan01_config["roi_name"], data=roi_data_pkg["roi_data"],
                                fd_path=Swan01_config["fd_path"],
                                roi_data_format=roi_data_format)
    url = f'{Swan01_config["fd_path"]}/{Swan01_config["roi_name"]}.txt'
    _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
    info = f"ROI data has been save to {_hyper_link}"
    print(info)

    if save_sel == 0:
        return

    # ROI masking数据效果保存
    # /////////////////////////////////////////////////
    img_fp = f'{Swan01_config["fd_path"]}/image'

    canvas = Swan01MaskingDynamicFig(roi_data_pkg)
    canvas.roi_img_save(img_fp=img_fp)

    # 释放内存
    canvas.roi_data_pkg = None
    canvas = None
    gc.collect()

    url = f'{img_fp}'
    _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
    info = f"Image data has been save to {_hyper_link}"
    print(info)
    return


def ScriptDataSave(swan01_config):
    """
    根据配置生成Swan01配置脚本
        swan01_config (dict): Swan 配置集合
    """
    __swan01_config__ = copy.deepcopy(swan01_config)
    # __reg_cfg__ = copy.deepcopy(reg_cfg)
    # print(__swan01_config__)
    work_mode_q = swan01_config["WORK_MODE"]

    def traverse_dict(d, parent_key=''):
        for key, value in d.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                traverse_dict(value, full_key)
            else:
                try:
                    d[key] = eval(value)
                except:
                    pass

    # traverse_dict(d=__reg_cfg__, parent_key='')     # 将reg_config的配置值全部转换为数字类型

    for work_mode in work_mode_q:
        __swan01_config__["WORK_MODE"] = work_mode
        __swan01_config__["reg_name"] = swan01_config["reg_name"] if len(work_mode_q) == 0 \
            else f'SPHR_{swan01_config["reg_name"]}' if work_mode == 0 \
            else f'PHR_{swan01_config["reg_name"]}' if work_mode == 1 \
            else f'FHR_{swan01_config["reg_name"]}' if work_mode == 2 \
            else f'PCM_{swan01_config["reg_name"]}'  # if work_mode == 3 \
        Swan01PubMethod.GenerateSwanRegConfig(swan01_config=__swan01_config__,
                                              reg_cfg_fp=__swan01_config__["Swan01RegConfigFile"])
        # Swan01PubMethod.GenerateSwanRegConfigByJson(swan01_config=__swan01_config__, reg_cfg=__reg_cfg__)
        url = f'{__swan01_config__["fd_path"]}/{__swan01_config__["reg_name"]}.txt'
        _hyper_link = LogerPubMethod.create_file_hyperlink(url=url)
        info = f"Script data has been save to {_hyper_link}"
        print(info)


def ScriptParse(swan01_config, file):
    Swan01PubMethod.ParseSwanRegConfig(file, swan01_config["protocol"])

import copy

from AdapsChip.Hawk01.Common import HawkPubMethod
from AdapsChip.Hawk01.MSKU.MSKU_Cali.ROICalibration import ROICalibration
from AdapsChip.Hawk01.MSKU.MSKU_GEN import ROIGenerate
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from AdapsChip.ChipUI.windows.Hawk01Function.MaskingDisplayUI import Hawk01MaskingDynamicFig
import gc
import matplotlib.pyplot as plt
from SelfDefinedPackge import ArrayPubMethod
from matplotlib.pyplot import MultipleLocator
import logging
from SelfDefinedPackge import LogerPubMethod, MatplotExtension


def MskuRoiGenerateByJson(cfg: dict) -> dict:
    """完全通过Json文件生成 MskuRoi"""
    roi_data_pkg = {}
    msku_roi_mem = ROIGenerate.MskuRoiGenerate(cfg)
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg,
                                                                                                is_save=0)
    roi_data = RoiMemGenerate(msku_roi_mem, cfg)
    roi_data_pkg["roi_gen_type"] = 0
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["pcm_array"] = pcm_array
    roi_data_pkg["ptm_array"] = ptm_array
    roi_data_pkg["masking_arrays"] = masking_arrays
    roi_data_pkg["masking_coor_info"] = masking_coor_info
    return roi_data_pkg


def MskuRoiGenerateByFile(cfg: dict) -> dict:
    """通过手动的标定坐标生成ROI"""
    roi_data_pkg = {}
    cali_data = MskuPubMethod.DirectAccessCaliData(cfg)
    msku_roi_mem = ROICalibration.MskuRoiGenerate(cfg=cfg, cali_data=cali_data)
    roi_data = RoiMemGenerate(msku_roi_mem, cfg)
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg,
                                                                                                is_save=0)
    roi_data_pkg["roi_gen_type"] = 1
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["pcm_array"] = pcm_array
    roi_data_pkg["ptm_array"] = ptm_array
    roi_data_pkg["masking_arrays"] = masking_arrays
    roi_data_pkg["masking_coor_info"] = masking_coor_info
    gc.collect()
    return roi_data_pkg


def MskuRoiGenerateByBase(cfg: dict) -> dict:  # TODO
    roi_data_pkg = {}
    roi_data_pkg["roi_gen_type"] = 2
    return roi_data_pkg


# @profile
def MskuRoiGenerateByCali(cfg: dict) -> dict:  # TODO
    """通过直接标定PCM图片生成ROI"""
    roi_data_pkg = {}
    cali_run = ROICalibration()
    cali_data, light_imags = cali_run.GetCaliDataFromPCMImage(cfg)
    msku_roi_mem = ROICalibration.MskuRoiGenerate(cfg=cfg, cali_data=cali_data)
    roi_data = RoiMemGenerate(msku_roi_mem, cfg)
    masking_arrays, pcm_array, ptm_array, masking_coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg)
    masking_arrays, cali_fusion_image, fusion_image_cali_3D_image = cali_run.CaliResultDisplay(cali_data, light_imags,
                                                                                               cfg, is_save=0)
    roi_data_pkg["roi_gen_type"] = 3
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


def ROIDataPackageSave(roi_data_pkg, cfg, save_sel=0, roi_data_format=1):
    """
    保存ROI数据: 包含图片、ROI数据
    Args:
        roi_data_pkg (dict): 包含生成ROI的所有必要信息
        cfg (dict): Hawk 配置集合
        save_sel (int): 0: 仅保存ROI数据,1: 保存ROI数据和图片数据
        roi_data_format (int): ROI存储格式：0：byte对齐, 1: half-word对齐

    Returns:

    """
    MskuPubMethod.roi_data_save(f_name=cfg["roi_name"], data=roi_data_pkg["roi_data"], fd_path=cfg["fd_path"],
                                roi_data_format=roi_data_format)
    url = f'{cfg["fd_path"]}/{cfg["roi_name"]}.txt'
    info = LogerPubMethod.create_file_hyperlink(file_type="ROI data", url=url)
    logging.info(info)

    if save_sel == 0:
        return

    # ROI masking数据效果保存
    # /////////////////////////////////////////////////
    img_fp = f'{cfg["fd_path"]}/image'

    canvas = Hawk01MaskingDynamicFig(roi_data_pkg)
    canvas.roi_img_save(img_fp=img_fp)
    canvas = None
    gc.collect()

    url = f'{img_fp}'
    info = LogerPubMethod.create_file_hyperlink(file_type="Image", url=url)
    logging.info(info)
    return


def ScriptDataSave(hawk01_cfg):
    """
    根据配置生成Hawk01配置脚本
        hawk_cfg (dict): Hawk 配置集合
    """
    __hawk01_cfg__ = copy.deepcopy(hawk01_cfg)
    # __reg_cfg__ = copy.deepcopy(reg_cfg)

    work_mode_q = hawk01_cfg["WORK_MODE"]

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
        __hawk01_cfg__["WORK_MODE"] = work_mode
        __hawk01_cfg__["reg_name"] = hawk01_cfg["reg_name"] if len(work_mode_q) == 0 \
            else f'Ranging_Mode_{hawk01_cfg["reg_name"]}' if work_mode == 0 \
            else f'Echo_Mode_{hawk01_cfg["reg_name"]}' if work_mode == 1 \
            else f'Histogram_Mode_{hawk01_cfg["reg_name"]}' if work_mode == 2 \
            else f'Gray_Scale_Mode_{hawk01_cfg["reg_name"]}'  # if work_mode == 3 \
        HawkPubMethod.GenerateHawkRegConfig(hawk_cfg=__hawk01_cfg__)
        # HawkPubMethod.GenerateHawkRegConfigByJson(hawk_cfg=__hawk01_cfg__, reg_cfg=__reg_cfg__)
        url = f'{__hawk01_cfg__["fd_path"]}/{__hawk01_cfg__["reg_name"]}.txt'
        info = LogerPubMethod.create_file_hyperlink(file_type="Script data", url=url)
        logging.info(info)

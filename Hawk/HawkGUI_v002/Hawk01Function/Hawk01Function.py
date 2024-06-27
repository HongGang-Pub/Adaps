from typing import Tuple, List, Any

from numpy import ndarray, dtype, floating, float_
from numpy._typing import _64Bit

from SelfDefinedPackge import PubMethod
from Hawk.MSKU.MSKU_Cali.ROICalibration import ROICalibration
from Hawk.MSKU.MSKU_GEN import ROIGenerate
from Hawk.MSKU import MskuPubMethod
import gc
from memory_profiler import profile


def MskuRoiGenerateByJson(cfg: dict) -> dict:
    """完全通过Json文件生成 MskuRoi"""
    data = {}
    msku_roi_mem = ROIGenerate.MskuRoiGenerate(cfg)
    arrays, acc_spad_array, depth_spad_array, coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg)
    data["msku_roi_mem"] = msku_roi_mem
    data["arrays"] = arrays
    data["coor_coor_info"] = coor_info
    data["acc_spad_array"] = acc_spad_array
    data["depth_spad_array"] = depth_spad_array
    return data


def MskuRoiGenerateByFile(cfg: dict) -> dict:
    """通过手动的标定坐标生成ROI"""
    data = {}
    cali_data = MskuPubMethod.DirectAccessCaliData(cfg)
    msku_roi_mem = ROICalibration.MskuRoiGenerate(cfg=cfg, cali_data=cali_data)
    arrays, acc_spad_array, depth_spad_array, coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg)
    data["msku_roi_mem"] = msku_roi_mem
    data["arrays"] = arrays
    data["coor_info"] = coor_info
    data["acc_spad_array"] = acc_spad_array
    data["depth_spad_array"] = depth_spad_array
    gc.collect()
    return data


def MskuRoiGenerateByBase(cfg: dict) -> dict:  # TODO
    data = {}
    return data


@profile
def MskuRoiGenerateByCali(cfg: dict) -> dict:  # TODO
    """通过直接标定PCM图片生成ROI"""
    data = {}
    cali_run = ROICalibration()
    cali_data, light_imags = cali_run.GetCaliDataFromPCMImage(cfg)
    msku_roi_mem = ROICalibration.MskuRoiGenerate(cfg=cfg, cali_data=cali_data)
    arrays, acc_spad_array, depth_spad_array, coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg)
    arrays, fusion_image, spad_array_3D = cali_run.CaliResultDisplay(cali_data, light_imags, cfg, is_save=0)
    data["msku_roi_mem"] = msku_roi_mem
    data["arrays"] = arrays
    data["fusion_image"] = fusion_image
    data["spad_array_3D"] = spad_array_3D
    data["acc_spad_array"] = acc_spad_array
    data["depth_spad_array"] = depth_spad_array
    data["coor_info"] = coor_info
    del light_imags
    gc.collect()
    return data


def RoiMemGenerate(msku_roi_mem, cfg):
    roi_data = []
    try:
        zones_config = MskuPubMethod.ZonesConfigGenerate(cfg=cfg)
    except BaseException as msg:
        raise msg

    for vroll_cnt in range(len(msku_roi_mem)):
        per_zone_mem = zones_config[vroll_cnt] + msku_roi_mem[vroll_cnt]
        roi_data = roi_data + per_zone_mem
    MskuPubMethod.roi_data_save(f_name=f"{cfg['roi_name']}.txt", data=roi_data, fd_path=cfg["fd_path"])
    return

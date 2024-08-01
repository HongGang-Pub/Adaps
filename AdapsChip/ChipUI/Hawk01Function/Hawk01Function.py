import copy

from AdapsChip.Hawk01.Common import HawkPubMethod
from AdapsChip.Hawk01.MSKU.MSKU_Cali.ROICalibration import ROICalibration
from AdapsChip.Hawk01.MSKU.MSKU_GEN import ROIGenerate
from AdapsChip.Hawk01.MSKU import MskuPubMethod
import gc
import matplotlib.pyplot as plt
from SelfDefinedPackge import ArrayPubMethod
from matplotlib.pyplot import MultipleLocator
import logging
from SelfDefinedPackge import LogerPubMethod

def MskuRoiGenerateByJson(cfg: dict) -> dict:
    """完全通过Json文件生成 MskuRoi"""
    roi_data_pkg = {}
    msku_roi_mem = ROIGenerate.MskuRoiGenerate(cfg)
    arrays, acc_spad_array, depth_spad_array, coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg, is_save=0)
    roi_data = RoiMemGenerate(msku_roi_mem, cfg)
    roi_data_pkg["roi_gen_type"] = 0
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["arrays"] = arrays
    roi_data_pkg["coor_info"] = coor_info
    roi_data_pkg["acc_spad_array"] = acc_spad_array
    roi_data_pkg["depth_spad_array"] = depth_spad_array
    return roi_data_pkg

def MskuRoiGenerateByFile(cfg: dict) -> dict:
    """通过手动的标定坐标生成ROI"""
    roi_data_pkg = {}
    cali_data = MskuPubMethod.DirectAccessCaliData(cfg)
    msku_roi_mem = ROICalibration.MskuRoiGenerate(cfg=cfg, cali_data=cali_data)
    roi_data = RoiMemGenerate(msku_roi_mem, cfg)
    arrays, acc_spad_array, depth_spad_array, coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg, is_save=0)
    roi_data_pkg["roi_gen_type"] = 1
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["arrays"] = arrays
    roi_data_pkg["coor_info"] = coor_info
    roi_data_pkg["acc_spad_array"] = acc_spad_array
    roi_data_pkg["depth_spad_array"] = depth_spad_array
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
    arrays, acc_spad_array, depth_spad_array, coor_info = MskuPubMethod.RollingArrayCollect(msku_roi_mem, cfg)
    arrays, fusion_image, spad_array_3D = cali_run.CaliResultDisplay(cali_data, light_imags, cfg, is_save=0)
    roi_data_pkg["roi_gen_type"] = 3
    roi_data_pkg["roi_data"] = roi_data
    roi_data_pkg["arrays"] = arrays
    roi_data_pkg["fusion_image"] = fusion_image
    roi_data_pkg["spad_array_3D"] = spad_array_3D
    roi_data_pkg["acc_spad_array"] = acc_spad_array
    roi_data_pkg["depth_spad_array"] = depth_spad_array
    roi_data_pkg["coor_info"] = coor_info
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

    # SPAD阵列保存
    try:
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        ax.yaxis.set_major_locator(MultipleLocator(50))
        ax.xaxis.set_major_locator(MultipleLocator(48))
        # ax.imshow(spad_array, cmap="gray")
        ax.imshow(roi_data_pkg["acc_spad_array"])
        # plt.show()
        for info in roi_data_pkg["coor_info"]:
            MskuPubMethod.do_mark(info)
        ArrayPubMethod.ArrayImageSave(fname='imag_msku', fd_path=img_fp)
        plt.close()
    except:
        pass
    # SPAD 深度数据保存
    try:
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.tick_top()  # 设置x坐标轴位置在顶部
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.xaxis.set_major_locator(MultipleLocator(16))
        ax.imshow(roi_data_pkg["depth_spad_array"])
        # plt.show()
        ArrayPubMethod.ArrayImageSave(fname="imag_depth", fd_path=img_fp)
        plt.close()
    except:
        pass

    # 标定数据保存
    # /////////////////////////////////////////////////
    if roi_data_pkg["roi_gen_type"] == 3:
        try:
            roll_num = len(roi_data_pkg["arrays"])
            for roll_cnt in range(roll_num):
                (x, y, text) = roi_data_pkg["coor_info"][roll_cnt]
                file_path = "{}\\image\\{}.png".format(cfg["fd_path"], text)
                plt.imsave(file_path, roi_data_pkg["arrays"][roll_cnt])
            # 保存图像
            # ///////////////////////////////////////////////////////////////
            f1 = "{}\\{}.png".format(img_fp, "fusion_imag")
            f2 = "{}\\{}.png".format(img_fp, "fusion_msku")
            plt.imsave(f1, roi_data_pkg["fusion_image"])
            plt.imsave(f2, roi_data_pkg["spad_array_3D"])
        except:
            pass
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
            else f'Gray_Scale_Mode_{hawk01_cfg["reg_name"]}'   # if work_mode == 3 \
        HawkPubMethod.GenerateHawkRegConfig(hawk_cfg=__hawk01_cfg__)
        # HawkPubMethod.GenerateHawkRegConfigByJson(hawk_cfg=__hawk01_cfg__, reg_cfg=__reg_cfg__)
        url = f'{__hawk01_cfg__["fd_path"]}/{__hawk01_cfg__["reg_name"]}.txt'
        info = LogerPubMethod.create_file_hyperlink(file_type="Script data", url=url)
        logging.info(info)

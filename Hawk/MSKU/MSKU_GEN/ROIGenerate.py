from Hawk.MSKU import MskuPubMethod
from SelfDefinedPackge import PubMethod

from tkinter import messagebox
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt


def MskuRoiGenerate(cfg):
    scan_mode = cfg['SCAN_MODE']
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM']
    seg_hs = cfg['seg_hs']
    h_vld_seg = cfg['H_VLD_SEG']
    spad_vs = cfg['spad_vs']
    light_shift = cfg['light_shift']
    sublight_shift = cfg['sublight_shift']
    roi_shape = cfg['roi_shape']
    v_spad_shift = cfg['v_spad_shift']
    h_seg_shitf = cfg['h_seg_shift']

    """按照rolling生成与 MSKU 相关的 ROI Data"""
    msku_roi_mem = []
    per_rolling_roi_mem = []
    result = ""

    if scan_mode == 0 and (seg_hs + h_vld_seg) > 15:
        result = result + "1D scan_mode: [(seg_hs + h_vld_seg) > 15], config is not correct!"
        raise ValueError(result)

    if scan_mode == 1 and (seg_hs + h_seg_shitf * h_roll_num) > 15:
        result = result + "2D scan_mode: [(seg_hs + h_seg_shift * _v_roll_num) > 15], config is not correct!"
        raise ValueError(result)

    # 生成ROI memory数据
    for v_roll_cnt in range(0, v_roll_num + 1):
        light_vs = light_shift * v_roll_cnt + spad_vs

        if scan_mode == 0:  # 1D scan
            # sub_frame_num = v_roll_cnt
            for j in range(0, 6):
                sublight_vs = light_vs + sublight_shift * j
                for seg_num in range(0, h_vld_seg + 1):
                    h_seg_s = seg_hs + seg_num
                    if roi_shape == 0:
                        v_spad_c = sublight_vs + v_spad_shift * seg_num
                    elif seg_num <= h_vld_seg / 2:
                        v_spad_c = sublight_vs + v_spad_shift * seg_num
                    else:
                        v_spad_c = sublight_vs + v_spad_shift * (h_vld_seg - seg_num)

                    v_spad_c = 0 if v_spad_c < 0 else v_spad_c
                    v_spad_c = 576 if v_spad_c > 575 else v_spad_c
                    per_rolling_roi_mem.append((int(h_seg_s << 10) + v_spad_c))
        else:  # 2D scan
            for h_roll_cnt in range(0, h_roll_num + 1):
                # sub_frame_num = v_roll_cnt * (_v_roll_num + 1) + h_roll_cnt
                h_seg_s = seg_hs + h_seg_shitf * h_roll_cnt

                for j in range(0, 6):
                    sublight_vs = light_vs + sublight_shift * j
                    v_spad_c = sublight_vs + v_spad_shift * h_roll_cnt
                    if v_spad_c < 0:
                        v_spad_c = 0
                    if v_spad_c > 575:
                        v_spad_c = 576
                    per_rolling_roi_mem.append((int(h_seg_s << 10) + v_spad_c))
        msku_roi_mem.append(per_rolling_roi_mem)
        per_rolling_roi_mem = []

    return msku_roi_mem


def RoiMemGenerate():
    roi_data = []
    cfg = PubMethod.ReadJsonFile('ROIConfig.json')

    try:
        zone_mem = MskuPubMethod.ZonesConfigGenerate(cfg=cfg)
    except BaseException as msg:
        raise msg

    try:
        msku_roi_mem = MskuRoiGenerate(cfg)
    except BaseException as msg:
        raise ValueError("The ROI configuration may be missing or incorrect! Log: {}".format(msg))

    MskuPubMethod.roi_imag(msku_roi_mem, cfg, f_name=cfg['file_name'], fd_path=cfg["fd_path"])
    # arr = MskuPubMethod.PerRollingArrayCollect(msku_roi_mem, cfg, f_name=cfg['file_name'], fd_path=cfg["fd_path"])
    # MskuPubMethod.animation_img(arr)
    # msku_gui(arr)

    for index in range(len(zone_mem)):
        per_zone_mem = zone_mem[index] + msku_roi_mem[index]
        # if cfg['per_rolling_data_save'] == 1:
        #     MskuPubMethod.roi_data_save(f_name="ROLL_{}_{}".format(index, file), data=per_zone_mem)
        roi_data = roi_data + per_zone_mem

    file = "{}.txt".format(cfg['file_name'])
    MskuPubMethod.roi_data_save(f_name=file, data=roi_data, fd_path=cfg["fd_path"], data_format=cfg['data_format'])
    return f"{file} 生成完成！"


if __name__ == '__main__':
    try:
        info = RoiMemGenerate()
    except BaseException as log:
        info = repr(log)

    messagebox.showinfo("执行结果", info)

    # info = RoiSram.RoiMemGenerate()
    # print(info)

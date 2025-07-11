import logging

import AdapsChip.Common.common
from AdapsChip.Hawk01.MSKU import MskuPubMethod
from SelfDefinedPackge import PubMethod
import os


def expand_groups(groups, total_boxes=6):
    """
    根据传入的 groups 列表自动扩展分组方案，以确保总箱子数为 total_boxes。
    如果 groups 的总箱子数超过 total_boxes，则截取多余的部分。

    参数:
        groups (list): 用户传入的初始分组。
        total_boxes (int): 总箱子数，默认是6。

    返回:
        list: 完整的分组方案，确保总箱子数为 total_boxes。
    """
    current_count = sum(groups)

    # 如果当前分组总箱子数超过 total_boxes，截取前面的部分使其等于 total_boxes
    if current_count > total_boxes:
        trimmed_groups = []
        box_count = 0
        for group_size in groups:
            if box_count + group_size > total_boxes:
                # 截取最后一组的部分，使总数刚好等于 total_boxes
                trimmed_groups.append(total_boxes - box_count)
                break
            trimmed_groups.append(group_size)
            box_count += group_size
        return trimmed_groups

    # 如果当前分组已涵盖所有箱子，直接返回
    if current_count == total_boxes:
        return groups[:]

    # 计算剩余箱子数量，并用最后一个组大小填充
    remaining_boxes = total_boxes - current_count
    last_group_size = groups[-1]
    expanded_groups = groups + [last_group_size] * (remaining_boxes // last_group_size)

    # 如果有剩余箱子不足以形成一个完整组，单独加一个组
    if sum(expanded_groups) < total_boxes:
        expanded_groups.append(total_boxes - sum(expanded_groups))

    return expanded_groups


def calculate_distances(groups, base_distance=0, increment=3, intra_group_offset=3):
    """
    计算每个箱子的移动距离，组间和组内均有偏移。

    参数:
        groups (list): 用户传入的初始分组。

    返回:
        list: 每个箱子移动的距离。
    """
    expanded_groups = expand_groups(groups)

    distances = []

    for i, group_size in enumerate(expanded_groups):
        group_distance = base_distance + increment * i  # 每组的初始距离
        # 为当前组的每个箱子计算偏移量
        for j in range(group_size):
            distances.append(group_distance + intra_group_offset * j)

    return distances


def MskuRoiGenerate(hawk01_cfg):
    scan_mode = hawk01_cfg['SCAN_MODE']
    v_roll_num = hawk01_cfg['V_ROLL_NUM']
    h_roll_num = hawk01_cfg['H_ROLL_NUM']
    seg_hs = hawk01_cfg['seg_hs']
    h_vld_seg = hawk01_cfg['H_VLD_SEG']
    spad_vs = hawk01_cfg['spad_vs']
    light_shift = hawk01_cfg['light_shift']
    sublight_shift = hawk01_cfg['sublight_shift']
    roi_shape = hawk01_cfg['roi_shape']
    v_spad_shift = hawk01_cfg['v_spad_shift']
    h_seg_shitf = hawk01_cfg['h_seg_shift']
    roi_retrace = hawk01_cfg['roi_retrace']

    try:
        sublight_group = hawk01_cfg["sublight_group"].split(",")
        sublight_group = list(map(int, sublight_group))
    except BaseException as e:
        logging.warning(f"The sublight_group config format is error. {e}")
        sublight_group = [6]

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
        distance = calculate_distances(groups=sublight_group,
                                       base_distance=light_vs,
                                       increment=sublight_shift,
                                       intra_group_offset=3)
        if scan_mode == 0:  # 1D scan
            # sub_frame_num = v_roll_cnt
            for j in range(0, 6):
                sublight_vs = distance[j]
                # sublight_vs = light_vs + 3 * j + sublight_shift*(j//3)
                for seg_num in range(0, h_vld_seg + 1):
                    h_seg_s = seg_hs + seg_num
                    if roi_shape == 0:
                        v_spad_c = sublight_vs + v_spad_shift * seg_num
                    elif seg_num <= h_vld_seg / 2:
                        v_spad_c = sublight_vs + v_spad_shift * seg_num
                    else:
                        v_spad_c = sublight_vs + v_spad_shift * (h_vld_seg - seg_num)

                    v_spad_c = 0 if v_spad_c < 0 \
                        else v_spad_c % 576 if roi_retrace == 1 \
                        else min(v_spad_c, 576)
                    per_rolling_roi_mem.append((int(h_seg_s << 10) + v_spad_c))
        else:  # 2D scan
            for h_roll_cnt in range(0, h_roll_num + 1):
                h_seg_s = seg_hs + h_seg_shitf * h_roll_cnt

                for j in range(0, 6):
                    sublight_vs = distance[j]
                    v_spad_c = sublight_vs + v_spad_shift * h_roll_cnt
                    v_spad_c = 0 if v_spad_c < 0 \
                        else v_spad_c % 576 if roi_retrace == 1 \
                        else min(v_spad_c, 576)
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

    MskuPubMethod.RollingArrayCollect(msku_roi_data=msku_roi_mem, cfg=cfg, is_save=1, fd_path=cfg["fd_path"])
    # arr = MskuPubMethod.RollingArrayCollect(msku_roi_mem, hawk01_config, f_name=hawk01_config['file_name'], fd_path=hawk01_config["fd_path"])
    # MskuPubMethod.animation_img(arr)
    # msku_gui(arr)

    for index in range(len(zone_mem)):
        per_zone_mem = zone_mem[index] + msku_roi_mem[index]
        # if hawk01_config['per_rolling_data_save'] == 1:
        #     MskuPubMethod.roi_data_save(f_name="ROLL_{}_{}".format(index, file), data=per_zone_mem)
        roi_data = roi_data + per_zone_mem

    AdapsChip.Common.common.roi_data_save(f_name=cfg["roi_name"], data=roi_data, fd_path=cfg["fd_path"], roi_data_format=cfg['roi_data_format'])
    return


if __name__ == '__main__':
    try:
        RoiMemGenerate()
    except BaseException as log:
        info = repr(log)
        logging.fatal(info)

    # info = RoiSram.GenerateRoiMem()
    # print(info)

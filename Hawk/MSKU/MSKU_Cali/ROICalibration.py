import os
import numpy as np
import matplotlib.pyplot as plt
from SelfDefinedPackge import PubMethod
from Hawk.MSKU import MskuPubMethod
from scipy import signal
from Hawk.MSKU.MSKU_Cali import GlobalDef


def get_pcm_file(fp: str, frame_num=5) -> dict:
    """
    从指定的文件夹中获取对应的灰度图，用于成图

    Args:
        fp (str): 文件路径
        frame_num (int): 采用第几帧数据进行标定

    Returns:
        dict: type(dict): {索引：文件路径}
    """
    f1 = PubMethod.get_fp(fd_path=fp, mode=0, match_filter='GrayImage', regression=1, f_type="PCM Imag")
    get_frame_cnt = 1

    f_dict = {}
    for f in f1:
        if os.path.splitext(f)[1] == ".raw":
            f_name = os.path.split(f)[1]
            index = float(f_name.split("_")[3])
            if index in f_dict:
                get_frame_cnt += 1
                if get_frame_cnt > frame_num:
                    continue
            else:
                get_frame_cnt = 1
            f_dict[index] = f
    return f_dict


def get_pcm_file_1(fp: str) -> dict:
    """
    从指定的文件夹中获取对应的灰度图，用于成图

    Args:
        fp (str): 文件路径

    Returns:
        dict: type(dict): {索引：文件路径}
    """
    f1 = PubMethod.get_fp(fd_path=fp, mode=0, match_filter='GrayImage', regression=1, f_type="PCM Imag")
    f_dict = {}
    for f in f1:
        if os.path.splitext(f)[1] == ".raw":
            index = float(os.path.split(f)[0].split("\\")[-1].split("_")[0])
            f_dict[index] = f
    return f_dict


def MoveCoorByPixel(hist_array: np.ndarray, cali_point: int) -> int:
    """
    对坐标按照pixel进行标定

    Args:
        hist_array (np.ndarray): 基准标定数据
        cali_point (int): 需要按照pixel移位的点

    Returns:

    """
    sub_point = (cali_point // 3) * 3
    add_point = (cali_point // 3 + 1) * 3
    if (add_point + 17 < 576) and (hist_array[sub_point] < hist_array[add_point + 17]):
        return add_point
    else:
        return sub_point


def Conv2(image: np.ndarray) -> np.ndarray:
    """
    对 image 进行 3*3 卷积，实现噪点去除功能

    Args:
        image (np.ndarray): image

    Returns:
        np.ndarray: 和输入图像尺寸大小相同的feature map
    """
    kernel = np.ones((3, 3), dtype=int)

    res2d = signal.convolve2d(image[:, :, 0], kernel, 'same')

    H = image.shape[0]
    W = image.shape[1]
    res = np.zeros([H, W, 1])
    res[:, :, 0] = res2d

    # 卷积大小固定为3*3卷积，这里因为固定了卷积大小，所以写代码前可以直接确定：卷积步长为1
    # image = np.insert(image, obj=0, values=image[:, 0, :], axis=1)
    # image = np.insert(image, obj=W, values=image[:, W, :], axis=1)
    # image = np.insert(image, obj=0, values=image[0, :, :], axis=0)
    # image = np.insert(image, obj=H, values=image[H, :, :], axis=0)
    #
    # for i in range(H):
    #     for j in range(W):
    #         temp = image[i:i + 3, j:j + 3]
    #         temp = np.multiply(temp, kernel)
    #         res[i][j] = round(temp.sum() / 9)

    return res


def SegAccumulation(array: np.ndarray, accum_seg: int = 1) -> np.ndarray:
    """
    将面阵按指定的段数进行累加(步径为1)

    Args:
        array (np.ndarray): image数组，shape:567 * 768 * 1
        accum_seg (int): 累加的段数。eg: 1*48 spad 累加

    Returns:
        np.ndarray: 数组，shape:567 * 16 * 1
    """
    seg_sum_array = np.zeros((576, 16))

    for i in range(0, 16):
        if i + accum_seg - 1 < 16:
            seg = array[:, i * 48:(i + accum_seg) * 48]
            seg_sum_array[:, i:i + 1] = np.sum(seg, axis=1)
        else:
            break
    return seg_sum_array


def OpenWindows(hist_array: np.ndarray, ini_point: int, window_size: int) -> int:
    """
    按照配置值进行开窗

    Args:
        hist_array (np.ndarray): 需要开窗的一维数组
        ini_point (int): 开窗的起始点
        window_size (int): 开窗的大小

    Returns:
        int: 返回开窗后的起始点(左边界索引)
    """
    initial_point = 0
    H = hist_array.shape[0]
    for index in range(ini_point, H):
        if (index + window_size < H) and (hist_array[index] < hist_array[index + window_size]):
            continue
        else:
            initial_point = index
            break
    return initial_point


def SCANMODE_1D(img, h_vld_seg, ref_segment, curvature) -> list:
    """
    1D Scan Mode下，根据配置标定ROI

    Args:
        img (np.ndarray): image
        h_vld_seg (int): 寄存器配置
        ref_segment(int): 指定基准段用于偏移矫正
        curvature (int): 曲率配置，若不需要曲率自动矫正，配置值 > 576 即可

    Returns:
        list: 返回 ROI 标定数据
    """
    per_img_roi_data = []  # 存储一张PCM灰度图获取的ROI数据

    # 1D scan_mode将 spad 按照 576*48 (共16段划分)，然后累和
    # ///////////////////////////////////////////////////////////////
    seg_sum_array = SegAccumulation(array=img, accum_seg=1)

    # 检索 seg_sum_array 矩阵中的最大值，返回 value 和 index
    # ///////////////////////////////////////////////////////////////
    v_spad_value = np.max(seg_sum_array, axis=0)
    v_spad_max_index = np.argmax(seg_sum_array, axis=0)

    # 横向开窗，按照 h_vld_seg，找到亮度最高的段数
    # ///////////////////////////////////////////////////////////////
    index = np.argmax(v_spad_value) - h_vld_seg
    index = index if index > 0 else 0
    # 增加 ini_point 是确保开窗位置包含最大值(开窗较小时有用)
    seg_hs = OpenWindows(v_spad_value, index, h_vld_seg + 1)

    # 按段纵向开窗，找到每段rolling开6行pixel的spad的起始点
    # ///////////////////////////////////////////////////////////////
    start_index_list = []

    # 对 seg_sum_array 进行平滑处理
    # ///////////////////////////////////////////////////////////////
    # kernel = np.ones(18, int)
    #
    # H = seg_sum_array.shape[0]
    # top_array = seg_sum_array[0, :]
    # top_array = np.expand_dims(top_array, 0).repeat(17, axis=0)
    # botton_array = seg_sum_array[H-1, :]
    # botton_array = np.expand_dims(botton_array, 0).repeat(17, axis=0)

    # _seg_sum_array = seg_sum_array
    # _seg_sum_array = np.insert(_seg_sum_array, obj=H, values=botton_array, axis=0)
    # _seg_sum_array = np.insert(_seg_sum_array, obj=0, values=top_array, axis=0)

    for seg_num in range(seg_hs, seg_hs + h_vld_seg + 1):
        ini_point = v_spad_max_index[seg_num] - 17
        ini_point = ini_point if ini_point > 0 else 0

        # _seg_array = np.convolve(_seg_sum_array[:, seg_num], kernel, mode='same')
        # seg_array = _seg_array[18:576+18]

        seg_array = seg_sum_array[:, seg_num]
        start_index = OpenWindows(seg_array, ini_point, 18)

        # for debug
        # if seg_num == 0:
        #     plt.subplot(1, 2, 1)
        #     plt.plot(seg_sum_array[:, seg_num])
        #     plt.subplot(1, 2, 2)
        #     plt.plot(seg_array)

        # 最后一段根据光子数进行矫正, 主要解决 spadisapp 覆盖式更新, 成图效果差的问题
        # ///////////////////////////////////////////////////////////////
        if seg_hs < seg_num < (seg_hs + h_vld_seg + 1) and GlobalDef.cali_info not in ["first_frame", "last_frame"]:
            ref_value = np.min(seg_sum_array[start_index:start_index + 18, seg_num])
            coefficient = ref_value / v_spad_value[seg_num]
            GlobalDef.coefficient = coefficient if GlobalDef.coefficient is None \
                else min(coefficient, GlobalDef.coefficient)
            # print(GlobalDef.cali_info, GlobalDef.coefficient)

        if GlobalDef.cali_info == "last_frame":
            for coor in range(start_index, 576):
                if seg_sum_array[coor, seg_num] < v_spad_value[seg_num] * GlobalDef.coefficient:
                    continue
                else:
                    start_index = coor
                    break
        start_index_list.append(start_index)

    # 校准：根据 基准段 & 设置的曲率（spad步径）
    # 判断某段标定位置是否偏移过大，如果过大，则会进行校准
    # ///////////////////////////////////////////////////////////////
    ref_segment = np.argmax(v_spad_value) if ref_segment is None else ref_segment
    h_center = ref_segment - seg_hs
    # 向前校准
    for cnt in range(0, h_center):
        pre_index = h_center - cnt - 1
        index = h_center - cnt
        pre_vcoor = start_index_list[pre_index]
        vcoor = start_index_list[index]
        pre_vcoor = vcoor if abs(vcoor - pre_vcoor) > curvature else pre_vcoor
        start_index_list[pre_index] = pre_vcoor
    # 向后校准
    for index in range(h_center, h_vld_seg):
        post_index = index + 1
        vcoor = start_index_list[index]
        post_vcoor = start_index_list[post_index]
        post_vcoor = vcoor if abs(vcoor - post_vcoor) > curvature else post_vcoor
        start_index_list[post_index] = post_vcoor

    # 通过 seg_hs 和 start_index进行组合产生横纵坐标
    # ///////////////////////////////////////////////////////////////
    for seg_num in range(seg_hs, seg_hs + h_vld_seg + 1):
        start_index = start_index_list[seg_num - seg_hs]
        per_img_roi_data.append([seg_num, start_index])

    # 修改 dsp_img 图片
    # ///////////////////////////////////////////////////////////////
    valid_spad_max_photon_count = v_spad_value.max() / 48
    dsp_img = img[:, :, 0] / valid_spad_max_photon_count
    dsp_img = np.where(dsp_img <= 1, dsp_img, 1)
    GlobalDef.light_imags.append(dsp_img)

    return per_img_roi_data


def SCANMODE_2D(img: np.ndarray, h_vld_seg: int, mode: int = 0) -> list:
    """
    2D Scan Mode下，根据配置标定ROI

    Args:
        img (np.ndarray): image
        h_vld_seg (int): 寄存器配置
        mode (int): 2D Scan Mode标定模式：0：以光条能量优先；1：以能 Masking的最大光子数优先

    Returns:
        list: 返回 ROI 标定数据
    """
    per_img_roi_data = []  # 存储一张PCM灰度图获取的ROI数据

    # 2D scan_mode将 spad 按照 576*(48*h_vld_seg) 步径为 1 进行累和
    seg_sum_array = SegAccumulation(array=img, accum_seg=h_vld_seg + 1)

    # 检索 seg_sum_array 矩阵中的最大值，返回 value 和 index
    v_spad_value = np.max(seg_sum_array, axis=0)
    v_spad_max_index = np.argmax(seg_sum_array, axis=0)

    seg_hs = np.argmax(v_spad_value)

    if mode == 1:
        photon_max_num = 0
        for seg_num in range(0, 16 - h_vld_seg):
            ini_point = v_spad_max_index[seg_num] - 17
            ini_point = ini_point if ini_point > 0 else 0
            start_index = OpenWindows(seg_sum_array[:, seg_num], ini_point, 18)
            # 开窗，通过 ROI 框的光子数量，找最优解
            photon_num = np.sum(seg_sum_array[start_index: start_index + 17, seg_num: seg_num + 1])
            if photon_max_num < photon_num:
                seg_hs = seg_num
                photon_max_num = photon_num
    # print(seg_hs, end="\t")

    # 获取start_index
    index = v_spad_max_index[seg_hs]
    ini_point = index - 17 if index - 16 > 0 else 0
    start_index = OpenWindows(seg_sum_array[:, seg_hs], ini_point, 18)

    # 通过 seg_hs 和 spad_vs进行组合产生横纵坐标，并根据标定位置修改spad_array，辅助成图check ROI是否正确
    per_img_roi_data.append([seg_hs, start_index])

    # 返回有效光条的二维数组
    valid_spad_max_photon_count = v_spad_value.max() / ((h_vld_seg + 1) * 48)
    dsp_img = img[:, :, 0] / valid_spad_max_photon_count
    dsp_img = np.where(dsp_img <= 1, dsp_img, 1)
    GlobalDef.light_imags.append(dsp_img)

    return per_img_roi_data


def GetRoiDataFromImag(file: str, img_name: str, scan_mode: int = 0, h_vld_seg: int = 15, ref_segment=None,
                       curvature: int = 30, noise_filter: int = 0, mode2D: int = 0, img_reverse: int = 0) -> list:
    """
    根据配置调用相应方法对单张图片进行识别，找出光条，并生成 ROI 标定效果图片

    Args:
        file (str): 读取的 raw 文件路径
        img_name (str): 生成的 ROI 标定图像存储名称，且用于日志打印
        scan_mode (int): 寄存器配置
        h_vld_seg (int): 寄存器配置
        ref_segment(int): 指定基准段用于偏移矫正
        curvature (int): 相邻两段SPAD偏移范围，超过偏移配置值，强行矫正标定的ROI
        noise_filter (int): 是否进行噪点消除
        mode2D (int):2D Scan mode标定方式
        img_reverse (int): img是否需要镜像：0：不镜像; 1: x轴镜像; 2: y轴镜像 3: x+y轴镜像

    Returns:
        list: ROI 标定数据
    """

    # 读取 .raw文件
    # ///////////////////////////////////////////////////////////////
    # 利用numpy的fromfile函数读取raw文件，并指定数据格式
    ini_img = np.fromfile(file, dtype='uint32')
    # 利用numpy中array的reshape函数将读取到的数据进行重新排列
    ini_img = ini_img.reshape(576, 768, 1)

    img = Conv2(image=ini_img) if noise_filter == 1 else ini_img
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.imshow(images)

    if img_reverse == 2:
        img = np.flip(img, axis=0)
    elif img_reverse == 1:
        img = np.flip(img, axis=1)
    elif img_reverse == 3:
        img = np.flip(img)
    else:
        img = img
    # plt.subplot(1, 2, 2)
    # plt.imshow(images)
    # plt.show()

    if scan_mode == 0:
        per_img_roi_data = SCANMODE_1D(img, h_vld_seg, ref_segment, curvature)
    else:
        per_img_roi_data = SCANMODE_2D(img, h_vld_seg, mode=mode2D)

    print("完成 {} 图像识别！！！".format(img_name))
    return per_img_roi_data


def GetRoiDataFromAllImags(f_dict: dict, cfg: dict) -> list:
    """
    对文件按照给定的顺序调用标定方法标定，并成图展示整体标定效果

    Args:
        f_dict (dict): 标定数据 .raw 文件的集合，一个 .raw文件对应一次rolling。
            {key: value}, key为文件索引，value为文件路径。
            LIKE:
                f_dict = {  0:"./roll0.raw",
                            1:"./roll1.raw"}
            标定顺序根据 key 进行排序标定，可正序 或 倒序
        cfg (dict): 相关配置信息

    Returns:
        tuple: 按照顺序标定后返回的标定值
        ROI_DATA 返回格式:
        [
        [[0, 0], [1, 0], [2, 0], ...，], // roll =0
        ...
        ]
    """

    # 文件读取数顺序处理
    # ///////////////////////////////////////////////////////////////
    # 根据config文件赋值
    reverse = True if cfg['is_reverse'] == 1 else False
    # 对获取的文件进行排序，按排序进行图像识别
    file_index_list = list(f_dict.keys())
    file_index_list.sort(reverse=reverse)

    # 数据标定
    # ///////////////////////////////////////////////////////////////
    # 循环对所有图片进行识别，对图片进行融合
    image_roi_datas = []
    # for index in file_index_list[0:2]:
    for roll_cnt in range(len(file_index_list)):
        file = f_dict[file_index_list[roll_cnt]]
        f_name = "Roll{}_{}".format(roll_cnt, file_index_list[roll_cnt])

        GlobalDef.cali_info = "first_frame" if (roll_cnt == 0) \
            else "last_frame" if (roll_cnt == len(file_index_list) - 1) \
            else None  # 1D scan_mode used
        per_img_roi_data = GetRoiDataFromImag(file=file,
                                              img_name=f_name,
                                              scan_mode=cfg['SCAN_MODE'],
                                              h_vld_seg=cfg['H_VLD_SEG'],
                                              ref_segment=cfg['ref_segment'],
                                              curvature=cfg['curvature'],
                                              noise_filter=cfg['remove_noise'],
                                              mode2D=cfg["mode2D"],
                                              img_reverse=cfg["img_reverse"])

        image_roi_datas.append(per_img_roi_data)
    return image_roi_datas


def Std_correct(A, B, precision):
    """
    Hawk 按照18行 spad 规格进行矫正 (只对横坐标进行矫正)
    Args:
        A (list): 基准数据, 数据格式：[[0, 0], [1, 0], [2, 0], [3, 0], ...]
        B (list): 需矫正数据, 数据格式同 A
        precision (int): 矫正精度(spad为单位)

    Returns:
        list: 返回矫正后的数据
    """

    for i in range(len(A)):
        A_value = A[i][1]
        B_value = B[i][1]
        if abs(A_value - B_value) <= 18:
            continue
        elif abs(A_value - B_value) - 18 <= precision:
            B[i][1] = A_value - 18 if A_value > B_value else A_value + 18
    return B


def fill_gaps(blocks: list, length: int = 6, max_move: int = 2, base_block_index: int = 0) -> tuple:
    """
    移动方块以填充缝隙，同时确保不产生新的缝隙

    Args:
        blocks (list): 方块的初始位置列表
        length (int): 方块的长度（默认为6）
        max_move (int): 每个方块最大移动范围（默认为1）
        base_block_index (int): 基准块, 基于基准块移动其他方块消除黑条

    Returns:
        tuple: 1.调整位置后的方块列表
               2.移除缝隙方块移动的距离合计
               3.缝隙是否完全消除: True or False
    """

    move_distance_sum = 0
    is_success = True

    correct_blocks = blocks[:]
    if not correct_blocks:
        return [], 0, False

    # 对方块进行排序
    correct_blocks.sort()

    # 以基准块为中心，通过平移后面的方块，移除缝隙
    # ///////////////////////////////////////////////////////////////
    i = base_block_index
    while i < len(correct_blocks) - 1:
        end_of_current = correct_blocks[i] + length
        start_of_next = correct_blocks[i + 1]
        distance = start_of_next - end_of_current

        if distance < 0:  # 存在重叠
            # 检查后面是否有缝隙
            if i + 1 < len(correct_blocks) - 1:
                next_end = correct_blocks[i + 1] + length
                gap_after_next = correct_blocks[i + 2] - next_end
                if gap_after_next > 0:
                    # 使用重叠部分来填充缝隙
                    move_distance = min(max_move, min(-distance, gap_after_next))
                    correct_blocks[i + 1] += move_distance

                    move_distance_sum += move_distance
                    is_success = False if max_move < min(-distance, gap_after_next) else True

        elif distance > 0:  # 存在缝隙
            # 确保移动不会产生新的缝隙
            if i == 0:
                # move_distance = min(max_move, distance)
                move_distance = distance
                correct_blocks[i] += move_distance
                move_distance_sum += move_distance
            else:
                move_distance = min(max_move, distance)
                correct_blocks[i + 1] -= move_distance

                move_distance_sum += move_distance
                is_success = False if max_move < distance else True
        i += 1

    # 以基准块为中心，通过平移前面的方块，移除缝隙
    # ///////////////////////////////////////////////////////////////
    i = base_block_index
    while i > 0:
        end_of_current = correct_blocks[i - 1] + length
        start_of_next = correct_blocks[i]
        distance = start_of_next - end_of_current

        if distance < 0:  # 存在重叠
            # 检查前面是否有缝隙
            if i > 1:
                next_end = correct_blocks[i - 2] + length
                gap_after_next = correct_blocks[i - 1] - next_end
                if gap_after_next > 0:
                    # 使用重叠部分来填充缝隙
                    move_distance = min(max_move, min(-distance, gap_after_next))
                    correct_blocks[i - 1] -= move_distance

                    move_distance_sum += move_distance
                    is_success = False if max_move < min(-distance, gap_after_next) else True

        elif distance > 0:  # 存在缝隙
            # 确保移动不会产生新的缝隙
            if i == len(correct_blocks) - 1:
                # move_distance = min(max_move, distance)
                move_distance = distance
                correct_blocks[i] -= move_distance
                move_distance_sum += move_distance
            else:
                move_distance = min(max_move, distance)
                correct_blocks[i - 1] += move_distance

                move_distance_sum += move_distance
                is_success = False if max_move < distance else True
        i -= 1
    return correct_blocks, move_distance_sum, is_success


def roi_correct(blocks: list, max_move=1) -> list:
    optimal_blocks = []
    optimal_move_distance = 888  # 不能给0，否则不会更新

    # 以不同的 index 为基准平移，寻找最优移动方案
    # print("----------------------------------------------------------")
    for i in range(len(blocks)):
        correct_blocks, move_distance, is_success = fill_gaps(blocks, max_move=max_move, base_block_index=i)
        if (is_success is True) and (move_distance <= optimal_move_distance):
            # 如果移动的距离累计相等，取中心点
            if (move_distance == optimal_move_distance) and (i > len(blocks) / 2):
                continue
            optimal_blocks = correct_blocks
            optimal_move_distance = move_distance
            # print(i, move_distance, is_success)

    if not optimal_blocks:
        raise ValueError("光条缝隙太大，请尝试修改矫正阈值后再运行")
    return optimal_blocks


def CoorCorrect_1D(roi_data: list, cfg: dict) -> list:
    """
    对一维 ROI 数据进行矫正，减少 rolling 之间的间隙，影响成图效果
    Args:
        roi_data (list): ROI标定后的原始数据
        cfg (int): 配置信息

    Returns:
        list：矫正后的 ROI 数据
    """
    correct_roi_data = roi_data

    if cfg["roi_correct"] == 0 or cfg["SCAN_MODE"] == 1:  # 1D配置不进行矫正 或者 2D scan_mode不进行矫正
        return correct_roi_data

    vroll_num = len(correct_roi_data)
    h_vld_seg = len(correct_roi_data[0])

    for h_seg_cnt in range(0, h_vld_seg):
        v_coors_list = []
        v_pixel_list = []
        v_coors_dict = {}  # 矫正时需对坐标排序再进行矫正，因此需要记录实际矫正位置

        # 以段为单位解析每次 rolling 的坐标
        for vroll_cnt in range(0, vroll_num):
            v_coor = correct_roi_data[vroll_cnt][h_seg_cnt][1]
            v_coors_dict[v_coor] = vroll_cnt  # 记录实际矫正位置
            v_coors_list.append(v_coor)
            v_pixel_list.append(v_coor // 3)
        v_coors_list.sort()
        v_pixel_list.sort()

        # 按照 pixel进行矫正
        correct_pixel_list = roi_correct(v_pixel_list, cfg["correct_thres"])

        # 按照矫正的 pixel 对 ROI 进行矫正
        for vroll_cnt in range(0, vroll_num):
            act_roll = v_coors_dict[v_coors_list[vroll_cnt]]
            old_pixel_value = v_pixel_list[vroll_cnt]
            new_pixel_value = correct_pixel_list[vroll_cnt]
            if old_pixel_value == new_pixel_value:
                continue
            elif old_pixel_value < new_pixel_value:  # 像下矫正
                correct_coor = new_pixel_value * 3
            else:  # 像上矫正
                correct_coor = new_pixel_value * 3 + 2
            correct_roi_data[act_roll][h_seg_cnt][1] = correct_coor

    return correct_roi_data


def CaliResultDisplay(cali_data, ligth_imags, cfg):
    """融合ROI 标定数据和imag数据，成3D图像"""

    # 根据config文件赋值
    # ///////////////////////////////////////////////////////////////
    fp = cfg['file_path']
    scan_mode = cfg['SCAN_MODE']
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM'] if scan_mode == 1 else 0
    img_vld_seg = cfg['H_VLD_SEG'] if scan_mode == 1 else 0
    msk_intensity = cfg['msk_intensity']
    light_intensity = cfg['light_intensity']

    if not os.path.exists(fp):
        # 目录不存在，进行创建操作
        os.makedirs(fp)

    # 循环对所有图片进行识别，对图片进行融合
    # ///////////////////////////////////////////////////////////////
    spad_array_3D = np.zeros((576, 768, 3))
    fusion_image = np.zeros((576, 768))  # 融合所有图片的光条
    fusion_spad_array = np.zeros((576, 768))  # 融合所有开启的SPAD

    for vroll_cnt in range(v_roll_num + 1):
        for hroll_cnt in range(h_roll_num + 1):
            roll_cnt = vroll_cnt * (h_roll_num + 1) + hroll_cnt
            sub_spad_array_3D = np.zeros((576, 768, 3))
            spad_array = np.zeros((576, 768))  # 展示masking效果：使用标定算法找到的ROI开启的spad，此矩阵对应位置会被打开

            # 光条二维数组
            img = ligth_imags[roll_cnt]

            per_img_roi_data = cali_data[roll_cnt]
            for coors in per_img_roi_data:
                v_spad_c = coors[1]
                seg_num = coors[0]
                spad_array[v_spad_c: v_spad_c + 18, seg_num * 48: (seg_num + img_vld_seg + 1) * 48] = 1

            # plt.imshow(spad_array)
            # plt.show()
            # 融合光条和 ROI 数组, 成图展示标定效果
            sub_spad_array_3D[:, :, 0] = img
            sub_spad_array_3D[:, :, 2] = spad_array * 0.8

            file_path = "{}\\Roll{}_{}.png".format(fp, vroll_cnt, hroll_cnt)
            plt.imsave(file_path, sub_spad_array_3D)

            fusion_image += img
            fusion_spad_array += spad_array

    # 对整图数据进行处理，确保可以保存
    # ///////////////////////////////////////////////////////////////
    fusion_spad_array = np.where(fusion_spad_array <= 1, fusion_spad_array, 1)
    spad_array_3D[:, :, 2] = fusion_spad_array * msk_intensity / 100

    fusion_image = fusion_image / (fusion_image.max() / 2)  # 光条一般只会重叠一次，因此进行衰减
    fusion_image = np.where(fusion_image <= 1, fusion_image, 1)
    spad_array_3D[:, :, 0] = fusion_image * light_intensity / 100

    # 成图或者保存图片
    # plt.figure()
    # plt.title("Image")
    # plt.imshow(fusion_image_tmp)
    # plt.colorbar()
    # plt.figure()
    # plt.title("Masking")
    # plt.imshow(spad_array_3D)
    # plt.colorbar()
    # plt.show()

    # 保存图像
    # ///////////////////////////////////////////////////////////////
    f1 = "{}\\{}.png".format(fp, "fusion_imag")
    f2 = "{}\\{}.png".format(fp, "fusion_msku")
    # plt.imsave(f1, fusion_image, vmax=fusion_image.max() / 2)
    plt.imsave(f1, fusion_image)
    plt.imsave(f2, spad_array_3D)


def MskuRoiGenerate(cali_data: list, cfg: dict) -> list:
    """
    根据标定数据和相关配置生成 Masking 相关的 ROI Data
    Args:
        cali_data (list):
        cfg (dict):

    Returns:
        list: msku_roi_mem
    """
    scan_mode = cfg['SCAN_MODE']
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM']
    # h_vld_seg = csru_cfg['H_VLD_SEG']

    start_roll = cfg['start_roll']

    roll_num = (v_roll_num + 1) if scan_mode == 0 else (h_roll_num + 1) * (v_roll_num + 1)
    if len(cali_data) != roll_num:
        raise ValueError("The calibration data does not match the data required to generate ROI.")

    # 按分区生成 MSKU ROI Data
    # ///////////////////////////////////////////////////////////////
    msku_roi_mem = []
    per_rolling_roi_mem = []

    if scan_mode == 0:
        for vroll_cnt in range(v_roll_num + 1):
            # per_rolling_roi_data = cali_data[vroll_cnt]
            roll_cnt = vroll_cnt
            index = (roll_cnt + start_roll) % roll_num
            per_img_roi_data = cali_data[index]
            for j in range(0, 6):
                # for seg_light_vs in per_rolling_roi_data:
                for seg_datas in per_img_roi_data:  # seg_datas = [seg_num, v_spad_index]
                    seg_num = seg_datas[0]
                    # v_spad_c = info[1] + j * 3 + int(vroll_cnt * 2.5)
                    v_spad_c = seg_datas[1] + j * 3
                    per_rolling_roi_mem.append((seg_num << 10) + v_spad_c)
            msku_roi_mem.append(per_rolling_roi_mem)
            per_rolling_roi_mem = []
    else:
        roll_cnt = 0
        for vroll_cnt in range(v_roll_num + 1):
            for hroll_cnt in range(h_roll_num + 1):
                index = (roll_cnt + start_roll) % roll_num
                per_img_roi_data = cali_data[index]
                for j in range(0, 6):
                    seg_num = per_img_roi_data[0][0]
                    v_spad_c = per_img_roi_data[0][1] + j * 3
                    per_rolling_roi_mem.append((seg_num << 10) + v_spad_c)
                roll_cnt += 1
            msku_roi_mem.append(per_rolling_roi_mem)
            per_rolling_roi_mem = []

    return msku_roi_mem


def RoiMemGenerate(cali_data, cfg):
    """
    逐步调用 MskuRoiGenerate()、ZonesConfigGenerate()方法生成 ROI Data
    Args:
        cali_data (list): 标定数据
        cfg (dict): 配置数据

    Returns:
        None: 无返回值
    """
    roi_data = []
    try:
        msku_roi_mem = MskuRoiGenerate(cfg=cfg, cali_data=cali_data)
    except BaseException as msg:
        raise msg

    try:
        zones_config = MskuPubMethod.ZonesConfigGenerate(cfg=cfg)
    except BaseException as msg:
        raise msg

    for vroll_cnt in range(len(msku_roi_mem)):
        per_zone_mem = zones_config[vroll_cnt] + msku_roi_mem[vroll_cnt]
        roi_data = roi_data + per_zone_mem

    MskuPubMethod.roi_imag(msku_roi_mem, cfg, fd_path=cfg['file_path'])  # 成图

    MskuPubMethod.roi_data_save(f_name=f"{cfg['roi_name']}.txt", data=roi_data, fd_path=cfg["file_path"])

    print("ROI 生成完成！！！")
    return


def do_work(config_file):
    cfg = PubMethod.ReadJsonFile(config_file)
    scan_mode = cfg['SCAN_MODE']
    v_roll_num = cfg['V_ROLL_NUM']
    h_roll_num = cfg['H_ROLL_NUM']
    h_vld_seg = cfg['H_VLD_SEG']

    # Check配置数据是否正确
    # ///////////////////////////////////////////////////////////////
    if v_roll_num > 31 or h_roll_num > 15 or h_vld_seg > 15:
        raise ValueError(
            "寄存器相关值配置错误：v_roll_num:{}, v_roll_num:{}, h_vld_seg:{}".format(v_roll_num, h_roll_num, h_vld_seg))
    roll_num = (v_roll_num + 1) if scan_mode == 0 else (h_roll_num + 1) * (v_roll_num + 1)

    # 获取 .raw 标定文件，并按照给定要求返回字典
    # ///////////////////////////////////////////////////////////////
    file_dict = get_pcm_file(cfg['fd_path'], cfg["cali_frm_num"])
    if len(file_dict) != roll_num:
        raise ValueError("文件数据错误：ROI标定需要{}个文件，实际只有{}个文件".format(roll_num, len(file_dict)))

    # 标定，返回标定数据
    # ///////////////////////////////////////////////////////////////
    _img_roi_datas = GetRoiDataFromAllImags(file_dict, cfg)
    # print(_img_roi_datas)

    # 对标定的原始数据按照配置进行矫正，消除黑条
    # ///////////////////////////////////////////////////////////////
    img_roi_datas = CoorCorrect_1D(_img_roi_datas, cfg)

    # 保存标定效果图片
    # ///////////////////////////////////////////////////////////////
    print("标定信息保存中...")
    light_imags = GlobalDef.light_imags
    CaliResultDisplay(img_roi_datas, light_imags, cfg)

    # 生成ROI Data
    # ///////////////////////////////////////////////////////////////
    RoiMemGenerate(img_roi_datas, cfg)
    return


if __name__ == '__main__':
    # try:
    #     logs = do_work('MskuCalibration_cfg.json')
    # except BaseException as msg:
    #     logs = msg

    do_work('MskuCalibrationConfig.json')
    plt.show()

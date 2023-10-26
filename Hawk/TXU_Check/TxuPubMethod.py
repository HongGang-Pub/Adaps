import Hawk.Common.HawkPubMethod
from SelfDefinedPackge import PubMethod
from Hawk.Common import HawkPubMethod
from Hawk.Common import MipiPubMethod


def get_golden_data(f, work_mode, seg_hs, h_vld_seg, v_pixel_out_num, hroll_num, scan_mode, h_seg_shift=4):
    gld_data = []
    data = []
    if f == "NoCheck":
        gld_data = ["NoCheck!!!"]
        return gld_data
    else:
        frame_data = PubMethod.read_file(fname=f)
        if len(frame_data) == 0:
            raise ValueError("[Param] 指定的golden_data文件为空。")

        try:
            if work_mode == 2 or work_mode == 3:
                if scan_mode == 0:
                    for i in range(v_pixel_out_num):
                        start_index = i * 16 * 4 + 4 * seg_hs
                        data.extend(frame_data[start_index:start_index + (h_vld_seg + 1) * 4])
                    gld_data.append(data)
                else:
                    for h_roll_cnt in range(hroll_num + 1):
                        for i in range(v_pixel_out_num):
                            start_index = i * 16 * 4 + 4 * (seg_hs + h_seg_shift * h_roll_cnt)
                            if seg_hs + h_seg_shift * h_roll_cnt + h_vld_seg > 15:  # 超边界情况处理
                                seg_num = 15 - (seg_hs + h_seg_shift * h_roll_cnt)
                                _data = frame_data[start_index:start_index + (seg_num + 1) * 4]
                                out_len = h_vld_seg - seg_num
                                for out_index in range(out_len):
                                    _data.extend(_data[-4:])
                                data.extend(_data)
                            else:  # 正常二维扫描处理
                                data.extend(frame_data[start_index:start_index + (h_vld_seg + 1) * 4])
                        gld_data.append(data)
                        data = []
            elif work_mode == 0 or work_mode == 1:
                # with open(f_name, 'r', encoding='utf-8') as f_name:
                #     frame_data = f_name.readlines()
                if scan_mode == 0:
                    start_index = 16 * seg_hs
                    data.extend(frame_data[start_index:start_index + (h_vld_seg + 1) * 16])
                    gld_data.append(data)
                else:
                    for h_roll_cnt in range(hroll_num + 1):
                        start_index = 16 * (seg_hs + h_seg_shift * h_roll_cnt)
                        if seg_hs + h_seg_shift * h_roll_cnt + h_vld_seg > 15:  # 超边界情况处理
                            seg_num = 15 - (seg_hs + h_seg_shift * h_roll_cnt)
                            _data = frame_data[start_index:start_index + (seg_num + 1) * 16]
                            out_len = h_vld_seg - seg_num
                            for out_index in range(out_len):
                                _data.extend(_data[-16:])
                            data.extend(_data)
                        else:  # 正常二维扫描处理
                            data.extend(frame_data[start_index:start_index + (h_vld_seg + 1) * 16])
                        gld_data.append(data)
                        data = []
            return gld_data
        except IndexError as msg:
            raise ValueError("[Param] 构造Golden data失败，请检查配置是否正确。")


def cal_subframe_num(scan_mode, work_mode, tx_frame_mode, v_roll_num, h_roll_num):
    # 计算一个.txt文件有多少个subframe
    if tx_frame_mode == 1:
        if scan_mode == 0:
            if work_mode == 3:
                subframe_num_in_onefile = (v_roll_num + 1) * 9
            else:
                subframe_num_in_onefile = v_roll_num + 1
        else:
            subframe_num_in_onefile = (v_roll_num + 1) * (h_roll_num + 1)
    else:
        subframe_num_in_onefile = 1
    return subframe_num_in_onefile


def hist_testen_mipi_pkg_chk(cmp_data=None, base_data=None, wc=0):
    if base_data is None:
        base_data = []
    if cmp_data is None:
        cmp_data = []
    for i in range(len(cmp_data)):
        _cmp_data = cmp_data[i].split(" ")
        _base_data = base_data[i].split(" ")

        wc_l = int(_cmp_data[1], 16)  # data_frame_id L
        wc_h = int(_cmp_data[2], 16)  # data_frame_id H
        act_wc = wc_h * 256 + wc_l
        pkg_len = int(act_wc / 1.5)

        if wc != act_wc:
            return "WC_Error!"
        elif _cmp_data[0] != _base_data[0]:  # Data type check
            return "DT_Error!"
        elif _cmp_data[4:4 + pkg_len] != _base_data[4:4 + pkg_len]:  # playload check
            return "Data_Error"
        elif len(_cmp_data) == len(_base_data) and _cmp_data[-3:-1] != _base_data[-3:-1]:  # Packge foot check
            return "PKGF_Error"
        else:
            return "Success!!!"


def fuzzy_match_mipi_pkg_chk(cmp_data=None, base_data=None, threshold=10, wc=0, f_idx=0, sub_cnt=0, file_path=''):
    """
    f_idx & sub_cnt：用于生成存储文件名，区分每帧数据，文件名：mipi_f_idx_sub_cnt.txt
    """
    file_name = "mipi_{}_{}.txt".format(f_idx, sub_cnt)
    if base_data is None:
        base_data = []
    if cmp_data is None:
        cmp_data = []
    for i in range(len(cmp_data)):
        _cmp_data = cmp_data[i].split(" ")
        _base_data = base_data[i].split(" ")

        wc_l = int(_cmp_data[1], 16)  # data_frame_id L
        wc_h = int(_cmp_data[2], 16)  # data_frame_id H
        act_wc = wc_h * 256 + wc_l
        pkg_len = int(act_wc / 1.5)
        cmp_ans = []
        max_value = 0

        if wc != act_wc:
            return "WC_Error!"
        elif _cmp_data[0] != _base_data[0]:  # Data type check
            return "DT_Error!"
        else:
            for index in range(4, 4 + pkg_len):
                value = int(_cmp_data[index], 16) - int(_base_data[index], 16)
                cmp_ans.append(value)
                max_value = max_value if abs(value) < max_value else abs(value)
            is_cover = 1 if i == 0 else 0  # 第一次覆盖写入，后续新增写入

            file = PubMethod.data_save(fname=file_name, data_list=cmp_ans, split=' ', is_cover=is_cover, fd_path=file_path)
    # log = "模糊匹配比对文件存储路径"
    # print("{}: {}".format(log, file))

    if max_value > threshold:
        return "Max_value:{}".format(max_value)
    else:
        return "Success!!!"


def do_chk(cfg, mipi_fd_path="", golden_fp_list=[], hist_testen=1, threshold=10, file_path='.', **kwargs):
    """
    对MIPI数据进行check，包括：frame information，MIPI数据正确性check。
    hist_testen=1进行精准匹配；hist_testen=0进行模糊匹配。

    Args:
        cfg (dict): 寄存器配置信息
        mipi_fd_path (str): 需要check的MIPI数据存储路径
        golden_fp_list (list): 基准数据路径：hist_test=0 & work_mode=0，golden_fp需要有9帧数据，其他情况只需要1帧数据
        hist_testen (int): 0：hist_tesen=0, 1: hist_testen=1
        threshold (int): 阈值，模糊匹配时bin_num比较的阈值，如果超过阈值，则认为Mipi cali_data error
        file_path (str): 比对产生的相关日志存储路径
        **kwargs (any): None

    Returns:
        dict: chk_dict = {"flag": 1,
                          "log": "",
                          "frame_info": [],
                          "gld_data": [],
                          "file" :f_dict,
                          "subframe_info":[{f_idx, vroll_num, hroll_num}]
                          }

    """

    work_mode = cfg["work_mode"]
    scan_mode = cfg["scan_mode"]
    seg_hs = cfg["seg_hs"]
    h_vld_seg = cfg["h_vld_seg"]
    v_pxl_out_num = cfg["v_pxl_out_num"]
    tx_frame_mode = cfg["tx_frame_mode"]
    v_roll_num = cfg["v_roll_num"]
    h_roll_num = cfg["h_roll_num"]
    h_seg_shift = cfg["h_seg_shift"]
    out_bin_num = cfg["out_bin_num"]
    one_dt_mode = cfg["one_dt_mode"]
    log1 = "frame_info"
    log2 = "golden_data"

    chk_dict = {"flag": 1,  # 文件比对标志，存在相关错误时value=0，读取log信息查看相关错误类型
                "log": "比对无异常！！！",  # 返回错误类型
                "gld_data": [],  # golden cali_data
                "frame_info": [],  # 每sub帧信息比对结果
                "file": {},  # 读取的MIPI文件列表
                "subframe_info": []  # 按照sub帧返回frame information，包含：文件索引，以及当前文件对应的vroll_num, hroll_num信息
                }

    frame_info = []
    lane_data_info = []
    error_symbol = 0
    loss_pkg_symbol = 0
    loss_subframe_symbol = 0
    compare_log = []

    aim_data_type = 0x2C if one_dt_mode == 1 else 0x30

    v_pixel_out_num = 6 if v_pxl_out_num == 1 else 1

    subframe_num_in_onefile = cal_subframe_num(scan_mode=scan_mode, tx_frame_mode=tx_frame_mode, work_mode=work_mode,
                                               h_roll_num=h_roll_num, v_roll_num=v_roll_num)

    """对传入的golden_file_path进行检车"""
    if hist_testen == 0 and work_mode == 3 and len(golden_fp_list) != 9:
        # chk_dict["flag"] = 0
        chk_dict["log"] = "golden_fp_list没有足够的文件！"
        # return chk_dict
        raise ValueError(chk_dict["log"])

    if (hist_testen == 1 or work_mode != 3) and len(golden_fp_list) != 1:
        # chk_dict["flag"] = 0
        chk_dict["log"] = "golden_fp_list没有足够的文件！"
        # return chk_dict
        raise ValueError(chk_dict["log"])

    golden_fp = golden_fp_list[0]
    gld_data = get_golden_data(f=golden_fp,
                               work_mode=work_mode,
                               seg_hs=seg_hs,
                               h_vld_seg=h_vld_seg,
                               v_pixel_out_num=v_pixel_out_num,
                               hroll_num=h_roll_num,
                               scan_mode=scan_mode,
                               h_seg_shift=h_seg_shift)

    pkg_num = Hawk.Common.HawkPubMethod.cal_pkg_num(cfg)
    # print("PKG_num: {}; Subframe_num_in_onefile: {}".format(pkg_num, subframe_num_in_onefile))

    file_dict = HawkPubMethod.GetMipiFile(fd_path=mipi_fd_path)
    chk_dict["file"] = file_dict

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    frame_num = 0
    sub_frame_num = 0
    # for f_idx in file_index_list[0:1]:
    for f_idx in file_index_list:
        frame_num += 1
        subframe_loss_pkg_cnt = 0
        file = file_dict[f_idx]

        frame_data = PubMethod.read_file(file)
        actual_pkg_num = len(frame_data)

        if actual_pkg_num == 0:
            chk_dict["log"] = "读取的MIPI数据为空，请检查。[FILE]: {}".format(file)
            raise ValueError(chk_dict["log"])

        # 通过package number数量check脚本与MIPI数据是否匹配
        expect_pkg_num = pkg_num * subframe_num_in_onefile
        if actual_pkg_num > expect_pkg_num + 10 or actual_pkg_num < expect_pkg_num - 10:
            # chk_dict["flag"] = 0
            # print(file)
            chk_dict["log"] = "脚本与MIPI数据可能不匹配，请检查脚本或者重新抓取MIPI数据!!! [FILE]: {}".format(file)
            # return chk_dict
            raise ValueError(chk_dict["log"])
            # continue

        # 多帧合一且 one_dt_mode=1时，只进行丢帧检查
        if tx_frame_mode == 1 and one_dt_mode == 1:
            if subframe_num_in_onefile * pkg_num > actual_pkg_num:
                frame_info.append("Loss ImageFrame Data!")
                continue

        for sub_cnt in range(subframe_num_in_onefile):
            sub_frame_num += 1
            subframe_start_index = sub_cnt * pkg_num - subframe_loss_pkg_cnt
            info = frame_data[subframe_start_index:subframe_start_index + pkg_num]
            if len(info) == 0:
                # chk_dict["flag"] = 0
                chk_dict["log"] = "读取的MIPI数据为空，请检查。[FILE]: {}".format(file)
                # data_save(fname="frame_info.txt", data_list=["读取数据为空，请检查MIPI数据或脚本配置是否正确！！！"],
                #           split='\n', fd_path=fd_path, note=log1)
                # return chk_dict
                raise ValueError(chk_dict["log"])

            """多帧合一，且one_dt_mode=0时，通过DT判断是否丢包"""
            if one_dt_mode == 0:
                while len(info) > 0:
                    __info__ = info[-1].split(" ")
                    _data_type = int(__info__[0], 16) % 64
                    if _data_type != 0x30:
                        info.pop()
                        subframe_loss_pkg_cnt += 1
                    else:
                        break
            if len(info) == 0:
                # chk_dict["flag"] = 0
                chk_dict["log"] = "获取到的Frame information为空，请检查脚本配置是否正确！！！"
                # data_save(fname="frame_info.txt",
                #           data_list=["获取到的Frame information为空，请检查脚本配置是否正确！！！"], split='\n',
                #           fd_path=fd_path, note=log1)
                # return chk_dict
                raise ValueError(chk_dict["log"])
            # print(subframe_start_index, sub_cnt, subframe_loss_pkg_cnt)

            """获取frame information"""
            for data in info[-2:]:
                subframe_info = data.split(" ")
                data_type = int(subframe_info[0], 16) % 64
                id_l = int(subframe_info[4], 16)  # data_frame_id L
                id_h = int(subframe_info[5], 16)  # data_frame_id H
                if one_dt_mode == 0:
                    # cur hroll num: 2'b0, 1'b roisram_num, 1'b syscfg_grpsw, 4'b cur_hroll_num
                    hroll_num = int(subframe_info[6], 16) % 16
                    vroll_num = int(subframe_info[7], 16)  # 5'b cur_vroll_num
                    frame_id = id_h * 256 + id_l
                else:
                    cur_roll_num = int(subframe_info[6], 16)
                    hroll_num = cur_roll_num % 16
                    vroll_num = cur_roll_num // 64
                    frame_id = id_h * (2 ^ 12) + id_l
                lane_data_info.append([data_type, frame_id, hroll_num, vroll_num])

            """Check frame information是否正确，比较内容：Lane0和Lane1的数据是否相同，Data Type是否正确"""
            if lane_data_info[0] != lane_data_info[1] or data_type != aim_data_type:
                lane_log = "Lane_Erro: DT:{:2X}, frame_id:{}, vroll_num:{:>2}, hroll_num:{:>2}".format(
                    data_type, frame_id, vroll_num, hroll_num)
            else:
                lane_log = "Lane_info: DT:{:2X}, frame_id:{}, vroll_num:{:>2}, hroll_num:{:>2}".format(
                    data_type, frame_id, vroll_num, hroll_num)

                # 对于frame information正确且没有丢包的数据，存储subframe info信息
                if len(info) == pkg_num:
                    chk_dict["subframe_info"].append(
                        {'file_index': f_idx, 'vroll_num': vroll_num, 'hroll_num': hroll_num})

            """进行MIPI数据比对"""
            if golden_fp != "NoCheck":
                index = 0 if scan_mode == 0 else hroll_num
                if len(info) == pkg_num:
                    subframe_data = info[:-2]
                    word_cnt, flnr = Hawk.Common.HawkPubMethod.CalMipiFlnrAndWC(cfg)
                    if hist_testen == 1:
                        """"精准匹配"""
                        cmp_answer = hist_testen_mipi_pkg_chk(cmp_data=subframe_data,
                                                              base_data=gld_data[index],
                                                              wc=word_cnt)
                    else:
                        """模糊匹配"""
                        if hist_testen == 0 and work_mode == 3:
                            # 如果为模糊匹配且PCM模式，9次rolling的比对基准数据不同
                            golden_fp = golden_fp_list[hroll_num]
                            gld_data = get_golden_data(f=golden_fp,
                                                       work_mode=work_mode,
                                                       seg_hs=seg_hs,
                                                       h_vld_seg=h_vld_seg,
                                                       v_pixel_out_num=v_pixel_out_num,
                                                       hroll_num=h_roll_num,
                                                       scan_mode=scan_mode,
                                                       h_seg_shift=h_seg_shift)

                        cmp_answer = fuzzy_match_mipi_pkg_chk(cmp_data=subframe_data,
                                                              base_data=gld_data[index],
                                                              threshold=threshold,
                                                              wc=word_cnt,
                                                              f_idx=f_idx,
                                                              sub_cnt=sub_cnt,
                                                              file_path=file_path)
                    # 记录匹配日志文件
                    compare_log.append("文件比对：mipiData-{} -> {}".format(f_idx, golden_fp))
                    if cmp_answer != "Success!!!":
                        error_symbol += 1
                else:
                    # 对于丢包的数据，打印丢包日志，不进行数据匹配
                    loss_pkg_num = pkg_num - len(info)
                    cmp_answer = "PKG_Loss:{}".format(loss_pkg_num)
                    loss_pkg_symbol += 1
            else:
                cmp_answer = "No MIPI Check!!!"
                compare_log.append("NoCheck!!!")
                error_symbol = -1  # 返回-1，表示NoCheck

            """格式化打印信息"""
            file_sp1 = file.split("\\")
            file_sp2 = file_sp1[-1].split("-")
            file_name = "{}-{:>04}".format(file_sp2[0], int(file_sp2[1]))
            frame_log = "{}: cmp_answer: {:<10}; {}".format(file_name, cmp_answer, lane_log)

            """通过Frame_id检查是否丢帧"""
            if len(frame_info) > 0 and pre_frame_id + 1 != frame_id and tx_frame_mode == 0:
                loss_subframe_symbol += 1
                frame_info.append("Loss SubFrame Data!")
                pre_frame_id = frame_id
            else:
                pre_frame_id = frame_id
            frame_info.append(frame_log)

            lane_data_info = []
    chk_dict['gld_data'] = gld_data
    chk_dict["frame_info"] = frame_info
    answer = "Frame num: {}; Subrame num: {}; Loss_subframe: {}; Data_error: {}; Packge_loss: {}".format(
        frame_num, sub_frame_num, loss_subframe_symbol, error_symbol, loss_pkg_symbol)
    chk_dict["log"] = answer

    """Do Save"""
    if chk_dict['flag'] != 0:
        PubMethod.data_save(fname="frame_info.txt", data_list=chk_dict["frame_info"], split='\n', fd_path=file_path, note=log1)
        PubMethod.data_save(fname="compare_log.txt", data_list=compare_log, split='\n', fd_path=file_path, note="比对文件日志")

        file_data = []
        for gld_data in chk_dict['gld_data']:
            file_data.extend(gld_data)
        PubMethod.data_save(fname="golden_data.txt", data_list=file_data, split='', fd_path=file_path, note=log2)
    return chk_dict

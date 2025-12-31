#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : Eagle01PubMethod.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    :

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025-10-30 10:25    honggang_li    v1.0        

=================================================================================================
"""
import logging

# ///////////////////////////////////////////////
# Parameter
# ///////////////////////////////////////////////
TSEG_NUM = 4
ANGLE_GRP_NUM = 6
TX_NUM = 4
SEG_NUM = 16
SIGNAL_HOLD = 4
SRAM_CFG_NUM = 4


def expo_time_cal(sram_cs_sel):
    tseg_expo_time = [0 for i in range(TX_NUM)]

    MARGIN = 200

    # 列表定义
    expo_time = [0, 0, 0, 0]  # expo_time N channel: unit: ns
    ref_expo_lasprd = 0  # 13位无符号整数
    main_expo_lasprd = 0  # 13位无符号整数
    expo_trgo_en = [0, 0, 0, 0]  # 4个1位布尔值
    ambi_expo_time_reg = 0  # 13位无符号整数
    ambi_start_sel = 0  # 1位布尔值
    ref_shot_num = [0, 0, 0, 0]  # 4个4位无符号整数
    main_shot_num = [0, 0, 0, 0]  # 4个8位无符号整数
    sub_shotnum = [0, 0, 0, 0]  # 4个整数
    ref_expo_time = [0, 0, 0, 0]  # 4个整数
    main_expo_time = [0, 0, 0, 0]  # 4个整数
    trg_expo_time = [0, 0, 0, 0]  # 4个整数

    # 外部数据列表（需要在其他地方初始化）
    tsegx_ref_shot_num = []  # 4个整数
    tsegx_main_shot_num = []  # 4个整数
    ref_trgo_period = []  # 4个整数
    main_trgo_period = []  # 4个整数
    ambi_expo_time = []  # 4个整数
    ambi_expo_start_sel = []  # 1位布尔值
    ambi_light_en = []  # 1位布尔值
    # cs_tseg_expo_time = []

    # 从相应的数组中获取值（这里需要根据实际情况调整数据来源）
    ref_shot_num = tsegx_ref_shot_num[sram_cs_sel]
    main_shot_num = tsegx_main_shot_num[sram_cs_sel]
    ref_expo_lasprd = 1 + ref_trgo_period[sram_cs_sel]
    main_expo_lasprd = 1 + main_trgo_period[sram_cs_sel]
    ambi_expo_time_reg = ambi_expo_time[sram_cs_sel]
    ambi_start_sel = ambi_expo_start_sel[sram_cs_sel]

    for chnl in range(4):
        sub_shotnum[chnl] = main_shot_num[chnl] + ref_shot_num[chnl]
        ref_expo_time[chnl] = ref_shot_num[chnl] * ref_expo_lasprd
        main_expo_time[chnl] = main_shot_num[chnl] * main_expo_lasprd

    for chnl in range(4):
        trg_expo_time[chnl] = ref_expo_time[chnl] + main_expo_time[chnl] + 2 + 3  # 2cycle gate 3cycle sync
        if ambi_light_en:
            if not ambi_start_sel:
                if (trg_expo_time[chnl] * 4) > ((ambi_expo_time_reg + 1) * 100):
                    expo_time[chnl] = (trg_expo_time[chnl] + 9) * 4
                else:
                    expo_time[chnl] = (ambi_expo_time_reg + 1) * 100 + 9 * 4
            else:
                expo_time[chnl] = trg_expo_time[chnl] * 4 + ambi_expo_time_reg * 100 + 18 * 4
        else:
            expo_time[chnl] = trg_expo_time[chnl] * 4 + 18 * 4

        expo_time[chnl] = expo_time[chnl] + MARGIN  # MARGIN=200

    tseg_expo_time = expo_time
    return tseg_expo_time


def mipi_config_cal(csru: dict):
    # ///////////////////////////////////////////////
    # Parameter
    # ///////////////////////////////////////////////
    RAW8 = 8
    RAW12 = 12
    SPOT_NUM = 6
    SEG_BLIND_NUM = 6
    AMBI_NUM = 9
    HIST_NUM = 9

    # ///////////////////////////////////////////////
    # REG_CFG
    # ///////////////////////////////////////////////
    mst_mode = csru['mst_mode']
    mst_ctrl_mode = csru['mst_ctrl_mode']
    work_mode = csru['work_mode']
    tseg_en = csru['tseg_en']
    segx_v_num = [27 for i in range(SEG_NUM)]  # TODO: 理论上应该根据实际情况进行处理
    tsegx_trgo_sel = [i for i in range(TSEG_NUM)]
    main_pixel_maxbin = csru['main_pixel_maxbin']
    main_pixel_minbin = csru['main_pixel_minbin']
    spot_pixel_maxbin = csru['spot_pixel_maxbin']
    spot_pixel_minbin = csru['spot_pixel_minbin']
    mipi_command_fifo_len = csru['mipi_command_fifo_len']

    mipi_dt = csru['mipi_dt']
    frame_info_en = csru['frame_info_en']
    slot_info_en = csru['slot_info_en']
    main_hist_pkt_en = csru['main_hist_pkt_en']
    blind_hist_pkt_en = csru['blind_hist_pkt_en']
    spot_hist_pkt_en = csru['spot_hist_pkt_en']
    echo_pkt_en = csru['echo_pkt_en']
    range_pkt_en = csru['range_pkt_en']
    range_depth_pkt_en = csru['range_depth_pkt_en']
    embeded_pkt_en = csru['embeded_pkt_en']
    ambi_pcm_pkt_en = csru['ambi_pcm_pkt_en']
    ambi_data_en = csru['ambi_data_en']
    nseg_echo_data_pack = csru['nseg_echo_data_pack']
    nseg_range_data_pack = csru['nseg_range_data_pack']
    pxl_binn_sel = csru['pxl_binn_sel']
    grpx_sw_num = csru['grpx_sw_num']
    grpx_subx_slot_num = csru['grpx_subx_slot_num']  # grpx_subx_slot_num[ANGLE_GRP_NUM][GRP_SW_NUM]
    grpx_subx_slot_sram = csru['grpx_subx_slot_sram']  # grpx_subx_slot_sram[ANGLE_GRP_NUM][GRP_SW_NUM]
    mpix_out_echo_num = csru['mpix_out_echo_num']
    bpix_out_echo_num = csru['bpix_out_echo_num']
    mpix_echo_total_intf_bin_num = csru['mpix_echo_total_intf_bin_num']
    mpix_echo_total_accu_bin_num = csru['mpix_echo_total_accu_bin_num']

    TSEG_ST = 0 if (tseg_en & 0b0001) else \
        1 if (tseg_en & 0b0010) else \
            2 if (tseg_en & 0b0100) else 3

    TSEG_END = 3 if (tseg_en & 0b1000) else \
        2 if (tseg_en & 0b0100) else \
            1 if (tseg_en & 0b0010) else 0

    TSEG_VLD_NUM = TSEG_END - TSEG_ST + 1
    
    minbin_thrs = main_pixel_minbin[0]          # main_pixel_minbin.max()
    maxbin_thrs = main_pixel_maxbin[0]          # main_pixel_maxbin.max()
    spot_minbin_thrs = spot_pixel_minbin[0]     # spot_pixel_minbin.max()
    spot_maxbin_thrs = spot_pixel_maxbin[0]     # spot_pixel_maxbin.max()
    pxl_extract_num = 0
    nseg_blind_hist_pack = TSEG_VLD_NUM # rm_dl.TOF_TXU.TXU_PACK_NSEG.NSEG_BLIN_HST_PACK.get_mirrored_value
    nseg_spot_hist_pack = 2     # rm_dl.TOF_TXU.TXU_PACK_NSEG.NSEG_SPOT_HST_PACK.get_mirrored_value
    nseg_echo_data_pack_cal = nseg_echo_data_pack + 1
    nseg_range_data_pack_cal = (nseg_range_data_pack + 1) * 2

    maxbin = (maxbin_thrs + 1) * 4 - 1
    minbin = minbin_thrs * 4
    spot_hist_maxbin = (spot_maxbin_thrs + 1) * 4 - 1
    spot_hist_minbin = spot_minbin_thrs * 4
    seg_main_pixel_num = 27 // (3 ** (pxl_binn_sel % 3))
    ptype = RAW8 if (mipi_dt == 0) else RAW12
    raw_type_factor = 1 if (mipi_dt == 0) else 1.5
    mpix_out_echo_num_cal = 6 if (mpix_out_echo_num >= 6) else mpix_out_echo_num + 1
    bpix_out_echo_num_cal = 6 if (bpix_out_echo_num >= 6) else bpix_out_echo_num + 1
    if mpix_echo_total_intf_bin_num % 2 != 0:
        raise ValueError(f"mpix_echo_total_intf_bin_num={mpix_echo_total_intf_bin_num} %2 !=0!!!")

    all_echo_bin_num = (6 * mpix_out_echo_num_cal + mpix_echo_total_accu_bin_num + mpix_echo_total_intf_bin_num) if mipi_dt == 0 \
        else (4 * mpix_out_echo_num_cal + mpix_echo_total_accu_bin_num + mpix_echo_total_intf_bin_num / 2)

    # ///////////////////////////////////////////////
    # Cal WC & FLNR
    # ///////////////////////////////////////////////
    adt_data_len = {}
    # -----------------------------------------------
    # main_hist_pl
    # -----------------------------------------------
    main_hist_one_pixel_pl   = (2+2+(maxbin-minbin+1)+(maxbin-minbin+1)/4)	                        # pixel_header+ref_data+acc hist+intf det hist
    main_hist_pl             = (6 + main_hist_one_pixel_pl * 3 + 4)	                                # payload_header+pixel_pl*pixel_num+crc32
    if main_hist_pl % 2 == 0:
        raise ValueError(f"main_hist_pl={main_hist_pl} % 2 != 0")
    main_hist_pkt_num = 0 if not main_hist_pkt_en else (seg_main_pixel_num*TSEG_VLD_NUM)//3
    adt_data_len["main_hist_pl"] = main_hist_pl - 4
    # -----------------------------------------------
    # blind_hist_pl
    # -----------------------------------------------
    blind_hist_one_pixel_pl  = (2+2+32+16)	                                                        # pixel_header+ref_data+blind hist+intf det hist
    blind_hist_pl            = (6+blind_hist_one_pixel_pl*SEG_BLIND_NUM*nseg_blind_hist_pack+4)	    # payload_header+pixel_pl*pixel_num+crc32
    blind_hist_pkt_num = 0 if not blind_hist_pkt_en else 1
    adt_data_len["main_hist_pl"] = blind_hist_pl - 4
    # -----------------------------------------------
    # spot_hist_pl
    # -----------------------------------------------
    spot_hist_one_pixel_pl   = (2+2+(spot_hist_maxbin-spot_hist_minbin+1)/4)	                    # pixel_header+spot hist
    spot_hist_pl             = (6+spot_hist_one_pixel_pl*SPOT_NUM*nseg_spot_hist_pack+4)	        # payload_header+pixel_pl*pixel_num+crc32
    main_echo_one_pixel_pl   = (2+6+all_echo_bin_num) if (mipi_dt == 0) else (2+4+all_echo_bin_num)	# pixel header+pixel common data+
    # -----------------------------------------------
    # echo_pl
    # -----------------------------------------------
    blind_echo_one_pixel_pl  = (2+2+32+8) if (mipi_dt == 0) else (2+2+32+4)
    echo_pl                  = (8+(main_echo_one_pixel_pl*seg_main_pixel_num+blind_echo_one_pixel_pl*SEG_BLIND_NUM)*nseg_echo_data_pack_cal+4) if (mipi_dt == 0) else \
                               (6+(main_echo_one_pixel_pl*seg_main_pixel_num+blind_echo_one_pixel_pl*SEG_BLIND_NUM)*nseg_echo_data_pack_cal+4)  # payload header+..+crc32
    # -----------------------------------------------
    # range_pl & range_depth_pl
    # -----------------------------------------------
    main_range_one_pixel_pl  = (2+6+24*mpix_out_echo_num_cal)	 # pixel header+pixel range common data+..
    blind_range_one_pixel_pl = (2+6+24*bpix_out_echo_num_cal)	 # pixel header+pixel range common data+..
    range_pl                 = (8+(main_range_one_pixel_pl*seg_main_pixel_num+blind_range_one_pixel_pl*SEG_BLIND_NUM)*nseg_range_data_pack_cal+4) if (mipi_dt == 0) else \
                               (6+(main_range_one_pixel_pl*seg_main_pixel_num+blind_range_one_pixel_pl*SEG_BLIND_NUM)*nseg_range_data_pack_cal+4)     # payload header+..+crc32
    range_depth_pl           = (8+((2+6+(23+5)*mpix_out_echo_num_cal)*seg_main_pixel_num+(2+6+(23+5)*bpix_out_echo_num_cal)*SEG_BLIND_NUM)*nseg_range_data_pack_cal+4) if (mipi_dt == 0) else \
                               (6+((2+6+(23+5)*mpix_out_echo_num_cal)*seg_main_pixel_num+(2+6+(23+5)*bpix_out_echo_num_cal)*SEG_BLIND_NUM)*nseg_range_data_pack_cal+4) # payload header+..+crc32
    # -----------------------------------------------
    # slot_pl
    # -----------------------------------------------
    slot_pl                  = (8 if mipi_dt == 0 else 6) + 28 + 4 + 20 + 2 + 20 + 4 + 4 + 16 + 4
    # -----------------------------------------------
    # embeded_pl
    # -----------------------------------------------
    slot_info_pl             = (32+320+28+4+20+2+20+4+4+16)	 # ambi pkt
    embeded_pl               = (8+4+slot_info_pl+(1296*4 if ambi_data_en else 0)+4) if (mipi_dt == 0) else (6+4+slot_info_pl+(1296*2 if ambi_data_en else 0)+4)
    # -----------------------------------------------
    # pcm_ambi_pl
    # -----------------------------------------------
    pcm_ambi_pl              = (8+2+2+16*AMBI_NUM*HIST_NUM*4+4) if (mipi_dt == 0) else (6+2+2+16*AMBI_NUM*HIST_NUM*2+4)
    # -----------------------------------------------
    # frame_info_len
    # -----------------------------------------------
    frame_info_len           = 8+8+128+2+mipi_command_fifo_len+4
    # -----------------------------------------------
    # pcm_hist_pl
    # -----------------------------------------------
    pcm_hist_pl              = 6+(2+1024)*TSEG_VLD_NUM*27

    return


def slot_time_cal(csru: dict):
    """
    slot time calculate
    Returns:

    """
    # ///////////////////////////////////////////////
    # Parameter
    # ///////////////////////////////////////////////
    TSEG_NUM = 4
    ANGLE_GRP_NUM = 6
    TX_NUM = 4
    SEG_NUM = 16
    SIGNAL_HOLD = 4
    SRAM_CFG_NUM = 4
    MARGIN = 1000  # unit: ns

    # ///////////////////////////////////////////////
    # Return
    # ///////////////////////////////////////////////
    tsegx_trg_expo_delay = [[0 for i in range(TX_NUM)] for j in range(SRAM_CFG_NUM)]
    grpx_slot_time = [0 for i in range(ANGLE_GRP_NUM)]
    frm_idle_time = 0

    # ///////////////////////////////////////////////
    # System config
    # ///////////////////////////////////////////////
    tseg_expo_diff = 0  # 0: No time-sharing zoning 1: Time-sharning zoning
    SYSC_CLK = 400  # unit: MHz
    TDC_CLK = 250  # unit: MHz
    MIPI_RATE = 2500  # unit: Gbps
    MIPI_LANE_NUM = 4
    MIPI_PKT_INTV = 1000  # unit: ns
    MIPI_FIFO_SIZE = 960

    # ///////////////////////////////////////////////
    # REG_CFG
    # ///////////////////////////////////////////////
    mst_mode = csru['mst_mode']
    mst_ctrl_mode = csru['mst_ctrl_mode']
    work_mode = csru['work_mode']
    tseg_en = csru['tseg_en']
    segx_v_num = [27 for i in range(SEG_NUM)]  # TODO: 理论上应该根据实际情况进行处理
    tsegx_trgo_sel = [i for i in range(TSEG_NUM)]
    main_pixel_maxbin = csru['main_pixel_maxbin']
    main_pixel_minbin = csru['main_pixel_minbin']
    spot_pixel_maxbin = csru['spot_pixel_maxbin']
    spot_pixel_minbin = csru['spot_pixel_minbin']

    mipi_dt = csru['mipi_dt']
    frame_info_en = csru['frame_info_en']
    slot_info_en = csru['slot_info_en']
    main_hist_pkt_en = csru['main_hist_pkt_en']
    blind_hist_pkt_en = csru['blind_hist_pkt_en']
    spot_hist_pkt_en = csru['spot_hist_pkt_en']
    echo_pkt_en = csru['echo_pkt_en']
    range_pkt_en = csru['range_pkt_en']
    range_depth_pkt_en = csru['range_depth_pkt_en']
    embeded_pkt_en = csru['embeded_pkt_en']
    ambi_pcm_pkt_en = csru['ambi_pcm_pkt_en']
    nseg_echo_data_pack = csru['nseg_echo_data_pack']
    nseg_range_data_pack = csru['nseg_range_data_pack']
    pxl_binn_sel = csru['pxl_binn_sel']
    grpx_sw_num = csru['grpx_sw_num']
    grpx_subx_slot_num = csru['grpx_subx_slot_num']  # grpx_subx_slot_num[ANGLE_GRP_NUM][GRP_SW_NUM]
    grpx_subx_slot_sram = csru['grpx_subx_slot_sram']  # grpx_subx_slot_sram[ANGLE_GRP_NUM][GRP_SW_NUM]

    # ///////////////////////////////////////////////
    # Available
    # ///////////////////////////////////////////////
    tseg_mask_time = [0 for i in range(TSEG_NUM)]
    trgo_chn_mask_time = [0 for i in range(TSEG_NUM)]
    cs_tseg_expo_time = [[0 for i in range(TX_NUM)] for j in range(SRAM_CFG_NUM)]
    cs_hist_dsp_deal_time = [0 for i in range(SRAM_CFG_NUM)]
    cs_tseg_mipi_wastes_time = [[0 for i in range(TX_NUM)] for j in range(SRAM_CFG_NUM)]
    cs_slot_complete_time = [0 for i in range(SRAM_CFG_NUM)]
    cs_slot_release_time = [0 for i in range(SRAM_CFG_NUM)]
    cs_slot_min_time = [0 for i in range(SRAM_CFG_NUM)]
    T_grp_slot_time = [0 for i in range(ANGLE_GRP_NUM)]
    frame_idle_time = 0

    # ///////////////////////////////////////////////
    # Coding
    # ///////////////////////////////////////////////
    # -----------------------------------------------
    # Initial
    # -----------------------------------------------
    print("----------------------------------")
    print("Do slot_time cal")
    print("----------------------------------")
    if work_mode == 0b01 or work_mode == 0b11:  # Single && PCM not support
        return
    if tseg_en == 0:
        return

    DATA_MODE = []
    DATA_MODE[0] = 1 if (echo_pkt_en or range_pkt_en or range_depth_pkt_en) else 0
    DATA_MODE[1] = 1 if (main_hist_pkt_en or blind_hist_pkt_en or spot_hist_pkt_en) else 0

    TSEG_ST = 0 if (tseg_en & 0b0001) else \
        1 if (tseg_en & 0b0010) else \
            2 if (tseg_en & 0b0100) else 3

    TSEG_END = 3 if (tseg_en & 0b1000) else \
        2 if (tseg_en & 0b0100) else \
            1 if (tseg_en & 0b0010) else 0

    TSEG_VLD_NUM = TSEG_END - TSEG_ST + 1

    # -----------------------------------------------
    # Get TSEG masking time
    # -----------------------------------------------
    for tseg_idx in range(TSEG_ST, TSEG_END + 1):  # Each spad masking time -> tseg_masking_time
        mask_v_num = max(segx_v_num[tseg_idx * 4:(tseg_idx + 1) * 4])
        tseg_mask_time[tseg_idx] = int((mask_v_num + 2) * SIGNAL_HOLD * 2 * 1000.0 / SYSC_CLK)  # unit: ns
    print("  tseg_mask_time           (ns   ): ", tseg_mask_time)

    for tseg_idx in range(TSEG_ST, TSEG_END + 1):  # If TSEG trgo_sel is same, they need use the max masking time
        trgo_sel = tsegx_trgo_sel[tseg_idx]
        trgo_chn_mask_time[trgo_sel] = max(trgo_chn_mask_time[trgo_sel], tseg_mask_time[tseg_idx])

    for tseg_idx in range(TSEG_ST, TSEG_END + 1):  # Back mark every TSEG masking time
        trgo_sel = tsegx_trgo_sel[tseg_idx]
        tseg_mask_time[tseg_idx] = trgo_chn_mask_time[trgo_sel]
    print("  tseg_mask_time           (ns   ): ", tseg_mask_time)

    # -----------------------------------------------
    # Get A/B/C/D expo_time
    # -----------------------------------------------
    cs_tseg_expo_time = [[0 for i in range(TX_NUM)] for j in range(SRAM_CFG_NUM)]
    for sram_cfg_cnt in range(SRAM_CFG_NUM):  # TODO: Need get the real expo_time
        cs_tseg_expo_time[sram_cfg_cnt] = expo_time_cal(sram_cfg_cnt)
    print("  cs_tseg_expo_time        (ns   ): ", cs_tseg_expo_time)

    # -----------------------------------------------
    # Get A/B/C/D dsp_deal_tim
    # -----------------------------------------------
    for sram_cfg_cnt in range(SRAM_CFG_NUM):  # TODO: Need get the real expo_time
        pass
    print("  cs_hist_dsp_deal_time    (ns   ): ", cs_hist_dsp_deal_time)

    # -----------------------------------------------
    # Get A/B/C/D expo_delay
    # -----------------------------------------------
    expo_delay = 0
    for sram_cfg_cnt in range(SRAM_CFG_NUM):
        for tseg_idx in range(TSEG_ST, TSEG_END + 1):
            if tseg_idx == TSEG_ST or tseg_expo_diff == 0:
                expo_delay = 0
            else:
                pre_trgo_sel = tsegx_trgo_sel[tseg_idx - 1]
                trgo_sel = tsegx_trgo_sel[tseg_idx]
                if pre_trgo_sel == trgo_sel:
                    expo_delay = expo_delay
                else:
                    expo_delay = (expo_delay +
                                  tseg_mask_time[tseg_idx - 1] +
                                  cs_tseg_expo_time[sram_cfg_cnt][tseg_idx - 1] -
                                  tseg_mask_time[tseg_idx])

            tsegx_trg_expo_delay[sram_cfg_cnt][tseg_idx] = expo_delay if expo_delay == 0 \
                else (expo_delay // 100 + 1)  # unit: 0.1us
    print("  tsegx_trg_expo_delay     (0.1us): ", tsegx_trg_expo_delay)

    # -----------------------------------------------
    # Cal one pkt mipi send time
    # -----------------------------------------------
    wc = 0  # TODO: need cal WC
    frame_info_len = 0  # TODO: need cal WC
    mipi_rate = MIPI_RATE * MIPI_LANE_NUM
    raw_type_factor = 1 if mipi_dt == 0 else 1.5
    txu_rd_cyc = int(wc / raw_type_factor / 2)
    txu_rd_time = int(txu_rd_cyc * 1000 / SYSC_CLK)  # unit: ns
    one_pkt_mipi_time = int(wc * 8 * 100 / mipi_rate) + MIPI_PKT_INTV
    one_pkt_mipi_time = max(txu_rd_time, one_pkt_mipi_time)

    # -----------------------------------------------
    # Cal read time
    # -----------------------------------------------
    pxl_num_in_seg = int(27 / (3 ** (pxl_binn_sel % 3)))
    tseg_noise_cal_time = int(1000 / TDC_CLK * (255 + 20))
    main_hist_rd_time = 0 if not main_hist_pkt_en else int(((main_pixel_maxbin[0] + 1 - main_pixel_minbin[0]) * 4 + 10 + 14) * 3 * 1000 / SYSC_CLK)
    main_hist_rd_time = 0 if not main_hist_pkt_en else max(main_hist_rd_time, one_pkt_mipi_time)

    fs_rd_time = MIPI_PKT_INTV
    fram_info_rd_time = 0 if not frame_info_en else int((frame_info_len * 8 * 1000 / MIPI_RATE + MIPI_PKT_INTV))
    slot_info_rd_time = 0 if not slot_info_en else one_pkt_mipi_time
    tseg_echo_rd_time = 0 if not echo_pkt_en else one_pkt_mipi_time * (4 >> nseg_echo_data_pack)
    tseg_range_rd_time = 0 if not range_pkt_en else one_pkt_mipi_time * (2 >> nseg_range_data_pack)
    tseg_depth_rd_time = 0 if not range_depth_pkt_en else one_pkt_mipi_time * (2 >> nseg_range_data_pack)
    tseg_main_hist_rd_time = 0 if not main_hist_pkt_en else main_hist_rd_time * int(pxl_num_in_seg / 3) * 4
    tseg_spot_hist_rd_time = 0 if not spot_hist_pkt_en else one_pkt_mipi_time * 2
    blind_hist_rd_time = 0 if not blind_hist_pkt_en else one_pkt_mipi_time
    embeded_info_rd_time = 0 if not embeded_pkt_en else one_pkt_mipi_time
    ambi_pcm_rd_time = 0 if not ambi_pcm_pkt_en else one_pkt_mipi_time

    tseg_dsp_data_rd_time = tseg_echo_rd_time + tseg_range_rd_time + tseg_depth_rd_time
    fe_rd_time = MIPI_PKT_INTV

    slot_mipi_rd_time = (fs_rd_time +
                         fram_info_rd_time +
                         slot_info_rd_time +
                         tseg_dsp_data_rd_time * TSEG_VLD_NUM +
                         main_hist_rd_time * (DATA_MODE == [1, 0]) +
                         tseg_main_hist_rd_time * TSEG_VLD_NUM +
                         tseg_spot_hist_rd_time * TSEG_VLD_NUM +
                         blind_hist_rd_time +
                         embeded_info_rd_time +
                         ambi_pcm_rd_time +
                         fe_rd_time)

    tseg_parall_expo_rd_time = tseg_echo_rd_time if echo_pkt_en else \
        tseg_range_rd_time if range_pkt_en else \
            tseg_depth_rd_time if range_depth_pkt_en else \
                tseg_main_hist_rd_time if main_hist_pkt_en else \
                    0

    sysc_main_hist_rd_time = 0 if not main_hist_pkt_en else tseg_main_hist_rd_time
    sysc_spot_hist_rd_time = 0 if not spot_hist_pkt_en else int((24 + (spot_pixel_maxbin[0] - spot_pixel_minbin[0] + 1) * 5 + 23 * 4) * 1000 / SYSC_CLK)
    sysc_blind_hist_rd_time = 0 if not blind_hist_pkt_en else int(326 * 1000 / SYSC_CLK)

    print("  one_pkt_mipi_time        (ns   ): %0d", one_pkt_mipi_time)
    print("  main_hist_rd_time        (ns   ): %0d", main_hist_rd_time)
    print("  fram_info_rd_time        (ns   ): %0d", fram_info_rd_time)
    print("  slot_info_rd_time        (ns   ): %0d", slot_info_rd_time)
    print("  tseg_echo_rd_time        (ns   ): %0d", tseg_echo_rd_time)
    print("  tseg_range_rd_time       (ns   ): %0d", tseg_range_rd_time)
    print("  tseg_depth_rd_time       (ns   ): %0d", tseg_depth_rd_time)
    print("  tseg_dsp_data_rd_time    (ns   ): %0d", tseg_dsp_data_rd_time)
    print("  tseg_main_hist_rd_time   (ns   ): %0d", tseg_main_hist_rd_time)
    print("  tseg_spot_hist_rd_time   (ns   ): %0d", tseg_spot_hist_rd_time)
    print("  tseg_parall_expo_rd_time (ns   ): %0d", tseg_parall_expo_rd_time)
    print("  blind_hist_rd_time       (ns   ): %0d", blind_hist_rd_time)
    print("  embeded_info_rd_time     (ns   ): %0d", embeded_info_rd_time)
    print("  slot_mipi_rd_time        (ns   ): %0d", slot_mipi_rd_time)

    # -----------------------------------------------
    # Cal MIPI wastes time between TSEG
    # -----------------------------------------------
    for sram_cfg_cnt in range(SRAM_CFG_NUM):
        for tseg_idx in range(TSEG_ST, TSEG_END + 1):
            tseg_parall_expo_all_data_rd_time = ((fs_rd_time + fram_info_rd_time + slot_info_rd_time) if tseg_idx == (
                    TSEG_ST + 1) else 0) + tseg_parall_expo_rd_time
            if tseg_idx > TSEG_ST:  # From 2nd TSEG calculate MIPI wastes time
                T1 = tsegx_trg_expo_delay[sram_cfg_cnt][tseg_idx - 1] * 100 + tseg_mask_time[tseg_idx - 1] + \
                     cs_tseg_expo_time[sram_cfg_cnt][tseg_idx - 1]  # unit: ns
                T2 = tsegx_trg_expo_delay[sram_cfg_cnt][tseg_idx] * 100 + tseg_mask_time[tseg_idx] + \
                     cs_tseg_expo_time[sram_cfg_cnt][tseg_idx]  # unit: ns
                T3 = T2 - T1
                cs_tseg_mipi_wastes_time[sram_cfg_cnt][tseg_idx] = max(T3 - tseg_parall_expo_all_data_rd_time, 0)
    print("  cs_tseg_mipi_wastes_time (ns   ): ", cs_tseg_mipi_wastes_time)

    # -----------------------------------------------
    # Cal each CS slot_info
    # -----------------------------------------------
    for sram_cfg_cnt in range(SRAM_CFG_NUM):
        T1 = 0 if not (
                embeded_pkt_en | ambi_pcm_pkt_en) else int(81 * 16 * 1000 / SYSC_CLK)  # Amibi need time transfer to TXU buffer // TODO: It's can hide to dsp_deal
        cs_slot_complete_time[sram_cfg_cnt] = (tsegx_trg_expo_delay[sram_cfg_cnt][TSEG_ST] * 100 +
                                               tseg_mask_time[0] +
                                               cs_tseg_expo_time[sram_cfg_cnt][TSEG_ST] +
                                               tseg_noise_cal_time +
                                               cs_hist_dsp_deal_time[sram_cfg_cnt] +
                                               slot_mipi_rd_time +
                                               cs_tseg_mipi_wastes_time[sram_cfg_cnt][0] +
                                               cs_tseg_mipi_wastes_time[sram_cfg_cnt][1] +
                                               cs_tseg_mipi_wastes_time[sram_cfg_cnt][2] +
                                               cs_tseg_mipi_wastes_time[sram_cfg_cnt][3] +
                                               T1 + MARGIN)

        cs_slot_release_time[sram_cfg_cnt] = (tsegx_trg_expo_delay[sram_cfg_cnt][TSEG_ST] * 100 +
                                              tseg_mask_time[0] +
                                              cs_tseg_expo_time[sram_cfg_cnt][TSEG_ST] +
                                              tseg_noise_cal_time +
                                              cs_hist_dsp_deal_time[sram_cfg_cnt])

        # Consider the slot_info send (spot & zdd data is locked at the all TSEG expo done), slot_min_time is need promise
        # Get the last TSEG expo done time
        for tseg_idx in range(TSEG_ST, TSEG_END + 1):
            T1 = tseg_noise_cal_time
            T2 = 0 if not (embeded_pkt_en | ambi_pcm_pkt_en) else int(81 * 16 * 1000 / SYSC_CLK)
            tseg_slot_min_time = (tsegx_trg_expo_delay[sram_cfg_cnt][tseg_idx] * 100 +
                                  tseg_mask_time[tseg_idx] +
                                  cs_tseg_expo_time[sram_cfg_cnt][tseg_idx] +
                                  max(T1, T2) + MARGIN)
            if cs_slot_min_time[sram_cfg_cnt] < tseg_slot_min_time:  # Get the max value
                cs_slot_min_time[sram_cfg_cnt] = tseg_slot_min_time
    print("  cs_slot_complete_time    (ns   ): ", cs_slot_complete_time)
    print("  cs_slot_release_time     (ns   ): ", cs_slot_release_time)
    print("  cs_slot_min_time         (ns   ): ", cs_slot_min_time)

    for angle_grp_cnt in range(ANGLE_GRP_NUM):
        # Initial
        grpx_slot_time[angle_grp_cnt] = 0
        if mst_mode == 0 and angle_grp_cnt <= 4:  # Slave
            continue
        if mst_mode == 1 and mst_ctrl_mode == 0 and angle_grp_cnt == 5:  # Angle_trig
            continue
        if mst_mode == 1 and mst_ctrl_mode == 1 and angle_grp_cnt <= 4:  # Timer_trig
            continue
        # -----------------------------------------------
        # Get the group CS send sequence
        # -----------------------------------------------
        grp_cs_sel_seq = []
        grp_sw_num = grpx_sw_num[angle_grp_cnt]

        for grp_sw_cnt in range(grp_sw_num + 1):
            # Get and deal slot_num
            slot_num = grpx_subx_slot_num[angle_grp_cnt][grp_sw_cnt]
            slot_sram = grpx_subx_slot_sram[angle_grp_cnt][grp_sw_cnt]
            slot_num = 1 if (slot_num >= 1) else 0
            for slot_cnt in range(slot_num + 1):
                grp_cs_sel_seq.append(slot_sram)
        # -----------------------------------------------
        # Base the send sequence, cal the delay_done max GAP
        # -----------------------------------------------
        cs_tseg_dealy_gap_time = [[0.0 for i in range(TX_NUM)] for j in range(SRAM_CFG_NUM)]
        length = len(grp_cs_sel_seq)
        for idx in range(length):
            post_idx = (idx + 1) % length
            cs_sel = grp_cs_sel_seq[idx]
            post_cs_sel = grp_cs_sel_seq[post_idx]
            for tseg_idx in range(TSEG_ST, TSEG_END + 1):
                tseg_delay_gap_time = tsegx_trg_expo_delay[cs_sel][tseg_idx] - tsegx_trg_expo_delay[post_cs_sel][
                    tseg_idx]
                if cs_tseg_dealy_gap_time[cs_sel][tseg_idx] < tseg_delay_gap_time * 100:  # Get the max value
                    cs_tseg_dealy_gap_time[cs_sel][tseg_idx] = tseg_delay_gap_time * 100

        # -----------------------------------------------
        # Cal the min_slot_time:
        #   slot_time > (slot0_delay - slot1_delay).max() + slot0_masking  + slot0_expo + noise_cal + slot_dsp_deal
        # -----------------------------------------------
        T_grp_slot_min_time = [0 for i in range(ANGLE_GRP_NUM)]
        for idx in range(length):
            cs_sel = grp_cs_sel_seq[idx]
            for tseg_idx in range(TSEG_ST, TSEG_END + 1):
                if DATA_MODE[1]:
                    tseg_slot_min_time = (cs_tseg_dealy_gap_time[cs_sel][tseg_idx] +
                                          cs_slot_complete_time[cs_sel] -
                                          sysc_main_hist_rd_time * (TSEG_END - tseg_idx) + MARGIN)
                else:
                    T1 = (cs_tseg_dealy_gap_time[cs_sel][tseg_idx] +
                          tseg_mask_time[tseg_idx] +
                          cs_tseg_expo_time[cs_sel][tseg_idx])
                    T2 = (tseg_noise_cal_time +
                          cs_hist_dsp_deal_time[cs_sel] +
                          sysc_main_hist_rd_time * (tseg_idx - TSEG_ST + 1) +
                          sysc_spot_hist_rd_time +
                          sysc_blind_hist_rd_time)
                    T3 = 0 if not (embeded_pkt_en | ambi_pcm_pkt_en) else int((81 * 4 * (tseg_idx - 1)) * 1000 / SYSC_CLK)
                    tseg_slot_min_time = T1 + max(T2, T3) + MARGIN
                if T_grp_slot_min_time[angle_grp_cnt] < tseg_slot_min_time:     # Get the max value
                    T_grp_slot_min_time[angle_grp_cnt] = tseg_slot_min_time

            if T_grp_slot_min_time[angle_grp_cnt] < cs_slot_min_time[cs_sel]:   # Get the max value
                T_grp_slot_min_time[angle_grp_cnt] = cs_slot_min_time[cs_sel]

        # -----------------------------------------------
        # Cal slot_time
        # -----------------------------------------------
        T_grp_slot_time[angle_grp_cnt] = 0
        for idx in range(length):
            post_idx = (idx + 1) % length
            cs_sel = grp_cs_sel_seq[idx]
            post_cs_sel = grp_cs_sel_seq[post_idx]
            T1 = cs_slot_complete_time[cs_sel]
            T2 = cs_slot_release_time[post_cs_sel]
            T3 = T1 - T2
            T_grp_slot_time[angle_grp_cnt] = max(T_grp_slot_time[angle_grp_cnt], T3)     # Find the max value
            frame_idle_time = max(frame_idle_time, T2)    # Find the max value

        T_grp_slot_time[angle_grp_cnt] = max(T_grp_slot_time[angle_grp_cnt], T_grp_slot_min_time[angle_grp_cnt])
        T4 = int(T_grp_slot_time[angle_grp_cnt] * SYSC_CLK / 1000)  # unit: cycle
        if T4 > 0xFFFF_FFFF:
            logging.error("SLOT_TIME_CAL: The grp%0d_slot_time cal out of bound: %0d > 32'hFFFF_FFFF", angle_grp_cnt, T4)
        else:
            grpx_slot_time[angle_grp_cnt] = T4

    frm_idle_time = int((frame_idle_time + MARGIN) * SYSC_CLK / 1000) # unit: cycle
    if frame_idle_time > 0xF_FFFF:
        logging.error("SLOT_TIME_CAL: The frame_idle_time cal out of bound: %0d > 20'hF_FFFF", frame_idle_time)

    print("  grpx_slot_time           (ns   ): ", T_grp_slot_time)
    print("  grpx_slot_time           (cycle): ", grpx_slot_time)
    print("  frame_idle_time          (cycle): %0d", frame_idle_time)


if __name__ == '__main__':
    pass

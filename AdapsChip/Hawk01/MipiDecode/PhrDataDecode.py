import logging

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, MaxNLocator


PL = 80 * 6

WC = int(PL * 1.5)
FLNR = 17
VROLL = 22
HROLL = 6
H_VLD_SEG = 2

PKT_NUM = FLNR * VROLL * HROLL * 2


def ParseMIPIRaw12Data(file):
    """
    """
    raw_data = np.fromfile(file, dtype=np.uint8)
    raw_data.shape = PKT_NUM, WC
    mipi_data = np.zeros((PKT_NUM, PL), dtype=np.uint16)

    for pkt_cnt in range(PKT_NUM):
        for wc_cnt in range(0, WC, 3):
            pl_cnt = wc_cnt // 3
            byte0 = raw_data[pkt_cnt, wc_cnt + 0].item()
            byte1 = raw_data[pkt_cnt, wc_cnt + 1].item()
            byte2 = raw_data[pkt_cnt, wc_cnt + 2].item()
            mipi_data[pkt_cnt, pl_cnt * 2 + 0] = ((byte2 & 0x0F) >> 0) + ((byte0 & 0xFF) << 4)
            mipi_data[pkt_cnt, pl_cnt * 2 + 1] = ((byte2 & 0xF0) >> 4) + ((byte1 & 0xFF) << 4)
    return mipi_data


def GerMipiFrameInfo(mipi_data):
    pre_frame_id = -1
    for roll_cnt in range(VROLL * HROLL):
        STEP = FLNR * 2

        vc1_info_index = roll_cnt * STEP + STEP - 2
        vc0_info_index = roll_cnt * STEP + STEP - 1

        vc0_info = mipi_data[vc0_info_index].tolist()
        vc1_info = mipi_data[vc1_info_index].tolist()

        vc0_frame_id = vc0_info[0] + ((vc0_info[1] & 0x00F) << 12)
        vc1_frame_id = vc1_info[0] + ((vc1_info[1] & 0x00F) << 12)

        vc0_v_rll_num = vc0_info[2] >> 6
        vc1_v_rll_num = vc1_info[2] >> 6
        vc0_h_rll_num = vc0_info[2] & 0x0F
        vc1_h_rll_num = vc1_info[2] & 0x0F

        if vc0_frame_id != vc1_frame_id or vc0_v_rll_num != vc1_v_rll_num or vc0_h_rll_num != vc1_h_rll_num:
            logging.error("frame id not equal: {} != {}".format(vc0_frame_id, vc1_frame_id))
        else:
            print(vc0_frame_id, vc0_v_rll_num, vc0_h_rll_num)
        if roll_cnt > 1 and pre_frame_id+1 != vc0_frame_id:
            logging.error("frame id not continuous: {}!= {}".format(pre_frame_id, vc0_frame_id))

        if vc0_v_rll_num != roll_cnt // HROLL or vc0_h_rll_num!= roll_cnt % HROLL:
            logging.error("roll num not equal: {}!= {} or {}!= {}".format(vc0_v_rll_num, roll_cnt // HROLL, vc0_h_rll_num, roll_cnt % HROLL))
        pre_frame_id = vc0_frame_id


def MipiImage(mipi_data, reverse=0):
    image = np.zeros((132, 192))
    for v_roll_cnt in range(VROLL):
        for h_roll_cnt in range(HROLL):
            roll_cnt = v_roll_cnt * HROLL + h_roll_cnt
            for seg_cnt in range(H_VLD_SEG):
                for pixel_cnt in range(16):
                    if reverse == 1:
                        index = seg_cnt * 16 + pixel_cnt
                    else:
                        if pixel_cnt % 2 == 0:
                            index = seg_cnt * 16 + pixel_cnt + 1
                        else:
                            index = seg_cnt * 16 + pixel_cnt - 1
                    pixel_data = mipi_data[roll_cnt * FLNR * 2 + index].tolist()
                    result = [pixel_data[i] + (pixel_data[i + 1] << 12) for i in range(0, len(pixel_data) - 1, 2)]
                    for v_pxl_cnt in range(6):
                        st_index = v_pxl_cnt * 40 + 4
                        v_pxl_data = sum(result[st_index:st_index + 36])
                        v_coor = v_roll_cnt * 6 + v_pxl_cnt
                        h_coor = h_roll_cnt * H_VLD_SEG * 16 + seg_cnt * 16 + pixel_cnt
                        image[v_coor, h_coor] = v_pxl_data

    fig = plt.figure()
    ax = fig.add_subplot(111)
    title = "Reverse:{}".format(reverse)
    # plt.imshow(arr, vmin=vmin, vmax=vmax)
    ax.imshow(image, vmin=None, vmax=None, cmap="gray")
    ax.xaxis.set_major_locator(MultipleLocator(16))
    ax.yaxis.set_major_locator(MultipleLocator(6))
    plt.title(title)


if __name__ == "__main__":
    f = r"C:\Users\honggang.li\Downloads\20250415_zyt_rawdata_script\rawdata\20250411170016899SIdx19_SubIdx0MirId2_Fs0_.raw"
    # f = r"C:\Users\honggang.li\Downloads\20250415_zyt_rawdata_script\rawdata\20250411170023359SIdx51_SubIdx0MirId2_Fs0_.raw"
    # f = r"C:\Users\honggang.li\Downloads\20250421163311272SIdx3_SubIdx0MirId2_Fs0_.raw"
    mipi_data = ParseMIPIRaw12Data(f)
    print(mipi_data.shape)
    GerMipiFrameInfo(mipi_data)
    MipiImage(mipi_data)
    MipiImage(mipi_data, reverse=1)
    plt.show()

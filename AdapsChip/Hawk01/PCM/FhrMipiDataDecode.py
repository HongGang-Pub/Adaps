from SelfDefinedPackge import PubMethod
from AdapsChip.Hawk01 import Hawk01MipiPubMethod, Hawk01PubMethod


def ParseFHRData(file_path, vroll=31, h_vld_seg=15):
    file_dict = Hawk01PubMethod.GetMipiFile(fd_path=file_path)

    pkg_num = 4 * (h_vld_seg + 1) * 6 + 2

    if not Hawk01MipiPubMethod.ChkMipiReliablity(file_dict, pkg_num):
        raise ValueError("MiPi数据错误！！！")

    data = []
    frame_data = []

    pixel_num = (vroll + 1) * (h_vld_seg + 1) * 6 * 16

    file_index_list = list(file_dict.keys())
    file_index_list.sort()

    for f_idx in file_index_list:
        file = file_dict[f_idx]
        subframe_data = PubMethod.read_file(file)

        # 获取 frame info 信息
        frame_id, vroll_num, hroll_num = Hawk01MipiPubMethod.GerMipiFrameInfo(file)

        if vroll_num == 0:
            print("MIPI_{}: frame_id:{}, vroll_num:{}".format(f_idx, frame_id, vroll_num))

        for vc_num in range((h_vld_seg + 1) * 6 * 2):
            pkg_index = vc_num * 2
            vc1_pixel_data = Hawk01MipiPubMethod.PackageSplit(subframe_data[pkg_index])
            vc0_pixel_data = Hawk01MipiPubMethod.PackageSplit(subframe_data[pkg_index + 1])
            for pixel_cnt in range(4):
                frame_data.append(vc0_pixel_data[pixel_cnt])
                frame_data.append(vc1_pixel_data[pixel_cnt])
        if len(frame_data) == pixel_num:
            data.append(frame_data)
            frame_data = []

    # for frame_num_sel in range(1):
    for frame_num in range(len(data)):
        fname = "FrameData{}.txt".format(frame_num)
        for pix_cnt in range(len(data[frame_num])):
            pix_data = data[frame_num][pix_cnt]
            cover = 1 if pix_cnt == 0 else 0
            PubMethod.data_save(fname=fname, data_list=pix_data, is_cover=cover, split=' ',
                                fd_path="../Hawk/TXU_Check/FHR1", note="MIPI_DATA")

    print("完成{}帧数据解析!!!".format(len(data)))
    return


if __name__ == '__main__':
    ParseFHRData(file_path=r"C:\Users\honggang.li\Downloads\MipiData_1seg_40ms",
                 vroll=31,
                 h_vld_seg=0)

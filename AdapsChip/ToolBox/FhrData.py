import numpy as np
import matplotlib.pyplot as plt

from SelfDefinedPackge import PubMethod
from AdapsChip.Hawk01 import Hawk01MipiPubMethod, Hawk01PubMethod


def fhr_data2array(data):
    data1 = data.split(" ")
    data2 = list(map(int, data1[0:-1]))
    dt = np.array(data2)
    return dt


def do_work1():
    """
    读取 SpadisApp FHR.txt文件，分析黑点数据
    """
    file = PubMethod.get_fp(fd_path=r"D:\Software\SpadisApp\InternalRelease_SpadisApp(NoROI)\SavedImages\Record_2023_09_18_04_30_41",
                            mode=0,
                            match_filter="RawDataHistogramMap_frame",
                            regression=1)

    base_coor = (0, 0)
    coor = [base_coor]

    histograms = []

    datas = PubMethod.read_file(file[0])

    for line in range(len(datas)):
        x = line % 256
        y = line // 256
        dt = fhr_data2array(datas[line])

        photon_sum = np.sum(dt)
        if photon_sum < 4300:
            coor.append((x, y))
            print("Line:{}: ({}, {}) -> photon_cnt:{}".format(line, x, y, photon_sum))

        if (x, y) in coor:
            histograms.append(dt)

        if len(coor) > 10:
            break

    for index in range(len(histograms)):
        # hist = histograms[index] / len(file)
        hist = histograms[index]
        base_hist = histograms[0]

        plt.figure()
        color = "r" if index == 0 else "b"
        plt.bar(np.arange(0, 672, 1), base_hist, align='center', alpha=0.5, color="r")
        plt.bar(np.arange(0, 672, 1), hist, align='center', alpha=0.5, color="b")
        # plt.hist(hist, bins=672)
        print("coor{}: max_bin={},sum={}".format(coor[index], hist.max(), np.sum(hist)))
        plt.title("coor{}: max_bin={},sum={}".format(coor[index], hist.max(), np.sum(hist)))

    plt.show()


def do_work2(file_path, script_file):
    """
    FHR MIPI 数据成直方图
    """
    hawk01_config = Hawk01MipiPubMethod.GetCsruAndROIConfig(script_file)
    h_vld_seg = hawk01_config["H_VLD_SEG"]
    v_roll = 0  # 第几次v_roll
    h_roll = 0  # 第几次h_roll
    sub_light = 0   # 第几个光条
    seg_cnt = 0     # 第几段
    per_seg_pkg_cnt = 0  # 第几个包

    file_dict = Hawk01PubMethod.GetMipiFile(fd_path=file_path)

    # pkg_num = Hawk01MipiPubMethod.CalPkgNum(hawk01_config=hawk01_config)
    # if not Hawk01MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=pkg_num):
    #     raise ValueError("MiPi数据错误!!!")

    vroll_num, hroll_num, f_index = Hawk01MipiPubMethod.GetSpecificMipiFile(f_dict=file_dict, v_roll_num=v_roll, h_roll_num=h_roll)

    file = file_dict[f_index]
    subframe_data = PubMethod.read_file(file)

    pkg_index = sub_light * (h_vld_seg + 1) * 4 + seg_cnt * 4
    pixel_data = Hawk01MipiPubMethod.PackageSplit(data=subframe_data[pkg_index + per_seg_pkg_cnt],
                                                  bin_number=672)

    for index in range(len(pixel_data)):
        hist = np.array(pixel_data[index])

        # hist = histograms[index]
        plt.figure()
        plt.bar(np.arange(0, 672, 1), hist, align='center', alpha=0.5, color="b")
        # plt.hist(hist, bins=672)
        print("coor[{}]: max_bin={},sum={}".format(index, hist.max(), np.sum(hist)))
        plt.title("coor[{}]: max_bin={},sum={}".format(index, hist.max(), np.sum(hist)))

    plt.show()


def do_work3(file_path, script_file):
    """
    PHR MIPI 数据成直方图
    """
    hawk01_config = Hawk01MipiPubMethod.GetCsruAndROIConfig(script_file)
    v_roll = 0  # 第几次v_roll
    h_roll = 0  # 第几次h_roll
    seg_cnt = 0     # 第几段
    per_seg_pkg_cnt = 0  # 每段第几个包

    file_dict = Hawk01PubMethod.GetMipiFile(fd_path=file_path)

    # pkg_num = Hawk01MipiPubMethod.CalPkgNum(hawk01_config=hawk01_config)
    # if not Hawk01MipiPubMethod.ChkMipiReliablity(f_dict=file_dict, pkg_num=pkg_num):
    #     raise ValueError("MiPi数据错误!!!")

    vroll_num, hroll_num, f_index = Hawk01MipiPubMethod.GetSpecificMipiFile(f_dict=file_dict, v_roll_num=v_roll, h_roll_num=h_roll)

    file = file_dict[f_index]
    subframe_data = PubMethod.read_file(file)

    pkg_index = seg_cnt * 16 + per_seg_pkg_cnt
    pixel_data = Hawk01MipiPubMethod.PackageSplit(data=subframe_data[pkg_index],
                                                  bin_number=80,
                                                  pixel_num=6)

    for index in range(len(pixel_data)):
        hist = np.zeros(672)
        pxl_data = pixel_data[index]
        for pks_cnt in range(0, 3):
            pk_depth_index_idx = 2 + 2 * pks_cnt
            pk_depth_index = (pxl_data[pk_depth_index_idx] + (pxl_data[pk_depth_index_idx+1] << 12)) >> 5

            pk_phr_echo_data_idx = 8 + pks_cnt * 24
            phr_echo_data0 = pxl_data[pk_phr_echo_data_idx: pk_phr_echo_data_idx + 24]

            phr_echo_data1 = []
            for dt_idx in range(0, 12):
                phr_echo_data1.append((phr_echo_data0[dt_idx*2] + (phr_echo_data0[dt_idx*2+1] << 12)))

            pk_hist = np.array(phr_echo_data1)

            st = pk_depth_index-6
            st = 0 if st < 0 else st
            st = st if st+12 < 672 else 672-12

            hist[st:st+12] = pk_hist

        # hist = histograms[index]
        plt.figure()
        plt.bar(np.arange(0, 672, 1), hist, align='center', alpha=0.5, color="b")
        # plt.hist(hist, bins=672)
        print("coor[{}]: max_bin={},sum={}".format(index, hist.max(), np.sum(hist)))
        plt.title("coor[{}]: max_bin={},sum={}".format(index, hist.max(), np.sum(hist)))

    plt.show()


if __name__ == '__main__':
    # do_work3(file_path=r"D:\Software\DothinkTester\MipiData\1PHR",
    #          config_file=r"D:\Software\DothinkTester\Script\250mhz\test_ptm_phr_2d_scan.txt")
    do_work1()

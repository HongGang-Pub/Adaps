#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : PubMethod.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    : 本文件实现了 Hawk MIPI 仿真模型, 用于确保 Hawk相关寄存器配置的正确性

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025/01/12 09:00    honggang_li    v1.0        1. 创建 Hawk MIPI 仿真模型;
                                               2. 由于 DLY 中存在的 1us 误差, 要求将 MIPI_PKTDLY-1, 然
                                                  后再传给模型进行计算, 此方法可能会导致仿真出来的配置值偏大;
                                               3. MIPI_PKT_interval 使用字典查找仿真值的方式, 后续会考虑
                                                  直接使用公式计算的方式, 避免字典查找的方式;

2025/04/24 09:00    honggang_li    v1.1        1. 将 MIPI_PKT_interval 字典查找方式, 改为直接使用公式计
                                                  算的方式;
                                               2. 抹除 DLY 1us 误差的影响, 通过寄存器配置获取真实的 DLY,
                                                  再进行 MIPI 仿真 (PHR 下, 各个 group 的 DLY 不同, 模
                                                  型中直接使用 最小DLY 进行计算, 带来的误差可以忽略不计(除
                                                  非在部分极端条件下, group间的 DLY 出现 1us 的跳变, 可
                                                  能会导致 仿真模型提示 FIFO 溢出, 实际传输不会溢出的场景,
                                                  代码中已对此种情况打印 warning 信息));
                                               3. 对于第一个包起始点由于没有与 1M 时钟对齐, 带来的 1us 误差,
                                                  MIPI仿真模型 中未做处理, 目前可以通过将 MIPI仿真模型 中的
                                                  MIPI_FIFO_SIZE 设置小一点去冲抵此误差带来的影响, 后续可
                                                  以考虑在模型中进行处理;
=================================================================================================
"""
import logging

from PubMethod import *
from HawkConfig import *  # 导入 Hawk 配置

# Hawk01 设计规格. PS: MIPI_PKT_interval 后面直接使用公式计算, 因此废弃此字典查找方式
# MIPI_PKT_interval_dict = {
#     # SYS_CLK
#     324: {
#         # MIPI_RATE:
#         800: 1250,
#         1000: 1100,
#         1200: 1010,
#         1500: 900,
#     },
#     330: {
#         # MIPI_RATE:
#         800: 1240,
#         1000: 1070,
#         1200: 980,
#         1500: 900,
#     }
# }


def mipi_model(csru_cfg: dict, mipi_cfg: dict,SYS_CLK: int=330, MIPI_RATE: int=1500):
    """
    计算 MIPI 速率模型: 此模型仅支持 MIPI 速率小于 TXU 速率场景

    Args:
        csru_cfg(dict): Hawk 寄存器配置
        mipi_cfg(dict): Hawk MIPI 配置
        SYS_CLK(int): 系统时钟频率, unit: Mhz
        MIPI_RATE: MIPI 速率, unit: Gbps/Lane

    Returns:
        None: None
    """

    # Hawk 基本参数计算
    WORK_MODE = csru_cfg["WORK_MODE"]
    ONE_DT_MODE = csru_cfg["ONE_DT_MODE"]
    # PKT_DLY = max(csru_cfg["MIPI_PKTDLY"] - 1, 0) * 1000  # unit: ns. 需要根据配置值换算为 ns. 同时配置值存在 -1 的误差, 需要 -1 后再进行单位换算

    # MIPI 基本参数计算
    MIPI_PKT_INTV = MipiPKGIntvCal(mipi_cfg=mipi_cfg, SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)
    WC, FLNR = CalMipiFlnrAndWC(csru_cfg, unit="subframe")  # 此处 FLNR 仅对 1个sub-frame 进行计算

    # MIPI & TXU 速率

    TXU_rate = 12 / (1000 / SYS_CLK)  # RAW12 = 12, unit: bit/ns
    MIPI_rate = MIPI_RATE * MIPI_LANE_NUM / 1000  # unit: bit/ns
    # 计算 TXU 写 fifo 时间 和 间隔时间
    TXU_PKT_read_t = WC * 8 / TXU_rate

    # BIN_NUMBER = (csru_cfg["MAXBIN_THRS"] + 1) * 4 - csru_cfg["MINBIN_THRS"] * 2
    # TXU_PKT_interval = (31 + BIN_NUMBER + 27) * (1000 / SYS_CLK) if WORK_MODE == 0 or WORK_MODE == 1 \
    #     else (24 + 8 * 3) * (1000 / SYS_CLK)    # unit: ns

    if WORK_MODE == 0 or WORK_MODE == 1:
        once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCalForPHR(csru_cfg)
        once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[-1]  # 每个 Group 递减, 从严法则, 选择最小值进行仿真
        if once_hist_rd_add_txdly_Q[-1][0] - once_hist_rd_add_txdly_Q[-1][0] > 0:
            logging.warning(f"PHR 模型中, 存在 DLY 跳变, 仿真结果可能不准确...")
    else:
        once_hist_rd_add_txdly_Q = OnceHistReadAddTxdlyCycCalForFHR(csru_cfg)
        once_hist_rd_add_txdly_cyc, rd_out_ind_cyc = once_hist_rd_add_txdly_Q[0]  # 每个 Seg 数据都相同, 因此仅用 0 进行计算

    TXU_PKT_interval = once_hist_rd_add_txdly_cyc * (1000 / SYS_CLK)   # 起始点到起始点的时间, 并不是终点和起点间的间隔

    TXU_PKT_read_t = round(TXU_PKT_read_t, precision)
    TXU_PKT_interval = round(TXU_PKT_interval, precision)

    # 计算 VC0 MIPI 读出 fifo 时间 和 间隔时间
    MIPI_PKT_read_t = (WC * 8 + 6 * 8) / MIPI_rate

    # VC0_MIPI_PKT_interval = MIPI_PKT_interval_dict[SYS_CLK][MIPI_RATE] * 2 + MIPI_PKT_read_t
    # MIPI_PKT_INTV = 1070
    VC0_MIPI_PKT_interval = MIPI_PKT_INTV * 2 + MIPI_PKT_read_t
    MIPI_PKT_read_t = round(MIPI_PKT_read_t, precision)
    VC0_MIPI_PKT_interval = round(VC0_MIPI_PKT_interval, precision)

    # /////////////////////////////////////////////////////////////
    # MIPI 仿真模型开始
    # /////////////////////////////////////////////////////////////
    # 初始化
    fifo_size = MIPI_FIFO_SIZE * 32
    timer_step = 1 / (10 ** precision)

    timer = 0
    txu_read_timer = 0
    mipi_read_timer = 0

    pkt_num_cnt = 0
    txu_read_time = 0
    fifo_overflow = True
    current_fifo_data_size = 0

    while current_fifo_data_size < fifo_size:
        # TXU_read 逻辑
        timer = round(timer + timer_step, precision)  # 增加总时间
        txu_read_timer = round(txu_read_timer + timer_step, precision)

        if pkt_num_cnt < FLNR:
            if txu_read_timer <= TXU_PKT_read_t:
                if txu_read_timer == timer_step:
                    current_fifo_data_size += 4 * 8  # PH 4 byte

                current_fifo_data_size += TXU_rate / (10 ** precision)  # 增 加注水量

                if txu_read_timer == TXU_PKT_read_t:
                    current_fifo_data_size += 2 * 8  # PF: 2 byte
                    pkt_num_cnt += 1
                    print(f"@ {timer} ns: TXU read package {pkt_num_cnt} complete...")
                    if pkt_num_cnt == FLNR - ONE_DT_MODE:
                        txu_read_time = timer
                        txu_read_timer = 0  # ONE_DT_MODE=1时, 需要重置 TXU 计时器, 立即发送 info 包
            elif txu_read_timer >= TXU_PKT_interval:
                txu_read_timer = 0  # 重置 TXU 计时器
        # 检查注满条件
        if current_fifo_data_size >= fifo_size:
            break

        # MIPI read 逻辑
        if timer <= (VC0_MIPI_PKT_interval + TXU_PKT_read_t):  # The first package is VC1
            pass
        else:
            mipi_read_timer = round(mipi_read_timer + timer_step, precision)
            if mipi_read_timer <= MIPI_PKT_read_t:
                current_fifo_data_size -= MIPI_rate / (10 ** precision)
            elif mipi_read_timer >= MIPI_PKT_read_t + VC0_MIPI_PKT_interval:
                mipi_read_timer = 0  # 重置 MIPI 计时器

        if pkt_num_cnt == FLNR and current_fifo_data_size <= 0:
            print(f"TXU write time: {txu_read_time}ns, MIPI read time: {timer}ns")
            fifo_overflow = False
            break
        current_fifo_data_size = max(current_fifo_data_size, 0)

    if fifo_overflow:
        raise ValueError(f"MIPI fifo在 第{pkt_num_cnt}个包 发生溢出, 溢出耗时: {timer:.2f} ns")
    return


if __name__ == '__main__':
    # ////////////////////////////////////////////////
    # 仿真精度
    # ////////////////////////////////////////////////
    precision = 1  # 小数位宽: 精度越大, 仿真越慢, 仿真结果越准确, 一般 0.1ns 精度已经足够

    mipi_model(csru_cfg=csru_cfg, mipi_cfg=mipi_cfg, SYS_CLK=SYS_CLK, MIPI_RATE=MIPI_RATE)

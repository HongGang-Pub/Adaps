import logging

# ////////////////////////////////////////////////
# 仿真精度
# ////////////////////////////////////////////////
precision = 1  # 小数位宽: 精度越大, 仿真越慢, 仿真结果越准确

# ////////////////////////////////////////////////
# 根据配置脚本填写配置值
# ////////////////////////////////////////////////
WORK_MODE = 1
SYS_CLK = 324
MIPI_RATE = 1500
WC = 132 * 1.5
FLNR = 128
BIN_NUMBER = 488
PKT_DLY = 0  # unit: ns. 需要根据配置值换算为 ns. 同时配置值存在 -1 的误差, 需要 -1 后再进行单位换算

# ////////////////////////////////////////////////
# Hawk 基本参数
# ////////////////////////////////////////////////
RAW12 = 12
MIPI_FIFO_SIZE = 1024 * 32
package_size = WC * 8

# ////////////////////////////////////////////////
# MIPI & TXU 速率
# ////////////////////////////////////////////////
TXU_rate = RAW12 / (1000 / SYS_CLK)  # unit: bit/ns
MIPI_rate = MIPI_RATE * 4 / 1000  # unit: bit/ns

# ////////////////////////////////////////////////
# 包间间隔计算(unit: ns)
# ////////////////////////////////////////////////
TxEscClkDiv_Q = {200: 11, 250: 14, 324: 16, 300: 16}
TXHSByteClkDiv = 8

T_TxClkEsc = 1000 / (SYS_CLK / (TxEscClkDiv_Q[SYS_CLK] + 1))
T_TxByteClkHS = 1000 / (MIPI_RATE / TXHSByteClkDiv)

DataTxThslpxcnt = 2
DataTxThsexitCnt = 2
DataTxThsprepareCnt = 0
DataTxThszeroCnt = 19
DataTxThstrailCnt = 12

MIPI_PKT_INTV = ((120 if DataTxThsexitCnt == 0 else 360) +
                 T_TxClkEsc * DataTxThslpxcnt +
                 T_TxClkEsc * (DataTxThsprepareCnt+1) +
                 T_TxByteClkHS * (DataTxThszeroCnt+4) +
                 T_TxByteClkHS * (DataTxThstrailCnt+1) +
                 (6*8 + 8) / (MIPI_RATE*4))
print(f"T_TxClkEsc: {T_TxClkEsc:0.2f}")
print(f"T_TxByteClkHS: {T_TxByteClkHS:0.2f}")
print(f"MIPI 包间间隔: {MIPI_PKT_INTV:0.2f}")
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
# Hawk01 设计规格


# 计算 TXU 写 fifo 时间 和 间隔时间
TXU_PKT_read_t = package_size / TXU_rate

if WORK_MODE == 0 or WORK_MODE == 1:
    TXU_PKT_interval = (31 + BIN_NUMBER + 27) * (1000 / SYS_CLK)  # ns
elif WORK_MODE == 2 or WORK_MODE == 3:
    TXU_PKT_interval = (24 + 8 * 3) * (1000 / SYS_CLK)
else:
    TXU_PKT_interval = 0
    logging.fatal("WORK_MODE config error...")

TXU_PKT_interval = TXU_PKT_interval + PKT_DLY

TXU_PKT_read_t = round(TXU_PKT_read_t, precision)
TXU_PKT_interval = round(TXU_PKT_interval, precision)

# 计算 VC0 MIPI 读出 fifo 时间 和 间隔时间
MIPI_PKT_read_t = (package_size + 6 * 8) / MIPI_rate
# VC0_MIPI_PKT_interval = MIPI_PKT_interval_dict[SYS_CLK][MIPI_RATE] * 2 + MIPI_PKT_read_t
VC0_MIPI_PKT_interval = MIPI_PKT_INTV * 2 + MIPI_PKT_read_t
MIPI_PKT_read_t = round(MIPI_PKT_read_t, precision)
VC0_MIPI_PKT_interval = round(VC0_MIPI_PKT_interval, precision)


# ////////////////////////////////////////////////
# MIPI 模型: 此模型仅支持 MIPI 速率小于 TXU 速率场景
# ////////////////////////////////////////////////
def mipi_model():
    # 初始化
    current_fifo_data_size = 0
    timer_step = 1 / (10 ** precision)

    timer = 0
    txu_read_timer = 0
    mipi_read_timer = 0

    pkg_number_count = 0
    txu_read_time = 0
    fifo_overflow = True

    while current_fifo_data_size < MIPI_FIFO_SIZE:
        # TXU_read 逻辑
        timer = round(timer + timer_step, precision)  # 增加总时间
        txu_read_timer = round(txu_read_timer + timer_step, precision)

        if pkg_number_count < FLNR:
            if txu_read_timer <= TXU_PKT_read_t:
                if txu_read_timer == timer_step:
                    current_fifo_data_size += 4 * 8  # PH 4 byte

                current_fifo_data_size += TXU_rate / (10 ** precision)  # 增 加注水量

                if txu_read_timer == TXU_PKT_read_t:
                    current_fifo_data_size += 2 * 8  # PF: 2 byte
                    pkg_number_count += 1
                    print(f"@ {timer} ns: TXU read package {pkg_number_count} complete...")
                    if pkg_number_count == FLNR:
                        txu_read_time = timer
            elif txu_read_timer >= TXU_PKT_read_t + TXU_PKT_interval:
                txu_read_timer = 0  # 重置 TXU 计时器
        # 检查注满条件
        if current_fifo_data_size >= MIPI_FIFO_SIZE:
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

        if pkg_number_count == FLNR and current_fifo_data_size <= 0:
            print(f"TXU write time: {txu_read_time}ns, MIPI read time: {timer}ns")
            fifo_overflow = False
            break
        current_fifo_data_size = max(current_fifo_data_size, 0)

    if fifo_overflow:
        print(f"fifo溢出耗时: {timer:.2f} ns。")
        print(f"fifo溢出包数量为: {pkg_number_count} ")
    return


if __name__ == '__main__':
    mipi_model()

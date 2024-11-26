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
MIPI_RATE = 800
WC = 132 * 1.5
BIN_NUMBER = 448
PKT_DLY = 0  # unit: ns. 需要根据配置值换算为 ns. 同时配置值存在 -1 的误差, 需要 -1 后再进行单位换算

# ////////////////////////////////////////////////
# 以下配置为常量,
# ////////////////////////////////////////////////
# 根据仿真结果获取的包间隔 (unit: ns)
#   1. 包间隔为 MIPI 寄存器默认配置时的仿真值, 留有一定 margin (40ns), 确保仿真通过时, 硬件实测可以通过
#   2. 目前仅提供 SYS_CLk=330, (T_txesc_clk = 19.41M (330M 进行 17 分频)) 的仿真结果
MIPI_PKT_interval_dict = {
    # SYS_CLK
    324: {
        # MIPI_RATE:
        800: 1250,
        1000: 1100,
        1200: 1010,
        1500: 900,
    },
    330: {
        # MIPI_RATE:
        800: 1240,
        1000: 1070,
        1200: 980,
        1500: 900,
    }
}
# Hawk01 设计规格
RAW12 = 12
fifo_size = 1024 * 32

# ////////////////////////////////////////////////
# 根据配置进行计算相关数据
# ////////////////////////////////////////////////
package_size = WC * 8  # bit
TXU_rate = RAW12 / (1000 / SYS_CLK)  # unit: bit/ns
MIPI_rate = MIPI_RATE * 4 / 1000  # unit: bit/ns

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
VC0_MIPI_PKT_interval = MIPI_PKT_interval_dict[SYS_CLK][MIPI_RATE] * 2 + MIPI_PKT_read_t
MIPI_PKT_read_t = round(MIPI_PKT_read_t, precision)
VC0_MIPI_PKT_interval = round(VC0_MIPI_PKT_interval, precision)


# ////////////////////////////////////////////////
# MIPI 模型
# ////////////////////////////////////////////////
def mipi_model():
    # 初始化
    current_fifo_data_size = 0
    timer_step = 1 / (10 ** precision)

    timer = 0
    txu_read_timer = 0
    mipi_read_timer = 0

    pkg_number_count = 0

    while current_fifo_data_size < fifo_size:
        # TXU_read 逻辑
        timer = round(timer + timer_step, precision)  # 增加总时间
        txu_read_timer = round(txu_read_timer + timer_step, precision)

        if txu_read_timer <= TXU_PKT_read_t:
            if txu_read_timer == timer_step:
                print(f"TXU read package time: {timer}")
                current_fifo_data_size += 4 * 8  # PH 4 byte
                pkg_number_count += 1

            current_fifo_data_size += TXU_rate / (10 ** precision)  # 增加注水量

            if txu_read_timer == TXU_PKT_read_t:
                current_fifo_data_size += 2 * 8  # PF: 2 byte
        elif txu_read_timer >= TXU_PKT_read_t + TXU_PKT_interval:
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

        # 更新计时器和总时间
        # if total_time % 10 == 0:
        #     print(total_time, current_fifo_data_size)
        # 水量不能低于 0
        if current_fifo_data_size < 0:
            print("ERROR: fifo empty...")
        current_fifo_data_size = max(current_fifo_data_size, 0)

    # 转换总时间为分钟
    return timer, pkg_number_count


# 运行模拟
t, pkg_number_cnt = mipi_model()
print(f"fifo溢出耗时: {t:.2f} ns。")
print(f"fifo溢出包数量为: {pkg_number_cnt} ")

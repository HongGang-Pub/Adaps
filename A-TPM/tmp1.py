WORK_MODE = 2
SYS_CLK = 330
MIPI_RATE = 1500
WC = 448 * 4 * 1.5
FIFO_THRESHOLD = 0xC0
BIN_NUMBER = 448

MIPI_PKT_interval_dict = {
    800: 860,
    1000: 860,
    1200: 860,
    1500: 900,
}


raw12 = 12
fifo_size = 1024 * 32

TXU_rate = raw12 / (1000 / SYS_CLK)      # unit: bit/ns
MIPI_rate = 1500 * 4 / 1000     # unit: bit/ns

package_size = WC * 8   # bit

TXU_PKT_read_t = package_size / TXU_rate

if WORK_MODE == 0:
    TXU_PKT_interval = (31 + BIN_NUMBER + 27) * (1000 / SYS_CLK)    # ns
elif WORK_MODE == 1:
    TXU_PKT_interval = (31 + BIN_NUMBER + 27) * (1000 / SYS_CLK)    # ns
elif WORK_MODE == 2:
    TXU_PKT_interval = (24 + 8 * 3) * (1000 / SYS_CLK)
else:
    pass

MIPI_PKT_read_t = (package_size + 6 * 8) / MIPI_rate

# Add 20ns: because package_end = 10 ns
VC0_MIPI_PKT_interval = MIPI_PKT_interval_dict[MIPI_RATE] * 2 + MIPI_PKT_read_t


def simulate_parallel_fill_with_counts():
    # 初始化
    current_fifo_data_size = 0

    total_time = 0
    txu_read_timer = 0
    mipi_read_timer = 1

    pkg_number_count = 0

    while current_fifo_data_size < fifo_size:
        # TXU_read 逻辑
        total_time += 1   # 增加总时间

        txu_read_timer += 1

        if txu_read_timer <= TXU_PKT_read_t:
            if txu_read_timer == 1:
                print(f"total_time: {total_time}")
                current_fifo_data_size += 4*8   # PH 4 byte
                pkg_number_count += 1

            current_fifo_data_size += TXU_rate  # 增加注水量

            if txu_read_timer == TXU_PKT_read_t:
                current_fifo_data_size += 2*8   # PF: 2 byte
        elif txu_read_timer >= TXU_PKT_read_t + TXU_PKT_interval:
            txu_read_timer = 0  # 重置 TXU 计时器

        # 检查注满条件
        if current_fifo_data_size >= fifo_size:
            break

        # MIPI read 逻辑
        if total_time <= (VC0_MIPI_PKT_interval + TXU_PKT_read_t):  # The first package is VC1
            pass
        else:
            mipi_read_timer += 1
            if mipi_read_timer <= MIPI_PKT_read_t:
                current_fifo_data_size -= MIPI_rate
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
    return total_time, pkg_number_count


# 运行模拟
total_t, pkg_number_cnt = simulate_parallel_fill_with_counts()
print(f"fifo溢出耗时: {total_t:.2f} ns。")
print(f"fifo溢出包数量为: {pkg_number_cnt} ")

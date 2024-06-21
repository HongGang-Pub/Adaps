data_width_sel = 2

data2 = 0x8607D
data3 = 0x00c91
if data_width_sel in [0, 3]:
    echo_start = ((data2 >> 0) & 0xFF) + (((data2 >> 12) & 0x03) << 8)
    peak_index = ((data2 >> 14) & 0x3F) + (((data3 >> 0) & 0x0F) << 6)
    echo_end = ((data3 >> 4) & 0x0F) + (((data3 >> 12) & 0x3F) << 4)
else:
    echo_start = (data2 >> 0) & 0x3FF
    peak_index = (data2 >> 12) & 0x3FF
    echo_end = (data3 >> 0) & 0x3ff

print("echo_start:", echo_start)
print("peak_index:", peak_index)
print("echo_end  :", echo_end)
print("length    :", echo_end-echo_start+1)

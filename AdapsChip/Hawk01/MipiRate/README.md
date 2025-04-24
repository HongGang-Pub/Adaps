# 1. README
- [1. README](#1-readme)
- [2. 简介](#2-简介)
- [3. 使用说明](#3-使用说明)
- [4. DPHY 时序图](#4-dphy-时序图)

# 2. 简介
本文件仅适用于`Hawk`产品, 包含了多个与 MIPI 相关的计算模型, 具体如下:  
  1. MIPI发送&接收模型 `mipi_model.py`
  2. 帧率计算模型 `mipi_subframe_time_cal.py`
  3. 流控寄存器(MIPI_PKTDLY) 理论计算模型 `mipi_pktdly_cal.py`
  4. DPHY协议开销寄存器计算模型 `dphy_config.cal`

# 3. 使用说明
1. `修改配置`: 根据Hawk实际寄存器配置, 修改`HawkConfig.py` 文件中的参数
2. `Running脚本`: 根据需求, running 对应的模型, 即可输出相应的结果  
<u>*ps: 修改的变量包含: *SYS_CLK & MIPI_RATE &  csru_cfg & mipi_cfg**</u>

# 4. DPHY 时序图 
DPHY 的时序要求如下图, DPHY协议开销寄存器配置值基于以下时序图进行计算
<img src="./DPHY.png" alt="DPHY" title="DPHY">
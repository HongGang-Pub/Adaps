# 1. README
- [1. README](#1-readme)
- [2. 软件介绍](#2-软件介绍)
- [3. 使用方法](#3-使用方法)
- [4. 标定文件格式说明](#4-标定文件格式说明)
- [5. ROI配置校验](#5-roi配置校验)
- [6. 寄存器配置生成功能说明](#6-寄存器配置生成功能说明)

# 2. 软件介绍  
1. 软件界面如下  
![软件界面](figs/Software.jpg "Software.jpg")
2. Config: 
   1. XCLK: PLL_CLKIN 的输出参考时钟，可配置为24M或25M
   2. MST_MODE: 寄存器配置, 芯片是作为 Slave or Master 
   3. WORK_MODE: 寄存器配置, 芯片工作模式选择, 可多选, 同时选择所有4种工作模式, 保存时则生成4种模式的系统配置脚本
   4. MIPI RATE：MIPI 速率配置, 下拉选择，0.8 / 1.0 / 1.2 / 1.5 Gbps/Lane
   5. SYS_CLK: 系统时钟, TDC bin width配置后自动设置好系统时钟, 系统时钟支持：200M、250M、330M
   6. TDC bin width：下拉选择，0.75 / 1.00 / 1.25 / 1.50 / 2.00 / 2.50 ns
   7. V_PXL_NUM: 寄存器配置, V_PXL_OUT_NUM
   8. TRG_I_EN: 寄存器配置, TRG_I Enable or Disable, 根据硬件设计配置
   9. MINBIN_TRHS: 寄存器配置, 修改配置时自动计算 BIN_NUMBER
   10. MAXBIN_TRHS: 寄存器配置, 修改配置时自动计算 BIN_NUMBER
   11. OUT_BIN_NUM：寄存器配置
   12. PKS_ECHO_NUM：寄存器配置
   13. SCAN_MODE: 寄存器配置, Rolling方式，1D or 2D scan_mode
   14. V_ROLL_NUM: 寄存器配置, 垂直方向Rolling次数，选择范围: 1~32次
   15. H_ROLL_NUM: 寄存器配置, 水平方向ROlling次数，选择范围: 1~16次(仅 2D scan mode 配置)
   16. H_VLD_SEG: 寄存器配置, 每次Rolling打开的段数, 1~16段
3. Input：
   1. Load ROI file：标定文件选择窗口, 默认打开./Input文件夹  
      > 标定文件格式请参看[**标定文件格式说明**](#4-标定文件格式说明)
   2. Sel Config file：基准配置文件选择窗口
      > 程序会根据选择的基准配置文件以及最新的配置信息，自动生成新的寄存器配置脚本  
      > 寄存器配置脚本支持的功能请参看[**寄存器配置生成功能说明**](#6-寄存器配置生成功能说明)
4. Output:
   1. REG CFG File：生成的寄存器配置脚本文件名
   2. ROI SRAM File：生成的ROI文件名
5. Operate:
   1. 操作界面分别为预览、保存、日志清除按钮，分别支持相应的功能
6. Control：  
   ![软件界面](figs/PlayerCtrl.jpg "PlayerCtrl.jpg")  
   从左到右，按钮功能依次为：
      - `预览上一帧`
      - `向后连续预览`
      - `停止预览`
      - `向前连续预览`
      - `预览下一帧`
# 3. 使用方法
1. 根据需求在界面上进行相应的配置
2. 将标定文件保存在`./Input`文件夹下
3. 选择标定文件以及基准配置脚本, 标定文件格式请参看[**标定文件格式说明**](#4-标定文件格式说明)
4. 点击预览, 查看Rolling效果
5. 点击保存, 程序将生成Hawk配置脚本以及相关ROI文件, 文件保存在`./Output`路径下  
6. 输出文件说明: `*.png`为整体Rolling效果展示图; `*.txt`为`Hawk配置脚本` & `ROI标定信息`文件  
*ps: 点击保存时，保存的ROI文件为左侧预览窗口的Rolling信息。因此, 修改相关配置或重新加载标定文件后, 请先点击预览, 再点击保存*

# 4. 标定文件格式说明
1. 标定信息仅支持`*.txt`文件格式
2. 每次Rolling需要指定一个坐标, Rolling与Rolling之间的坐标信息需换行配置, 不支持配置在同一行 
3. 坐标配置顺序需按照Rolling顺序依次配置, 如:
   1. 1D SCAN_MODE: V_ROLL_NUM=32 为例，先配置第1次Rolling坐标, 再配置第2次、第3次...  
      ![软件界面](figs/1D_SCAN.jpg "1D SCAN_MODE配置示例")
   2. 2D SCNA_MODE: V_ROLL_NUM=32, H_ROLL_NUM=4 为例:  
      1. 配置 vroll=1, hroll=1 简称`1-1` 的Rolling坐标  
      2. 配置 vroll=1, hroll=2 简称`1-2` 的Rolling坐标 
      3. 再依次配置`1-3、1-4、2-1、2-2...`  
      ![软件界面](figs/2D_SCAN.jpg "2D SCAN_MODE配置示例")
      
4. 坐标配置格式：`x, y`分别为横坐标，纵坐标。支持使用`英文/中文`的`逗号/分号` 分隔横纵坐标, 即(`,|;|，|；`), 禁止使用空格
5. 代码注释：可使用双斜杠(`//`)在行尾添加注释或整行注释

# 5. ROI配置校验
主要包含以下校验：
1. 标定文档格式校验
2. 标定文档数据正确性校验, 如: 坐标是否超过`(768, 576)`校验
3. 标定文档坐标信息条数校验, 坐标信息实际条数应为: 
   ~~~ python
   if SCAN_MODE == '1D SCAN_MODE': 
      num = V_ROLL_NUM
   else:
      num = V_ROLL_NUM * H_ROLL_NUM
   ~~~
   如: 配置`SCAN_MODE=1D SCAN_MODE, V_ROLL_NUM=15`, 则标定文档至少需要有15条坐标信息
   1. 若标定文档少于15条配置信息, 预览失败
   2. 若标定文档多于15条配置信息，预览成功, 并提示: `标定文档可能与寄存器配置不匹配`

4. 坐标与配置信息综合合理性校验, 如: 标定信息为`(48, 0)`, 配置`SCAN_MODE=1D SCAN_MODE, H_VLD_SEG=15`时, 由于 `48 + H_VLD_SEG*48 > 768`, 会导致Rolling超边界, 预览失败

# 6. 寄存器配置生成功能说明
1. 系统时钟330、250、200M及分频相关寄存器配置
2. Upsampling 寄存器配置
3. MIPI 速率 0.8、1.0、1.2、1.5 Gbps/Lane 相关寄存器配置
4. MIPI_PKTDLY 自适应配置
5. ROI SRAM Block_write 配置
6. MIPI WC & FLNR配置
7. V_ROLL_NUM、H_ROLL_NUM、H_VLD_SEG、WOKR_MODE、SCAN_MODE等寄存器配置
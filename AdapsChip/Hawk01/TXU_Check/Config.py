"""
增加本文件目的主要是统一变量配置入口，其他模块导入后，可直接使用配置的变量，增加可阅读性
"""
# work_mode = 0
# tc_name = "1D_base"
# config_file=get_script_path(work_mode, tc_name)

script_file = r"D:\OneDrive - 深圳市灵明光子科技有限公司\Program Files\DothinkTester\Script\TXU_Script\test_ptm_fhr\test_ptm_fhr_1D_base.txt"

sram_data_path = r"D:\OneDrive - 深圳市灵明光子科技有限公司\Program Files\DothinkTester\SramData"
mipi_file_path = r"D:\OneDrive - 深圳市灵明光子科技有限公司\Program Files\DothinkTester\MipiData"
result_folder = "result"


# hist_testen=1，配置golden_data_path
golden_data_path = "None"

# hist_testen=0，配置subframe脚本和mipi file相关信息
subframe_script_file = ""
subframe_mipidata_path = ""
subframe_result_folder = "sub_result"

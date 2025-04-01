for pxl_pack_sel in [0, 1, 2, 3, 4, 5, 6, 7]:
    pxl_pack_num = 1 << pxl_pack_sel
    register_value = pxl_pack_num - 1
    print(f"{register_value:0>8b}")
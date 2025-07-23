#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
=================================================================================================
@FileName    : SoftPackageCMD.py.py
@Author      : honggang_li
@Email       : honggang.li@adaps-ph.com

@Function    :

@Modify Time        @Author        @Version    @Description
----------------    -----------    --------    -------------
2025-07-14 17:15    honggang_li    v1.0        

=================================================================================================
"""

from SelfDefinedPackge import PubMethod

cmd = "nuitka"

row_cmd_data = PubMethod.read_file("./cmdtext.txt")
include_cmd_cmd = ""
for s in row_cmd_data:
    s = s.strip()
    if s[0:2] == "//":
        continue
    cmd = cmd + " " + s.replace("\n", "")
if __name__ == '__main__':
    print(cmd)

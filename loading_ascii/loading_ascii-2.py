#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 逐行加载 ASCII 艺术字文件

import os
import sys
import time

# 切换到脚本所在目录
script_dir = sys.path[0]  # 脚本所在目录
os.chdir(script_dir)  # 切换到脚本所在目录

logo = f'files/{sys.argv[1]}' if len(sys.argv) > 1 else None  # 需要加载的 ASCII 艺术字文件
all_wait_time = 1  # 加载的总等待时间

if logo:
    with open(logo, 'r', encoding='utf-8') as file:
        data = file.readlines()
        line = len(data)  # 文件总行数
        wait_time = all_wait_time / line  # 加载每行的等待时间
        # print(wait_time)
        for i in range(line):
            print(data[i], end='')
            time.sleep(wait_time)

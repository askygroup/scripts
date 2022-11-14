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
wait_time = 0.1  # 加载每行的等待时间

if logo:
    with open(logo, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in range(len(data)):
            print(data[i], end='')
            time.sleep(wait_time)

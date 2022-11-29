#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Python 脚本模板
# 无特殊依赖、无配置文件
# 2022-11-02 asky

import os
import sys
from pathlib import Path

# 切换到脚本所在目录
script_dir = sys.path[0]  # 脚本所在目录
print(f'{script_dir=}')
os.chdir(script_dir)  # 切换到脚本所在目录
current_dir = Path.cwd()  # 当前所在目录
print(f'{current_dir=}')

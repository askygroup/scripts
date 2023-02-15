#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import sys
from pathlib import Path
import json
import random


def main():
    # 判断是否存在食物列表文件，有就读取文件，没有则报错退出
    if foods_file.is_file():
        with open(foods_file, 'r', encoding='utf-8') as file:
            foods_data = json.load(file)
    else:
        print(f'食物列表文件 {foods_file} 不存在，请先填写食物列表文件！')
        exit(1)

    foods = [key for key in foods_data]  # 食物列表
    # print(foods)

    # 从食物列表中，随机挑选一个输出食物名称，按Ctrl+C键结束
    try:
        while True:
            lucky_food = random.choice(foods)
            print(f'今天吃：{lucky_food}\r', end='')
    except KeyboardInterrupt:
        print(f'今天吃：{lucky_food}')


if __name__ == '__main__':
    # 切换到脚本所在目录
    script_dir = sys.path[0]  # 脚本所在目录
    os.chdir(script_dir)  # 切换到脚本所在目录
    current_dir = Path.cwd()  # 当前所在目录
    foods_file = current_dir.joinpath('foods.json')  # 食物列表文件

    main()  # 主函数

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import sys
from pathlib import Path
import json
import random
import datetime
from get_holiday_cn.client import getHoliday


def main():
    # 判断是否存在食物列表文件，有就读取文件，没有则报错退出
    if foods_file.is_file():
        with open(foods_file, 'r', encoding='utf-8') as file:
            foods_data = json.load(file)
    else:
        print(f'食物列表文件 {foods_file} 不存在，请先填写食物列表文件！')
        exit(1)

    # 食物列表
    foods = [key for key in foods_data]
    # print(foods)
    # 食物权重，如果没有设置 like 值，权重为0，食物会被随机展示但不会被挑选，like 值越高，会被选中的概率就越高
    weights = [value.get('like', 0) for value in foods_data.values()]
    # print(weights)

    # 当前时间，区分早中晚食物
    date_time = datetime.datetime.now()
    # date_time_hour = 10
    date_time_hour = date_time.hour
    # 早餐时间
    if 5 < date_time_hour <= 9:
        pop_index = [index for index, food in enumerate(foods) if '早' not in foods_data[food].get('dinnertime')]
    # 午餐时间
    elif 9 < date_time_hour <= 14:
        pop_index = [index for index, food in enumerate(foods) if '中' not in foods_data[food].get('dinnertime')]
    # 晚餐时间
    elif 14 < date_time_hour <= 20:
        pop_index = [index for index, food in enumerate(foods) if '晚' not in foods_data[food].get('dinnertime')]
    # 夜宵时间
    elif 20 < date_time_hour <= 23 or 0 <= date_time_hour <= 2:
        pop_index = [index for index, food in enumerate(foods) if '夜' not in foods_data[food].get('dinnertime')]
    # 打烊了
    else:
        print('打烊了！')
        exit()
    pop_index.reverse()  # 颠倒索引列表，防止删除元素是索引越界
    for index in pop_index:
        foods.pop(index)
        weights.pop(index)
    # print(pop_index, foods, weights)

    # 获取今天的节假日类型(是节假日还是工作日)
    try:
        today_is_holiday = False  # 默认不是法定节假日
        client = getHoliday()
        today_data = client.assemble_holiday_data()
        today_data_type = today_data['type'].get('type')  # 节假日类型
    except:
        print(f'获取今天的节假日类型失败 {today_data}，请检查！')
        exit(1)
    # 判断今天是否是工作日，如果是则去除较远的食物
    # 节假日类型：0：工作日，1：周末，2：节日，3：调班日
    if today_data_type == 0 or today_data_type == 3:
        pop_index = [index for index, food in enumerate(foods) if '近' not in foods_data[food].get('distance')]
        pop_index.reverse()  # 颠倒索引列表，防止删除元素是索引越界
        for index in pop_index:
            foods.pop(index)
            weights.pop(index)
    # print(pop_index, foods, weights)

    # 从食物列表中，随机挑选一个输出食物名称，按Ctrl+C键结束
    try:
        while True:
            lucky_food = random.choices(foods, weights)[0]
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

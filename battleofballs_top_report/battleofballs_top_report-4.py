#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

import os
import sys
from pathlib import Path
import shutil
import datetime
import time
import pyautogui
from PIL import Image, ImageDraw, ImageFont, ImageColor
import easyocr
import json
import math
import win32api
from wechat import *


def open_battleofballs():
    """打开雷电模拟器，然后再打开球球大作战"""
    # 打开雷电模拟器应用
    # ldmnq_exe = 'dnplayer.exe'
    # ldmnq_program_dir = r'C:\Software\leidian\LDPlayer4'
    # ldmnq_program = ldmnq_program_dir + '\\' + ldmnq_exe
    # win32api.ShellExecute(0, 'open', ldmnq_program, '', '', 1)

    # 搜索雷电模拟器应用
    # pyautogui.hotkey('win', 'q')  # 打开"Windows 搜索"菜单
    pyautogui.hotkey('win', 's')  # 打开"Windows 搜索"菜单
    time.sleep(0.5)
    print(f'搜索雷电模拟器应用')
    write('雷电模拟器')
    time.sleep(0.5)
    ldmnq_image = 'images/ldmnq.png'  # 雷电模拟器应用
    ldmnq_location = pyautogui.locateCenterOnScreen(ldmnq_image, confidence=0.85, minSearchTime=2)
    if ldmnq_location:
        print('打开雷电模拟器')
        pyautogui.moveTo(ldmnq_location, duration=0.5)
        pyautogui.click(clicks=1)
        time.sleep(2)  # 等待雷电模拟器启动

        battleofballs_window_image = 'images/battleofballs_window.png'  # 球球大作战主窗口
        battleofballs_window_location = pyautogui.locateCenterOnScreen(battleofballs_window_image, confidence=0.7, minSearchTime=2)
        if battleofballs_window_location:
            time.sleep(2)  # 等待游戏启动
            pyautogui.press('x', presses=8, interval=0.3)  # 连续点击8次自定义键F，关闭游戏启动后的所有弹窗
            top_image = 'images/top.png'  # 球球大作战排行榜图标
            top_location = pyautogui.locateCenterOnScreen(top_image, confidence=0.85, minSearchTime=2)
            if top_location:
                # 打印下球球大作战启动总耗时(球球大作战在后台已启动时，耗时10秒左右，后台未启动时，耗时20秒)
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'球球大作战已打开，共耗时 {tmp_run_time} 秒')
            else:
                print('排行榜图标未正常显示，继续尝试')
                open_battleofballs()  # 球球大作战排行榜图标未正常显示，需要重新调用 open_battleofballs() 函数
        else:
            battleofballs_image = 'images/battleofballs.png'  # 球球大作战应用
            battleofballs_location = pyautogui.locateCenterOnScreen(battleofballs_image, confidence=0.85, minSearchTime=2)
            if battleofballs_location:
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'雷电模拟器已打开，共耗时 {tmp_run_time} 秒')
                print('打开球球大作战')
                pyautogui.moveTo(battleofballs_location, duration=0.5)
                pyautogui.click(clicks=1)
                time.sleep(2)  # 等待球球大作战启动
            open_battleofballs()  # 球球大作战未启动完成，需要重新调用 open_battleofballs() 函数
    else:
        print(f'未找到雷电模拟器应用图标，继续尝试')
        open_battleofballs()  # 未找到雷电模拟器应用图标，需要重新调用 open_battleofballs() 函数


def close_battleofballs():
    """关闭雷电模拟器和球球大作战"""
    ldmnq_exe = 'dnplayer.exe'
    # 关闭模拟器应用
    os.system(f'taskkill /F /IM {ldmnq_exe}')
    print(f'模拟器已关闭 {ldmnq_exe}')
    time.sleep(5)


def look_history_top():
    """查看历史最高段位排行榜"""
    top_image = 'images/top.png'  # 球球大作战排行榜图标
    top_location = pyautogui.locateCenterOnScreen(top_image, confidence=0.85, minSearchTime=2)
    if top_location:
        # 打开排行榜
        print('打开排行榜')
        pyautogui.press('t', presses=3)  # 连续快速点击3次，兼容因关闭游戏启动后所有弹窗时，误打开游戏设置而无法打开排行榜的情况
        time.sleep(1)
        more_top_image = 'images/more_top.png'  # 更多排名图标
        more_top_location = pyautogui.locateCenterOnScreen(more_top_image, confidence=0.85, minSearchTime=2)
        if more_top_location:
            pyautogui.moveTo(more_top_location, duration=0.5)
            pyautogui.click(clicks=1)
            print('更多排名页面已打开')
            time.sleep(1)
            pyautogui.press('f', presses=3)  # 连续快速点击3次自定义键F，查看段位榜，兼容随机出现的榜页面情况
            time.sleep(1)
            pyautogui.press('z', presses=3)  # 连续快速点击3次自定义键F，查看历史最高榜，兼容随机出现的榜页面情况
            time.sleep(1)
            history_top_image = 'images/history_top.png'  # 历史最高段位排行榜页面
            history_top_location = pyautogui.locateCenterOnScreen(history_top_image, confidence=0.85, minSearchTime=2)
            if history_top_location:
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'历史最高段位排行榜已打开，共耗时 {tmp_run_time} 秒')
                time.sleep(1)
            else:
                print('历史最高段位排行榜未正常打开，继续尝试')
                look_history_top()  # 随机出现的榜页面未切换到历史最高段位排行榜，需要重新调用 look_history_top() 函数
        else:
            # 兼容模拟器应用长时间使用会夯住，导致球球大作战应用无法点击使用的情况
            print('更多排名页面未正常打开，模拟器已夯住，球球大作战无法点击使用，需要重启下模拟器')
            close_battleofballs()  # 关闭球球大作战应用
            open_battleofballs()  # 打开球球大作战应用
            look_history_top()  # 重新调用 look_history_top() 函数
    else:
        print('排行榜图标未正常显示，返回游戏主界面，继续尝试')
        pyautogui.press('b')  # 返回游戏主窗口界面
        pyautogui.press('x', presses=2)  # 关闭游戏启动后延时显示的弹窗
        look_history_top()  # 球球大作战排行榜图标未正常显示，需要重新调用 look_history_top() 函数


def look_top():
    """查看大赛季段位排行榜"""
    top_image = 'images/top.png'  # 球球大作战排行榜图标
    top_location = pyautogui.locateCenterOnScreen(top_image, confidence=0.85, minSearchTime=2)
    if top_location:
        # 打开排行榜
        print('打开排行榜')
        pyautogui.press('t', presses=3)  # 连续快速点击3次，兼容因关闭游戏启动后所有弹窗时，误打开游戏设置而无法打开排行榜的情况
        time.sleep(1)
        competition_season_image = 'images/competition_season.png'  # 大赛季页面图标
        competition_season_location = pyautogui.locateCenterOnScreen(competition_season_image, confidence=0.85, minSearchTime=2)
        if competition_season_location:
            pyautogui.moveTo(competition_season_location, duration=0.5)
            pyautogui.click(clicks=1)
            print('大赛季页面已打开')
            time.sleep(1)
            pyautogui.press('f', presses=3)  # 连续快速点击3次自定义键F，查看段位榜，兼容随机出现的榜页面情况
            time.sleep(1)
            pyautogui.press('h', presses=3)  # 连续快速点击3次自定义键H，查看段位分榜，兼容随机出现的榜页面情况
            time.sleep(1)
            level_image = 'images/level.png'  # 大赛季段位排行榜页面
            level_location = pyautogui.locateCenterOnScreen(level_image, confidence=0.85, minSearchTime=2)
            if level_location:
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'大赛季段位排行榜已打开，共耗时 {tmp_run_time} 秒')
                time.sleep(1)
            else:
                print('大赛季段位排行榜未正常打开，继续尝试')
                look_top()  # 随机出现的榜页面未切换到大赛季段位排行榜，需要重新调用 look_top() 函数
        else:
            # 兼容模拟器应用长时间使用会夯住，导致球球大作战应用无法点击使用的情况
            print('大赛季页面未正常打开，模拟器已夯住，球球大作战无法点击使用，需要重启下模拟器')
            close_battleofballs()  # 关闭球球大作战应用
            open_battleofballs()  # 打开球球大作战应用
            look_top()  # 重新调用 look_top() 函数
    else:
        print('排行榜图标未正常显示，返回游戏主界面，继续尝试')
        pyautogui.press('b')  # 返回游戏主窗口界面
        pyautogui.press('x', presses=2)  # 关闭游戏启动后延时显示的弹窗
        look_top()  # 球球大作战排行榜图标未正常显示，需要重新调用 look_top() 函数


def screenshot(image):
    """截屏保存"""
    # 计算球球大作战左上角坐标，雷电模拟器启动后默认居中显示 1920*1080，如果移动窗口可能会导致截图不完成
    screen_width, screen_height = pyautogui.size()
    # print(screen_width, screen_height)  # output: "2560 1440"
    game_width, game_height = (1920, 1080)  # 球球大作战屏幕尺寸
    ldmnq_window_image = 'images/ldmnq_window.png'  # 雷电模拟器窗口
    ldmnq_window_coords = pyautogui.locateOnScreen(ldmnq_window_image, confidence=0.85, minSearchTime=2)
    if ldmnq_window_coords:
        game_left_x, game_top_y = left_lower(ldmnq_window_coords)  # 计算左下角的坐标
        # print(game_left_x, game_top_y)  # output: "319 150"
        # 截屏
        region = (game_left_x, game_top_y, game_width, game_height)
        pyautogui.screenshot(image, region=region)
        time.sleep(1)
        print(f'已截图并保存到 {image}')

        pyautogui.press('b')  # 截图后返回游戏主窗口界面
        # pyautogui.hotkey('alt', 'F4')  # 关闭雷电模拟器应用，容易误伤自己
    else:
        print('未找到雷电模拟器窗口，继续尝试')
        screenshot(image)  # 需要重新调用 look_top() 函数


def watermark(image):
    """给截图加水印"""
    im = Image.open(image)
    # 水印文字
    # text = 'logo'
    text = f"【菲时报】 {datetime.datetime.now().strftime('%F %T')}"
    # 设置颜色
    # color = ImageColor.getrgb('#ff0000')
    # color = '#ff0000'
    color = (120, 142, 95)  # 灰色
    # 设置字体、字体大小
    font = ImageFont.truetype('typefaces/SmileySans-Oblique.ttf', 45)  # 得意黑
    # 添加水印
    draw = ImageDraw.Draw(im)
    draw.text((1350, 45), text, fill=color, font=font)  # 水印左上角坐标为(1350, 45)
    # 保存图像
    im.save(image)
    time.sleep(1)
    print(f'截图已加水印并保存到 {image}')


def ocr(image, box):
    """OCR 识别图像指定区域的文本内容"""
    # 裁切图像
    ocr_image = 'screenshots/tmp_ocr_image.png'
    im = Image.open(image)
    im = im.crop(box)  # 裁切图像指定区域并保存，只识别指定区域的文本内容
    im.save(ocr_image)
    print(f'图像已裁切并保存到 {ocr_image}')

    # OCR 识别
    reader = easyocr.Reader(['ch_sim', 'en'])  # 识别中英文两种语言
    result = reader.readtext(ocr_image, paragraph=True, x_ths=1.5, detail=0)  # 将距离较近的文本合并成段落输出，只输出检测到的文本
    tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
    print(f'图像已识别，共耗时 {tmp_run_time} 秒，识别到的文本内容是：\n{result}')

    # 处理识别的文本
    # 判断段位数据是否为超神段位，如果是则只保留超神的星星数量，如果不是则保留段位信息
    ocr_top_data = {}  # 记录处理后的每行内容
    for index, value in enumerate(result):
        # 分别处理用户名和段位
        if index in list(range(1, len(result), 2)):
            if '超神' in value and value.split()[-1].isdigit():  # 星星数量是否为数字，兼容数字未识别成功的情况
                ocr_top_data[tmp_name] = value.split()[-1]  # 去掉超神等信息，只保留星星数量
            else:
                ocr_top_data[tmp_name] = value  # 保留段位信息
        else:
            tmp_name = value.split()[0]  # 去掉头衔信息，只保留用户名
    print(f'段位排行榜：{ocr_top_data}')

    return ocr_top_data


def update_top_data(current_date, ocr_top_data):
    """更新排行榜历史数据文件"""
    # 判断是否存在排行榜历史数据文件，如果有，就读取文件，不存在则将历史数据设置为一个空字典
    if top_data_file.is_file():
        with open(top_data_file, 'r', encoding='utf-8') as file:
            top_data = json.load(file)
    else:
        top_data = {}

    # 记录用户的段位(星星数量)
    tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
    ocr_top_data['run_time'] = tmp_run_time
    top_data[current_date] = ocr_top_data
    # print(top_data)
    # 将排行榜历史数据记录到文件中
    print(f'更新排行榜历史数据文件 {top_data_file}')
    with open(top_data_file, 'w', encoding='utf-8') as file:
        file.write(json.dumps(top_data, ensure_ascii=False, indent=4))


def update_history_top():
    """更新历史最高排行榜第一名"""
    current_month = datetime.datetime.now().strftime('%Y-%m')  # 当前月份 2023-02
    print(f'{current_month}，更新历史最高段位排行榜')
    # 查看历史最高段位排行榜
    screenshot_image = files_dir.joinpath(f"screenshot_{current_month}.png")  # 截图名称
    open_battleofballs()  # 打开球球大作战
    look_history_top()  # 查看历史最高段位排行榜
    screenshot(screenshot_image)  # 截图历史最高段位排行榜
    watermark(screenshot_image)  # 给截图加水印
    # 裁切图像指定区域，只识别历史最高排行榜第一名
    ocr_box = (420, 240, 1310, 355)  # 排行榜第一名，识别用户名、段位
    ocr_result = ocr(screenshot_image, ocr_box)  # OCR 识别
    tmp_top_data = [[key, value] for key, value in ocr_result.items()]
    print(f'历史最高排行榜第一名：{tmp_top_data[0][0]}，段位：{tmp_top_data[0][1]}\n')
    update_top_data(current_month, ocr_result)  # 更新排行榜历史数据文件


def generate_message(ocr_top_data):
    """读取 OCR 识别到的文本，生成信息内容"""
    # 判断是否存在排行榜历史数据文件，有就读取历史数据文件，没有则将历史数据设置为一个空字典
    if top_data_file.is_file():
        with open(top_data_file, 'r', encoding='utf-8') as file:
            top_data = json.load(file)
    else:
        top_data = {}

    # 生成信息内容
    message = f'【菲时报，为您播报】\n北京时间：{ft_date_time}\n'
    # 凌晨0点会有特殊提醒消息
    if datetime.datetime.now().hour == 0 and datetime.datetime.now().minute < 10:
        message += '\n新的一天开始喽，继续加油哦！\n'

    # 最新段位排行榜
    long_name_length = len(max([k for k in ocr_top_data], key=lambda name: len(name))) + 2  # 最长用户名的长度加2
    sep = '   '  # 一个中文字符的宽度对应三个空格的宽度
    message += '\n最新段位排行榜：\n'
    message += '{:<4}{}{:<6}{:>4}\n'.format('排名', '用户名' + sep * (long_name_length - len('用户名')), '段位', '日新增')
    # 加入排行榜信息
    count = 1
    for key, value in ocr_top_data.items():
        # 判断是否有排行榜历史数据，有就获取用户的历史段位(星星数量)，没有就将历史数据设置为空字符串
        if top_data:
            history_ft_date_time = [k for k in top_data][-1]  # 最后一次的历史数据
            print(f'上一次的历史数据：{history_ft_date_time}')
            history_stars = top_data[history_ft_date_time].get(key, '')  # 如果未获取到历史数据则返回空字符串
            today_history_data = [k for k in top_data if k.startswith(ft_date_time.split()[0])]  # 今日历史数据
            if today_history_data:
                today_history_ft_date_time = today_history_data[0]  # 用户今日的第一条历史数据
                print(f'今日的第一条历史数据：{today_history_ft_date_time}')
                today_history_stars = top_data[today_history_ft_date_time].get(key, '')  # 如果未获取到历史数据则返回空字符串
            else:
                today_history_stars = ''
        else:
            history_stars = ''
            today_history_stars = ''
        # 判断当前和历史段位(星星数量)是否都为数字，是的话就计算
        print(key, value, history_stars, today_history_stars)
        if value.isdigit():
            if history_stars.isdigit():
                delta_stars = int(value) - int(history_stars)  # 用户新增星星数量
            elif history_stars:
                delta_stars = int(value)  # 历史段位不为空，是超神以下，用户新增星星数量等于当前星星数量
            else:
                delta_stars = '-'  # 历史段位为空串，无数据，用户新增星星数量等于'-'
            if today_history_stars.isdigit():
                today_delta_stars = int(value) - int(today_history_stars)  # 用户今日新增星星数量
            elif today_history_stars:
                today_delta_stars = int(value)  # 历史段位不为空，是超神以下，用户今日新增星星数量等于当前星星数量
            else:
                today_delta_stars = '-'  # 历史段位为空串，无数据，用户今日新增星星数量等于'-'
        else:
            delta_stars = '-'
            today_delta_stars = '-'

        message += '{:<8}{}{:<6}{:>8}({})\n'.format(count, key + sep * (long_name_length - len(key)), value, today_delta_stars, delta_stars)
        count += 1

    # 历史最高段位排行榜
    # 判断是否有排行榜历史数据，有就获取历史最高段位(星星数量)
    current_month = datetime.datetime.now().strftime('%Y-%m')  # 当前月份 2023-02
    if top_data:
        history_top = top_data.get(current_month)
        # 判断是否有历史最高段位数据
        if history_top:
            tmp_top_data = [[key, value] for key, value in history_top.items()]
            history_top_name, history_top_stars = tmp_top_data[0][0], tmp_top_data[0][1]  # 历史最高段位
            t_top_data = [[key, value] for key, value in ocr_top_data.items()]
            first_name, first_stars = t_top_data[0][0], t_top_data[0][1]  # 当前段位排行榜第一名
            print(f'历史最高排行榜第一名：{history_top_name}，段位：{history_top_stars}')
            print(f'当前段位排行榜第一名：{first_name}，段位：{first_stars}')
            message += f'\n历史最高段位：\n'
            # print(history_top_stars, first_stars)

            # 判断当前和历史最高的段位(星星数量)是否都为数字，是的话就计算
            if first_stars.isdigit() and history_top_stars.isdigit():
                # 当月的总天数
                next_month_first_day = (datetime.date.today().replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
                current_month_first_day = datetime.date.today().replace(day=1)
                current_month_days = (next_month_first_day - current_month_first_day).days
                # 平均每天需要升级的星星数量，超神以下的段位数暂不计算在内
                # 青铜3颗、白银4颗、黄金两段8颗，共计15颗；月初段位重置后最高为白金段位，白金以下暂不计算在内
                # 白金两段10颗、钻石三段15颗、大师三段15颗、王者三段17颗(一段5颗、二三段6颗)，共计57颗
                day_average_stars = math.ceil((int(history_top_stars) + 1) / current_month_days)
                hour_average_stars = math.ceil(day_average_stars / 24)
                # 今日目标星星数量
                today_target_stars = day_average_stars * datetime.date.today().day
                message += '{:<5}{:<5}{}\n'.format('总目标', '日目标', '日平均(时)')
                message += '{:<9}{:<9}{}({})\n'.format(int(history_top_stars) + 1, today_target_stars, day_average_stars, hour_average_stars)

                # 距离历史最高还差多少颗星星
                remain_stars = int(history_top_stars) - int(first_stars) + 1
                # 距离今天目标还差多少颗星星
                if int(first_stars) < today_target_stars:
                    today_remain_stars = today_target_stars - int(first_stars)
                elif int(first_stars) == today_target_stars:
                    today_remain_stars = '已达标'
                else:
                    today_remain_stars = f'超额完成 {-(today_target_stars - int(first_stars))}'
                # 当月剩余天数(包含当天，按小时折算)
                remain_days = current_month_days - datetime.date.today().day
                current_hour = datetime.datetime.today().hour
                remain_days += (24 - current_hour) / 24
                # 预计剩余天数每天需要升级的星星数量
                remain_day_average_stars = math.ceil(remain_stars / remain_days)
                remain_hour_average_stars = math.ceil(remain_day_average_stars / 24)
                message += '{:<5}{:<5}{}\n'.format('总差距', '日差距', '日需平均(时)')
                message += '{:<9}{:<9}{}({})\n'.format(remain_stars, today_remain_stars, remain_day_average_stars, remain_hour_average_stars)
            else:
                message += f'当前段位排行榜第一名段位较低 {first_stars}，超神以下暂不计算\n'

    print('新的信息内容已生成')
    # print(message)
    return message


def task():
    """执行任务"""
    # 联系人
    # contact_name = 'ghost'
    # contact_name = '东升的太阳'
    contact_name = '菲时报'

    # 截图名称
    screenshot_image = files_dir.joinpath(f"screenshot_{datetime.datetime.now().strftime('%F_%H-%M-%S')}.png")

    # 执行任务
    # 查看大赛季段位排行榜
    open_battleofballs()  # 打开球球大作战
    look_top()  # 查看大赛季段位排行榜
    screenshot(screenshot_image)  # 截图大赛季段位排行榜
    watermark(screenshot_image)  # 给截图加水印
    # 裁切图像指定区域，只识别排行榜前三名
    # ocr_box = (100, 200, 1310, 570)  # 排行榜前三名，识别排名、用户名、段位
    ocr_box = (420, 240, 1310, 570)  # 排行榜前三名，识别用户名、段位
    # ocr_box = (1185, 240, 1310, 570)  # 排行榜前三名，只识别段位(星星数)
    ocr_result = ocr(screenshot_image, ocr_box)  # OCR 识别
    message_content = generate_message(ocr_result)  # 生成信息内容
    update_top_data(ft_date_time, ocr_result)  # 更新排行榜历史数据文件

    # 微信播报最新段位排行榜
    open_wechat()  # 打开微信
    search_contact(contact_name)  # 搜索联系人
    send_message(message_content, 'text')  # 发送文字消息
    send_message(screenshot_image, 'image')  # 发送图片消息


def main():
    """主函数"""
    global tmp_start_time, ft_date_time
    # exec_task_time = list(range(0, 60, 20))  # 整点开始，每二十分钟执行一次
    exec_task_time = [0, 30]  # 执行任务的时间分钟，整点、5分、30分执行
    wait_time = 60  # 程序等待时间
    repost_count = 1  # 记录播报次数
    while True:
        date_time = datetime.datetime.now()  # 当前时间
        ft_date_time = date_time.strftime('%F %T')  # 2023-01-17 12:00:00
        tmp_start_time = date_time.timestamp()  # 任务开始执行时间
        date_time_minute = date_time.minute  # 当前时间分钟数
        date_time_day = date_time.day  # 当前时间天数
        last_month = (date_time.replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m')  # 上个月月份 2023-01

        # 月初第一天，切割下历史排行榜文件
        if date_time_day == 1:
            top_data_file_bak = current_dir.joinpath(top_data_file.name.replace('.', f'-{last_month}.'))
            # 如果不存在上个月的文件，则切割；如果存在，则说明已经切割了
            if not top_data_file_bak.is_file():
                shutil.move(top_data_file, top_data_file_bak)
                print(f'历史排行榜文件已切割完成 {top_data_file_bak}')

        # 月初第一天，更新下历史最高段位排行榜
        if date_time_day == 1 and date_time_minute < 10:
            update_history_top()

        # 判断是否到执行任务的时间，是则继续，否则继续等待；第一执行任务时不需要检查时间
        if repost_count != 1:
            if date_time_minute not in exec_task_time:
                time.sleep(wait_time)  # 程序等待
                continue  # 中断当前循环的当次执行，继续下一次循环
        print(f"{ft_date_time} 第 {repost_count} 次执行播报")
        task()  # 执行任务
        date_time = datetime.datetime.now()  # 当前时间
        date_time_second = date_time.second  # 当前时间秒钟数
        tmp_run_time = int(date_time.timestamp() - tmp_start_time)
        print(f"{date_time.strftime('%F %T')} 第 {repost_count} 次播报完成，共耗时 {tmp_run_time} 秒\n")
        repost_count += 1
        time.sleep(60 - date_time_second)  # 程序等待，确保一分钟内只会播报一次，且下次也能整分钟播报


if __name__ == '__main__':
    # 程序开始时间
    start_time = tmp_start_time = datetime.datetime.now().timestamp()
    ft_date_time = datetime.datetime.now().strftime('%F %T')
    print(f"开始时间：{ft_date_time}\n")

    # 切换到脚本所在目录
    script_dir = sys.path[0]  # 脚本所在目录
    os.chdir(script_dir)  # 切换到脚本所在目录
    current_dir = Path.cwd()  # 当前所在目录
    files_dir = current_dir.joinpath('screenshots')  # 截图文件存放目录
    files_dir.mkdir(exist_ok=True)  # 如果目录不存在，创建截图文件存放目录
    top_data_file = current_dir.joinpath('top.json')  # 排行榜历史数据文件

    main()  # 主函数

    # 程序结束时间
    run_time = int(datetime.datetime.now().timestamp() - start_time)
    print(f'\n共耗时 {run_time} 秒')
    print(f"结束时间：{datetime.datetime.now().strftime('%F %T')}\n")

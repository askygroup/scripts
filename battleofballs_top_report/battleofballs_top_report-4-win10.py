#!/usr/bin/python3
# _*_ coding: utf-8 _*_

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
from wechat_win10 import *
from online_doc_win10 import *


def open_battleofballs():
    """打开雷电模拟器，然后再打开球球大作战"""
    global max_retry_count
    # 打开雷电模拟器应用
    # ldmnq_exe = 'dnplayer.exe'
    # ldmnq_program_dir = r'D:\leidian\LDPlayer4'
    # ldmnq_program = ldmnq_program_dir + '\\' + ldmnq_exe
    # win32api.ShellExecute(0, 'open', ldmnq_program, '', '', 1)

    # 搜索雷电模拟器应用
    # pyautogui.hotkey('win', 'q')  # 打开"Windows 搜索"菜单
    pyautogui.hotkey('win', 's')  # 打开"Windows 搜索"菜单
    time.sleep(0.5)
    print('搜索雷电模拟器应用')
    write('雷电模拟器')
    time.sleep(0.5)
    ldmnq_image = 'images/ldmnq-win10.png'  # 雷电模拟器应用
    ldmnq_location = pyautogui.locateCenterOnScreen(ldmnq_image, confidence=0.85, minSearchTime=2)
    if ldmnq_location:
        print('打开雷电模拟器')
        pyautogui.moveTo(ldmnq_location, duration=0.5)
        pyautogui.click(clicks=1)
        time.sleep(2)  # 等待雷电模拟器启动

        battleofballs_window_image = 'images/battleofballs_window-win10.png'  # 球球大作战主窗口
        battleofballs_window_location = pyautogui.locateCenterOnScreen(battleofballs_window_image, confidence=0.7, minSearchTime=2)
        if battleofballs_window_location:
            top_image = 'images/top-win10.png'  # 球球大作战排行榜图标
            top_location = pyautogui.locateCenterOnScreen(top_image, confidence=0.85, minSearchTime=2)
            if top_location:
                # 打印下球球大作战启动总耗时(球球大作战在后台已启动时，耗时10秒左右，后台未启动时，耗时20秒)
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'球球大作战已打开，共耗时 {tmp_run_time} 秒')
                max_retry_count = 5  # 球球大作战打开后，重置最大可重试次数
            else:
                if max_retry_count:
                    max_retry_count -= 1  # 最大可重试次数-1
                    print('球球大作战已打开，但排行榜图标未正常显示，继续尝试')
                    time.sleep(2)  # 等待游戏启动
                    pyautogui.press('x', presses=8, interval=0.3)  # 连续点击8次自定义键X，关闭游戏启动后的所有弹窗
                else:
                    print('排行榜图标未正常显示，球球大作战无法正常使用，需要重启模拟器')
                    close_program(ldmnq_exe)  # 关闭球球大作战应用
                    max_retry_count = 5  # 球球大作战重新打开后，重置最大可重试次数
                open_battleofballs()  # 球球大作战排行榜图标未正常显示，需要重新调用 open_battleofballs() 函数
        else:
            battleofballs_image = 'images/battleofballs-win10.png'  # 球球大作战应用
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


def close_program(program):
    """关闭应用程序"""
    if program:
        # 关闭应用程序
        os.system(f'taskkill /F /IM {program}')
        print(f'{program} 应用程序已关闭')
        time.sleep(5)
    else:
        print(f'应用程序可执行文件 {program} 为空，请确认！！！')
        exit(1)


def look_history_top():
    """查看历史最高段位排行榜"""
    global max_retry_count
    top_image = 'images/top-win10.png'  # 球球大作战排行榜图标
    top_location = pyautogui.locateCenterOnScreen(top_image, confidence=0.85, minSearchTime=2)
    if top_location:
        # 打开排行榜
        print('打开排行榜')
        pyautogui.press('t', presses=2, interval=0.3)  # 连续点击2次自定义键T，兼容因关闭游戏启动后所有弹窗时，误打开游戏设置而无法打开排行榜的情况
        time.sleep(1)
        more_top_image = 'images/more_top-win10.png'  # 更多排名图标
        more_top_location = pyautogui.locateCenterOnScreen(more_top_image, confidence=0.85, minSearchTime=2)
        if more_top_location:
            max_retry_count = 5  # 更多排名页面打开后，重置最大可重试次数
            pyautogui.moveTo(more_top_location, duration=0.5)
            pyautogui.click(clicks=1)
            print('更多排名页面已打开')
            time.sleep(1)
            pyautogui.press('f', presses=2, interval=0.3)  # 连续点击2次自定义键F，查看段位榜，兼容随机出现的榜页面情况
            time.sleep(1)
            pyautogui.press('z', presses=2, interval=0.3)  # 连续点击2次自定义键Z，查看历史最高榜，兼容随机出现的榜页面情况
            time.sleep(1)
            history_top_image = 'images/history_top-win10.png'  # 历史最高段位排行榜页面
            history_top_location = pyautogui.locateCenterOnScreen(history_top_image, confidence=0.85, minSearchTime=2)
            if history_top_location:
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'历史最高段位排行榜已打开，共耗时 {tmp_run_time} 秒')
                time.sleep(2)
            else:
                print('历史最高段位排行榜未正常打开，继续尝试')
                look_history_top()  # 随机出现的榜页面未切换到历史最高段位排行榜，需要重新调用 look_history_top() 函数
        else:
            if max_retry_count:
                max_retry_count -= 1  # 最大可重试次数-1
                print('更多排名页面未正常打开，继续尝试')
                look_history_top()  # 重新调用 look_top() 函数
            else:
                # 兼容模拟器应用长时间使用会夯住，导致球球大作战应用无法点击使用的情况
                print('更多排名页面未正常打开，模拟器已夯住，球球大作战无法点击使用，需要重启模拟器')
                close_program(ldmnq_exe)  # 关闭球球大作战应用
                open_battleofballs()  # 打开球球大作战应用
                max_retry_count = 5  # 球球大作战重新打开后，重置最大可重试次数
                look_history_top()  # 重新调用 look_history_top() 函数
    else:
        print('排行榜图标未正常显示，返回游戏主界面，继续尝试')
        pyautogui.press('b')  # 返回游戏主窗口界面
        pyautogui.press('x', presses=2, interval=0.3)  # 连续点击2次自定义键X，关闭游戏启动后延时显示的弹窗
        look_history_top()  # 排行榜图标未正常显示，需要重新调用 look_history_top() 函数


def look_top():
    """查看大赛季段位排行榜"""
    global max_retry_count
    top_image = 'images/top-win10.png'  # 球球大作战排行榜图标
    top_location = pyautogui.locateCenterOnScreen(top_image, confidence=0.85, minSearchTime=2)
    if top_location:
        # 打开排行榜
        print('打开排行榜')
        pyautogui.press('t', presses=2, interval=0.3)  # 连续点击2次，兼容因关闭游戏启动后所有弹窗时，误打开游戏设置而无法打开排行榜的情况
        time.sleep(1)
        competition_season_image = 'images/competition_season-win10.png'  # 大赛季页面图标
        competition_season_location = pyautogui.locateCenterOnScreen(competition_season_image, confidence=0.85, minSearchTime=2)
        if competition_season_location:
            max_retry_count = 5  # 大赛季页面打开后，重置最大可重试次数
            pyautogui.moveTo(competition_season_location, duration=0.5)
            pyautogui.click(clicks=1)
            print('大赛季页面已打开')
            time.sleep(1)
            pyautogui.press('f', presses=2, interval=0.3)  # 连续点击2次自定义键F，查看段位榜，兼容随机出现的榜页面情况
            time.sleep(1)
            pyautogui.press('h', presses=2, interval=0.3)  # 连续点击2次自定义键H，查看段位分榜，兼容随机出现的榜页面情况
            time.sleep(1)
            level_image = 'images/level-win10.png'  # 大赛季段位排行榜页面
            level_location = pyautogui.locateCenterOnScreen(level_image, confidence=0.85, minSearchTime=2)
            if level_location:
                tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
                print(f'大赛季段位排行榜已打开，共耗时 {tmp_run_time} 秒')
                time.sleep(2)
            else:
                print('大赛季段位排行榜未正常打开，继续尝试')
                look_top()  # 随机出现的榜页面未切换到大赛季段位排行榜，需要重新调用 look_top() 函数
        else:
            if max_retry_count:
                max_retry_count -= 1  # 最大可重试次数-1
                print('大赛季页面未正常打开，继续尝试')
                look_top()  # 重新调用 look_top() 函数
            else:
                # 兼容模拟器应用长时间使用会夯住，导致球球大作战应用无法点击使用的情况
                print('大赛季页面未正常打开，模拟器已夯住，球球大作战无法点击使用，需要重启模拟器')
                close_program(ldmnq_exe)  # 关闭球球大作战应用
                open_battleofballs()  # 打开球球大作战应用
                max_retry_count = 5  # 球球大作战重新打开后，重置最大可重试次数
                look_top()  # 重新调用 look_top() 函数
    else:
        print('排行榜图标未正常显示，返回游戏主界面，继续尝试')
        pyautogui.press('b')  # 返回游戏主窗口界面
        pyautogui.press('x', presses=2, interval=0.3)  # 连续点击2次自定义键X，关闭游戏启动后延时显示的弹窗
        look_top()  # 排行榜图标未正常显示，需要重新调用 look_top() 函数


def screenshot(image):
    """截屏保存"""
    # 计算球球大作战左上角坐标，雷电模拟器启动后默认居中显示 1920*1080，如果移动窗口可能会导致截图不完成
    screen_width, screen_height = pyautogui.size()
    # print(screen_width, screen_height)  # output: "1920 1080"
    game_width, game_height = (1747, 983)  # 球球大作战屏幕尺寸
    ldmnq_window_image = 'images/ldmnq_window-win10.png'  # 雷电模拟器窗口
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
    draw.text((1200, 35), text, fill=color, font=font)  # 水印左上角坐标为(1200, 35)
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
    result = reader.readtext(ocr_image, paragraph=True, x_ths=2, detail=0)  # 将距离较近的文本合并成段落输出，只输出检测到的文本
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
    print(f'{current_month} 更新历史最高段位排行榜')
    # 查看历史最高段位排行榜
    screenshot_image = files_dir.joinpath(f"screenshot_{current_month}.png")  # 截图名称
    open_battleofballs()  # 打开球球大作战
    look_history_top()  # 查看历史最高段位排行榜
    screenshot(screenshot_image)  # 截图历史最高段位排行榜
    watermark(screenshot_image)  # 给截图加水印
    # 裁切图像指定区域，只识别历史最高排行榜第一名
    ocr_box = (385, 220, 1200, 320)  # 排行榜第一名，识别用户名、段位
    ocr_result = ocr(screenshot_image, ocr_box)  # OCR 识别
    tmp_top_data = [[key, value] for key, value in ocr_result.items()]
    print(f'历史最高排行榜第一名：{tmp_top_data[0][0]}，段位：{tmp_top_data[0][1]}')
    update_top_data(current_month, ocr_result)  # 更新排行榜历史数据文件


def generate_message(ocr_top_data):
    """读取 OCR 识别到的文本，生成信息内容"""
    def new_top_message():
        """生成最新段位排行榜信息"""
        nonlocal top_data, ocr_top_data, message, current_ft_date_time

        print('开始生成最新段位排行榜信息')
        # 青铜3颗、白银4颗、黄金两段8颗、白金两段10颗、钻石前二段10颗，共计35颗；月初段位重置后最高为钻石二段满星
        # 钻石第三段1+5颗(其中钻石二段满星到砖石三段直接有1颗星)、大师三段15颗、王者三段17颗(一段5颗、二三段6颗)，共计38颗
        start_stars = 38  # 赛季重置后，超神以下需要升级的段位星星数
        long_name_length = len(max([k for k in ocr_top_data], key=lambda name: len(name))) + 1
        sep = '   '  # 一个中文字符的宽度对应三个空格的宽度
        message += '\n最新段位排行榜：\n'
        message += '{:<4}{}{:<6}{:>4}\n'.format('排名', '用户名' + sep * (long_name_length - len('用户名')), '段位', '日新增(最近)')
        # 加入排行榜信息
        count = 1
        for key, value in ocr_top_data.items():
            if count > 3:  # 只加入排行榜前三名信息
                break
            # 判断是否有排行榜历史数据，有就获取用户的历史段位(星星数量)，没有就将历史数据设置为空字符串
            if top_data:
                history_ft_date_time = [k for k in top_data][-1]  # 最近一次的历史数据
                history_stars = top_data[history_ft_date_time].get(key, '')  # 如果未获取到历史数据则返回空字符串
                day_history_data = [k for k in top_data if k.startswith(current_ft_date_time.split()[0])]  # 当日历史数据，凌晨00:05前获取的是前一天的数据
                if day_history_data:
                    day_history_ft_date_time = day_history_data[0]  # 用户当日的第一条历史数据
                    day_history_stars = top_data[day_history_ft_date_time].get(key, '')  # 如果未获取到历史数据则返回空字符串
                    if count == 1:  # 只打印一次
                        print(f'当日的第一条历史数据：{day_history_ft_date_time}: {top_data[day_history_ft_date_time]}')
                        print(f'最近一次的历史数据：{history_ft_date_time}: {top_data[history_ft_date_time]}')
                else:
                    day_history_stars = ''
            else:
                history_stars = ''
                day_history_stars = ''
            # 判断当前和历史段位(星星数量)是否都为数字，是的话就计算
            print(f'第 {count} 名，当前和历史段位数据：{key} {value} {history_stars} {day_history_stars}')
            if value.isdigit():
                # 计算用户新增星星数量
                if history_stars.isdigit():
                    delta_stars = int(value) - int(history_stars)
                elif history_stars:
                    delta_stars = int(value)  # 历史段位不为空，是超神以下，用户新增星星数量等于当前星星数量
                else:
                    delta_stars = '-'  # 历史段位为空串，无数据，用户新增星星数量等于'-'
                # 用户当日新增星星数量
                if day_history_stars.isdigit():
                    day_delta_stars = int(value) - int(day_history_stars)
                elif day_history_stars:
                    day_delta_stars = int(value)  # 历史段位不为空，是超神以下或识别的段位有问题，用户新增星星数量等于当前星星数量
                    # 月初第一天，用户当日新增星星数量等于当前星星数量，加上超神以下需要升级的段位星星数
                    if current_ft_date_time.split()[0].split('-')[-1] == '01':
                        day_delta_stars = int(value) + start_stars
                else:
                    day_delta_stars = '-'  # 历史段位为空串，无数据，用户当日新增星星数量等于'-'
                    # 月初第一天，用户当日新增星星数量等于当前星星数量，加上超神以下需要升级的段位星星数
                    if current_ft_date_time.split()[0].split('-')[-1] == '01':
                        day_delta_stars = int(value) + start_stars
            else:
                delta_stars = '-'
                day_delta_stars = '-'

            message += '{:<8}{}{:<6}{:>8}({})\n'.format(count, key + sep * (long_name_length - len(key)), value, day_delta_stars, delta_stars)
            count += 1

    def history_top_message():
        """生成历史最高段位排行榜信息"""
        nonlocal top_data, ocr_top_data, message

        print('开始生成历史最高段位排行榜信息')
        top_username_info = top_data.get('top_username')  # 获取本月冲榜用户名
        if top_username_info:
            first_name = top_username_info.get('主号')  # 获取本月冲榜主号
            if first_name:
                first_stars = ocr_top_data.get(first_name)  # 冲榜主号段位
        else:
            first_name = ''

        # 判断是否有排行榜历史数据，有就获取历史最高段位(星星数量)
        current_month = datetime.datetime.now().strftime('%Y-%m')  # 当前月份 2023-02
        one_day_hours = 24  # 一天的小时数
        if top_data:
            history_top = top_data.get(current_month)
            # 判断是否有历史最高段位数据
            if history_top:
                tmp_top_data = [[key, value] for key, value in history_top.items()]
                history_top_name, history_top_stars = tmp_top_data[0][0], tmp_top_data[0][1]  # 历史最高段位
                # 判断是否存在主号信息，是统计主号，不是就统计当前段位第一名
                if first_name and first_stars:
                    print(f'冲榜主号：{first_name}，段位：{first_stars}')
                else:
                    t_top_data = [[key, value] for key, value in ocr_top_data.items()]
                    first_name, first_stars = t_top_data[0][0], t_top_data[0][1]  # 当前段位排行榜第一名
                    print(f'当前段位排行榜第一名：{first_name}，段位：{first_stars}')
                print(f'历史最高排行榜第一名：{history_top_name}，段位：{history_top_stars}')
                message += f'\n历史最高段位：\n'
                # print(history_top_stars, first_stars)

                # 判断当前和历史最高的段位(星星数量)是否都为数字，是的话就计算
                if first_stars.isdigit() and history_top_stars.isdigit():
                    # 当月的总天数
                    next_month_first_day = (datetime.date.today().replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
                    current_month_first_day = datetime.date.today().replace(day=1)
                    current_month_days = (next_month_first_day - current_month_first_day).days
                    # 平均每天需要升级的星星数量，超神以下的段位数暂不计算在内
                    day_average_stars = (int(history_top_stars) + 1) / current_month_days
                    hour_average_stars = day_average_stars / one_day_hours
                    # 今日目标星星数量
                    today_target_stars = day_average_stars * datetime.date.today().day
                    # 凌晨0点分钟数小于5时，当前的数据应该是前一天的数据
                    if datetime.datetime.now().hour == 0 and datetime.datetime.now().minute < 5:
                        today_target_stars = day_average_stars * (datetime.date.today().day - 1)
                    # 今时目标星星数量
                    today_remain_hours = one_day_hours - datetime.datetime.now().hour - 1  # 今天剩余小时数
                    # 分钟数小于5时，段位数据应该是前一小时的数据
                    if datetime.datetime.now().minute < 5:
                        today_remain_hours = one_day_hours - datetime.datetime.now().hour  # 今天剩余小时数
                        if datetime.datetime.now().hour == 0:  # 如果是凌晨0点分钟数小于5时，今日剩余小时数为0
                            today_remain_hours = 0
                    hour_target_stars = math.ceil(today_target_stars - today_remain_hours * hour_average_stars)
                    today_target_stars = math.ceil(today_target_stars)
                    hour_average_stars = math.ceil(hour_average_stars)
                    day_average_stars = math.ceil(day_average_stars)
                    message += '{:<5}{:<9}{}\n'.format('总目标', '日目标(时)', '日平均(时)')
                    message += '{:<8}{}({}){:>8}({})\n'.format(int(history_top_stars) + 1, today_target_stars, hour_target_stars, day_average_stars, hour_average_stars)

                    # 距离历史最高还差多少颗星星
                    remain_stars = int(history_top_stars) - int(first_stars) + 1
                    # 距离今日目标还差多少颗星星
                    today_remain_stars = today_target_stars - int(first_stars)
                    if today_remain_stars == 0:
                        today_remain_stars = '已达标'
                    elif today_remain_stars < 0:
                        today_remain_stars = f'超 {-today_remain_stars}'
                    # 距离今时目标还差多少颗星星
                    hour_remain_stars = hour_target_stars - int(first_stars)
                    if hour_remain_stars == 0:
                        hour_remain_stars = '已达标'
                    elif hour_remain_stars < 0:
                        hour_remain_stars = f'超 {-hour_remain_stars}'
                    # 当月剩余天数(包含当天，当天按小时折算)
                    remain_days = current_month_days - datetime.date.today().day
                    remain_days += (one_day_hours - datetime.datetime.now().hour - 1) / one_day_hours
                    if remain_days < 1:  # 如果当月剩余天数小于1，将值赋值为1
                        remain_days = 1
                    # 预计剩余天数每天需要升级的星星数量
                    remain_day_average_stars = remain_stars / remain_days
                    # 预计剩余天数每小时需要升级的星星数量
                    remain_hour_average_stars = math.ceil(remain_day_average_stars / one_day_hours)
                    remain_day_average_stars = math.ceil(remain_day_average_stars)
                    message += '{:<5}{:<9}{}\n'.format('总差距', '日差距(时)', '日需平均(时)')
                    message += '{:<8}{}({}){:>8}({})\n'.format(remain_stars, today_remain_stars, hour_remain_stars, remain_day_average_stars, remain_hour_average_stars)
                else:
                    message += f'当前段位排行榜第一名段位较低 {first_stars}，超神以下暂不计算\n'

    def count_stars_message():
        """生成当日段位升级效率统计信息"""
        nonlocal top_data, ocr_top_data, message, current_ft_date_time, current_hour

        print('开始生成段位升级效率统计信息')
        top_username_info = top_data.get('top_username')  # 获取本月冲榜用户名
        if top_username_info:
            first_name = top_username_info.get('主号')  # 获取本月冲榜主号
            if first_name:
                first_stars = ocr_top_data.get(first_name)  # 冲榜主号段位
        else:
            first_name = ''

        # 判断是否存在主号信息，是统计主号，不是就统计当前段位第一名
        if first_name and first_stars:
            print(f'冲榜主号：{first_name}，段位：{first_stars}')
        else:
            t_top_data = [[key, value] for key, value in ocr_top_data.items()]
            first_name, first_stars = t_top_data[0][0], t_top_data[0][1]  # 当前段位排行榜第一名
            print(f'当前段位排行榜第一名：{first_name}，段位：{first_stars}')
        # 判断是否有排行榜历史数据，有就获取当日数据
        if top_data:
            day_history_data = [k for k in top_data if k.startswith(current_ft_date_time.split()[0])]  # 当日历史数据
            # print(day_history_data)
            if day_history_data:
                message += f'\n段位升级效率统计({first_name})：\n'
                count_hours = ['{:0>2}'.format(i) for i in range(0, current_hour + 1)]
                # 用户当日段位数据
                day_stars = {}  # 星星数量
                for hour in count_hours:
                    hour_ft_date_time = f'{current_ft_date_time.split()[0]} {hour}'
                    hour_history_data = [k for k in top_data if k.startswith(hour_ft_date_time)]
                    if hour_history_data:
                        hour_ft_date_time = hour_history_data[0]  # 当前小时的第一条历史数据
                        hour_history_stars = top_data[hour_ft_date_time].get(first_name, '')  # 如果未获取到历史数据则返回空字符串
                    else:
                        hour_history_stars = ''
                    day_stars[hour_ft_date_time.split(':')[0]] = hour_history_stars
                # 分钟数小于5时，只统计前一小时数据
                if datetime.datetime.now().minute < 5:
                    current_hour = current_hour
                else:
                    current_hour = current_hour + 1
                day_stars['{} {:0>2}'.format(current_ft_date_time.split()[0], current_hour)] = first_stars  # 当前时间段位数据
                print(f'{first_name} 当日每小时段位历史数据：{day_stars}')
                # 统计当日段位升级效率
                cache_hour = [k for k in day_stars][0]  # 当天的第一条历史数据的时间
                cache_stars = day_stars[cache_hour]  # 当天的第一条历史数据
                count_stars = []  # 统计段位升级效率
                day_stars.pop(cache_hour)  # 去除当天的第一条历史数据
                for stars in day_stars.values():
                    if stars.isdigit():
                        if cache_stars.isdigit():
                            count_stars.append(str(int(stars) - int(cache_stars)))
                        elif cache_stars:
                            count_stars.append(stars)  # 历史段位不为空，是超神以下，用户新增星星数量等于当前星星数量
                        else:
                            count_stars.append('-')  # 历史段位为空串，无数据，用户新增星星数量等于'-'
                    else:
                        count_stars.append('-')  # 当前段位是超神以下，用户新增星星数量等于'-'
                    cache_stars = stars
                print(f'{first_name} 当日每小时段位升级效率：{count_stars}')
                # 生成当日段位升级效率统计信息
                for i in range(0, current_hour, 4):
                    tmp_count_stars = count_stars[i:i + 4]
                    sum_stars = sum([int(i) for i in tmp_count_stars if i.isdigit()])
                    tmp_count_stars = ['{:>2}'.format(i) for i in tmp_count_stars]
                    message += '{:0>2}-{:0>2}(共计{:>2})：{}\n'.format(str(i), str(i + 3), sum_stars, ' '.join(tmp_count_stars))

    def info_message():
        """生成本月赞助、本月榜号、当前打手名字、打手效率统计的在线表格网站等信息"""
        nonlocal top_data, message
        # 打印本月赞助的小伙伴
        print('开始生成本月赞助信息')
        vip_info = top_data.get('vip')  # 获取本月赞助的小伙伴
        if vip_info:
            print(f'赞助信息：{vip_info}')
            money = sum(vip_info.values())  # 赞助费列表
            print(f'本月共收到赞助费：{round(money, 2)} 元')
            vip = list(vip_info.keys())  # 小伙伴列表
            # message += '\n##### 贵宾观战席 #####\n'
            message += '\n##### 电费赞助商 #####\n'
            message += '#\n'
            vip_top = [f'#  {i}\n' for i in vip[:3]]  # 前三名
            message += f"{''.join(vip_top)}"
            message += '#\n'
            if len(vip) > 3:
                message += f"#    {'、'.join(vip[3:])}\n"  # 其他
            message += '#####\n'

        # 打印本月榜号和在线表格网站
        print('开始生成本月榜号和在线表格网站')
        top_username_info = top_data.get('top_username')  # 获取本月冲榜用户名
        if top_username_info:
            print(f'榜号信息：{top_username_info}')
            top_username = list(top_username_info.values())
            message += f"\n本月榜号：{'、'.join(top_username)}\n"
        message += f'\n打手升级效率信息详见在线表格：\n{online_doc_url}\n'

    # 判断是否存在排行榜历史数据文件，有就读取历史数据文件，没有则将历史数据设置为一个空字典
    if top_data_file.is_file():
        with open(top_data_file, 'r', encoding='utf-8') as file:
            top_data = json.load(file)
    else:
        top_data = {}
    print(f'历史数据长度：{len(top_data)}')

    # 生成信息内容
    message = f'【菲时报，为您播报】\n北京时间：{ft_date_time}\n'
    current_ft_date_time = ft_date_time
    current_hour = datetime.datetime.now().hour
    # 凌晨0点分钟数小于5时，会有特殊提醒消息，当前的数据应该是前一天的数据
    if datetime.datetime.now().hour == 0 and datetime.datetime.now().minute < 5:
        message += '\n新的一天开始喽，继续加油哦！\n'
        current_ft_date_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%F %T')  # 昨天的日期时间
        current_hour = 24

    # 本月赞助、本月榜号、当前打手名字、打手效率统计的在线表格网站等信息
    info_message()

    # 最新段位排行榜
    new_top_message()

    # 当日段位升级效率统计
    count_stars_message()

    # 历史最高段位排行榜
    history_top_message()

    print(f'新的信息内容已生成：\n{message}')
    return message


def update_excel(doc, url, ocr_top_data):
    """下载在线文档表格，生成本地文档表格，更新在线文档表格"""
    # 下载在线文档表格
    open_url(url)  # 打开在线文档
    download_online_doc()  # 下载在线文档
    # 查找下载的文档
    # 如果循环被 break 终止，说明文件下载成功；如果循环正常执行结束，说明文件下载失败，报错退出
    for i in range(max_retry_count):
        tmp_doc_list = list(downloads_dir.glob(f'菲时报*.xlsx'))
        if tmp_doc_list:
            if len(tmp_doc_list) == 1:
                tmp_doc = tmp_doc_list[0]
            else:
                tmp_doc_list.sort(key=lambda f: os.path.getmtime(f))  # 按文件最后修改时间排序，从旧到新
                tmp_doc = tmp_doc_list[-1]
            shutil.move(tmp_doc, doc)
            time.sleep(1)
            print(f'已将下载的在线文档 {tmp_doc} 移动到当前工作目录 {current_dir}')
            break
        else:
            time.sleep(5)  # 等待文件下载
    else:
        print(f'下载目录 {downloads_dir} 未找到下载的在线文档，文件下载超时，请确认！！！')
        exit(1)

    # 生成本地文档表格
    generate_excel(doc, ocr_top_data)

    # 更新在线文档表格
    open_doc(doc)  # 打开本地文档
    upload_online_doc()  # 更新在线文档

    # 关闭WPS和浏览器应用
    close_program(wps_exe)  # 关闭WPS应用
    close_program(browser_exe)  # 关闭浏览器应用

    # 将生成的本地文档移动到文档存放目录
    doc_file = docs_dir.joinpath(doc)
    shutil.move(doc, doc_file)
    time.sleep(1)
    print(f'已将生成的本地文档 {doc} 移动到文档存放目录 {docs_dir}')


def task():
    """执行任务"""
    # 联系人
    # contact_name = '东升的太阳'
    # contact_name = 'ghost'
    contact_name = '菲时报'

    # 截图名称
    screenshot_image = files_dir.joinpath(f"screenshot_{datetime.datetime.now().strftime('%F_%H-%M-%S')}.png")

    # 本地文档
    doc_file = f"最新菲时报_{datetime.datetime.now().strftime('%F_%H-%M-%S')}.xlsx"

    # 执行任务
    # 查看大赛季段位排行榜
    open_battleofballs()  # 打开球球大作战
    look_top()  # 查看大赛季段位排行榜
    screenshot(screenshot_image)  # 截图大赛季段位排行榜
    watermark(screenshot_image)  # 给截图加水印
    # 裁切图像指定区域，只识别排行榜前三名
    # ocr_box = (90, 180, 1200, 520)  # 排行榜前三名，识别排名、用户名、段位
    # ocr_box = (385, 220, 1200, 520)  # 排行榜前三名，识别用户名、段位
    # ocr_box = (385, 220, 1200, 720)  # 排行榜前五名，识别用户名、段位
    ocr_box = (385, 220, 1200, 900)  # 排行榜前七名，识别用户名、段位
    ocr_result = ocr(screenshot_image, ocr_box)  # OCR 识别
    message_content = generate_message(ocr_result)  # 生成信息内容
    update_top_data(ft_date_time, ocr_result)  # 更新排行榜历史数据文件

    # 微信播报最新段位排行榜
    open_wechat()  # 打开微信
    search_contact(contact_name)  # 搜索联系人
    send_message(message_content, 'text')  # 发送文字消息
    send_message(screenshot_image, 'image')  # 发送图片消息

    # 更新在线文档表格
    update_excel(doc_file, online_doc_url, ocr_result)


def main():
    """主函数"""
    global tmp_start_time, ft_date_time
    # exec_task_time = list(range(0, 60, 20))  # 整点开始，每二十分钟执行一次
    exec_task_time = [0, 30]  # 执行任务的时间分钟，整点、30分执行
    wait_time = 60  # 程序等待时间
    repost_count = 1  # 记录播报次数
    while True:
        date_time = datetime.datetime.now()  # 当前时间
        ft_date_time = date_time.strftime('%F %T')  # 2023-01-17 12:00:00
        tmp_start_time = date_time.timestamp()  # 任务开始执行时间
        date_time_hour = date_time.hour  # 当前时间小时数
        date_time_minute = date_time.minute  # 当前时间分钟数
        date_time_day = date_time.day  # 当前时间天数
        last_month = (date_time.replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m')  # 上个月月份 2023-01

        # 月初第一天0时，切割下历史排行榜文件
        if date_time_day == 1 and date_time_hour == 0 and date_time_minute < 5:
            top_data_file_bak = current_dir.joinpath(top_data_file.name.replace('.', f'-{last_month}.'))
            # 如果不存在上个月的文件，则切割；如果存在，则说明已经切割了
            if not top_data_file_bak.is_file():
                shutil.move(top_data_file, top_data_file_bak)
                print(f'{ft_date_time} 历史排行榜文件已切割完成 {top_data_file_bak}')

        # 月初第一天00:03，更新下历史最高段位排行榜
        if date_time_day == 1 and date_time_hour == 0 and date_time_minute == 3:
            update_history_top()

        # 判断是否到执行任务的时间，是则继续，否则继续等待；第一执行任务时不需要检查时间
        if repost_count != 1:
            # 当月的最后一天
            next_month_first_day = (datetime.date.today().replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
            current_month_first_day = datetime.date.today().replace(day=1)
            current_month_last_day = (next_month_first_day - current_month_first_day).days
            # 月底最后一天23:28，执行下任务，获取下月底数据
            if date_time_day == current_month_last_day and date_time_hour == 23 and date_time_minute == 58:
                print(f"\n{ft_date_time} 月底了，更新下月底数据")
            elif date_time_minute not in exec_task_time:
                time.sleep(wait_time)  # 程序等待
                continue  # 中断当前循环的当次执行，继续下一次循环
        print(f"\n{ft_date_time} 第 {repost_count} 次执行播报")
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
    downloads_dir = current_dir.joinpath('C:/Users/admin/Downloads/')  # 系统下载目录
    docs_dir = current_dir.joinpath('docs')  # 文档文件存放目录
    docs_dir.mkdir(exist_ok=True)  # 如果目录不存在，创建文档文件存放目录

    online_doc_url = 'https://www.kdocs.cn/l/cns5PSA1gu0Z'  # 在线文档网站

    ldmnq_exe = 'dnplayer.exe'  # 雷电模拟器应用程序可执行文件
    wps_exe = 'wps.exe'  # WPS应用程序可执行文件
    browser_exe = 'msedge.exe'  # 浏览器应用程序可执行文件

    max_retry_count = 5  # 最大可重试次数

    main()  # 主函数

    # 程序结束时间
    run_time = int(datetime.datetime.now().timestamp() - start_time)
    print(f'\n共耗时 {run_time} 秒')
    print(f"结束时间：{datetime.datetime.now().strftime('%F %T')}\n")

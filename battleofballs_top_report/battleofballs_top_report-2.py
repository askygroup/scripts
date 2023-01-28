#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

import os
import sys
from pathlib import Path
import datetime
import time
import pyautogui
from PIL import Image, ImageDraw, ImageFont, ImageColor
from wechat import *


def open_battleofballs():
    """打开雷电模拟器，然后再打开球球大作战"""
    # 搜索雷电模拟器应用
    # pyautogui.hotkey('win', 'q')  # 打开"Windows 搜索"菜单
    pyautogui.hotkey('win', 's')  # 打开"Windows 搜索"菜单
    time.sleep(1)
    print(f'搜索雷电模拟器应用')
    write('雷电模拟器')
    ldmnq_image = 'images/ldmnq.png'  # 雷电模拟器应用
    ldmnq_location = pyautogui.locateCenterOnScreen(ldmnq_image, confidence=0.85, minSearchTime=2)
    if ldmnq_location:
        print('打开雷电模拟器')
        pyautogui.moveTo(ldmnq_location, duration=0.5)
        pyautogui.click(clicks=1)
        time.sleep(2)  # 等待雷电模拟器启动

        battleofballs_window_image = 'images/battleofballs_window.png'  # 球球大作战主窗口
        battleofballs_window_location = pyautogui.locateCenterOnScreen(battleofballs_window_image, confidence=0.85, minSearchTime=2)
        if battleofballs_window_location:
            # 打印下球球大作战启动总耗时(球球大作战在后台已启动时，耗时10秒左右，后台未启动时，耗时20秒)
            tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
            print(f'球球大作战已打开，共耗时 {tmp_run_time} 秒')
            pyautogui.press('x', presses=6, interval=0.3)  # 连续点击6次自定义键F，关闭游戏启动后的所有弹窗
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
        print(f'未找到雷电模拟器应用图标 【{ldmnq_image}】')
        exit(1)


def look_top():
    """查看大赛季段位排行榜"""
    # 打开排行榜
    pyautogui.press('t', presses=2)  # 连续快速点击2次，兼容因关闭游戏启动后所有弹窗时，误打开游戏设置而无法打开排行榜的情况
    time.sleep(1)

    competition_season_image = 'images/competition_season-win10.png'  # 大赛季段位排行榜页面
    competition_season_location = pyautogui.locateCenterOnScreen(competition_season_image, confidence=0.85, minSearchTime=2)
    if competition_season_location:
        pyautogui.moveTo(competition_season_location, duration=0.5)
        pyautogui.click(clicks=1)
        print('大赛季页面已打开')
        time.sleep(1)
    else:
        print('大赛季页面未正常打开，继续尝试')
        look_top()  # 随机出现的榜页面未切换到大赛季段位排行榜，需要重新调用 look_top() 函数

    pyautogui.press('f', presses=2)  # 连续快速点击2次自定义键F，查看段位榜，兼容随机出现的榜页面情况
    time.sleep(1)
    pyautogui.press('h', presses=2)  # 连续快速点击2次自定义键H，查看段位分榜，兼容随机出现的榜页面情况
    time.sleep(1)
    level_image = 'images/level.png'  # 大赛季段位排行榜页面
    level_location = pyautogui.locateCenterOnScreen(level_image, confidence=0.85, minSearchTime=2)
    if level_location:
        tmp_run_time = int(datetime.datetime.now().timestamp() - tmp_start_time)
        print(f'大赛季段位排行榜已打开，共耗时 {tmp_run_time} 秒')
        time.sleep(2)
    else:
        print('大赛季段位排行榜未正常打开，继续尝试')
        look_top()  # 随机出现的榜页面未切换到大赛季段位排行榜，需要重新调用 look_top() 函数


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
    font = ImageFont.truetype('typefaces/SmileySans-Oblique.ttf', 50)  # 得意黑
    # 添加水印
    draw = ImageDraw.Draw(im)
    draw.text((870, 35), text, fill=color, font=font)  # 水印左上角坐标为(850, 20)
    # 保存图像
    im.save(image)
    time.sleep(1)
    print(f'截图已加水印并保存到 {image}')


def main():
    """主函数"""
    global tmp_start_time
    # exec_task_time = list(range(0, 60, 20))  # 每二十分钟执行一次
    exec_task_time = [0, 5, 30]  # 执行任务的时间分钟，整点、5分、30分执行
    wait_time = 60  # 程序等待时间
    repost_count = 1  # 记录播报次数
    while True:
        date_time = datetime.datetime.now()  # 当前时间
        ft_date_time = date_time.strftime('%F %T')  # 2023-01-17 12:00:00
        tmp_start_time = date_time.timestamp()  # 任务开始执行时间
        date_time_minute = date_time.minute  # 当前时间分钟数
        date_time_hour = date_time.hour  # 当前时间小时数

        # 联系人
        # contact_name = 'ghost'
        # contact_name = '东升的太阳'
        contact_name = '菲时报'

        # 消息，凌晨0点会有特殊提醒消息
        if date_time_hour == 0 and date_time_minute < 10:
            message_content = f"【菲时报，为您播报】\n北京时间：{ft_date_time}\n新的一天开始喽！\n\n最新段位排行榜："
        else:
            message_content = f"【菲时报，为您播报】\n北京时间：{ft_date_time}\n\n最新段位排行榜："

        # 截图名称
        screenshot_image = files_dir.joinpath(f"screenshot_{date_time.strftime('%F_%H-%M-%S')}.png")

        # 执行任务
        # 第一执行任务不需要检查时间
        if repost_count != 1:
            if date_time_minute not in exec_task_time:
                time.sleep(wait_time)  # 程序等待
                continue  # 中断当前循环的当次执行，继续下一次循环
        # print(f'执行任务的时间已到 {date_time_minute}，开始执行任务')
        print(f"{ft_date_time} 第 {repost_count} 次执行播报")
        open_battleofballs()  # 打开球球大作战
        look_top()  # 查看大赛季段位排行榜
        screenshot(screenshot_image)  # 截图大赛季段位排行榜
        watermark(screenshot_image)  # 给截图加水印

        # 第一执行任务不需要检查时间
        if repost_count != 1:
            # 截图后再检查下当时时间，如果时间未到播报时间，重新执行，兼容执行时间过长，导致播报时间分钟已过的情况，向后兼容一分钟
            if date_time_minute not in exec_task_time and date_time_minute not in [i + 1 for i in exec_task_time]:
                print(date_time_minute, exec_task_time)
                continue  # 中断当前循环的当次执行，继续下一次循环
        open_wechat()  # 打开微信
        search_contact(contact_name)  # 搜索联系人
        send_message(message_content, 'text')  # 发送文字消息
        send_message(screenshot_image, 'image')  # 发送图片消息

        date_time = datetime.datetime.now()  # 当前时间
        date_time_second = date_time.second  # 当前时间秒钟数
        tmp_run_time = int(date_time.timestamp() - tmp_start_time)
        print(f"{date_time.strftime('%F %T')} 第 {repost_count} 次播报完成，共耗时 {tmp_run_time} 秒\n")
        repost_count += 1
        time.sleep(60 - date_time_second)  # 程序等待，确保一分钟内只会播报一次，且下次也能整分钟播报


if __name__ == '__main__':
    # 程序开始时间
    start_time = tmp_start_time = datetime.datetime.now().timestamp()
    print(f"开始时间：{datetime.datetime.now().strftime('%F %T')}\n")

    # 切换到脚本所在目录
    script_dir = sys.path[0]  # 脚本所在目录
    os.chdir(script_dir)  # 切换到脚本所在目录
    current_dir = Path.cwd()  # 当前所在目录
    files_dir = current_dir.joinpath('screenshots')  # 截图文件存放目录
    files_dir.mkdir(exist_ok=True)  # 如果目录不存在，创建截图文件存放目录

    main()

    # 程序结束时间
    run_time = int(datetime.datetime.now().timestamp() - start_time)
    print(f'\n共耗时 {run_time} 秒')
    print(f"结束时间：{datetime.datetime.now().strftime('%F %T')}\n")

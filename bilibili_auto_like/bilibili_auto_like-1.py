#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

import os
import sys
import datetime
import time
import re
import pyautogui
import pyperclip


def write(text):
    """判断文本内容是否有中文字符，有就直接复制粘贴，没有就全是英文字符了，可以模仿键盘一个个输入"""
    chinese_codes = "[\u4e00-\u9fa5]+"  # 中文编码范围
    if re.search(chinese_codes, text):
        pyperclip.copy(text)  # 复制文本到粘贴板
        pyautogui.hotkey('ctrl', 'v')  # 粘贴
        time.sleep(1)
    else:
        english_typewriting_image = 'images/english_typewriting.png'  # 英文输入法
        english_typewriting_location = pyautogui.locateCenterOnScreen(english_typewriting_image, confidence=0.85, minSearchTime=2)
        # print(english_typewriting_location)
        if not english_typewriting_location:
            print('切换为英文输入法')
            pyautogui.press('shift')  # 切换为英文输入法
        pyautogui.write(text, interval=0.1)  # 只能输入英文，且输入法必须是英文状态


def open_url(browser, url):
    """打开网站"""
    if url:
        # 搜索浏览器
        # pyautogui.hotkey('win', 'q')  # 打开"Windows 搜索"菜单
        pyautogui.hotkey('win', 's')  # 打开"Windows 搜索"菜单
        time.sleep(1)
        print(f'搜索浏览器应用 【{browser}】')
        write(browser)  # 输入
        if browser.startswith('microsoft') or browser.startswith('Microsoft'):
            browser_image = 'images/microsoft_edge.png'  # 微软浏览器
        elif browser.startswith('google') or browser.startswith('Google'):
            browser_image = 'images/google_chrome.png'  # 谷歌浏览器
        else:
            print(f'需要手动添加该浏览器【{browser}】', flush=True)
            exit(1)

        browser_location = pyautogui.locateCenterOnScreen(browser_image, confidence=0.85, minSearchTime=2)
        if browser_location:
            print('打开浏览器')
            pyautogui.moveTo(browser_location, duration=0.5)
            pyautogui.click()
            time.sleep(2)  # 等待浏览器启动
            # pyautogui.hotkey('win', 'up')  # 最大化当前窗口，Windows11快捷命令变了，如果有浏览器是全屏打开的，默认新的浏览器窗口就是全屏的，如果再次点击此快捷键会将窗口居上放置，会影响后面的输入
            print('浏览器已打开')
            print(f'输入网址 【{url}】')
            write(url)  # 输入
            pyautogui.press('enter')
            time.sleep(2)
            print(f'网站已打开 【{url}】')
        else:
            print(f'【{browser}】 浏览器打开失败，未找到图标 【{browser_image}】')
            exit(1)
    else:
        print('网站打开失败，网址为空')
        exit(1)


def search_up(up):
    """"搜索UP主"""
    search_box_image = 'images/search_box.png'  # 搜索框
    search_box_location = pyautogui.locateCenterOnScreen(search_box_image, confidence=0.85, minSearchTime=2)
    if search_box_location:
        print(f'搜索UP主 【{up}】')
        pyautogui.moveTo(search_box_location, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        write(up)  # 输入
        pyautogui.press('enter')
    else:
        print(f'未找到搜索框 【{search_box_image}】')
        exit(1)


def open_video(video):
    """搜索并打开需要观看的视频"""
    video_cover_image = f'images/{video}'  # 视频封面
    video_cover_location = pyautogui.locateCenterOnScreen(video_cover_image, confidence=0.85, minSearchTime=2)
    if video_cover_location:
        print(f'打开视频 【{video_cover_image}】')
        pyautogui.moveTo(video_cover_location, duration=0.5)
        pyautogui.click()
        time.sleep(2)  # 等待页面加载
        bullet_screen_box_image = f'images/bullet_screen_box.png'  # 弹幕栏
        bullet_screen_box_location = pyautogui.locateCenterOnScreen(bullet_screen_box_image, confidence=0.85, minSearchTime=2)
        if bullet_screen_box_location:
            time.sleep(1)
            print(f'视频已打开 【{video_cover_image}】')
        else:
            print('尝试打开视频失败，继续查找')
            open_video(video)  # 重新调用 open_video() 函数
    else:
        view_all_manuscripts_image = 'images/view_all_manuscripts.png'  # 查看UP主的所有稿件
        view_all_manuscripts_location = pyautogui.locateCenterOnScreen(view_all_manuscripts_image, confidence=0.85, minSearchTime=2)
        if view_all_manuscripts_location:
            print('查看UP主的全部视频')
            pyautogui.moveTo(view_all_manuscripts_location, duration=0.5)
            pyautogui.click()
            time.sleep(2)
            all_videos_image = 'images/all_videos.png'  # 查看UP主的全部视频
            all_videos_location = pyautogui.locateCenterOnScreen(all_videos_image, confidence=0.85, minSearchTime=2)
            if all_videos_location:
                pyautogui.moveTo(all_videos_location, duration=0.5)
                pyautogui.click()
                pyautogui.scroll(-233)  # 鼠标向下滚动233，查看UP主的视频列表
                open_video(video)  # 重新调用 open_video() 函数
            else:
                print('尝试查看UP主的全部视频失败，继续尝试')
                open_video(video)  # 重新调用 open_video() 函数
        else:
            bottom_of_page_image = 'images/bottom_of_page.png'  # 已滚动到页面底部
            bottom_of_page_location = pyautogui.locateCenterOnScreen(bottom_of_page_image, confidence=0.95, minSearchTime=2)
            if bottom_of_page_location:
                # pyautogui.moveTo(bottom_of_page_location, duration=0.5)
                print('已滚动到页面底部，尝试查看下一页，继续查找')
                next_page_image = 'images/next_page.png'  # 查看下一页
                next_page_location = pyautogui.locateCenterOnScreen(next_page_image, confidence=0.85, minSearchTime=2)
                if next_page_location:
                    pyautogui.moveTo(next_page_location, duration=0.5)
                    pyautogui.click()
                    time.sleep(1)
                    open_video(video)  # 重新调用 open_video() 函数
                else:
                    print('已查看了UP主的全部视频，但是还未找到指定的视频封面 【{video}】')
                    exit(1)
            else:
                print('尝试滚动页面，继续查找')
                pyautogui.scroll(-555)  # 鼠标向下滚动555，尝试继续查找视频封面
                open_video(video)  # 重新调用 open_video() 函数


def send_bullet_screen(bullet_screen):
    """自动发送弹幕"""
    # 输入弹幕
    bullet_screen_box_image = f'images/bullet_screen_box.png'  # 弹幕栏
    bullet_screen_box_location = pyautogui.locateCenterOnScreen(bullet_screen_box_image, confidence=0.85, minSearchTime=2)
    if bullet_screen_box_location:
        print(f'输入弹幕 【{bullet_screen}】')
        pyautogui.moveTo(bullet_screen_box_location, duration=0.5)
        pyautogui.click()
        write(bullet_screen)  # 输入
        print('弹幕输入成功')
    else:
        print('未找到弹幕输入框 【{bullet_screen_box_image}】')
        exit(1)

    # 发送弹幕
    send_bullet_screen_image = 'images/send_bullet_screen.png'
    send_bullet_screen_location = pyautogui.locateCenterOnScreen(send_bullet_screen_image, confidence=0.85, minSearchTime=2)
    if send_bullet_screen_location:
        print(f'发送弹幕 【{bullet_screen}】')
        pyautogui.moveTo(send_bullet_screen_location, duration=0.5)
        pyautogui.click()
        print('弹幕发送成功')
    else:
        print(f'发送弹幕 【{bullet_screen}】')
        pyautogui.press('enter')  # 未找到发布按钮，使用回车键发送
        print('弹幕发送成功')


def send_comment(comment):
    """自动发布评论"""

    # 滚动页面到评论页面
    pyautogui.scroll(-233)  # 鼠标向下滚动233，滚动到评论页面
    time.sleep(1)
    print('滚动页面到评论页面')
    pyautogui.scroll(-666)  # 鼠标向下滚动666，模仿真人习惯滚动鼠标
    time.sleep(1)

    # 输入评论
    comment_box_image = f'images/comment_box.png'  # 评论框
    comment_box_location = pyautogui.locateCenterOnScreen(comment_box_image, confidence=0.85, minSearchTime=2)
    if comment_box_location:
        print(f'输入评论 【{comment}】')
        pyautogui.moveTo(comment_box_location, duration=0.5)
        pyautogui.click()
        write(comment)  # 输入
        print('评论输入成功')
    else:
        print('未找到评论输入框 【{comment_box_image}】')
        exit(1)

    # 发布评论
    send_comment_image = 'images/send_comment.png'
    send_comment_location = pyautogui.locateCenterOnScreen(send_comment_image, confidence=0.85, minSearchTime=2)
    if send_comment_location:
        print(f'发布评论 【{comment}】')
        pyautogui.moveTo(send_comment_location, duration=0.5)
        pyautogui.click()
        print('评论发布成功')
    else:
        print(f'发布评论 【{comment}】')
        pyautogui.press('enter')  # 未找到发布按钮，使用回车键发布
        print('评论发布成功')

    # 评论按最新排序
    newest_comment_image = f'images/newest_comment.png'
    newest_comment_location = pyautogui.locateCenterOnScreen(newest_comment_image, confidence=0.85, minSearchTime=2)
    if newest_comment_location:
        print('评论按最新排序')
        pyautogui.moveTo(newest_comment_location, duration=0.5)
        pyautogui.click()
        time.sleep(2)
    else:
        print('INFO: 尝试按最新排序失败，未找到图标 【{newest_comment_image}】，使用默认的最热排序')


def like():
    """自动点赞"""
    # 点赞后再次打开同一个视频后，可能会导致点赞无效的情况，点赞数有，但还可以继续点赞(B站数据同步机制原因)
    global like_count, mouse_location_cache

    # 给评论点赞
    like_image = f'images/like.png'  # 点赞按钮
    like_location = pyautogui.locateCenterOnScreen(like_image, confidence=0.95, minSearchTime=1)
    # print(like_location, mouse_location_cache)
    if like_location and like_location[1] != mouse_location_cache[1]:
        pyautogui.moveTo(like_location, duration=0.5)
        pyautogui.click()
        like_count += 1
        print(f'已点赞 {like_count} 次')
        mouse_location_cache = like_location
        print(mouse_location_cache)
        like()  # 重新调用 like() 函数
    else:
        bottom_of_page_image = 'images/bottom_of_page.png'  # 已滚动到页面底部
        bottom_of_page_location = pyautogui.locateCenterOnScreen(bottom_of_page_image, confidence=0.95, minSearchTime=1)
        if bottom_of_page_location:
            print('已滚动到页面底部，自动点赞完成')
        else:
            pyautogui.scroll(-555)  # 鼠标向下滚动555
            time.sleep(0.5)  # 暂停0.5s，避免出现滚动屏幕后，搜索到的按钮位置发生偏移(屏幕刷新率原因)
            like()  # 重新调用 like() 函数


def main():
    """主函数"""
    # 浏览器
    web_browser = 'Microsoft Edge'  # 浏览器
    # web_browser = 'Google Chrome'  # 浏览器
    web_url = 'https://www.bilibili.com/'  # B站网址

    # UP主网名
    uploader = '我就是星月'  # UP主网名
    # uploader = '东升的太阳'  # UP主网名

    # 需要打开的视频封面
    # video_cover = 'video_cover.png'  # 视频封面
    # video_cover = 'zoo_video_cover.png'  # 小矛动物园
    video_cover = 'video_cover-1.png'  # 特级教师口吻征婚
    # video_cover = 'video_cover-2.png'  # 征婚视频社死现场
    # video_cover = 'video_cover-3.png'  # 社死现场后续
    # video_cover = 'video_cover-11.png'  # 985的废物
    # video_cover = 'video_cover-12.png'  # 自卑抑郁的文科状元

    # 弹幕
    bullet_screen_content = '一键三连！'

    # 评论
    # comment_content = '你眼里有宇宙，胜过我见过的所有山川河流。'
    # comment_content = '此视频已经被我盯上了，你敢评论，我就敢点赞[doge]'
    # comment_content = 'B站的算法工程师呀，咱们能不能不要这么智能，不要推的这么精准好不好？'
    # comment_content = '你就这么寂寞吗 [doge]'
    # comment_content = '助力每一个梦想(社死bushi)[doge]'
    comment_content = '嘿~嘿！'

    open_url(web_browser, web_url)  # 打开B站
    search_up(uploader)  # 搜索UP主，打开要观看的视频
    open_video(video_cover)  # 打开需要观看的视频
    send_bullet_screen(bullet_screen_content)  # 自动发送弹幕
    send_comment(comment_content)  # 自动发布评论
    like()  # 自动点赞


if __name__ == '__main__':
    # 程序开始时间
    start_time = datetime.datetime.now().timestamp()
    print(f"开始时间：{datetime.datetime.today().strftime('%F %T')}")

    # 切换到脚本所在目录
    script_dir = sys.path[0]  # 脚本所在目录
    os.chdir(script_dir)  # 切换到脚本所在目录

    sys.setrecursionlimit(2000)  # 设置解释器的递归调用深度限制
    print(f'递归限制已调整为：{sys.getrecursionlimit()}\n')

    # 点赞次数和鼠标光标位置
    like_count = 0
    mouse_location_cache = (0, 0)  # 增加纪录鼠标当前光标位置，防止出现部分点赞按钮在页面底部无法点击的问题

    main()

    # 程序结束时间
    run_time = int(datetime.datetime.now().timestamp() - start_time)
    print(f'\n共耗时 {run_time} 秒', flush=True)
    print(f"结束时间：{datetime.datetime.today().strftime('%F %T')}\n")

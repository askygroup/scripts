#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

import os
import sys
import datetime
import time
import re
import pyautogui
import pyperclip


def center_lower(coords):
    # 计算中下部的坐标
    return coords[0] + int(coords[2] / 2), coords[1] + coords[3]


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


def open_wechat():
    """打开微信"""
    wechat_window_image = 'images/wechat_window.png'  # 微信窗口
    wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)  # 降低匹配精度，兼容小的窗口，最多等待2秒
    if wechat_window_location:
        print('微信已打开')
    else:
        # pyautogui.hotkey('win', 'q')  # 打开"Windows 搜索"菜单
        pyautogui.hotkey('win', 's')  # 打开"Windows 搜索"菜单
        # 搜索微信应用
        print(f'搜索微信应用')
        # write('微信')
        write('wechat')
        wechat_image = 'images/wechat.png'  # 微信应用
        wechat_location = pyautogui.locateCenterOnScreen(wechat_image, confidence=0.85, minSearchTime=2)
        if wechat_location:
            print('打开微信')
            pyautogui.moveTo(wechat_location, duration=0.5)
            pyautogui.click(clicks=2)
            wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)
            if wechat_window_location:
                # pyautogui.hotkey('alt', 'space', 'x')  # 最大化当前窗口，快捷键方式不太好用
                pyautogui.hotkey('win', 'up')  # 最大化当前窗口，Windows11快捷命令变了，如果有浏览器是全屏打开的，默认新的浏览器窗口就是全屏的，如果再次点击此快捷键会将窗口居上放置，会影响后面的输入
                time.sleep(1)
                print('微信已打开')
            else:
                # 扫码登录
                scan_code_login_image = 'images/scan_code_login.png'  # 扫码登录微信
                scan_code_login_location = pyautogui.locateCenterOnScreen(scan_code_login_image, confidence=0.85, minSearchTime=2)
                if scan_code_login_location:
                    print('请用手机扫码登录微信')
                    for i in range(20):
                        time.sleep(1)
                        wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)
                        if wechat_window_location:
                            print('微信已打开')
                            break
                        elif i >= 20:
                            print('微信扫码登录打开失败')
                            exit(1)
                else:
                    # 确定登录
                    enter_wechat_image = 'images/enter_wechat.png'  # 确定进入微信
                    enter_wechat_location = pyautogui.locateCenterOnScreen(enter_wechat_image, confidence=0.85, minSearchTime=2)
                    if enter_wechat_location:
                        pyautogui.moveTo(enter_wechat_location, duration=0.5)
                        pyautogui.click()
                        for i in range(20):
                            time.sleep(1)
                            wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)
                            if wechat_window_location:
                                print('微信已打开')
                                break
                            elif i >= 20:
                                print('进入微信打开失败')
                                exit(1)
                    else:
                        print('微信打开失败')
                        exit(1)
        else:
            print(f'桌面上未找到微信应用图标 【{wechat_desktop_shortcut_image}】')
            exit(1)


def search_contact(contact):
    """搜索联系人"""
    search_box_image = 'images/search_box.png'  # 搜索框
    search_box_location = pyautogui.locateCenterOnScreen(search_box_image, confidence=0.85, minSearchTime=2)
    if search_box_location:
        print(f'搜索联系人 【{contact}】')
        pyautogui.moveTo(search_box_location, duration=0.5)
        pyautogui.click()
        write(contact)  # 输入
    else:
        chat_image = 'images/chat.png'  # 聊天页
        chat_location = pyautogui.locateCenterOnScreen(chat_image, confidence=0.85, minSearchTime=2)
        if chat_location:
            print('切换到聊天页')
            pyautogui.moveTo(chat_location, duration=0.5)
            pyautogui.click()
            chat_on_image = 'images/chat_on.png'  # 当前页为聊天页
            chat_on_location = pyautogui.locateCenterOnScreen(chat_on_image, confidence=0.85, minSearchTime=2)
            if chat_on_location:
                search_contact(contact)  # 重新调用 search_contact() 函数
            else:
                print(f'当前页未切换到聊天页 【{chat_on_image}】')
                exit(1)
        else:
            print(f'未找到聊天页图标 【{chat_image}】')
            exit(1)

    # 选择搜索到的第一个联系人
    first_search_contact_image = 'images/first_search_contact.png'  # 搜索到的第一个联系人
    first_search_contact_coords = pyautogui.locateOnScreen(first_search_contact_image, confidence=0.85, minSearchTime=2)
    if first_search_contact_coords:
        first_search_contact_location = center_lower(first_search_contact_coords)  # 计算中下部的坐标
        pyautogui.moveTo(first_search_contact_location, duration=0.5)
        pyautogui.click()
        print(f'已找到联系人 【{contact}】')
    else:
        print(f'未找到微信好友 【{contact}】')
        exit(1)


def new_message():
    """查看新消息"""
    chat_new_message_on_image = 'images/chat_new_message_on.png'  # 当前聊天页新消息
    chat_new_message_on_location = pyautogui.locateCenterOnScreen(chat_new_message_on_image, confidence=0.85, minSearchTime=2)
    if chat_new_message_on_location:
        pyautogui.moveTo(chat_new_message_on_location, duration=0.5)
        pyautogui.click(clicks=2)
        new_message_image = 'images/new_message.png'  # 新消息
        new_message_location = pyautogui.locateCenterOnScreen(new_message_image, confidence=0.8, minSearchTime=2)
        if new_message_location:
            print('查看新消息')
            pyautogui.moveTo(new_message_location, duration=0.3)
            pyautogui.click()
            return True  # 返回真
        else:
            print('没有新的消息')
    else:
        chat_new_message_image = 'images/chat_new_message.png'  # 聊天页新消息
        chat_new_message_location = pyautogui.locateCenterOnScreen(chat_new_message_image, confidence=0.85, minSearchTime=2)
        if chat_new_message_location:
            print('切换到聊天页新消息')
            pyautogui.moveTo(chat_new_message_location, duration=0.5)
            pyautogui.click()
            chat_new_message_on_image = 'images/chat_new_message_on.png'  # 当前页为聊天页
            chat_new_message_on_location = pyautogui.locateCenterOnScreen(chat_new_message_on_image, confidence=0.85, minSearchTime=2)
            if chat_new_message_on_location:
                new_message()  # 重新调用 new_message() 函数
            else:
                print('当前页未切换成聊天页新消息')
                exit(1)
        else:
            print('没有新的消息')


def send_message(message):
    """发送消息"""
    # 输入消息
    input_message_box_null_image = 'images/input_message_box_null.png'  # 消息输入框
    input_message_box_null_location = pyautogui.locateCenterOnScreen(input_message_box_null_image, confidence=0.85, minSearchTime=2)
    if input_message_box_null_location:
        print(f'输入消息 【{message}】')
        pyautogui.moveTo(input_message_box_null_location, duration=0.5)
        pyautogui.click()
        write(message)  # 输入
        print('消息输入成功')
    else:
        input_message_box_image = 'images/input_message_box.png'  # 消息输入框非空
        input_message_box_coords = pyautogui.locateOnScreen(input_message_box_image, confidence=0.85, minSearchTime=2)
        if input_message_box_coords:
            input_message_box_location = center_lower(input_message_box_coords)  # 计算中下部的坐标
            pyautogui.moveTo(input_message_box_location, duration=0.5)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')  # 全选
            pyautogui.press('backspace')  # 删除
            send_message(message)  # 重新调用 send_message() 函数
        else:
            print('未找到消息输入框')
            exit(1)

    # 发送消息
    send_message_image = 'images/send_message.png'  # 消息发送
    send_message_location = pyautogui.locateCenterOnScreen(send_message_image, confidence=0.85, minSearchTime=2)
    if send_message_location:
        print(f'发送消息 【{message}】')
        pyautogui.moveTo(send_message_location, duration=0.5)
        pyautogui.click()
        print('消息发送成功')
    else:
        print(f'发送消息 【{message}】')
        pyautogui.press('enter')  # 未找到消息发送按钮，使用回车键发送
        print('消息发送成功')


def auto_send(contact, message):
    """自动给微信好友发送消息"""
    if contact:
        search_contact(contact)  # 搜索联系人
        send_message(message)  # 发送消息
    else:
        print('自动给微信好友发送消息失败，好友为空')
        exit(1)


def auto_reply(message):
    """自动回复微信消息"""
    def reply(_message, n=1):
        nonlocal reply_count
        print(f"{datetime.datetime.today().strftime('%F %T')} 第 {n} 次执行自动回复，已自动回复 {reply_count} 次")
        # 打开微信
        open_wechat()
        # 查看新消息
        result = new_message()
        # 如果有新消息，自动回复新消息，如果一个人第二次发送消息，不会自动回复(因为当前对话框自动已读了)
        if result:
            send_message(_message)
            reply_count += 1

    # 执行自动回复
    count, reply_count = 1, 0
    while True:
        reply(message, count)
        count += 1
        time.sleep(10)


def main():
    """主函数"""
    # 联系人
    # contact_name = 'ghost'
    contact_name = '东升的太阳'
    # contact_name = '诺'

    # 消息
    # message_content = '你好'
    # message_content = 'Hello'
    # message_content = '早上好'
    # message_content = '收到'
    # message_content = '您好，主人已开启睡觉模式，晚安喽，明天见！'
    message_content = '【您好，我现在有事不在，一会再和您联系。】'
    # message_content = '哈哈哈'

    open_wechat()  # 打开微信
    # auto_send(contact_name, message_content)  # 自动给微信好友发送消息
    auto_reply(message_content)  # 自动回复微信消息


if __name__ == '__main__':
    # 程序开始时间
    start_time = datetime.datetime.now().timestamp()
    print(f"开始时间：{datetime.datetime.today().strftime('%F %T')}")

    # 切换到脚本所在目录
    script_dir = sys.path[0]  # 脚本所在目录
    os.chdir(script_dir)  # 切换到脚本所在目录

    sys.setrecursionlimit(2000)  # 设置解释器的递归调用深度限制
    print(f'递归限制已调整为：{sys.getrecursionlimit()}\n')

    main()

    # 程序结束时间
    run_time = int(datetime.datetime.now().timestamp() - start_time)
    print(f'\n共耗时 {run_time} 秒')
    print(f"结束时间：{datetime.datetime.today().strftime('%F %T')}\n")

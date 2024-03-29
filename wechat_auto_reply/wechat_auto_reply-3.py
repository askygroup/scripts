#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import os
import sys
import datetime
import time
import re
import pyautogui
import pyperclip
from PIL import Image
import io
import win32clipboard


def center_lower(coords):
    """计算中下部的坐标"""
    return coords[0] + int(coords[2] / 2), coords[1] + coords[3]


def copy_image_to_clipboard(image):
    """将图片文件复制到系统剪贴板"""
    # 将图片转存为位图格式的二进制字符串
    with Image.open(image) as image_file:  # 图像对象的模式是 RGB
        image_bytes = io.BytesIO()  # 使用 BytesIO 字节对象存储图片转换之后的二进制字符串
        image_file.save(image_bytes, 'BMP')  # 使用 BMP(Bitmap) 位图格式存储到 BytesIO 字节对象
        image_data = image_bytes.getvalue()[14:]  # BMP 格式的图片有14个字节的header，需要去除
        image_bytes.close()  # 关闭 BytesIO 字节对象

    # 将位图格式的图片写入到系统剪贴板
    win32clipboard.OpenClipboard()  # 打开剪贴板
    win32clipboard.EmptyClipboard()  # 清空剪贴板，清空后新的数据才好写入
    # 设置好剪贴板的数据格式，再传入对应格式的数据，才能正确向剪贴板写入数据
    # unicode 字符通常是传入 win32con.CF_UNICODETEXT
    # win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, image)  # 将数据写入到剪切板
    # print(win32clipboard.GetClipboardData())  # 获取剪切板内容
    # print(win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT))   # 获取剪切板中 CF_DIB 格式的内容

    # BMP 位图格式的图片也会以.DIB和RLE作为文件扩展名，DIB(device-independent bitmap) 设备无关位图，需要传入 win32clipboard.CF_DIB
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, image_data)  # 将数据写入到剪切板
    # print(win32clipboard.GetClipboardData(win32clipboard.CF_DIB))   # 获取剪切板中 CF_DIB 格式的内容
    print(f'已将图片复制到剪贴板 {image}')
    win32clipboard.CloseClipboard()  # 关闭剪贴板
    time.sleep(1)


def write(data, data_type='text'):
    """将数据输入到输入框"""
    if data_type == 'text':
        # 判断文本内容是否有中文字符，有就直接复制粘贴，没有就全是英文字符了，可以模仿键盘一个个输入
        chinese_codes = "[\u4e00-\u9fa5]+"  # 中文编码范围
        if re.search(chinese_codes, data):
            print('输入中文文本')
            pyperclip.copy(data)  # 复制文本到粘贴板
            pyautogui.hotkey('ctrl', 'v')  # 粘贴
            time.sleep(1)
        else:
            print('输入英文文本')
            english_typewriting_image = 'images/english_typewriting.png'  # 英文输入法
            english_typewriting_location = pyautogui.locateCenterOnScreen(english_typewriting_image, confidence=0.85, minSearchTime=2)
            # print(english_typewriting_location)
            if not english_typewriting_location:
                print('切换为英文输入法')
                pyautogui.press('shift')  # 切换为英文输入法
            pyautogui.write(data, interval=0.1)  # 只能输入英文，且输入法必须是英文状态
    elif data_type == 'image':
        print('输入图片')
        copy_image_to_clipboard(data)  # 将截图复制到系统剪切板
        # pyautogui.hotkey('win', 'v')  # 打开系统剪贴板
        # time.sleep(1)
        # pyautogui.press('down', presses=2, interval=0.3)  # 连续点击2次，选择第三条粘贴(第一条是刚发的文本信息，第二条是联系人名称)
        # pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')  # 粘贴
        time.sleep(1)
    else:
        print(f'需要输入的数据类型 【{msg_type}】 暂不支持')
        exit(1)


def open_wechat():
    """打开微信"""
    # 搜索微信应用
    # pyautogui.hotkey('win', 'q')  # 打开"Windows 搜索"菜单
    pyautogui.hotkey('win', 's')  # 打开"Windows 搜索"菜单
    time.sleep(0.5)
    print(f'搜索微信应用')
    # write('wechat')
    write('微信')
    time.sleep(0.5)
    wechat_image = 'images/wechat.png'  # 微信应用
    wechat_location = pyautogui.locateCenterOnScreen(wechat_image, confidence=0.85, minSearchTime=2)
    if wechat_location:
        print('打开微信')
        pyautogui.moveTo(wechat_location, duration=0.5)
        pyautogui.click()
        time.sleep(2)  # 等待微信启动

        wechat_window_image = 'images/wechat_window.png'  # 微信窗口
        wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)
        if wechat_window_location:
            # 最大化当前窗口
            # Windows11快捷命令变了，如果应用已经是全屏打开的，再次点击此快捷键会将窗口居上放置，会影响后面的输入
            pyautogui.hotkey('win', 'up')
            time.sleep(0.5)
            pyautogui.hotkey('win', 'down')  # 兼容窗口居上放置，而不是全屏的情况
            time.sleep(0.5)
            pyautogui.hotkey('win', 'up')
            time.sleep(0.5)
            print('微信已打开')
        else:
            scan_code_login_image = 'images/scan_code_login.png'  # 扫码登录微信
            scan_code_login_location = pyautogui.locateCenterOnScreen(scan_code_login_image, confidence=0.85, minSearchTime=2)
            enter_wechat_image = 'images/enter_wechat.png'  # 确定进入微信
            enter_wechat_location = pyautogui.locateCenterOnScreen(enter_wechat_image, confidence=0.85, minSearchTime=2)
            # 扫码登录
            if scan_code_login_location:
                print('请用手机扫码登录微信')
                for i in range(20):
                    time.sleep(1)
                    wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)
                    if wechat_window_location:
                        print('微信已打开')
                        break
                    elif i >= 20:
                        print('微信扫码登录打开失败，扫码登录超时')
                        exit(1)
            # 确定登录
            elif enter_wechat_location:
                pyautogui.moveTo(enter_wechat_location, duration=0.5)
                pyautogui.click()
                for i in range(20):
                    time.sleep(1)
                    wechat_window_location = pyautogui.locateCenterOnScreen(wechat_window_image, confidence=0.85, minSearchTime=2)
                    if wechat_window_location:
                        print('微信已打开')
                        break
                    elif i >= 20:
                        print('进入微信打开失败，进入微信超时')
                        exit(1)
            else:
                print('未找到微信扫码登录或确认登录窗口，继续尝试')
                open_wechat()  # 需要重新调用 open_wechat() 函数
    else:
        print('未找到微信应用图标，继续尝试')
        open_wechat()  # 需要重新调用 open_wechat() 函数


def search_contact(contact):
    """搜索联系人"""
    search_box_image = 'images/search_box.png'  # 搜索框
    search_box_location = pyautogui.locateCenterOnScreen(search_box_image, confidence=0.85, minSearchTime=2)
    if search_box_location:
        print(f'搜索联系人 【{contact}】')
        pyautogui.moveTo(search_box_location, duration=0.5)
        pyautogui.click()
        write(contact)  # 输入
        time.sleep(1)
        pyautogui.press('enter')  # 点击回车键，选择搜索到的第一个联系人
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


def send_message(message, msg_type='text'):
    """发送消息"""
    input_message_box_null_image = 'images/input_message_box_null.png'  # 消息输入框
    input_message_box_null_location = pyautogui.locateCenterOnScreen(input_message_box_null_image, confidence=0.85, minSearchTime=2)
    if input_message_box_null_location:
        # 如果消息类型为 text、image，调用 write() 函数输入消息；如果是其他类型则报错退出
        if msg_type == 'text' or msg_type == 'image':
            print(f'输入消息 【{message}】')
            pyautogui.moveTo(input_message_box_null_location, duration=0.5)
            pyautogui.click()
            write(message, msg_type)  # 输入
            print('消息输入成功')

            print(f'发送消息 【{message}】')
            pyautogui.press('enter')  # 使用回车键发送消息
            print('消息发送成功')

        else:
            print(f'需要发送的消息类型 【{msg_type}】 暂不支持')
            exit(1)
    else:
        input_message_box_image = 'images/input_message_box.png'  # 消息输入框非空
        input_message_box_coords = pyautogui.locateOnScreen(input_message_box_image, confidence=0.85, minSearchTime=2)
        if input_message_box_coords:
            input_message_box_location = center_lower(input_message_box_coords)  # 计算中下部的坐标
            pyautogui.moveTo(input_message_box_location, duration=0.5)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')  # 全选
            pyautogui.press('backspace')  # 删除
            send_message(message, msg_type)  # 重新调用 send_message() 函数
        else:
            print('未找到消息输入框')
            exit(1)


def auto_send(contact, message, msg_type='text'):
    """自动给微信好友发送消息"""
    if contact:
        search_contact(contact)  # 搜索联系人
        send_message(message, msg_type)  # 发送消息
    else:
        print('自动给微信好友发送消息失败，好友为空')
        exit(1)


def auto_reply(message, msg_type='text'):
    """自动回复微信消息"""
    def reply(_message, _msg_type='text', n=1):
        nonlocal reply_count
        print(f"{datetime.datetime.today().strftime('%F %T')} 第 {n} 次执行自动回复，已自动回复 {reply_count} 次")
        # 打开微信
        open_wechat()
        # 查看新消息
        result = new_message()
        # 如果有新消息，自动回复新消息，如果一个人第二次发送消息，不会自动回复(因为当前对话框自动已读了)
        if result:
            send_message(_message, _msg_type)
            reply_count += 1

    # 执行自动回复
    count, reply_count = 1, 0
    while True:
        reply(message, msg_type, count)
        count += 1
        time.sleep(10)


def main():
    """主函数"""
    # 联系人
    # contact_name = 'ghost'
    contact_name = '东升的太阳'
    # contact_name = '诺'

    # 文字消息
    # message_content = '你好'
    # message_content = 'Hello'
    # message_content = '早上好'
    # message_content = '收到'
    # message_content = '您好，主人已开启睡觉模式，晚安喽，明天见！'
    # message_content = '【您好，我现在有事不在，一会再和您联系。】'
    # message_content = '哈哈哈'

    # 图片消息
    message_content = 'images/asky.png'

    open_wechat()  # 打开微信
    # auto_send(contact_name, message_content, 'text')  # 自动给微信好友发送文字消息
    # auto_send(contact_name, message_content, 'image')  # 自动给微信好友发送图片消息
    # auto_reply(message_content, 'text')  # 自动回复微信消息，回复文字消息
    auto_reply(message_content, 'image')  # 自动回复微信消息，回复图片消息


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

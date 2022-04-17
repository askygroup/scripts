#!/usr/bin/env python3
# _*_ coding: UTF-8 _*_

from tkinter import *

# 创建一个窗口
window = Tk()
window.title("测试")
window.geometry(f'{300}x{150}+{500}+{100}')

# 创建标签、输入框组件，并将窗口组件放置到主窗口中
Label(window, text="用户名：").grid(row=0, column=0)
Label(window, text="密码：").grid(row=1, column=0)
window_ex1 = Entry(window)
window_ex2 = Entry(window, show='*')
window_ex1.grid(row=0, column=1, padx=10, pady=5)
window_ex2.grid(row=1, column=1, padx=10, pady=5)
# 创建按钮组件，并将窗口组件放置到主窗口中


def get_info():
	print(f"用户名：{window_ex1.get()}")
	print(f"密码：{window_ex2.get()}")
	window_ex1.delete(0, END)
	window_ex2.delete(0, END)


Button(window, text="获取信息", width=10, cursor='hand2', command=get_info).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(window, text="退出", width=10, cursor='hand2', command=window.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

# 进入窗口消息循环
window.mainloop()
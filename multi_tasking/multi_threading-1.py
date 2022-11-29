#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 多线程并发执行，使用 threading 模块，全量并发（并行）

import datetime
import random
import time
import threading


def action(n):
	print(n)
	# time.sleep(random.choice(range(5)))  # 线程随机暂停几秒
	time.sleep(1)  # 线程暂停一秒


def task():
	task_num = 10  # 总任务数

	threads = []  # # 线程池
	for i in range(task_num):
		# 将子任务添加到线程池中
		threads.append(threading.Thread(target=action, args=(i,)))

	# 执行线程池中的线程
	for thread in threads:
		thread.start()
	# 阻塞主线程，等待所有子线程运行完毕后，再退出主线程
	for thread in threads:
		thread.join()


if __name__ == '__main__':
	# 程序开始时间
	start_time = datetime.datetime.now().timestamp()
	print(datetime.datetime.today().strftime("%F %T"), flush=True)

	# 多线程
	task()

	# 程序结束时间
	run_time = int(datetime.datetime.now().timestamp() - start_time)
	print(f'The program takes {run_time}s', flush=True)
	print(datetime.datetime.today().strftime("%F %T"), flush=True)

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 多线程并发执行，使用 threading 模块，使用信号量控制并发数，并发数可控（并行可控）

import datetime
import random
import time
import threading


def action(n):
	global thread_pool  # 全局变量

	# 方式一：
	# thread_pool.acquire()  # 加锁，限制线程数
	# print(n)
	# time.sleep(1)  # 线程暂停一秒
	# thread_pool.release()  # 解锁，释放线程数

	# 方式二：
	with thread_pool:
		print(n)
		# time.sleep(random.choice(range(5)))  # 线程随机暂停几秒
		time.sleep(1)  # 线程暂停一秒


def task():
	task_num = 10  # 总任务数

	threads = []  # # 线程池
	for t in range(task_num):
		# 将子任务添加到线程池中
		threads.append(threading.Thread(target=action, args=(t,)))

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

	max_threads = 3  # 最大线程数
	# thread_pool = threading.Semaphore(max_threads)  # 线程数池
	thread_pool = threading.BoundedSemaphore(max_threads)  # 线程数池
	# 多线程
	task()

	# 程序结束时间
	run_time = int(datetime.datetime.now().timestamp() - start_time)
	print(f'The program takes {run_time}s', flush=True)
	print(datetime.datetime.today().strftime("%F %T"), flush=True)

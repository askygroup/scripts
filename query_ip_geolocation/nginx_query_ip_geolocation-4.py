#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 读取 nginx 来源IP地址，查询IP属地信息

import datetime
import os
import sys
from pathlib import Path
import shutil
import requests
import json
import threading
import math


def ipinfo_api(ip):
	# ip信息 API https://ip.useragentinfo.com/json?ip=125.119.233.10
	url = f"https://ip.useragentinfo.com/json?ip={ip}"
	# 调用API
	# 异常情况重试，重试三次还失败，退出函数返回None
	try_time = 3  # 最大重试次数
	try:
		response = requests.get(url, timeout=3)
		result_code = response.status_code
		result_info = response.json()
		if result_code == 200:
			# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
			# 所在地理位置："中国 浙江省 杭州市 西湖区 电信"
			ip_geolocation = f"{result_info['country']} {result_info['province']} {result_info['city']} {result_info['area']} {result_info['isp']}"
			return ip_geolocation
		else:
			print(f"请求失败！返回码【{result_code}】")
	except:
		if try_time:
			ipinfo_api(ip)  # 异常后继续重试
			try_time -= 1


def query(ip, full_ip, result):
	with thread_pool:
		# 通过 API 查询IP属地信息
		ip_info = ipinfo_api(ip)
		if ip_info:
			result.append(f"{full_ip}|{ip_info}\n")
		else:
			result.append(f"{full_ip}|未查询到属地信息\n")


def task():
	# 查询IP属地
	# 判断 ip_list 是否指定，没有指定抛异常并退出
	if ip_list:
		ip_list_file = current_dir.joinpath(ip_list)
	else:
		raise ValueError(f"ERROR：The ip_list file to be queried is not specified !!!\n")
	# 判断 ip_list 文件是否存在，不存在抛异常并退出
	if not ip_list_file.is_file():
		raise ValueError(f"ERROR: The {ip_list_file} does not exist !!!\n")

	# 读取所有IP的地理位置信息 json 文件，文件存在则读取成字典，不存在则为空字典
	json_file = current_dir.joinpath(all_ip_geolocation)
	if json_file.is_file():
		with open(json_file, 'r', encoding='utf-8') as file:
			all_ip_geolocation_dict = json.load(file)
	else:
		all_ip_geolocation_dict = {}

	tasks = []  # 任务列表
	threads = []  # 待执行的线程池
	result = []  # 查询结果

	# 读取需要查询的IP地址列表文件，将查询到的信息写入结果文件中
	with open(ip_list_file, 'r', encoding='utf-8') as ip_file, open(result_file, 'w', encoding='utf-8') as file:
		for full_ip in ip_file.readlines():
			full_ip = full_ip.strip()  # 去掉首位空白字符(换行符)
			ip = full_ip.split("|")[1]
			# print(ip)
			if all_ip_geolocation_dict.get(ip) and all_ip_geolocation_dict.get(ip) != "未查询到属地信息":
				ip_info = all_ip_geolocation_dict[ip]
				file.write(f"{full_ip}|{ip_info}\n")
			else:
				tasks.append(full_ip)

		# Linux 系统设置有最大线程池，任务需要分批加入线程池
		sys_max_thread_pool = 3000  # 系统最大线程池
		time = math.ceil(len(tasks) / sys_max_thread_pool)  # 切片次数
		start = 0  # 切片起始索引
		for i in range(time):
			end = start + sys_max_thread_pool
			tmp_tasks = tasks[start:end]
			# print(tmp_tasks)
			start = end  # 更新切片起始索引
			for full_ip in tmp_tasks:
				full_ip = full_ip.strip()
				ip = full_ip.split("|")[1]
				# print(ip)
				# 将子任务添加到待执行的线程池中
				threads.append(threading.Thread(target=query, args=(ip, full_ip, result)))
			# 执行线程池中的线程
			for thread in threads:
				thread.start()
			# 阻塞主线程，等待所有子线程运行完毕后，再退出主线程
			for thread in threads:
				thread.join()
			threads.clear()  # 清空线程池

		# 将查询后的数据写入到结果文件中
		file.writelines(result)

	# 过滤出境外IP的top30
	overseas_ip = []
	with open(overseas_file, 'a', encoding='utf-8') as data_file, open(result_file, 'r', encoding='utf-8') as file:
		for info in file.readlines():
			if "中国" in info or "本地局域网" in info:
				pass
			else:
				overseas_ip.append(info)
		overseas_ip.sort(key=lambda item: int(item.split('|')[0]), reverse=True)  # 按第一列的数字大小进行排序
		data_file.write(f"##### {ip_list}\n")
		data_file.writelines(overseas_ip[:30])

	# 更新所有IP的地理位置信息 json 文件
	for info in result:
		full_info = info.strip().split("|")
		# print(full_info)
		all_ip_geolocation_dict[full_info[1]] = full_info[-1]
	# 将IP的地理位置信息写入缓存文件中
	with open(json_file, 'w', encoding='utf-8') as file:
		file.write(json.dumps(all_ip_geolocation_dict, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
	# 程序开始时间
	start_time = datetime.datetime.now().timestamp()
	print(datetime.datetime.today().strftime("%F %T"), flush=True)
	today = datetime.datetime.today().strftime("%Y%m%d")
	# 切换到脚本所在目录
	script_dir = sys.path[0]  # 脚本所在目录
	os.chdir(script_dir)  # 切换到脚本所在目录
	current_dir = Path.cwd()  # 当前所在目录
	files_dir = current_dir.joinpath('files')  # 文件存放目录
	files_dir.mkdir(exist_ok=True)  # 如果目录不存在，创建文件存放目录

	# 配置文件
	all_ip_geolocation = "all_ip.json"  # 所有IP的地理位置信息（IP属地）
	# ip_list = "test_ip.list"  # 需要查询的IP列表
	# result_data = "test_ip.txt"  # 查询结果数据
	ip_list = sys.argv[1] if len(sys.argv) > 1 else ''  # 执行脚本时的第一参数是需要查询的IP列表
	result_data = ip_list.replace('.list', '.txt')  # 查询结果数据
	result_file = current_dir.joinpath(result_data)  # result 文件
	overseas_data = f"overseas_ip-{today}.list"  # 境外IP数据
	overseas_file = files_dir.joinpath(overseas_data)  # overseas 文件

	# 多线程
	max_threads = 50  # 最大线程数
	thread_pool = threading.BoundedSemaphore(max_threads)  # 线程数池

	# 查询
	task()

	# 程序结束时间
	run_time = int(datetime.datetime.now().timestamp() - start_time)
	print(f'The program takes {run_time}s', flush=True)
	print(datetime.datetime.today().strftime("%F %T"), flush=True)

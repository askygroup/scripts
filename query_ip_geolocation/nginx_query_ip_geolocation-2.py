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


def query():
	# 查询IP属地
	# 判断 ip_list 文件是否存在，不存在抛异常并退出
	ip_list_file = files_dir.joinpath(ip_list)
	if not ip_list_file.is_file():
		raise ValueError(f"ERROR: The {ip_list_file} does not exist !!!")
	# 备份 result 文件
	result_file = files_dir.joinpath(result_data)
	# 判断 result 文件是否存在，存在则备份，不存在则创建
	if result_file.is_file():
		result_file_bak = files_dir.joinpath(result_file.name.replace('.', f'-{today}.'))
		shutil.move(result_file, result_file_bak)

	# 读取需要查询的IP地址列表文件，将查询到的信息写入结果文件中
	with open(ip_list_file, 'r', encoding='utf-8') as ip_file, open(result_file, 'w', encoding='utf-8') as result_file:
		for full_ip in ip_file.readlines():
			full_ip = full_ip.strip()  # 去掉首位空白字符(换行符)
			ip = full_ip.split("|")[1]
			# print(ip)
			# 通过 API 查询IP属地信息
			ip_info = ipinfo_api(ip)
			if ip_info:
				result_file.write(f"{full_ip}|{ip_info}\n")
			else:
				print(f"{ip}|未查询到属地信息")
				result_file.write(f"{full_ip}|未查询到属地信息\n")


if __name__ == '__main__':
	# 程序开始时间
	start_time = datetime.datetime.now().timestamp()
	print(datetime.datetime.today().strftime("%F %T"), flush=True)
	today = datetime.datetime.today().strftime("%Y%m%d%H%M")
	# 切换到脚本所在目录
	script_dir = sys.path[0]  # 脚本所在目录
	os.chdir(script_dir)  # 切换到脚本所在目录
	current_dir = Path.cwd()  # 当前所在目录
	files_dir = current_dir.joinpath('files')  # 文件存放目录
	files_dir.mkdir(exist_ok=True)  # 如果目录不存在，创建文件存放目录

	# 配置文件
	ip_list = "test_ip.list"  # 需要查询的IP列表
	result_data = "test_ip.txt"  # 查询结果数据

	# 查询
	query()

	# 程序结束时间
	run_time = int(datetime.datetime.now().timestamp() - start_time)
	print(f'The program takes {run_time}s', flush=True)
	print(datetime.datetime.today().strftime("%F %T"), flush=True)

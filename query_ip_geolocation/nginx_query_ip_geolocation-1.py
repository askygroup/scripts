#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 读取 nginx 来源IP地址，查询IP属地信息

import datetime
import os
import sys
from pathlib import Path


def query():
	# 查询IP属地

	# 读取所有IP的地理位置信息文件
	with open(all_ip_geolocation, encoding='utf-8') as file:
		all_ip_info = file.readlines()

	with open(ip_list, 'r', encoding='utf-8') as ip_file, open(result_data, 'w', encoding='utf-8') as result_file:
		for full_ip in ip_file.readlines():
			# 取IP所在的网段（形如：192.168.1.0）
			ip = full_ip.split("|")[1]
			ip = ".".join(ip.split('.')[:3]) + ".0"
			# print(ip)
			ip_tag = True  # 是否未查询到
			for ip_info in all_ip_info:
				if ip_info.find(ip) != -1:
					result_file.write(f"{full_ip.strip()}|{ip_info.split('|', maxsplit=2)[-1]}")
					ip_tag = False  # 已查询到
			if ip_tag:
				result_file.write(f"{full_ip.strip()}|未查询到属地信息\n")


if __name__ == '__main__':
	# 程序开始时间
	start_time = datetime.datetime.now().timestamp()
	print(datetime.datetime.today().strftime("%F %T"), flush=True)
	# 切换到脚本所在目录
	script_dir = sys.path[0]  # 脚本所在目录
	os.chdir(script_dir)  # 切换到脚本所在目录
	current_dir = Path.cwd()  # 当前所在目录

	# 配置文件
	all_ip_geolocation = "all_ip.list"  # 所有IP的地理位置信息（IP属地）
	ip_list = "files/test_ip.list"  # 需要查询的IP列表
	result_data = "files/test_ip.txt"  # 查询结果数据

	# 查询
	query()

	# 程序结束时间
	run_time = int(datetime.datetime.now().timestamp() - start_time)
	print(f'The program takes {run_time}s', flush=True)
	print(datetime.datetime.today().strftime("%F %T"), flush=True)

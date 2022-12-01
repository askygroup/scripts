#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 查询单个IP（IPV4 地址、IPV6 地址）属地信息

import requests
import json


def ipinfo_ipv4_api(ip=''):
	# ip信息 IPV4 API https://ip.useragentinfo.com/json?ip=125.119.233.10
	url = f"https://ip.useragentinfo.com/json?ip={ip}"
	# 调用API
	response = requests.get(url, headers={}, data={}, timeout=3)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："中国 浙江省 杭州市 西湖区 电信"
		ip_geolocation = f"{result_info['country']} {result_info['province']} {result_info['city']} {result_info['area']} {result_info['isp']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def ipinfo_ipv6_api():
	# ip信息 IPV6 API https://ip.useragentinfo.com/ipv6/240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a
	url = f"https://ip.useragentinfo.com/ipv6/{ip}"
	# 调用API
	response = requests.get(url, headers={}, data={}, timeout=3)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："China Zhejiang Quzhou"
		ip_geolocation = f"{result_info['country']} {result_info['region']} {result_info['city']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def baidu_api(ip):
	# 百度 API http://opendata.baidu.com/api.php?query=125.119.233.10&co=&resource_id=6006&oe=utf8
	url = f"http://opendata.baidu.com/api.php?query={ip}&co=&resource_id=6006&oe=utf8"
	# 调用API
	response = requests.get(url, timeout=3)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："浙江省杭州市 电信"
		ip_geolocation = f"{result_info['data'][0]['location']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def taipingyang_api(ip=''):
	# 太平洋 API http://whois.pconline.com.cn/ipJson.jsp?ip=125.119.233.10&json=true
	url = f"http://whois.pconline.com.cn/ipJson.jsp?ip={ip}&json=true"
	# 调用API
	response = requests.get(url, timeout=3)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："浙江省杭州市 电信ADSL"
		ip_geolocation = f"{result_info['addr']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def ip_api(ip=''):
	# 查询速度较慢，容易超时；支持 IPV6 地址
	# ip API http://ip-api.com/json/125.119.233.10?lang=zh-CN
	url = f"http://ip-api.com/json/{ip}?lang=zh-CN"
	# 调用API
	response = requests.get(url, timeout=5)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："中国 浙江省 杭州 Chinanet"
		ip_geolocation = f"{result_info['country']} {result_info['regionName']} {result_info['city']} {result_info['isp']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def vore_ipv4_api(ip=''):
	# 查询速度较慢，容易超时
	# vore ipv4 API https://api.vore.top/api/IPv4?v4=125.119.233.10
	url = f"https://api.vore.top/api/IPv4?v4={ip}"
	# 调用API
	response = requests.get(url, timeout=5)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："浙江省 杭州市 西湖区 电信"
		ip_geolocation = f"{result_info['ipdata']['info1']} {result_info['ipdata']['info2']} {result_info['ipdata']['info3']} {result_info['ipdata']['isp']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def vore_ipv6_api(ip=''):
	# 查询速度较慢，容易超时
	# vore ipv6 API https://api.vore.top/api/IPv6?v6=240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a
	url = f"https://api.vore.top/api/IPv6?v6={ip}"
	# 调用API
	response = requests.get(url, timeout=5)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："云南省 昆明市 西山区 电信"
		ip_geolocation = f"{result_info['ipdata']['info1']} {result_info['ipdata']['info2']} {result_info['ipdata']['info3']} {result_info['ipdata']['isp']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def vore_api(ip=''):
	# 查询速度较慢，容易超时；支持 IPV6 地址
	# ip API https://api.vore.top/api/IPdata?ip=125.119.233.10
	url = f"https://api.vore.top/api/IPdata?ip={ip}"
	# 调用API
	response = requests.get(url, timeout=5)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："浙江省杭州市西湖区 - 电信"
		ip_geolocation = f"{result_info['adcode']['o']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


def zxinc_api(ip):
	# zxinc API https://ip.zxinc.org/api.php?type=json&ip=125.119.233.10
	url = f"https://ip.zxinc.org/api.php?type=json&ip={ip}"
	# 调用API
	response = requests.get(url, timeout=3)
	result_code = response.status_code
	result_info = response.json()
	if result_code == 200:
		# print(f"请求成功：{json.dumps(result_info, ensure_ascii=False, indent=4)}")
		# 所在地理位置："浙江省杭州市 电信"
		ip_geolocation = f"{result_info['data']['location']}"
		return ip_geolocation
	else:
		print(f"请求失败！返回码【{result_code}】")


# 查询IP属地信息
test_ip = '125.119.233.10'  # 所在地理位置："中国 浙江省 杭州市 西湖区 电信"
# test_ip = '114.36.113.10'  # 所在地理位置："中国 台湾省 台北市  中華電信"
# test_ip = '119.237.75.10'  # 所在地理位置："中国 香港特别行政区   电讯盈科"
# test_ip = '103.237.126.10'  # 所在地理位置："中国 澳门特别行政区   "
# test_ip = '144.202.124.10'  # 所在地理位置："美国 加利福尼亚 洛杉矶  "
# test_ip = '139.162.66.10'  # 所在地理位置："日本 东京   "
# test_ip = '101.112.48.70'  # 所在地理位置："澳大利亚 新南威尔士 悉尼  Vodafone Australia"
# test_ip = '240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a'  # 所在地理位置："China Zhejiang Quzhou"

print(ipinfo_ipv4_api(test_ip))
# print(ipinfo_ipv6_api(test_ip))
# print(baidu_api(test_ip))
# print(taipingyang_api(test_ip))
# print(ip_api(test_ip))  # 查询速度较慢
# print(vore_ipv4_api(test_ip))  # 查询速度较慢
# print(vore_ipv6_api(test_ip))  # 查询速度较慢
# print(vore_api(test_ip))  # 查询速度较慢
# print(zxinc_api(test_ip))

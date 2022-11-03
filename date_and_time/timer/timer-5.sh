#!/bin/bash
# 计时器(脚本功能介绍)
# Timer(script function introduction)

s=0
echo $s s
date=`date +%s`  # 记录初始秒
while true
do
	date1=`date +%s`  # 获取最新秒
	let t=$date1-$date  # 计算增加秒数
	if [ $t -eq 1 ]  # 增加秒数等于1，更新初始秒为最新秒，秒+1，显示计时时间
	then
		date=$date1
		let s++
		echo $s s
	else  # 增加秒数不等于1，则继续循环等待
		sleep 0.1
	fi
done

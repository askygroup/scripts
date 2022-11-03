#!/bin/bash
# 计时器(脚本功能介绍)
# Timer(script function introduction)

FORMAT()
{
if [ $s -lt 60 ]  # 当秒小于60时
then
	if [ $d -eq 0 ] && [ $h -eq 0 ] && [ $m -eq 0 ]  # 当天等于0，小时等于0，分钟等于0时，只显示秒
	then
		echo $s s
	elif [ $d -eq 0 ] && [ $h -eq 0 ]  # 当天等于0，小时等于0时，显示分钟和秒
	then
		echo $m m $s s
	elif [ $d -eq 0 ] && [ $h -gt 0 ]  # 当天等于0，小时大于0时，显示小时、分钟和秒
	then
		echo $h h $m m $s s
	else  # 当天大于0时，显示天、小时、分钟和秒
		echo $d d $h h $m m $s s
	fi
else  # 当秒等于60时
	let m++  # 分钟增加1，秒归零
	s=0
	if [ $m -lt 60 ]  # 当分钟小于60时
	then
		if [ $d -eq 0 ] && [ $h -eq 0 ]  # 当天等于0，小时等于0时，显示分钟
		then
			echo $m m
		elif [ $d -eq 0 ]  # 当天等于0时，显示小时和分钟
		then
			echo $h h $m m
		else  # 当天大于0时，显示天、小时和分钟
			echo $d d $h h $m m
		fi
	else  # 当分钟等于60时
		let h++  # 小时增加1，分钟归零
		m=0
		if [ $h -lt 24 ]  # 当小时小于24时
		then
			if [ $d -eq 0 ]  # 当天等于0时，显示小时
			then
				echo $h h
			else  # 当天大于0时，显示天和小时
				echo $d d $h h
			fi
		else  # 当小时等于24时
			let d++  # 天增加1，小时归零
			h=0
			echo $d d  # 显示天
		fi
	fi
fi
}

s=0
m=0
h=0
d=0
date=`date +%s`  # 记录初始秒
FORMAT  # 显示初始值
while true
do
	date1=`date +%s`  # 获取最新秒
	let t=$date1-$date  # 计算增加秒数
	if [ $t -eq 1 ]  # 增加秒数等于1，更新初始秒为最新秒，秒+1，显示计时时间
	then
		date=$date1
		let s++
		FORMAT
	else  # 增加秒数不等于1，则继续循环等待
		sleep 0.1
	fi
done

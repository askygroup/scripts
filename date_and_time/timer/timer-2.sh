#!/bin/bash
# 计时器(脚本功能介绍)
# Timer(script function introduction)

s=0
m=0
while true
do
	if [ $s -lt 60 ]  # 秒一直显示0-59
	then
		if [ $m -eq 0 ]  # 当分钟数等于0，只显示秒，即echo $s s
		then
			echo $s s
		else  # 当分钟数大于0，显示分钟和秒，即echo $m m $s s
			echo $m m $s s
		fi
	else  # 当秒等于60，分钟+1，秒归零，即s=0，echo $m m
		let m++
		s=0
		echo $m m
	fi
	let s++
	sleep 1
done

#!/bin/bash
# 计时器(脚本功能介绍)
# Timer(script function introduction)

s=0
m=0
h=0
while true
do
	if [ $s -lt 60 ]  # 秒一直显示0-59
	then
		if [ $h -eq 0 ] && [ $m -eq 0 ]  # 当分钟数和小时数都等于0，只显示秒，即echo $s s
		then
			echo $s s
		elif [ $h -eq 0 ]  # 当小时数等于0，显示分钟和秒，即echo $m m $s s
		then
			echo $m m $s s
		else  # 当小时数大于0，显示小时、分钟和秒，即echo $h h $m m $s s
			echo $h h $m m $s s
		fi
	else  # 当秒等于60，分钟+1，秒归零
		let m++
		s=0
		if [ $m -lt 60 ]  # 分钟一直显示0-59
		then
			if [ $h -eq 0 ]  # 当小时等于0，显示分钟，即echo $m m
			then
				echo $m m
			else  # 当小时大于0，显示小时和分钟，即echo $h h $m m
				echo $h h $m m
			fi
		else  # 当分钟等于60，小时+1，分钟归零，即m=0，echo $h h
			let h++
			m=0
			echo $h h
		fi
	fi
	let s++
	sleep 1
done

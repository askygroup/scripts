#!/bin/bash
# 整点报时器

DISPLAY()
{
	# 显示时间
	ns=`date +%N`
	ms=${ns:0:3}
	time=`date +%T`
	s=${time:6:2}
	m=${time:3:2}
	if [ $m -eq 59 ] && [ $s -ne 00 ] # 整点倒计时
	then
		s=$((10#$s))
		t=`printf "%2d\n" $((60-$s))`  # 数字右对齐
		echo -en "\033[1m  $time.$ms\033[0m"
		if [ $((t%5)) -eq 0 ]  # 每5秒响铃一会儿
		then
			echo -en "\t${t}s\a\r"
		else
			echo -en "\t${t}s\r"
		fi
	elif [ $s -ge 50 ]  # 整分钟倒计时
	then
		t=`printf "%2d\n" $((60-$s))`  # 数字右对齐
		echo -en "\033[1m  $time.$ms\033[0m"
		echo -en "\t${t}s\r"
	elif [ $m -eq 00 ] && [ $s -eq 00 ]  # 整点显示
	then
		echo -en "\033[1;31m  $time          \r\033[0m"
	elif [ $s -eq 00 ]  # 整分钟显示
	then
		echo -en "\033[31m  $time          \r\033[0m"
	else  # 正常时间显示
		echo -en "\033[1m  $time.$ms\r\033[0m"
	fi
}

# 显示初始时间
DISPLAY
# 显示
while true
do
	DISPLAY
done

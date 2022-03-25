#!/bin/bash
# 整点报时器

DISPLAY()
{
# 显示时间
	time=`date +%T`
	s=${time:6:2}
	m=${time:3:2}
	if [ $m -eq 59 ] && [ $s -ge 50 ]  # 整点倒计时
	then
		t=$((60-$s))
		echo -en "\033[1m  $time\033[0m"
		echo -e "\t${t}s"
	elif [ $s -ge 55 ]  # 整分钟倒计时
	then
		t=$((60-$s))
		echo -en "\033[1m  $time\033[0m"
		echo -e "\t${t}s"
	elif [ $m -eq 00 ] && [ $s -eq 00 ]  # 整点显示
	then
		echo -e "\033[1;31m  $time\033[0m"
		echo -e "\033[1m\a--------------------\n--------------------\033[0m"
	elif [ $s -eq 00 ]  # 整分钟显示
	then
		echo -e "\033[31m  $time\033[0m"
		echo -e "\033[1m\a----------\033[0m"
	else  # 正常时间显示
		echo -e "\033[1m  $time\033[0m"
	fi
}

# 记录初始秒
date=`date +%s`
# 显示初始时间
echo -e "\033[1m  `date +%T`\033[0m"
# 显示
while true
do
	# 获取最新秒
	date1=`date +%s`
	# 计算增加秒数
	let t=$date1-$date
	# 增加秒数等于1，更新初始秒为最新秒，显示时间
	if [ $t -eq 1 ]
	then
		date=$date1
		DISPLAY
	fi
done

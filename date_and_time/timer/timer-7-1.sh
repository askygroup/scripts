#!/bin/bash
# 计时器(脚本功能介绍)
# Timer(script function introduction)

# 误差值，越小越精确、CPU消耗越大
error=0.01

DISPLAY()
{
# 将时间补零，方便显示
s=`echo $s |awk '{printf("%02d\n",$0)}'`
m=`echo $m |awk '{printf("%02d\n",$0)}'`
h=`echo $h |awk '{printf("%02d\n",$0)}'`
if [ $d -eq 0 ]  # 当天等于0时，显示时分秒
then
	#clear
	echo -en "\033[1m  $h:$m:$s\033[0m\r"
else  # 当天大于0时，显示天时分秒
	#clear
	echo -en "\033[1m  $d $h:$m:$s\033[0m\r"
fi
# 将时间前面的零去掉，方便计算(避免09、08的尴尬)
let h=$((10#$h))
let m=$((10#$m))
let s=$((10#$s))
}

FORMAT()
{
if [ $s -lt 60 ]  # 当秒小于60时
then
	DISPLAY
else  # 当秒等于60时
	let m++  # 分钟增加1，秒归零
	s=0
	if [ $m -lt 60 ]  # 当分钟小于60时
	then
		DISPLAY
	else  # 当分钟等于60时
		let h++  # 小时增加1，分钟归零
		m=0
		if [ $h -lt 24 ]  # 当小时小于24时
		then
			DISPLAY
		else  # 当小时等于24时
			let d++  # 天增加1，小时归零
			h=0
			DISPLAY
		fi
	fi
fi
}

s=0
m=0
h=0
d=0
date=`date +%s`  # 记录初始秒
echo -e "计时开始：\n"
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
		sleep $error
	fi
done

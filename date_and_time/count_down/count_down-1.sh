#!/bin/bash
# 倒计时

# 误差值，越小越精确、CPU消耗越大
error=0.01

# 截止时间
# 支持输入格式：12:00、20221118、2022-11-18 12:00
deadline=$*
# echo $deadline

# 检查输入的截止日期是否合法
CHECK()
{
	cache_deadline=`date -d "$deadline" +%s 2> /dev/null`  # 丢弃错误输出，将标准输出赋值给变量
	if [ $cache_deadline ]; then
		datetime=`date -d "$deadline" "+%F %T"`
		echo "截止时间：$datetime"
		# echo $cache_deadline
		if [ $cache_deadline -gt $date_s ]; then
			deadline_s=$(($cache_deadline-$date_s))  # 截止时间还有多少秒
			# echo $deadline_s
		else
			echo -e "\n您输入的截止时间小于当前时间，时间已过，请重新尝试"
			echo -e "\a" && exit 1
		fi
	else
		echo -e "\n您输入的截止时间不合法，请重新尝试【$deadline】"
		echo -e "\a" && exit 1
	fi
}

# 计算时间
COUNT()
{
	# 截止时间和现在的时间之间，还有几天
	one_day_s=$((60*60*24))
	d=$(($deadline_s/$one_day_s))
	# 减去剩余天数后，计算剩余的小时数
	hour_s=$(($deadline_s%$one_day_s))
	one_hour_s=$((60*60))
	h=$(($hour_s/$one_hour_s))
	# 再减去剩余的小时数后，计算剩余的分钟数
	minute_s=$(($hour_s%$one_hour_s))
	one_minute_s=60
	m=$(($minute_s/$one_minute_s))
	# 再减去剩余的分钟数后，剩余的就是秒数
	second_s=$(($minute_s%$one_minute_s))
	s=$second_s
}

# 显示倒计时
DISPLAY()
{
# 将时间补零，方便显示
s=`echo $s |awk '{printf("%02d\n",$0)}'`
m=`echo $m |awk '{printf("%02d\n",$0)}'`
h=`echo $h |awk '{printf("%02d\n",$0)}'`
if [ $d -eq 0 ]  # 当天等于0时，显示时分秒
then
	echo -e "\033[1m  $h:$m:$s\033[0m"
else  # 当天大于0时，显示天时分秒
	echo -e "\033[1m  $d $h:$m:$s\033[0m"
fi
}

date_s=`date +%s`  # 记录当前系统秒
CHECK
while true; do
	now_date_s=`date +%s`  # 现在的系统秒数
	t=$(($now_date_s-$date_s)) # 计算增加秒数
	if [ $t -eq 1 ]  # 增加秒数等于1，更新初始秒为最新秒，秒+1，显示计时时间
	then
		date_s=$now_date_s
		# 将时间前面的零去掉，方便计算(避免09、08的尴尬)
		let deadline_s=$((10#$deadline_s))
		let deadline_s--
		if [ $deadline_s -eq 0 ]; then
			echo -e "时间到：$datetime"
			exit
		fi
		COUNT
		DISPLAY
	else  # 增加秒数不等于1，则继续循环等待
		sleep $error
	fi
done

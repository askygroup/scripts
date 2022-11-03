#!/bin/bash
# 日期计算脚本(脚本功能介绍)

# 开始结束日期
date1=$1
date2=$2
year=`date +%Y`
month=`date +%m`

# 如果没有输入年份、月份，自动补全年份、月份
TABLE ()
{
# 判断开始日期是否自动补全，是则补全结束日期
if echo $date1 | egrep -q '\<[0-9]{8}\>'
then
	date=$date2
# 不是则补全开始日期
else
	date=$date1
fi

# 判断日期长度，自动补全
# 判断日期长度，两位则补全年份和月份
if echo $date | egrep -q '\<[0-9]{2}\>'
then
	# 判断日期参数大小，如果是1-31，则自动补全年份和月份
	# 将时间前面的零去掉，方便计算(避免09、08的尴尬)
	let date=$((10#$date))
	if [ $date -ge 1 ] && [ $date -le 31 ]
	then
		date=$yesr$month`echo $date |awk '{printf("%02d\n",$0)}'`
	# 大于则代表表示日期日份不对
	else
		date=error
	fi
# 四位则补全年份
elif echo $date | egrep -q '\<[0-9]{4}\>'
then
	date=error
else
	date=date
fi
}

# 判断是否输入参数，若没有提醒输入，并检查参数格式
TEST ()
{
# 判断开始日期是否存在，存在则检查参数格式
if [ $date1 ]
then
	# 判断开始日期格式，格式正确则判断结束日期
	if [ -z `echo $date1 | sed 's/[0-9]//g'` ]
	then
		#TABLE
		date1=$date1
		# 判断结束日期是否存在，存在则检查参数格式
		if [ $date2 ]
		then
			# 判断开始日期格式，格式正确则继续
			if [ -z `echo $date2 | sed 's/[0-9]//g'` ]
			then
				#TABLE
				date2=$date2
				if [ $date1 -ge $date2 ]
				then
					echo -e "\n您输入的开始日期大于结束日期，请重新尝试 (例如: 19950817)\n"
					echo -e "\a" && exit 1
				fi
			# 结束日期格式不正确，提醒重新输入
			else
				echo -e "\n您输入的结束日期格式不正确，请重新输入 (例如: 19950818)\n"
				read -p "请输入结束日期 (例如: 19950818) : " date2
				TEST
			fi
		# 结束日期不存在，则提醒输入
		else
			read -p "请输入结束日期 (例如: 19950818) : " date2
			TEST
		fi
	# 开始日期格式不正确，提醒重新输入
	else
		echo -e "\n您输入的开始日期格式不正确，请重新输入 (例如: 19950817)\n"
		read -p "请输入开始日期 (例如: 19950817) : " date1
		TEST
	fi
# 开始日期不存在，则提醒输入
else
	read -p "请输入开始日期 (例如: 19950817) : " date1
	TEST
fi
}

# 计算日期
HANDLE()
{
# 开始、结束日期那天的系统秒数
date1_s=`date -d $date1 +%s`
date2_s=`date -d $date2 +%s`

# 开始、结束日期之间的秒数
date_s=$[$date2_s-$date1_s]
echo $date_s

# 开始、结束日期之间的天数(分时日)
one_day_s=$[60*60*24]
date_day=$[$date_s/$one_day_s]
echo -e "\n开始、结束日期之间的天数是: $date_day天\n"

}

TEST
HANDLE

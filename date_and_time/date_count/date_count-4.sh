#!/bin/bash
# 日期计算脚本(脚本功能介绍)

# 开始结束日期
date1=$1
date2=$2

# 使用 "date -d" 智能补全日期
TABLE ()
{
cache_date=`date -d $2 +%Y%m%d 2> /dev/null`  # 丢弃错误输出，将标准输出赋值给变量
if [ $cache_date ] && [ $1 == 'date1' ]
then
	date1=$cache_date
elif [ $cache_date ] && [ $1 == 'date2' ]
then
	date2=$cache_date
# 补全失败重新输入
elif [ $1 == 'date1' ]
then
	date1=''
	echo -e "\n开始日期智能补全失败，请重新尝试\n"
	TEST
elif [ $1 == 'date2' ]
then
	date2=''
	echo -e "\n结束日期智能补全失败，请重新尝试\n"
	TEST
fi
}

# 判断是否输入参数，若没有提醒输入，并检查参数格式
TEST ()
{
# 判断开始日期是否存在，存在则检查参数格式
if [ $date1 ]
then
	TABLE date1 $date1
	# 判断结束日期是否存在，存在则检查参数格式
	if [ $date2 ]
	then
		TABLE date2 $date2
		if [ $date1 -gt $date2 ]
		then
			echo -e "\n您输入的开始日期大于结束日期，请重新尝试\n"
			echo -e "\a" && exit 1
		fi
	# 结束日期不存在，则提醒输入
	else
		read -p "请输入结束日期 (例如: 19950818) : " date2
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
echo $date1 $date2
date1_s=`date -d $date1 +%s`
date2_s=`date -d $date2 +%s`

# 开始、结束日期之间的秒数
date_s=$[$date2_s-$date1_s]
echo -e "\n开始、结束日期之间的秒数是: $date_s 秒"

# 开始、结束日期之间的天数(分时日)
one_day_s=$[60*60*24]
date_day=$[$date_s/$one_day_s]
echo -e "\n开始、结束日期之间的天数是: $date_day天\n"

}

TEST
HANDLE

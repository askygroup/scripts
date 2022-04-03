#!/bin/bash
# 生日计算

# 出生日期年月日
birth_date=$1

CHECK_SPECIAL()
{
	# 特殊日期排除
	md=$birth_date_month$birth_date_day
	y=$((10#$birth_date_year))
	case $md in
	# 二月没有30日，二、四、六、九、十一月没有31日
	0230|0231|0431|0631|0931|1131)
		echo -e "\n您输入的日期不合理 ( $birth_date 日期不存在)"
		echo -e "\a" && exit 1
		;;
	# 平年二月没有29日
	0229)
		if [ ! $(($y%4)) == 0 ]
		then
			echo -e "\n您输入的日期不合理(平年二月没有29日) ( $birth_date 日期不存在)"
			echo -e "\a" && exit 1
		fi
		;;
	esac
}

CHECK_DATE()
{
	# 出生年份 出生月份 出生日，日期合法性判断
	# 判断获取的年月日是否都不为空
	#echo $birth_date_year $birth_date_month $birth_date_day
	if [ ! $birth_date_year -o ! $birth_date_month -o ! $birth_date_day ]
	then
		echo -e "\a" && exit 1
	fi
	# 将时间前面的零去掉，方便计算(避免09、08的尴尬)
	m=$((10#$birth_date_month))
	d=$((10#$birth_date_day))
	# 判断日期参数大小，如果月份在1-12之间，日份在1-31之间，则合理性初步通过
	if [ $m -ge 1 ] && [ $m -le 12 ] && [ $d -ge 1 ] && [ $d -le 31 ]
	then
		CHECK_SPECIAL
	# 否则代表表示日期不合理
	else
		echo -e "\n您输入的日期不合理(月或日) ( $birth_date 日期不存在)"
		echo -e "\a" && exit 1
	fi
}

TEST ()
{
	# 判断是否输入参数，若没有提醒输入，并检查参数格式，格式正常输出出生日期年月日
	# 年份4位数，月份、日2位数，不够前面补零
	if [ $birth_date ]
	then
		if echo $birth_date | egrep -q '\<[0-9]{5,8}\>'
		then
			birth_date_year=`date -d $birth_date +%Y`
			birth_date_month=`date -d $birth_date +%m`
			birth_date_day=`date -d $birth_date +%d`
		elif echo $birth_date | egrep -q '\<[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}\>' || echo $birth_date | egrep -q '\<[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,2}\>'
		then
			birth_date_year=`date -d $birth_date +%Y`
			birth_date_month=`date -d $birth_date +%m`
			birth_date_day=`date -d $birth_date +%d`
		else
			echo -e "\n您输入的日期格式不正确，请重新尝试"
			echo -e "\a" && exit 1
		fi
		CHECK_DATE
	else
		read -p "请输入您的出生日期 (例如: 19950817(1995-08-17、1995/08/17)) : " birth_date
		TEST
	fi
}

AGE()
{
	# 今天生日年月日
	now_year_birthday=$now_date_year$birth_date_month$birth_date_day
	# 今年生日那天的系统秒数
	now_year_birthday_date_s=`date -d $now_year_birthday +%s`
	# 现在的系统秒数
	now_date_s=`date +%s`

	# 距离今年生日那天的秒数，计算出距离今年生日那天的天数
	one_day_s=$((60*60*24))
	birthday_time_s=$(($now_year_birthday_date_s-$now_date_s))
	birthday_d=$(($birthday_time_s/$one_day_s))
	# 减去今年生日那天的天数后，计算剩余的小时数
	hour_s=$(($birthday_time_s%$one_day_s))
	one_hour_s=$((60*60))
	birthday_h=$(($hour_s/$one_hour_s))
	# 减去今年生日那天的天数后，再减去小时数，计算剩余的分钟数
	minute_s=$(($hour_s%$one_hour_s))
	one_minute_s=60
	birthday_m=$(($minute_s/$one_minute_s))
	# 减去今年生日那天的天数后，再减去小时数、分钟数，剩余的就是秒数
	second_s=$(($minute_s%$one_minute_s))
	birthday_s=$second_s

	# 现在年龄
	age=$(($now_date_year-$y))
	# 判断生日是否已过，已过时间在一天时间内,说明生日是今天
	if [ $birthday_time_s -le 0 ] && [ $birthday_time_s -ge -$one_day_s ]
	then
		echo -e "\n您现在的年龄是: ${age}岁"
		echo -e "今天是您的生日，祝您生日快乐 ！\n"
	elif [ $birthday_time_s -lt -$one_day_s ]
	then
		echo -e "\n您现在的年龄是: ${age}岁"
		birthday_d=$((-$birthday_d-1))
		birthday_h=$((-$birthday_h))
		birthday_m=$((-$birthday_m))
		birthday_s=$((-$birthday_s))
		echo -e "您今年的生日已过去：${birthday_d}天${birthday_h}小时${birthday_m}分钟${birthday_s}秒\n"
	else
		# 今年生日没过，年龄减一岁(满足玻璃心)
		age=$(($age-1))
		echo -e "\n您现在的年龄是: ${age}岁"
		echo -e "距离您今年的生日还有：${birthday_d}天${birthday_h}小时${birthday_m}分钟${birthday_s}秒\n"
	fi
}

BIRTHDAY()
{
	# 出生日期
	echo -e "\n您的出生日期是: ${birth_date_year}年${birth_date_month}月${birth_date_day}日"

	# 今年年份
	now_date_year=`date +%Y`
	# 今年生日
	echo -e "您今年的生日是: ${now_date_year}年${birth_date_month}月${birth_date_day}日"

	# 现在年龄
	AGE

	# 出生那天的系统秒数
	birth_date_s=`date -d $birth_date +%s`
	# 现在的系统秒数
	now_date_s=`date +%s`
	# 已活秒数
	live_s=$(($now_date_s-$birth_date_s))
	echo -e "您已活的秒数是: ${live_s}秒"

	# 已活天数(分时日)
	one_day_s=$((60*60*24))
	live_day=$(($live_s/$one_day_s))
	echo -e "您已活的天数是: ${live_day}天\n"
}

TEST
BIRTHDAY

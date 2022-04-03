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
			birth_date_year=`printf "%04d\n" ${birth_date:0:-4}`
			birth_date_month_day=${birth_date: -4}
			birth_date_month=${birth_date_month_day:0:2}
			birth_date_day=${birth_date_month_day:2:2}
		elif echo $birth_date | egrep -q '\<[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}\>' || echo $birth_date | egrep -q '\<[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,2}\>'
		then
			birth_date_year=`echo $birth_date | awk -F '-|/' '{printf("%04d\n",$1)}'`
			birth_date_month=`echo $birth_date | awk -F '-|/' '{printf("%02d\n",$2)}'`
			birth_date_day=`echo $birth_date | awk -F '-|/' '{printf("%02d\n",$3)}'`
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

TEST

# 出生日期
echo -e "\n您的出生日期是: ${birth_date_year}年${birth_date_month}月${birth_date_day}日\n"

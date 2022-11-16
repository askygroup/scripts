#!/bin/bash
# 日期计算脚本(脚本功能介绍)

# 开始结束日期
date1=$1
date2=$2

# 特殊情况排除
T2 ()
{
md2=${date2:4:4}
y2=${date2:0:4}
case $md2 in
# 二月没有30日，二、四、六、九、十一月没有31日
0230|0231|0431|0631|0931|1131)
	echo -e "\n您输入的结束日期不合理 ( $date2 日期不存在)\n"
	date2=error
	TEST2
	;;
# 平年二月没有29日
0229)
	if [ $(($y2%4)) == 0 ]
	then
		date2=$date2
	else
		echo -e "\n您输入的结束日期不合理 ( $date2 日期不存在)\n"
		date2=error
		TEST2
	fi
	;;
*)
	date2=$date2
esac
}

# 日期合理性判断
TRUE2 ()
{
# 检查结束日期的合理性
# 将时间前面的零去掉，方便计算(避免09、08的尴尬)
m2=$((10#${date2:4:2}))
d2=$((10#${date2:6:2}))
# 判断日期参数大小，如果月份在1-12之间，日份在1-31之间，则合理性初步通过
if [ $m2 -ge 1 ] && [ $m2 -le 12 ] && [ $d2 -ge 1 ] && [ $d2 -le 31 ]
then
	T2
# 否则代表表示日期不合理
else
	echo -e "\n您输入的结束日期不合理 ( $date2 日期不存在)\n"
	date2=error
	TEST2
fi

# 结束日期大于开始日期检测
if [ $date1 -gt $date2 ]
then
	echo -e "\n您输入的开始日期大于结束日期，请重新尝试\n"
	echo -e "\a" && exit 1
fi
}

# 特殊情况排除
T1 ()
{
md1=${date1:4:4}
y1=${date1:0:4}
case $md1 in
# 二月没有30日，二、四、六、九、十一月没有31日
0230|0231|0431|0631|0931|1131)
	echo -e "\n您输入的开始日期不合理 ( $date1 日期不存在)\n"
	date1=error
	TEST
	;;
# 平年二月没有29日
0229)
	if [ $(($y1%4)) == 0 ]
	then
		date1=$date1
	else
		echo -e "\n您输入的开始日期不合理 ( $date1 日期不存在)\n"
		date1=error
		TEST1
	fi
	;;
*)
	date1=$date1
esac
}

# 日期合理性判断
TRUE1 ()
{
# 检查开始日期的合理性
# 将时间前面的零去掉，方便计算(避免09、08的尴尬)
m1=$((10#${date1:4:2}))
d1=$((10#${date1:6:2}))
# 判断日期参数大小，如果月份在1-12之间，日份在1-31之间，则合理性初步通过
if [ $m1 -ge 1 ] && [ $m1 -le 12 ] && [ $d1 -ge 1 ] && [ $d1 -le 31 ]
then
	T1
# 否则代表表示日期不合理
else
	echo -e "\n您输入的开始日期不合理 ( $date1 日期不存在)\n"
	date1=error
	TEST1
fi
}

TEST2 ()
{
# 判断结束日期是否存在，存在则检查参数格式
if [ $date2 ]
then
	# 判断开始日期格式，格式正确则继续
	if echo $date2 | egrep -q '\<[0-9]{8}\>'
	then
		TRUE2
	# 结束日期格式不正确，提醒重新输入
	else
		echo -e "\n您输入的结束日期格式不正确，请重新输入 (例如: 19950818)\n"
		read -p "请输入结束日期 (例如: 19950818) : " date2
		TEST2
	fi
# 结束日期不存在，则提醒输入
else
	read -p "请输入结束日期 (例如: 19950818) : " date2
	TEST2
fi
}

# 判断是否输入参数，若没有提醒输入，并检查参数格式
TEST1 ()
{
# 判断开始日期是否存在，存在则检查参数格式
if [ $date1 ]
then
	# 判断开始日期格式，格式正确则判断结束日期
	if echo $date1 | egrep -q '\<[0-9]{8}\>'
	then
		TRUE1
	# 开始日期格式不正确，提醒重新输入
	else
		echo -e "\n您输入的开始日期格式不正确，请重新输入 (例如: 19950817)\n"
		read -p "请输入开始日期 (例如: 19950817) : " date1
		TEST1
	fi
# 开始日期不存在，则提醒输入
else
	read -p "请输入开始日期 (例如: 19950817) : " date1
	TEST1
fi
}

# 计算日期
HANDLE()
{
# 开始、结束日期那天的系统秒数
date1_s=`date -d $date1 +%s`
date2_s=`date -d $date2 +%s`

# 开始、结束日期之间的秒数
if [ $date1_s ] && [ $date2_s ]
then
	date_s=$[$date2_s-$date1_s]
else
	echo -e "\n您输入的开始或结束日期不合理 ( $date1 或 $date2 日期不存在) ，请重新尝试\n"
	echo -e "\a" && exit 1
fi

# 开始、结束日期之间的天数(分时日)
one_day_s=$[60*60*24]
date_day=$[$date_s/$one_day_s]
echo -e "\n开始、结束日期之间的天数是: $date_day天\n"
}

TEST1
TEST2
HANDLE

#!/bin/bash
# 日期计算脚本(脚本功能介绍)

# 开始结束日期
date1=$1
date2=$2

# 判断是否输入参数，若没有提醒输入，并检查参数格式
TEST ()
{
# 判断开始日期是否存在，存在则检查参数格式
if [ $date1 ]
then
	# 判断开始日期格式，格式正确则判断结束日期
	if echo $date1 | egrep -q '\<[0-9]{8}\>'
	then
		date1=$date1
		# 判断结束日期是否存在，存在则检查参数格式
		if [ $date2 ]
		then
			# 判断开始日期格式，格式正确则继续
			if echo $date2 | egrep -q '\<[0-9]{8}\>'
			then
				date2=$date2
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

TEST
echo $date1 $date2

#!/bin/bash
# 生日计算

# 出生日期年月日
birth_date=$1

TEST ()
{
# 判断是否输入参数，若没有提醒输入，并检查参数格式，格式正常输出出生日期年月日
if [ $birth_date ]
then
	if echo $birth_date | egrep -q '\<[0-9]{8}\>'
	then
		birth_date=$birth_date
	else
		echo -e "\n您输入的日期格式不正确，请重新尝试"
		echo -e "\a" && exit 1
	fi
else
	read -p "请输入您的出生日期 (例如: 19950817) : " birth_date
	TEST
fi
}

TEST

#echo -e "\n您的出生日期是: ${birth_date:0:4}年${birth_date:4:2}月${birth_date:6:2}日\n"
# 出生年份 出生月份 出生日
birth_date_year=${birth_date:0:4}
birth_date_month=${birth_date:4:2}
birth_date_day=${birth_date:6:2}
# 出生日期
echo -e "\n您的出生日期是: ${birth_date_year}年${birth_date_month}月${birth_date_day}日\n"

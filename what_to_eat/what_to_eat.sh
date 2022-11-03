#！/bin/bash

foods="食物列表.txt"
cd `dirname $0`

# 食物总数
number_total=`wc -l $foods | awk '{print $1}'`
# echo $number_total

# 生成随机数当作行号(随机数默认从0开始，且"wc -l"统计空文件也是0行，所以需要加1)
random=`echo $[RANDOM%$number_total]`
# number_food=$((random + 1))
# echo $random $number_food
# head -$number_food $foods | tail -1
let random++
# 根据随机行号，打印食物名称
head -$random $foods | tail -1


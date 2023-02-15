#！/bin/bash

cd `dirname $0`
foods="foods.txt"

# 食物总数("wc -l"统计文件行数是按换行符统计的，最后一行需保留空行)
number_total=`wc -l $foods | awk '{print $1}'`
# echo $number_total

# 生成随机数当作行号(随机数默认从0开始，所以需要加1)
random=`echo $[RANDOM%$number_total]`
# random=$((random + 1))
let random++
# echo $random
# 根据随机行号，打印食物名称
head -$random $foods | tail -1

#!/bin/bash
# shell脚本多进程并发功能脚本(脚本功能介绍)
# 多进程并发执行(并行)

TASK()
{
	for i in `seq 10`
	do
		{
			echo $i
			sleep 1
		} &
	done

	# 等待所有后台子进程结束
	wait
}

echo -e "\nStart time : `date '+%F %T'`\n"
t1=`date +%s`

TASK

echo -e "\nEnd time : `date '+%F %T'`\n"
t2=`date +%s`
time=$[$t2-$t1]
echo -e "The process cost time ${time}s\n"

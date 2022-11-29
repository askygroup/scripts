#!/bin/bash
# shell脚本多进程并发功能脚本(脚本功能介绍)
# 多进程并发执行，使用两层循环控制并发数(并行可控)

TASK()
{
	# 并发的最大进程数
	thread=3
	# 总任务数
	task=10
	# 任务需要执行的次数
	task_time=$(($task/$thread))
	remainder=$(($task%$thread))
	# echo $task_time $remainder
	# 如果有余数，执行次数加一
	if [ $remainder -gt 0 ]
	then
		let task_time++
	fi

	start_task=1  # 起始任务
	for ((t=0; t<task_time; t++))
	do
		end_task=$(($start_task+$thread-1))  # 结束任务
		# 判断结束任务是否大于于总任务数，大于则结束任务等于总任务数
		if [ $end_task -gt $task ]
		then
			end_task=$task
		fi
		# echo $start_task $end_task
		for ((i=$start_task; i<=$end_task; i++))
		do
			{
			echo $i
			sleep 1
			} &
		done
		start_task=$(($end_task+1))
		wait  # 等待子进程结束
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

#!/bin/bash
# shell脚本多进程并发功能脚本(脚本功能介绍)
# 多进程并发执行，并发数可控(并行可控)

ACTION()
{
	echo $i
	sleep 1
}

TASK()
{
	# 新建一个fifo类型的管道文件（类似一个消息队列）（$$ 为当前进程的PID）
	tmp_fifofile="$$.fifo"
	mkfifo $tmp_fifofile
	# 以读写模式（<>）操作管道文件
	# 系统调用 exec 是以新的进程去替代原来的进程，进程的PID保持不变，本质上是调用进程内部执行一个可执行文件
	# 6为文件描述符，这个数字除了0、1、2之外的所有未声明过的字符
	exec 6<> $tmp_fifofile
	rm $tmp_fifofile  # 删除创建的管道文件

	# 并发的最大进程数
	thread=3
	# 在文件描述符中，为并发进程创建占位信息，事实上就是在管道fd6中放置了 $thread 个回车符
	for ((i=0; i<$thread; i++))
	do
		echo
	done >& 6

	for i in `seq 10`
	do
		# 一个 read -u6 命令执行一次，就从管道fd6中减去一个回车符，然后向下执行
		# 管道fd6中没有回车符时候，就停在这里了，从而实现线程数量控制
		read -u6
		{
			ACTION
			# 当进程结束以后，再向管道fd6中加上一个回车符，即补上了 read -u6 减去的那个
			#echo
			echo >& 6
		} &
	done

	# 等待所有后台子进程结束
	wait
	# 关闭管道fd6
	exec 6>& -
}

echo -e "\nStart time : `date '+%F %T'`\n"
t1=`date +%s`

TASK

echo -e "\nEnd time : `date '+%F %T'`\n"
t2=`date +%s`
time=$[$t2-$t1]
echo -e "The process cost time ${time}s\n"

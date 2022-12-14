#!/bin/bash
# iowait告警自动打堆栈脚本(脚本功能介绍)

# 触发器：CPU iowait 超过35%
# 告警描述：cpu iowait 连续三分钟超过40%时报警,当连续5分钟低于35%时为恢复正常
# 告警问题表达形式：(({TRIGGER.VALUE}=0 and {HOST_NAME:system.cpu.util[,iowait].min(3m)}>40) or ({TRIGGER.VALUE}=1 and {HOST_NAME:system.cpu.util[,iowait].min(5m)}>35))

# 脚本触发条件：cpu iowait 连续三分钟超过40%时报警，并触发自动打堆栈
# 脚本方案：计划任务每分钟调用一次脚本，并记录iowait使用百分比，当出现连续三分钟值都超过35%，则自动打三次堆栈

host=`hostname`
data=iowait.data
log=iowait.log
cd `dirname $0`

# 自动切割日志文件
day=`date +%Y%m%d%H%M`
yesterday=`date -d yesterday +%Y%m%d`
# 一个月切割一次202005 010000 (01)
#if [ ${day:6:6} == 010000 ]
# 一天切割一次20200501 0000 (01)
if [ ${day:8:4} == 0000 ]
then
	mv $log $log.$yesterday-bak
	mv $data $data.$yesterday-bak
	# 历史记录保留两条，脚本对比数据使用
	tail -2 $data.$yesterday-bak > $data
fi

# 获取当前iowiat使用百分比，并记录
#io=`iostat -c | grep -A 1 "%iowait" | awk '{print $(NF-2)}' | tail -1`
#io=`sar 1 1 | grep -A 1 "%iowait" | awk '{print $(NF-2)}' | tail -1`
#io=`sar 5 10 | grep "Average" | awk '{print $(NF-2)}'`
io=`sar 2 30 | grep "Average\|平均时间" | awk '{print $(NF-2)}'`
date=`date "+%F %T"`
time=`date +%Y%m%d-%H%M%S`
echo "$date iowait : $io" >> $data

JSTACK ()
{
pid=`jps | grep -v grep | grep Bootstrap | awk '{print $1}'`
# 判断Bootstrap进程PID是否存在，存在则打堆栈，不存在则报错退出
if [ $pid ]
then
	# 打三次堆栈
	for i in `seq 3`
	do
		jstack $pid >> jstack.$host.$time.txt
	done
else
	echo "Process PID does not exist" >> $log
	return 1
fi
}

# 判断io使用百分比是否大于35，如果大于35，则判断前两分钟io是否也大于35
if [[ $(echo "$io > 35" | bc) = 1 ]]
then
	echo "$date iowait : $io" >> $log
	io1=`tail -2 $data | head -1 | awk '{print $(NF)}'`
	io2=`tail -3 $data | head -1 | awk '{print $(NF)}'`
	# 判断前两分钟io是否也大于35，都大于35则自动打三次堆栈，并记录日志，有一个不大于则退出
	if [ $(echo "$io1 > 35" | bc) = 1 ] && [ $(echo "$io2 > 35" | bc) = 1 ]
	then
		echo -e "\n$date The iowait alarm has been violated , and it starts to stack automatically !" >> $log
		if JSTACK
		then
			echo -e "$date Stack done !\n\n" >> $log
		else
			echo -e "$date Stack failed ! ! !\n\n" >> $log
		fi
	# 有一个不大于则退出
	else
		echo "$date Not triggered !" >> $log
	fi
fi

# 自动清理日志和jstack文件，保留最新的20个文件
files=($data $log jstack)
for file in ${files[*]}
do
	number=`ls ${file}?* | wc -l`
	if [ $number -gt 20 ]
	then
		rm `ls -tr ${file}?* | head -1`
	fi
done

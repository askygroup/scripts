#!/bin/bash
# iowait告警自动打堆栈脚本(脚本功能介绍)

# 触发器：CPU iowait 超过35%
# 告警描述：cpu iowait 连续三分钟超过40%时报警,当连续5分钟低于35%时为恢复正常
# 告警问题表达形式：(({TRIGGER.VALUE}=0 and {HOST_NAME:system.cpu.util[,iowait].min(3m)}>40) or ({TRIGGER.VALUE}=1 and {HOST_NAME:system.cpu.util[,iowait].min(5m)}>35))

# 脚本触发条件：cpu iowait 连续三分钟超过40%时报警，并触发自动打堆栈
# 脚本方案：计划任务每分钟调用一次脚本，并记录iowait使用百分比，当出现连续三分钟值都超过40%，则自动打三次堆栈

date=`date "+%F %T"`
time=`date +%Y%m%d-%H%M%S`
host=`hostname`
data=iowait.data
log=iowait.log
cd `dirname $0`

# 获取当前iowiat使用百分比，并记录
#io=`iostat -c | grep -A 1 "%iowait" | awk '{print $(NF-2)}' | tail -1`
#io=`sar 1 1 | grep -A 1 "%iowait" | awk '{print $(NF-2)}' | tail -1`
io=`sar 5 10 | grep "Average" | awk '{print $(NF-2)}'`

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

# 判断io使用百分比是否大于40，如果大于40，则判断前两分钟io是否也大于40
if [[ $(echo "$io > 40" | bc) = 1 ]]
then
	echo "$date iowait : $io" >> $log
	io1=`tail -2 $data | head -1 | awk '{print $(NF)}'`
	io2=`tail -3 $data | head -1 | awk '{print $(NF)}'`
	# 判断前两分钟io是否也大于40，都大于40则自动打三次堆栈，并记录日志，有一个不大于则退出
	if [ $(echo "$io1 > 40" | bc) = 1 ] && [ $(echo "$io2 > 40" | bc) = 1 ]
	then
		echo -e "\nThe iowait alarm has been violated , and it starts to stack automatically !" >> $log
		if JSTACK
		then
			echo -e "Stack done !\n\n" >> $log
		else
			echo -e "Stack failed ! ! !\n\n" >> $log
		fi
	# 有一个不大于则退出
	else
		echo "Not triggered !" >> $log
	fi
fi

#!/bin/bash
# shell脚本多进程并发功能脚本(脚本功能介绍)
# 多进程并发执行，使用 "xargs -P" 命令控制并发数(并行可控)

TASK()
{
	seq 10 | xargs -i -P 3 bash -c "echo {}; sleep 1"
}

echo -e "\nStart time : `date '+%F %T'`\n"
t1=`date +%s`

TASK

echo -e "\nEnd time : `date '+%F %T'`\n"
t2=`date +%s`
time=$[$t2-$t1]
echo -e "The process cost time ${time}s\n"

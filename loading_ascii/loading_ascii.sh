#!/bin/bash
# 逐行加载 ASCII 艺术字文件

cd `dirname $0`  # 切换到脚本所在目录

logo=files/$1  # 需要加载的 ASCII 艺术字文件
wait_time=0.1  # 加载每行的等待时间

if [ $logo ] && [ -f $logo ]; then
    line=`wc -l $logo | awk '{print $1}'`
    for i in `seq 1 $line`; do
        sed -n "${i}p" $logo  # 逐行打印
        sleep $wait_time
    done
fi

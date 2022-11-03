#!/bin/bash
# 计时器(脚本功能介绍)
# Timer(script function introduction)

s=0
while true
do
	echo $s s
	let s++
	sleep 1
done

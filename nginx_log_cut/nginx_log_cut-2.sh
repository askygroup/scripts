#!/bin/bash
# nginx日志切割转存，备份日志，重新生成新的日志，清理旧的日志备份(脚本功能介绍)

# 日志类型和路径
logs_type=(access error)
logs_path=/home/nginx/logs/

# 备份的日志日期：date=yyyymmddhh
# date=$(date -d "yesterday" +%Y%m%d)  # 一天切割一次
date=$(date -d "-1 hour" +%Y%m%d%H)  # 一小时切割一次

CUT()
{
    # 日志切割转存
    cd $logs_path
    for type in ${logs_type[@]}; do
        mv ${type}.log ${type}_${date}.log
    done
    # 重新加载nginx
    # /home/nginx/openresty/nginx/sbin/nginx -s reload
    # /usr/local/nginx/sbin/nginx -s reload
    # pid=`cat /usr/local/nginx/logs/nginx.pid`
    pid=`cat /home/nginx/openresty/nginx/logs/nginx.pid`
    # kill -USR1 $pid
    kill -10 $pid
    echo -e "\n##### $date cut sucessful !"
}

CLEAN()
{
    # 清理旧的日志备份
    echo "start cleanning up old logs"
    for type in ${logs_type[@]}; do
        # for log in `find $logs_path -type f -name "${type}_??????????.log" -ctime +3`; do
        for log in `find $logs_path -type f -name "${type}_??????????.log" -mmin +360`; do
            echo "$log cleaned"
        done
        # find $logs_path -type f -name "${type}_??????????.log" -ctime +3 | xargs -i rm -rf {}
        find $logs_path -type f -name "${type}_??????????.log" -mmin +360 -delete
        echo "old ${type}.log cleanup completed !"
    done
}

CUT
CLEAN

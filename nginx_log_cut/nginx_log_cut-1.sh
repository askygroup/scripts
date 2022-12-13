#!/bin/bash
# nginx日志切割转存，备份日志，重新生成新的日志，清理旧的日志备份(脚本功能介绍)

# 日志路径
logs_path=/home/nginx/logs/

# 备份的日志日期：date=yyyymmddhh
# date=$(date -d "yesterday" +%Y%m%d)  # 一天切割一次
date=$(date -d "-1 hour" +%Y%m%d%H)  # 一小时切割一次

# 日志切割转存
cd $logs_path
mv access.log access_${date}.log
mv error.log error_${date}.log
# 重新加载nginx
# /home/nginx/openresty/nginx/sbin/nginx -s reload
# /usr/local/nginx/sbin/nginx -s reload
# pid=`cat /usr/local/nginx/logs/nginx.pid`
pid=`cat /home/nginx/openresty/nginx/logs/nginx.pid`
# kill -USR1 $pid
kill -10 $pid
echo -e "\n##### $date cut sucessful !"

# 清理旧的日志备份
find $logs_path -type f -name "access_??????????.log" -mmin +360
# find $logs_path -type f -name "access_??????????.log" -mmin +360 | xargs -i rm -rf {}
find $logs_path -type f -name "access_??????????.log" -mmin +360 -delete
echo "access.log cleanup completed !"
find $logs_path -type f -name "error_??????????.log" -ctime +3
find $logs_path -type f -name "error_??????????.log" -ctime +3 -delete
echo "error.log cleanup completed !"

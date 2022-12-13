# nginx日志切割脚本
nginx日志切割脚本


---


#### 脚本迭代记录

##### nginx_log_cut.sh

|脚本迭代版本|描述|
|---|---|
|nginx_log_cut-1.sh|nginx日志切割脚本，可以按日或者按小时切割|
|nginx_log_cut-2.sh|nginx日志切割脚本，可以按日或者按小时切割，代码优化|
|||


---


#### 使用说明

在 nginx 主机上添加计划任务，即可实现日志割接

按日切割：

0 1 * * * /bin/bash /home/nginx/cut_hour.sh >> /home/nginx/cut_hour.log &> /dev/null

按小时切割：

10 * * * * /bin/bash /home/nginx/cut_hour.sh >> /home/nginx/cut_hour.log &> /dev/null


---


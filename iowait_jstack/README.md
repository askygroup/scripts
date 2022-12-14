# iowait告警自动打堆栈
iowait告警自动打堆栈


---


#### 脚本迭代记录

##### nginx_log_cut.sh

|脚本迭代版本|描述|
|---|---|
|iowait-1.sh|iowait告警自动打堆栈|
|iowait-2.sh|iowait告警自动打堆栈，阀值修改为35%，优化数据采集准确性，增加日志切割，增加自动清理日志和jstack文件|
|||


---


#### 使用说明

在主机上添加计划任务，即可实现iowait告警自动打堆栈

```sh
* * * * * /bin/bash /home/nginx/cut_hour.sh >> /home/nginx/cut_hour.log &> /dev/null
```

---


# 多任务（多进程多线程）
多任务，使用多线程或多进程执行任务


---


#### 脚本迭代记录

##### multi_tasking.sh

|脚本迭代版本|描述|
|---|---|
|multi_tasking-1.sh|单进程顺序执行（串行）|
|multi_tasking-2.sh|多进程并发执行，全量并发（并行）|
|multi_tasking-2-1.sh|多进程并发执行，使用两层循环控制并发数（并行可控）|
|multi_tasking-3.sh|多进程并发执行，并发数可控（并行可控）|
|multi_tasking-4.sh|多进程并发执行，使用 "xargs -P" 命令控制并发数（并行可控）|
|||

##### multi_threading.py

|脚本迭代版本|描述|
|---|---|
|multi_threading-1.py|多线程并发执行，使用 threading 模块，全量并发（并行）|
|multi_threading-1-1.py|多线程并发执行，使用 threading 模块，使用两层循环控制并发数（并行可控）|
|multi_threading-2.py|多线程并发执行，使用 threading 模块，使用信号量控制并发数，并发数可控（并行可控）|
|||

python多进程后续慢慢补充吧！


---


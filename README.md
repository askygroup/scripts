# scripts
脚本仓库


---


#### 文件结构

|功能|脚本|描述|状态|
|---|---|:---:|:---:|
|:loudspeaker: 状态说明：|||:no_entry: :x: :heavy_check_mark:|
|:pushpin:||||
|[template_file]|---|模板文件|:o:|
|[test]|---|测试文件|:bug:|
|||||
|:pushpin:||||
|date_and_time|[timer]|计时器|:heavy_check_mark:|
|date_and_time|[report_time]|整点报时器|:heavy_check_mark:|
|date_and_time|[count_down]|倒计时|:heavy_check_mark:|
|date_and_time|[date_count]|日期相关计算|:heavy_check_mark:|
|date_and_time|[birthday_count]|生日相关计算|:heavy_check_mark:|
|:pushpin:||||
|[multi_tasking]|---|多任务（多进程多线程）|:heavy_check_mark:|
|[what_to_eat]|---|吃啥|:x:|
|[loading_ascii]|---|逐行加载 ASCII 艺术字文件|:heavy_check_mark:|
|[query_ip_geolocation]|---|查询IP属地信息|:heavy_check_mark:|
||||施工中 :no_entry:|
|||||

[template_file]: ./template_file
[test]: ./test
[timer]: ./date_and_time/timer
[report_time]: ./date_and_time/report_time
[count_down]: ./date_and_time/count_down
[date_count]: ./date_and_time/date_count
[birthday_count]: ./date_and_time/birthday_count
[multi_tasking]: ./multi_tasking
[what_to_eat]: ./what_to_eat
[loading_ascii]: ./loading_ascii
[query_ip_geolocation]: ./query_ip_geolocation


---


#### 文件存放规范

##### 目录（文件夹）：

1. 按功能类型区分（未确定类型的，可以先放着在“项目根目录”内）
    1. 一类功能一个目录（大类）
    2. 一种功能一个子目录（子类）

##### 文件：

1. 必要的说明性文件

    - 每个目录中必须有一个说明性文件 "README.md" ，文件内容包括：

      1. 当前目录下，文件功能介绍，脚本的功能，其他文件作用

      2. 每个脚本迭代纪录信息，新增了什么功能，优化了什么方式，修改了什么内容

      3. 脚本的思路和逻辑(可选)

2. 脚本版本命名

    - 每次的版本迭代，脚本都需要保留：

      1. 版本：name-1.*

      2. 子版本：name-1-1.*

##### 模板文件：

详见：
[:link: 模板文件](https://github.com/askygroup/scripts/tree/master/template_file "脚本相关模板文件")


---


# scripts
脚本仓库



#### 文件

| 功能   | 脚本       | 描述           |
| ------ | ---------- | -------------- |
| test   | test       | 测试           |
| 时间类 | 整点报时器 | 整点倒计时报时 |
| 时间类 | 生日计算   | 生日相关计算   |
|        |            |                |



#### 文件存放规范

##### 目录：

​	1、按功能区分，一类功能一个目录，一种功能一个子目录

##### 文件：

​	1、必要的说明性文件

​		每个目录中必须有一个说明性文件 "README.md" ，文件内容包括：

​		1）当前目录下，文件功能介绍，脚本的功能，其他文件作用

​		2）每个脚本迭代纪录信息，新增了什么功能，优化了什么方式，修改了什么内容

​		3）脚本的逻辑思路(可选)

​	2、脚本版本命名

​		每次的版本迭代，脚本都需要保留：

​		1）版本：name-1.*

​		2）子版本：name-1-1.*



##### 脚本模板：

​	1、Shell脚本模板，*.sh

```sh
#!/usr/bin/env bash
# 脚本功能介绍
# 依赖信息(可选)
# 编辑时间，编辑人信息等(可选)

# 定义变量
var_name="value"

# 函数
# function function_name()
function_name()
{
    # 函数功能
    # 代码
    echo $var_name
}

# 调用函数
function_name

```

​	2、Python脚本模板，*.py

```python
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 脚本功能介绍
# 依赖信息(可选)
# 编辑时间，编辑人信息等(可选)

# 导入库
import sys

# 定义变量
var_name = "value"


# 类
class ClassName(var):
	# 类功能
	def __init__(self, var):
		self.var = var
		print(self.var)


# 调用类
ClassName(var_name)


# 函数
def function_name(var):
	# 函数功能
	# 代码
	print(var)


# 调用函数
function_name(var_name)

```


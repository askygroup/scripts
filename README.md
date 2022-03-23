# scripts
脚本库



#### 脚本存放规范

##### 目录：

​	1、按功能区分，一类功能一个文件夹，一种功能一个子文件夹

##### 文件：

​	1、文件说明.txt

​		每个目录中必须有一个说明性文件，文件内容包括：

​		1）当前目录下，文件功能介绍，脚本的功能，其他文件作用

​		2）每个脚本迭代纪录信息，新增了什么功能，优化了什么方式，修改了什么内容

​		3）部分脚本的逻辑思路

​	2、脚本版本命名

​		每次的版本迭代，脚本都需要保留

​		1）版本：name-1.sh name-1.py

​		2）子版本：name-1-1.sh name-1-1.py

​	3、*.sh，Shell脚本规范

​		1）

```sh
#！/bin/bash
# 脚本功能介绍
# 依赖信息(可选)
# 编辑时间，编辑人信息等(可选)

# 定义变量
name="asky"

# 函数
# 代码

# 调用函数

```

​	4、*.py，Python脚本规范

​		1）

```python
#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# 脚本功能介绍
# 依赖信息(可选)
# 编辑时间，编辑人信息等(可选)

# 导入库
import sys

# 定义变量
name = "aksy"

# 类
# 函数
# 代码

# 调用类、函数

```


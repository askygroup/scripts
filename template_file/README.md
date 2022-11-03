# 模板文件
模板文件


---


##### 脚本模板：

    可直接复制使用：

    Shell_template.sh
    Python_template.py
    README_template.md

###### 1、Shell脚本模板，*.sh

```sh
#!/usr/bin/env bash
# 脚本功能介绍
# 依赖信息(可选)
# 编辑时间，编辑人信息等(可选)

# 定义变量(variable)
var_name="var_value"

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

###### 2、Python脚本模板，*.py

```python
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 脚本功能介绍
# 依赖信息(可选)
# 编辑时间，编辑人信息等(可选)

# 导入库
import sys

# 定义变量
var_name = "var_value"


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


---


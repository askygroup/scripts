#!/bin/bash
# Shell 脚本模板
# 无特殊依赖、无配置文件
# 2022-11-02 asky

# 切换到脚本所在目录
script_dir=`dirname $0`  # 脚本所在目录
echo "script_dir=$script_dir"
cd $script_dir  # 切换到脚本所在目录
current_dir=`pwd`  # 当前所在目录
echo "current_dir=$current_dir"

#範例指令稿16-12.sh  格式控制碼簡單使用
#! /bin/bash

echo 背景色變成紅色
echo  -e "\033[41mhello\033[0m"

echo 前景色變成黃色
echo  -e "\033[32mhello\033[0m"

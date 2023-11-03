#範例指令稿16-10.sh  使用格式控制碼
#! /bin/bash

echo 使用斜體顯示
echo  -e "\033[3mhello"
echo  this is control_test

echo 使用下劃線
echo  -e "\033[4mhello"
echo  this is control_test

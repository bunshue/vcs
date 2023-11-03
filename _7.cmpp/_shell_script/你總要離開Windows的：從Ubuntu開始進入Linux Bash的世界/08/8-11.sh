#範例指令稿16-11.sh  使用格式控制碼
#! /bin/bash

echo 使用下劃線
echo  -e "\033[4mhello"

echo 還原預設設定
echo -e "\033[0m"
echo  this is control_test

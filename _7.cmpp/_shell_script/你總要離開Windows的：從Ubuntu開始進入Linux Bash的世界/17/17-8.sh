#案例指令稿17-8.sh   工作的移除
#! /bin/bash

echo顯示設定的工作
at -l
echo

echo 移除工作號為3的工作
atrm 3 
echo

echo重新顯示設定的工作
at -l

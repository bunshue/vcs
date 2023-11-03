#案例指令稿17-9.sh   atq指令的使用
#! /bin/bash

echo顯示設定的工作
atq
echo

echo 顯示a佇列中的工作
atq -q a
echo

echo 顯示b佇列中的工作
atq -q b

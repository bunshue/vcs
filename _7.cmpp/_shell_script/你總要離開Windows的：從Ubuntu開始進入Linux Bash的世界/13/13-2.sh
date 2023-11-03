#範例指令稿13-2.sh  sed位址範圍符號的使用
#! /bin/bash

echo 移除第2行到尾端的所有內容
sed '3,$d'  data1.txt
echo

echo 移除第2行到第3行的內容
sed '2,3d'  date1.txt
echo

echo 不使用位址範圍符號
sed 'd' date1.txt

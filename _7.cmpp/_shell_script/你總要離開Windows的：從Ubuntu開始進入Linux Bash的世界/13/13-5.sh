#範例指令稿13-5.sh  移除指令的使用
#! /bin/bash

echo 移除is所在行
sed '/is/d' data.txt
echo

echo 移除is a所在行
sed '/is/d' data.txt
echo

echo 檢視檔案data.txt的內容
cat data.txt

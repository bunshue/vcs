#範例指令稿13-1.sh  sed常用選項的使用
#! /bin/bash

echo 取消預設輸出
sed -n '/a/p' data.txt
echo

echo 使用預設輸出
sed  '/a/p' data.txt

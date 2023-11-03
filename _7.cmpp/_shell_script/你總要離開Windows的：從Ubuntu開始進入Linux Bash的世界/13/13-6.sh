#範例指令稿13-6.sh  文字加入和置換
#! /bin/bash

echo 在第2行後面追加一行
sed '3a\this is add line ' data.txt
echo

echo在第2行前面追加一行
sed '3i\this is add line ' data.txt
echo

echo 置換第2行
sed '3c\this is add line ' data.txt

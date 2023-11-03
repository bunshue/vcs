#範例指令稿14-17.sh  字串處理函數在gawk中的使用
#! /bin/bash

echo 取得字元h在第一個字段中的位置
gawk '{print index($1,"h") }' str.txt
echo

echo 取得長度
gawk '{print length($0) }' str.txt
echo

echo將字元轉為大寫字元
gawk '{print toupper($2)}' str.txt

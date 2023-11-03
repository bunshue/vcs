#範例指令稿14-16.sh  數學函數在gawk中的使用
#! /bin/bash

echo 使用取整函數
gawk '{num=int($1); print num }' data4.txt
echo

echo 使用取平方根函數
gawk '{num=sqrt($1);print num}' data4.txt
echo

echo 使用取對數函數
gawk '{num=log ($1);print num}' data4.txt

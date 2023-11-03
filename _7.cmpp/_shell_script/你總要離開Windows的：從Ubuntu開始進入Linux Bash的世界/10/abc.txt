#範例指令稿10-10.sh  bc工具的使用
#! /bin/bash

echo -n 輸入一個浮點數：
read num

echo 計算浮點數的次方運算
echo "$num^2" |bc

echo 改為二進位顯示
echo “obase=2;$num" |bc

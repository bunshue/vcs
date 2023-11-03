#範例指令稿7-7.sh使用test指令判斷數值是否相等
#! /bin/bash

num1=3
num2=5
num3=5
echo 判斷兩個數是否相等
test  $num1  -eq  $num2
echo "$num1 = $num2 :$?"
echo

echo 判斷兩個數的大小
test  $num3  -le  $num2
echo "$num3 = $num2 :$?"
echo

test  $num3  -lt  $num2
echo "$num3  -lt $num2 :$?"

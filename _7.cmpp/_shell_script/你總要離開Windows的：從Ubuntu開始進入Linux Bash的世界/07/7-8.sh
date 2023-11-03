#範例指令稿7-8.sh復合測試條件的使用
#! /bin/bash

num1=3
num2=5
num3=5

echo 使用邏輯或運算符
test $num1 -ge $num2 -o $num3 -eq $num2
echo "邏輯或運算運算結果:$?"
echo

echo 使用邏輯與運算符
test $num1 -ge $num2 -a $num3 -eq $num2
echo "邏輯與運算運算結果:$?"


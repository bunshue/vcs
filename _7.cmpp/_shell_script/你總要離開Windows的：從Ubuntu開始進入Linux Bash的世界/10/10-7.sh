#範例指令稿10-7.sh  算術運算的預設處理模式
#! /bin/bash

echo 使用預設儲存模式進行算術運算
echo 輸入加數：
read  num1

echo 輸入另外一個加數：
read  num2

sum=$num1+$num2
echo 算術運算的結果為$sum

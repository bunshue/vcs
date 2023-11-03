#範例指令稿10-9.sh  指令(())的使用
#! /bin/bash

echo 使用符號(())進行算術運算
echo 輸入加數：
read  num1

echo 輸入另外一個加數：
read num2

echo 算術運算的結果為$((num1+num2))

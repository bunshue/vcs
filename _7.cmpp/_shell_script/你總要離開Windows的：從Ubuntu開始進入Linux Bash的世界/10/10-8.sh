#範例指令稿10-8.sh  let指令的使用
#! /bin/bash

echo使用指令let進行算術運算
echo輸入加數：
read  num1

echo輸入另外一個加數：
read num2

let sum=num1+num2
echo 算術運算的結果為$sum

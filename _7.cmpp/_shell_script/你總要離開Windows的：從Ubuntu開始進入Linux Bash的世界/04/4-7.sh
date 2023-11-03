#範例指令稿4-7.sh  使用-n選項限定輸入字元個數
#! /bin/bash

echo "使用-n選項限定輸入字元個數"
read -n4  num1					#限定為4個字元
echo "num1 = "$num1
echo "不限定字元個數，輸入10個字元"
read num1						#不限定時間輸入
echo  "num1 = "$num1				

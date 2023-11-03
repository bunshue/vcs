#範例指令稿4-6.sh  使用-t選項限定等待時間
#! /bin/bash

echo "設定等待時間為4秒"
read -t4  num1					#限定等待時間為4秒
echo "num1 = "$num1
echo "不限定時間輸入"
read num1						#不限定時間輸入
echo  "num1 = "$num1	

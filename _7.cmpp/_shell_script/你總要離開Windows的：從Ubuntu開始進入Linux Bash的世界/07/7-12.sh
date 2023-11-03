#範例指令稿7-12.sh  指令“[]”在if-then-else結構中的使用
#! /bin/bash

echo 使用[] 指令置換test進行邏輯判斷
echo 判斷3是否小於5
if [ 3 -le 5 ]
then 
 	echo 3 小於 5
else
	echo 3 大於 5
fi
 
echo 判斷5是否小於3
if [ 5 -le 3 ]
then 
	echo 5 小於 3
else
	echo 5 大於 3
fi

#範例指令稿7-13.sh  指令“[]”在if-then-else結構中的使用
#! /bin/bash

echo if-then結構的嵌套使用
echo 判斷3和5的關系
if [ 3 -le 5 ]
then 
	if [ 3 -eq 5 ]
	then
		echo 3 等於 5
	fi
	
	if [ 3 -ge 5 ]
	then
		echo 3 大於 5
	fi
echo 3 小於 5
fi

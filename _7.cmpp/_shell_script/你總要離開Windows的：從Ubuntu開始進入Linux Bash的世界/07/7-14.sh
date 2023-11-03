#範例指令稿7-14.sh  if-elif-else結構的使用
#! /bin/bash

echo if-then結構的嵌套使用
echo 判斷3和5的關系
if [ 3 -le 5 ]
then 
   echo 3小於5
elif [ 3 -eq 5 ]
then
   echo 3等於5
else
    echo 3大於5
fi

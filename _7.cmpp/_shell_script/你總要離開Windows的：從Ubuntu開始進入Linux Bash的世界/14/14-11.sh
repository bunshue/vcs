#範例指令稿14-11.sh  if else結構的使用
#! /bin/bash

echo if結構在gawk中的使用
gawk '{if ($1 > $2) {print $1 "大於" $2} 
else {print $1 "不大於" $2}}'
 data.txt

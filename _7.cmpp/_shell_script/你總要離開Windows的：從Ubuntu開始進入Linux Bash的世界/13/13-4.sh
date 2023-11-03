#範例指令稿13-4.sh  置換標示的使用
#! /bin/bash

echo 置換第2個is
sed 's/is/sed/2'  data.txt
echo

echo 置換全部的is
sed 's/is/sed/g'  data.txt


#範例指令稿13-10.sh  重新導向sed輸出
#! /bin/bash

echo 置換this不使用重新導向
sed ‘s/this/sed  data.txt
echo

echo 使用重新導向
NewResult=`sed ‘s/this/sed  data.txt`
echo $NewResult

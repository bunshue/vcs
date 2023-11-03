#範例指令稿4-14.sh  $@和$*的區別
#! /bin/bash

echo 使用for結構處理變數$@
count=1
for tmpstr in "$@" 
do
   echo 第$count個變數的值為：$tmpstr
   count=$[ $count + 1 ]
done
echo

echo使用for結構處理變數$*

count=1
for tmpstr in "$*" 
do
   echo 第$count個變數的值為：$tmpstr
   count=$[ $count + 1 ]
done

#範例指令稿13-3.sh  置換指令的使用
#! /bin/bash

echo 'sed置換指令的基本使用’
echo 置換this
sed 's/this/sed'  data.txt
echo

echo 置換is
sed 's/is/sed'  data.txt

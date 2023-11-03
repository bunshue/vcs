#案例指令稿14-4.sh   變更分隔符
#! /bin/bash

echo 指定分隔符為字元a
echo  this is a gawk program
gawk  -Fa '{print $1}' 14-4.sh
echo

echo 指定分隔符為字元c
gawk  -Fc '{print $1}' 14-4.sh

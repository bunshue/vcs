#範例指令稿11-9.sh  模式出現機率的使用
#! /bin/bash

echo 比對字元b至少出現2次
grep "b\{2\}"  11-9.sh  
echo

echo 比對字元c出現1-2次
grep "c\{1,2\}"  11-9.sh

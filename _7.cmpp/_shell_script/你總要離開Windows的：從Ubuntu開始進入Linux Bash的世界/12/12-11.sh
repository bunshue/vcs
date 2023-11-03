#範例指令稿12-11.sh  模式出現機率的使用
#! /bin/bash

#hello
#HEllo
#helloHELlo

echo 比對字元l至少出現2次
grep "l\{2\}"  12-11.sh  
echo
echo 比對字元l出現1-2次
grep "l\{1,2\}"  12-11.sh

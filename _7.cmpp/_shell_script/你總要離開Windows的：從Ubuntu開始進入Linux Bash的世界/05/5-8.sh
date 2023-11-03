#範例指令稿5-8.sh 比對出現頻率
#! /bin/bash

mkdir hello  Hello   HELLO   HEllo   HELlo   helloHELlo
echo "比對字元l至少出現2次"
ls | grep l\{2\}                 #至少出現2次l
echo

echo "比對字元l出現1-2次"
ls  | grep l\{1,2\}”                  #比對字元l出現1-2次

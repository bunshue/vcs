#範例指令稿5-6.sh 範圍比對的使用
#! /bin/bash

echo 使用中括號表示範圍
mkdir hao123abc  hao145acd  hao124def   hao345cef   hao345gef
echo 顯示"hao[1-3]*
ls | grep hao[1-3]*

echo 顯示"hao[1-2][2-3][3-4]*"
ls | grep hao[1-2][2-3][3-4]*

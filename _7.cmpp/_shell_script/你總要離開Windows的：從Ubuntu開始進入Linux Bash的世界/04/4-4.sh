#範例指令稿4-4.sh  不指定變數名輸入資料，使其儲存在環境變數$REPLY中
#! /bin/bash

echo "指定變數num"
read num			#指定變數num接收數值
echo '$num='$num
echo "未指定變數"
read  			#不指定變數名，使資料儲存在環境變數$REPLY中
echo '$num='$num
echo '$REPLY'=$REPLY

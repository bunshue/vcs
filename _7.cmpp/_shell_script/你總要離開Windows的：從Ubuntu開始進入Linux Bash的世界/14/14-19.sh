#範例指令稿14-19.sh  strftime函數的使用
#! /bin/bash

echo 使用函數strftime輸出到目前時間
echo | gawk '{print strftime("%D",systime())}'
echo | gawk '{print strftime("%e",systime())}'
echo | gawk '{print strftime("%w",systime())}'

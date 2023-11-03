#範例指令稿13-9.sh  反向指令
#! /bin/bash

echo 輸出沒有a的行
sed -n '/a/!p' data.txt 

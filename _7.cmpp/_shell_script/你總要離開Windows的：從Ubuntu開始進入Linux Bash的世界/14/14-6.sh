#範例指令稿14-6.sh   使用內建變數
#! /bin/bash

echo 顯示檔名
gawk 'NR==1 { print FILENAME }' 14-6.sh
echo

echo 顯示目前記錄中的字段數
gawk '{print NF}' 14-6.sh

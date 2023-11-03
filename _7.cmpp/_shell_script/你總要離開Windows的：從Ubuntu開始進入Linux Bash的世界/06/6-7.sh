#範例指令稿6-7.sh 輸入重新導向符
#! /bin/bash

echo 顯示data.txt中的內容
cat data.txt
echo
echo 顯示data.txt中的行數
wc -l < data.txt

echo 顯示data.txt中的字元數
wc -c < data.txt

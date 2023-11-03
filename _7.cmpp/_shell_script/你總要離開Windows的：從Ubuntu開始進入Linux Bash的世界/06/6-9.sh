#範例指令稿6-9.sh 追加輸出重新導向符
#! /bin/bash

echo 顯示資料檔data.txt中的內容
cat data.txt
echo

echo 使用輸出重新導向符並且顯示重新導向後的檔案內容
cat data.txt > data_bak.txt
cat data_bak.txt

echo 使用追加模式進行重新導向符並且顯示重新導向後的檔案內容
cat data.txt >> data_bak.txt
cat data_bak.txt

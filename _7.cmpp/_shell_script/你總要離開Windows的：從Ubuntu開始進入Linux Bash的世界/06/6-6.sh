#範例指令稿6-6.sh重新導向符簡單使用
#! /bin/bash

echo '使用ls指令顯示目錄/home中部分的內容'
ls -l /home

echo 'home重新導向ls指令顯示的目錄/home中部分的內容'
ls -l /home  1>home.txt           

echo 顯示重新導向檔案home.txt中的內容
cat home.txt

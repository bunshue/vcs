#範例指令稿6-10.sh合並標准輸出和標准錯誤

#! /bin/bash

echo 合並標准輸出和標准錯誤
ls /home no_exist
ls /home no_exist 1>log.txt
ls /home no_exist 2>log.txt
ls /home no_exist &>log.txt

echo 顯示重新導向檔案的內容
cat log.txt

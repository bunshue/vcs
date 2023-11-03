#範例指令稿12-16.sh  目錄的搜尋使用案例
#! /bin/bash

echo 在目前目錄檔案中查詢檔案12-16.sh
ls -l | grep 12-16.sh
echo

echo '目前檔案中查詢grep字元'
ls -l | grep 12-16.sh |grep "grep"

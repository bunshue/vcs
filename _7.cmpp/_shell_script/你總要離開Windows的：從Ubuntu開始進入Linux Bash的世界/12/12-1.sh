#範例指令稿12-1.sh  grep指令的使用
#! /bin/bash

echo "grep指令的簡單使用範例"
echo "在目前目錄中查詢檔案"
grep "12-1.sh"./
echo 找到檔案12-1.sh
echo "使用grep指令查詢不存在的檔案"
grep "no_exsit.txt" ./
echo 找不到不存在的檔案

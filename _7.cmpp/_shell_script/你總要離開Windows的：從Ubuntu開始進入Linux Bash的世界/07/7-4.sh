#範例指令稿7-4.sh使用test指令判斷檔案屬性
#! /bin/bash

file1=./7-4.sh

ls -l $file1
echo 判斷檔案是否具有讀取權限
test -r $file1
echo "test -r file1 :$?"

echo 判斷檔案是否具有寫入權限
test -w $file1
echo "test -w file1 :$?"

echo 判斷檔案是否具有可執行權限
test -x $file1
echo "test -x file1 :$?"

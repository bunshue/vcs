#範例指令稿7-3.sh使用test指令判斷檔案屬性
#! /bin/bash

file1=./7-3.sh
file2=/home
echo “使用-e選項判斷檔案是否存在“
test -e file1
echo "test -e $file1 :$?"
test -e file_noexist
echo "test -e file_noexist :$?"

echo “使用-f選項判斷檔案是否是普通檔案“
test -e $file1
echo "test -e $file1:$?"
test -e $file2
echo "test -e $file2 :$?"

echo “使用-d選項判斷檔案是否是目錄檔案”
test -d $file1
echo "test -d $file1 :$?"
test -d $file2
echo "test -d $file2:$?"

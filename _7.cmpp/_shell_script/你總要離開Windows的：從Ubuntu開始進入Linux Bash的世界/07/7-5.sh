#範例指令稿7-5.sh使用test指令判斷檔案新舊
#! /bin/bash

file1=/dev
file2=/dev;
file3=/tmp;

echo 使用-nt選項判斷檔案的新舊
test $file1 -nt $file3
echo "$file1 -nt $file3 :$?"
test $file3 -nt $file1
echo "$file1 -nt $file3 :$?"
echo

echo 使用-ot選項判斷檔案的新舊
test $file1 -ot $file3
echo "$file1 -ot $file3 :$?"
test $file3 -ot $file1
echo "$file1 -ot $file3 :$?"
echo

echo 使用-ef選項判斷檔案是否相同
test $file1 -ef $file2
echo "$file1 -ot $file3 :$?"
test $file2 -ef $file3
echo "$file1 -ot $file3 :$?"

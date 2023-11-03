#範例指令稿12-3.sh  grep指令中選項的使用
#! /bin/bash

echo '顯示比對hello的內容'
grep -E "hello" test.txt
echo 顯示比對的行數
grep -c "hello" test.txt
echo

echo '顯示Hello比對的內容'
grep -E "Hello" test.txt
echo 顯示比對的行數
grep -c "Hello" test.txt

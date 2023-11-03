#範例指令稿12-4.sh  grep指令中選項的使用
#! /bin/bash
#hello
#HELLO

echo 不使用-E選項不區分大小寫
echo 比對hello
grep *hello*  12-4.sh
echo

echo 比對HELLO
grep *HELLO* 12-4.sh
echo

echo 使用-E選項區分大小寫
echo 區分大小寫比對hello
grep -E *hello* 12-4.sh

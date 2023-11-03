#範例指令稿12-5.sh  grep指令中選項的使用
#! /bin/bash
#hello
#Hello
#HELLO
#123
#345

echo 顯示比對行
grep -E *hello*  12-5.sh
echo 使用-v選項顯示不符合行
grep -v *hello*  12-5.sh
grep -v *HELLO*  12-5.sh

echo 顯示開頭字元不是字母的資料
grep -v ^[a-zA-Z] 12-5.sh

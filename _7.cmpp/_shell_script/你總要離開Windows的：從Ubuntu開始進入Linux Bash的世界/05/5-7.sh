#範例指令稿5-7.sh 萬用字元的使用
#! /bin/bash

mkdir  hello123  Hello123   123hello   123HAO 
echo "使用脫字元比對開頭字元"
echo 比對開頭字元是小寫字元
ls | grep [^a-z] 
echo

echo 顯示開頭字元是大寫字元H
ls | grep [^H]

echo “使用美元符號比對結尾字元”
echo 顯示結尾字元是數字
ls  | grep [1-9$] 
echo

echo 顯示結尾字元是大寫字元
ls  | grep [A-Z$]

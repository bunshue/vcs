#範例指令稿9-4.sh  使用函數傳回值
#! /bin/bash

echo "傳回普通指令的傳回值"
ls /home
echo "正確執行指令ls後傳回值為：$?"
ls /no_exist
echo "錯誤執行指令ls後傳回值為：$?"

ls /no_exist
ls /home
echo "上一筆指令是正確執行指令ls後傳回值為：$?"

ls /home
ls /no_exist
echo "上一筆指令是錯誤執行指令ls後傳回值為：$?"

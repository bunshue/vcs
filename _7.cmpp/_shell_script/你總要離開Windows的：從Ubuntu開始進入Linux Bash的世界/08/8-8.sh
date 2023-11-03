#範例指令稿16-8.sh  使用格式控制碼
#! /bin/bash

echo 顯示輸入框
dialog --inputbox "請輸入訊息" 10 20 "hello world"

echo  輸入編輯框
dialog --editbox date.txt  12 30

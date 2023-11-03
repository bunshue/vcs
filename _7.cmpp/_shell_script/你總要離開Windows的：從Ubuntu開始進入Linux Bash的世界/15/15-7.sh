#範例指令稿15-7.sh  renice指令的使用
#! /bin/bash

echo 檢視執行緒訊息
ps -efl | grep 15-1.sh | grep -v grep
echo

echo 使用renice指令重設執行緒的優先級
 renice 16 -p 6009 
echo

echo 檢視執行緒訊息
ps -efl | grep 15-1.sh | grep -v grep

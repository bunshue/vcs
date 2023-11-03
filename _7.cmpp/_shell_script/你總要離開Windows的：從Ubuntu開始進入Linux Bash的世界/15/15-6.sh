#範例指令稿15-6.sh  nice指令的使用
#! /bin/bash

echo “設定執行緒的優先級”
nice -10 ./nice-test.sh &
echo

echo 檢視執行緒訊息
ps -efl | grep 15-1.sh | grep -v grep

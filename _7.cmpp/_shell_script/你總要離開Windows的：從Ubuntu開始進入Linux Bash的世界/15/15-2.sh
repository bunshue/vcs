#範例指令稿15-2.sh  使用鍵碟按鍵向指令稿傳送訊號
#!/bin/bash

echo 檢視執行緒是否存在
ps -ef | grep 15-1.sh |grep -v grep

echo 殺掉執行緒15-1.sh
ps -ef | grep 15-1.sh | awk ‘{print $4}’ | xargs kill -9

echo 檢視執行緒是否存在
ps -ef | grep 15-1.sh 

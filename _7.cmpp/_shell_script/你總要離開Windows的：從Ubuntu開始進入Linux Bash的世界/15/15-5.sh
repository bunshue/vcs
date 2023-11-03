#範例指令稿15-5.sh  nohup指令的使用
#!/bin/bash

echo  使用nohup指令執行15-3.sh
nohup ./15-3.sh &
echo

echo 使用背景執行符執行15-1.sh
./15-1.sh &
echo

echo 檢視執行緒
ps -ef  | grep 15-* | grep -v grep

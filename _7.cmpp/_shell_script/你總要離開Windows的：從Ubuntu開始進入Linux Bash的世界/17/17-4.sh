#範例指令稿17-4.sh  使用at指令建立計劃工作
#! /bin/bash

echo 使用12小時設定計劃工作
at -f 17-4.sh  4: 20PM  tomorrow
echo

at -f 17-4.sh  16:10  tomorrow
echo

echo 顯示設定的定時工作
at -l

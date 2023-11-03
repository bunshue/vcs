#範例指令稿17-3.sh  使用at指令建立計劃工作
#! /bin/bash

echo 使用at指令建立計劃工作
at  -f 17-3.sh now + 2 minutes
echo

echo 顯示設定的定時工作
at -l

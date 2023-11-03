#範例指令稿16-3.sh  dialog指令傳回值1
#! /bin/bash

echo  建立視窗，選取yes按鍵
dialog --yesno --title “提示框” “是否移除” 10 20
echo 傳回值是$?

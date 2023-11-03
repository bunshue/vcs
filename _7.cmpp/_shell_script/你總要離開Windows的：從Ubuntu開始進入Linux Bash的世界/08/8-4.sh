#範例指令稿16-4.sh  diallog指令傳回值2
#! /bin/bash

echo建立視窗，選取no按鍵
dialog --yesno --title “提示框” “是否移除” 10 20
echo 傳回值是$?

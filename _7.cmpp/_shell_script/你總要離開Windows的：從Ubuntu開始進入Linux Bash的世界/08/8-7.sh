#範例指令稿16-7.sh  yesno視窗預設按鈕
#! /bin/bash

echo 修改預設按鈕
dialog --title "是否儲存"   --defaultno --yesno "請確認是否儲存？" 10 20

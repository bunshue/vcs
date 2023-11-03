#範例指令稿5-2.sh 使用雙引號輸出特殊字元
#! /bin/bash

echo "不使用雙引號"
echo "輸出環境變數$HOME
echo $HOME                #輸出環境變數$HOME
echo "使用反斜線控制符"
echo a\tb\a\tc            	#用反斜線控制符
echo "輸入一個反斜線"        #輸入一個反斜線
echo \\

echo "使用雙引號輸出對應的符號"
echo "$HOME"
echo "a\tb\a\tc"
echo "\\"

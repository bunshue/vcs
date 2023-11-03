#範例指令稿14-8.sh  使用自訂變數
#! /bin/bash

echo 自訂變數
gawk  ' { FR="test"} { print FR} ' 14-8.sh

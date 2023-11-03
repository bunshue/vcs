#範例指令稿14-7.sh  修改內建變數的值
#! /bin/bash

echo 變更檔名
gawk ' { FILENAME ="14-5.sh"} { print FILENAME} '

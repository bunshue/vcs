#範例指令稿14-10.sh  if結構的簡單使用
#! /bin/bash

echo if結構在gawk中的使用
gawk '{if ($1 > $2) {print $1 "大於" $2} }' data.txt

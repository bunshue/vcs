#範例指令稿14-13.sh  while結構在gawk中的使用
#! /bin/bash

echo while結構在gawk中的使用
gawk '{i=1; sum=0;while(i <= NF) {i++; print $2}}' data2.txt

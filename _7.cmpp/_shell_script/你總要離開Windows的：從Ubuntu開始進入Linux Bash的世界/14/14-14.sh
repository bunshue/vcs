#範例指令稿14-14.sh  for結構在gawk中的使用
#! /bin/bash

echo  for結構在gawk中的使用
gawk '{
sum=0;
for(i = 1;i <= NF;i++)
 {print $1}
}'
 data2.txt

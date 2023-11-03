#範例指令稿14-15.sh  循環結構控制敘述結構在gawk中的使用
#! /bin/bash

echo 循環控制敘述在gawk中的使用
gawk '{
for(i = 1; i <= NF; i++)
{if($1 == 3) 
{continue;} 
if ($1 == 4){break;} 
print $1}
}' 
data3.txt

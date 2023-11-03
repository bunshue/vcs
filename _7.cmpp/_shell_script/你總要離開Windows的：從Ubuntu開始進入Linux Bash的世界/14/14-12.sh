#範例指令稿14-12.sh  if else結構的復雜使用
#! /bin/bash

echo if結構在gawk中的使用
gawk '{if ($1 > $2) {print $1 "大於" $2}
 else if($1 < $2) {print $1 "小於" $2}
 else {print $1 "等於" $2}}' data.txt

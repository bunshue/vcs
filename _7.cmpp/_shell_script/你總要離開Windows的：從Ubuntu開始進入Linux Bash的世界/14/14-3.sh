#範例指令稿14-3.sh  取得字段
#! /bin/bash

echo 顯示字段1
gawk  '{print $1}’ 14-3.sh
echo

echo 顯示字段2
gawk  '{print $2}' 14-3.sh

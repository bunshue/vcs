#範例指令稿14-18.sh  時間函數在gawk中的使用
#! /bin/bash

echo "使用systime()取得秒數"
echo | gawk '{print systime()}'
echo

echo "使用mktime ()取得秒數"
echo | gawk '{print mktime ("2014 03 28 14 12 12")}'

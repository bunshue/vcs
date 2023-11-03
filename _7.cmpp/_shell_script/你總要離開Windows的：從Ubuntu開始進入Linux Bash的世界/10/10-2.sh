#範例指令稿10-2.sh   使用函數進行注解
#! /bin/bash

echo 指令稿開始
echo使用函數進行注解
fun()
{
echo this # is 'is'

echo 在注解中使用雙引號
echo this # is "is"

echo 在注解中使用倒引號
echo this # `is`

echo 輸出一個井號
echo this \#
}
echo 不執行函數
echo 指令稿結束

#範例指令稿9-2.sh  使用未建立的函數
#! /bin/bash

echo "在shell指令稿中使用未建立的函數fun1"

fun1

function fun1
{
    echo "在呼叫函數fun1之後建立函數";
}

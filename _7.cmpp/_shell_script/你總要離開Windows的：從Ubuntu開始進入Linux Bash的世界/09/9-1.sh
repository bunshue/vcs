#範例指令稿9-1.sh  建立函數的基本模式
#! /bin/bash

echo "在shell指令稿中使用函數"
echo "使用指令function建立函數"
function fun1
{
    echo "使用指令function建立函數";
}

echo "呼叫函數fun1"
fun1

echo "不使用指令function建立函數"
function fun1
{
    echo "在函數fun2中";
}

echo "呼叫函數fun2"
fun2

#範例指令稿9-3.sh  使用函數參數
#! /bin/bash

echo "在函數fun中使用函數參數"
fun()
{
echo "傳入的參數的個數為：$#";
echo "函數名是：$0";
echo "第1個參數是：$1";
echo "第2個參數是：$2";
echo "第3個參數是：$3";
echo "第4個參數是：$4";
echo "第5個參數是：$5";

)

echo "呼叫函數，並傳遞5個參數"
fun 1 2 3 4 5
fun "hello" "world" "is" "the" "first" "shell script"

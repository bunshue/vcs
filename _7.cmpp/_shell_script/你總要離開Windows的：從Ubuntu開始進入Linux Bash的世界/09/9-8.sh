#範例指令稿9-8.sh  全局變數的使用
#! /bin/bash

echo "在函數中使用全局變數"
num=10
string=’hello world"
fun1()
{
    $num=$[ $num + 10]
    echo "全局變數string = $string"
}
fun1
echo "在函數fun1中變化以後，變數num的值為：$num"

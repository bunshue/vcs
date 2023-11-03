#範例指令稿9-9.sh  局部變數的使用
#! /bin/bash

echo "在函數中使用局部變數"
num=10
string="hello world"
fun1()
{
	local num=100
	local string="local value"
	echo "在函數fun1中呼叫取得的變數num的值為：$num"
	echo "在函數fun1中呼叫取得的變數string = $string"
	num=$[ $num + 100]
}

fun1
echo "在函數fun1外，變數num的值為 ： $num"
echo "在函數fun1外，變數string的值為 ： $string"

#範例指令稿9-10.sh  陣列作為函數參數
#! /bin/bash

echo "標準模式下使用陣列作為函數的參數"
num1=(1,2,3,4,5)
num1=(a,b,c,d,e)

fun1()
{
	local array1=($1)
echo 傳遞的陣列1中的數值分別為：${array1[*]}"

local array2=($2)
echo 傳遞的陣列2中的數值分別為：${array2[*]}"

}
fun1 "${num1[*]}"
echo

echo "向函數傳遞多個陣列作為參數"
fun2 "${num1[*]}""${num2[*]}"

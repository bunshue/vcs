#範例指令稿9-5.sh  函數預設傳回值
#! /bin/bash

echo "取得函數的預設傳回值"
fun1()
{
	echo "最後一條指令為執行正確的指令"
    echo "hello world"
}
fun1
echo "函數fun1的傳回值為：$?"
echo

fun2()
{
	echo "最後一條指令為執行錯誤的指令"
    ls /no_exist.sh

}
fun2
echo "函數fun2的傳回值為：$?"

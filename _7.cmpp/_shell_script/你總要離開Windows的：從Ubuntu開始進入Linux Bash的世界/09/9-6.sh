#範例指令稿9-6.sh  使用return傳回特定傳回值
#! /bin/bash

echo "使用return指令傳回函數的傳回值"
fun1()
{
	for (( num=1; num<10; num++ ))
{
	    if  [$num -eq 5]
         then
           return $num
         fi
}
}
fun1
echo "函數fun1的傳回值為：$?"
echo

fun2()
{
	echo "使用return指令傳回大於255的數值"
     return 256

}
fun2
echo "函數fun2的傳回值為：$?"

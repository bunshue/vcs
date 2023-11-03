#範例指令稿9-7.sh  使用函數的傳回值
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

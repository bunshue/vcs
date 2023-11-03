#範例指令稿9-13.sh  嵌套函數的使用

#! /bin/bash
echo "函數的嵌套使用案例"
fun1()
{
    echo "在函數fun1\(\)中"
}
fun2()
{
echo "在函數fun2\(\)中"
echo

echo "執行函數fun1\(\)"
     fun1

    }

echo "呼叫函數fun2\(\)"
fun2

#範例指令稿10-4.sh   使用管線案例
#! /bin/bash

fun1()
{
for ((i=0;i<10000;i++))
do
    echo hello world | tee -a data.txt
done
}
fun2()
{
  for ((i=0;i<10000;i++))
do
    echo hello world >> data.txt
done

}

echo 記錄函數fun1執行時間
time fun1
echo

echo 記錄函數fun2執行時間
time fun2

#範例指令稿7-15.sh  case結構的使用
#! /bin/bash

echo -n 輸入一個分數: 
read num

case $num in 
1) echo 輸入的數值為1;;
2) echo 輸入的數值為2;;
3) echo 輸入的數值為3;;
4) echo 輸入的數值為4;;
5) echo 輸入的數值為5;;
*) echo 輸入的數值大於5;;
esac
echo case結構執行結束

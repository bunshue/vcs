#範例指令稿10-6.sh   加入提示性訊息

#! /bin/bash   

echo  -n 輸入一個整數：
read num
echo輸入的整數是：$num

echo  -n 輸入一個整數：
read num2
echo num2
echo 兩個數相加的和為$(($num+$num2))

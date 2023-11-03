#範例指令稿4-9.sh  使用-n選項不輸出換行符
#! /bin/bash

echo "不使用-n選項輸出換行符"
echo "輸入數值："
read   num1	
echo  "輸入的數值為："$num1		

echo  "使用-n選項不輸出換行符"
echo  -n "輸入數值："
read   num1		
echo  "輸入的數值為："$num1		

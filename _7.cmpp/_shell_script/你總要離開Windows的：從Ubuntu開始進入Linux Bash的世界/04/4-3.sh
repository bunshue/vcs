#範例指令稿4-3.sh  變數的輸入和輸出
#! /bin/bash

echo -n 輸入變數的值： 
read num			#為變數num給予值為整數10
echo 變數的值為$num
echo

echo -n 輸入變數的值： 
read num 		#為變數num給予值為字串”10”
echo 變數的值為$num
echo

echo -n 輸入變數的值： 
read  num		#為變數num給予值浮點型數值1.2 
echo 變數的值為$num

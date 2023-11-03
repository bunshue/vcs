#範例指令稿4-8.sh  使用-s選項不顯示輸入的內容
#! /bin/bash

echo "使用-s選項不顯示輸入的內容"
read -s  num1						#不顯示輸入的內容
echo "num1 = "$num1
echo "標準顯示輸入內容"
read num1						#顯示輸入的內容
echo  "num1 = "$num1					

#範例指令稿10-5.sh   不加入提示性訊息

#! /bin/bash   
read num
echo num

read num2
echo num2
echo  $(( $num+$num2 ))

#範例指令稿14-9.sh  陣列的使用
#! /bin/bash

echo 使用數字作為陣列的索引
echo 輸出數值中的元素
gawk 'BEGIN{numarrary[1]="this";
			numarrary[2]="is";
			numarrary[3]="num";
			numarrary[4]="index"; 
{for(i in numarrary) print numarrary[i]}}'
echo

echo 使用字串作為陣列的索引
echo 輸出陣列中的元素
gawk 'BEGIN{strarrary ["first"]= "this";
			strarrary["second"]="is";
			strarrary["third"]="string";
			strarrary["four"]="index";
 {for(j in strarrary) print strarrary[j]}}'

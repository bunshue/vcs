#範例指令稿12-13.sh  國際模式比對的類別名的使用
#! /bin/bash

#hello123
#Hello123
#Hao123hao123
#HAO123HAOo123
#HELlo123

echo 使用國際模式比對的類別名
echo 比對開頭字元是大寫字元
grep "#[[:upper:]]" 12-13.sh
echo 

echo 比對開頭字元是H，後面必須是2個字元，然後是數字 
grep "H[[:alpha:]][[:alpha:]][[:digit:]]*" 12-13.sh   

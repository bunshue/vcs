#範例指令稿12-10.sh  字元的比對
#! /bin/bash

#hello
#Hello
#HELLO
#HEllo
#HELlo

echo 使用通配符點號比對一個字元
grep -E "#HE.lo"  12-10.sh
echo 

echo 使用通配符星號*比對0個字元或多個字元
echo '比對#H*'
grep -E "#H*" 12-10.sh 
echo
echo '比對*lo'
grep -E "*lo" 12-10.sh

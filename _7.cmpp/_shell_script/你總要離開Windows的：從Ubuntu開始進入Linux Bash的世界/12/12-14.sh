#範例指令稿12-14.sh  egrep指令的使用
#! /bin/bash

#hello123
#Hello123
#Hao123hao123
# HAO123HAOo123
#HELlo123

echo "egrep指令的使用案例"
echo "使用加號連線字串"
egrep 'h+[h, H]' 12-14.sh      
egrep '*+123*' 12-14.sh      
echo "使用grep指令實現相同的效果"
grep 'h[h, H]' 12-14.sh
egrep '*123*' 12-14.sh
echo "使用egrep指令比對任意字串"
egrep '(h|H)(a|A)o' 12-14.sh

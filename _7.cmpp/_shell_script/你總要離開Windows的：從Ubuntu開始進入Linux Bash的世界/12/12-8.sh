#範例指令稿12-8.sh  模式範圍以及範圍群組合的使用
#! /bin/bash

#hello123
#Hello123
#Hao123hao123
#HAO123HAOo123
#HELlo123

echo 使用模式範圍
echo '比對#[h,H]e[l,L]'
grep -E "#[h,H]e[l, L]*" 12-8.sh
echo
echo '比對[1-9][1-9].[A-Z]'
grep -E "*[1-9][1-9].[A-Z]*" 12-8.sh

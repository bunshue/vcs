#範例指令稿7-6.sh使用test指令處理字串
#! /bin/bash

str1="hello";
str2="Hello";
str_null="";
str3="hello";

echo 使用-n選項測試字串是否為空
echo 測試字串str1是否為空
test -n $str1
echo "test -n $str1:$?"
echo 測試字串str1是否為空
test -n $str2
echo "test -n $str2:$?"

echo 使用-z選項測試字串是否為空
test -z $str_null;
echo "test -z $str_null:$?"

echo 使用符號=判斷兩個字串是否相同
test $str1 = $str2;
echo "$str1 = $str2 :$?"
test $str1 = $str3;
echo "$str1 = $str3 :$?"
echo 使用符號!=判斷兩個字串是否相同
test $str1 != $str2;
echo "$str1 = $str2:$?"
test $str1 != $str3;
echo "$str1 = $str3 :$?"

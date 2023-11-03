#範例指令稿12-9.sh  定位符的使用
#! /bin/bash

echo 使用脫字元比對開頭字元
grep -E "[^a-z]" test.txt

echo 使用定位符比對空行
grep '^$' 12-9.sh

echo 使用美元符號比對結尾字元
grep "[1-9$].sh" 12-9.sh

#範例指令稿18-4.sh  插入敘述的基本使用
#! /bin/bash

UpdateSql="update Book_Info set Book_Num=10 where ISDN=001"
echo連線資料庫
mysql -u root -p binghehj

echo 插入記錄
mysql -e "${ UpdateSql }"

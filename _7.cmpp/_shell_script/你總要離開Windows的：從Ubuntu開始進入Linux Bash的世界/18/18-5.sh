#範例指令稿18-5.sh  移除敘述的基本使用
#! /bin/bash

DeleteSql="delete Book_Info  where ISDN=001"
echo連線資料庫
mysql -u root -p binghehj

echo 移除記錄
mysql -e "${ DeleteSql }"

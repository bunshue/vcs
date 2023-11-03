#範例指令稿18-1.sh  mysql的基本使用
#! /bin/bash

echo  連線資料庫
mysql -u root -p binghehj

echo 執行查詢敘述
mysql -e "select * from book_info"

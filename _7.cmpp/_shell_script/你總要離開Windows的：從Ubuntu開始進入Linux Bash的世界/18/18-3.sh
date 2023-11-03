#範例指令稿18-3.sh  插入敘述的基本使用
#! /bin/bash

InsertSql="INSERT INTO Book_Info
           (ISDN
           ,Book_Code
           ,Book_Name
           ,Book_Type
           ,Publish_Name
           ,Author_Name
           ,Book_Price
           ,Book_Quantity
           ,Book_Page
           ,Book_Num
	      ,Book_Desc
           ,Buy_Date)
     VALUES
           ('001'
           ,N'C++入門經典'
           ,N'教科書'
           ,N'清華大學出版社'
           ,N'黃靜'
           ,121.50
           ,2
           ,758
	   ,N'該書適合初學者，入門教學'
           ,'2014-01-22');"
echo連線資料庫
mysql -u root -p binghehj

echo 插入記錄
mysql -e "${InsertSql}"

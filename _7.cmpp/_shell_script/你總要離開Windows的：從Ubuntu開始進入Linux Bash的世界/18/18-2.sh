#範例指令稿18-2.sh  建表的基本使用
#! /bin/bash

CreateTableSql="create table BookInfo
{
    ISBN varchar(20) NOT NULL,
	Book_code nvarchar(100) NOT NULL,
	Book_Name nvarchar(100) ,
	Book_Type nvarchar(50) ,
	Publish_Name nvarchar(100) ,
	Author_Name nvarchar(100) ,
	Book_Price decimal(30, 2) ,
	Book_Quantity int ,
	Book_Page int ,
	Book_ Num  int ,
	Book_Desc nvarchar(max) ,
	Buy_Date date ,
    Is_User   Boolean,
	Create_Date datetime
}"

echo 連線資料庫
mysql -u root -p binghehj

echo 建立表
mysql -e "${CreateTableSql}"

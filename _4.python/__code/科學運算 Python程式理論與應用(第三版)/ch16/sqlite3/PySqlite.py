# -*- coding:utf-8 -*-
# file: PySqlite.py
#
import sqlite3											# 匯入sqlite3模組
con = sqlite3.connect('python')									# 連線到資料庫
cur = con.cursor()										# 獲得資料庫游標
cur.execute('insert into people (name,age,sex) values (\'Jee\',21,\'F\')')			# 執行SQL敘述
r = cur.execute('delete from people where age=20')						# 執行SQL敘述
con.commit()											# 傳送交易
cur.execute('select * from people')								# 執行SQL敘述
s = cur.fetchall()										# 獲得資料
print(s)												# 列印資料
cur.close()											# 關閉游標
con.close()											# 關閉資料庫連線

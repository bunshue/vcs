# -*- coding:utf-8 -*-
# file: PyMySQL.py
#

import MySQLdb											# 匯入MySQLdb模組
db = MySQLdb.connect(host='localhost',								# 連線到資料庫，伺服器為本機
		user='root',									# 使用者為root
		passwd='python',								# 密碼為python
		db='python')									# 資料庫名為python
cur = db.cursor()										# 獲得資料庫游標
cur.execute('insert into people (name,age,sex) values (\'Jee\',21,\'F\')')			# 執行SQL敘述
r = cur.execute('delete from people where age=20')						# 執行SQL敘述
r = cur.execute('select * from people')								# 執行SQL敘述
con.commit()											# 傳送交易
r = cur.fetchall()										# 取得資料
print r												# 輸出資料
cur.close()											# 關閉游標
db.close()											# 關閉資料庫連線

# -*- coding:utf-8 -*-
# file: PySqlite.py
#
import sqlite3											# 匯入sqlite3模組
con = sqlite3.connect('message')						# 連線到資料庫
cur = con.cursor()										# 獲得資料庫游標, 'GBK')
cur.execute('select * from message')								# 執行SQL敘述
results = cur.fetchall()										# 獲得資料
print('''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>use Python in ASP</title>
</head>
<body>
<center>
<h1>所有留言</h1>
</center>
<hr />
''')
for result in results:
	print( '姓名:', result[0])
	print( '<br>')
	print( '時間:', result[4])
	print( '<br>')
	print( '信箱:', result[1])
	print( '<br>')
	print( '網站', result[2])
	print( '<br>')
	print( '留言內容:')
	print( '<br>')
	print( result[3])
	print( '<hr />')
print('''
</body>
</html>
''')
cur.close()											# 關閉游標
con.close()											# 關閉資料庫連線

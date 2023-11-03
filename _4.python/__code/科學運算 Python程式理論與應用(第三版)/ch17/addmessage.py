# -*- coding:utf-8 -*-
# file: addmessage.py
#
import cgi
import sqlite3											# 匯入sqlite3模組
import datetime
form = cgi.FieldStorage()
name = form["name"].value
mail = form["email"].value
site = form["site"].value
content =form["content"].value
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d %H:%M:%S')
con = sqlite3.connect('message')									# 連線到資料庫
cur = con.cursor()										# 獲得資料庫游標
cur.execute("INSERT INTO message VALUES(?,?,?,?,?)", (name, mail, site, content, time))
con.commit()
# 執行SQL敘述
cur.close()											# 關閉游標
con.close()
print('''
<html>
<head>
<title>加入成功</title>
</head>
<body>
<h1>加入成功</h1>
<br>
<a href=show.py>點擊檢視留言</a>
</body>
</html>
''')

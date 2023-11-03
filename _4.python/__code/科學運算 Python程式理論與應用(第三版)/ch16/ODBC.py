# -*- coding:utf-8 -*-
# file: ODBC.py
#
import odbc										# 匯入odbc模組
con = odbc.odbc('podbc')								# 連線到資料庫，即在資料源名中填寫的名字
cursor = con.cursor()									# 建立cursor物件
cursor.execute('select id,name from people where id = 1')				# 執行SQL敘述查詢ID為1的記錄
r = cursor.fetchall()									# 獲得所有記錄
print(r)											# 輸出記錄
cursor.execute('insert into people (name,age,sex) values (\'Jee\',21,\'female\')')	# 加入記錄
cursor.execute('DELETE FROM people where id = 3')					# 移除ID為3的記錄
con.commit()										# 傳送交易
cursor.close()										# 關閉cursor
con.close()										# 關閉連線

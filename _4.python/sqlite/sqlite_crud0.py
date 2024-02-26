"""
sqlite基本範例 一個 基本款

簡易建立資料庫

增加(13)

刪除資料(1)
讀取全部資料
搜尋資料

刪除資料庫


原始資料 9 筆
	id_num	ename	cname	weight
第1筆 : 5	horse	馬	36
第2筆 : 1	mouse	鼠	3
第3筆 : 4	elephant象	100	(此筆資料錯誤, 應刪除)

第4筆 : 9	ox		48
第5筆 : 2	sheep		66	(此筆資料錯誤, 應為goat 29)

第6筆 : 8	snake		16	(詢問是否刪除此筆資料)
第7筆 : 3	tiger		33

第8筆 : 7	rabbit		8

第9筆 : 6	tiger		240

1. 建立資料庫
2. 新增資料 9筆
3. 修改2號的name
4. 刪除4號
5. 詢問是否刪除8號資料
6. 搜尋


SQLite Autoincrement（自動遞增）

SQLite 的 AUTOINCREMENT 是一個關鍵字，用于表中的字段值自動遞增。
我們可以在創建表時在特定的列名稱上使用 AUTOINCREMENT 關鍵字實現該字段值的自動增加。
關鍵字 AUTOINCREMENT 只能用于整型（INTEGER）字段。

"""

print('------------------------------------------------------------')	#60個

import sqlite3

print('------------------------------------------------------------')	#60個

import time

db_filename = 'C:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#CREATE 建立
#CREATE TABLE table01
#PRIMARY KEY 主鍵
#序號 自動遞增 不可重複

sqlstr = """
CREATE TABLE IF NOT EXISTS table01 (
    idx    INTEGER PRIMARY KEY AUTOINCREMENT,
    id_num INTEGER NOT NULL,
    ename  TEXT NOT NULL,
    cname  TEXT,
    weight INTEGER NOT NULL CHECK(weight > 0) -- 預設錯誤時會顯示
);
"""

cursor.execute(sqlstr)
conn.commit() # 更新


print('新增資料 2 筆 寫法三, 有些欄位可以不寫, 序號自動遞增')


cursor.execute("INSERT INTO table01 (id_num, ename, cname, weight) VALUES (5, 'horse', '馬', 48)")
cursor.execute("INSERT INTO table01 (id_num, ename, cname, weight) VALUES (1, 'mouse', '鼠', 66)")
cursor.execute("INSERT INTO table01 (id_num, ename, cname, weight) VALUES (4, 'elephant', '象', 48)")

cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (9, 'ox', 48)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (2, 'sheep', 66)")

cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (8, 'snake', 16)")
cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (3, 'tiger', 33)")

cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (7, 'rabbit', 8)")

cursor.execute("INSERT INTO table01 (id_num, ename, weight) VALUES (6, 'tiger', 240)")

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

#UPDATE 更新
print('更新資料, 修改2號的資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
conn.execute("UPDATE table01 SET ename = '{}'  WHERE id_num = {}".format('goat', 2))  #修改2號的資料, 要先確保已經有2號的資料, 才可以修改
conn.execute("UPDATE table01 SET weight = '{}' WHERE id_num = {}".format(29, 2))      #修改2號的資料, 要先確保已經有2號的資料, 才可以修改
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

#DELETE 刪除
print('刪除資料, 刪除4號的資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
conn.execute("DELETE FROM table01 WHERE id_num = {}".format(4))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print('------------------------------------------------------------')	#60個

print('用fetchall()讀取 全部資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM table01')      #SELECT * : 取得所有資料
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = '')
    #print(rows[i])
    print("{}\t{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4]))
    
conn.close()  # 關閉資料庫連線

print('------------------------------------------------------------')	#60個

"""
print('------------------------------------------------------------')	#60個
print('刪除資料庫中的資料表')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('DROP TABLE table01')
conn.commit() # 更新
conn.close()  # 關閉資料庫連線
"""


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)

cursor = conn.execute('select * from contact')

'''
#讀取一筆資料
row = cursor.fetchone()
print(row[0], row[1])

#再讀取一筆資料
row = cursor.fetchone()
print(row[0], row[1])
'''

rows = cursor.fetchall()    #讀取全部資料
print('共有 : ' + str(len(rows)) + " 筆資料")
print('顯示原始資料')
print(rows)

print('逐筆顯示資料')
for row in rows:
    print(row[0],row[1])


conn.close()  # 關閉資料庫連線

import sqlite3

db_filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)

# 定義資料串列
datas = [[1, 'David', '02-123456789'],
        [2, 'Lily', '02-987654321'],]
for data in datas:
    # 新增資料
    print("INSERT INTO contact (id, name, tel) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2]))
    #conn.execute("INSERT INTO contact (id, name, tel) VALUES ({}, '{}', '{}')".format(data[0], data[1], data[2]))
conn.commit() # 更新

conn.close()  # 關閉資料庫連線

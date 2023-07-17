import sqlite3
conn = sqlite3.connect('school.db') # 建立資料庫連線
# 定義資料串列
datas = [[1,'葉大雄',65,62,40],
        [2,'陳靜香',85,90,87],
        [3,'王聰明',92,90,95]]

# 新增資料
for data in datas:
    conn.execute("INSERT INTO scores (id, name, chinese, english, math) VALUES \
                 ({}, '{}', {}, {}, {})".format(data[0], data[1], data[2], data[3], data[4]))
conn.commit() # 更新
conn.close()  # 關閉資料庫連線
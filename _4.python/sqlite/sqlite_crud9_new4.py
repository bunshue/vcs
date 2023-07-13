
#exception的寫法

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE table01 (id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

with conn:
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("David",))
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
    conn.execute("INSERT INTO table01(name) VALUES (?)", ("Mouse",))

try:
    with conn:
        conn.execute("INSERT INTO table01(name) VALUES (?)", ("Lion",))
except sqlite3.IntegrityError:
    print("couldn't add Lion twice")

cursor = conn.execute('SELECT * FROM table01')      #SELECT * : 取得所有資料
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    print(rows[i])
conn.close()  # 關閉資料庫連線



import sqlite3

import datetime

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE table01(d DATE, ts TIMESTAMP)")

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into table01(d, ts) VALUES (?, ?)", (today, now))
cur.execute("select d, ts from table01")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))




import sqlite3

persons = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
    ]

con = sqlite3.connect(":memory:")

# Create the table
con.execute("create table person(firstname, lastname)")

# Fill the table
con.executemany("insert into person(firstname, lastname) values (?, ?)", persons)

# Print the table contents
for row in con.execute("select firstname, lastname from person"):
    print(row)

print("I just deleted", con.execute("delete from person").rowcount, "rows")



import sqlite3

conn = sqlite3.connect("MyBook.db")
cursor = conn.execute("SELECT * FROM book")
for row in cursor:
    print(row[0], row[1])
conn.close()


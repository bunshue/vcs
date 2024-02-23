import sqlite3

con = sqlite3.connect('sqlite/sq01.db')
print("Opened database successfully")
cur = con.cursor()
data = [("0002", "Water", 11, 123)]
 
cur.executemany("INSERT INTO test VALUES(?, ?, ?, ?)", data)
print("Table created successfully")
con.commit()
con.close()
import sqlite3

con = sqlite3.connect('sq01.db')
print("Opened database successfully")
cur = con.cursor()
name = 'oxxo'
sql = 'SELECT * FROM test WHERE name="%s";'%(name)
cur.execute(sql)
student = cur.fetchone() 
print(student)
con.commit()
con.close()

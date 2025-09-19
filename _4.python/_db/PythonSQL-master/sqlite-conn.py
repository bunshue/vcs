import sqlite3

conn = sqlite3.connect('DevDb.db')

cursor = conn.cursor()
cursor.execute('SELECT * FROM `app_info`;')

records = cursor.fetchall()
print(records)
print("record type => ", type(records))
print("record[0] type => ", type(records[0]))

for r in records:
    print(r)

print("\n---\n")

for r in records:
    app_id, app_name, app_ver, app_author, app_date, app_remark = r
    print("id => ", app_id)
    print("name => ", app_name)
    print("\n---\n")

cursor.close()
conn.close()

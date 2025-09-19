import mysql.connector

conn = mysql.connector.connect(
    host='localhost', port='3306', user='DevAuth', password='Dev127336', database='DevDb')

cursor = conn.cursor()

cursor.execute('SELECT * FROM `app_info`;')

records = cursor.fetchall()
print("record type => ", type(records))
print("record[i] type => ", type(records[0]))
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

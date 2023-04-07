import sqlite3

db_filename = 'animal.sqlite'
print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#Create table Animal
#primary key (animalId), animalId不可重複 
#cursor.execute("create table Animal ( animalId char(5), subjectId char(4) not null, " +
#               "animalNumber integer, title varchar(50) not null, primary key (animalId))")

#animalId可重複
#cursor.execute("create table Animal ( animalId char(5), subjectId char(4) not null, " +
#               "animalNumber integer, title varchar(50) not null)")

#animalId可重複, 若資料庫已存在 則不用重新建立
cursor.execute("create table if not exists Animal ( animalId char(5), subjectId char(4) not null, " +
               "animalNumber integer, title varchar(50) not null)")

#Insert
cursor.execute("insert into Animal (animalId, subjectId, animalNumber, title) " + 
               "values ('123', 'AAA', '333', 'Elephant')")

#Insert
cursor.execute("insert into Animal (animalId, subjectId, animalNumber, title) " + 
               "values ('456', 'BBB', '555', 'Giraffe')")

#Insert
cursor.execute("insert into Animal (animalId, subjectId, animalNumber, title) " + 
               "values ('789', 'CCC', '888', 'Rabbit')")

#Insert, 可重複
cursor.execute("insert into Animal (animalId, subjectId, animalNumber, title) " + 
               "values ('789', 'CCC', '888', 'Rabbit')")

conn.commit() # 主動更新

cursor.execute("select * from Animal")
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)

for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i) + '筆資料 : ', end="")
    print(rows[i])
    #print("{}\t{}".format(rows[i][0],rows[i][1]))

conn.close()  # 關閉資料庫連線

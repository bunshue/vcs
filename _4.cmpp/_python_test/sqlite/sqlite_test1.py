import sqlite3

conn = sqlite3.connect("db")

cursor = conn.cursor()

cursor.execute("create table Course ( " +
               "courseId char(5), subjectId char(4) not null, " +
               "courseNumber integer, title varchar(50) not null, " +
               "numOfCredits integer, primary key (courseId))")

cursor.execute("insert into Course (courseId, subjectId, " + 
               " courseNumber, title, numOfCredits) " + 
               "values ('11113', 'CSCI', '3720', 'Database Systems', 3)")

cursor.execute("insert into Course (courseId, subjectId, " + 
               " courseNumber, title, numOfCredits) " + 
               "values ('11111', 'CSCI', '1301', 'Introduction to Programming', 3)")
conn.commit()

cursor.execute("select * from Course")

rows = cursor.fetchall()    #讀取全部資料

print(rows)

conn.close()  # 關閉資料庫連線

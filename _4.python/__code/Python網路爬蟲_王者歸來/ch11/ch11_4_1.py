# ch11_4_1.py
import sqlite3
conn = sqlite3.connect("myInfo2.db")     # 資料庫連線
print("請輸入myInfo資料庫student2表單資料")
while True:
    n_name = input("請輸入name : ")
    n_gender = input("請輸入gender : ")
    x = (n_name, n_gender)
    sql = '''insert into student2(name, gender) values(?,?)'''  
    conn.execute(sql,x)
    conn.commit()                       # 更新資料庫
    again = input("繼續(y/n)? ")
    if again[0].lower() == "n":
        break
conn.close()                            # 關閉資料庫連線













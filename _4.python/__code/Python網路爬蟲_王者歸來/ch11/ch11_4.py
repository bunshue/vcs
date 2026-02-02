# ch11_4.py
import sqlite3
conn = sqlite3.connect("myInfo.db")     # 資料庫連線
print("請輸入myInfo資料庫students表單資料")
while True:
    new_id = int(input("請輸入id : "))  # 轉成整數
    new_name = input("請輸入name : ")
    new_gender = input("請輸入gender : ")
    x = (new_id, new_name, new_gender)
    sql = '''insert into students values(?,?,?)'''  
    conn.execute(sql,x)
    conn.commit()                       # 更新資料庫
    again = input("繼續(y/n)? ")
    if again[0].lower() == "n":
        break
conn.close()                            # 關閉資料庫連線













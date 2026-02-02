# ch11_11.py
import sqlite3
import csv
import matplotlib.pyplot as plt

conn = sqlite3.connect("populations.db")    # 資料庫連線
sql = '''Create table population( 
        area TEXT,
        male int,                     
        female int,
        total int)'''
conn.execute(sql)                           # 執行SQL指令

fn = 'Taipei_Population.csv'
with open(fn) as csvFile:                   # 儲存在SQLite
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)               # 轉成串列
    csvData = listCsv[4:]                   # 切片刪除前4 rows
    for row in csvData:
        area = row[0]                       # 區名稱
        male = int(row[7])                  # 男性人數
        female = int(row[8])                # 女性人數
        total = int(row[6])                 # 總人數
        x = (area, male, female, total)
        sql = '''insert into population values(?,?,?,?)'''
        conn.execute(sql,x)
        conn.commit()

results = conn.execute("SELECT * from population")
for record in results:
    print("區域       = ", record[0])
    print("男性人口數 = ", record[1])
    print("女性人口數 = ", record[2])
    print("總計人口數 = ", record[3])
       
conn.close()                                # 關閉資料庫連線













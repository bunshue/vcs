'''
各種讀取資料庫範例
'''

#----------------------------------------------------------------

print('讀取資料庫範例')

import sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'

def disp_menu():
    print("中油歷年油價查詢系統")
    print("------------")
    print("1.顯示歷年油價資訊")
    print("2.最近10週油價資訊")
    print("0.結束")
    print("------------")

def disp_alldata():
    print('建立資料庫連線, 資料庫 : ' + db_filename)
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute('select * from prices order by gdate desc;')

    #不是用fetchall()讀取全部資料
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". format(row[0],row[1],row[2],row[3]))
        n = n + 1
        '''
        if n == 20:  # 一次顯示20筆
            x = input("請按Enter鍵繼續...(Q:回主選單)")
            if x == 'Q' or x == 'q': break
            n = 0
        '''
def disp_10data():
    print('建立資料庫連線, 資料庫 : ' + db_filename)
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    
    cursor = conn.execute('select * from prices order by gdate desc;')
    
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". format(row[0],row[1],row[2],row[3]))
        n = n + 1
        #讀取10筆資料, 即跳出
        if n == 10:
            break

print("中油歷年油價查詢系統")

print("1.顯示歷年油價資訊")
#disp_alldata()
print("2.最近10週油價資訊")
disp_10data()



#----------------------------------------------------------------


print('讀取資料庫範例')

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/DataBasePM25.sqlite'

import sqlite3

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

'''
# 建立一個資料表
sqlstr= 'CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)'
cursor.execute(sqlstr)
'''

print('從資料庫讀取資料...') 
cursor=conn.execute("select *  from TablePM25")
rows=cursor.fetchall()

i = 0;
for row in rows:
    print("站名:{}   PM2.5={}".format(row[1],row[2]))
    i += 1
    if i > 10:
        break

conn.close()  # 關閉資料庫連線




#----------------------------------------------------------------


print('從資料庫讀出一筆資料')

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite';

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01 where num=1')
row = cursor.fetchone()
if not row==None:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線

#----------------------------------------------------------------

print('從資料庫讀出全部資料')

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/python01.sqlite';

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01')
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("{}\t{}".format(row[0],row[1]))

conn.close()  # 關閉資料庫連線


#----------------------------------------------------------------

print('從資料庫讀出全部資料')

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/headlines.sqlite';

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from titles')
rows = cursor.fetchall()
#print(rows)
r = 0
for row in rows:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
    r += 1
    if r == 10:
        break;
    
    

conn.close()  # 關閉資料庫連線





#----------------------------------------------------------------





#----------------------------------------------------------------





#----------------------------------------------------------------



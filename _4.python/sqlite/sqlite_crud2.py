import sqlite3

db_filename = 'C:/______test_files2/_db/gasoline.sqlite'

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




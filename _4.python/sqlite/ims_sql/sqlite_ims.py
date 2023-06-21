#同一個資料庫內 可以放多個table table名稱不同即可

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import sys
import csv
import time
import sqlite3

print('----------------------------------------------------------------------')	#70個

def process_csv_file1(filename):
    global stage
    global tablename
    if filename.endswith('_1.csv') == True:
        print('第1站')
        stage = 1
        tablename = 'table01'
    elif filename.endswith('_2.csv') == True:
        print('第2站')
        stage = 2
        tablename = 'table02'
    elif filename.endswith('_3.csv') == True:
        print('第3站')
        stage = 3
        tablename = 'table03'
    elif filename.endswith('_4.csv') == True:
        print('第4站')
        stage = 4
        tablename = 'table04'
    elif filename.endswith('_5.csv') == True:
        print('第5站')
        stage = 5
        tablename = 'table05'
    elif filename.endswith('_6.csv') == True:
        print('第6站')
        stage = 6
        tablename = 'table06'
    elif filename.endswith('_7.csv') == True:
        print('第7站')
        stage = 7
        tablename = 'table07'
    elif filename.endswith('_8.csv') == True:
        print('第8站')
        stage = 8
        tablename = 'table08'
    elif filename.endswith('_9.csv') == True:
        print('第9站')
        stage = 9
        tablename = 'table09'
    elif filename.endswith('_10.csv') == True:
        print('第10站')
        stage = 10
        tablename = 'table10'
    elif filename.endswith('_11.csv') == True:
        print('第11站')
        stage = 11
        tablename = 'table11'
    elif filename.endswith('_12.csv') == True:
        print('第12站')
        stage = 12
        tablename = 'table12'
    elif filename.endswith('_13a.csv') == True:
        print('第13a站')
        stage = 131
        tablename = 'table13a'
    elif filename.endswith('_13b.csv') == True:
        print('第13b站')
        stage = 132
        tablename = 'table13b'
    elif filename.endswith('_14.csv') == True:
        print('第14站')
        stage = 14
        tablename = 'table14'
    elif filename.endswith('_15.csv') == True:
        print('第15站')
        stage = 15
        tablename = 'table15'
    else:
        print('第XXXXXXXXX站')
        stage = 0
    if stage == 0:
        print('不合法的csv檔 : ', filename, ',\t跳過')

def process_csv_file2(filename):
    global stage
    global tablename

    with open(filename, encoding = 'big5') as csvFile:
        csvReader = csv.reader(csvFile)
        datas = list(csvReader)    #將資料轉成list

    length = len(datas)

    print('len = ', length)

    #print(datas)
    data_column = len(datas[0])
    print('data_column = ', data_column)

    cnt = 0
    for row in datas:
        print(row)
        print(type(row))
        #print(len(row))
        cnt += 1
        if(cnt == 5):
            break

    #同一個資料庫內 可以放多個table table名稱不同即可

    #print('建立資料庫連線, 資料庫 : ' + db_filename)
    conn = sqlite3.connect(db_filename) # 建立資料庫連線

    cursor = conn.cursor() # 建立 cursor 物件

    print('建立一個資料表')
    #Create 建立

    sqlstr = "create table if not exists '{}' ('data1' TEXT PRIMARY KEY NOT NULL".format(tablename)

    for i in range(2, data_column):
        #print(i)
        sqlstr += ", '{}' TEXT NOT NULL".format('data' + str(i))

    sqlstr += ')'
    print(sqlstr)

    cursor.execute(sqlstr)
    conn.commit() # 更新

    print('len = ', len(datas))

    #Insert
    for data in datas:
        if len(data) == 0:
            continue

        # 新增資料
        insert_data = "insert into '{}' (".format(tablename)
        for i in range(1, data_column):
            #print(i)
            if i == data_column - 1:
                insert_data += 'data' + str(i)
            else:
                insert_data += 'data' + str(i) + ", "
           
        insert_data +=') VALUES ('
        for i in range(1, data_column):
            #print(i)
            if i == data_column - 1:
                insert_data += "'{}'".format(data[i])
            else:
                insert_data += "'{}', ".format(data[i])

        insert_data +=')'

        #print(insert_data)
        
        #insert_data = "insert into '{}' (data1, data2, data3, data4, data5) VALUES ('{}', '{}', '{}', '{}', '{}')".format(tablename, data[1], data[2], data[3], data[4], data[5])
        #print(insert_data)
        conn.execute(insert_data)
    conn.commit() # 更新

    cursor.execute(sqlstr)
    conn.commit() # 更新
    conn.close()  # 關閉資料庫連線

    print('不是用fetchall()讀取 全部資料')
    #print('建立資料庫連線, 資料庫 : ' + db_filename)
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute("select * from '{}'".format(tablename))
    i = 0
    for row in cursor:
        #print(type(row))
        #print(len(row))
        #print('第' + str(i + 1) + '筆資料 : ', end = "")
        #print(rows[i])
        #print("{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))
        for r in row:
            print(r, end = '\t')
        print()
        i = i + 1
    conn.close()  # 關閉資料庫連線

print('----------------------------------------------------------------------')	#70個

stage = 0
tablename = 'table00'

import os, time, glob, sys, shutil

source_dir = 'QC/csv'
target_dir = 'QC/csv_old'

db_filename = 'C:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';
#db_filename = 'db_ims.sqlite';


#準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        #os.makedirs(target_dir, exist_ok=True)

#尋找檔案
import glob
print('尋找目前目錄下之 *.csv')
files = glob.glob(source_dir + "/*.csv") 
for filename in files:
    print(filename)
    stage = 0
    tablename = 'table00'
    process_csv_file1(filename)
    if stage != 0:
        print('繼續')
        #process_csv_file2(filename)
        #若能正確處理完畢, 再搬到old資料夾
        #shutil.move(filename, target_dir)

print('----------------------------------------------------------------------')	#70個

'''
filename = 'C:/_git/vcs/_4.python/sqlite/ims_sql/QC/csv/ims_20221218_13b.csv'

stage = 0
tablename = 'table00'
process_csv_file1(filename)
if stage != 0:
    process_csv_file2(filename)
'''

print('----------------------------------------------------------------------')	#70個




print('----------------------------------------------------------------------')	#70個

# 建立csv二維串列資料
'''
all_data = [
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
]
'''
all_data = [
]

print('從資料庫讀出全部資料')

db_filename = 'db_ims.sqlite'

print('第1站')
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table01')
rows = cursor.fetchall()
#print(rows)
index = 1
for row in rows:
    print(len(row))
    #print("{}\t{}".format(row[0],row[1]))
    print(row)
    all_data.append(row)
    index += 1
conn.close()  # 關閉資料庫連線

print('第2站')
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('select * from table02')
rows = cursor.fetchall()
#print(rows)
for row in rows:
    #print("{}\t{}".format(row[0],row[1]))
    print(row)
    all_data.append(row)
conn.close()  # 關閉資料庫連線





print('----------------------------------------------------------------------')	#70個



# 開啟輸出的 csv 檔案
filename_w = 'automation_ims.csv'
with open(filename_w, 'w', newline='') as csvfile:
    # 建立 csv 檔寫入物件
    writer = csv.writer(csvfile)

    # 寫入二維串列資料
    writer.writerows(all_data)





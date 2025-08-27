#同一個資料庫內 可以放多個table table名稱不同即可

print('------------------------------------------------------------')	#60個
print('準備工作')

import os
import sys
import csv
import time
import sqlite3
import tkinter as tk
from tkinter.filedialog import askopenfile #tk之openFileDialog
from tkinter.filedialog import asksaveasfile #tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

flag_debug_mode = True

# 建立csv二維串列資料
all_data = [
]

list_stage01 = list()
list_stage02 = list()
list_stage03 = list()
list_stage04 = list()
list_stage05 = list()
list_stage06 = list()
list_stage07 = list()
list_stage08 = list()
list_stage09 = list()
list_stage10 = list()
list_stage11 = list()
list_stage12 = list()
list_stage13a = list()
list_stage13b = list()
list_stage14 = list()
list_stage15 = list()

choice = []

stage_no = [
'第1站 下蓋清潔', '第2站 點膠', '第3站 前2站NG', '第4站 模組接合',
'第5站 間隙檢查', '第6站 UV固化', '第7站 點膠線檢查', '第8站 前4站NG',
'第9站 氣密測試', '第10站 Hi-pot', '第11站 色調', '第12站 前3站NG',
'第13a站 等級判定', '第13b站 資料燒錄', '第14站 前2站NG', '第15站 包裝出料'
]

table_list = [
'table01', 'table02', 'table03', 'table04',
'table05', 'table06', 'table07', 'table08',
'table09', 'table10', 'table11', 'table12',
'table13a', 'table13b', 'table14', 'table15'
]

list_stage_list = [
'list_stage01', 'list_stage02', 'list_stage03', 'list_stage04',
'list_stage05', 'list_stage06', 'list_stage07', 'list_stage08',
'list_stage09', 'list_stage10', 'list_stage11', 'list_stage12',
'list_stage13a', 'list_stage13b', 'list_stage14', 'list_stage15'
]


stage = -1
tablename = ''
db_filename = ''
#db_filename = 'D:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

dummy_data = 'abcd'
count = 0

print('------------------------------------------------------------')	#60個

#公用副程式

#取得一個資料庫內所有表單的名稱, list格式
def get_table_names(conn):
    table_names = []
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in tables.fetchall():
        table_names.append(table[0])
    return table_names

#取得一個表單內所有欄位的名稱, list格式
def get_column_names(conn, table_name):
    column_names = []
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names

#清除記憶體內的資料
def clear_all_data():
    global all_data
    all_data = [
    ]

    global list_stage01
    global list_stage02
    global list_stage03
    global list_stage04
    global list_stage05
    global list_stage06
    global list_stage07
    global list_stage08
    global list_stage09
    global list_stage10
    global list_stage11
    global list_stage12
    global list_stage13a
    global list_stage13b
    global list_stage14
    global list_stage15
    
    list_stage01 = list()
    list_stage02 = list()
    list_stage03 = list()
    list_stage04 = list()
    list_stage05 = list()
    list_stage06 = list()
    list_stage07 = list()
    list_stage08 = list()
    list_stage09 = list()
    list_stage10 = list()
    list_stage11 = list()
    list_stage12 = list()
    list_stage13a = list()
    list_stage13b = list()
    list_stage14 = list()
    list_stage15 = list()
    
print('------------------------------------------------------------')	#60個

def process_csv_file1(filename):
    global stage
    global tablename

    if filename.endswith('_1.csv') == True:
        #print('第1站')
        stage = 1
        tablename = 'table01'
    elif filename.endswith('_2.csv') == True:
        #print('第2站')
        stage = 2
        tablename = 'table02'
    elif filename.endswith('_3.csv') == True:
        #print('第3站')
        stage = 3
        tablename = 'table03'
    elif filename.endswith('_4.csv') == True:
        #print('第4站')
        stage = 4
        tablename = 'table04'
    elif filename.endswith('_5.csv') == True:
        #print('第5站')
        stage = 5
        tablename = 'table05'
    elif filename.endswith('_6.csv') == True:
        #print('第6站')
        stage = 6
        tablename = 'table06'
    elif filename.endswith('_7.csv') == True:
        #print('第7站')
        stage = 7
        tablename = 'table07'
    elif filename.endswith('_8.csv') == True:
        #print('第8站')
        stage = 8
        tablename = 'table08'
    elif filename.endswith('_9.csv') == True:
        #print('第9站')
        stage = 9
        tablename = 'table09'
    elif filename.endswith('_10.csv') == True:
        #print('第10站')
        stage = 10
        tablename = 'table10'
    elif filename.endswith('_11.csv') == True:
        #print('第11站')
        stage = 11
        tablename = 'table11'
    elif filename.endswith('_12.csv') == True:
        #print('第12站')
        stage = 12
        tablename = 'table12'
    elif filename.endswith('_13a.csv') == True:
        #print('第13a站')
        stage = 131
        tablename = 'table13a'
    elif filename.endswith('_13b.csv') == True:
        #print('第13b站')
        stage = 132
        tablename = 'table13b'
    elif filename.endswith('_14.csv') == True:
        #print('第14站')
        stage = 14
        tablename = 'table14'
    elif filename.endswith('_15.csv') == True:
        #print('第15站')
        stage = 15
        tablename = 'table15'
    else:
        print('第XXXXXXXXX站')
        stage = 0
    if stage == 0:
        print('不合法的csv檔 : ', filename, ',\t跳過')

def save_data_in_list(datas):
    #print(type(datas))
    data_length = len(datas)
    if stage == 1:
        #print('第1站')
        length = len(list_stage01)
        if length == 0:
            list_stage01.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage01.append(datas[i])
    elif stage == 2:
        #print('第2站')
        length = len(list_stage02)
        if length == 0:
            list_stage02.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage02.append(datas[i])
    elif stage == 3:
        #print('第3站')
        length = len(list_stage03)
        if length == 0:
            list_stage03.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage03.append(datas[i])
    elif stage == 4:
        #print('第4站')
        length = len(list_stage04)
        if length == 0:
            list_stage04.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage04.append(datas[i])
    elif stage == 5:
        #print('第5站')
        length = len(list_stage05)
        if length == 0:
            list_stage05.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage05.append(datas[i])
    elif stage == 6:
        #print('第6站')
        length = len(list_stage06)
        if length == 0:
            list_stage06.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage06.append(datas[i])
    elif stage == 7:
        #print('第7站')
        length = len(list_stage07)
        if length == 0:
            list_stage07.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage07.append(datas[i])
    elif stage == 8:
        #print('第8站')
        length = len(list_stage08)
        if length == 0:
            list_stage08.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage08.append(datas[i])
    elif stage == 9:
        #print('第9站')
        length = len(list_stage09)
        if length == 0:
            list_stage09.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage09.append(datas[i])
    elif stage == 10:
        #print('第10站')
        length = len(list_stage10)
        if length == 0:
            list_stage10.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage10.append(datas[i])
    elif stage == 11:
        #print('第11站')
        length = len(list_stage11)
        if length == 0:
            list_stage11.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage11.append(datas[i])
    elif stage == 12:
        #print('第12站')
        length = len(list_stage12)
        if length == 0:
            list_stage12.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage12.append(datas[i])
    elif stage == 131:
        #print('第13a站')
        length = len(list_stage13a)
        if length == 0:
            list_stage13a.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage13a.append(datas[i])
    elif stage == 132:
        #print('第13b站')
        length = len(list_stage13b)
        if length == 0:
            list_stage13b.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage13b.append(datas[i])
    elif stage == 14:
        #print('第14站')
        length = len(list_stage14)
        if length == 0:
            list_stage14.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage14.append(datas[i])
    elif stage == 15:
        #print('第15站')
        length = len(list_stage15)
        if length == 0:
            list_stage15.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage15.append(datas[i])
    else:
        print('第XXXXXXXXX站')

def process_csv_file2(filename):
    global stage
    global tablename

    #with open(filename, newline = '') as csvfile:
    with open(filename, encoding = 'big5') as csvfile:
        rows = csv.reader(csvfile)  # 讀取 csv 檔案內容
        datas = list(rows)    #將資料轉成list

    length = len(datas)
    #print('len = ', length)

    save_data_in_list(datas)

    #print(datas)
    data_column = len(datas[0])
    #print('data_column = ', data_column)

    for row in datas:
        for i in range(0, len(row)):
            row[i] = row[i].strip()

    '''
    cnt = 0
    for row in datas:
        print(row)
        print(type(row))
        #print(len(row))
        cnt += 1
        if cnt == 3:
            break
    '''

    #同一個資料庫內 可以放多個table table名稱不同即可

    #print('建立資料庫連線, 資料庫 : ' + db_filename)
    conn = sqlite3.connect(db_filename) # 建立資料庫連線

    cursor = conn.cursor() # 建立 cursor 物件

    #print('建立一個資料表')
    #Create 建立

    sqlstr = "CREATE TABLE IF NOT EXISTS '{}' ('data1' TEXT PRIMARY KEY NOT NULL".format(tablename)

    for i in range(2, data_column):
        #print(i)
        sqlstr += ", '{}' TEXT NOT NULL".format('data' + str(i))

    sqlstr += ')'
    #print(sqlstr)

    cursor.execute(sqlstr)
    conn.commit() # 更新

    #print('len = ', len(datas))

    #Insert
    for data in datas:
        if len(data) == 0:
            continue

        # 新增資料
        insert_data = "INSERT INTO '{}' (".format(tablename)
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
                insert_data += "'{}'".format(data[i].strip())
            else:
                insert_data += "'{}', ".format(data[i].strip())

        insert_data +=')'

        #print(insert_data)
        
        #insert_data = "INSERT INTO '{}' (data1, data2, data3, data4, data5) VALUES ('{}', '{}', '{}', '{}', '{}')".format(tablename, data[1], data[2], data[3], data[4], data[5])
        #print(insert_data)
        conn.execute(insert_data)
    conn.commit() # 更新

    cursor.execute(sqlstr)
    conn.commit() # 更新
    conn.close()  # 關閉資料庫連線

    #print('不是用fetchall()讀取 全部資料')
    #print('建立資料庫連線, 資料庫 : ' + db_filename)
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute("SELECT * FROM '{}'".format(tablename))
    '''
    cnt = 0
    for row in cursor:
        #print(type(row))
        #print(len(row))
        #print('第' + str(i + 1) + '筆資料 : ', end = "")
        #print(rows[i])
        #print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
        for r in row:
            print(r, end = '\t')
        print()
        cnt += 1
        if cnt == 3:
            break
    '''
    conn.close()  # 關閉資料庫連線

def precheck_csv_data():
    print('預先檢查這些csv檔案是否皆可用')
    
    #1. 無舊資料
    #2. 有舊資料 要考慮序號是否
    #3. 第一站資料必定要先存在
    
    import os, time, glob, sys, shutil

    source_dir = 'QC/csv'
    target_dir = 'QC/csv_old'

    if flag_debug_mode == True:
        source_dir = 'QC_debug/csv'
        target_dir = 'QC_debug/csv_old'

    #準備輸出資料夾 若不存在, 則建立
    if not os.path.exists(target_dir):
            os.mkdir(target_dir)
            #os.makedirs(target_dir, exist_ok = True)

    import glob
    # 撈出單層csv檔
    files = glob.glob(source_dir + "/*.csv") 
    for filename in files:
        #print(filename)
        stage = 0
        tablename = 'table00'
        #process_csv_file1(filename)
        if stage != 0:
            print('繼續')
            #process_csv_file2(filename)
            #若能正確處理完畢, 再搬到old資料夾
            #shutil.move(filename, target_dir)

    #message = "匯入生產資料 完成"
    #print(message)
    #text1.insert('end', message)
    
def precheck_data_base():
    print('匯入資料庫時要預先檢查這個新的資料庫資料是否皆可用')
    
def import_csv_data():
    global stage
    global tablename

    import os, time, glob, sys, shutil

    source_dir = 'QC/csv'
    target_dir = 'QC/csv_old'

    if flag_debug_mode == True:
        source_dir = 'QC_debug/csv'
        target_dir = 'QC_debug/csv_old'

    #準備輸出資料夾 若不存在, 則建立
    if not os.path.exists(target_dir):
            os.mkdir(target_dir)
            #os.makedirs(target_dir, exist_ok = True)

    import glob
    # 撈出單層csv檔
    files = glob.glob(source_dir + "/*.csv") 
    for filename in files:
        #print(filename)
        stage = 0
        tablename = 'table00'
        process_csv_file1(filename)
        if stage != 0:
            #print('繼續')
            process_csv_file2(filename)
            #若能正確處理完畢, 再搬到old資料夾
            #shutil.move(filename, target_dir)

    message = "匯入生產資料 完成"
    print(message)
    text1.insert('end', message)

def read_from_db():
    
    # 還有其他站 TBD,  還要讀出資料後 將資料 加/附加 到list裏
    
    if db_filename == '':
        message = '尚未開啟資料庫, 離開'
        print(message)
        text1.insert('end', message)
        return
    
    global all_data
    all_data = [
    ]
    message = ''

    print('從資料庫讀出全部資料')

    conn = sqlite3.connect(db_filename) # 建立資料庫連線

    print('目前資料庫 : ' + db_filename)

    conn = sqlite3.connect(db_filename)

    table_names = get_table_names(conn)
    print(type(table_names))
    talbe_names_length = len(table_names)
    if talbe_names_length <= 0:
        print('資料庫內無表單, 離開')
        conn.close()
        return;
    
    print('裡面有:', talbe_names_length, ' 個表單')
        
    conn.close()

    table_data_exists = False
    for table_name in table_names:
        if(table_name == 'table01'):
            print('第1站資料存在')
            table_data_exists = True

    if table_data_exists == False:
        print('無第1站資料, 離開')
        return;

    print('第1站')
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute('SELECT * FROM table01')
    rows = cursor.fetchall()
    #print(rows)
    index = 1
    for row in rows:
        print(len(row))
        #print('{}\t{}'.format(row[0], row[1]))
        #print(row)
        all_data.append(row)
        index += 1
    conn.close()  # 關閉資料庫連線


    table_data_exists = False
    for table_name in table_names:
        if(table_name == 'table02'):
            print('第1站資料存在')
            table_data_exists = True

    if table_data_exists == False:
        print('無第2站資料, 離開')
        return;

    print('第2站')
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute('SELECT * FROM table02')
    rows = cursor.fetchall()
    #print(rows)
    for row in rows:
        #print('{}\t{}'.format(row[0], row[1]))
        #print(row)
        all_data.append(row)
        message = message + str(row) + '\n'
    conn.close()  # 關閉資料庫連線
    text1.insert('end', message)

    for i in range(1, len(table_list)):
        print('檢查 : ', table_list[i])

        table_data_exists = False
        for table_name in table_names:
            if(table_name == table_list[i]):
                print('表單: ', table_list[i], ' 存在')
                table_data_exists = True

        if table_data_exists == False:
            print('表單: ', table_list[i], ' 不存在')
            continue

        print('讀取表單: ', table_list[i], ' 資料')
        conn = sqlite3.connect(db_filename) # 建立資料庫連線


        sqlstr = "SELECT * FROM {}".format(table_list[i])   #SELECT * : 取得所有資料
        #print(sqlstr)
        cursor = conn.execute(sqlstr)
        rows = cursor.fetchall()    #讀取全部資料
        length = len(rows)
        print('共有', length, '筆資料')

        cursor = conn.execute(sqlstr)
        rows = cursor.fetchall()    #讀取全部資料
        #print(rows)
        for row in rows:
            #print('{}\t{}'.format(row[0], row[1]))
            #print(row)
            all_data.append(row)
            message = message + str(row) + '\n'
        conn.close()  # 關閉資料庫連線
        text1.insert('end', message)


    message = "從資料庫讀出全部資料 完成"
    print(message)
    text1.insert('end', message)

def merge_stage_data0(list_stage):
    
    length = len(list_stage)

    if length >= 0:
        #print('list_stage 資料長度 : ', length)
        data_column = len(list_stage[0])
        #print('data_column = ', data_column)

        #檔頭
        columns = list(list_stage[0])    #將資料轉成list
        for data in columns:
            all_data[0].append(data)

        #資料內容
        for i in range(1, length):
            if len(list_stage[i]) <= 0:
                continue
            
            columns = list(list_stage[i])    #將資料轉成list

            sn_new = columns[1]

            all_data_length = len(all_data)
            for index in range(1, all_data_length):
                #print(all_data[index][1])
                if all_data[index][1] == sn_new:
                    break;

            for data in columns:
                all_data[index].append(data)

        #缺資料的要補滿
        all_data_columns_length = len(all_data[0])
        #print('資料總寬度 : ', all_data_columns_length)
        #print(all_data_columns_length)

        all_data_length = len(all_data)

        for i in range(1, all_data_length):
            #print('i = ', i, 'len = ', len(all_data[i]))
            if len(all_data[i]) < all_data_columns_length:
                for j in range(0, all_data_columns_length - len(all_data[i])):
                    all_data[i].append('')

    
def merge_stage_data():
    print('merge_stage_data')

    #print('第1站')
    length = len(list_stage01)
    print('list_stage01 資料長度 : ', length)
    if length >= 0:
        for i in range(0, length):
            all_data.append(list_stage01[i])
            
    length = len(all_data)
    print('all_data 資料長度 : ', length)
   
    #print('第2站')
    merge_stage_data0(list_stage02)
    
    #print('第3站')
    merge_stage_data0(list_stage03)

    #print('第4站')
    merge_stage_data0(list_stage04)

    #print('第5站')
    merge_stage_data0(list_stage05)

    #print('第6站')
    merge_stage_data0(list_stage06)

    #print('第7站')
    merge_stage_data0(list_stage07)

    #print('第8站')
    merge_stage_data0(list_stage08)

    #print('第9站')
    merge_stage_data0(list_stage09)

    #print('第10站')
    merge_stage_data0(list_stage10)

    #print('第11站')
    merge_stage_data0(list_stage11)
    
    #print('第12站')
    merge_stage_data0(list_stage12)
    
    #print('第13a站')
    merge_stage_data0(list_stage13a)

    #print('第13b站')
    merge_stage_data0(list_stage13b)

    #print('第14站')
    merge_stage_data0(list_stage14)

    #print('第15站')
    merge_stage_data0(list_stage15)


def show_info():
    print('show_info')
    length = len(all_data)
    print('資料長度 : ', length)
    print('目前選取的內容 : ')
    str = "選擇："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + stage_no[i] + " "
    print(str)


    length = len(list_stage01)
    print('第1站 資料長度: ', length)


    '''
    global db_filename
    if db_filename == '':
        message = '尚未開啟資料庫, 離開'
        print(message)
        text1.insert('end', message)
        return

    print('目前資料庫 : ' + db_filename)

    conn = sqlite3.connect(db_filename)

    table_names = get_table_names(conn)
    print(type(table_names))
    talbe_names_length = len(table_names)
    print('裡面有:', talbe_names_length, ' 個表單')
    print('分別是:')
    for table_name in table_names:
        print('表單:', table_name, end = '\t')
        column_names = get_column_names(conn, table_name)
        column_names_length = len(column_names)
        print('裡面有:', column_names_length, ' 個欄位', end = ' ')
        print('分別是:', end = ' ')
        for column_name in column_names:
            print(column_name, end = ' ')
        print()


    conn.close()
    '''

def show_list_stage():
    print('第1站')
    print(list_stage01)
    print('第2站')
    print(list_stage02)
    print('第3站')
    print(list_stage03)
    print('第4站')
    print(list_stage04)
    print('第5站')
    print(list_stage05)
    '''
    print('第6站')
    print(list_stage06)
    print('第7站')
    print(list_stage07)
    print('第8站')
    print(list_stage08)
    print('第9站')
    print(list_stage09)
    print('第10站')
    print(list_stage10)
    print('第11站')
    print(list_stage11)
    print('第12站')
    print(list_stage12)
    print('第13a站')
    print(list_stage13a)
    print('第13b站')
    print(list_stage13b)
    print('第14站')
    print(list_stage14)
    print('第15站')
    print(list_stage15)
    '''

    '''
    #還是只能當字串 不能當變數.......
    int('合在一起')
    for i in range(0, len(list_stage_list)):
        print('顯示 : ', list_stage_list[i])
        print(list_stage_list[i])
    '''

def show_all_data():

    length = len(all_data)
    print('all_data 資料長度 : ', length)
    for i in range(0, length):
        print(all_data[i])

def export_data():
    global all_data
    length = len(all_data)
    print('資料長度 : ', length)
    if length == 0:
        message = '無資料, 離開'
        print(message)
        text1.insert('end', message)
        main_message2.set(message)
    else:
        # 開啟輸出的 csv 檔案
        filename_w = '匯出資料範例.csv'
        with open(filename_w, 'w', newline = '') as csvfile:
            # 建立 csv 檔寫入物件
            writer = csv.writer(csvfile)

            # 寫入二維串列資料
            writer.writerows(all_data)

        message = '匯出資料 完成'
        print(message)
        text1.insert('end', message)

def button00Click():
    print('你按了 新建資料庫')
    global db_filename
    db_filename = 'db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';
    message = '資料庫 : ' + db_filename
    print(message)
    text1.insert('end', message)
    main_message1.set(message)

    print('新建資料庫, 清除記憶體資料')
    clear_all_data()

def button01Click():
    print('你按了 開啟資料庫')
    button01_text.set("開啟資料庫...")
    file = askopenfile(parent = window, mode = 'rb', title = "選取資料庫", filetypes = [("資料庫檔案", "*.sqlite")])
    if file:
        global db_filename
        db_filename = file.name
        message = '資料庫 : ' + db_filename
        print(message)
        text1.insert('end', message)
        main_message1.set(message)

    button01_text.set("開啟資料庫")
    print('開啟資料庫, 清除記憶體資料')
    clear_all_data()

def button02Click():
    print('你按了 讀取資料庫資料')
    global db_filename
    if db_filename == '':
        message = '尚未開啟資料庫, 離開'
        print(message)
        text1.insert('end', message)
        return
    
    read_from_db()

def button03Click():
    print('你按了 匯入生產資料並將資料加入資料庫')
    global db_filename
    print(db_filename)
    if db_filename == '':
        message = '尚未開啟資料庫, 離開'
        print(message)
        text1.insert('end', message)
        return

    import_csv_data()
    merge_stage_data()

def button04Click():
    print('你按了 匯入資料庫 TBD')

def button05Click():
    print('你按了 匯出生產資料')
    export_data()

def button10Click():
    print('你按了button10')
    show_info()

def button11Click():
    print('你按了button11')
    precheck_csv_data()

def button12Click():
    print('你按了button12')
    show_list_stage()
    show_all_data()

def button13Click():
    print('你按了button13')
    window.destroy()

def button14Click():
    #print('你按了button14')
    set_data()

def button15Click():
    #print('你按了button15')
    clear_text1()

def set_data():
    '''
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + dummy_data
    print(mesg)
    text1.insert('end', mesg)
    '''
    global count
    count = count + 1
    message = '  次數' + str(count)
    text1.insert('end', message)

def clear_text1():
    text1.delete(1.0, 'end')
    # 執行 clear 函式時，清空內容

def choose():
    str = "選擇："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + stage_no[i] + " "
    print(str)
    msg.set(str)

window = tk.Tk()

main_message1 = tk.StringVar()
main_message2 = tk.StringVar()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title('自動化產線生產資料庫')

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

icon_filename = 'D:/_git/vcs/_1.data/______test_files1/_material/ims.ico'
window.iconbitmap(icon_filename)   # 更改圖示

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width = w, height = h, command = button00Click, text = '新建資料庫')
button00.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

#開啟資料庫按鈕
#button01 = tk.Button(window, width = w, height = h, command = button01Click, text = '開啟資料庫')
#button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01_text = tk.StringVar()
#button01 = tk.Button(window, textvariable = button01_text, command = lambda:button01Click(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button01 = tk.Button(window, textvariable = button01_text, width = w, height = h, command = lambda:button01Click())
#button01 = tk.Button(window, command = xxxxxxx, text='選取檔案')
button01_text.set("開啟資料庫")

button02 = tk.Button(window, width = w, height = h, command = button02Click, text = '讀取資料庫資料')
button02.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button03 = tk.Button(window, width = w, height = h, command = button03Click, text = '匯入生產資料\n將資料加入資料庫')
button03.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button04 = tk.Button(window, width = w, height = h, command = button04Click, text = '匯入資料庫')
button04.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button05 = tk.Button(window, width = w, height = h, command = button05Click, text = '匯出生產資料')
button05.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button00.place(x = x_st + dx * 0, y = y_st + dy * 0)
button01.place(x = x_st + dx * 1, y = y_st + dy * 0)
button02.place(x = x_st + dx * 2, y = y_st + dy * 0)
button03.place(x = x_st + dx * 3, y = y_st + dy * 0)
button04.place(x = x_st + dx * 4, y = y_st + dy * 0)
button05.place(x = x_st + dx * 5, y = y_st + dy * 0)

if flag_debug_mode == True:
    button10 = tk.Button(window, width = w, height = h, command = button10Click, text = 'Info')
    button10.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button11 = tk.Button(window, width = w, height = h, command = button11Click, text = '檢查csv/db')
    button11.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button12 = tk.Button(window, width = w, height = h, command = button12Click, text = '顯示記憶體資料')
    button12.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button13 = tk.Button(window, width = w, height = h, command = button13Click, text = '關閉視窗')
    button13.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button14 = tk.Button(window, width = w, height = h, command = button14Click, text = 'Send Data')
    button14.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button15 = tk.Button(window, width = w, height = h, command = button15Click, text = 'Clear')
    button15.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

    button10.place(x = x_st + dx * 0, y = y_st + dy * 1)
    button11.place(x = x_st + dx * 1, y = y_st + dy * 1)
    button12.place(x = x_st + dx * 2, y = y_st + dy * 1)
    button13.place(x = x_st + dx * 3, y = y_st + dy * 1)
    button14.place(x = x_st + dx * 4, y = y_st + dy * 1)
    button15.place(x = x_st + dx * 5, y = y_st + dy * 1)

font_size = 20

# 加入 Label
label_message1 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message1)
label_message1.pack()
label_message1.place(x = 5, y = 0 + 10)
main_message1.set('')

label_message2 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message2)
label_message2.pack()
label_message2.place(x = 5 + W * 3 / 4, y = 0 + 10)
main_message2.set('')

msg = tk.StringVar()
label1 = tk.Label(window, text = '選擇顯示站別：')
label1.pack()
label1.place(x = x_st + dx * 0, y = y_st + dy * 2 - 20)
label2 = tk.Label(window, fg = 'red', textvariable = msg)
label2.pack()
label2.place(x = x_st + dx * 0, y = y_st + dy * 2 + 80)

# 加入 Checkbutton
dx2 = dx * 4 / 4   #為了微調距離用
for i in range(0, len(stage_no)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text = stage_no[i], variable = choice[i], command = choose)
    item.pack()
    item.place(x = x_st + dx2 * (i % 6), y = y_st + dy * 2 + int(i / 6) * 25)

# 加入 Text
text1 = tk.Text(window, width = 100, height = 30)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 3 + 50)

message = "尚未開啟資料庫"
main_message1.set(message)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


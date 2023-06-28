#同一個資料庫內 可以放多個table table名稱不同即可

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import os
import sys
import csv
import time
import sqlite3
import tkinter as tk

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
'第1站', '第2站', '第3站', '第4站', '第5站', '第6站', '第7站', '第8站',
'第9站', '第10站', '第11站', '第12站', '第13a站', '第13b站', '第14站', '第15站'
]

db_filename = 'C:/_git/vcs/_1.data/______test_files2/db_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

dummy_data = 'abcd'
count = 0

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

def save_data_in_list(datas):
    #print(type(datas))
    data_length = len(datas)
    if stage == 1:
        print('第1站')
        length = len(list_stage01)
        if length == 0:
            list_stage01.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage01.append(datas[i])
    elif stage == 2:
        print('第2站')
        length = len(list_stage02)
        if length == 0:
            list_stage02.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage02.append(datas[i])
    elif stage == 3:
        print('第3站')
        length = len(list_stage03)
        if length == 0:
            list_stage03.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage03.append(datas[i])
    elif stage == 4:
        print('第4站')
        length = len(list_stage04)
        if length == 0:
            list_stage04.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage04.append(datas[i])
    elif stage == 5:
        print('第5站')
        length = len(list_stage05)
        if length == 0:
            list_stage05.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage05.append(datas[i])
    elif stage == 6:
        print('第6站')
        length = len(list_stage06)
        if length == 0:
            list_stage06.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage06.append(datas[i])
    elif stage == 7:
        print('第7站')
        length = len(list_stage07)
        if length == 0:
            list_stage07.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage07.append(datas[i])
    elif stage == 8:
        print('第8站')
        length = len(list_stage08)
        if length == 0:
            list_stage08.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage08.append(datas[i])
    elif stage == 9:
        print('第9站')
        length = len(list_stage09)
        if length == 0:
            list_stage09.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage09.append(datas[i])
    elif stage == 10:
        print('第10站')
        length = len(list_stage10)
        if length == 0:
            list_stage10.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage10.append(datas[i])
    elif stage == 11:
        print('第11站')
        length = len(list_stage11)
        if length == 0:
            list_stage11.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage11.append(datas[i])
    elif stage == 12:
        print('第12站')
        length = len(list_stage12)
        if length == 0:
            list_stage12.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage12.append(datas[i])
    elif stage == 131:
        print('第13a站')
        length = len(list_stage13a)
        if length == 0:
            list_stage13a.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage13a.append(datas[i])
    elif stage == 132:
        print('第13b站')
        length = len(list_stage13b)
        if length == 0:
            list_stage13b.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage13b.append(datas[i])
    elif stage == 14:
        print('第14站')
        length = len(list_stage14)
        if length == 0:
            list_stage14.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage14.append(datas[i])
    elif stage == 15:
        print('第15站')
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
                insert_data += "'{}'".format(data[i])
            else:
                insert_data += "'{}', ".format(data[i])

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

def import_csv_data():
    global stage
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
        #print(filename)
        stage = 0
        tablename = 'table00'
        process_csv_file1(filename)
        print('new stage = ', stage)
        print('new tablename = ', tablename)
        if stage != 0:
            #print('繼續')
            process_csv_file2(filename)
            #若能正確處理完畢, 再搬到old資料夾
            #shutil.move(filename, target_dir)

    message = "匯入生產資料 完成"
    print(message)
    text1.insert('end', message)

def read_from_db():
    global all_data
    message = ''

    print('從資料庫讀出全部資料')

    db_filename = 'db_ims.sqlite'

    print('第1站')
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute('SELECT * FROM table01')
    rows = cursor.fetchall()
    #print(rows)
    index = 1
    for row in rows:
        print(len(row))
        #print('{}\t{}'.format(row[0], row[1]))
        print(row)
        all_data.append(row)
        index += 1
    conn.close()  # 關閉資料庫連線

    print('第2站')
    conn = sqlite3.connect(db_filename) # 建立資料庫連線
    cursor = conn.execute('SELECT * FROM table02')
    rows = cursor.fetchall()
    #print(rows)
    for row in rows:
        #print('{}\t{}'.format(row[0], row[1]))
        print(row)
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

    print('第1站')
    length = len(list_stage01)
    print('list_stage01 資料長度 : ', length)
    if length >= 0:
        for i in range(0, length):
            all_data.append(list_stage01[i])
            
    length = len(all_data)
    print('all_data 資料長度 : ', length)
   
    print('第2站')
    merge_stage_data0(list_stage02)
    
    print('第3站')
    merge_stage_data0(list_stage03)

    print('第4站')
    merge_stage_data0(list_stage04)

    print('第5站')
    merge_stage_data0(list_stage05)

    print('第6站')
    merge_stage_data0(list_stage06)

    print('第7站')
    merge_stage_data0(list_stage07)

    print('第8站')
    merge_stage_data0(list_stage08)

    print('第9站')
    merge_stage_data0(list_stage09)

    print('第10站')
    merge_stage_data0(list_stage10)

    print('第11站')
    merge_stage_data0(list_stage11)
    
    print('第12站')
    merge_stage_data0(list_stage12)
    
    print('第13a站')
    merge_stage_data0(list_stage13a)

    print('第13b站')
    merge_stage_data0(list_stage13b)

    print('第14站')
    merge_stage_data0(list_stage14)

    print('第15站')
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

def do_debug():
    filename = 'C:/_git/vcs/_4.python/sqlite/ims_sql/QC/csv/ims_20221218_1.csv'
    print(filename)
    global stage
    stage = 0
    tablename = 'table01'
    process_csv_file1(filename)
    print(stage)
    
    if stage != 0:
        print('繼續')
        process_csv_file2(filename)
    else:
        print('XXXXXXXXXXXXXXXX')

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

def show_all_data():
    merge_stage_data()

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
    else:
        # 開啟輸出的 csv 檔案
        filename_w = 'automation_ims.csv'
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

def button01Click():
    print('你按了 開啟資料庫')

def button02Click():
    print('你按了 讀取資料庫資料')
    read_from_db()

def button03Click():
    print('你按了 匯入生產資料並將資料加入資料庫')
    import_csv_data()

def button04Click():
    print('你按了 匯出生產資料')
    export_data()

def button05Click():
    print('你按了button05')

def button10Click():
    print('你按了button10')
    show_info()

def button11Click():
    print('你按了button11')
    do_debug()

def button12Click():
    print('你按了button12')
    show_list_stage()

def button13Click():
    print('你按了button13')
    show_all_data()

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

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, text = '新建資料庫', width = w, height = h, command = button00Click)
button00.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01 = tk.Button(window, text = '開啟資料庫', width = w, height = h, command = button01Click)
button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button02 = tk.Button(window, text = '讀取資料庫資料', width = w, height = h, command = button02Click)
button02.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button03 = tk.Button(window, text = '匯入生產資料\n將資料加入資料庫', width = w, height = h, command = button03Click)
button03.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button04 = tk.Button(window, text = '匯出生產資料', width = w, height = h, command = button04Click)
button04.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button05 = tk.Button(window, text = '', width = w, height = h, command = button05Click)
button05.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button10 = tk.Button(window, text = 'Info', width = w, height = h, command = button10Click)
button10.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button11 = tk.Button(window, text = 'Debug', width = w, height = h, command = button11Click)
button11.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button12 = tk.Button(window, text = 'Show All', width = w, height = h, command = button12Click)
button12.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button13 = tk.Button(window, text = 'Show all_data', width = w, height = h, command = button13Click)
button13.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button14 = tk.Button(window, text = 'Send Data', width = w, height = h, command = button14Click)
button14.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button15 = tk.Button(window, text = 'Clear', width = w, height = h, command = button15Click)
button15.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button00.place(x = x_st + dx * 0, y = y_st + dy * 0)
button01.place(x = x_st + dx * 1, y = y_st + dy * 0)
button02.place(x = x_st + dx * 2, y = y_st + dy * 0)
button03.place(x = x_st + dx * 3, y = y_st + dy * 0)
button04.place(x = x_st + dx * 4, y = y_st + dy * 0)
button05.place(x = x_st + dx * 5, y = y_st + dy * 0)
button10.place(x = x_st + dx * 0, y = y_st + dy * 1)
button11.place(x = x_st + dx * 1, y = y_st + dy * 1)
button12.place(x = x_st + dx * 2, y = y_st + dy * 1)
button13.place(x = x_st + dx * 3, y = y_st + dy * 1)
button14.place(x = x_st + dx * 4, y = y_st + dy * 1)
button15.place(x = x_st + dx * 5, y = y_st + dy * 1)

# 加入 Label
msg = tk.StringVar()
label1 = tk.Label(window, text = '選擇顯示站別：')
label1.pack()
label1.place(x = x_st + dx * 0, y = y_st + dy * 2 - 20)
label2 = tk.Label(window, fg = 'red', textvariable = msg)
label2.pack()
label2.place(x = x_st + dx * 0, y = y_st + dy * 2 + 50)

# 加入 Checkbutton
dx2 = dx * 3 / 4
for i in range(0, len(stage_no)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text = stage_no[i], variable = choice[i], command = choose)
    item.pack()
    item.place(x = x_st + dx2 * (i % 8), y = y_st + dy * 2 + int(i / 8) * 25)

# 加入 Text
text1 = tk.Text(window, width = 100, height = 30)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 3)

window.mainloop()











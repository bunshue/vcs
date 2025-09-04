"""

準備做資料庫用

"""
# 同一個資料庫內 可以放多個table table名稱不同即可

print("------------------------------------------------------------")  # 60個
print("準備工作")

import os
import sys
import csv
import time
import sqlite3
import tkinter as tk
import tkinter as tk
from tkinter.filedialog import askopenfile  # tk之openFileDialog
from tkinter.filedialog import asksaveasfile  # tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

flag_debug_mode = True

# 建立csv二維串列資料
all_data = []

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
    "第1站 下蓋清潔",
    "第2站 點膠",
    "第3站 前2站NG",
    "第4站 模組接合",
    "第5站 間隙檢查",
    "第6站 UV固化",
    "第7站 點膠線檢查",
    "第8站 前4站NG",
    "第9站 氣密測試",
    "第10站 Hi-pot",
    "第11站 色調",
    "第12站 前3站NG",
    "第13a站 等級判定",
    "第13b站 資料燒錄",
    "第14站 前2站NG",
    "第15站 包裝出料",
]

table_list = [
    "table01",
    "table02",
    "table03",
    "table04",
    "table05",
    "table06",
    "table07",
    "table08",
    "table09",
    "table10",
    "table11",
    "table12",
    "table13a",
    "table13b",
    "table14",
    "table15",
]

list_stage_list = [
    "list_stage01",
    "list_stage02",
    "list_stage03",
    "list_stage04",
    "list_stage05",
    "list_stage06",
    "list_stage07",
    "list_stage08",
    "list_stage09",
    "list_stage10",
    "list_stage11",
    "list_stage12",
    "list_stage13a",
    "list_stage13b",
    "list_stage14",
    "list_stage15",
]


stage = -1
tablename = ""
db_filename = ""
db_filename = "tmp_db_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"

dummy_data = "abcd"
count = 0

print("------------------------------------------------------------")  # 60個

# 公用副程式


# 取得一個資料庫內所有表單的名稱, list格式
def get_table_names(conn):
    table_names = []
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in tables.fetchall():
        table_names.append(table[0])
    return table_names


# 取得一個表單內所有欄位的名稱, list格式
def get_column_names(conn, table_name):
    column_names = []
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names


# 清除記憶體內的資料
def clear_all_data():
    global all_data
    all_data = []

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


print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import stat


def walk_python_files(paths):
    for path in paths:
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for filename in files:
                    if filename.endswith(".csv"):
                        print(filename)


foldername1 = "D:/_git/vcs/_1.data/______test_files3"

paths = [foldername1]
walk_python_files(paths)

filename = "D:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

print("全檔名/長檔名 : ", filename)


filename1 = filename.split(".")[-2]  # 取得檔案名稱(不添加副檔名)

print(filename1)
print("前檔名 : ", filename1)

foldername = os.path.dirname(filename)
print("全資料夾 : ", foldername)


"""
sql 
資料庫準備資料

D:/AAAA/BBBB/CCCC/DDDD/EEEE.mp4	4.64GB

全檔名、長檔名			D:/AAAA/BBBB/CCCC/DDDD/EEEE.mp4
簡檔名、短檔名			EEEE.mpg
前檔名				EEEE
全路徑 全資料夾 長路徑 長資料夾	D:/AAAA/BBBB/CCCC/DDDD
短路徑 短資料夾			DDDD
副檔名				mp4
檔案大小			4.46GB
影片格式			W = 1920, H =1080


描述1				kaede
描述2				kaede
描述3				kaede


另有更好

中文版

4K
非1080p

720p
480p

name
airi
anna
sora
jun
3333
7777

series

gggg
debut

ssss	same
dddd	delete
mmmm

"""


# 我的sql規劃

"""
table01
        string          int             string
	filename	filesize	description
第1筆 : filename1       123             'aaaa'
第2筆 : filename2       456             'bbbb'
第3筆 : filename3       789             'cccc'

updatetime
        string
	updatetime
第1筆 : 2023-05-29 13:57:39.206064
第2筆 : 2023-05-29 13:57:43.085771
第3筆 : 2023-05-29 13:57:48.938803
"""

filename1 = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "D:/_git/vcs/_1.data/______test_files1/file2.txt"
filename3 = "D:/_git/vcs/_1.data/______test_files1/bear.jpg"

import os
import time
import datetime
import sqlite3

db_filename = "tmp_my_db.sqlite"

# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線

cursor = conn.cursor()  # 建立 cursor 物件

print("建立一個資料表")

# 若資料庫已存在 則不用重新建立

sqlstr = 'CREATE TABLE IF NOT EXISTS table01 ("filename" TEXT NOT NULL, "filesize"  INT, "description"  TEXT NOT NULL)'

"""
print('建立表單')
cursor.execute("CREATE TABLE table01"
"("
"   filename varchar(32),"
"   filesize varchar(32)"
")")
cursor.execute("INSERT INTO table01"
"  (filename, filesize)"
"  VALUES"
"  (?, ?)",
('aaaa.mp4', '12345'))
"""

cursor.execute(sqlstr)
conn.commit()  # 更新

print("新增資料 3 筆")
# Insert
filename = filename1
filesize = os.path.getsize(filename1)
description = "aaaa"
sqlstr = "INSERT INTO table01 VALUES('{}','{}','{}');".format(
    filename, filesize, description
)
cursor.execute(sqlstr)

filename = filename2
filesize = os.path.getsize(filename2)
description = "bbbb"
sqlstr = "INSERT INTO table01 VALUES('{}','{}','{}');".format(
    filename, filesize, description
)
cursor.execute(sqlstr)

filename = filename3
filesize = os.path.getsize(filename3)
description = "cccc"
sqlstr = "INSERT INTO table01 VALUES('{}','{}','{}');".format(
    filename, filesize, description
)
cursor.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("建立資料庫連線, 寫入時間戳記")

# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件
print("建立一個資料表")
# 若資料庫已存在 則不用重新建立
sqlstr = 'CREATE TABLE IF NOT EXISTS updatetime ("updatetime" TEXT NOT NULL)'
cursor.execute(sqlstr)
conn.commit()  # 更新

print("新增資料 1 筆")
# Insert
current_time = datetime.datetime.now()  # 取得現在時間
sqlstr = "INSERT INTO updatetime VALUES('{}');".format(current_time)
cursor.execute(sqlstr)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("不是用fetchall()讀取 全部資料")
# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM table01")
i = 0
for row in cursor:
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 : ", end="")
    # print(rows[i])
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
    i = i + 1
conn.close()  # 關閉資料庫連線

print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM table01")
rows = cursor.fetchall()  # 讀取全部資料
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 : ", end="")
    # print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線

print("用fetchall()讀取 全部資料 依 filesize 排序, 降冪")
# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
# cursor = conn.execute('SELECT * FROM table01 ORDER BY filesize;')#由小到大, 升冪
cursor = conn.execute(
    "SELECT * FROM table01 ORDER BY filesize DESC;"
)  # 由小到大 + 反相 = 由大到小, 降冪
rows = cursor.fetchall()  # 讀取全部資料
length = len(rows)
print("共有", length, "筆資料")
for i in range(length):
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 : ", end="")
    # print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線


print("不是用fetchall()讀取 全部資料")
# print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename)  # 建立資料庫連線
cursor = conn.execute("SELECT * FROM updatetime")
i = 0
for row in cursor:
    # print(type(rows[i]))
    print("第" + str(i + 1) + "筆資料 : ", end="")
    # print(rows[i])
    print("{}".format(row[0]))
    i = i + 1
conn.close()  # 關閉資料庫連線


# ----------------------------------------------------------------


def read_from_db():
    # 還有其他站 TBD,  還要讀出資料後 將資料 加/附加 到list裏

    if db_filename == "":
        message = "尚未開啟資料庫, 離開"
        print(message)
        text1.insert("end", message)
        return

    global all_data
    all_data = []
    message = ""

    print("從資料庫讀出全部資料")

    conn = sqlite3.connect(db_filename)  # 建立資料庫連線

    print("目前資料庫 : " + db_filename)

    conn = sqlite3.connect(db_filename)

    table_names = get_table_names(conn)
    print(type(table_names))
    talbe_names_length = len(table_names)
    if talbe_names_length <= 0:
        print("資料庫內無表單, 離開")
        conn.close()
        return

    print("裡面有:", talbe_names_length, " 個表單")

    conn.close()

    table_data_exists = False
    for table_name in table_names:
        if table_name == "table01":
            print("第1站資料存在")
            table_data_exists = True

    if table_data_exists == False:
        print("無第1站資料, 離開")
        return

    print("第1站")
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    cursor = conn.execute("SELECT * FROM table01")
    rows = cursor.fetchall()
    # print(rows)
    index = 1
    for row in rows:
        print(len(row))
        # print('{}\t{}'.format(row[0], row[1]))
        # print(row)
        all_data.append(row)
        index += 1
    conn.close()  # 關閉資料庫連線

    table_data_exists = False
    for table_name in table_names:
        if table_name == "table02":
            print("第1站資料存在")
            table_data_exists = True

    if table_data_exists == False:
        print("無第2站資料, 離開")
        return

    print("第2站")
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    cursor = conn.execute("SELECT * FROM table02")
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        # print('{}\t{}'.format(row[0], row[1]))
        # print(row)
        all_data.append(row)
        message = message + str(row) + "\n"
    conn.close()  # 關閉資料庫連線
    text1.insert("end", message)

    for i in range(1, len(table_list)):
        print("檢查 : ", table_list[i])

        table_data_exists = False
        for table_name in table_names:
            if table_name == table_list[i]:
                print("表單: ", table_list[i], " 存在")
                table_data_exists = True

        if table_data_exists == False:
            print("表單: ", table_list[i], " 不存在")
            continue

        print("讀取表單: ", table_list[i], " 資料")
        conn = sqlite3.connect(db_filename)  # 建立資料庫連線

        sqlstr = "SELECT * FROM {}".format(table_list[i])
        # print(sqlstr)
        cursor = conn.execute(sqlstr)
        rows = cursor.fetchall()
        # print(rows)
        for row in rows:
            # print('{}\t{}'.format(row[0], row[1]))
            # print(row)
            all_data.append(row)
            message = message + str(row) + "\n"
        conn.close()  # 關閉資料庫連線
        text1.insert("end", message)

    message = "從資料庫讀出全部資料 完成"
    print(message)
    text1.insert("end", message)


def show_all_data():
    print("show_all_data")
    """
    length = len(all_data)
    print('all_data 資料長度 : ', length)
    for i in range(0, length):
        print(all_data[i])
    """


def export_data():
    print("export_data")
    """
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
    """


def button00Click():
    print("你按了 新建資料庫")
    global db_filename
    db_filename = "db_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".sqlite"
    message = "資料庫 : " + db_filename
    print(message)
    text1.insert("end", message)
    main_message1.set(message)

    print("新建資料庫, 清除記憶體資料")
    # clear_all_data()


def button01Click():
    print("你按了 開啟資料庫")
    button01_text.set("開啟資料庫...")
    file = askopenfile(
        parent=window, mode="rb", title="選取資料庫", filetypes=[("資料庫檔案", "*.sqlite")]
    )
    if file:
        global db_filename
        db_filename = file.name
        message = "資料庫 : " + db_filename
        print(message)
        text1.insert("end", message)
        main_message1.set(message)

    button01_text.set("開啟資料庫")
    print("開啟資料庫, 清除記憶體資料")
    # clear_all_data()


def button02Click():
    print("你按了 讀取資料庫資料")
    global db_filename
    if db_filename == "":
        message = "尚未開啟資料庫, 離開"
        print(message)
        text1.insert("end", message)
        return

    # read_from_db()


def button03Click():
    print("你按了 匯入生產資料並將資料加入資料庫")
    global db_filename
    print(db_filename)
    if db_filename == "":
        message = "尚未開啟資料庫, 離開"
        print(message)
        text1.insert("end", message)
        return

    # import_csv_data()
    # merge_stage_data()


def button04Click():
    print("你按了 匯入資料庫 TBD")


def button05Click():
    print("你按了 匯出生產資料")
    export_data()


def button10Click():
    print("你按了button10")
    show_info()


def button11Click():
    print("你按了button11")
    # precheck_csv_data()


def button12Click():
    print("你按了button12")
    # show_list_stage()
    # show_all_data()


def button13Click():
    print("你按了button13")


def button14Click():
    # print('你按了button14')
    set_data()


def button15Click():
    # print('你按了button15')
    clear_text1()


def set_data():
    """
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + dummy_data
    print(mesg)
    text1.insert('end', mesg)
    """
    global count
    count = count + 1
    message = "  次數" + str(count)
    text1.insert("end", message)


def clear_text1():
    text1.delete(1.0, "end")
    # 執行 clear 函式時，清空內容


def choose():
    str = "選擇："
    for i in range(0, len(choice)):
        if choice[i].get() == 1:
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
# size = str(W)+'x'+str(H)
# size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title("自動化產線生產資料庫")

# 設定主視窗之背景色
# window.configure(bg = "#7AFEC6")

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width=w, height=h, command=button00Click, text="新建資料庫")
button00.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)

# 開啟資料庫按鈕
# button01 = tk.Button(window, width = w, height = h, command = button01Click, text = '開啟資料庫')
# button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01_text = tk.StringVar()
# button01 = tk.Button(window, textvariable = button01_text, command = lambda:button01Click(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button01 = tk.Button(
    window,
    textvariable=button01_text,
    width=w,
    height=h,
    command=lambda: button01Click(),
)
# button01 = tk.Button(window, command = xxxxxxx, text='選取檔案')
button01_text.set("開啟資料庫")

button02 = tk.Button(window, width=w, height=h, command=button02Click, text="讀取資料庫資料")
button02.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button03 = tk.Button(
    window, width=w, height=h, command=button03Click, text="匯入生產資料\n將資料加入資料庫"
)
button03.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button04 = tk.Button(window, width=w, height=h, command=button04Click, text="匯入資料庫")
button04.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button05 = tk.Button(window, width=w, height=h, command=button05Click, text="匯出生產資料")
button05.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button00.place(x=x_st + dx * 0, y=y_st + dy * 0)
button01.place(x=x_st + dx * 1, y=y_st + dy * 0)
button02.place(x=x_st + dx * 2, y=y_st + dy * 0)
button03.place(x=x_st + dx * 3, y=y_st + dy * 0)
button04.place(x=x_st + dx * 4, y=y_st + dy * 0)
button05.place(x=x_st + dx * 5, y=y_st + dy * 0)

if flag_debug_mode == True:
    button10 = tk.Button(window, width=w, height=h, command=button10Click, text="Info")
    button10.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
    button11 = tk.Button(
        window, width=w, height=h, command=button11Click, text="檢查csv/db"
    )
    button11.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
    button12 = tk.Button(
        window, width=w, height=h, command=button12Click, text="顯示記憶體資料"
    )
    button12.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
    button13 = tk.Button(window, width=w, height=h, command=button13Click, text="")
    button13.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
    button14 = tk.Button(
        window, width=w, height=h, command=button14Click, text="Send Data"
    )
    button14.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
    button15 = tk.Button(window, width=w, height=h, command=button15Click, text="Clear")
    button15.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)

    button10.place(x=x_st + dx * 0, y=y_st + dy * 1)
    button11.place(x=x_st + dx * 1, y=y_st + dy * 1)
    button12.place(x=x_st + dx * 2, y=y_st + dy * 1)
    button13.place(x=x_st + dx * 3, y=y_st + dy * 1)
    button14.place(x=x_st + dx * 4, y=y_st + dy * 1)
    button15.place(x=x_st + dx * 5, y=y_st + dy * 1)

font_size = 20

# 加入 Label
label_message1 = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=main_message1
)
label_message1.pack()
label_message1.place(x=5, y=0 + 10)
main_message1.set("")

label_message2 = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=main_message2
)
label_message2.pack()
label_message2.place(x=5 + W * 3 / 4, y=0 + 10)
main_message2.set("")

msg = tk.StringVar()
label1 = tk.Label(window, text="選擇顯示站別：")
label1.pack()
label1.place(x=x_st + dx * 0, y=y_st + dy * 2 - 20)
label2 = tk.Label(window, fg="red", textvariable=msg)
label2.pack()
label2.place(x=x_st + dx * 0, y=y_st + dy * 2 + 80)

# 加入 Checkbutton
dx2 = dx * 4 / 4  # 為了微調距離用
for i in range(0, len(stage_no)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text=stage_no[i], variable=choice[i], command=choose)
    item.pack()
    item.place(x=x_st + dx2 * (i % 6), y=y_st + dy * 2 + int(i / 6) * 25)

# 加入 Text
text1 = tk.Text(window, width=100, height=30)  # 放入多行輸入框
text1.pack()
text1.place(x=x_st + dx * 0, y=y_st + dy * 3 + 50)

message = "尚未開啟資料庫"
main_message1.set(message)

window.mainloop()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

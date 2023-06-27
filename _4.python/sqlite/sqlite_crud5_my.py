'''

準備做資料庫用


'''

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



TB = 1024 * 1024 * 1024 * 1024  #定義TB的計算常量
GB = 1024 * 1024 * 1024         #定義GB的計算常量
MB = 1024 * 1024                #定義MB的計算常量
KB = 1024                       #定義KB的計算常量

def ByteConversionTBGBMBKB(size):
    if size < 0:
        return "不合法的數值"
    elif (size / TB >= 1024):    #如果目前Byte的值大於等於1024TB
        return "無法表示"
    elif (size / TB >= 1):   #如果目前Byte的值大於等於1TB
        return format(size / TB, ".2f") + " TB" #將其轉換成TB
    elif (size / GB >= 1):   #如果目前Byte的值大於等於1GB
        return format(size / GB, ".2f") + " GB" #將其轉換成GB
    elif (size / MB >= 1):   #如果目前Byte的值大於等於1MB
        return format(size / MB, ".2f") + " MB" #將其轉換成MB
    elif (size / KB >= 1):   #如果目前Byte的值大於等於1KB
        return format(size / KB, ".2f") + " KB" #將其轉換成KB
    else:
        return str(size) + " Byte"    #顯示Byte值

filesize = 123456
print('filesize = ', filesize , '\t檔案大小 : ', ByteConversionTBGBMBKB(filesize))

foldername1 = 'C:/_git/vcs/_1.data/______test_files3'

paths = [foldername1]
walk_python_files(paths)




filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

print('全檔名/長檔名 : ', filename)


filename1 = filename.split(".")[-2] # 取得檔案名稱(不添加副檔名)

print(filename1)
print('前檔名 : ', filename1)

foldername = os.path.dirname(filename)
print('全資料夾 : ', foldername)


'''
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

'''

filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

'''
ST_SIZE: 普通文件以字節為單位的大小；包含等待某些特殊文件的數據。
ST_ATIME: 上次訪問的時間。
ST_MTIME: 最後一次修改的時間。
ST_CTIME: 由操作系統報告的"ctime"。在某些系統上（如Unix）是最新的元數據更改的時間，在其它系統上（如Windows）是創建時間（詳細信息參見平臺的文檔）。
'''

statinfo = os.stat(filename)
#print(statinfo)

filesize = statinfo[stat.ST_SIZE]
create_time = statinfo[stat.ST_CTIME]
modify_time = statinfo[stat.ST_MTIME]
access_time = statinfo[stat.ST_ATIME]

'''
print('檔案建立時間\t', create_time)
print('最後修改時間\t', modify_time)
print('最後存取時間\t', access_time)
'''

print('檔案大小:\t', filesize, ' 拜')
print('檔案大小:\t', ByteConversionTBGBMBKB(filesize))
print("建立日期:\t", time.ctime(create_time))
print("修改時間:\t", time.ctime(modify_time))
print("存取時間:\t", time.ctime(access_time))

'''
filesize = os.path.getsize(filename)
print("檔案大小\t" + str(filesize) + " 拜")
print("建立日期:\t", os.path.getmtime(filename))
print("建立日期:\t", time.ctime(os.path.getmtime(filename)))
'''




#我的sql規劃

'''
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
'''

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/file2.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'

import os
import time
import datetime
import sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files2/my_db.sqlite';

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線

cursor = conn.cursor() # 建立 cursor 物件

print('建立一個資料表')

#若資料庫已存在 則不用重新建立

sqlstr = 'CREATE TABLE IF NOT EXISTS table01 ("filename" TEXT NOT NULL, "filesize"  INT, "description"  TEXT NOT NULL)'

'''
print('建立表單')
cursor.execute("CREATE TABLE talbe01"
"("
"   filename varchar(32),"
"   filesize varchar(32)"
")")
cursor.execute("INSERT INTO talbe01"
"  (filename, filesize)"
"  VALUES"
"  (?, ?)",
('aaaa.mp4', '12345'))
'''

cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 3 筆')
#Insert
filename = filename1
filesize = os.path.getsize(filename1)
description = 'aaaa'
sqlstr = "INSERT INTO table01 VALUES('{}','{}','{}');".format(filename, filesize, description)
cursor.execute(sqlstr)

filename = filename2
filesize = os.path.getsize(filename2)
description = 'bbbb'
sqlstr = "INSERT INTO table01 VALUES('{}','{}','{}');".format(filename, filesize, description)
cursor.execute(sqlstr)

filename = filename3
filesize = os.path.getsize(filename3)
description = 'cccc'
sqlstr = "INSERT INTO table01 VALUES('{}','{}','{}');".format(filename, filesize, description)
cursor.execute(sqlstr)

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print('建立資料庫連線, 寫入時間戳記')

#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件
print('建立一個資料表')
#若資料庫已存在 則不用重新建立
sqlstr = 'CREATE TABLE IF NOT EXISTS updatetime ("updatetime" TEXT NOT NULL)'
cursor.execute(sqlstr)
conn.commit() # 更新

print('新增資料 1 筆')
#Insert
current_time = datetime.datetime.now() # 取得現在時間
sqlstr = "INSERT INTO updatetime VALUES('{}');".format(current_time)
cursor.execute(sqlstr)

conn.commit() # 更新
conn.close()  # 關閉資料庫連線

print('不是用fetchall()讀取 全部資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM table01')
i = 0
for row in cursor:
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
    i = i + 1
conn.close()  # 關閉資料庫連線

print('用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM table01')
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線

print('用fetchall()讀取 全部資料 依 filesize 排序, 降冪')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
#cursor = conn.execute('SELECT * FROM table01 ORDER BY filesize;')#由小到大, 升冪
cursor = conn.execute('SELECT * FROM table01 ORDER BY filesize DESC;')#由小到大 + 反相 = 由大到小, 降冪
rows = cursor.fetchall()    #讀取全部資料
length = len(rows)
print('共有', length, '筆資料')
for i in range(length):
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}\t{}\t{}".format(rows[i][0], rows[i][1], rows[i][2]))
conn.close()  # 關閉資料庫連線


print('不是用fetchall()讀取 全部資料')
#print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM updatetime')
i = 0
for row in cursor:
    #print(type(rows[i]))
    print('第' + str(i + 1) + '筆資料 : ', end = "")
    #print(rows[i])
    print("{}".format(row[0]))
    i = i + 1
conn.close()  # 關閉資料庫連線



#----------------------------------------------------------------







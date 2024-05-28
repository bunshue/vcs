import sqlite3

print("------------------------------------------------------------")  # 60個

#delete.py

conn = sqlite3.connect('singMatch.db') 	# 連線資料庫
selId = int(input('請輸入要移除的 編號 : '))
sql = 'DELETE FROM 參賽者 WHERE 編號 = {0}'.format(selId)
conn.execute(sql)                      	# 執行SQL指令
print('編號 = {0} 的記錄 已經刪除....'.format(selId))
conn.commit()                           # 更新資料庫
conn.close()  

print("------------------------------------------------------------")  # 60個

#insert01.py

conn = sqlite3.connect('singMatch.db')  # 連線資料庫
print ('請輸入「參賽者」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newName = input('姓名 : ')
    newSex = input('性別 : ')
    newTel = input('電話 : ')
    record = (newId, newName, newSex, newTel)
    sql = 'INSERT INTO 參賽者 VALUES(?,?,?,?)'
    conn.execute(sql,record)           # 執行SQL指令
    conn.commit()                      # 更新資料庫
    again = input('是否繼續輸入資料 ? ')
conn.close()                          # 關閉資料庫

print("------------------------------------------------------------")  # 60個

#insert02.py

import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql1 = 'CREATE TABLE IF NOT EXISTS 音色( \
        編號 INTEGER UNIQUE NOT NULL, \
        音色50 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「音色」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('音色50 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 音色 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()

print("------------------------------------------------------------")  # 60個

#insert03.py

import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql1 = 'CREATE TABLE IF NOT EXISTS 技巧( \
         編號 INTEGER UNIQUE NOT NULL, \
         技巧30 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「技巧」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('技巧30 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 技巧 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()

print("------------------------------------------------------------")  # 60個

#insert04.py

import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql1 = 'CREATE TABLE IF NOT EXISTS 儀態( \
         編號 INTEGER UNIQUE NOT NULL, \
         儀態20 INTEGER)'
conn.execute(sql1)                         	# 執行SQL指令

print ('請輸入「儀態」資料表的記錄資料')
again = 'y'
while again.lower() == 'y':
    newId = int(input('編號 : '))
    newScore = int(input('儀態20 : '))
    record = (newId, newScore)
    sql2 = 'INSERT INTO 儀態 VALUES(?,?)'
    conn.execute(sql2,record)
    conn.commit()
    again = input('是否繼續輸入資料 ? ')
conn.close()

print("------------------------------------------------------------")  # 60個

#match.py

import sqlite3

def fnCreateTable():
    sql1 = 'CREATE TABLE IF NOT EXISTS 參賽者( \
            編號 INTEGER UNIQUE NOT NULL, \
            姓名 TEXT, \
            性別 TEXT, \
            電話 TEXT)'
    conn.execute(sql1)
    
    sql2 = 'CREATE TABLE IF NOT EXISTS 音色( \
            編號 INTEGER UNIQUE NOT NULL, \
            音色50 INTEGER)'
    conn.execute(sql2)
    
    sql3 = 'CREATE TABLE IF NOT EXISTS 技巧( \
            編號 INTEGER UNIQUE NOT NULL, \
            技巧30 INTEGER)'
    conn.execute(sql3)
    
    sql4 = 'CREATE TABLE IF NOT EXISTS 儀態( \
            編號 INTEGER UNIQUE NOT NULL, \
            儀態20 INTEGER)'
    conn.execute(sql4)
    
    anykey = input('請按 <enter>鍵 繼續...')
    
def fnInsert01():
    print ('\n請輸入「參賽者」資料表的記錄資料')
    again = 'y'
    while again.lower() == 'y':
        newId = int(input('編號 : '))
        newName = input('姓名 : ')
        newSex = input('性別 : ')
        newTel = input('電話 : ')
        record = (newId, newName, newSex, newTel)
        sql = 'INSERT INTO 參賽者 VALUES(?,?,?,?)'
        conn.execute(sql,record)
        conn.commit()
        again = input('是否繼續輸入資料 ? ')

def fnSelect01():
    sql = 'SELECT * FROM 參賽者'
    data = conn.execute(sql)
    print('編號\t姓名\t性別\t電話')
    for rec in data:
        print('%d\t%s\t%s\t%s' %(rec[0],rec[1],rec[2],rec[3]))
    anykey = input('請按 <enter>鍵 繼續...')

def fnDelect01():
    delId = int(input('請輸入要刪除的參賽者編號: '))
    sql = 'DELETE FROM 參賽者 WHERE 編號 = {0}'.format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input('請按 <enter>鍵 繼續...')

def fnInsert02():
    print ('\n請輸入「音色」資料表的記錄資料')
    again = 'y'
    while again.lower() == 'y':
        newId = int(input('編號 : '))
        newScore = int(input('音色50 : '))
        record = (newId, newScore)
        sql = 'INSERT INTO 音色 VALUES(?,?)'
        conn.execute(sql,record)
        conn.commit()
        again = input('是否繼續輸入資料 ? ')

def fnSelect02():
    sql = 'SELECT * FROM 音色'
    data = conn.execute(sql)
    print('編號\t音色50')
    for rec in data:
        print('%d\t%d' %(rec[0],rec[1]))
    anykey = input('請按 <enter>鍵 繼續...')

def fnDelect02():
    delId = int(input('請輸入要刪除的音色編號: '))
    sql = 'DELETE FROM 音色 WHERE 編號 = {0}'.format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input('請按 <enter>鍵 繼續...')

def fnInsert03():
    print ('\n請輸入「技巧」資料表的記錄資料')
    again = 'y'
    while again.lower() == 'y':
        newId = int(input('編號 : '))
        newScore = int(input('技巧30 : '))
        record = (newId, newScore)
        sql = 'INSERT INTO 技巧 VALUES(?,?)'
        conn.execute(sql,record)
        conn.commit()
        again = input('是否繼續輸入資料 ? ')

def fnSelect03():
    sql = 'SELECT * FROM 技巧'
    data = conn.execute(sql)
    print('編號\t技巧30')
    for rec in data:
        print('%d\t%d' %(rec[0],rec[1]))
    anykey = input('請按 <enter>鍵 繼續...')

def fnDelect03():
    delId = int(input('請輸入要刪除的技巧編號: '))
    sql = 'DELETE FROM 技巧 WHERE 編號 = {0}'.format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input('請按 <enter>鍵 繼續...')

def fnInsert04():
    print ('\n請輸入「儀態」資料表的記錄資料')
    again = 'y'
    while again.lower() == 'y':
        newId = int(input('編號 : '))
        newScore = int(input('儀態20 : '))
        record = (newId, newScore)
        sql = 'INSERT INTO 儀態 VALUES(?,?)'
        conn.execute(sql,record)
        conn.commit()
        again = input('是否繼續輸入資料 ? ')

def fnSelect04():
    sql = 'SELECT * FROM 儀態'
    data = conn.execute(sql)
    print('編號\t儀態20')
    for rec in data:
        print('%d\t%d' %(rec[0],rec[1]))
    anykey = input('請按 <enter>鍵 繼續...')

def fnDelect04():
    delId = int(input('請輸入要刪除的儀態編號: '))
    sql = 'DELETE FROM 儀態 WHERE 編號 = {0}'.format(delId)
    conn.execute(sql)
    conn.commit()
    anykey = input('請按 <enter>鍵 繼續...')

def fnRelation():
    print ('編號\t姓名\t音色50\t技巧30\t儀態20\t總分')
    sql = 'SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
           技巧.技巧30,儀態.儀態20 from 參賽者 \
           INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
           INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
           INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號'
    result = conn.execute(sql)
    for r in result:
        tot = r[2] + r[3] + r[4]
        print('%d\t%s\t%d\t%d\t%d\t%d' %(r[0],r[1],r[2],r[3],r[4],tot))
    anykey = input('請按 <enter>鍵 繼續...')

#####  主程式  #####
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
while True:
    print('\n*** 博碩歌唱比賽評分管理系統 ***')
    print('    1. 建立資料表')
    print('    2. 管理 參賽者 資料表')
    print('    3. 管理 音色 資料表')
    print('    4. 管理 技巧 資料表')
    print('    5. 管理 儀態 資料表')
    print('    6. 顯示 比賽總成績')
    print('    7. 離開系統')
    print('===========================')
    n = input('請選擇操作項目: ')
    
    if n == '1':
        fnCreateTable()
    elif n == '2':
        while True:
            print('\n** 管理 參賽者 資料表 **')
            print('   1. 新增記錄')
            print('   2. 查詢記錄')
            print('   3. 刪除記錄')
            print('   4. 回上一層操作')
            print('-------------------------')
            n2 = int(input('請選擇管理項目: '))
            if n2 == 1:
                fnInsert01()
            elif n2 == 2:
                fnSelect01()
            elif n2 == 3:
                fnDelect01()
            elif n2 == 4:
                break
    elif n == '3':
        while True:
            print('\n** 管理 音色 資料表 **')
            print('   1. 新增記錄')
            print('   2. 查詢記錄')
            print('   3. 刪除記錄')
            print('   4. 回上一層操作')
            print('-------------------------')
            n3 = int(input('請選擇管理項目: '))
            if n3 == 1:
                fnInsert02()
            elif n3 == 2:
                fnSelect02()
            elif n3 == 3:
                fnDelect02()
            elif n3 == 4:
                break
    elif n == '4':
        while True:
            print('\n** 管理 技巧 資料表 **')
            print('   1. 新增記錄')
            print('   2. 查詢記錄')
            print('   3. 刪除記錄')
            print('   4. 回上一層操作')
            print('-------------------------')
            n4 = int(input('請選擇管理項目: '))
            if n4 == 1:
                fnInsert03()
            elif n4 == 2:
                fnSelect03()
            elif n4 == 3:
                fnDelect03()
            elif n4 == 4:
                break
    elif n == '5':
        while True:
            print('\n** 管理 儀態 資料表 **')
            print('   1. 新增記錄')
            print('   2. 查詢記錄')
            print('   3. 刪除記錄')
            print('   4. 回上一層操作')
            print('-------------------------')
            n5 = int(input('請選擇管理項目: '))
            if n5 == 1:
                fnInsert04()
            elif n5 == 2:
                fnSelect04()
            elif n5 == 3:
                fnDelect04()
            elif n5 == 4:
                break
    elif n == '6':
        fnRelation()
    elif n == '7':
        break
    
conn.close()         
            

print("------------------------------------------------------------")  # 60個

#relation.py

import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫

print ('編號\t姓名\t音色50\t技巧30\t儀態20\t總分')
sql = 'SELECT 參賽者.編號,參賽者.姓名,音色.音色50, \
       技巧.技巧30,儀態.儀態20 from 參賽者 \
       INNER JOIN 音色 ON 音色.編號 = 參賽者.編號 \
       INNER JOIN 技巧 ON 技巧.編號 = 參賽者.編號 \
       INNER JOIN 儀態 ON 儀態.編號 = 參賽者.編號'
result = conn.execute(sql)
for r in result:
    tot = r[2] + r[3] + r[4]
    print('%d\t%s\t%d\t%d\t%d\t%d' %(r[0],r[1],r[2],r[3],r[4],tot))
conn.close()

print("------------------------------------------------------------")  # 60個

#select01.py

conn = sqlite3.connect('singMatch.db')  # 連線資料庫
sql = 'SELECT * FROM 參賽者'            
data = conn.execute(sql)                # 執行SQL指令,傳回記錄資料
print('編號\t姓名\t性別\t電話')
for rec in data:
    print('%d\t%s\t%s\t%s' %(rec[0],rec[1],rec[2],rec[3]))
conn.close()                          # 關閉資料庫

print("------------------------------------------------------------")  # 60個

#select02.py

conn = sqlite3.connect('singMatch.db')  # 連線資料庫
sql = 'SELECT 姓名,電話 FROM 參賽者'            
data = conn.execute(sql)                # 執行SQL指令,傳回記錄資料
print('姓名\t電話')
for rec in data:
    print('%s\t%s' %(rec[0],rec[1]))
conn.close()                           # 關閉資料庫

print("------------------------------------------------------------")  # 60個

#select03.py

conn = sqlite3.connect('singMatch.db')  # 連線資料庫
selId = int(input('請輸入要查詢的 編號 : '))
sql = 'SELECT * FROM 參賽者 WHERE 編號 = {0}'.format(selId)
data = conn.execute(sql)                # 執行SQL指令,傳回記錄資料
print('編號\t姓名\t性別\t電話')
for rec in data:
    print('%d\t%s\t%s\t%s' %(rec[0],rec[1],rec[2],rec[3]))
conn.close()                          # 關閉資料庫

print("------------------------------------------------------------")  # 60個

#select04.py

conn = sqlite3.connect('singMatch.db')  # 連線資料庫
selName = input('請輸入要查詢的 姓名 : ')
sql = 'SELECT * FROM 參賽者 WHERE 姓名 = "{0}"'.format(selName)
data = conn.execute(sql)                # 執行SQL指令,傳回記錄資料
print('編號\t姓名\t性別\t電話')
for rec in data:
    print('%d\t%s\t%s\t%s' %(rec[0],rec[1],rec[2],rec[3]))
conn.close()                          # 關閉資料庫

print("------------------------------------------------------------")  # 60個

#table.py

import sqlite3                             	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db')    	# 連線資料庫
sql = 'CREATE TABLE IF NOT EXISTS 參賽者( \
       編號 INTEGER UNIQUE NOT NULL,\
       姓名 TEXT, \
       性別 TEXT, \
       電話 TEXT)'
conn.execute(sql)                          	# 執行SQL指令
conn.close()                               	# 關閉資料庫

print("------------------------------------------------------------")  # 60個

#update.py

import sqlite3                         	# 匯入sqlite3套件
conn = sqlite3.connect('singMatch.db') 	# 連線資料庫
selId = int(input('請輸入要異動的 編號 : '))
print('\n選擇要異動的欄位名稱...')
field = input('1.姓名  2.性別  3.電話 ..... ? ')
if field == '1':
    newName = input('姓名 :')
    sql = 'UPDATE 參賽者 \
           SET 姓名 = "{0}" \
           WHERE 編號 = {1}'.format(newName, selId)
elif field == '2':
    newSex = input('性別 :')
    sql = 'UPDATE 參賽者 \
           SET 性別 = "{0}" \
           WHERE 編號 = {1}'.format(newSex, selId)
elif field == '3':
    newTel = input('電話 :')
    sql = 'UPDATE 參賽者 \
           SET 電話 = "{0}" \
           WHERE 編號 = {1}'.format(newTel, selId)
   
conn.execute(sql)                      	# 執行SQL指令
conn.commit()                           # 更新資料庫
conn.close()                           	# 關閉資料庫

print("------------------------------------------------------------")  # 60個


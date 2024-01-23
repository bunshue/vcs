import sys
import csv

#csv檔 逗號分隔值(comma-seperated values)

#csvWriter = csv.writer(csvFile, delimiter='\t') # 建立Writer物件, 使用TAB區分項目 不使用逗號

#先寫後讀

print('------------------------------------------------------------')	#60個

print("寫入CSV檔 1 writer")
filename = 'tmp_animals1.csv'
csvfile = open(filename, 'w+', newline = '')
try:
    writer = csv.writer(csvfile)
    # 寫入欄位名稱
    writer.writerow(("中文名","英文名","體重","全名"))
    # 寫入資料(12筆)
    writer.writerow(("鼠","mouse",3,"米老鼠"))
    writer.writerow(("牛","ox",48,"班尼牛"))
    writer.writerow(("虎","tiger",33,"跳跳虎"))
    writer.writerow(("兔","rabbit",8,"彼得兔"))
    writer.writerow(("龍","dragon",38,"逗逗龍"))
    writer.writerow(("蛇","snake",16,"貪吃蛇"))
    writer.writerow(("馬","horse",36,"草泥馬"))
    writer.writerow(("羊","goat",29,"喜羊羊"))
    writer.writerow(("猴","monkey",22,"山道猴"))
    writer.writerow(("雞","chicken",6,"肯德雞"))
    writer.writerow(("狗","dog",12,"貴賓狗"))
    writer.writerow(("豬","pig",42,"佩佩豬"))
finally:
    csvfile.close()

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print('------------------------------------------------------------')	#60個

print("寫入CSV檔 2 DictWriter")
filename = 'tmp_animals2.csv'
with open(filename, 'w', newline = '') as csvfile:
    # 定義欄位
    fieldnames = ['中文名', '英文名', '體重', '全名']

    writer = csv.DictWriter(csvfile, fieldnames = fieldnames) # 建立Writer物件

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料, 將 dictionary 寫入 csv 檔
    writer.writerow({'中文名': "鼠", '英文名': "mouse", '體重': 3, '全名': "米老鼠"})
    writer.writerow({'中文名': "牛", '英文名': "ox", '體重': 48, '全名': "班尼牛"})
    writer.writerow({'中文名': "虎", '英文名': "tiger", '體重': 33, '全名': "跳跳虎"})
    writer.writerow({'中文名': "兔", '英文名': "rabbit", '體重': 8, '全名': "彼得兔"})
    writer.writerow({'中文名': "龍", '英文名': "dragon", '體重': 38, '全名': "逗逗龍"})
    writer.writerow({'中文名': "蛇", '英文名': "snake", '體重': 16, '全名': "貪吃蛇"})
    writer.writerow({'中文名': "馬", '英文名': "horse", '體重': 36, '全名': "草泥馬"})
    writer.writerow({'中文名': "羊", '英文名': "goat", '體重': 29, '全名': "喜羊羊"})
    writer.writerow({'中文名': "猴", '英文名': "monkey", '體重': 22, '全名': "山道猴"})
    writer.writerow({'中文名': "雞", '英文名': "chicken", '體重': 6, '全名': "肯德雞"})
    writer.writerow({'中文名': "狗", '英文名': "dog", '體重': 12, '全名': "貴賓狗"})
    writer.writerow({'中文名': "豬", '英文名': "pig", '體重': 42, '全名': "佩佩豬"})

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print('------------------------------------------------------------')	#60個

print("寫入CSV檔 3 二維串列資料 一次寫入")

filename = 'tmp_animals3a.csv'

# 建立csv二維串列資料
csvtable = [
        ['中文名', '英文名', '體重', '全名'],
        ["鼠","mouse",3,"米老鼠"],
        ["牛","ox",48,"班尼牛"],
        ["虎","tiger",33,"跳跳虎"],
        ["兔","rabbit",8,"彼得兔"],
        ["龍","dragon",38,"逗逗龍"],
        ["蛇","snake",16,"貪吃蛇"],
        ["馬","horse",36,"草泥馬"],
        ["羊","goat",29,"喜羊羊"],
        ["猴","monkey",22,"山道猴"],
        ["雞","chicken",6,"肯德雞"],
        ["狗","dog",12,"貴賓狗"],
        ["豬","pig",42,"佩佩豬"],
]

# 開啟輸出的 csv 檔案
#with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
with open(filename, 'w', newline = '') as csvfile:
    # 建立 csv 檔寫入物件
    writer = csv.writer(csvfile)

    # 寫入二維串列資料
    writer.writerows(csvtable)

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("寫入CSV檔 3 二維串列資料 一次寫一行(row)")

filename = 'tmp_animals3b.csv'

with open(filename, 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in csvtable:
        writer.writerow(row)

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print("python讀寫CSV檔 1 讀取 gggg")

filename = 'data/python_ReadWrite_CSV2.csv'

#讀取方法相同 印出資料方法1
with open(filename, newline = '') as csvfile:
    rows = csv.reader(csvfile)  # 讀取 csv 檔案內容
    print(type(rows))

    # 以迴圈顯示每一列
    for row in rows:
        print(type(row))
        print(len(row))
        print(row)

#讀取方法相同 印出資料方法2, 完整地讀取每一個元素
with open(filename, newline = '') as csvfile:
    rows = csv.reader(csvfile)  # 讀取 csv 檔案內容
    print(type(rows))

    datas = list(rows)    #將資料轉成list
    length = len(datas)
    print('len = ', length)
    #print(datas)
    data_column = len(datas[0])
    print('data_column = ', data_column)
    for row in datas:
        print(row)
        print(type(row))
        #print(len(row))

print('------------------------------------------------------------')	#60個

print("python讀寫CSV檔 3 讀取")

from urllib.request import urlopen
from io import StringIO

#遠端檔案
filename_r1 = 'http://pythonscraping.com/files/MontyPythonAlbums.csv'
print('讀取一個遠端csv檔案 : ' + filename_r1)

#本地檔案
filename_r2 = 'data/MontyPythonAlbums.local.csv'

print('讀取一個本地csv檔案 : ' + filename_r2)

#讀取遠端檔案
#data = urlopen(filename_r1).read().decode('ascii', 'ignore')

#讀取本地檔案
data = open(filename_r2).read()

csvfile = StringIO(data)

rows = csv.reader(csvfile)  # 讀取 csv 檔案內容

for row in rows:
	print("The album \"" + row[0] + "\" was released in " + str(row[1]))

print('------------------------------------------------------------')	#60個

"""
print("python讀寫CSV檔 4 讀取 many")

filename = 'data/zipcode.csv'

with open(filename, 'r', encoding = 'utf-8') as csvfile:
    rows = csv.reader(csvfile)  # 讀取 csv 檔案內容
    for row in rows:
        if row != "":
            sqlstr = "insert into zipcode (Zip5, City, Area, Road, Scope) values ('{}', '{}', '{}', '{}', '{}')".format(row[0], row[1], row[2], row[3], row[4])
            #print(sqlstr) many
            #cursor.execute(sqlstr)
"""
print('------------------------------------------------------------')	#60個

print("python讀寫CSV檔 7 讀取")

filename = 'data/python_ReadWrite_CSV3_eword.csv'

count = 0
with open(filename, 'r', encoding = 'UTF-8-sig') as csvfile:
    for line in csvfile:
        eword, cword = line.rstrip('\n').split(',')
        word1 = {eword : cword}
        print(word1)
        word2 = {'eword' : eword, 'cword' : cword}
        print(word2)
        count += 1
        if count == 10:
            break

print('------------------------------------------------------------')	#60個
print("python讀寫CSV檔 8 讀取")

filename = 'data/python_ReadWrite_CSV1.csv'

with open(filename, 'rt') as csvfile:
    data = csvfile.readlines()
print(type(data))
print(data)

print('------------------------------------------------------------')	#60個

print("python讀寫CSV檔 11 讀取")

filename = 'data/python_ReadWrite_CSV1.csv'
import pprint as pp
data = list()
with open(filename, 'rt') as csvfile:
    columns = csvfile.readline().split(",")
    for item in csvfile.readlines():
        temp = dict()
        for i, field in enumerate(item.split(",")):
            temp[columns[i].strip()] = field.strip()
        data.append(temp)
pp.pprint(data)

print('------------------------------------------------------------')	#60個
print("python讀寫CSV檔 12 讀取 pandas")

import pandas as pd

filename = 'data/twstock_all.csv'

pd.options.mode.chained_assignment = None  #取消顯示pandas資料重設警告

df = pd.read_csv(filename, encoding='big5')  #以pandas讀取檔案
dfprice=pd.DataFrame(df['收盤價'])
    
print(df)

print()

print(dfprice)

print('------------------------------------------------------------')	#60個

'''
print('------------------------------------------------------------')	#60個

print('讀取 csv 檔案')
filename = 'csvReport.csv'
with open(filename, encoding='utf-8') as csvFile: # 開啟csv檔案
    csvReader = csv.reader(csvFile)         # 讀檔案建立Reader物件
    listReport = list(csvReader)            # 將資料轉成串列  
for row in listReport:  
    print(row)                              # 輸出串列

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('讀取 csv 檔案')
infilename = 'csvReport.csv'                  # 來源檔案
outfilename = 'out19_6.csv'                   # 目的檔案
with open(infilename, encoding='utf-8') as csvRFile: # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)    # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列 

"""
print('寫入 csv 檔案')   一讀一寫
with open(outfilename,'w',newline='') as csvOFile:  
    csvWriter = csv.writer(csvOFile)    # 建立Writer物件   
    for row in listReport:              # 將串列寫入
        csvWriter.writerow(row)
"""
print('------------------------------------------------------------')	#60個

filename = 'csvReport2.csv'
with open(filename) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == 'Steve':
        if row[1] == '2025':
            total2025 += int(row[5])
        if row[1] == '2026':
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)

'''
print('------------------------------------------------------------')	#60個

""" many
filename_r = 'data/workfile.csv'
filename_w = 'tmp_csv9.csv'

#一讀一寫
print('讀取csv檔, 檔案 :', filename_r)

with open(filename_r, 'r') as fin:
    with open(filename_w, 'w') as fout:
        read = csv.reader(fin, delimiter=',')
        write = csv.writer(fout, delimiter=',')
        header = next(read)
        print(header)
        # get number of columns
        #array = header.split(',')
        first_item = header[0]
        write.writerow(header)
        for row in read:
            print(','.join(row))
            write.writerow(row)
            print(row[2])

print('寫入csv檔, 檔案 :', filename_w)
"""

print('------------------------------------------------------------')	#60個

'''
print("------------------------------------------------------------")  # 60個

print('讀取csv檔')

csvfile = "data/pl.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))

print()
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

'''

print('------------------------------------------------------------')	#60個

filename = 'data/python_ReadWrite_CSV2.csv'
print("讀取CSV檔 1 DictReader, 檔案 :", filename)

data = list()
with open(filename, newline = '') as csvfile:
    rows = csv.DictReader(csvfile)      # 讀取 csv 檔內容，將每一列轉成 dictionary
    print(type(rows))
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row['姓名'], row['身高'], row['體重'])
        print(row)
        data.append(dict(row))

print(type(data))
print(len(data))
print(data)
print(len(data[0]))
print(type(data[0]))
print(data[0])
print(data[0]['姓名'])
print(data[0]['身高'])
print(data[0]['體重'])
print(len(data[1]))
print(type(data[1]))
print(data[1])
print(data[1]['姓名'])
print(data[1]['身高'])
print(data[1]['體重'])

print('------------------------------------------------------------')	#60個

filename = 'data/python_ReadWrite_CSV1.csv'
print("讀取CSV檔 2 DictReader, 檔案 :", filename)

import pprint as pp

data = list()
with open(filename, 'rt') as csvfile:
    rows = csv.DictReader(csvfile)      # 讀取 csv 檔內容，將每一列轉成 dictionary
    print(type(rows))
    for row in rows:
        data.append(dict(row))
pp.pprint(data)

print('------------------------------------------------------------')	#60個

filename = 'data/python_ReadWrite_CSV1.csv'
print("讀取CSV檔 3 DictReader, 檔案 :", filename)

import pprint as pp

with open(filename, 'rt') as csvfile:
    rows = csv.DictReader(csvfile)      # 讀取 csv 檔內容，將每一列轉成 dictionary
    data = [dict(row) for row in rows]
pp.pprint(data)

print('------------------------------------------------------------')	#60個

filename = 'data/csvPeople.csv'
print("讀取CSV檔 4 DictReader, 檔案 :", filename)

with open(filename) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 列出DictReader各列內容
        print(row)

    for row in csvDictReader:               # 列出DictReader各列內容
        print(row['first_name'], row['last_name'])
        
print('------------------------------------------------------------')	#60個

filename = 'data/member.csv'
print("讀取CSV檔 5 DictReader, 檔案 :", filename)

# 讀取 CSV 檔案並提取電子郵件地址
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['姓名'], end = "\t")   #不能用
        print(row['電子郵件'], end = "\t")
        print(row['體重'])

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

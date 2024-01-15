import sys

#各種檔案寫讀範例 csv 1

#csv檔 逗號分隔值(comma-seperated values)

import csv

print('------------------------------------------------------------')	#60個
print("python讀寫CSV檔 1 寫入")

filename = 'tmp_csv1.csv'

print("打開一個csv檔案 : " + filename)
csvfile = open(filename, 'w+', newline = '')

try:
    writer = csv.writer(csvfile)
    writer.writerow(('column1', 'column2', 'column3'))
    writer.writerow((1, 2, 3))
    writer.writerow(('', '', '', 4, 5, 6))   #前幾欄是空的
    writer.writerow((7, 8,'', 9))         #空一欄
    writer.writerow((7, 8, 9))
    writer.writerow(('a', 'b', 'c'))
    writer.writerow(('lion', 'mouse', 'cat', 'dog'))
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvfile.close()

print("寫入檔案 " + filename + " 完成")

print('------------------------------------------------------------')	#60個
print("python讀寫CSV檔 2 寫入")

filename = 'tmp_csv2.csv'
with open(filename, 'w', newline = '') as csvfile:
    # 定義欄位
    fieldnames = ['姓名', '身高', '體重']

    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'姓名': 'Chiou', '身高': 170, '體重': 65})
    writer.writerow({'姓名': 'David', '身高': 183, '體重': 78})

print("寫入檔案 " + filename + " 完成")
    
print('------------------------------------------------------------')	#60個
print("python讀寫CSV檔 3 寫入")

filename = 'tmp_csv3.csv'
with open(filename, 'w', newline = '') as csvfile:
  # 建立 csv 檔寫入物件
  writer = csv.writer(csvfile)

  # 寫入欄位名稱
  writer.writerow(['姓名', '身高', '體重'])
  # 寫入資料
  writer.writerow(['Chiou', 170, 65])
  writer.writerow(['David', 183, 78])

print("寫入檔案 " + filename + " 完成")

print('------------------------------------------------------------')	#60個

print("python讀寫CSV檔 4 寫入")

filename = 'tmp_csv4.csv'

# 建立csv二維串列資料
csvtable = [
        ['姓名', '身高', '體重'],
        ['Chiou', 170, 65],
        ['David', 183, 78],
]

# 開啟輸出的 csv 檔案
with open(filename, 'w', newline = '') as csvfile:
    # 建立 csv 檔寫入物件
    writer = csv.writer(csvfile)

    # 寫入二維串列資料
    writer.writerows(csvtable)

print("寫入檔案 " + filename + " 完成")

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
print("python讀寫CSV檔 2 讀取")

filename = 'data/python_ReadWrite_CSV2.csv'

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
print("python讀寫CSV檔 4 讀取 many")

filename = 'data/zipcode.csv'

with open(filename, 'r', encoding = 'utf-8') as csvfile:
    rows = csv.reader(csvfile)  # 讀取 csv 檔案內容
    for row in rows:
        if row != "":
            sqlstr = "insert into zipcode (Zip5, City, Area, Road, Scope) values ('{}', '{}', '{}', '{}', '{}')".format(row[0], row[1], row[2], row[3], row[4])
            #print(sqlstr) many
            #cursor.execute(sqlstr)

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
print("python讀寫CSV檔 9 讀取")

filename = 'data/python_ReadWrite_CSV1.csv'
import pprint as pp

data = list()
with open(filename, 'rt') as csvfile:
    rows = csv.DictReader(csvfile)      # 讀取 csv 檔內容，將每一列轉成 dictionary
    print(type(rows))
    for row in rows:
        data.append(dict(row))
pp.pprint(data)

print('------------------------------------------------------------')	#60個
print("python讀寫CSV檔 10 讀取")

filename = 'data/python_ReadWrite_CSV1.csv'
import pprint as pp

with open(filename, 'rt') as csvfile:
    rows = csv.DictReader(csvfile)      # 讀取 csv 檔內容，將每一列轉成 dictionary
    data = [dict(row) for row in rows]
pp.pprint(data)

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

print("python讀寫CSV檔 13")

import csv

filename = 'tmp_csv5_list1.csv'

data = [
    ['姓名', '身高', '體重'],
    ['王小明', 174, 56],
    ['林小華', 185, 80],
    ['陳小強', 168, 60] ]

with open(filename, 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerows(data)
    
print("done")

print('------------------------------------------------------------')	#60個

import csv
filename = 'tmp_csv5_list2.csv'

data = [
    ['王小明', 174, 56],
    ['林小華', 185, 80],
    ['陳小強', 168, 60] ]

with open(filename, 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(['姓名', '身高', '體重'])
    csvwriter.writerows(data)
print("done")
        
print('------------------------------------------------------------')	#60個


import os
import sys
import time
import random

'''
print('------------------------------------------------------------')	#60個

import csv

print('讀取 csv 檔案')
fn = 'csvReport.csv'
with open(fn, encoding='utf-8') as csvFile: # 開啟csv檔案
    csvReader = csv.reader(csvFile)         # 讀檔案建立Reader物件
    listReport = list(csvReader)            # 將資料轉成串列  
for row in listReport:  
    print(row)                              # 輸出串列

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])

print('------------------------------------------------------------')	#60個

import csv

print('讀取 csv 檔案')

fn = 'csvPeople.csv'
with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 列出DictReader各列內容
        print(row)

    for row in csvDictReader:               # 列出DictReader各列內容
        print(row['first_name'], row['last_name'])
        
print('------------------------------------------------------------')	#60個

import csv

print('寫入 csv 檔案')

fn = 'out19_5.csv'
with open(fn,'w',newline='') as csvFile:  # 開啟csv檔案
    csvWriter = csv.writer(csvFile)       # 建立Writer物件   
    csvWriter.writerow(['姓名', '年齡', '城市'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])

print('------------------------------------------------------------')	#60個

import csv

print('讀取 csv 檔案')
infn = 'csvReport.csv'                  # 來源檔案
outfn = 'out19_6.csv'                   # 目的檔案
with open(infn, encoding='utf-8') as csvRFile: # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)    # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列 

"""
print('寫入 csv 檔案')
with open(outfn,'w',newline='') as csvOFile:  
    csvWriter = csv.writer(csvOFile)    # 建立Writer物件   
    for row in listReport:              # 將串列寫入
        csvWriter.writerow(row)
"""
print('------------------------------------------------------------')	#60個

import csv

print('寫入 csv 檔案')
fn = 'out19_7.csv'
with open(fn, 'w', newline = '') as csvFile:        # 開啟csv檔案
    csvWriter = csv.writer(csvFile, delimiter='\t') # 建立Writer物件   
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])

print('------------------------------------------------------------')	#60個

import csv

print('寫入 csv 檔案')
fn = 'out19_8.csv'
with open(fn, 'w', newline = '') as csvFile:                # 開啟csv檔案
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)  # 建立Writer物件

    dictWriter.writeheader()                                # 寫入標題
    dictWriter.writerow({'Name':'Hung', 'Age':'35', 'City':'Taipei'})
    dictWriter.writerow({'Name':'James', 'Age':'40', 'City':'Chicago'})

print('------------------------------------------------------------')	#60個

fn = 'csvReport2.csv'
with open(fn) as csvFile:               # 開啟csv檔案
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

import csv

filename_r = 'data/workfile.csv'
filename_w = 'tmp_csv9.csv'

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


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個






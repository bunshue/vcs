
print("------------------------------------------------------------")  # 60個



import sys

import csv
import numpy as np

#csv檔 逗號分隔值(comma-seperated values)

#預設使用','分隔, 也可以使用其他分隔符號
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

import random
print("寫入CSV檔 3a 一維串列資料 一次寫入")

filename = 'tmp_1d_array.csv'

# 建立csv一維串列資料

print("一維 串列")
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

# 開啟輸出的 csv 檔案
#with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
with open(filename, 'w', newline = '') as csvfile:
    # 建立 csv 檔寫入物件
    writer = csv.writer(csvfile)

    # 寫入一維串列資料
    writer.writerows(np.array(animals))

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("寫入CSV檔 3b 二維串列資料 一次寫入")

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

print("寫入CSV檔 3c 二維串列資料 一次寫一行(row)")

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
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個

import pathlib

infile = "data/namelist.csv"
f = pathlib.Path(infile).open(encoding="UTF-8")
dataReader = csv.reader(f)
for row in dataReader:          #取得每一列資料
    for value in row:           #取得資料時，以逗號間隔
        print(value)
        
print("------------------------------------------------------------")  # 60個

import pathlib

infile = "xxxxx.csv"
try:
    f = pathlib.Path(infile).open(encoding="UTF-8")
    dataReader = csv.reader(f)
    for row in dataReader:          #取得每一列資料
        for value in row:           #取得資料時，以逗號間隔
            print(value)
except:
    print("無法載入檔案。")

print("------------------------------------------------------------")  # 60個

filename = 'data/csvReport2.csv'
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

print("------------------------------------------------------------")  # 60個

print('2025年1月台北天氣報告')

filename = 'data/TaipeiWeatherJan.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []                       
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        meanTemps.append(int(row[2]))    # 儲存均溫
        lowTemps.append(int(row[3]))     # 儲存最低溫

print('高溫', highTemps)
print('均溫', meanTemps)
print('低溫', lowTemps)

print("------------------------------------------------------------")  # 60個

import ast

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores.csv'

scores = dict()
with open(filename,'r') as fp:
    filedata = fp.read()
    #scores = ast.literal_eval(filedata)
print("以下是{}成績檔的字典型態資料:".format(filename))

print("------------------------------------------------------------")  # 60個

#擷取登入帳號資訊

def passwd_to_dict(filename):
    users = {}
    with open(filename) as f:
        for line in f:
            user_info = line.split(':')
            users.update({user_info[0]: user_info[2]})
    return users

print(passwd_to_dict(r'.\data\passwd.cfg'))

#擷取登入帳號資訊（生成版）

def passwd_to_dict_2(filename):
    with open(filename) as f:
        d = {words[0]: words[2]
             for words
             in [line.split(':') for line in f]}
    return d

print(passwd_to_dict_2(r'.\data\passwd.cfg'))


def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, 'r') as f_read, \
            open(csv_filename, 'w', newline='') as f_write:
        csv_reader = csv.reader(f_read, delimiter=':')
        csv_writer = csv.writer(f_write, delimiter='\t', lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])

passwd_to_csv(r'.\data\passwd.cfg', r'tmp_passwd.csv')

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/animals.csv'

try:
    with open(filename, encoding = 'utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))

print('------------------------------------------------------------')	#60個

csvfile = "data/Example.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))

print("------------------------------------------------------------")  # 60個

csvfile = "data/Example2.csv"
list1 = [[10,33,45], [5, 25, 56]]
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["Data1","Data2","Data3"])
    for row in list1:
        writer.writerow(row)

print("------------------------------------------------------------")  # 60個


fn = 'data/csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    
for row in listReport:                  # 迴圈輸出串列內容
    print(row)

print("------------------------------------------------------------")  # 60個

fn = 'data/csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])

print("------------------------------------------------------------")  # 60個

fn = 'data/csvPeople.csv'
with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 列出DictReader各列內容
        print(row)

print("------------------------------------------------------------")  # 60個

fn = 'data/csvPeople.csv'
with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 列出DictReader各列內容
        print(row['first_name'], row['last_name'])

print("------------------------------------------------------------")  # 60個

fn = 'tmp_01.csv'
with open(fn,'w',newline='',encoding="utf-8") as csvFile: # 開啟csv檔案
    csvWriter = csv.writer(csvFile)                     # 建立Writer物件   
    csvWriter.writerow(['姓名', '年齡', '城市'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])

print("------------------------------------------------------------")  # 60個

infn = 'data/csvReport.csv'                          # 來源檔案
outfn = 'tmp_02.csv'                           # 目的檔案
with open(infn,encoding='utf-8') as csvRFile:   # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)            # 讀檔案建立Reader物件
    listReport = list(csvReader)                # 將資料轉成串列 

with open(outfn,'w',newline='',encoding="utf-8") as csvOFile:  
    csvWriter = csv.writer(csvOFile)            # 建立Writer物件   
    for row in listReport:                      # 將串列寫入
        csvWriter.writerow(row)

print("------------------------------------------------------------")  # 60個

fn = 'tmp_03.csv'
with open(fn, 'w', newline = '') as csvFile:        # 開啟csv檔案
    csvWriter = csv.writer(csvFile, delimiter='\t') # 建立Writer物件   
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])

print("------------------------------------------------------------")  # 60個

fn = 'tmp_04.csv'
with open(fn, 'w', newline = '') as csvFile:                # 開啟csv檔案
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)  # 建立Writer物件

    dictWriter.writeheader()                                # 寫入標題
    dictWriter.writerow({'Name':'Hung', 'Age':'35', 'City':'Taipei'})
    dictWriter.writerow({'Name':'James', 'Age':'40', 'City':'Chicago'})

print("------------------------------------------------------------")  # 60個

# 定義串列,元素是字典
dictList = [{'姓名':'Hung','年齡':'35','城市':'台北'},  
          {'姓名':'James', '年齡':'40', '城市':'芝加哥'}]
          
fn = 'tmp_05.csv'
with open(fn, 'w', newline = '', encoding = 'utf-8') as csvFile:  
    fields = ['姓名', '年齡', '城市']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)  # 建立Writer物件
    dictWriter.writeheader()                                # 寫入標題
    for row in dictList:                                    # 寫入內容
        dictWriter.writerow(row)

print("------------------------------------------------------------")  # 60個

fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)     # 讀取文件下一列
print(headerRow)

for i, header in enumerate(headerRow):
    print(i, header)

print("------------------------------------------------------------")  # 60個

fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)         # 讀取文件下一列
    highTemps, lowTemps = [], []        # 設定空串列
    for row in csvReader:
        highTemps.append(row[1])        # 儲存最高溫
        lowTemps.append(row[3])         # 儲存最低溫

print("最高溫 : ", highTemps)
print("最低溫 : ", lowTemps)    

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一列
    highTemps = []                          # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))       # 儲存最高溫
plt.figure(figsize=(12, 8))                 # 設定繪圖區大小                  
plt.plot(highTemps)
plt.title("2025年1月台北天氣報告", fontsize=24)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一列
    dates, highTemps = [], []               # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))       # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)
       
plt.figure(figsize=(12, 8))                 # 設定繪圖區大小                  
plt.plot(dates, highTemps)                  # 圖標增加日期刻度
plt.title("2025年1月台北天氣報告", fontsize=24)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一列
    dates, highTemps = [], []               # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))       # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)
       
fig = plt.figure(figsize=(12, 8))           # 設定繪圖區大小                  
plt.plot(dates, highTemps)                  # 圖標增加日期刻度
fig.autofmt_xdate()                         # 預設最佳化角度旋轉
plt.title("2025年1月台北天氣報告", fontsize=24)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一列
    dates, highTemps = [], []               # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))       # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)
       
fig = plt.figure(figsize=(12, 8))           # 設定繪圖區大小                  
plt.plot(dates, highTemps)                  # 圖標增加日期刻度
fig.autofmt_xdate(rotation=60)              # 日期旋轉60度
plt.title("2025年1月台北天氣報告", fontsize=24)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一列
    dates, highTemps, lowTemps = [], [], [] # 設定空串列
    for row in csvReader:
        try:                    
            currentDate = datetime.strptime(row[0], "%Y/%m/%d")
            highTemp = int(row[1])          # 設定最高溫
            lowTemp = int(row[3])           # 設定最低溫
        except Exception:
            print('有缺值')
        else:
            highTemps.append(highTemp)      # 儲存最高溫
            lowTemps.append(lowTemp)        # 儲存最低溫
            dates.append(currentDate)       # 儲存日期
       
fig = plt.figure(figsize=(12, 8))           # 設定繪圖區大小
plt.plot(dates, highTemps)                  # 繪製最高溫
plt.plot(dates, lowTemps)                   # 繪製最低溫
plt.fill_between(dates,highTemps,lowTemps,color='y',alpha=0.2) # 填滿
fig.autofmt_xdate()                         # 日期旋轉
plt.title("2025年1月台北天氣報告", fontsize=24)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split('/'))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/ST43_3479_202310.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    for _ in range(5):                              # 跳過前 5 列
        next(csvReader)
    all_rows = list(csvReader)
    data_without_last_row = all_rows[:-1]           # 跳過最後一列
    
    mydates, highPrices, lowPrices, closePrices = [], [], [], []    
    
    for row in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d") # 轉換後日期
            highPrice = eval(row[4])                # 設定最高價
            lowPrice = eval(row[5])                 # 設定最低價
            closePrice = eval(row[6])               # 設定收盤價
        except Exception:
            print(f'有缺值 {row}')
        else:
            highPrices.append(highPrice)            # 儲存最高價
            lowPrices.append(lowPrice)              # 儲存最低價
            closePrices.append(closePrice)          # 儲存收盤價
            mydates.append(currentDate)             # 儲存日期

fig = plt.figure(figsize=(12, 8))                   # 設定繪圖區大小
plt.plot(mydates, highPrices, '-*', label='最高價')    # 繪製最高價
plt.plot(mydates, lowPrices, '-o', label='最低價')     # 繪製最低價
plt.plot(mydates, closePrices, '-^', label='收盤價')   # 繪製收盤價
plt.legend()
fig.autofmt_xdate()                                 # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel('價格', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split('/'))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'data/ST43_3479_202310.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    all_rows = list(csvReader)
    data_row = all_rows[5:-1]                       # 切片
    
    mydates, highPrices, lowPrices, closePrices = [], [], [], []    
    
    for row in data_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d") # 轉換後日期
            highPrice = eval(row[4])                # 設定最高價
            lowPrice = eval(row[5])                 # 設定最低價
            closePrice = eval(row[6])               # 設定收盤價
        except Exception:
            print(f'有缺值 {row}')
        else:
            highPrices.append(highPrice)            # 儲存最高價
            lowPrices.append(lowPrice)              # 儲存最低價
            closePrices.append(closePrice)          # 儲存收盤價
            mydates.append(currentDate)             # 儲存日期

fig = plt.figure(figsize=(12, 8))                   # 設定繪圖區大小
plt.plot(mydates, highPrices, '-*', label='最高價')    # 繪製最高價
plt.plot(mydates, lowPrices, '-o', label='最低價')     # 繪製最低價
plt.plot(mydates, closePrices, '-^', label='收盤價')   # 繪製收盤價
plt.legend()
fig.autofmt_xdate()                                 # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel('價格', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 

df.to_csv("vehicles.csv",index=False,encoding="big5")

df.to_json("vehicles1.json")
df.to_json("vehicles2.json", force_ascii = False)

"""
#匯出DataFrame
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)
df.to_excel(filename)
df.to_sql(table, con = engine)

#匯入DataFrame
df.read_csv(filename)
df.read_json(filename)
df.read_html(filename)
df.read_excel(filename)
df.read_sql(query, engine)
"""
import pandas as pd

df1 = pd.read_csv("vehicles.csv", encoding="big5")
df2 = pd.read_json("vehicles.json")
print(df1)
print(df2)


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

import sys
import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

# pip install xlsxwriter

#data = pd.read_csv('data/ExpensesRecord.csv')
df = pd.read_excel('data/ExpensesRecord.xls', 'sheet')
#data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df.head(5) )

from pandas import ExcelWriter

writer = ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')
writer.save()

print('------------------------------------------------------------')	#60個

df = pd.read_csv('data/ExpensesRecord.csv')
print(df.head(5) )
df.to_csv("test.csv")

print('------------------------------------------------------------')	#60個

"""
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0].head(5) )

#df = pd.read_html('http://news.baidu.com/tech')
#print(df[0].head(5) )
"""

print('------------------------------------------------------------')	#60個

DataFrame = pd.read_csv('data/ExpensesRecord.csv')
print(DataFrame["說明"])
print(DataFrame[["說明","支出金額"]] )

df = pd.DataFrame({'Math': [90, 91,92, 93, 94],'English': np.arange(80,85,1) })
print(df[["Math","English"]])

print('------------------------------------------------------------')	#60個

DataFrame = pd.read_csv('data/ExpensesRecord.csv')
DataFrame["單價"]=DataFrame["支出金額"]/DataFrame["數量"]
print(DataFrame[["數量","支出金額","單價"]] )

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# 3 filter'

print("--------------------")
print(df['Date'] == '2018-01-05')
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'
print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())

#  5 matplotlib
import matplotlib.pyplot as plt
df.plot(x='Date', y='Open',grid=True, color='blue')
plt.show()

import matplotlib.pyplot as plt
df.plot( y='diff',grid=True, color='red',kind='hist')
plt.show()

fig, ax = plt.subplots()
for name, group in df.groupby('month'):
    group.plot(x='day', y='Open', ax=ax, label=name)
plt.show()

fileds=['Open','Close','High']
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x='Date', y=name, ax=ax, label=name)
plt.show()

dfMonths = df.loc[df['month'].isin([1,2,3,4,5,6,7])]
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(values = 'High', columns = 'month', index = 'day')
dfMonthsPivot.plot(kind = 'box',title = 'Months High')
plt.show()


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




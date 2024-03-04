import sys

print("------------------------------------------------------------")  # 60個

import pathlib
import csv

infile = "data/namelist.csv"
f = pathlib.Path(infile).open(encoding="UTF-8")
dataReader = csv.reader(f)
for row in dataReader:          #取得每一列資料
    for value in row:           #取得資料時，以逗號間隔
        print(value)
        
print("------------------------------------------------------------")  # 60個

import pathlib
import csv

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

import csv

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

import csv

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

import csv

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

import csv

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/animals.csv'

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

import csv

csvfile = "data/Example.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))

print("------------------------------------------------------------")  # 60個

import csv

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



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


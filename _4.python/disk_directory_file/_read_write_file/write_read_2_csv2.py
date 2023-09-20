import os
import sys
import time
import random

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

'''
print('寫入 csv 檔案')
with open(outfn,'w',newline='') as csvOFile:  
    csvWriter = csv.writer(csvOFile)    # 建立Writer物件   
    for row in listReport:              # 將串列寫入
        csvWriter.writerow(row)
'''
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


print('------------------------------------------------------------')	#60個



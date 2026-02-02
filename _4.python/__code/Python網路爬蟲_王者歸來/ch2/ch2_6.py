# ch2_6.py
import csv

fn = 'csvPeople.csv'
with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 使用迴圈列出字典內容
        print(row['first_name'], row['last_name'])




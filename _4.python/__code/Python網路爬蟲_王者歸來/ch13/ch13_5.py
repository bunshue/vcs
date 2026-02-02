# ch13_5.py
import csv
import pandas as pd

fn = 'out13_4.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    

for row in listReport:                  # 將'-'改為'0'
    while '-' in row:
        i = row.index('-')
        row[i] = '0'    

time_period = listReport[0]             # 將第一個串列改為columns
time_period = time_period[1:]

listReport = listReport[1:]             # 切片

bank = []
newReport = []
for row in listReport:                  # 取得index
    bank.append(row[0])
    newReport.append(row[1:])           # 建立新利率串列

df = pd.DataFrame(newReport,columns=time_period,index=bank)

print(df)



# ch22_1.py
import csv

fn = 'csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    
for row in listReport:                  # 迴圈輸出串列內容
    print(row)




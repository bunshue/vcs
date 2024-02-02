from pathlib import Path
import csv

infile = "data/namelist.csv"
f = Path(infile).open(encoding="UTF-8")
dataReader = csv.reader(f)
for row in dataReader:          #取得每一列資料
    for value in row:           #取得資料時，以逗號間隔
        print(value)
        
print("------------------------------------------------------------")  # 60個

from pathlib import Path
import csv

infile = "xxxxx.csv"
try:
    f = Path(infile).open(encoding="UTF-8")
    dataReader = csv.reader(f)
    for row in dataReader:          #取得每一列資料
        for value in row:           #取得資料時，以逗號間隔
            print(value)
except:
    print("無法載入檔案。")

print("------------------------------------------------------------")  # 60個



import csv

filename = 'data/csvReport3.csv'
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



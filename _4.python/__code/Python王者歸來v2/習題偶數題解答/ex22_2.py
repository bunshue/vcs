# ex22_2.py
import csv

fn = 'csvReport.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
total2015 = 0
total2016 = 0
for row in listReport:
    if row[0] == 'Steve':
        if row[1] == '2015':
            total2015 += int(row[5])
        if row[1] == '2016':
            total2016 += int(row[5])

print("Steve's Total Revenue of 2015 = ", total2015)
print("Steveis Total Revenue of 2016 = ", total2016)





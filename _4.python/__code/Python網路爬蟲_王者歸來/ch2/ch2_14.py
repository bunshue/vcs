# ch2_14.py
import csv

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)         # 讀取文件下一行
    highTemps, lowTemps = [], []        # 設定空串列
    for row in csvReader:
        highTemps.append(row[1])        # 儲存最高溫
        lowTemps.append(row[3])         # 儲存最低溫

print("最高溫 : ", highTemps)
print("最低溫 : ", lowTemps)    


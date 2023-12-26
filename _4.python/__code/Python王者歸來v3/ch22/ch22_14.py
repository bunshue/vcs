# ch22_14.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'TaipeiWeatherJan.csv'
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



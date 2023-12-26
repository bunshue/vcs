# ch22_20.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一行
    dates, highTemps = [], []               # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))       # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)
       
fig = plt.figure(dpi=80, figsize=(12, 8))   # 設定繪圖區大小                  
plt.plot(dates, highTemps)                  # 圖標增加日期刻度
fig.autofmt_xdate(rotation=60)              # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()



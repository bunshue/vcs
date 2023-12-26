# ch22_15.py
import csv
import matplotlib.pyplot as plt

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一行
    highTemps = []                       # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        
plt.plot(highTemps)
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()



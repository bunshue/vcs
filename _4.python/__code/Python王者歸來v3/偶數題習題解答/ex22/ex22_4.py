# ex22_4.py
import csv
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []                       
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        meanTemps.append(int(row[2]))    # 儲存均溫
        lowTemps.append(int(row[3]))     # 儲存最低溫

seq = range(1,32)
plt.plot(seq,highTemps,seq,meanTemps,seq,lowTemps)

plt.title("2025年1月台北天氣報告", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()



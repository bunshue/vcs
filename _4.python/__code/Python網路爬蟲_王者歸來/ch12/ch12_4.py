# ch12_4.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = 'MI_30MINS.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)                   # 轉成串列
    csvData = listCsv[1:]                       # 切片刪除非成交資訊
    times, items = [], []                       # 設定空串列
    for row in csvData:
        try:
            time = row[0]                       # 時間
            item = row[1]                       # 累積成交數
        except Exception:
            print('有缺值')
        else:
            times.append(time)                  # 儲存時間
            items.append(item)                  # 儲存累積成交數
       
fig = plt.figure(dpi=80, figsize=(12, 8))       # 設定繪圖區大小
plt.plot(times, items, '-*')                    # 繪製累積成交數
fig.autofmt_xdate()                             # 時間旋轉
plt.title("Accumulated deal every 30 minutes", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Accumulated deal", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()



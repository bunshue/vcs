# ch22_18_1.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split('/'))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'ST43_3479_202310.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    all_rows = list(csvReader)
    data_row = all_rows[5:-1]                       # 切片
    
    mydates, highPrices, lowPrices, closePrices = [], [], [], []    
    
    for row in data_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d") # 轉換後日期
            highPrice = eval(row[4])                # 設定最高價
            lowPrice = eval(row[5])                 # 設定最低價
            closePrice = eval(row[6])               # 設定收盤價
        except Exception:
            print(f'有缺值 {row}')
        else:
            highPrices.append(highPrice)            # 儲存最高價
            lowPrices.append(lowPrice)              # 儲存最低價
            closePrices.append(closePrice)          # 儲存收盤價
            mydates.append(currentDate)             # 儲存日期

fig = plt.figure(figsize=(12, 8))                   # 設定繪圖區大小
plt.plot(mydates, highPrices, '-*', label='最高價')    # 繪製最高價
plt.plot(mydates, lowPrices, '-o', label='最低價')     # 繪製最低價
plt.plot(mydates, closePrices, '-^', label='收盤價')   # 繪製收盤價
plt.legend()
fig.autofmt_xdate()                                 # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel('價格', fontsize=14)
plt.show()



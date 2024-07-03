# Python 測試 twstock 6 plot

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import csv

from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split("/"))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"


plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/ST43_3479_202310.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    for _ in range(5):  # 跳過前 5 列
        next(csv_reader)
    list_data = list(csv_reader)
    data_without_last_row = list_data[:-1]  # 跳過最後一列

    mydates, highPrices, lowPrices, closePrices = [], [], [], []

    for line in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(line[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d")  # 轉換後日期
            highPrice = eval(line[4])  # 設定最高價
            lowPrice = eval(line[5])  # 設定最低價
            closePrice = eval(line[6])  # 設定收盤價
        except Exception:
            print(f"有缺值 {line}")
        else:
            highPrices.append(highPrice)  # 儲存最高價
            lowPrices.append(lowPrice)  # 儲存最低價
            closePrices.append(closePrice)  # 儲存收盤價
            mydates.append(currentDate)  # 儲存日期

fig = plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(mydates, highPrices, "-*", label="最高價")  # 繪製最高價
plt.plot(mydates, lowPrices, "-o", label="最低價")  # 繪製最低價
plt.plot(mydates, closePrices, "-^", label="收盤價")  # 繪製收盤價
plt.legend()
fig.autofmt_xdate()  # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel("價格", fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




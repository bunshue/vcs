"""
csv檔 逗號分隔值(comma-seperated values)

預設使用','分隔, 也可以使用其他分隔符號
csv_writer = csv.writer(csvFile, delimiter='\t') # 建立Writer物件, 使用TAB區分項目 不使用逗號
csv_reader = csv.reader(csvfile, delimiter="\t")  # 建立reader物件使用 '\t' 當分隔符號

先寫後讀

1. csv_writer = csv.writer() + writerows()

2. csv_dict_writer = csv.DictWriter() + writerows()

3. csv.reader()

4. csv.DictReader()

5. pandas

6. 應用範例

7. 其他 & 新進

csv常用的方法(4)

reader()	讀取CSV檔案 串列形式
writer()	寫入CSV檔案 串列形式
DictReader()	讀取CSV檔案 字典形式
DictWriter()	寫入CSV檔案 字典形式

"""
print("------------------------------------------------------------")  # 60個

import sys
import csv
import random
import pathlib
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
print("1. csv_writer = csv.writer() + writerows()")
print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 一維/2維 串列資料")

filename = "tmp_write_read_csv01aaba.csv"

# 建立 一維串列資料
print("一維 串列")
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

# 建立 二維串列資料
csvtable = [
    ["中文名", "英文名", "體重", "全名"],
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
]

# 開啟輸出的 csv 檔案
# with open(filename, 'w', encoding='utf-8', newline='') as csvfile:  # 開啟csv檔案
with open(filename, "w+", newline="") as csvfile:  # 開啟csv檔案
    # 建立 csv 檔寫入物件
    csv_writer = csv.writer(csvfile)  # 建立Writer物件

    # 寫入欄位名稱
    csv_writer.writerow(("中文名", "英文名", "體重", "全名"))

    # 寫入一維串列當做標題
    csv_writer.writerow(["中文名", "英文名", "體重"])

    # 寫入一維串列資料
    csv_writer.writerow(animals)

    # 寫入一維串列資料
    csv_writer.writerows(np.array(animals))
    
    # 寫入資料 writerow (一次一列資料, 寫入一維串列)
    csv_writer.writerow(["鼠", "mouse", 3, "米老鼠"])
    csv_writer.writerow(("鼠", "mouse", 3, "米老鼠"))
    csv_writer.writerow(("牛", "ox", 48, "班尼牛"))
    csv_writer.writerow(("虎", "tiger", 33, "跳跳虎"))
    csv_writer.writerow(["兔", "rabbit", 8, "彼得兔"])
    
    # 寫入資料 writerows (一次多列資料, 寫入二維串列)

    print("寫入CSV檔 二維串列資料 一次寫入")
    # 寫入二維串列資料
    csv_writer.writerows(csvtable)

    print("寫入CSV檔 二維串列資料 一次寫一行(row)")
    for line in csvtable:
        csv_writer.writerow(line)

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("2. csv_dict_writer = csv.DictWriter() + writerows()")
print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 DictWriter")

filename = "tmp_write_read_csv02.csv"

with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    # 定義欄位
    fieldnames = ["中文名", "英文名", "體重", "全名"]

    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # 建立Writer物件

    # 寫入欄位名稱
    csv_dict_writer.writeheader()
    # 寫入資料, 將 dictionary 寫入 csv 檔
    csv_dict_writer.writerow({"中文名": "鼠", "英文名": "mouse", "體重": 3, "全名": "米老鼠"})
    csv_dict_writer.writerow({"中文名": "牛", "英文名": "ox", "體重": 48, "全名": "班尼牛"})
    csv_dict_writer.writerow({"中文名": "虎", "英文名": "tiger", "體重": 33, "全名": "跳跳虎"})
    csv_dict_writer.writerow({"中文名": "兔", "英文名": "rabbit", "體重": 8, "全名": "彼得兔"})

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個

csvfile = open("tmp_dictWriterProduct.csv", "w", newline="")
# 建立writer物件，同時指定欄位名稱
csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["中文名", "英文名", "體重"])
csv_dict_writer.writeheader()  # 寫入欄位名稱
csv_dict_writer.writerow({"中文名": "鼠", "英文名": "mouse", "體重": 3})

# 寫入兩筆產品記錄到csv檔中
csv_dict_writer.writerow({"中文名": "牛", "英文名": "ox", "體重": 48})

csvfile.close()

print("------------------------------------------------------------")  # 60個

filename = "tmp_write_read_csv11.csv"
with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    fields = ["中文名", "英文名", "體重"]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fields)  # 建立Writer物件

    csv_dict_writer.writeheader()  # 寫入標題
    csv_dict_writer.writerow({"中文名": "鼠", "英文名": "mouse", "體重": "3"})
    csv_dict_writer.writerow({"中文名": "牛", "英文名": "ox", "體重": "48"})

print("------------------------------------------------------------")  # 60個

# 定義串列,元素是字典
dictList = [
    {"中文名": "鼠", "英文名": "mouse", "體重": "3"},
    {"中文名": "牛", "英文名": "ox", "體重": "48"},
]

filename = "tmp_write_read_csv12.csv"
with open(filename, "w", newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
    fields = ["中文名", "英文名", "體重"]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fields)  # 建立Writer物件
    csv_dict_writer.writeheader()  # 寫入標題
    for line in dictList:  # 寫入內容
        csv_dict_writer.writerow(line)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("3. csv.reader()")
print("------------------------------------------------------------")  # 60個

filename = "data/animals.csv"

# 讀取方法相同 印出資料方法1
#with open(filename, newline="") as csvfile:  # 開啟csv檔案
with open(filename, 'r', encoding='utf-8') as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容
    # 以迴圈顯示每一列
    for line in csv_reader:
        print(line)

# 讀取方法相同 印出資料方法2, 完整地讀取每一個元素
#with open(filename, newline="") as csvfile:  # 開啟csv檔案
with open(filename, 'r', encoding='utf-8') as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容

    list_data = list(csv_reader)  # 將資料轉成串列
    length = len(list_data)
    data_column = len(list_data[0])
    print("data_column = ", data_column)
    for line in list_data:
        print(line)

print("------------------------------------------------------------")  # 60個

filename = "data/animals.csv"

with open(filename, "r", encoding="UTF-8-sig") as csvfile:  # 開啟csv檔案
    for line in csvfile:
        print(line)

print("------------------------------------------------------------")  # 60個

print('測試 readline() 與 readlines()')

filename = "data/animals.csv"

with open(filename, "rt", encoding="UTF-8-sig") as csvfile:  # 開啟csv檔案
    cc = csvfile.readline() # 讀出1行
    print(cc)
    cc = csvfile.readline()  # 讀出1行
    print(cc)
    cc = csvfile.readlines()  # 從目前位置讀到檔尾 => 一維串列
    print(cc)

print("------------------------------------------------------------")  # 60個

filename = "./data/csvReport.csv"

#with open(filename) as csvfile:  # 開啟csv檔案
with open(filename, encoding="utf-8") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    list_data = list(csv_reader)  # 將資料轉成串列
    print(list_data)

filename = "data/csvReport2.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    list_data = list(csv_reader)  # 將資料轉成串列
    for line in list_data:  # 將二維串列list_data 逐列印出
        print(line)

print("------------------------------------------------------------")  # 60個

filename = "data/animals.csv"

try:
    with open(filename, encoding="utf-8") as csvfile:  # 開啟csv檔案
        csv_reader = csv.reader(csvfile)
        list_data = list(csv_reader)
except FileNotFoundError:
    print("無法打開文件:", filename)
else:
    for line in list_data:
        print("%-20s%-20s%-10s%-20s" % (line[0], line[1], line[2], line[3]))

print("------------------------------------------------------------")  # 60個

filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
print(headerRow)

for i, header in enumerate(headerRow):
    print(i, header)

print("------------------------------------------------------------")  # 60個

print("2025年1月臺北天氣報告")

filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []
    for line in csv_reader:
        highTemps.append(int(line[1]))  # 儲存最高溫
        meanTemps.append(int(line[2]))  # 儲存均溫
        lowTemps.append(int(line[3]))  # 儲存最低溫

print("高溫", highTemps)
print("均溫", meanTemps)
print("低溫", lowTemps)

print("------------------------------------------------------------")  # 60個

filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    highTemps, lowTemps = [], []  # 設定空串列
    for line in csv_reader:
        highTemps.append(line[1])  # 儲存最高溫
        lowTemps.append(line[3])  # 儲存最低溫

print("最高溫 : ", highTemps)
print("最低溫 : ", lowTemps)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("4. csv.DictReader()")
print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

list_data = list()
with open(filename, newline="") as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    # 以迴圈顯示每一列
    for line in csv_dict_reader:  # 列出DictReader各列內容
        print(line)
        list_data.append(dict(line))

print(type(list_data))
print(len(list_data))
print(list_data)

print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

import pprint as pp

list_data = list()
with open(filename, "rt") as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    for line in csv_dict_reader:  # 列出DictReader各列內容
        list_data.append(dict(line))
pp.pprint(list_data)

print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

# with open(filename, newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
with open(filename) as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    for line in csv_dict_reader:  # 列出DictReader各列內容
        print(line)
        #print(line["中文名"], line["英文名"])

print("------------------------------------------------------------")  # 60個

from io import StringIO

# 本地檔案
filename_r2 = "data/MontyPythonAlbums.local.csv"

print("讀取一個本地csv檔案 : " + filename_r2)

# 讀取本地檔案
data = open(filename_r2).read()

csvfile = StringIO(data)

csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容

for line in csv_reader:
    print('The album "' + line[0] + '" was released in ' + str(line[1]))

print("------------------------------------------------------------")  # 60個
print("5. pandas")
print("------------------------------------------------------------")  # 60個

filename = "data/twstock_all.csv"

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
dfprice = pd.DataFrame(df["收盤價"])

print(df)

print()

print(dfprice)

print("------------------------------------------------------------")  # 60個


data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

df.to_csv("tmp_write_read_csv13_vehicles.csv", index=False, encoding="big5")
df.to_json("tmp_write_read_csv13_vehicles1.json")
df.to_json("tmp_write_read_csv13_vehicles2.json", force_ascii=False)

df1 = pd.read_csv("tmp_write_read_csv13_vehicles.csv", encoding="big5")
df2a = pd.read_json("tmp_write_read_csv13_vehicles1.json")
df2b = pd.read_json("tmp_write_read_csv13_vehicles2.json")
print(df1)
print(df2a)
print(df2b)

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/numpy_pandas/data/ExpensesRecord.csv"

df = pd.read_csv(filename)
print(df.head(5))

filename = "tmp_write_read_csv15.csv"

df.to_csv(filename)

print("------------------------------------------------------------")  # 60個

"""
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0].head(5) )

#df = pd.read_html('http://news.baidu.com/tech')
#print(df[0].head(5) )
"""

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/numpy_pandas/data/ExpensesRecord.csv"
DataFrame = pd.read_csv(filename)
print(DataFrame["說明"])
print(DataFrame[["說明", "支出金額"]])

df = pd.DataFrame({"Math": [90, 91, 92, 93, 94], "English": np.arange(80, 85, 1)})
print(df[["Math", "English"]])

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/numpy_pandas/data/ExpensesRecord.csv"
DataFrame = pd.read_csv(filename)
DataFrame["單價"] = DataFrame["支出金額"] / DataFrame["數量"]
print(DataFrame[["數量", "支出金額", "單價"]])

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("6. 應用範例")
print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    highTemps = []  # 設定空串列
    for line in csv_reader:
        highTemps.append(int(line[1]))  # 儲存最高溫
plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(highTemps)
plt.title("2025年1月臺北天氣報告", fontsize=24)
plt.ylabel(r"溫度 $C^{o}$", fontsize=14)
# plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps = [], []  # 設定空串列
    for line in csv_reader:
        highTemps.append(int(line[1]))  # 儲存最高溫
        currentDate = datetime.strptime(line[0], "%Y/%m/%d")
        dates.append(currentDate)

plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 圖標增加日期刻度
plt.title("2025年1月臺北天氣報告", fontsize=24)
plt.ylabel(r"溫度 $C^{o}$", fontsize=14)
# plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps = [], []  # 設定空串列
    for line in csv_reader:
        highTemps.append(int(line[1]))  # 儲存最高溫
        currentDate = datetime.strptime(line[0], "%Y/%m/%d")
        dates.append(currentDate)

fig = plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 圖標增加日期刻度
fig.autofmt_xdate()  # 預設最佳化角度旋轉
plt.title("2025年1月臺北天氣報告", fontsize=24)
plt.ylabel(r"溫度 $C^{o}$", fontsize=14)
# plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps = [], []  # 設定空串列
    for line in csv_reader:
        highTemps.append(int(line[1]))  # 儲存最高溫
        currentDate = datetime.strptime(line[0], "%Y/%m/%d")
        dates.append(currentDate)

fig = plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 圖標增加日期刻度
fig.autofmt_xdate(rotation=60)  # 日期旋轉60度
plt.title("2025年1月臺北天氣報告", fontsize=24)
plt.ylabel(r"溫度 $C^{o}$", fontsize=14)
# plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/TaipeiWeatherJan.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps, lowTemps = [], [], []  # 設定空串列
    for line in csv_reader:
        try:
            currentDate = datetime.strptime(line[0], "%Y/%m/%d")
            highTemp = int(line[1])  # 設定最高溫
            lowTemp = int(line[3])  # 設定最低溫
        except Exception:
            print("有缺值")
        else:
            highTemps.append(highTemp)  # 儲存最高溫
            lowTemps.append(lowTemp)  # 儲存最低溫
            dates.append(currentDate)  # 儲存日期

fig = plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 繪製最高溫
plt.plot(dates, lowTemps)  # 繪製最低溫
plt.fill_between(dates, highTemps, lowTemps, color="y", alpha=0.2)  # 填滿
fig.autofmt_xdate()  # 日期旋轉
plt.title("2025年1月臺北天氣報告", fontsize=24)
plt.ylabel(r"溫度 $C^{o}$", fontsize=14)
# plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
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
# plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
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
    list_data = list(csv_reader)
    data_row = list_data[5:-1]  # 切片

    mydates, highPrices, lowPrices, closePrices = [], [], [], []

    for line in data_row:
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
# plt.show()


print("------------------------------------------------------------")  # 60個
print("7. 其他 & 新進")
print("------------------------------------------------------------")  # 60個

""" many
filename_r = 'data/workfile.csv'
filename_w = 'tmp_write_read_csv06.csv'

#一讀一寫

with open(filename_r, 'r') as csvfile1:  # 開啟csv檔案
    with open(filename_w, 'w') as csvfile2:  # 開啟csv檔案
        csv_reader = csv.reader(csvfile1, delimiter=',')
        csv_writer = csv.writer(csvfile2, delimiter=',')
        header = next(csv_reader)
        print(header)
        # get number of columns
        #array = header.split(',')
        first_item = header[0]
        csv_writer.writerow(header)
        for line in csv_reader:
            print(','.join(line))
            csv_writer.writerow(line)
            print(line[2])

print('寫入csv檔, 檔案 :', filename_w)
"""

print("------------------------------------------------------------")  # 60個


# 擷取登入帳號資訊


def passwd_to_dict(filename):
    users = {}
    with open(filename) as csvfile:  # 開啟csv檔案
        for line in csvfile:
            user_info = line.split(":")
            users.update({user_info[0]: user_info[2]})
    return users


print(passwd_to_dict(r".\data\passwd.cfg"))

# 擷取登入帳號資訊（生成版）


def passwd_to_dict_2(filename):
    with open(filename) as csvfile:  # 開啟csv檔案
        d = {words[0]: words[2] for words in [line.split(":") for line in csvfile]}
    return d


print(passwd_to_dict_2(r".\data\passwd.cfg"))


def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, "r") as csvfile1, open(
        csv_filename, "w", newline=""
    ) as csvfile2:
        csv_reader = csv.reader(csvfile1, delimiter=":")
        csv_writer = csv.writer(csvfile2, delimiter="\t", lineterminator="\n")
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])


filename = "tmp_write_read_csv07_password.csv"

passwd_to_csv(r".\data\passwd.cfg", filename)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
with open('songs.csv', 'w', newline='', encoding="big5") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入一列資料
    writer.writerow(["排名", "歌名", "作者", "發行日期", "連結"])
    
    ...
    
    writer.writerow([song_rank, song_name, song_artist, song_date, song_url])



        self.load_rules(os.path.join(os.path.dirname(__file__), '..',
                                     'susp-ignored.csv'))


            self.warn('[%s:%d] "%s" found in "%-.120s"' %
                      (self.docname, lineno, issue, text))



            csvfile = open(self.log_file_name, 'a')
            writer = csv.writer(csvfile, dialect)
            writer.writerow([self.docname, lineno, issue, text.strip()])
            csvfile.close()


        # 開啟輸出的 csv 檔案
        filename_w = '匯出資料範例.csv'
        with open(filename_w, 'w', newline = '') as csvfile:
            # 建立 csv 檔寫入物件
            writer = csv.writer(csvfile)

            # 寫入二維串列資料
            writer.writerows(csv_data)

"""




"""
    ["中文名", "英文名", "體重", "全名"],
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
"""


"""


應該重複
with open(filename, "r") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        print(line)




csvfile = pathlib.Path(filename).open(encoding="UTF-8")
csvfile = pathlib.Path(filename).open(encoding="UTF-8")

with pathlib.Path(filename).open(encoding="big5") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        print(line)



csvfile = open(filename, "w", newline="")

# 以附加模式開啟檔案
csvfile=open(filename, 'a', newline='') 


with open(filename, "w", newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
with open(filename, "w+", newline="") as csvfile:  # 開啟csv檔案
#with open(filename, "w", newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
with open(filename, 'w', newline='') as csvfile:    # 開啟csv檔案
with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    csv_writer = csv.writer(csvfile, delimiter="\t")  # 建立Writer物件
    


"""


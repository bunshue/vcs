"""
csv檔 逗號分隔值(comma-seperated values)

預設使用','分隔, 也可以使用其他分隔符號
csvWriter = csv.writer(csvFile, delimiter='\t') # 建立Writer物件, 使用TAB區分項目 不使用逗號

先寫後讀

csv.writer()
csv.DictWriter(csvfile, fieldnames=fieldnames)  # 建立Writer物件
writer = csv.writer(csvfile)
writer.writerows(np.array(animals))

1. csv.reader()


"""
print("------------------------------------------------------------")  # 60個

import sys
import csv
import random
import numpy as np
import pandas as pd
'''
print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 1 writer")

filename = "tmp_write_read_csv01.csv"

csvfile = open(filename, "w+", newline="")
try:
    writer = csv.writer(csvfile)
    # 寫入欄位名稱
    writer.writerow(("中文名", "英文名", "體重", "全名"))
    # 寫入資料(12筆)
    writer.writerow(("鼠", "mouse", 3, "米老鼠"))
    writer.writerow(("牛", "ox", 48, "班尼牛"))
    writer.writerow(("虎", "tiger", 33, "跳跳虎"))
    writer.writerow(("兔", "rabbit", 8, "彼得兔"))
    writer.writerow(("龍", "dragon", 38, "逗逗龍"))
    writer.writerow(("蛇", "snake", 16, "貪吃蛇"))
    writer.writerow(("馬", "horse", 36, "草泥馬"))
    writer.writerow(("羊", "goat", 29, "喜羊羊"))
    writer.writerow(("猴", "monkey", 22, "山道猴"))
    writer.writerow(("雞", "chicken", 6, "肯德雞"))
    writer.writerow(("狗", "dog", 12, "貴賓狗"))
    writer.writerow(("豬", "pig", 42, "佩佩豬"))
finally:
    csvfile.close()

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 2 DictWriter")

filename = "tmp_write_read_csv02.csv"
with open(filename, "w", newline="") as csvfile:
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
    csv_dict_writer.writerow({"中文名": "龍", "英文名": "dragon", "體重": 38, "全名": "逗逗龍"})
    csv_dict_writer.writerow({"中文名": "蛇", "英文名": "snake", "體重": 16, "全名": "貪吃蛇"})
    csv_dict_writer.writerow({"中文名": "馬", "英文名": "horse", "體重": 36, "全名": "草泥馬"})
    csv_dict_writer.writerow({"中文名": "羊", "英文名": "goat", "體重": 29, "全名": "喜羊羊"})
    csv_dict_writer.writerow({"中文名": "猴", "英文名": "monkey", "體重": 22, "全名": "山道猴"})
    csv_dict_writer.writerow({"中文名": "雞", "英文名": "chicken", "體重": 6, "全名": "肯德雞"})
    csv_dict_writer.writerow({"中文名": "狗", "英文名": "dog", "體重": 12, "全名": "貴賓狗"})
    csv_dict_writer.writerow({"中文名": "豬", "英文名": "pig", "體重": 42, "全名": "佩佩豬"})

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 3a 一維串列資料 一次寫入")

filename = "tmp_write_read_csv03.csv"

# 建立csv一維串列資料

print("一維 串列")
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

# 開啟輸出的 csv 檔案
# with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
with open(filename, "w", newline="") as csvfile:
    # 建立 csv 檔寫入物件
    csv_writer = csv.writer(csvfile)

    # 寫入一維串列資料
    csv_writer.writerows(np.array(animals))

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("寫入CSV檔 3b 二維串列資料 一次寫入")

filename = "tmp_write_read_csv04.csv"

# 建立csv二維串列資料
csvtable = [
    ["中文名", "英文名", "體重", "全名"],
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
    ["龍", "dragon", 38, "逗逗龍"],
    ["蛇", "snake", 16, "貪吃蛇"],
    ["馬", "horse", 36, "草泥馬"],
    ["羊", "goat", 29, "喜羊羊"],
    ["猴", "monkey", 22, "山道猴"],
    ["雞", "chicken", 6, "肯德雞"],
    ["狗", "dog", 12, "貴賓狗"],
    ["豬", "pig", 42, "佩佩豬"],
]

# 開啟輸出的 csv 檔案
# with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
with open(filename, "w", newline="") as csvfile:
    # 建立 csv 檔寫入物件
    csv_writer = csv.writer(csvfile)

    # 寫入二維串列資料
    csv_writer.writerows(csvtable)

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("寫入CSV檔 3c 二維串列資料 一次寫一行(row)")

filename = "tmp_write_read_csv05.csv"

with open(filename, "w+", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in csvtable:
        csv_writer.writerow(row)

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
print("------------------------------------------------------------")  # 60個
print("csv.reader()")
print("------------------------------------------------------------")  # 60個

print("python讀寫CSV檔 1 讀取")

filename = "data/animals.csv"

# 讀取方法相同 印出資料方法1
#with open(filename, newline="") as csvfile:
with open(filename, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容
    # 以迴圈顯示每一列
    for row in csv_reader:
        print(row)

# 讀取方法相同 印出資料方法2, 完整地讀取每一個元素
#with open(filename, newline="") as csvfile:
with open(filename, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容

    datas = list(csv_reader)  # 將資料轉成list
    length = len(datas)
    data_column = len(datas[0])
    print("data_column = ", data_column)
    for row in datas:
        print(row)

print("------------------------------------------------------------")  # 60個

print("python讀寫CSV檔 7 讀取")

filename = "data/animals.csv"
with open(filename, "r", encoding="UTF-8-sig") as csvfile:
    for line in csvfile:
        print(line)

print("------------------------------------------------------------")  # 60個
print("python讀寫CSV檔 8 讀取")

filename = "data/animals.csv"

with open(filename, "rt", encoding="UTF-8-sig") as csvfile:
    #將所有資料讀出來變成一個一維串列
    data = csvfile.readlines()
print(type(data))
print(data)

print("------------------------------------------------------------")  # 60個

print("python讀寫CSV檔 11 讀取")

filename = "data/python_ReadWrite_CSV1.csv"

import pprint as pp

data_list = list()
with open(filename, "rt") as csvfile:
    columns = csvfile.readline().split(",")
    for item in csvfile.readlines():
        temp = dict()
        for i, field in enumerate(item.split(",")):
            temp[columns[i].strip()] = field.strip()
        data_list.append(temp)
pp.pprint(data_list)

print("------------------------------------------------------------")  # 60個

print("讀取 csv 檔案")
filename = "./data/csvReport.csv"

with open(filename, encoding="utf-8") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列

for row in listReport:
    print(row)  # 輸出串列

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])

print("------------------------------------------------------------")  # 60個

print("讀取 csv 檔案")
infilename = "./data/csvReport.csv"  # 來源檔案
outfilename = "out19_6.csv"  # 目的檔案
with open(infilename, encoding="utf-8") as csvfile:  # 開啟csv檔案供讀取
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列

print("------------------------------------------------------------")  # 60個

filename = "./data/csvReport2.csv"
with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == "Steve":
        if row[1] == "2025":
            total2025 += int(row[5])
        if row[1] == "2026":
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)

print("------------------------------------------------------------")  # 60個

""" many
filename_r = 'data/workfile.csv'
filename_w = 'tmp_write_read_csv06.csv'

#一讀一寫
print('讀取csv檔, 檔案 :', filename_r)

with open(filename_r, 'r') as csvfile1:
    with open(filename_w, 'w') as csvfile2:
        csv_reader = csv.reader(csvfile1, delimiter=',')
        csv_writer = csv.writer(csvfile2, delimiter=',')
        header = next(csv_reader)
        print(header)
        # get number of columns
        #array = header.split(',')
        first_item = header[0]
        csv_writer.writerow(header)
        for row in csv_reader:
            print(','.join(row))
            csv_writer.writerow(row)
            print(row[2])

print('寫入csv檔, 檔案 :', filename_w)
"""

print("------------------------------------------------------------")  # 60個

print("讀取csv檔")

filename = "data/pl.csv"
with open(filename, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(",".join(row))

print()
with open(filename, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

print("------------------------------------------------------------")  # 60個

filename = "data/python_ReadWrite_CSV2.csv"
print("讀取CSV檔 1 DictReader, 檔案 :", filename)

data = list()
with open(filename, newline="") as csvfile:
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    print(type(csv_dict_reader))

    # 以迴圈顯示每一列
    for row in csv_dict_reader:
        print(row["姓名"], row["身高"], row["體重"])
        print(row)
        data.append(dict(row))

print(type(data))
print(len(data))
print(data)
print(len(data[0]))
print(type(data[0]))
print(data[0])
print(data[0]["姓名"])
print(data[0]["身高"])
print(data[0]["體重"])
print(len(data[1]))
print(type(data[1]))
print(data[1])
print(data[1]["姓名"])
print(data[1]["身高"])
print(data[1]["體重"])

print("------------------------------------------------------------")  # 60個

filename = "data/python_ReadWrite_CSV1.csv"
print("讀取CSV檔 2 DictReader, 檔案 :", filename)

import pprint as pp

data = list()
with open(filename, "rt") as csvfile:
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    print(type(csv_dict_reader))
    for row in csv_dict_reader:
        data.append(dict(row))
pp.pprint(data)

print("------------------------------------------------------------")  # 60個

filename = "data/python_ReadWrite_CSV1.csv"
print("讀取CSV檔 3 DictReader, 檔案 :", filename)

import pprint as pp

with open(filename, "rt") as csvfile:
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    data = [dict(row) for row in csv_dict_reader]
pp.pprint(data)

print("------------------------------------------------------------")  # 60個

filename = "data/csvPeople.csv"
print("讀取CSV檔 4 DictReader, 檔案 :", filename)

with open(filename) as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀檔案建立DictReader物件
    for row in csv_dict_reader:  # 列出DictReader各列內容
        print(row)

    for row in csv_dict_reader:  # 列出DictReader各列內容
        print(row["first_name"], row["last_name"])

print("------------------------------------------------------------")  # 60個

filename = "data/member.csv"
print("讀取CSV檔 5 DictReader, 檔案 :", filename)

# 讀取 CSV 檔案並提取電子郵件地址
with open(filename, newline="", encoding="utf-8") as csvfile:
    csv_dict_reader = csv.DictReader(csvfile)
    for row in csv_dict_reader:
        # print(row['姓名'], end = "\t")   #不能用
        print(row["電子郵件"], end="\t")
        print(row["體重"])

print("------------------------------------------------------------")  # 60個

import pathlib

filename = "data/namelist.csv"
csvfile = pathlib.Path(filename).open(encoding="UTF-8")
csv_reader = csv.reader(csvfile)
for row in csv_reader:  # 取得每一列資料
    for value in row:  # 取得資料時，以逗號間隔
        print(value)

print("------------------------------------------------------------")  # 60個

import pathlib

filename = "xxxxx.csv"
try:
    csvfile = pathlib.Path(filename).open(encoding="UTF-8")
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:  # 取得每一列資料
        for value in row:  # 取得資料時，以逗號間隔
            print(value)
except:
    print("無法載入檔案。")

print("------------------------------------------------------------")  # 60個

filename = "data/csvReport2.csv"
with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == "Steve":
        if row[1] == "2025":
            total2025 += int(row[5])
        if row[1] == "2026":
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)

print("------------------------------------------------------------")  # 60個

print("2025年1月臺北天氣報告")

filename = "data/TaipeiWeatherJan.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []
    for row in csv_reader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        meanTemps.append(int(row[2]))  # 儲存均溫
        lowTemps.append(int(row[3]))  # 儲存最低溫

print("高溫", highTemps)
print("均溫", meanTemps)
print("低溫", lowTemps)

print("------------------------------------------------------------")  # 60個

import ast

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores.csv"

scores = dict()
with open(filename, "r") as csvfile:
    filedata = csvfile.read()
    # scores = ast.literal_eval(filedata)
print("以下是{}成績檔的字典型態資料:".format(filename))

print("------------------------------------------------------------")  # 60個

# 擷取登入帳號資訊


def passwd_to_dict(filename):
    users = {}
    with open(filename) as csvfile:
        for line in csvfile:
            user_info = line.split(":")
            users.update({user_info[0]: user_info[2]})
    return users


print(passwd_to_dict(r".\data\passwd.cfg"))

# 擷取登入帳號資訊（生成版）


def passwd_to_dict_2(filename):
    with open(filename) as csvfile:
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

filename = "data/animals.csv"

try:
    with open(filename, encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)
except FileNotFoundError:
    print("無法打開文件:", filename)
else:
    for item in data:
        print("%-20s%-20s%-10s%-20s" % (item[0], item[1], item[2], item[3]))

print("------------------------------------------------------------")  # 60個

filename = "data/Example.csv"
with open(filename, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(",".join(row))

print("------------------------------------------------------------")  # 60個

filename = "data/csvReport.csv"
with open(filename, encoding="utf-8") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列
for row in listReport:  # 迴圈輸出串列內容
    print(row)

print("------------------------------------------------------------")  # 60個

filename = "data/csvReport.csv"
with open(filename, encoding="utf-8") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])

print("------------------------------------------------------------")  # 60個

filename = "data/csvPeople.csv"
with open(filename) as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀檔案建立DictReader物件
    for row in csv_dict_reader:  # 列出DictReader各列內容
        print(row)

print("------------------------------------------------------------")  # 60個

filename = "data/csvPeople.csv"
with open(filename) as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀檔案建立DictReader物件
    for row in csv_dict_reader:  # 列出DictReader各列內容
        print(row["first_name"], row["last_name"])

print("------------------------------------------------------------")  # 60個

infilename = "data/csvReport.csv"  # 來源檔案
with open(infilename, encoding="utf-8") as csvfile:  # 開啟csv檔案供讀取
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    listReport = list(csv_reader)  # 將資料轉成串列

filename = "data/TaipeiWeatherJan.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
print(headerRow)

for i, header in enumerate(headerRow):
    print(i, header)

print("------------------------------------------------------------")  # 60個

filename = "data/TaipeiWeatherJan.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    highTemps, lowTemps = [], []  # 設定空串列
    for row in csv_reader:
        highTemps.append(row[1])  # 儲存最高溫
        lowTemps.append(row[3])  # 儲存最低溫

print("最高溫 : ", highTemps)
print("最低溫 : ", lowTemps)

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = "data/TaipeiWeatherJan.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    highTemps = []  # 設定空串列
    for row in csv_reader:
        highTemps.append(int(row[1]))  # 儲存最高溫
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
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps = [], []  # 設定空串列
    for row in csv_reader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
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
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps = [], []  # 設定空串列
    for row in csv_reader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
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
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps = [], []  # 設定空串列
    for row in csv_reader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
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
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    dates, highTemps, lowTemps = [], [], []  # 設定空串列
    for row in csv_reader:
        try:
            currentDate = datetime.strptime(row[0], "%Y/%m/%d")
            highTemp = int(row[1])  # 設定最高溫
            lowTemp = int(row[3])  # 設定最低溫
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
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    for _ in range(5):  # 跳過前 5 列
        next(csv_reader)
    all_rows = list(csv_reader)
    data_without_last_row = all_rows[:-1]  # 跳過最後一列

    mydates, highPrices, lowPrices, closePrices = [], [], [], []

    for row in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d")  # 轉換後日期
            highPrice = eval(row[4])  # 設定最高價
            lowPrice = eval(row[5])  # 設定最低價
            closePrice = eval(row[6])  # 設定收盤價
        except Exception:
            print(f"有缺值 {row}")
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
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    all_rows = list(csv_reader)
    data_row = all_rows[5:-1]  # 切片

    mydates, highPrices, lowPrices, closePrices = [], [], [], []

    for row in data_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d")  # 轉換後日期
            highPrice = eval(row[4])  # 設定最高價
            lowPrice = eval(row[5])  # 設定最低價
            closePrice = eval(row[6])  # 設定收盤價
        except Exception:
            print(f"有缺值 {row}")
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

csvfile = open("data/tScore.csv")  # 建立檔案物件f，此物件操作StudentScore.csv
csv_reader = csv.reader(csvfile, delimiter="\t")  # 建立reader物件使用 '\t' 當分隔符號
listData = list(csv_reader)  # 使用list()函數將data轉成串列再指定給Reader
for row in listData:  # 使用巢狀迴圈將ListData串列逐欄印出
    for col in row:
        print(col, "   ", end="")
    print()
csvfile.close()

print("------------------------------------------------------------")  # 60個

csvfile = open("data/StudentScore.csv")
csv_dict_reader = csv.DictReader(csvfile)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
for row in csv_dict_reader:  # 逐一印出字典的內容
    print(row)
csvfile.close()

print("------------------------------------------------------------")  # 60個

csvfile = open("data/StudentScore.csv")
csv_dict_reader = csv.DictReader(csvfile)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
print("學號\t姓名\t國文\t英語\t數學\t總分")
for row in csv_dict_reader:  # 逐一印出字典的內容，並計算總分
    print(
        "{}\t{}\t{}\t{}\t{}\t{}".format(
            row["學號"],
            row["姓名"],
            row["國文"],
            row["英語"],
            row["數學"],
            (int(row["國文"]) + int(row["英語"]) + int(row["數學"])),
        )
    )
csvfile.close()

print("------------------------------------------------------------")  # 60個

# searchName=input('請輸入學生姓名進行查詢成績：') #輸入查詢姓名
searchName = "david"

csvfile = open("data/StudentScore.csv")
csv_dict_reader = csv.DictReader(csvfile)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
for row in csv_dict_reader:  # 逐一比對姓名是否符合searchName
    if row["姓名"] == searchName:
        print("{}成績資訊如下：".format(row["姓名"]))
        print("學號：{}".format(row["學號"]))
        print("國文：{}".format(row["國文"]))
        print("英語：{}".format(row["英語"]))
        print("數學：{}".format(row["數學"]))
        print("總分：{}".format((int(row["國文"]) + int(row["英語"]) + int(row["數學"]))))
        break  # 離開迴圈
else:  # 當迴圈沒有執行break，即會執行else區域，表示沒有找到符合姓名
    print("查無{}成績".format(searchName))
csvfile.close()

print("------------------------------------------------------------")  # 60個

csvfile = open("tmp_dictWriterProduct.csv", "w", newline="")
# 建立writer物件，同時指定欄位名稱
csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["產品編號", "品名", "單價"])
csv_dict_writer.writeheader()  # 寫入欄位名稱
csv_dict_writer.writerow({"產品編號": "A02", "品名": "黑松沙士", "單價": 90})
# 寫入兩筆產品記錄到csv檔中
csv_dict_writer.writerow({"產品編號": "A02", "品名": "草苺蛋糕", "單價": 120})
csvfile.close()

print("------------------------------------------------------------")  # 60個

csvfile = open("data/StudentScore.csv")  # 建立檔案物件f，此物件操作StudentScore.csv
csv_reader = csv.reader(csvfile)  # 使用csv的reader()方法取得檔案物件f的資料並傳回Reader物件
listData = list(csv_reader)  # 使用list()函數將data轉換串列再指定給listData
for row in listData:  # 將二維串列listData 逐列印出
    print(row)
csvfile.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

csvfile = open("data/StudentScore.csv")  # 建立檔案物件f，此物件操作StudentScore.csv
csv_reader = csv.reader(csvfile)  # 使用csv的reader()方法取得檔案物件f的資料並傳回Reader物件
listData = list(csv_reader)  # 使用list()函數將csv_reader轉成串列再指定給listData
for row in listData:  # 使用巢狀迴圈將ListData串列逐欄印出
    for col in row:
        print(col, "  ", end="")
    print()
csvfile.close()

print("------------------------------------------------------------")  # 60個

csvfile = open("tmp_writerProduct.csv", "w", newline="")  # 開啟writerProduct.csv檔案
csvWriter = csv.writer(csvfile)  # 建立writer物件，物件名稱為csvWriter
# 建立listProduct二維串列有兩筆產品
listProduct = [["B01", "小林煎餅", "78"], ["B02", "五香豆干", "90"]]
# 寫入一維串列當做標題
csvWriter.writerow(["編號", "品名", "單價"])
csvWriter.writerows(listProduct)  # 將二維串列的兩筆產品寫入csv內
csvfile.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

"""
listProduct=["","",""] # 建立listProduct串列，用來存放一筆產品記錄
while True:
     option = input("功能選單：1.新增 2.查詢 3.離開：")
     if option=="1":
         # 以附加模式開啟tProduct.csv檔案
         f=open('tProduct.csv','a', newline='') 
         csvWriter=csv.writer(f) 
         listProduct[0] = input("編號：")   #listProduct[0]存放編號
         listProduct[1] = input("品名：")   #listProduct[1]存放品名
         listProduct[2] = input("單價：")   #listProduct[2]存放單價
         csvWriter.writerow(listProduct)
         print("新增成功")
         f.close()
     elif option=="2" :
         # 以讀檔模式開啟tProduct.csv檔案
         f=open ('tProduct.csv')
         csvdictreader=csv.DictReader(f)  
         print("編號\t品名\t單價")
         for row in csvdictreader:   		
             print("{}\t{}\t{}".format(row['編號'],row['品名'],row['單價']))
         f.close()
     else:
         break
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("python讀寫CSV檔 3 讀取")

from io import StringIO

# 本地檔案
filename_r2 = "data/MontyPythonAlbums.local.csv"

print("讀取一個本地csv檔案 : " + filename_r2)

# 讀取本地檔案
data = open(filename_r2).read()

csvfile = StringIO(data)

csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容

for row in csv_reader:
    print('The album "' + row[0] + '" was released in ' + str(row[1]))

print("------------------------------------------------------------")  # 60個
print("使用pd")
print("------------------------------------------------------------")  # 60個

print("python讀寫CSV檔 12 讀取 pandas")

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


# pip install xlsxwriter

filename = "C:/_git/vcs/_4.python/numpy_pandas/data/ExpensesRecord.xls"

df = pd.read_excel(filename, "sheet")
# data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df.head(5))

from pandas import ExcelWriter

filename = "tmp_write_read_csv14.xlsx"

writer = ExcelWriter(filename, engine="xlsxwriter")
df.to_excel(writer, sheet_name="sheet2")
writer.save()

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


""" no file
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# 3 filter'

print("--------------------")
print(df['Date'] == '2018-01-05')
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'
print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())

#  5 matplotlib
import matplotlib.pyplot as plt
df.plot(x='Date', y='Open',grid=True, color='blue')
#plt.show()

import matplotlib.pyplot as plt
df.plot( y='diff',grid=True, color='red',kind='hist')
#plt.show()

fig, ax = plt.subplots()
for name, group in df.groupby('month'):
    group.plot(x='day', y='Open', ax=ax, label=name)
#plt.show()

fileds=['Open','Close','High']
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x='Date', y=name, ax=ax, label=name)
#plt.show()

dfMonths = df.loc[df['month'].isin([1,2,3,4,5,6,7])]
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(values = 'High', columns = 'month', index = 'day')
dfMonthsPivot.plot(kind = 'box',title = 'Months High')
#plt.show()
"""
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

filename = "tmp_write_read_csv08.csv"

with open(filename, "w", newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
    csvWriter = csv.writer(csvfile)  # 建立Writer物件
    csvWriter.writerow(["姓名", "年齡", "城市"])
    csvWriter.writerow(["Hung", "35", "Taipei"])
    csvWriter.writerow(["James", "40", "Chicago"])



print("------------------------------------------------------------")  # 60個

filename = "data/Example2.csv"
list1 = [[10, 33, 45], [5, 25, 56]]
with open(filename, "w+", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data1", "Data2", "Data3"])
    for row in list1:
        writer.writerow(row)

"""
print('寫入 csv 檔案')   一讀一寫
with open(outfilename,'w',newline='') as csvfile:  
    csvWriter = csv.writer(csvfile)    # 建立Writer物件   
    for row in listReport:              # 將串列寫入
        csvWriter.writerow(row)
"""



outfilename = "tmp_write_read_csv09.csv"  # 目的檔案
with open(outfilename, "w", newline="", encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)  # 建立Writer物件
    for row in listReport:  # 將串列寫入
        csvWriter.writerow(row)

print("------------------------------------------------------------")  # 60個

filename = "tmp_write_read_csv10.csv"
with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    csvWriter = csv.writer(csvfile, delimiter="\t")  # 建立Writer物件
    csvWriter.writerow(["Name", "Age", "City"])
    csvWriter.writerow(["Hung", "35", "Taipei"])
    csvWriter.writerow(["James", "40", "Chicago"])

print("------------------------------------------------------------")  # 60個

filename = "tmp_write_read_csv11.csv"
with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    fields = ["Name", "Age", "City"]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fields)  # 建立Writer物件

    csv_dict_writer.writeheader()  # 寫入標題
    csv_dict_writer.writerow({"Name": "Hung", "Age": "35", "City": "Taipei"})
    csv_dict_writer.writerow({"Name": "James", "Age": "40", "City": "Chicago"})

print("------------------------------------------------------------")  # 60個

# 定義串列,元素是字典
dictList = [
    {"姓名": "Hung", "年齡": "35", "城市": "臺北"},
    {"姓名": "James", "年齡": "40", "城市": "芝加哥"},
]

filename = "tmp_write_read_csv12.csv"
with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    fields = ["姓名", "年齡", "城市"]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fields)  # 建立Writer物件
    csv_dict_writer.writeheader()  # 寫入標題
    for row in dictList:  # 寫入內容
        csv_dict_writer.writerow(row)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個






csvdictreader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary

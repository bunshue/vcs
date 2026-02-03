"""
Python網路爬蟲_大數據擷取、清洗、儲存與分析：王者歸來
ch01~ch05
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


import re
import csv
import json
import bs4
import requests

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ch1_1.py

listNumbers = [5, 10, 20, 1]  # 串列資料
tupleNumbers = (1, 5, 10, 9)  # 元組資料
jsonData1 = json.dumps(listNumbers)  # 將串列資料轉成json資料
jsonData2 = json.dumps(tupleNumbers)  # 將串列資料轉成json資料
print("串列轉換成json的陣列", jsonData1)
print("元組轉換成json的陣列", jsonData2)
print("json陣列在Python的資料類型 ", type(jsonData1))

print("------------------------------------------------------------")  # 60個

# ch1_2.py

listObj = [{"Name": "Peter", "Age": 25, "Gender": "M"}]  # 串列資料元素是字典
jsonData = json.dumps(listObj)  # 將串列資料轉成json資料
print("串列轉換成json的陣列", jsonData)
print("json陣列在Python的資料類型 ", type(jsonData))

print("------------------------------------------------------------")  # 60個

# ch1_3.py

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
jsonObj1 = json.dumps(players)  # 未用排序將字典轉成json物件
jsonObj2 = json.dumps(players, sort_keys=True)  # 有用排序將字典轉成json物件
print("未用排序將字典轉換成json的物件", jsonObj1)
print("使用排序將字典轉換成json的物件", jsonObj2)
print("有排序與未排序物件是否相同    ", jsonObj1 == jsonObj2)
print("json物件在Python的資料類型 ", type(jsonObj1))

print("------------------------------------------------------------")  # 60個

# ch1_4.py

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
jsonObj = json.dumps(players, sort_keys=True, indent=4)
print(jsonObj)

print("------------------------------------------------------------")  # 60個

# ch1_5.py

jsonObj = '{"b":80, "a":25, "c":60}'  # json物件
dictObj = json.loads(jsonObj)  # 轉成Python物件
print(dictObj)
print(type(dictObj))

print("------------------------------------------------------------")  # 60個

# ch1_6.py

obj = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])

print("------------------------------------------------------------")  # 60個

# ch1_7.py

obj = '{"Asia":\
        [{"Japan":"Tokyo"},\
         {"China":"Beijing"}]\
       }'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])

print("------------------------------------------------------------")  # 60個

# ch1_8.py

dictObj = {"b": 80, "a": 25, "c": 60}
fn = "tmp_out1_8.json"
with open(fn, "w") as fnObj:
    json.dump(dictObj, fnObj)

print("------------------------------------------------------------")  # 60個

# ch1_9.py

obj = {"Asia": [{"Japan": "Tokyo"}, {"China": "Beijing"}]}
fn = "tmp_out1_9.json"
with open(fn, "w") as fnObj:
    json.dump(obj, fnObj)

print("------------------------------------------------------------")  # 60個

# ch1_9_1.py

objlist = [{"日本": "Japan", "首都": "Tykyo"}, {"美州": "USA", "首都": "Washington"}]

fn = "tmp_out1_9_1.json"
with open(fn, "w") as fnObj:
    json.dump(objlist, fnObj)

print("------------------------------------------------------------")  # 60個

# ch1_9_2.py

objlist = [{"日本": "Japan", "首都": "Tykyo"}, {"美州": "USA", "首都": "Washington"}]

fn = "tmp_out1_9_2.json"
with open(fn, "w", encoding="utf-8") as fnObj:
    json.dump(objlist, fnObj, indent=2, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

# ch1_10.py

fn = "tmp_out1_9.json"
with open(fn, "r") as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))

print("------------------------------------------------------------")  # 60個

# ch1_11.py

fn = "login.json"
login = "david"
with open(fn, "w") as fnObj:
    json.dump(login, fnObj)
    print("%s! 歡迎使用本系統! " % login)

print("------------------------------------------------------------")  # 60個

# ch1_12.py

fn = "login.json"
with open(fn, "r") as fnObj:
    login = json.load(fnObj)
    print("%s! 歡迎回來使用本系統! " % login)

print("------------------------------------------------------------")  # 60個

# ch1_13.py

fn = "login1_13.json"
try:
    with open(fn) as fnObj:
        login = json.load(fnObj)
except Exception:
    login = "david"
    with open(fn, "w") as fnObj:
        json.dump(login, fnObj)
        print("系統已經記錄你的帳號 ")
else:
    print("%s 歡迎回來" % login)

print("------------------------------------------------------------")  # 60個

# ch1_14.py

fn = "data/populations.json"
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀json檔案

for getData in getDatas:
    if getData["Year"] == "2000":  # 篩選2000年的數據
        countryName = getData["Country Name"]  # 國家名稱
        countryCode = getData["Country Code"]  # 國家代碼
        population = int(float(getData["Numbers"]))  # 人口數據
        print("國家代碼 =", countryCode, "國家名稱 =", countryName, "人口數 =", population)

print("------------------------------------------------------------")  # 60個

# ch1_15.py
from pygal.maps.world import COUNTRIES

for countryCode in sorted(COUNTRIES.keys()):
    print("國家代碼 :", countryCode, "  國家名稱 = ", COUNTRIES[countryCode])

print("------------------------------------------------------------")  # 60個

# ch1_16.py
from pygal.maps.world import COUNTRIES


def getCountryCode(countryName):
    """輸入國家名稱回傳國家代碼"""
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode  # 如果找到則回傳國家代碼
    return None  # 找不到則回傳None


fn = "data/populations.json"
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀取人口數據json檔案

for getData in getDatas:
    if getData["Year"] == "2000":  # 篩選2000年的數據
        countryName = getData["Country Name"]  # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData["Numbers"]))  # 人口數
        if countryCode != None:
            print(countryCode, ":", population)  # 國家名稱相符
        else:
            print(countryName, " 名稱不吻合:")  # 國家名稱不吻合

print("------------------------------------------------------------")  # 60個

# ch1_17.py
import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "China in the Map"  # 世界地圖標題
worldMap.add("China", ["cn"])  # 標記中國
worldMap.render_to_file("tmp_out1_17.svg")  # 儲存地圖檔案


print("------------------------------------------------------------")  # 60個

# ch1_18.py
import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "China/Japan/Thailand"  # 世界地圖標題
worldMap.add("Asia", ["cn", "jp", "th"])  # 標記Asia
worldMap.render_to_file("tmp_out1_18.svg")  # 儲存地圖檔案


print("------------------------------------------------------------")  # 60個

# ch1_19.py
import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = " Asia, Europe, Africa, and North America"  # 世界地圖標題
worldMap.add("Asia", ["cn", "jp", "th"])  # 標記Asia
worldMap.add("Europe", ["fr", "de", "it"])  # 標記Europe
worldMap.add("Africa", ["eg", "ug", "ng"])  # 標記Africa
worldMap.add("North America", ["ca", "us", "mx"])  # 標記北美洲
worldMap.render_to_file("tmp_out1_19.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

# ch1_20.py
import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "Populations in China/Japan/Thailand"  # 世界地圖標題
worldMap.add("Asia", {"cn": 1262645000, "jp": 126870000, "th": 63155029})  # 標記人口資訊
worldMap.render_to_file("tmp_out1_20.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

# ch1_21.py
import pygal.maps.world
from pygal.maps.world import COUNTRIES


def getCountryCode(countryName):
    """輸入國家名稱回傳國家代碼"""
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode  # 如果找到則回傳國家代碼
    return None  # 找不到則回傳None


fn = "data/populations.json"
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀取人口數據json檔案

dictData = {}  # 定義地圖使用的字典
for getData in getDatas:
    if getData["Year"] == "2000":  # 篩選2000年的數據
        countryName = getData["Country Name"]  # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData["Numbers"]))  # 人口數
        if countryCode != None:
            dictData[countryCode] = population  # 代碼:人口數據加入字典

worldMap = pygal.maps.world.World()
worldMap.title = "World Population in 2000"
worldMap.add("Year 2000", dictData)
worldMap.render_to_file("tmp_out1_21.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

# ch1_22.py

import pygal.maps.world
from pygal.maps.world import COUNTRIES


def getCountryCode(countryName):
    """輸入國家名稱回傳國家代碼"""
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode  # 如果找到則回傳國家代碼
    return None  # 找不到則回傳None


fn = "data/populations.json"
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀取人口數據json檔案

dictData = {}  # 定義地圖使用的字典
for getData in getDatas:
    if getData["Year"] == "2000":  # 篩選2000年的數據
        countryName = getData["Country Name"]  # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData["Numbers"]))  # 人口數
        if countryCode != None:
            dictData[countryCode] = population  # 代碼:人口數據加入字典

dict1, dict2 = {}, {}  # 定義人口數分級的字典
for code, population in dictData.items():
    if population > 100000000:
        dict1[code] = population  # 人口數大於1000000000
    else:
        dict2[code] = population  # 人口數小於1000000000

worldMap = pygal.maps.world.World()
worldMap.title = "World Population in 2000"
worldMap.add("Over 1000000000", dict1)
worldMap.add("Under 1000000000", dict2)
worldMap.render_to_file("tmp_out1_22.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

# ch1_23.py
import xmltodict

with open("data/myxml.xml", encoding="utf-8") as f:
    txt = xmltodict.parse(f.read())
print(txt, "\n")
print(txt["深智數位"], "\n")
print("總經理 : ", txt["深智數位"]["總經理"])
print("總編輯 : ", txt["深智數位"]["編輯部"], "\n")
print(txt["深智數位"]["業務部"], "\n")
print(txt["深智數位"]["業務部"]["國外"], "\n")
print("國外業務主管 : ", txt["深智數位"]["業務部"]["國外"]["@主管"])
print("國外業務人數 : ", txt["深智數位"]["業務部"]["國外"]["人數"])
print("國內業務主管 : ", txt["深智數位"]["業務部"]["國內"])

print("------------------------------------------------------------")  # 60個

# ch2_1.py

fn = "data/csvReport.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列
print(listReport)  # 列印串列方法


print("------------------------------------------------------------")  # 60個

# ch2_2.py

fn = "data/csvReport.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件csvReader
    for row in csvReader:  # 用迴圈列出csvReader物件內容
        print("Row %s = " % csvReader.line_num, row)

print("------------------------------------------------------------")  # 60個

# ch2_3.py

fn = "data/csvReport.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列
for row in listReport:  # 使用迴圈列出串列內容
    print(row)

print("------------------------------------------------------------")  # 60個

# ch2_4.py

fn = "data/csvReport.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])

print("------------------------------------------------------------")  # 60個

# ch2_5.py

fn = "data/csvPeople.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile)  # 讀檔案建立DictReader物件
    for row in csvDictReader:  # 列出DictReader各行內容
        print(row)

print("------------------------------------------------------------")  # 60個

# ch2_6.py

fn = "data/csvPeople.csv"
with open(fn) as csvFile:  # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile)  # 讀檔案建立DictReader物件
    for row in csvDictReader:  # 使用迴圈列出字典內容
        print(row["first_name"], row["last_name"])

print("------------------------------------------------------------")  # 60個

# ch2_7.py

fn = "tmp_out2_7.csv"
with open(fn, "w", newline="") as csvFile:  # 開啟csv檔案
    csvWriter = csv.writer(csvFile)  # 建立Writer物件
    csvWriter.writerow(["Name", "Age", "City"])
    csvWriter.writerow(["Hung", "35", "Taipei"])
    csvWriter.writerow(["James", "40", "Chicago"])

print("------------------------------------------------------------")  # 60個

# ch2_7_1.py

fn = "tmp_out2_7_1.csv"
with open(fn, "w") as csvFile:  # 開啟csv檔案
    csvWriter = csv.writer(csvFile)  # 建立Writer物件
    csvWriter.writerow(["Name", "Age", "City"])
    csvWriter.writerow(["Hung", "35", "Taipei"])
    csvWriter.writerow(["James", "40", "Chicago"])

print("------------------------------------------------------------")  # 60個

# ch2_8.py

infn = "data/csvReport.csv"  # 來源檔案
outfn = "tmp_out2_8.csv"  # 目的檔案
with open(infn) as csvRFile:  # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列

with open(outfn, "w", newline="") as csvOFile:  # 開啟csv檔案供寫入
    csvWriter = csv.writer(csvOFile)  # 建立Writer物件
    for row in listReport:  # 將串列寫入
        csvWriter.writerow(row)

print("------------------------------------------------------------")  # 60個

# ch2_9.py

fn = "tmp_out2_9.csv"
with open(fn, "w", newline="") as csvFile:  # 開啟csv檔案
    csvWriter = csv.writer(csvFile, delimiter="\t")  # 建立Writer物件
    csvWriter.writerow(["Name", "Age", "City"])
    csvWriter.writerow(["Hung", "35", "Taipei"])
    csvWriter.writerow(["James", "40", "Chicago"])

print("------------------------------------------------------------")  # 60個

# ch2_10.py

fn = "tmp_out2_10.csv"
with open(fn, "w", newline="") as csvFile:  # 開啟csv檔案
    fields = ["Name", "Age", "City"]
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)  # 建立Writer物件

    dictWriter.writeheader()  # 寫入標題
    dictWriter.writerow({"Name": "Hung", "Age": "35", "City": "Taipei"})
    dictWriter.writerow({"Name": "James", "Age": "40", "City": "Chicago"})


print("------------------------------------------------------------")  # 60個

# ch2_11.py

dictList = [
    {"Name": "Hung", "Age": "35", "City": "Taipei"},  # 定義串列,元素是字典
    {"Name": "James", "Age": "40", "City": "Chicago"},
]

fn = "tmp_out2_11.csv"
with open(fn, "w", newline="") as csvFile:  # 開啟csv檔案
    fields = ["Name", "Age", "City"]
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)  # 建立Writer物件

    dictWriter.writeheader()  # 寫入標題
    for row in dictList:  # 寫入內容
        dictWriter.writerow(row)

print("------------------------------------------------------------")  # 60個

# ch2_12.py

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
print(headerRow)

print("------------------------------------------------------------")  # 60個

# ch2_13.py

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
for i, header in enumerate(headerRow):
    print(i, header)

print("------------------------------------------------------------")  # 60個

# ch2_14.py

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    highTemps, lowTemps = [], []  # 設定空串列
    for row in csvReader:
        highTemps.append(row[1])  # 儲存最高溫
        lowTemps.append(row[3])  # 儲存最低溫

print("最高溫 : ", highTemps)
print("最低溫 : ", lowTemps)

print("------------------------------------------------------------")  # 60個

# ch2_15.py

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    highTemps = []  # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))  # 儲存最高溫

plt.plot(highTemps)
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch2_16.py

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    highTemps = []  # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))  # 儲存最高溫
plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(highTemps)
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()


print("------------------------------------------------------------")  # 60個

# ch2_17.py
from datetime import datetime

dateObj = datetime.strptime("2017/1/1", "%Y/%m/%d")
print(dateObj)

print("------------------------------------------------------------")  # 60個

# ch2_18.py

from datetime import datetime

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    dates, highTemps = [], []  # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)

plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 圖標增加日期刻度
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch2_19.py

from datetime import datetime

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    dates, highTemps = [], []  # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 圖標增加日期刻度
fig.autofmt_xdate()  # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch2_20.py

from datetime import datetime

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    dates, highTemps = [], []  # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))  # 儲存最高溫
        currentDate = datetime.strptime(row[0], "%Y/%m/%d")
        dates.append(currentDate)

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 圖標增加日期刻度
fig.autofmt_xdate(rotation=60)  # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch2_21.py

from datetime import datetime

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    dates, highTemps, lowTemps = [], [], []  # 設定空串列
    for row in csvReader:
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

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 繪製最高溫
plt.plot(dates, lowTemps)  # 繪製最低溫
fig.autofmt_xdate()  # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch2_22.py

from datetime import datetime

fn = "data/TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
    dates, highTemps, lowTemps = [], [], []  # 設定空串列
    for row in csvReader:
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

fig = plt.figure(dpi=80, figsize=(12, 8))  # 設定繪圖區大小
plt.plot(dates, highTemps)  # 繪製最高溫
plt.plot(dates, lowTemps)  # 繪製最低溫
plt.fill_between(dates, highTemps, lowTemps, color="y", alpha=0.2)  # 填滿區間
fig.autofmt_xdate()  # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch2_23.py
import pickle

game_info = {
    "position_X": "100",
    "position_Y": "200",
    "money": 300,
    "pocket": ["黃金", "鑰匙", "小刀"],
}

fn = "tmp_ch2_23.dat"
fn_obj = open(fn, "wb")  # 二進位開啟
pickle.dump(game_info, fn_obj)
fn_obj.close()

print("------------------------------------------------------------")  # 60個

# ch2_24.py

import pickle

fn = "tmp_ch2_23.dat"
fn_obj = open(fn, "rb")  # 二進位開啟
game_info = pickle.load(fn_obj)
fn_obj.close()
print(game_info)

print("------------------------------------------------------------")  # 60個

# ch2_25.py

import xlwt

fn = "tmp_out2_25.xls"
datahead = ["Phone", "TV", "Notebook"]
price = ["35000", "18000", "28000"]
wb = xlwt.Workbook()
sh = wb.add_sheet("sheet1", cell_overwrite_ok=True)
for i in range(len(datahead)):
    sh.write(0, i, datahead[i])  # 寫入datahead list
for j in range(len(price)):
    sh.write(1, j, price[j])  # 寫入price list

wb.save(fn)

print("------------------------------------------------------------")  # 60個

# ch2_26.py

import xlrd

fn = "tmp_out2_25.xls"
wb = xlrd.open_workbook(fn)
sh = wb.sheets()[0]
rows = sh.nrows
for row in range(rows):
    print(sh.row_values(row))


print("------------------------------------------------------------")  # 60個

# ch3_1.py

import webbrowser

webbrowser.open("http://www.mcut.edu.tw")

print("------------------------------------------------------------")  # 60個

# ch3_2.py

import webbrowser

address = "300新竹市東區南大路345號"
webbrowser.open("http://www.google.com.tw/maps/place/" + address)

print("------------------------------------------------------------")  # 60個

# ch3_3.py

r = 6371  # 地球半徑
x1, y1 = 22.2838, 114.1731  # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168  # 台北車站經緯度

d = 6371 * math.acos(
    math.sin(math.radians(x1)) * math.sin(math.radians(x2))
    + math.cos(math.radians(x1))
    * math.cos(math.radians(x2))
    * math.cos(math.radians(y1 - y2))
)

print("distance = ", d)

print("------------------------------------------------------------")  # 60個

# ch3_5.py

url = "http://www.mcut.edu.tw"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
else:
    print("取得網頁內容失敗")

print("------------------------------------------------------------")  # 60個

# ch3_4.py

url = "http://www.mcut.edu.tw"
htmlfile = requests.get(url)
print(type(htmlfile))

print("------------------------------------------------------------")  # 60個

# ch3_5.py

url = "http://www.mcut.edu.tw"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
else:
    print("取得網頁內容失敗")

print("------------------------------------------------------------")  # 60個

# ch3_6.py

url = "http://www.mcut.edu.tw"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(htmlfile.text))
else:
    print("取得網頁內容失敗")

print("------------------------------------------------------------")  # 60個

# ch3_7.py

url = "http://www.mcut.edu.tw"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
else:
    print("取得網頁內容失敗")
print(htmlfile.text)  # 列印網頁內容

print("------------------------------------------------------------")  # 60個

# ch3_8.py

url = "http://www.mcut.edu.tw"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = "hello world"  # pattern存放欲搜尋的字串
    # 使用方法1
    if pattern in htmlfile.text:  # 方法1
        print("搜尋 %s 成功" % pattern)
    else:
        print("搜尋 %s 失敗" % pattern)
    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)  # 方法2
    if name != None:
        print("%s 出現 %d 次" % (pattern, len(name)))
    else:
        print("%s 出現 0 次" % pattern)
else:
    print("網頁下載失敗")

print("------------------------------------------------------------")  # 60個
"""NG
# ch3_9.py

url = "http://www.mcut.edu.tw/file_not_existed"  # 不存在的內容
htmlfile = requests.get(url)
try:
    htmlfile.raise_for_status()  # 異常處理
    print("下載成功")
except Exception as err:  # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
print("程式結束")

print("------------------------------------------------------------")  # 60個

# ch3_10.py

url = "http://www.gzaxxc.com/file_not_existed"  # 錯誤的網址
htmlfile = requests.get(url)
try:
    htmlfile.raise_for_status()  # 異常處理
    print("下載成功")
except Exception as err:  # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
print("程式結束")

print("------------------------------------------------------------")  # 60個

# ch3_11.py

url = "http://www.gzaxxc.com/file_not_existed"  # 錯誤的網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:  # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
print("程式結束")

print("------------------------------------------------------------")  # 60個
"""
# ch3_12.py

url = "http://aaa.24ht.com.tw/"
htmlfile = requests.get(url)
htmlfile.raise_for_status()

print("------------------------------------------------------------")  # 60個

# ch3_12_1.py
"""
url = "https://www.kingstone.com.tw/new/basic/2013120504769?zone=book&lid=search&actid=WISE"
htmlfile = requests.get(url)
htmlfile.raise_for_status()
"""
print("------------------------------------------------------------")  # 60個

# ch3_13.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://aaa.24ht.com.tw/"
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

print("------------------------------------------------------------")  # 60個

# ch3_13_1.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "https://www.kingstone.com.tw/new/basic/2013120504769?zone=book&lid=search&actid=WISE"
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

print("------------------------------------------------------------")  # 60個

# ch3_13_2.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/75.0.3770.142 Safari/537.36",
}
url = "https://www.kingstone.com.tw/new/basic/2013120504769?zone=book&lid=search&actid=WISE"
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

print("------------------------------------------------------------")  # 60個

# ch3_14.py

url = "http://www.deepmind.com.tw"  # 網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:  # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
# 儲存網頁內容
fn = "tmp_out3_14.txt"
with open(fn, "wb") as file_Obj:  # 以二進位儲存
    for diskStorage in htmlfile.iter_content(40960):  # Response物件處理
        size = file_Obj.write(diskStorage)  # Response物件寫入
        print(size)  # 列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)

print("------------------------------------------------------------")  # 60個

# ch3_15.py

import urllib.request

url = "https://www.mcut.edu.tw"
htmlfile = urllib.request.urlopen(url)
print(type(htmlfile))
print(htmlfile)

print("------------------------------------------------------------")  # 60個

# ch3_16.py
import urllib.request

url = "https://www.mcut.edu.tw"
htmlfile = urllib.request.urlopen(url)
print(htmlfile.read())

print("------------------------------------------------------------")  # 60個

# ch3_17.py

import urllib.request

url = "https://www.mcut.edu.tw"
htmlfile = urllib.request.urlopen(url)
print(htmlfile.read().decode("utf-8"))

print("------------------------------------------------------------")  # 60個

# ch3_18.py

import urllib.request

url = "https://www.mcut.edu.tw"
htmlfile = urllib.request.urlopen(url)
print("版本 : ", htmlfile.version)
print("網址 : ", htmlfile.geturl())
print("下載 : ", htmlfile.status)
print("表頭 : ")
for header in htmlfile.getheaders():
    print(header)

print("------------------------------------------------------------")  # 60個

# ch3_19.py
import urllib.request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://aaa.24ht.com.tw/"
req = urllib.request.Request(url, headers=headers)
htmlfile = urllib.request.urlopen(req)
print(htmlfile.read().decode("utf-8"))

print("------------------------------------------------------------")  # 60個

# ch3_20.py

import urllib.request

url_pict = "https://baidu.com/img/bd_logo1.png"
fn = "baidu.png"
pict = urllib.request.urlretrieve(url_pict, fn)

print("------------------------------------------------------------")  # 60個

# ch3_21.py

from urllib import parse

s = "台灣積體電路製造"
url_code = parse.quote(s)
print("URL編碼  : ", url_code)
code = parse.unquote(url_code)
print("中文編碼 : ", code)

print("------------------------------------------------------------")  # 60個

# ch3_22.py

from urllib import parse

url = "https://docs.python.org/3/search.html?q=parse&check_keywords=yes&area=default"
urp = parse.urlparse(url)
print(type(urp))
print(urp)
print("scheme   = ", urp.scheme)
print("netloc   = ", urp.netloc)
print("path     = ", urp.path)
print("params   = ", urp.params)
print("query    = ", urp.query)
print("fragment = ", urp.fragment)

print("------------------------------------------------------------")  # 60個

# ch3_23.py

from urllib import parse

url = "https://docs.python.org/3/search.html?q=parse&check_keywords=yes&area=default"
urp = parse.urlsplit(url)
print(type(urp))
print(urp)
print("scheme   = ", urp.scheme)
print("netloc   = ", urp.netloc)
print("path     = ", urp.path)
print("query    = ", urp.query)
print("fragment = ", urp.fragment)

print("------------------------------------------------------------")  # 60個

# ch3_24.py

from urllib import parse

scheme = "https"
netloc = "docs.python.org"
path = "/3/search.html"
params = ""
query = "q=parse&check_keywords=yes&area=default"
frament = ""
url_unparse = parse.urlunparse((scheme, netloc, path, params, query, frament))
print(url_unparse)
url_unsplit = parse.urlunsplit([scheme, netloc, path, query, frament])
print(url_unsplit)

print("------------------------------------------------------------")  # 60個

# ch3_25.py

from urllib import parse

url_python = "https://docs.python.org/3/search.html?"
query = {"q": "parse", "check_keywords": "yes", "area": "default"}
url = url_python + parse.urlencode(query)
print(url)

print("------------------------------------------------------------")  # 60個

# ch3_26.py

from urllib import parse

query_str = "q=parse&check_keywords=yes&area=default"
print("parse.parse_qs  = ", parse.parse_qs(query_str))
print("parse.parse_qsl = ", parse.parse_qsl(query_str))

print("------------------------------------------------------------")  # 60個

# ch3_27.py

from urllib import request, error

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
# 錯誤網址
url_error = "http://aaa.24t.com.tw/"  # 錯誤網址
try:
    htmlfile = request.urlopen(url_error)
except error.URLError as e:
    print("錯誤原因 : ", e.reason)
else:
    print("擷取網路資料成功")
# 正確網址
url = "http://aaa.24ht.com.tw/"  # 網址正確
try:
    req = request.Request(url, headers=headers)
    htmlfile = request.urlopen(req)
except error.URLError as e:
    print("錯誤原因 : ", e.reason)
else:
    print("擷取網路資料成功")

print("------------------------------------------------------------")  # 60個

# ch3_28.py

from urllib import request, error

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
# 錯誤1
url_error = "http://aaa.24t.com.tw/"  # 錯誤網址
try:
    htmlfile = request.urlopen(url_error)
except error.HTTPError as e:
    print("錯誤代碼 : ", e.code)
    print("錯誤原因 : ", e.reason)
    print("回應表頭 : ", e.headers)
except error.URLError as e:
    print("錯誤原因 : ", e.reason)
else:
    print("擷取網路資料成功")
print("-" * 70)
# 錯誤2
url = "http://aaa.24ht.com.tw/"  # 網址正確
try:
    htmlfile = request.urlopen(url)
except error.HTTPError as e:
    print("錯誤代碼 : ", e.code)
    print("錯誤原因 : ", e.reason)
    print("回應表頭 : ", e.headers)
except error.URLError as e:
    print("錯誤原因 : ", e.reason)
else:
    print("擷取網路資料成功")
print("-" * 70)
# 正確
url = "http://aaa.24ht.com.tw/"  # 網址正確
try:
    req = request.Request(url, headers=headers)
    htmlfile = request.urlopen(req)
except error.HTTPError as e:
    print("錯誤代碼 : ", e.code)
    print("錯誤原因 : ", e.reason)
    print("回應表頭 : ", e.headers)
except error.URLError as e:
    print("錯誤原因 : ", e.reason)
else:
    print("擷取網路資料成功")

print("------------------------------------------------------------")  # 60個

# ch3_29.py

url = "https://www.httpbin.org/get"
r = requests.get(url)
print(r.url)

print("------------------------------------------------------------")  # 60個

# ch3_30.py

url = "https://www.httpbin.org/get"
form_data = {"gender": "M", "page": "1"}
r = requests.get(url, params=form_data)
print(r.url)

print("------------------------------------------------------------")  # 60個

# ch3_31.py

url = "https://www.httpbin.org/post"
form_data = {"gender": "M", "page": "1"}
r = requests.post(url, data=form_data)
print(r.url)
print("-" * 70)
print(r.text)

print("------------------------------------------------------------")  # 60個

# ch3_32.py

url = "https://www.httpbin.org/post"
form_data = {"gender": "M", "page": "1"}
r = requests.post(url, data=json.dumps(form_data))
print(r.url)
print("-" * 70)
print(r.text)

print("------------------------------------------------------------")  # 60個

# ch3_33.py

url = "https://www.httpbin.org/post"
form_data = {"gender": "M", "page": "1"}
r = requests.post(url, json=form_data)
print(r.url)
print("-" * 70)
print(r.text)

print("------------------------------------------------------------")  # 60個

# ch3_34.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "https://www.httpbin.org/post"
form_data = {"gender": "M", "page": "1"}
r = requests.post(url, json=form_data, headers=headers)
print(r.url)
print("-" * 70)
print("r.request.headers :\n", r.request.headers)
print("-" * 70)
print("r.headers :\n", r.headers)

print("------------------------------------------------------------")  # 60個

# ch3_35.py

url = "https://www.httpbin.org/get"
r = requests.get(url)
print(r.status_code)
print(r.reason)

print("------------------------------------------------------------")  # 60個

# ch3_36.py

url = "https://www.httpbin.org/html"
r = requests.get(url)
print(r.encoding)
print("-" * 70)
print(r.text)

print("------------------------------------------------------------")  # 60個

# ch3_37.py

url = "https://www.httpbin.org/response-headers?freeform="
r = requests.get(url)
if r.status_code == 200:
    print(r.headers.get("content-type"))
    print("-" * 70)
    print(r.json())

print("------------------------------------------------------------")  # 60個

# ch3_38.py

url = "https://www.httpbin.org/image/jpeg"
r = requests.get(url)
img = r.content

fn = "tmp_out3_38.jpg"
with open(fn, "wb") as fout:
    fout.write(img)

print("------------------------------------------------------------")  # 60個

# ch3_39.py

url = "http://httpbin.org/cookies"
cookies = dict(key1="value1")
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個
"""NG
# ch3_40.py

proxies = {
    "http": "http://111.231.81.109:3128",  # ip:port
    "https": "https://111.231.81.109:1080",  # ip:port
}

r = requests.get("https://docs.python.org", proxies=proxies)
"""
print("------------------------------------------------------------")  # 60個

# ch3_41.py

proxies = {
    "http": "http://203.83.182.86:8080",  # ip:port
}

r = requests.get("https://docs.python.org", proxies=proxies)
if r.status_code == 200:
    print("代理IP使用成功")

print("------------------------------------------------------------")  # 60個

# ch4_1.py

years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index=years)
hongkong = pd.Series([25, 26, 27], index=years)
singapore = pd.Series([30, 29, 31], index=years)
citydf = pd.concat([beijing, hongkong, singapore])  # 預設axis=0
print(type(citydf))
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_2.py

years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index=years)
hongkong = pd.Series([25, 26, 27], index=years)
singapore = pd.Series([30, 29, 31], index=years)
citydf = pd.concat([beijing, hongkong, singapore], axis=1)  # axis=1
print(type(citydf))
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_3.py

years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index=years)
hongkong = pd.Series([25, 26, 27], index=years)
singapore = pd.Series([30, 29, 31], index=years)
citydf = pd.concat([beijing, hongkong, singapore], axis=1)  # axis=1
cities = ["Beijing", "HongKong", "Singapore"]
citydf.columns = cities
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_4.py

years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index=years)
hongkong = pd.Series([25, 26, 27], index=years)
singapore = pd.Series([30, 29, 31], index=years)
beijing.name = "Beijing"
hongkong.name = "HongKong"
singapore.name = "Singapore"
citydf = pd.concat([beijing, hongkong, singapore], axis=1)
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_5.py

data = [{"apple": 50, "Orange": 30, "Grape": 80}, {"apple": 50, "Grape": 80}]
fruits = pd.DataFrame(data)
print(fruits)

print("------------------------------------------------------------")  # 60個

# ch4_6.py

cities = {
    "country": ["China", "Japan", "Singapore"],
    "town": ["Beijing", "Tokyo", "Singapore"],
    "population": [2000, 1600, 600],
}
citydf = pd.DataFrame(cities)
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_7.py

cities = {
    "country": ["China", "Japan", "Singapore"],
    "town": ["Beijing", "Tokyo", "Singapore"],
    "population": [2000, 1600, 600],
}
rowindex = ["first", "second", "third"]
citydf = pd.DataFrame(cities, index=rowindex)
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_8.py

cities = {
    "country": ["China", "Japan", "Singapore"],
    "town": ["Beijing", "Tokyo", "Singapore"],
    "population": [2000, 1600, 600],
}
citydf = pd.DataFrame(cities, columns=["town", "population"], index=cities["country"])
print(citydf)

print("------------------------------------------------------------")  # 60個

# ch4_9.py

cities = {
    "Country": ["China", "China", "Thailand", "Japan", "Singapore"],
    "Town": ["Beijing", "Shanghai", "Bangkok", "Tokyo", "Singapore"],
    "Population": [2000, 2300, 900, 1600, 600],
}
df = pd.DataFrame(cities, columns=["Town", "Population"], index=cities["Country"])
print(df)

print("------------------------------------------------------------")  # 60個

# ch4_10.py

name = ["Frank", "Peter", "John"]
score = ["first", "second", "final"]
df = pd.DataFrame(np.random.randint(60, 100, size=(3, 3)), columns=name, index=score)
print(df)

print("------------------------------------------------------------")  # 60個

# ch4_11.py

course = ["Chinese", "English", "Math", "Natural", "Society"]
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame(
    [chinese, eng, math, nature, social], columns=course, index=range(1, 6)
)
print(df)

print("------------------------------------------------------------")  # 60個

# ch4_12.py

course = ["Chinese", "English", "Math", "Natural", "Society"]
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame(
    [chinese, eng, math, nature, social], columns=course, index=range(1, 6)
)
df.to_csv("tmp_out4_12a.csv")
df.to_csv("tmp_out4_12b.csv", header=False, index=False)

print("------------------------------------------------------------")  # 60個

# ch4_13.py

course = ["Chinese", "English", "Math", "Natural", "Society"]
x = pd.read_csv("tmp_out4_12a.csv", index_col=0)
y = pd.read_csv("tmp_out4_12b.csv", names=course)
print(x)
print(y)

print("------------------------------------------------------------")  # 60個

# ch4_14.py

population = [860, 1100, 1450, 1800, 2020, 2200, 2260]
tw = pd.Series(population, index=range(1950, 2011, 10))
tw.plot(title="Population in Taiwan")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_15.py

cities = {
    "population": [1000, 850, 800, 1500, 600, 800],
    "town": ["New York", "Chicago", "Bangkok", "Tokyo", "Singapore", "HongKong"],
}
tw = pd.DataFrame(cities, columns=["population"], index=cities["town"])

tw.plot(title="Population in the World")
plt.xlabel("City")
plt.ylabel("Population")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_16.py

cities = {
    "population": [1000, 850, 800, 1500, 600, 800],
    "town": ["New York", "Chicago", "Bangkok", "Tokyo", "Singapore", "HongKong"],
}
tw = pd.DataFrame(cities, columns=["population"], index=cities["town"])

tw.plot(title="Population in the World", kind="bar")
plt.xlabel("City")
plt.ylabel("Population")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_17.py

cities = {
    "population": [1000, 850, 800, 1500, 600, 800],
    "area": [400, 500, 850, 300, 200, 320],
    "town": ["New York", "Chicago", "Bangkok", "Tokyo", "Singapore", "HongKong"],
}
tw = pd.DataFrame(cities, columns=["population", "area"], index=cities["town"])

tw.plot(title="Population in the World")
plt.xlabel("City")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_18.py

cities = {
    "population": [10000000, 8500000, 8000000, 15000000, 6000000, 8000000],
    "area": [400, 500, 850, 300, 200, 320],
    "town": ["New York", "Chicago", "Bangkok", "Tokyo", "Singapore", "HongKong"],
}
tw = pd.DataFrame(cities, columns=["population", "area"], index=cities["town"])

tw.plot(title="Population in the World")
plt.xlabel("City")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_19.py

cities = {
    "population": [10000000, 8500000, 8000000, 15000000, 6000000, 8000000],
    "area": [400, 500, 850, 300, 200, 320],
    "town": ["New York", "Chicago", "Bangkok", "Tokyo", "Singapore", "HongKong"],
}
tw = pd.DataFrame(cities, columns=["population", "area"], index=cities["town"])

fig, ax = plt.subplots()
fig.suptitle("City Statistics")
ax.set_ylabel("Population")
ax.set_xlabel("City")

ax2 = ax.twinx()
ax2.set_ylabel("Area")
tw["population"].plot(ax=ax, rot=90)  # 繪製人口數線
tw["area"].plot(ax=ax2, style="g-")  # 繪製面積線
ax.legend(loc=1)  # 圖例位置在右上
ax2.legend(loc=2)  # 圖例位置在左上
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_20.py

cities = {
    "population": [10000000, 8500000, 8000000, 15000000, 6000000, 8000000],
    "area": [400, 500, 850, 300, 200, 320],
    "town": ["New York", "Chicago", "Bangkok", "Tokyo", "Singapore", "HongKong"],
}
tw = pd.DataFrame(cities, columns=["population", "area"], index=cities["town"])

fig, ax = plt.subplots()
fig.suptitle("City Statistics")
ax.set_ylabel("Population")
ax.set_xlabel("City")
ax.ticklabel_format(style="plain")  # 不用科學記號表示
ax2 = ax.twinx()
ax2.set_ylabel("Area")
tw["population"].plot(ax=ax, rot=90)  # 繪製人口數線
tw["area"].plot(ax=ax2, style="g-")  # 繪製面積線
ax.legend(loc=1)  # 圖例位置在右上
ax2.legend(loc=2)  # 圖例位置在左上
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_21.py

fruits = ["Apples", "Bananas", "Grapes", "Pears", "Oranges"]
s = pd.Series([2300, 5000, 1200, 2500, 2900], index=fruits, name="Fruits Shop")
explode = [0.4, 0, 0, 0.2, 0]
s.plot.pie(explode=explode, autopct="%1.2f%%")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_21_1.py

from datetime import datetime

timeNow = datetime.now()
print(type(timeNow))
print("現在時間 : ", timeNow)

print("------------------------------------------------------------")  # 60個

# ch4_21_10.py

dates = pd.date_range("3/11/2019", "3/15/2019")
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index=dates)
ts.plot(title="Data in Time Series")
plt.xlabel("Date")
plt.ylabel("Data")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_21_2.py

from datetime import datetime

timeNow = datetime.now()
print(type(timeNow))
print("現在時間 : ", timeNow)
print("年 : ", timeNow.year)
print("月 : ", timeNow.month)
print("日 : ", timeNow.day)
print("時 : ", timeNow.hour)
print("分 : ", timeNow.minute)
print("秒 : ", timeNow.second)

print("------------------------------------------------------------")  # 60個

# ch4_21_3.py

from datetime import datetime

timeStop = datetime(2019, 7, 28, 19, 50, 50)
while datetime.now() < timeStop:
    print("Program is sleeping.", end="")
print("Wake up")

print("------------------------------------------------------------")  # 60個

# ch4_21_4.py

from datetime import datetime, timedelta

deltaTime = timedelta(days=3, hours=5, minutes=8, seconds=10)
print(deltaTime.days, deltaTime.seconds, deltaTime.microseconds)

print("------------------------------------------------------------")  # 60個

# ch4_21_5.py
from datetime import datetime, timedelta

deltaTime = timedelta(days=3, hours=5, minutes=8, seconds=10)
print(deltaTime.total_seconds())

print("------------------------------------------------------------")  # 60個

# ch4_21_6.py

from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)
dates = [start + timedelta(days=x) for x in range(0, ndays)]
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index=dates)
print(type(ts))
print(ts)

print("------------------------------------------------------------")  # 60個

# ch4_21_7.py

from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)
dates = [start + timedelta(days=x) for x in range(0, ndays)]
data1 = [34, 44, 65, 53, 39]
ts1 = pd.Series(data1, index=dates)

data2 = [34, 44, 65, 53, 39]
ts2 = pd.Series(data2, index=dates)

addts = ts1 + ts2
print("ts1+ts2")
print(addts)

meants = (ts1 + ts2) / 2
print("(ts1+ts2)/2")
print(meants)

print("------------------------------------------------------------")  # 60個

# ch4_21_8.py

from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)
dates1 = [start + timedelta(days=x) for x in range(0, ndays)]
data1 = [34, 44, 65, 53, 39]
ts1 = pd.Series(data1, index=dates1)

dates2 = [start - timedelta(days=x) for x in range(0, ndays)]
data2 = [34, 44, 65, 53, 39]
ts2 = pd.Series(data2, index=dates2)

addts = ts1 + ts2
print("ts1+ts2")
print(addts)

print("------------------------------------------------------------")  # 60個

# ch4_21_9.py

dates = pd.date_range("3/11/2019", "3/15/2019")
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index=dates)
print(type(ts))
print(ts)

print("------------------------------------------------------------")  # 60個

# ch4_22.py

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
try:
    htmlfile = requests.get(url)  # 將檔案下載至htmlfile
    print("下載成功")
except Exception as err:
    print("下載失敗")

fn = "iris.csv"  # 未來儲存鳶尾花的檔案
with open(fn, "wb") as fileobj:  # 開啟iris.csv
    for diskstorage in htmlfile.iter_content(10240):
        size = fileobj.write(diskstorage)  # 寫入

print("------------------------------------------------------------")  # 60個

# ch4_23.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)
print("資料集長度 : ", len(iris))
print(iris)

print("------------------------------------------------------------")  # 60個

# ch4_24.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)

iris.plot(x="sepal_len", y="sepal_wd", kind="scatter")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Sepal length and width anslysis")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_25.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)

plt.plot(iris["sepal_len"], iris["sepal_wd"], "*", color="g")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Sepal length and width anslysis")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_26.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)

# 擷取不同品種的鳶尾花
iris_setosa = iris[iris["species"] == "Iris-setosa"]
iris_versicolor = iris[iris["species"] == "Iris-versicolor"]
iris_virginica = iris[iris["species"] == "Iris-virginica"]
# 繪製散點圖
plt.plot(
    iris_setosa["sepal_len"], iris_setosa["sepal_wd"], "*", color="g", label="setosa"
)
plt.plot(
    iris_versicolor["sepal_len"],
    iris_versicolor["sepal_wd"],
    "x",
    color="b",
    label="versicolor",
)
plt.plot(
    iris_virginica["sepal_len"],
    iris_virginica["sepal_wd"],
    ".",
    color="r",
    label="virginica",
)
# 標註軸和標題
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Sepal length and width anslysis")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_27.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)

# 鳶尾花分組統計均值
iris_mean = iris.groupby("species", as_index=False).mean()
# 繪製直條圖
iris_mean.plot(kind="bar")
# 刻度處理
plt.xticks(iris_mean.index, iris_mean["species"], rotation=0)

plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_28.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)
iris["species"] = iris["species"].apply(lambda x: x.replace("Iris-", ""))
# 鳶尾花分組統計均值
iris_mean = iris.groupby("species", as_index=False).mean()
# 繪製直條圖
iris_mean.plot(kind="bar")
# 刻度處理
plt.xticks(iris_mean.index, iris_mean["species"], rotation=0)

plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_29.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)
iris["species"] = iris["species"].apply(lambda x: x.replace("Iris-", ""))
# 鳶尾花分組統計均值
iris_mean = iris.groupby("species", as_index=False).mean()
# 繪製堆疊直條圖
iris_mean.plot(kind="bar", stacked=True)
# 刻度處理
plt.xticks(iris_mean.index, iris_mean["species"], rotation=0)

plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_30.py

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("iris.csv", names=colName)
iris["species"] = iris["species"].apply(lambda x: x.replace("Iris-", ""))
# 鳶尾花分組統計均值
iris_mean = iris.groupby("species", as_index=False).mean()
# 繪製堆疊橫條圖
iris_mean.plot(kind="barh", stacked=True)
# 刻度處理
plt.yticks(iris_mean.index, iris_mean["species"], rotation=0)

plt.show()

print("------------------------------------------------------------")  # 60個

# ch4_31.py

url = "http://www.stockq.org/market/currency.php"
currencys = pd.read_html(url)

print(type(currencys))  # 列出資料型態
print(currencys)  # 列出匯率的串列內容

print("------------------------------------------------------------")  # 60個

# ch4_32.py

url = "http://www.stockq.org/market/currency.php"
currencys = pd.read_html(url)  # 讀取全球匯率行情表

item = 0
for currency in currencys:
    print("元素 : ", item)  # 列出元素編號
    print(currency)  # 列出元素內容
    print()
    item += 1

print("------------------------------------------------------------")  # 60個
"""NG
# ch4_33.py

url = "http://www.stockq.org/market/currency.php"
currencys = pd.read_html(url)  # 讀取全球匯率行情表

currency = currencys[7]  # 讀取第7元素
currency = currency.drop(currency.index[[0, 1]])  # 拋棄前2 row
currency.columns = ["貨幣", "匯率", "漲跌", "比例", "台北"]  # 建立column標題
currency.index = range(len(currency.index))  # 建立row標題
print(currency)
"""
print("------------------------------------------------------------")  # 60個

# ch5_1.py

htmlFile = requests.get("http://www.deepmind.com.tw")
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
print("列印BeautifulSoup物件資料型態 ", type(objSoup))

print("------------------------------------------------------------")  # 60個

# ch5_2.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
print("列印BeautifulSoup物件資料型態 ", type(objSoup))

print("------------------------------------------------------------")  # 60個

# ch5_3.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
print("物件類型  = ", type(objSoup.title))
print("列印title = ", objSoup.title)

print("------------------------------------------------------------")  # 60個

# ch5_4.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
print("列印title = ", objSoup.title)
print("title內容 = ", objSoup.title.text)

print("------------------------------------------------------------")  # 60個

# ch5_5.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.find("h1")
print("資料型態       = ", type(objTag))
print("列印Tag        = ", objTag)
print("Text屬性內容   = ", objTag.text)
print("String屬性內容 = ", objTag.string)

print("------------------------------------------------------------")  # 60個

# ch5_6.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.find_all("h1")
print("資料型態    = ", type(objTag))  # 列印資料型態
print("列印Tag串列 = ", objTag)  # 列印串列
print("以下是列印串列元素 : ")
for data in objTag:  # 列印串列元素內容
    print(data.text)

print("------------------------------------------------------------")  # 60個

# ch5_6_1.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.find_all("h1", limit=2)
for data in objTag:  # 列印串列元素內容
    print(data.text)

print("------------------------------------------------------------")  # 60個

# ch5_7.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.find_all("h1")
print("資料型態    = ", type(objTag))  # 列印資料型態
print("列印Tag串列 = ", objTag)  # 列印串列
print("\n使用Text屬性列印串列元素 : ")
for data in objTag:  # 列印串列元素內容
    print(data.text)
print("\n使用getText()方法列印串列元素 : ")
for data in objTag:
    print(data.getText())

print("------------------------------------------------------------")  # 60個

# ch5_7_1.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.find(id="author")
print(objTag)
print(objTag.text)

print("------------------------------------------------------------")  # 60個

# ch5_7_2.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.find_all(id="content")
for tag in objTag:
    print(tag)
    print(tag.text)

print("------------------------------------------------------------")  # 60個

# ch5_7_3.py

htmlFile = "<div book-info='deepmind'>深智數位</div>"
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
tag = objSoup.find(attrs={"book-info": "deepmind"})
print(tag)
print(tag.text)

print("------------------------------------------------------------")  # 60個

# ch5_7_4.py

htmlFile = "<h1 class='boldtext'>深智數位</h1>"
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
tag = objSoup.find("h1", class_="boldtext")
print(tag)
print(tag.text)
print("-" * 70)
tag = objSoup.find("h1", "boldtext")
print(tag)
print(tag.text)

print("------------------------------------------------------------")  # 60個

# ch5_7_5.py

htmlFile = "<h1 class='boldtext'>深智數位</h1>"
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
tag = objSoup.find("h1", class_=re.compile("text"))
print(tag)
print(tag.text)

print("------------------------------------------------------------")  # 60個

# ch5_7_6.py

htmlFile = "<h1 class='bold italic'>深智數位</h1>"
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
tag = objSoup.find("h1", class_="bold")
print(tag)
print(tag.text)
print("-" * 70)
tag = objSoup.find("h1", class_="italic")
print(tag)
print(tag.text)

print("------------------------------------------------------------")  # 60個

# ch5_8.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.select("#author")
print("資料型態     = ", type(objTag))  # 列印資料型態
print("串列長度     = ", len(objTag))  # 列印串列長度
print("元素資料型態 = ", type(objTag[0]))  # 列印元素資料型態
print("元素內容     = ", objTag[0].getText())  # 列印元素內容

print("------------------------------------------------------------")  # 60個

# ch5_9.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.select("#author")
print("列出串列元素的資料型態    = ", type(objTag[0]))
print(objTag[0])
print("列出str()轉換過的資料型態 = ", type(str(objTag[0])))
print(str(objTag[0]))

print("------------------------------------------------------------")  # 60個

# ch5_10.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
objTag = objSoup.select("#author")
print(str(objTag[0].attrs))

print("------------------------------------------------------------")  # 60個

# ch5_11.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
pObjTag = objSoup.select("p")
print("含<p>標籤的串列長度 = ", len(pObjTag))
for pObj in pObjTag:
    print(str(pObj))  # 內部有子標籤<strong>字串
    print(pObj.getText())  # 沒有子標籤
    print(pObj.text)  # 沒有子標籤

print("------------------------------------------------------------")  # 60個

# ch5_12.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
imgTag = objSoup.select("img")
print("含<img>標籤的串列長度 = ", len(imgTag))
for img in imgTag:
    print(img)

print("------------------------------------------------------------")  # 60個

# ch5_13.py

htmlFile = open("data/myhtml.html", encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
imgTag = objSoup.select("img")
print("含<img>標籤的串列長度 = ", len(imgTag))
for img in imgTag:
    print("列印標籤串列 = ", img)
    print("列印圖檔     = ", img.get("src"))
    print("列印圖檔     = ", img["src"])

print("------------------------------------------------------------")  # 60個

# ch5_13_1.py

url = "data/ch5_2_1.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
titleobj = objSoup.find_all("h2")  # h2標題
print(titleobj[2].text)

itemobj = objSoup.find("ol", type="I")  # type='I'
items = itemobj.find_all("li")
for item in items:
    print(item.text)

print("------------------------------------------------------------")  # 60個

# ch5_13_2.py

url = "data/ch5_2_2.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

mycity = []
cityobj = objSoup.find("dl")
cities = cityobj.find_all("dt")
for city in cities:
    mycity.append(city.text)  # mycity串列

mycountry = []
countryobj = objSoup.find("dl")
countries = countryobj.find_all("dd")
for country in countries:
    mycountry.append(country.text)  # mycountry串列

print("國家 = ", mycountry)
print("首都 = ", mycity)
data = dict(zip(mycountry, mycity))
print(data)  # 字典顯示結果

print("------------------------------------------------------------")  # 60個

# ch5_13_3.py

url = "data/ch5_2_3.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

myriver = []  # 河川
tableobj = objSoup.find("table").find("tbody")
tables = tableobj.find_all("tr")
for table in tables:
    river = table.find("td")
    myriver.append(river.text)

mycountry = []  # 國家
for table in tables:
    countries = table.find_all("td")
    country = countries[1]
    mycountry.append(country.text)

print("國家 = ", mycountry)
print("河川 = ", myriver)
data = dict(zip(mycountry, myriver))
print(data)  # 字典顯示結果

print("------------------------------------------------------------")  # 60個

# ch5_13_4.py

url = "data/ch5_2_3.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

myriver = []  # 河川
mycountry = []  # 國家
tableobj = objSoup.find("table").find("tbody")
tables = tableobj.find_all("tr")
for table in tables:
    river = table.find("td")
    myriver.append(river.text)
    country = river.find_next_sibling("td")  # 下一個節點
    mycountry.append(country.text)

print("國家 = ", mycountry)
print("河川 = ", myriver)
data = dict(zip(mycountry, myriver))
print(data)  # 字典顯示結果

print("------------------------------------------------------------")  # 60個

# ch5_13_5.py

url = "data/ch5_2_3.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

myriver = []  # 河川
mystate = []  # 洲名
tableobj = objSoup.find("table").find("tbody")
tables = tableobj.find_all("tr")

for table in tables:
    countries = table.find_all("td")
    country = countries[1]  # 國家節點
    river = country.find_previous_sibling("td")  # 前一個節點
    myriver.append(river.text)
    state = country.find_next_sibling("td")  # 下一個節點
    mystate.append(state.text)

print("洲名 = ", mystate)
print("河川 = ", myriver)
data = dict(zip(mystate, myriver))
print(data)  # 字典顯示結果

print("------------------------------------------------------------")  # 60個

# ch5_13_6.py

url = "data/ch5_2_1.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
titleobj = objSoup.find("h2")  # h2標題
title = titleobj.find_next_siblings("h2")  # 下一系列節點
print("find_next_siblings     = ", title)

titleobj = objSoup.find_all("h2")
title = titleobj[2].find_previous_siblings("h2")  # 前一系列節點
print("find_previous_siblings = ", title)

print("------------------------------------------------------------")  # 60個

# ch5_13_7.py

url = "data/ch5_2_3.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

myriver = []  # 河川
tableobj = objSoup.find("table").find("tbody")
tables = tableobj.find_all("tr")
river = tables[1].find("td")
print(river.text)

river_parent = river.parent()
print(river_parent)

print("------------------------------------------------------------")  # 60個

# ch5_13_8.py

url = "data/ch5_2_3.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

myriver = []  # 河川
tableobj = objSoup.find("table").find("tbody")
tables = tableobj.find_all("tr")
river = tables[1].find("td")
print(river.text)

previous_row = river.parent.find_previous_sibling()
print(previous_row)
next_row = river.parent.find_next_sibling()
print(next_row)

print("------------------------------------------------------------")  # 60個

# ch5_13_9.py

url = "data/ch5_2_3.html"
htmlFile = open(url, encoding="utf-8")
objSoup = bs4.BeautifulSoup(htmlFile, "lxml")

myriver = []  # 河川
tableobj = objSoup.find("table").find("tbody")
tables = tableobj.find_all("tr")
river = tables[0].find("td")
print(river.text)
previous_rows = river.parent.find_next_siblings()
print(previous_rows)

river = tables[2].find("td")
print(river.text)
next_rows = river.parent.find_previous_siblings()
print(next_rows)

print("------------------------------------------------------------")  # 60個

# ch5_14.py

url = "http://www.grandtech.info/"  # 上奇資訊網頁
html = requests.get(url)
print("網頁下載中 ...")
html.raise_for_status()  # 驗證網頁是否下載成功
print("網頁下載完成")

destDir = "tmp_out5_14"  # 設定未來儲存圖片的資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)  # 建立資料夾供未來儲存圖片

objSoup = bs4.BeautifulSoup(html.text, "lxml")  # 建立BeautifulSoup物件

imgTag = objSoup.select("img")  # 搜尋所有圖片檔案
print("搜尋到的圖片數量 = ", len(imgTag))  # 列出搜尋到的圖片數量
if len(imgTag) > 0:  # 如果有找到圖片則執行下載與儲存
    for i in range(len(imgTag)):  # 迴圈下載圖片與儲存
        imgUrl = imgTag[i].get("src")  # 取得圖片的路徑
        print("%s 圖片下載中 ... " % imgUrl)
        finUrl = url + imgUrl  # 取得圖片在Internet上的路徑
        print("%s 圖片下載中 ... " % finUrl)
        picture = requests.get(finUrl)  # 下載圖片
        picture.raise_for_status()  # 驗證圖片是否下載成功
        print("%s 圖片下載成功" % finUrl)

        # 先開啟檔案, 再儲存圖片
        pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), "wb")
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

# ch5_15.py

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://aaa.24ht.com.tw/"  # 這個伺服器會擋住網頁
html = requests.get(url, headers=headers)
print("網頁下載中 ...")
html.raise_for_status()  # 驗證網頁是否下載成功
print("網頁下載完成")

destDir = "tmp_out5_15"  # 設定儲存資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)  # 建立目錄供未來儲存圖片

objSoup = bs4.BeautifulSoup(html.text, "lxml")  # 建立BeautifulSoup物件

imgTag = objSoup.select("img")  # 搜尋所有圖片檔案
print("搜尋到的圖片數量 = ", len(imgTag))  # 列出搜尋到的圖片數量
if len(imgTag) > 0:  # 如果有找到圖片則執行下載與儲存
    for i in range(len(imgTag)):  # 迴圈下載圖片與儲存
        imgUrl = imgTag[i].get("src")  # 取得圖片的路徑
        print("%s 圖片下載中 ... " % imgUrl)
        finUrl = url + imgUrl  # 取得圖片在Internet上的路徑
        print("%s 圖片下載中 ... " % finUrl)
        picture = requests.get(finUrl, headers=headers)  # 下載圖片
        picture.raise_for_status()  # 驗證圖片是否下載成功
        print("%s 圖片下載成功" % finUrl)

        # 先開啟檔案, 再儲存圖片
        pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), "wb")
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

# ch5_16.py

url = "http://www.taiwanlottery.com.tw"
html = requests.get(url)
print("網頁下載中 ...")
html.raise_for_status()  # 驗證網頁是否下載成功
print("網頁下載完成")

objSoup = bs4.BeautifulSoup(html.text, "lxml")  # 建立BeautifulSoup物件

dataTag = objSoup.select(".contents_box02")  # 尋找class是contents_box02
print("串列長度", len(dataTag))
for i in range(len(dataTag)):  # 列出含contents_box02的串列
    print(dataTag[i])
"""NG
# 找尋開出順序與大小順序的球
balls = dataTag[0].find_all("div", {"class": "ball_tx ball_green"})
print("開出順序 : ", end="")
for i in range(6):  # 前6球是開出順序
    print(balls[i].text, end="   ")

print("\n大小順序 : ", end="")
for i in range(6, len(balls)):  # 第7球以後是大小順序
    print(balls[i].text, end="   ")

# 找出第二區的紅球
redball = dataTag[0].find_all("div", {"class": "ball_red"})
print("\n第二區   :", redball[0].text)
"""
print("------------------------------------------------------------")  # 60個

# ch5_17.py

htmlFile = requests.get("https://tw.yahoo.com/")
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
headline_news = objSoup.find_all("a", class_="story-title")
for h in headline_news:
    print("焦點新聞 : " + h.text)
    print("新聞網址 : " + h.get("href"))


print("------------------------------------------------------------")  # 60個

# ch5_18.py

# 使用自己的IP
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "http://ip.filefab.com/index.php"
htmlFile = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(htmlFile.text, "lxml")
ip = soup.find("h1", id="ipd")
"""NG
print(ip.text.strip())
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

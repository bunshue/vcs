"""
pygal.maps.world

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


import bs4
import requests
import json
import csv

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from pygal.maps.world import COUNTRIES

"""
print(type(COUNTRIES)) # 字典

# 搜尋 國家代碼 和 國家名稱
for countryCode in sorted(COUNTRIES.keys()):
    # print("國家代碼 :", countryCode, "  國家名稱 = ", COUNTRIES[countryCode])
    pass

# 搜尋 國家代碼 和 國家名稱 字典
for dictCode, dictName in COUNTRIES.items():
    print(dictCode, dictName)
"""

import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "China in the Map"  # 世界地圖標題
worldMap.add("China", ["cn"])  # 標記中國
worldMap.render_to_file("tmp_世界地圖_中國.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "China/Japan/Thailand"  # 世界地圖標題
worldMap.add("Asia", ["cn", "jp", "th"])  # 標記Asia
worldMap.render_to_file("tmp_世界地圖_亞洲_中日泰.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = " Asia, Europe, Africa, and North America"  # 世界地圖標題
worldMap.add("Asia", ["cn", "jp", "th"])  # 標記Asia
worldMap.add("Europe", ["fr", "de", "it"])  # 標記Europe
worldMap.add("Africa", ["eg", "ug", "ng"])  # 標記Africa
worldMap.add("North America", ["ca", "us", "mx"])  # 標記北美洲
worldMap.render_to_file("tmp_世界地圖_亞歐非北美洲.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "Populations in China/Japan/Thailand"  # 世界地圖標題
worldMap.add("Asia", {"cn": 1262645000, "jp": 126870000, "th": 63155029})  # 標記人口資訊
worldMap.render_to_file("tmp_世界地圖人口_亞洲_中日泰.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

import pygal.maps.world
from pygal.maps.world import COUNTRIES


def getCountryCode(countryName):
    # 輸入國家名稱回傳國家代碼
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode  # 如果找到則回傳國家代碼
    return None  # 找不到則回傳None


fn = "populations.json"
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
worldMap.render_to_file("tmp_世界地圖人口1.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

import pygal.maps.world
from pygal.maps.world import COUNTRIES


fn = "populations.json"
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
worldMap.render_to_file("tmp_世界地圖人口2.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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

import sys

import json
import pygal.maps.world
from pygal_maps_world.maps import COUNTRIES

"""

pip install pygal
pip install pygal_maps_world

"""
print("------------------------------------------------------------")  # 60個

for countryCode in sorted(COUNTRIES.keys()):
    print("國家代碼 :",countryCode,"  國家名稱 = ",COUNTRIES[countryCode])

print("------------------------------------------------------------")  # 60個

def getCountryCode(countryName):
    '''輸入國家名稱回傳國家代碼'''
    for dictCode, dictName in COUNTRIES.items():    # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode                         # 如果找到則回傳國家代碼
    return None                                     # 找不到則回傳None

fn = 'data/populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                     # 讀取人口數據json檔案

for getData in getDatas:
    if getData['Year'] == '2000':                   # 篩選2000年的數據
        countryName = getData['Country Name']       # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData['Numbers'])) # 人口數       
        if countryCode != None:
            print(countryCode, ":", population)     # 國家名稱相符
        else:
            print(countryName," 名稱不吻合:")       # 國家名稱不吻合

print("------------------------------------------------------------")  # 60個

worldMap = pygal.maps.world.World()         # 建立世界地圖物件
worldMap.title = 'China in the Map'         # 世界地圖標題
worldMap.add('China',['cn'])                # 標記中國
worldMap.render_to_file('tmp_06.svg')     # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

worldMap = pygal.maps.world.World()         # 建立世界地圖物件
worldMap.title = 'China/Japan/Thailand'     # 世界地圖標題
worldMap.add('Asia',['cn', 'jp', 'th'])     # 標記Asia
worldMap.render_to_file('tmp_07.svg')     # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

worldMap = pygal.maps.world.World()                         # 建立世界地圖物件
worldMap.title = ' Asia, Europe, Africa, and North America' # 世界地圖標題
worldMap.add('Asia',['cn', 'jp', 'th'])                     # 標記Asia
worldMap.add('Europe',['fr', 'de', 'it'])                   # 標記Europe
worldMap.add('Africa',['eg', 'ug', 'ng'])                   # 標記Africa
worldMap.add('North America',['ca', 'us', 'mx'])            # 標記北美洲
worldMap.render_to_file('tmp_08.svg')                     # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

worldMap = pygal.maps.world.World()                     # 建立世界地圖物件
worldMap.title = 'Populations in China/Japan/Thailand'  # 世界地圖標題
worldMap.add('Asia',{'cn':1262645000,
                     'jp':126870000,
                     'th':63155029})                    # 標記人口資訊
worldMap.render_to_file('tmp_09.svg')                 # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

def getCountryCode(countryName):
    '''輸入國家名稱回傳國家代碼'''
    for dictCode, dictName in COUNTRIES.items():    # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode                         # 如果找到則回傳國家代碼
    return None                                     # 找不到則回傳None

fn = 'data/populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                     # 讀取人口數據json檔案

dictData = {}                                       # 定義地圖使用的字典
for getData in getDatas:
    if getData['Year'] == '2000':                   # 篩選2000年的數據
        countryName = getData['Country Name']       # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData['Numbers'])) # 人口數       
        if countryCode != None:
            dictData[countryCode] = population      # 代碼:人口數據加入字典

worldMap = pygal.maps.world.World()
worldMap.title = "World Population in 2000"
worldMap.add('Year 2000', dictData)
worldMap.render_to_file('tmp_10.svg')             # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

def getCountryCode(countryName):
    '''輸入國家名稱回傳國家代碼'''
    for dictCode, dictName in COUNTRIES.items():    # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode                         # 如果找到則回傳國家代碼
    return None                                     # 找不到則回傳None

fn = 'data/populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                     # 讀取人口數據json檔案

dictData = {}                                       # 定義地圖使用的字典
for getData in getDatas:
    if getData['Year'] == '2000':                   # 篩選2000年的數據
        countryName = getData['Country Name']       # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData['Numbers'])) # 人口數       
        if countryCode != None:
            dictData[countryCode] = population      # 代碼:人口數據加入字典

dict1, dict2 = {}, {}                               # 定義人口數分級的字典
for code, population in dictData.items():
    if population > 100000000:
        dict1[code] = population                    # 人口數大於1000000000
    else:
        dict2[code] = population                    # 人口數小於1000000000

worldMap = pygal.maps.world.World()
worldMap.title = "World Population in 2000"
worldMap.add('Over 1000000000', dict1)
worldMap.add('Under 1000000000', dict2)
worldMap.render_to_file('tmp_11.svg')             # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個



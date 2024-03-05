
#各種檔案寫讀範例 json

print('------------------------------------------------------------')	#60個

import sys
import json

print("------------------------------------------------------------")  # 60個

data = {
   "name": "Joe Chen", 
   "grade": 95, 
   "tel": "0933123456"   
}

json_str = json.dumps(data)
print(json_str)
data2 = json.loads(json_str)
print(data2)


jsonfile = "Student2.json"
with open(jsonfile, 'w') as fp:
    json.dump(data, fp)


animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
    "蛇": 16,
}

"""
jsonfile = "animal.json"
with open(jsonfile, 'w') as fp:
    json.dump(animals, fp)
"""

jsonfile = "animal.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp)
print(data)
json_str = json.dumps(data)
print(json_str)

print("------------------------------------------------------------")  # 60個

jsonfile = "Student.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp)
json_str = json.dumps(data)
print(json_str)  

print("------------------------------------------------------------")  # 60個

filename = 'data/populations.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

i = 0
filename = "_tmp_population.json"
tmpdict = {}
with open(filename, 'w') as fnObj:
    for getData in getDatas:
        if getData['Year'] == '2000':               # 篩選2000年的數據
            tmpdict["Country Name"] = getData['Country Name']
            tmpdict["Country Code"] = getData['Country Code']
            tmpdict["Year"] = getData['Year']
            tmpdict["Numbers"] = getData['Numbers']
            json.dump(tmpdict, fnObj)

print("------------------------------------------------------------")  # 60個

filename = 'data/aqi.json'

with open(filename) as fnObj:
    getDatas = json.load(fnObj)                         # 讀json檔案
print(getDatas)


for getData in getDatas:
    if getData['County'] == '臺北市':
        sitename = getData['SiteName']                  # 站台名稱
        siteid = getData['SiteId']                      # 站台ID
        pm25 = getData['PM2.5']                         # PM2.5值    
        print('站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
              (siteid, pm25, sitename))

print("------------------------------------------------------------")  # 60個

listNumbers = [5, 10, 20, 1]            # 串列資料
tupleNumbers = (1, 5, 10, 9)            # 元組資料
jsonData1 = json.dumps(listNumbers)     # 將串列資料轉成json資料
jsonData2 = json.dumps(tupleNumbers)    # 將串列資料轉成json資料
print("串列轉換成json的陣列", jsonData1)
print("元組轉換成json的陣列", jsonData2)
print("json陣列在Python的資料類型 ", type(jsonData1))

print("------------------------------------------------------------")  # 60個

listObj = [{'Name':'Peter', 'Age':25, 'Gender':'M'}]    # 串列元素是字典
jsonData = json.dumps(listObj)                          # 串列轉成json
print("串列轉換成json的陣列", jsonData)
print("json陣列在Python的資料類型 ", type(jsonData))

print("------------------------------------------------------------")  # 60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs',
          }
jsonObj1 = json.dumps(players)                  # 未用排序將字典轉成json
jsonObj2 = json.dumps(players, sort_keys=True)  # 有用排序將字典轉成json
print("未用排序將字典轉換成json的物件", jsonObj1)
print("使用排序將字典轉換成json的物件", jsonObj2)
print("有排序與未排序物件是否相同    ", jsonObj1 == jsonObj2 )
print("json物件在Python的資料類型 ", type(jsonObj1))

print("------------------------------------------------------------")  # 60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs',
          }
jsonObj = json.dumps(players, sort_keys=True, indent=4)   
print(jsonObj)

print("------------------------------------------------------------")  # 60個

jsonObj = '{"b":80, "a":25, "c":60}'    # json物件
dictObj = json.loads(jsonObj)           # 轉成Python物件
print(dictObj)
print(type(dictObj))

print("------------------------------------------------------------")  # 60個

obj = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])

print("------------------------------------------------------------")  # 60個

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

obj = {"Asia":\
        [{"Japan":"Tokyo"},\
         {"China":"Beijing"}]\
      }
filename = 'tmp_01.json'
with open(filename, 'w') as fnObj:
    json.dump(obj, fnObj)

print("------------------------------------------------------------")  # 60個

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

filename = 'tmp_02.json'
with open(filename, 'w') as fnObj:
    json.dump(objlist, fnObj)

print("------------------------------------------------------------")  # 60個

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

filename = 'tmp_03.json'
with open(filename, 'w') as fnObj:
    json.dump(objlist, fnObj, indent=2, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

filename = 'tmp_04.json'
with open(filename, 'w', encoding='utf-8') as fnObj:
    json.dump(objlist, fnObj, indent=2, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_04.json'
with open(filename, 'r', encoding='utf-8') as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))

print("------------------------------------------------------------")  # 60個

filename = 'data/populations.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

for getData in getDatas:
    if getData['Year'] == '2000':                   # 篩選2000年的數據
        countryName = getData['Country Name']       # 國家名稱
        countryCode = getData['Country Code']       # 國家代碼
        population = int(float(getData['Numbers'])) # 人口數據
        #print('國家代碼 =', countryCode,'國家名稱 =', countryName,'人口數 =', population)

print("------------------------------------------------------------")  # 60個

filename = 'data/aqi.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

for getData in getDatas:
    county = getData['County']                      # 城市名稱
    sitename = getData['SiteName']                  # 站台名稱
    siteid = getData['SiteId']                      # 站台ID
    pm25 = getData['PM2.5']                         # PM2.5值    
    #print('城市名稱 =%4s  站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' % (county, siteid, pm25, sitename))

print("------------------------------------------------------------")  # 60個

# 客戶數據管理
customer_data = [
    {"id":1, "name":"Tom", "email":"tom@example.com", "purchases":3},
    {"id":2, "name":"Bob", "email":"bob@example.com", "purchases":5}
]
with open('tmp_customers.json', 'w') as file:
    json.dump(customer_data, file)

# 庫存管理
inventory = {
    "products": [
        {"id":101, "name":"Laptop", "stock":40},
        {"id":102, "name":"Smartphone", "stock":100}
    ]
}
with open('tmp_inventory.json', 'w') as file:
    json.dump(inventory, file)

# 員工記錄
employees = [
    {"id":"E01", "name":"John Doe", "position":"Manager"},
    {"id":"E02", "name":"Jane Smith", "position":"Developer"}
]
with open('tmp_employees.json', 'w') as file:
    json.dump(employees, file)

# 銷售數據分析
sales_data = {
    "year": 2023,
    "sales": [
        {"month":"January", "total_sales":5000},
        {"month":"February", "total_sales":7000}
    ]
}
with open('tmp_sales_data.json', 'w') as file:
    json.dump(sales_data, file)

# 商業應用設定
config_settings = {
    "application":"Accounting Software",
    "version":"1.2.0",
    "features": {
        "auto_backup":True,
        "cloud_sync":True
    }
}
with open('tmp_config_settings.json', 'w') as file:
    json.dump(config_settings, file)

print("------------------------------------------------------------")  # 60個

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

print('------------------------------------------------------------')	#60個

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

print('------------------------------------------------------------')	#60個

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)

print("------------------------------------------------------------")  # 60個

import datetime

filename = 'C:/_git/vcs/_1.data/______test_files1/_json/data_earthquake.json'
fp = open(filename, 'r')
earthquakes = json.load(fp)

print("過去7天全球發生重大的地震資訊：")
for eq in earthquakes['features']:
    print("地點:{}".format(eq['properties']['place']))
    print("震度:{}".format(eq['properties']['mag']))
    et = float(eq['properties']['time']) /1000.0
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("時間:{}".format(d))


filename_json = 'C:/_git/vcs/_1.data/______test_files1/_json/ChinaBoundary_Province_City'
fp = open(filename_json, 'r', encoding ='UTF-8')
boundary_data = json.load(fp)
for b_data in boundary_data['Province']:
    print("ID:{}".format(b_data['ID']))
    print("code:{}".format(b_data['code']))
    print("name:{}".format(b_data['name']))


print('------------------------------------------------------------')	#60個

#抓取地震資料 用json拆解

import requests, datetime

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
html = requests.get(url)

earthquakes = json.loads(html.text)
dataset = list()
for eq in earthquakes['features']:
    item = dict()
    eptime = float(eq['properties']['time']) /1000.0
    d = datetime.datetime.fromtimestamp(eptime). \
        strftime('%Y-%m-%d %H:%M:%S')
    item['eqtime'] = d
    item['mag'] = eq['properties']['mag']
    item['place'] =  eq['properties']['place']
    dataset.append(item)
    #print(item)


for data in dataset:
        data = '(`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format(data['eqtime'], data['mag'], data['place'])
        #print(data)

print('------------------------------------------------------------')	#60個

import requests, hashlib, datetime, os.path

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
html = requests.get(url)
sig = hashlib.md5(html.text.encode('utf-8')).hexdigest()
old_sig=''

if os.path.exists('eq_sig.txt'):
    with open('eq_sig.txt', 'r') as fp:
        old_sig = fp.read()
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)
else:
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)

if sig == old_sig:
    print('資料未更新，不需要處理...')
    exit()

earthquakes = json.loads(html.text)
dataset = list()
for eq in earthquakes['features']:
    item = dict()
    eptime = float(eq['properties']['time']) /1000.0
    d = datetime.datetime.fromtimestamp(eptime). \
        strftime('%Y-%m-%d %H:%M:%S')
    item['eqtime'] = d
    item['mag'] = eq['properties']['mag']
    item['place'] =  eq['properties']['place']
    dataset.append(item)

for data in dataset:
    sql = 'insert into eq (`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format( \
           data['eqtime'], data['mag'], data['place'])
    #print(sql)
print('資料更新完成')


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_json/jdata.json'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_json/AQI1.json'  #fail

import pprint as pp

with open(filename, "rt") as fp:
    data = json.loads(fp.read())
pp.pprint(data)
print(data)

print('------------------------------------------------------------')	#60個

data = [
    {'姓名':'王小明', '身高':174, '體重':56},
    {'姓名':'林小華', '身高':185, '體重':80},
    {'姓名':'陳小強', '身高':168, '體重':60} ]

with open('p-data.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp)
print("done")

print("------------------------------------------------------------")  # 60個

#讀取 JSON 檔

from collections import defaultdict

def print_scores(filename):
    with open(filename) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)
 
        print('班級:', record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)
 
        for subject, scores in result.items():
            print('科目:', subject)
            print('\t最高分:', max(scores))
            print('\t最低分:', min(scores))
            print('\t平均:', sum(scores) / len(scores))

print_scores(r'.\data\score.json')

print('------------------------------------------------------------')	#60個

# 批次檔案讀取

import os, json
from collections import defaultdict

def print_scores(filename):
    with open(filename) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)
 
        print('班級:', record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)
 
        for subject, scores in result.items():
            print('科目:', subject)
            print('\t最高分:', max(scores))
            print('\t最低分:', min(scores))
            print('\t平均:', sum(scores) / len(scores))

def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith('.json'):
            print('讀取檔案: ', filename)
            print_scores(os.path.join(dirname, filename))

print_dir_scores(r'.\data\scores')

print('------------------------------------------------------------')	#60個


"""
json

filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)
"""



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day11\json1.py

"""
读取JSON数据

"""

import json

json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

# 请思考如何将下面JSON格式的天气数据转换成对象并获取我们需要的信息
# 稍后我们会讲解如何通过网络API获取我们需要的JSON格式的数据
"""
    {
        "wendu": "29",
        "ganmao": "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
        "forecast": [
            {
                "fengxiang": "南风",
                "fengli": "3-4级",
                "high": "高温 32℃",
                "type": "多云",
                "low": "低温 17℃",
                "date": "16日星期二"
            },
            {
                "fengxiang": "南风",
                "fengli": "微风级",
                "high": "高温 34℃",
                "type": "晴",
                "low": "低温 19℃",
                "date": "17日星期三"
            },
            {
                "fengxiang": "南风",
                "fengli": "微风级",
                "high": "高温 35℃",
                "type": "晴",
                "low": "低温 22℃",
                "date": "18日星期四"
            },
            {
                "fengxiang": "南风",
                "fengli": "微风级",
                "high": "高温 35℃",
                "type": "多云",
                "low": "低温 22℃",
                "date": "19日星期五"
            },
            {
                "fengxiang": "南风",
                "fengli": "3-4级",
                "high": "高温 34℃",
                "type": "晴",
                "low": "低温 21℃",
                "date": "20日星期六"
            }
        ],
        "yesterday": {
            "fl": "微风",
            "fx": "南风",
            "high": "高温 28℃",
            "type": "晴",
            "low": "低温 15℃",
            "date": "15日星期一"
        },
        "aqi": "72",
        "city": "北京"
    }
"""

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day11\json2.py

"""
写入JSON文件
"""

import json

teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


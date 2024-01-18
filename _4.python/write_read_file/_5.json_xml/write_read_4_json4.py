import sys

import json

listNumbers = [5, 10, 20, 1]            # 串列資料
tupleNumbers = (1, 5, 10, 9)            # 元組資料
jsonData1 = json.dumps(listNumbers)     # 將串列資料轉成json資料
jsonData2 = json.dumps(tupleNumbers)    # 將串列資料轉成json資料
print("串列轉換成json的陣列", jsonData1)
print("元組轉換成json的陣列", jsonData2)
print("json陣列在Python的資料類型 ", type(jsonData1))

print("------------------------------------------------------------")  # 60個

import json

listObj = [{'Name':'Peter', 'Age':25, 'Gender':'M'}]    # 串列元素是字典
jsonData = json.dumps(listObj)                          # 串列轉成json
print("串列轉換成json的陣列", jsonData)
print("json陣列在Python的資料類型 ", type(jsonData))

print("------------------------------------------------------------")  # 60個

import json

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

import json

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs',
          }
jsonObj = json.dumps(players, sort_keys=True, indent=4)   
print(jsonObj)

print("------------------------------------------------------------")  # 60個

import json

jsonObj = '{"b":80, "a":25, "c":60}'    # json物件
dictObj = json.loads(jsonObj)           # 轉成Python物件
print(dictObj)
print(type(dictObj))

print("------------------------------------------------------------")  # 60個

import json

obj = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])

print("------------------------------------------------------------")  # 60個

import json

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

import json

obj = {"Asia":\
        [{"Japan":"Tokyo"},\
         {"China":"Beijing"}]\
      }
filename = 'tmp_01.json'
with open(filename, 'w') as fnObj:
    json.dump(obj, fnObj)

print("------------------------------------------------------------")  # 60個

import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

filename = 'tmp_02.json'
with open(filename, 'w') as fnObj:
    json.dump(objlist, fnObj)

print("------------------------------------------------------------")  # 60個

import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

filename = 'tmp_03.json'
with open(filename, 'w') as fnObj:
    json.dump(objlist, fnObj, indent=2, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

filename = 'tmp_04.json'
with open(filename, 'w', encoding='utf-8') as fnObj:
    json.dump(objlist, fnObj, indent=2, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

import json
      
filename = 'tmp_04.json'
with open(filename, 'r', encoding='utf-8') as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))

print("------------------------------------------------------------")  # 60個

import json

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

import json

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

import json

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


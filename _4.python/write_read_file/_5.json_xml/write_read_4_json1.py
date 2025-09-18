"""
#各種檔案寫讀範例 json

json常用的方法(6)

.load()   # 讀取json檔案
.loads()  # json 轉 字典
.dump()   # 寫進json檔案
.dumps()  # 字典 轉 json
load  - 將文件中的JSON數據反序列化成對象
loads - 將字符串的內容反序列化成Python對象
dump  - 將Python對象按照JSON格式序列化到文件中
dumps - 將Python對象處理成JSON格式的字符串

JSONDecoder()
JSONEncoder()
"""

import os
import sys
import json
import datetime

print("------------------------------------------------------------")  # 60個
# 讀取專區

filename = "data/Student.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
print(datas)

json_str = json.dumps(datas)  # 字典 轉 json
print(json_str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/populations.json"
with open(filename) as fp:
    datas = json.load(fp)  # 讀取json檔案
    print("共有 :", len(datas), "筆資料")
    # print(datas)
    i = 0
    for data in datas:
        # print(data)  # 字典格式
        y = data["Year"]
        n = data["Country Name"]  # 國家名稱
        c = data["Country Code"]  # 國家代碼
        p = int(float(data["Numbers"]))  # 人口數
        print(y, "/", n, "/", c, "/", p)
        i += 1
        if i > 10:
            break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/aqi.json"
with open(filename) as fp:
    datas = json.load(fp)  # 讀取json檔案
    print("共有 :", len(datas), "筆資料")
    # print(datas)
    i = 0
    for data in datas:
        # print(data)  # 字典格式
        county = data["County"]  # 城市名稱
        sitename = data["SiteName"]  # 站台名稱
        siteid = data["SiteId"]  # 站台ID
        pm25 = data["PM2.5"]  # PM2.5值
        print(
            "城市名稱 =%4s  站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s "
            % (county, siteid, pm25, sitename)
        )
        i += 1
        if i > 10:
            break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/eq_data_1_day_m1.json"
with open(filename) as fp:
    datas = json.load(fp)  # 讀取json檔案
    print("共有 :", len(datas), "筆資料")
    # print(datas)
    for data in datas:
        print(data)

print("type :")
print(datas["type"])

print("features :")
print(datas["features"])
feature_data = datas["features"]
i = 0
for feature in feature_data:
    mag = feature["properties"]["mag"]
    lon = feature["geometry"]["coordinates"][0]
    lat = feature["geometry"]["coordinates"][1]
    print(mag, "/", lon, "/", lat)
    i += 1
    if i > 10:
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_1.data/______test_files1/_json/data_earthquake.json"
fp = open(filename, "r")
datas = json.load(fp)  # 讀取json檔案
print("共有 :", len(datas), "筆資料")

print("過去7天全球發生重大的地震資訊：")
for data in datas["features"]:
    print("地點:{}".format(data["properties"]["place"]))
    print("震度:{}".format(data["properties"]["mag"]))
    et = float(data["properties"]["time"]) / 1000.0
    d = datetime.datetime.fromtimestamp(et).strftime("%Y-%m-%d %H:%M:%S")
    print("時間:{}".format(d))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_json = (
    "D:/_git/vcs/_1.data/______test_files1/_json/ChinaBoundary_Province_City"
)
fp = open(filename_json, "r", encoding="UTF-8")
datas = json.load(fp)  # 讀取json檔案
print("共有 :", len(datas), "筆資料")
print(datas["ID"])
print(datas["code"])
print(datas["name"])
# print(datas['Province'])
print(datas["Province"][0]["ID"])
print(datas["Province"][0]["code"])
print(datas["Province"][0]["name"])
# print(datas['Province'][0]['rings'])
# print(datas['Province'][0]['City'])
print(datas["Province"][0]["City"][0]["code"])
print(datas["Province"][0]["City"][0]["name"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取一個JSON字典")

from difflib import get_close_matches

fp = open("data/WORD_DICTIONARY.json", "r")
datas = json.load(fp)  # 讀取json檔案
print("共有 :", len(datas), "筆資料")
# print(datas)

text = "XYZ"  # 找不到
text = "MoisTxure"  # 不完全相符
text = "MOISTURE"  # 全相符
text = "abiotic factor"  # 全相符

w = text.lower()
if w in datas:
    print("全相符")
    for i in range(len(datas[w])):
        axe = str(datas[w][i])
        print(axe)
        # text1.insert(END,w+" : "+axe+"\n")
        # speak(axe)
elif len(get_close_matches(w, datas.keys())) > 0:
    print("不完全相符, 最接近的字 %s " % get_close_matches(w, datas.keys())[0])
    for i in range(len(datas[get_close_matches(w, datas.keys())[0]])):
        print(
            str(get_close_matches(w, datas.keys())[0])
            + " : "
            + str(datas[get_close_matches(w, datas.keys())[0]][i])
            + "\n"
        )
else:
    print("找不到")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt  # 引用圖表使用套件

# 讀取109年9月臺中市10大易肇事路口.json資料並放入listTrafficEvent串列物件
fp = open("data/109年9月臺中市10大易肇事路口.json", "r", encoding="utf_8")
listTrafficEvent = json.load(fp)  # 讀取json檔案
fp.close()

# 將 listTrafficEvent 串列中的每筆字典物件印出來
for trafficEvent in listTrafficEvent:
    for key in trafficEvent:
        show = False
        # 若該筆字典的編號(key)有值(value)即印出
        if trafficEvent["編號"] != "":
            print("%s：%s" % (key, trafficEvent[key]))
            show = True
        else:
            break
    if show == True:
        print("=" * 30)

total = 0.0  # 統計肇事數量
listAllEvent = []  # listAllEvent用來存放車禍主要肇因
for trafficEvent in listTrafficEvent:
    if trafficEvent["編號"] != "":
        listAllEvent += [trafficEvent["主要肇因"]]
        total += 1

listEvent = []  # 存放所有車禍主要肇因，此串列存放不重複的車禍主要肇因
listCount = []  # 存放各主要肇因對應的車禍數量
for event in set(listAllEvent):  # 使用set()移除listAllEvent串列中重複的主要肇因
    print("主要肇因 %s 共 %s 件" % (event, listAllEvent.count(event)))
    listEvent += [event]
    listCount += [listAllEvent.count(event)]

# 計算各車禍主要肇因的百分比，並放入listPercent串列
listPercent = []
for c in listCount:
    listPercent.append(round((float(c) / total) * 100))

# 繪製車禍主要肇因的圓餅圖
font = {"family": "DFKai-SB"}
plt.rc("font", **font)
plt.pie(listPercent, labels=listEvent, autopct="%3.1f%%")
# plt.show()  # 顯示圓餅圖

print("圖表建置成成功")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 抓取地震資料 用json拆解

import requests

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
html = requests.get(url)

datas = json.loads(html.text)  # json 轉 字典
print("共有 :", len(datas), "筆資料")

dataset = list()

for data in datas["features"]:
    item = dict()
    eptime = float(data["properties"]["time"]) / 1000.0
    d = datetime.datetime.fromtimestamp(eptime).strftime("%Y-%m-%d %H:%M:%S")
    item["eqtime"] = d
    item["mag"] = data["properties"]["mag"]
    item["place"] = data["properties"]["place"]
    dataset.append(item)
    # print(item)

print("------------------------------")  # 30個

for data in dataset:
    data = '(`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format(
        data["eqtime"], data["mag"], data["place"]
    )
    # print(data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("串列 轉 json檔案")

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

filename = "tmp01_animals.json"
with open(filename, "w") as fp:
    json.dump(animals, fp)  # 寫進json檔案

print("------------------------------")  # 30個

print("json檔案 轉 串列")

filename = "tmp01_animals.json"
with open(filename) as fp:
    datas = json.load(fp)  # 讀取json檔案

print(type(datas))
print(datas)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("串列 轉 json")

# 串列
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
json_str = json.dumps(animals)  # 串列 轉 json
print("串列轉換成json的陣列", json_str)
print("json陣列在Python的資料類型 ", type(json_str))

print("元組 轉 json")

# 元組
tupleAnimals = ("鼠", "牛", "虎", "兔", "龍")
jsonData2 = json.dumps(tupleAnimals)  # 元組 轉 json  # 字典 轉 json
print("元組轉換成json的陣列", jsonData2)
print("json陣列在Python的資料類型 ", type(jsonData2))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
data = [
    {"姓名": "王小明", "身高": 174, "體重": 56},
    {"姓名": "林小華", "身高": 185, "體重": 80},
    {"姓名": "陳小強", "身高": 168, "體重": 60},
]

with open("tmp02_person.json", "w", encoding="utf-8") as fp:
    json.dump(data, fp)  # 寫進json檔案
print("done")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("字典 轉 json")

data = {"name": "Joe Chen", "score": 95, "tel": "0933123456"}
print(type(data))

json_str = json.dumps(data)  # 字典 轉 json
print(json_str)

data2 = json.loads(json_str)  # json 轉 字典
print(data2)

filename = "tmp03.json"
with open(filename, "w") as fp:
    json.dump(data, fp)  # 寫進json檔案

filename = "tmp03.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
listObj = [{"Name": "Peter", "Age": 25, "Gender": "M"}]  # 串列元素是字典
jsonData = json.dumps(listObj)  # 串列轉成json  # 字典 轉 json
print("串列轉換成json的陣列", jsonData)
print("json陣列在Python的資料類型 ", type(jsonData))

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
print(type(players))
jsonObj1 = json.dumps(players)  # 未用排序將字典轉成json  # 字典 轉 json
jsonObj2 = json.dumps(players, sort_keys=True)  # 有用排序將字典轉成json  # 字典 轉 json
print("未用排序將字典轉換成json的物件", jsonObj1)
print("使用排序將字典轉換成json的物件", jsonObj2)
print("有排序與未排序物件是否相同    ", jsonObj1 == jsonObj2)
print("json物件在Python的資料類型 ", type(jsonObj1))

jsonObj = json.dumps(players, sort_keys=True, indent=4)  # 字典 轉 json
print(jsonObj)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

jsonObj = '{"b":80, "a":25, "c":60}'  # json物件
dictObj = json.loads(jsonObj)  # json 轉 字典
print(dictObj)
print(type(dictObj))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 字串
obj = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'

json_obj = json.loads(obj)  # json 轉 字典
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 字典
obj = {"Asia": [{"Japan": "Tokyo"}, {"China": "Beijing"}]}

filename = "tmp06.json"
with open(filename, "w") as fp:
    json.dump(obj, fp)  # 寫進json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
objlist = [{"日本": "Japan", "首都": "Tokyo"}, {"美州": "USA", "首都": "Washington"}]

filename = "tmp07a.json"
with open(filename, "w") as fp:
    json.dump(objlist, fp)  # 寫進json檔案

filename = "tmp07b.json"
with open(filename, "w") as fp:
    json.dump(objlist, fp, indent=2, ensure_ascii=False)  # 寫進json檔案

filename = "tmp07c.json"
with open(filename, "w", encoding="utf-8") as fp:
    json.dump(objlist, fp, indent=2, ensure_ascii=False)  # 寫進json檔案

filename = "tmp07c.json"
with open(filename, "r", encoding="utf-8") as fp:
    datas = json.load(fp)  # 讀取json檔案

print(datas)
print(type(datas))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 客戶數據管理
# 串列, 元素是字典
customer_data = [
    {"id": 1, "name": "Tom", "email": "tom@example.com", "purchases": 3},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "purchases": 5},
]
with open("tmp11a_customers.json", "w") as fp:
    json.dump(customer_data, fp)  # 寫進json檔案

# 庫存管理
inventory = {
    "products": [
        {"id": 101, "name": "Laptop", "stock": 40},
        {"id": 102, "name": "Smartphone", "stock": 100},
    ]
}
with open("tmp11b_inventory.json", "w") as fp:
    json.dump(inventory, fp)  # 寫進json檔案

# 員工記錄
# 串列, 元素是字典
employees = [
    {"id": "E01", "name": "John Doe", "position": "Manager"},
    {"id": "E02", "name": "Jane Smith", "position": "Developer"},
]
with open("tmp11c_employees.json", "w") as fp:
    json.dump(employees, fp)  # 寫進json檔案

# 銷售數據分析
sales_data = {
    "year": 2023,
    "sales": [
        {"month": "January", "total_sales": 5000},
        {"month": "February", "total_sales": 7000},
    ],
}
with open("tmp11d_sales_data.json", "w") as fp:
    json.dump(sales_data, fp)  # 寫進json檔案

# 商業應用設定
config_settings = {
    "application": "Accounting Software",
    "version": "1.2.0",
    "features": {"auto_backup": True, "cloud_sync": True},
}
with open("tmp11e_config_settings.json", "w") as fp:
    json.dump(config_settings, fp)  # 寫進json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取 JSON 檔

from collections import defaultdict


def print_scores(filename):
    with open(filename) as fp:
        datas = json.load(fp)  # 讀取json檔案
        result = defaultdict(list)

        print("班級:", datas["class"])
        for data in datas["score"]:
            for subject, score in data.items():
                result[subject].append(score)

        for subject, scores in result.items():
            print("科目:", subject)
            print("\t最高分:", max(scores))
            print("\t最低分:", min(scores))
            print("\t平均:", sum(scores) / len(scores))


print_scores(r".\data\score.json")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 批次檔案讀取

from collections import defaultdict


def print_scores(filename):
    with open(filename) as fp:
        datas = json.load(fp)  # 讀取json檔案
        result = defaultdict(list)

        print("班級:", datas["class"])
        for data in datas["score"]:
            for subject, score in data.items():
                result[subject].append(score)

        for subject, scores in result.items():
            print("科目:", subject)
            print("\t最高分:", max(scores))
            print("\t最低分:", min(scores))
            print("\t平均:", sum(scores) / len(scores))


def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith(".json"):
            print("讀取檔案: ", filename)
            print_scores(os.path.join(dirname, filename))


print_dir_scores(r".\data\scores")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
filename = "tmp13.json"
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)  # 寫進json檔案
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

json_str = '{"name": "駱昊", "age": 38, "title": "叫獸"}'
result = json.loads(json_str)  # json 轉 字典
print(result)
print(type(result))
print(result["name"])
print(result["age"])

# 請思考如何將下面JSON格式的天氣數據轉換成對象并獲取我們需要的信息
# 稍后我們會講解如何通過網絡API獲取我們需要的JSON格式的數據
"""
    {
        "wendu": "29",
        "ganmao": "各項氣象條件適宜，發生感冒機率較低。但請避免長期處于空調房間中，以防感冒。",
        "forecast": [
            {
                "fengxiang": "南風",
                "fengli": "3-4級",
                "high": "高溫 32℃",
                "type": "多云",
                "low": "低溫 17℃",
                "date": "16日星期二"
            },
            {
                "fengxiang": "南風",
                "fengli": "微風級",
                "high": "高溫 34℃",
                "type": "晴",
                "low": "低溫 19℃",
                "date": "17日星期三"
            },
            {
                "fengxiang": "南風",
                "fengli": "微風級",
                "high": "高溫 35℃",
                "type": "晴",
                "low": "低溫 22℃",
                "date": "18日星期四"
            },
            {
                "fengxiang": "南風",
                "fengli": "微風級",
                "high": "高溫 35℃",
                "type": "多云",
                "low": "低溫 22℃",
                "date": "19日星期五"
            },
            {
                "fengxiang": "南風",
                "fengli": "3-4級",
                "high": "高溫 34℃",
                "type": "晴",
                "low": "低溫 21℃",
                "date": "20日星期六"
            }
        ],
        "yesterday": {
            "fl": "微風",
            "fx": "南風",
            "high": "高溫 28℃",
            "type": "晴",
            "low": "低溫 15℃",
            "date": "15日星期一"
        },
        "aqi": "72",
        "city": "北京"
    }
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
寫入JSON文件
"""
teacher_dict = {"name": "白元芳", "age": 25, "title": "講師"}
json_str = json.dumps(teacher_dict)  # 字典 轉 json
print(json_str)
print(type(json_str))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("串列 轉 json")

# 串列, 元素是字典
listProduct = [
    {"編號": "P01", "品名": "五香豆干", "單價": 89},
    {"編號": "P02", "品名": "龍哥可樂", "單價": 20},
    {"編號": "P03", "品名": "阿才紅茶", "單價": 15},
]
fp = open("tmp14_product.json", "w", encoding="utf_8")
json.dump(listProduct, fp, ensure_ascii=False, indent=4)  # 寫進json檔案
fp.close()
print("JSON產品資料存檔成功")

print("------------------------------")  # 30個

# 串列
listScore = [89, 100, 23, 78, 89]
print("listScore串列：", listScore)
print("listScore型別：", type(listScore))

jsonScore = json.dumps(listScore)  # 字典 轉 json
print("jsonScore字串：", jsonScore)
print("jsonScore型別：", type(jsonScore))

dictEmp = {"編號": "P01", "品名": "五香豆干", "單價": 89}
print("dictEmp字典：", dictEmp)
print("dictEmp型別：", type(dictEmp))

jsonEmp = json.dumps(dictEmp, ensure_ascii=False)  # 字典 轉 json
print("jsonEmp字串：", jsonEmp)
print("jsonEmp型別：", type(jsonEmp))

print("------------------------------")  # 30個

fruit = {"banana": "香蕉", "papaya": "木瓜", "apple": "蘋果"}
print(json.dumps(fruit, ensure_ascii=False))  # 字典 轉 json
print(json.dumps(fruit, ensure_ascii=False, sort_keys=True))  # 字典 轉 json
print(json.dumps(fruit, ensure_ascii=False, sort_keys=True, indent=4))  # 字典 轉 json

print("------------------------------")  # 30個

fp = open("tmp14_product.json", "r", encoding="utf_8")
datas = json.load(fp)  # 讀取json檔案
fp.close()

print("====== DTC商店 ======")
for product in datas:
    for key in product:
        print(key, "：", product[key])
    print("=" * 20)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

jsonStr = """
{"編號":"E01","姓名": "王小明",
"性別": true, "電話":["0912345678","0978123321"]}
"""
print("jsonStr字串：", jsonStr)
print("jsonStr型別：", type(jsonStr))
print()

pObj = json.loads(jsonStr)  # json 轉 字典
print("pObj物件：", pObj)
print("pObj型別：", type(pObj))
for key in pObj:
    print(key, ":", pObj[key], " value的型別：", type(pObj[key]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 新增員工記錄函式
def fnCreate():
    uid = input("編號：")
    if uid in listUid:
        print("編號重複，無法在記憶體中新增員工記錄")
        return
    name = input("姓名︰")
    salary = int(input("薪資︰"))
    newMember = {"編號": uid, "姓名": name, "薪資": salary}
    listMember.append(newMember)
    listUid.append(uid)
    print("記憶體新增編號 %s 的員工記錄" % (uid))


# 修改員工記錄函式
def fnUpdate():
    uid = input("編號：")
    for member in listMember:
        if member["編號"] == uid:
            name = input("姓名︰")
            salary = int(input("薪資︰"))
            newMember = {"編號": uid, "姓名": name, "薪資": salary}
            cIndex = listMember.index(member)
            listMember[cIndex] = newMember
            print("記憶體修改編號 %s 的員工記錄" % (uid))
            break
    else:
        print("查無編號，無法修改記憶體中的員工記錄")


# 刪除員工記錄函式
def fnDelete():
    uid = input("編號：")
    for member in listMember:
        if member["編號"] == uid:
            listMember.remove(member)
            listUid.remove(uid)
            print("記憶體刪除編號 %s 的員工記錄" % (uid))
            break
    else:
        print("查無編號，無法刪除記憶體中的員工記錄")


# 顯示員工記錄函式
def fnPrintMember():
    if len(listMember) == 0:
        print("記憶體中目前無員工記錄")
        return
    for member in listMember:
        for key in member:
            print(member[key], end="\t")
        print()


# 員工記錄儲存至MemberInfo.json的函式
def fnSaveJSONFile():
    fp = open(filename, "w", encoding="utf_8")
    json.dump(listMember, fp, ensure_ascii=False, indent=4)  # 寫進json檔案
    fp.close()
    print("記憶體中的員工記錄成功儲存至 %s 檔案" % (filename))


filename = "MemberInfo.json"

# 串列
listMember = []
listUid = []
if os.path.exists(filename):
    fp = open("MemberInfo.json", "r", encoding="utf_8")
    listMember = json.load(fp)  # 讀取json檔案
    listUid = []
    for member in listMember:
        listUid.append(member["編號"])
    fp.close()

"""
# 主程式
print("======= DTC員工管理系統 =======")
while True:
   option=int(input('系統功能->1.新增 2.修改 3.刪除 4.查詢 5.儲存JSON檔案 其他.離開：'))
   if option==1:
       fnCreate()
   elif option==2:
       fnUpdate()
   elif option==3:
       fnDelete()
   elif option==4:
       fnPrintMember()
   elif option==5:
       fnSaveJSONFile()
   else:
       print("離開系統")
       break;
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dictMeal = {"編號": "A", "品名": "雙人分享餐", "單價": 120}
jsonStr = json.dumps(dictMeal, ensure_ascii=False, indent=4)  # 字典 轉 json
print(jsonStr)

print("------------------------------------------------------------")  # 60個

jsonStr = '{"編號":"A", "品名":"雙人分享餐", "單價":120}'
dictMeal = json.loads(jsonStr)  # json 轉 字典

print("編號：%s" % (dictMeal["編號"]))
print("品名：%s" % (dictMeal["品名"]))
print("單價：%d" % (dictMeal["單價"]))

print("------------------------------------------------------------")  # 60個

jsonStr = """
    [    
        {"編號": "A","品名": "雙人分享餐","單價": 120},
        {"編號": "B","品名": "歡樂全家餐","單價": 399},
        {"編號": "C","品名": "情人精緻餐","單價": 540}
    ]
"""

listMeal = json.loads(jsonStr)  # json 轉 字典

for meal in listMeal:
    print("編號：%s" % (meal["編號"]))
    print("品名：%s" % (meal["品名"]))
    print("單價：%d" % (meal["單價"]))
    print("=" * 20)

for meal in listMeal:
    for key in meal:
        print("%s：%s" % (key, meal[key]))
    print("=" * 20)

print("------------------------------------------------------------")  # 60個

listMeal = [
    {"編號": "A", "品名": "雙人分享餐", "單價": 120},
    {"編號": "B", "品名": "歡樂全家餐", "單價": 399},
    {"編號": "C", "品名": "情人精緻餐", "單價": 540},
]

fp = open("tmp15_meal.json", "w", encoding="utf_8")

json.dump(listMeal, fp, ensure_ascii=False, indent=4)  # 寫進json檔案
fp.close()
print("JSON餐點記錄建置完成")

print("------------------------------")  # 30個

fp = open("tmp15_meal.json", "r", encoding="utf_8")
listMeal = json.load(fp)  # 讀取json檔案
fp.close()

for meal in listMeal:
    for key in meal:
        print("%s：%s" % (key, meal[key]))
    print("折扣：%.2f" % (float(meal[key]) * 0.9))
    print("=" * 20)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
data = [
    {"group": 0, "param": ["one", "two", "three"]},
    {"group": 1, "param": ["1", "2", "3"]},
]

jsonstr = json.dumps(data)  # 字典 轉 json
print(jsonstr)

jsonstr = json.dumps(
    data, sort_keys=True, indent=4, separators=(",", ": ")
)  # 字典 轉 json
print(jsonstr)

data1 = json.loads(jsonstr)  # json 轉 字典
print(data1, type(data1))

with open("tmp17.txt", "w") as fp:
    json.dump(data, fp)  # 寫進json檔案
    fp.close()

with open("tmp17.txt", "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
    fp.close()

print(datas, type(datas))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "tmp18.json"

with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
print(datas)

key = "aaa"
datas[key] = "AAAA"
with open(filename, "w") as fp:
    json.dump(datas, fp)  # 寫進json檔案

key = "bbb"
datas[key] = "BBBB"
with open(filename, "w") as fp:
    json.dump(datas, fp)  # 寫進json檔案

key = "ccc"
datas[key] = "CCCC"
with open(filename, "w") as fp:
    json.dump(datas, fp)  # 寫進json檔案

print("存了3筆資料")

print("讀取資料")
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
print(datas)

key = "bbb"
print(datas[key])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# json file
data = """{
"items":
{
"item":
[
{
"id": "0001",
"type": "donut",
"name": "Cake",
"ppu": 0.55,
"batters":
{
"batter":
[
{ "id": "1001", "type": "Regular" },
{ "id": "1002", "type": "Chocolate" },
{ "id": "1003", "type": "Blueberry" },
{ "id": "1004", "type": "Devil's Food" }
]
},
"topping":
[
{ "id": "5001", "type": "None" },
{ "id": "5002", "type": "Glazed" },
{ "id": "5005", "type": "Sugar" },
{ "id": "5007", "type": "Powdered Sugar" },
{ "id": "5006", "type": "Chocolate with Sprinkles" },
{ "id": "5003", "type": "Chocolate" },
{ "id": "5004", "type": "Maple" }
]
}
]
}
}"""

print(type(data))
# load JSON data into a dict
print("str 轉 json, str 變 dict")
data_dict = json.loads(data)  # json 轉 字典

# verify dict class
print(type(data_dict))
print()

# print the loaded data_dict
print(data_dict)
print()

# verify list class
print(type(data_dict["items"]["item"]))
print()

# print list
print(data_dict["items"]["item"])
print()

# print first item in the list
print(data_dict["items"]["item"][0])
print()

# print length of this list
print(len(data_dict["items"]["item"]))
print()

# access word 'Maple'
print(data_dict["items"]["item"][0]["topping"][6]["type"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests

url = "https://fchart.github.io/json/GoogleBooks.json"
filename = "tmp20_Books.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)  # json 轉 字典
with open(filename, "w") as fp:
    json.dump(json_data, fp)  # 寫進json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

# 3030
print("------------------------------")  # 30個


import hashlib

sig = hashlib.md5(html.text.encode("utf-8")).hexdigest()


import pprint as pp

# data = xxxx json格式

pp.pprint(data)
# print(data)

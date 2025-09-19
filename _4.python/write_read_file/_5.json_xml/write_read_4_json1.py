"""
#各種檔案寫讀範例 json

json常用的方法(6)

.load()   # 讀取json檔案
.loads()  # json轉字典
.dump()   # 寫進json檔案
.dumps()  # 字典轉json
load  - 將文件中的JSON數據反序列化成對象
loads - 將字符串的內容反序列化成Python對象
dump  - 將Python對象按照JSON格式序列化到文件中
dumps - 將Python對象處理成JSON格式的字符串

JSONDecoder()
JSONEncoder()


json為字串格式
json = json字串 = json_str

"""

import os
import sys
import json
import requests
import datetime
import pandas as pd

print("------------------------------------------------------------")  # 60個
print("格式轉換1, 串列轉json/json檔案")
print("------------------------------------------------------------")  # 60個

# 串列
data_list = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

# 串列, 元素是字典
data_list = [{"Name": "Peter", "Age": 25, "Gender": "M"}]  # 串列元素是字典

json_str = json.dumps(data_list)  # 串列轉json
print("串列 :", data_list)
print("串列轉json :", json_str)
print("json的資料類型 :", type(json_str))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("格式轉換2, 字典轉json/json檔案")
print("------------------------------------------------------------")  # 60個

print("字典轉json")

data_dict = {"name": "Joe Chen", "score": 95, "tel": "0933123456"}
print(type(data_dict))

json_str = json.dumps(data_dict)  # 字典轉json
print(json_str)

data2 = json.loads(json_str)  # json轉字典
print(data2)

filename = "tmp03.json"
with open(filename, "w") as fp:
    print(type(data_dict))
    json.dump(data_dict, fp)  # 寫進json檔案, 字典轉json檔案

filename = "tmp03.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
    print(type(datas))
    print(datas)

print("------------------------------------------------------------")  # 60個

# json字串
json_str = '{"name": "駱昊", "age": 38, "title": "叫獸"}'  # json字串

data_dict = json.loads(json_str)  # json轉字典
print(data_dict)
print(type(data_dict))
print(data_dict["name"])
print(data_dict["age"])

print("------------------------------------------------------------")  # 60個

# json字串
json_str = '{"b":80, "a":25, "c":60}'  # json字串

data_dict = json.loads(json_str)  # json轉字典
print(data_dict)
print(type(data_dict))

print("------------------------------------------------------------")  # 60個

# json字串
json_str = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'  # json字串

data_dict = json.loads(json_str)  # json轉字典
print(data_dict)
print(type(data_dict))
print(data_dict["Asia"])
print(data_dict["Asia"][0])
print(data_dict["Asia"][1])
print(data_dict["Asia"][0]["Japan"])
print(data_dict["Asia"][1]["China"])

print("------------------------------------------------------------")  # 60個

# json字串
json_str = """
{"編號":"E01","姓名": "王小明",
"性別": true, "電話":["0912345678","0978123321"]}
"""
print("jsonStr字串：", json_str)
print("jsonStr型別：", type(json_str))

data_dict = json.loads(json_str)  # json轉字典
print("data_dict物件：", data_dict)
print("data_dict型別：", type(data_dict))
for key in data_dict:
    print(key, ":", data_dict[key], " value的型別：", type(data_dict[key]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("字典轉json檔案")

# 字典
data_dict = {"Asia": [{"Japan": "Tokyo"}, {"China": "Beijing"}]}
print(type(data_dict))

filename = "tmp06.json"
with open(filename, "w") as fp:
    print(type(data_dict))
    json.dump(data_dict, fp)  # 寫進json檔案, 字典轉json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("格式轉換3, 元組轉json")
print("------------------------------------------------------------")  # 60個

# 元組
data_tuple = ("鼠", "牛", "虎", "兔", "龍")  # 元組
json_str = json.dumps(data_tuple)  # 元組轉json
print("元組轉json :", json_str)
print("json的資料類型 :", type(json_str))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("串列轉json檔案")

data_list = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

filename = "tmp01_animals.json"
with open(filename, "w") as fp:
    print(type(data_list))
    json.dump(data_list, fp)  # 寫進json檔案, 串列轉json檔案

print("------------------------------")  # 30個

print("json檔案轉串列")

filename = "tmp01_animals.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
    print(type(datas))
    print(datas)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
data_list = [
    {"姓名": "王小明", "身高": 174, "體重": 56},
    {"姓名": "林小華", "身高": 185, "體重": 80},
    {"姓名": "陳小強", "身高": 168, "體重": 60},
]

filename = "tmp02_person.json"
with open(filename, "w", encoding="utf-8") as fp:
    print(type(data_list))
    json.dump(data_list, fp)  # 寫進json檔案, 串列轉json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
data_list = [
    {"group": 0, "param": ["one", "two", "three"]},
    {"group": 1, "param": ["1", "2", "3"]},
]
print(type(data_list))
json_str = json.dumps(data_list)  # 串列轉json
print(json_str)

json_str = json.dumps(
    data_list, sort_keys=True, indent=4, separators=(",", ": ")
)  # 串列轉json
print(json_str)

data1 = json.loads(json_str)  # json轉串列
print(data1)
print(type(data1))

filename = "tmp17.json"
with open(filename, "w") as fp:
    print(type(data_list))
    json.dump(data_list, fp)  # 寫進json檔案, 串列轉json檔案
    fp.close()

filename = "tmp17.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
    print(type(datas))
    print(datas)

print(datas)
print(type(datas))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
print(type(players))
json_str1 = json.dumps(players)  # 未用排序將字典轉json  # 字典轉json
json_str2 = json.dumps(players, sort_keys=True)  # 有用排序將字典轉json  # 字典轉json
print("未用排序將字典轉換成json的物件", json_str1)
print("使用排序將字典轉換成json的物件", json_str2)
print("有排序與未排序物件是否相同    ", json_str1 == json_str2)
print("json物件在Python的資料類型 ", type(json_str1))

json_str = json.dumps(players, sort_keys=True, indent=4)  # 字典轉json
print(json_str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 串列, 元素是字典
objlist = [{"日本": "Japan", "首都": "Tokyo"}, {"美州": "USA", "首都": "Washington"}]

filename = "tmp07a.json"
with open(filename, "w") as fp:
    print(type(objlist))
    json.dump(objlist, fp)  # 寫進json檔案, 串列轉json檔案

filename = "tmp07b.json"
with open(filename, "w") as fp:
    print(type(objlist))
    json.dump(objlist, fp, indent=2, ensure_ascii=False)  # 寫進json檔案, 串列轉json檔案

filename = "tmp07c.json"
with open(filename, "w", encoding="utf-8") as fp:
    print(type(objlist))
    json.dump(objlist, fp, indent=2, ensure_ascii=False)  # 寫進json檔案, 串列轉json檔案

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

filename = "tmp11a_customers.json"
with open(filename, "w") as fp:
    print(type(customer_data))
    json.dump(customer_data, fp)  # 寫進json檔案, 串列轉json檔案

# 庫存管理
inventory = {
    "products": [
        {"id": 101, "name": "Laptop", "stock": 40},
        {"id": 102, "name": "Smartphone", "stock": 100},
    ]
}

filename = "tmp11b_inventory.json"
with open(filename, "w") as fp:
    print(type(inventory))
    json.dump(inventory, fp)  # 寫進json檔案, 字典轉json檔案

# 員工記錄
# 串列, 元素是字典
employees = [
    {"id": "E01", "name": "John Doe", "position": "Manager"},
    {"id": "E02", "name": "Jane Smith", "position": "Developer"},
]

filename = "tmp11c_employees.json"
with open(filename, "w") as fp:
    print(type(employees))
    json.dump(employees, fp)  # 寫進json檔案, 串列轉json檔案

# 銷售數據分析
sales_data = {
    "year": 2023,
    "sales": [
        {"month": "January", "total_sales": 5000},
        {"month": "February", "total_sales": 7000},
    ],
}
filename = "tmp11d_sales_data.json"
with open(filename, "w") as fp:
    print(type(sales_data))
    json.dump(sales_data, fp)  # 寫進json檔案, 字典轉json檔案

# 商業應用設定
config_settings = {
    "application": "Accounting Software",
    "version": "1.2.0",
    "features": {"auto_backup": True, "cloud_sync": True},
}
filename = "tmp11e_config_settings.json"
with open(filename, "w") as fp:
    print(type(config_settings))
    json.dump(config_settings, fp)  # 寫進json檔案, 字典轉json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
json_str = json.dumps(teacher_dict)  # 字典轉json
print(json_str)
print(type(json_str))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("串列轉json檔案")

# 串列, 元素是字典
listProduct = [
    {"編號": "P01", "品名": "五香豆干", "單價": 89},
    {"編號": "P02", "品名": "龍哥可樂", "單價": 20},
    {"編號": "P03", "品名": "阿才紅茶", "單價": 15},
]

filename = "tmp14_product.json"
with open(filename, "w", encoding="utf_8") as fp:
    print(type(listProduct))
    json.dump(listProduct, fp, ensure_ascii=False, indent=4)  # 寫進json檔案, 串列轉json檔案
    fp.close()
    print("JSON產品資料存檔成功")

print("------------------------------")  # 30個

# 串列
listScore = [89, 100, 23, 78, 89]
print("listScore串列：", listScore)
print("listScore型別：", type(listScore))

jsonScore = json.dumps(listScore)  # 字典轉json
print("jsonScore字串：", jsonScore)
print("jsonScore型別：", type(jsonScore))

dictEmp = {"編號": "P01", "品名": "五香豆干", "單價": 89}
print("dictEmp字典：", dictEmp)
print("dictEmp型別：", type(dictEmp))

jsonEmp = json.dumps(dictEmp, ensure_ascii=False)  # 字典轉json
print("jsonEmp字串：", jsonEmp)
print("jsonEmp型別：", type(jsonEmp))

print("------------------------------")  # 30個

fruit = {"banana": "香蕉", "papaya": "木瓜", "apple": "蘋果"}
print(json.dumps(fruit, ensure_ascii=False))  # 字典轉json
print(json.dumps(fruit, ensure_ascii=False, sort_keys=True))  # 字典轉json
print(json.dumps(fruit, ensure_ascii=False, sort_keys=True, indent=4))  # 字典轉json

print("------------------------------")  # 30個

filename = "tmp14_product.json"
with open(filename, "r", encoding="utf_8") as fp:
    datas = json.load(fp)  # 讀取json檔案
    fp.close()

print("====== DTC商店 ======")
for product in datas:
    for key in product:
        print(key, "：", product[key])
    print("=" * 20)

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
    with open(filename, "w", encoding="utf_8") as fp:
        print(type(listMember))
        json.dump(listMember, fp, ensure_ascii=False, indent=4)  # 寫進json檔案
        fp.close()
        print("記憶體中的員工記錄成功儲存至 %s 檔案" % (filename))


filename = "MemberInfo.json"

# 串列
listMember = []
listUid = []
if os.path.exists(filename):
    filename = "MemberInfo.json"
    with open(filename, "r", encoding="utf_8") as fp:
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
json_str = json.dumps(dictMeal, ensure_ascii=False, indent=4)  # 字典轉json
print(json_str)

print("------------------------------------------------------------")  # 60個

# json字串
json_str = '{"編號":"A", "品名":"雙人分享餐", "單價":120}'
dictMeal = json.loads(json_str)  # json轉字典

print("編號：%s" % (dictMeal["編號"]))
print("品名：%s" % (dictMeal["品名"]))
print("單價：%d" % (dictMeal["單價"]))

print("------------------------------------------------------------")  # 60個

# json字串
json_str = """
    [    
        {"編號": "A","品名": "雙人分享餐","單價": 120},
        {"編號": "B","品名": "歡樂全家餐","單價": 399},
        {"編號": "C","品名": "情人精緻餐","單價": 540}
    ]
"""
print(type(json_str))

data_list = json.loads(json_str)  # json轉串列
print(type(data_list))

for meal in data_list:
    print("編號：%s" % (meal["編號"]))
    print("品名：%s" % (meal["品名"]))
    print("單價：%d" % (meal["單價"]))
    print("=" * 20)

for meal in data_list:
    for key in meal:
        print("%s：%s" % (key, meal[key]))
    print("=" * 20)

print("------------------------------------------------------------")  # 60個

data_list = [
    {"編號": "A", "品名": "雙人分享餐", "單價": 120},
    {"編號": "B", "品名": "歡樂全家餐", "單價": 399},
    {"編號": "C", "品名": "情人精緻餐", "單價": 540},
]

filename = "tmp15_meal.json"
with open(filename, "w", encoding="utf_8") as fp:
    print(type(data_list))
    json.dump(data_list, fp, ensure_ascii=False, indent=4)  # 寫進json檔案, 串列轉json檔案
    print("JSON餐點記錄建置完成")

print("------------------------------")  # 30個

filename = "tmp15_meal.json"
with open(filename, "r", encoding="utf_8") as fp:
    data_list = json.load(fp)  # 讀取json檔案

for meal in data_list:
    for key in meal:
        print("%s：%s" % (key, meal[key]))
    print("折扣：%.2f" % (float(meal[key]) * 0.9))
    print("=" * 20)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
filename = "tmp18.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
print(datas)

key = "aaa"
datas[key] = "AAAA"
with open(filename, "w") as fp:
    print(type(datas))
    json.dump(datas, fp)  # 寫進json檔案

key = "bbb"
datas[key] = "BBBB"
with open(filename, "w") as fp:
    print(type(datas))
    json.dump(datas, fp)  # 寫進json檔案

key = "ccc"
datas[key] = "CCCC"
with open(filename, "w") as fp:
    print(type(datas))
    json.dump(datas, fp)  # 寫進json檔案

print("存了3筆資料")

print("讀取資料")
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
print(datas)

key = "bbb"
print(datas[key])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# json字串
json_str = """{
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

print(type(json_str))

print("json轉字典")
data_dict = json.loads(json_str)  # json轉字典
print(type(data_dict))
print(data_dict)
print()

print("看字典內容")
print(type(data_dict["items"]["item"]))
print()

print(data_dict["items"]["item"])
print()

print(data_dict["items"]["item"][0])
print()

print(len(data_dict["items"]["item"]))
print()

print(data_dict["items"]["item"][0]["topping"][6]["type"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/json/GoogleBooks.json"
filename = "tmp20_Books.json"
r = requests.get(url)
r.encoding = "utf8"
data_dict = json.loads(r.text)  # json轉字典
with open(filename, "w") as fp:
    print(type(data_dict))
    json.dump(data_dict, fp)  # 寫進json檔案, 字典轉json檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取專區

filename = "data/Student.json"
with open(filename, "r") as fp:
    datas = json.load(fp)  # 讀取json檔案
    print(type(datas))
    print(datas)

json_str = json.dumps(datas)  # 字典轉json
print(json_str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/populations.json"
with open(filename, "r") as fp:
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
with open(filename, "r") as fp:
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
with open(filename, "r") as fp:
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
with open(filename, "r") as fp:
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

filename = "D:/_git/vcs/_1.data/______test_files1/_json/ChinaBoundary_Province_City"

with open(filename, "r", encoding="utf-8") as fp:
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

filename = "data/WORD_DICTIONARY.json"
with open(filename, "r") as fp:
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

import matplotlib.pyplot as plt

# 讀取109年9月臺中市10大易肇事路口.json資料並放入listTrafficEvent串列物件

filename = "data/109年9月臺中市10大易肇事路口.json"
with open(filename, "r", encoding="utf_8") as fp:
    listTrafficEvent = json.load(fp)  # 讀取json檔案

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

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
html = requests.get(url)

datas = json.loads(html.text)  # json轉字典
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

"""
#import ast

data = dict()
with open('data\password.txt','r', encoding = 'UTF-8-sig') as fp:
   filedata = fp.read()
   print(filedata)
#   filedata = filedata.replace("\'", "\"")
#   data = ast.literal_eval(filedata)
   data = json.loads(filedata)

print(type(data),data)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from collections import defaultdict


def print_scores(filename):
    with open(filename, "r") as fp:
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


# 讀取 JSON 檔
print_scores(r".\data\score.json")


def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith(".json"):
            print("讀取檔案: ", filename)
            print_scores(os.path.join(dirname, filename))


# 批次檔案讀取
print_dir_scores(r".\data\scores")


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

import pprint as pp

# data = xxxx json格式

pp.pprint(data)
# print(data)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
response = requests.post(xxxx)
result = response.json()
print(result[0]['translations'][0]['text'])
print(result)	#列印結果
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# json轉dict

from urllib.request import urlopen
from html.entities import html5

entities_url = "http://dev.w3.org/html5/spec/entities.json"


def get_json(url):
    # Download the json file from the url and returns a decoded object.
    with urlopen(url) as fp:
        data = fp.read().decode("utf-8")
    return json.loads(data)


def create_dict(entities):
    # Create the html5 dict from the decoded json object.
    new_html5 = {}
    for name, value in entities.items():
        new_html5[name.lstrip("&")] = value["characters"]
    return new_html5


new_html5 = create_dict(get_json(entities_url))


print("------------------------------------------------------------")  # 60個
"""
postid = "237123381"
url = "https://www.dcard.tw/service/api/v2/posts/" + postid
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 查看有哪些欄位
print(data.keys())
# 因為只有一欄，而且沒有欄位名稱
# 否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data, orient="index")
# 查看有哪些內容
print(df)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
postid = "237123381"
url = "https://www.dcard.tw/service/api/v2/posts/" + postid
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 因為只有一欄，而且沒有欄位名稱
# 否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data, orient="index")
# 取出title、content內容
print(">>>>>文章標題")
print(df.loc["title", 0])
print()
print(">>>>>原Po文章")
print(str(df.loc["content", 0]).strip())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from datetime import datetime

postid = "237123381"
url = "https://www.dcard.tw/service/api/v2/posts/" + postid
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 因為只有一欄，而且沒有欄位名稱
# 否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data, orient="index")
# 取出title、content內容
print(">>>>>文章標題")
print(df[0]["title"])
print()
print(">>>>>原Po文章\n")
print(str(df[0]["content"]).strip())
url = "https://www.dcard.tw/service/api/v2/posts/" + postid + "/comments?popular=True"
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 因為有欄位名稱
# 只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
# 取出前3筆資料
for i in range(3):
    print("*******熱門留言" + str(i) + ":")
    print(df.loc[i, "content"])
    # 將最後修改文字日期轉換成日期
    updatedate = datetime.fromisoformat(str(df.loc[i, "updatedAt"]).replace("Z", ""))
    # 計算現在和最後修改日期的時間差
    datediff = datetime.today() - updatedate
    # 顯示幾天前有最新留言
    print(datediff.days, "天前")
    print()
# 若要查看有哪些欄位
print((df.keys()))
# 也可以透過df.info()查看
df.info()
# 也可以直接看前幾列
df.head(3)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from datetime import datetime

postid = "237123381"
url = "https://www.dcard.tw/service/api/v2/posts/" + postid
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 因為只有一欄，而且沒有欄位名稱
# 否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data, orient="index")
# 取出title、content內容
print(">>>>>文章標題")
print(df[0]["title"])
print()
print(">>>>>原Po文章\n")
print(str(df[0]["content"]).strip())
url = "https://www.dcard.tw/service/api/v2/posts/" + postid + "/comments"
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 因為有欄位名稱
# 只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
# 除了updatedAt, content, likeCount三個欄位以外，全部刪除
# 刪除欄依定要指定axis=1
# inplace=True真實刪除
df.drop(
    [
        "id",
        "anonymous",
        "postId",
        "createdAt",
        "floor",
        "withNickname",
        "hiddenByAuthor",
        "meta",
        "gender",
        "school",
        "host",
        "reportReason",
        "mediaMeta",
        "hidden",
        "inReview",
        "reportReasonText",
        "isSuspiciousAccount",
        "isModerator",
        "doorplate",
        "edited",
        "postAvatar",
        "activityAvatar",
        "verifiedBadge",
        "memberType",
        "enablePrivateMessage",
        "department",
    ],
    inplace=True,
    axis=1,
)
# 依據likeCout內容排序，以降序排列
df.sort_values(by="likeCount", inplace=True, ascending=False)
# 要記得重設index，這樣df.loc[]的結果才會正確
df = df.reset_index(drop=True)
# 取出前3筆資料
for i in range(3):
    print("*******熱門留言" + str(i) + ":")
    print(df.loc[i, "content"])
    # 將最後修改文字日期轉換成日期
    updatedate = datetime.fromisoformat(str(df.loc[i, "updatedAt"]).replace("Z", ""))
    # 計算現在和最後修改日期的時間差
    datediff = datetime.today() - updatedate
    # 顯示幾天前有最新留言
    print(datediff.days, "天前")
    print()
# 若要查看有哪些欄位
print((df.keys()))
# 也可以透過df.info()查看
df.info()
# 也可以直接看前幾列
df.head(3)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json"
res = requests.get(url)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
# 因為有欄位名稱
# 只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
# 轉換'確定病例數'欄位內容為整數(以利後面加總)
df["確定病例數"] = df["確定病例數"].astype(int)

startdate = "2021/07/20"
# startdate=input("請輸日期(yyyy/mm/dd)")
# 只保留個案研判日、是否為境外移入、確定病例數 三個欄位
df.drop(["確定病名", "縣市", "鄉鎮", "性別", "年齡層"], inplace=True, axis=1)
# 設定過濾條件(累積)
indexNames = df[df["個案研判日"] > startdate].index
# 刪除所有大於指定日期的個案
df.drop(indexNames, inplace=True)
# 計算累積確診人數
total = df.sum()["確定病例數"]
print("累積確診人數:", total)
# 設定過濾條件(今日)
indexNames = df[df["個案研判日"] != startdate].index
# 刪除所有不是指定日期的個案
df.drop(indexNames, inplace=True)
# 計算境外移入人數
imported = df[df["是否為境外移入"] == "是"].sum()["確定病例數"]
print("今日境外移入人數:", imported)
# 計算本土人數
domestic = df[df["是否為境外移入"] == "否"].sum()["確定病例數"]
print("今日本土人數:", domestic)
total = imported + domestic
print("今日總人數:", total)
# 若要查看有哪些欄位
print((df.keys()))
# 也可以透過df.info()查看
df.info()
# 也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

import csv
from docx import Document

url = "https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json"
res = requests.get(url)
data = res.json()
# 因為有欄位名稱
# 只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
# 轉換'確定病例數'欄位內容為整數(以利後面加總)
df["確定病例數"] = df["確定病例數"].astype(int)
startdate = "2021/07/20"
startdate = input("請輸日期(yyyy/mm/dd)")
# 只保留個案研判日、是否為境外移入、確定病例數 三個欄位
df.drop(["確定病名", "縣市", "鄉鎮", "性別", "年齡層"], inplace=True, axis=1)
# 設定過濾條件(累積)
indexNames = df[df["個案研判日"] > startdate].index
# 刪除所有大於指定日期的個案
df.drop(indexNames, inplace=True)
# 計算累積確診人數
total = df.sum()["確定病例數"]
print("累積確診人數:", total)
# 設定過濾條件(今日)
indexNames = df[df["個案研判日"] != startdate].index
# 刪除所有不是指定日期的個案
df.drop(indexNames, inplace=True)
# 計算境外移入人數
imported = df[df["是否為境外移入"] == "是"].sum()["確定病例數"]
print("今日境外移入人數:", imported)
# 計算本土人數
domestic = df[df["是否為境外移入"] == "否"].sum()["確定病例數"]
print("今日本土人數:", domestic)
print("今日總人數:", domestic + imported)

url = "https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv"
df = pd.read_csv(url)
# 只保留確診、死亡、送驗、排除四個欄位
df.drop(["昨日確診", "昨日排除", "昨日送驗"], inplace=True, axis=1)
totaldeath = df.loc[0, "死亡"]
print("累積死亡人數", totaldeath)

# 開啟指定的Word檔案
my_doc = Document("指揮中心快訊.docx")
# 設定要取代的串列list
replacements = {
    "%Date%": startdate,
    "%N1%": str(domestic + imported),
    "%N2%": str(domestic),
    "%N3%": str(imported),
    "%N4%": str(totaldeath),
    "%N5%": str(total),
}
# 尋找要取代的關鍵字
for key in replacements:
    # 尋找所有的表格
    for table in my_doc.tables:
        # 尋找表格中的列
        for row in table.rows:
            # 尋找列中的每個儲存格
            for cell in row.cells:
                # 尋找儲存格中的每一個斷落
                for paragraph in cell.paragraphs:
                    # 如果關鍵字出現在段落中
                    if key in paragraph.text:
                        # 為了避免修改掉原有的樣式，必須用這個方法處理
                        inline = paragraph.runs
                        for i in range(len(inline)):
                            if key in inline[i].text:
                                text = inline[i].text.replace(key, replacements[key])
                                inline[i].text = text
# 指定儲存的檔案名稱
fname = "指揮中心快訊" + startdate.replace("/", "") + ".docx"
# 儲存檔案
my_doc.save(fname)

"""
請輸日期(yyyy/mm/dd)2021/07/20
累積確診人數: 15450
今日境外移入人數: 6
今日本土人數: 18
今日總人數: 24
累積死亡人數 846
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

字典
data_dict = json.loads(data)  # json 轉 字典
字串
data_str

串列
data_list


json為字串格式
json = json字串 = json_str

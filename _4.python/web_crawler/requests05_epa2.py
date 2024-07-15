"""
AQI綜合指標（Air Quality Index 空氣品質指標）

空氣品質指標值(AQI)

細懸浮微粒(PM2.5)
懸浮微粒(PM10)

空氣品質指標(AQI)
資料集代碼 	AQX_P_432

空氣品質指標(AQI)(歷史資料)
資料集代碼 	AQX_P_488
"""

import os
import pandas as pd


print("------------------------------------------------------------")  # 60個


def get_epa_key():
    filename = "C:/_git/vcs/_1.data/______test_files1/_key/epa_key.txt"

    filename = os.path.abspath(filename)
    if not os.path.exists(filename):  # 檢查檔案是否存在
        print("EPA_KEY 檔案不存在, 離開, 檔案 : " + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, "r")
    epa_key = fo.read()
    fo.close()

    length = len(epa_key)
    if length != 36:
        print("EPA_KEY 錯誤, 離開")
        return ""
    return epa_key


epa_key = get_epa_key()
length = len(epa_key)
if length != 36:
    print("EPA_KEY 錯誤, 離開")
    sys.exit(1)  # 立刻退出程式


DataID = "AQX_P_432"
format = "csv"
year_month = "2023_04"
offset = "0"
limit = "100"
api_key = epa_key

url = f"https://data.epa.gov.tw/api/v2/{DataID}?format={format}&api_key={api_key}"
print(url)

data = pd.read_csv(url)

citylist = []  # 縣市串列
sitelist = []  # 鄉鎮串列

# 建立縣市串列
for c1 in data["county"]:
    if c1 not in citylist:  # 如果串列中無該縣市就將其加入
        citylist.append(c1)

# 建立第1個縣市的測站串列
count = 0
for c1 in data["county"]:
    if c1 == citylist[0]:  # 是第1個縣市的測站
        sitelist.append(data.iloc[count, 0])
    count += 1

print("縣市串列")
print(citylist)
print("測站串列")
print(sitelist)

print(data)

citynamelist = []  # 縣市串列

# 建立縣市串列
for c1 in data["county"]:
    if c1 not in citynamelist:  # 如果串列中無該縣市就將其加入
        citynamelist.append(c1)

print("顯示縣市")
for c1 in citynamelist:
    print(c1)

print("顯示全台灣所有測站")
n = 0
for city in data["county"]:  # 逐一取出選取縣市的測站
    # sitelist.append(data.iloc[n, 0])
    print("位於 ", city, "的測站 : ", data.iloc[n, 0])
    n += 1

print("顯示單一城市內的所有測站 及其資料")
cityname = "桃園市"
n = 0
for c1 in data["county"]:  # 逐一取出選取縣市的測站
    if c1 == cityname:
        # sitelist.append(data.iloc[n, 0])
        print("位於 ", cityname, "的測站 : ", data.iloc[n, 0], end="\t")
        pm = data.iloc[n, 2]  # 取得PM2.5的值
        if pm == "" or pm == "ND":  # 如果沒有資料
            print("站的 PM2.5 值目前無資料！")
        else:  # 如果有資料
            if int(pm) <= 35:  # 轉換為等級
                grade1 = "低"
            elif int(pm) <= 53:
                grade1 = "中"
            elif int(pm) <= 70:
                grade1 = "高"
            else:
                grade1 = "非常高"
            print("PM2.5 值為「" + str(pm) + "」：「" + grade1 + "」等級")

    n += 1

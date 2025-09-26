# Python 測試 requests

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("準備工作")

import re
import csv
import json
import codecs
import pprint
import requests
from datetime import datetime

print("------------------------------------------------------------")  # 60個

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個


# 無參數
def get_html_data1(url):
    print("無參數取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


# 有參數
def get_html_data2(url, params):
    print("有參數取得網頁資料: ", url)
    print("參數: ", params)
    resp = requests.get(url=url, params=params)  # 有參數的GET請求
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


def get_html_data_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print("無法取得網頁資料")
        sys.exit(1)  # 立刻退出程式

    html_data.encoding = "UTF-8"  # 或是 unicode 也可, 指定編碼方式
    return html_data.text


print("------------------------------------------------------------")  # 60個

print("Response 物件資訊")

url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"  # 博客來網址
response = requests.get(url)

# 印出<class "requests.models.Response">，表示response為Response物件
print("物件型別：", type(response))
print("網址：", response.url)
# print("表頭資訊：", response.headers)
print("連線狀態：", response.status_code)
print("網頁編碼模式：", response.encoding)
# print("網頁程式碼：", response.text)

# 檢查狀態碼
if response.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(response.text))
    # print(response.text)            # 列印網頁內容
else:
    print("取得網頁內容失敗")
    print(response.status_code, response.reason)  # 若發生錯誤(狀態碼不是 200), 則印出狀態碼及錯誤原因

"""
HTTP狀態碼    response.status_code

if response.status_code == 403:
    print("403 Forbidden")

200 OK
400 Bad Request
401 Unauthorized
402 Payment Required
403 Forbidden
404 Not Found
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取網頁異常處理")
url = "http://mcut.edu.tw/file_not_existed"  # 不存在的內容
try:
    response = requests.get(url)
    response.raise_for_status()  # 異常處理
    print("下載成功")
except Exception as err:  # err是系統內建的錯誤訊息
    print(f"網頁下載失敗, 原因 : {err}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import urllib.request

# 設定欲請求的網址
url = "http://www.grandtech.info/"
# 以with/as敘述來取得網址，離開之後也能釋放資源
with urllib.request.urlopen(url) as response:
    print("網頁網址", response.geturl())
    print("伺服器狀態碼", response.getcode())
    print("網頁表頭", response.getheaders())
    zct_str = response.read().decode("UTF-8")

# OK, many
# print("將網頁資料轉成字串格式", zct_str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from urllib.parse import urlparse

url = "https://www.zct.com.tw/hot_sale.php?act=goods&hash=5717321f978f1"

result = urlparse(url)
print("回傳的 ParseResult 物件:")
print(result)
print("通訊協定:" + result.scheme)
print("網站網址:", result.netloc)
print("路徑:", result.path)
print("查詢字串:", result.query)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("requests 測試 1 無參數 取得網頁資料 只是把網頁抓下來")

url = "https://tw.news.yahoo.com/most-popular/"
url = "http://www.itwhy.org"
url = "http://www.ehappy.tw/demo.htm"
url = "http://tw.yahoo.com"

html_data = get_html_data1(url)
if html_data:
    print("擷取網頁資料 OK")
    # print(html_data.text)  # OK, many
    # pprint.pprint(html_data.text)  # OK, many
else:
    print("無法取得網頁資料")

print("------------------------------------------------------------")  # 60個
print("requests 測試 2 有參數 取得網頁資料 只是把網頁抓下來")

print("有參數 取得網頁資料 a")
url = "http://dict.baidu.com/s"
params = {"wd": "python"}

html_data = get_html_data2(url, params)

print("111", html_data.url)
print("222", html_data.text)  # 打印解码后的返回数据
print("333", html_data)

print("------------------------------------------------------------")  # 60個

print("有參數 取得網頁資料 d")
search_word = "椎名林檎"
url = "https://zh.wikipedia.org/w/api.php"
params = {
    "format": "xmlfm",
    "action": "query",
    "prop": "revisions",
    "rvprop": "content",
}
params["titles"] = search_word
html_data = get_html_data2(url, params)

""" NG
# pprint.pprint(html_data)
# fo = codecs.open("tmp_wiki搜尋結果2" + search_word + ".html", "w", "utf-8") # same
fo = open("tmp_wiki搜尋結果2" + search_word + ".html", "w", encoding="utf-8")
fo.write(html_data.text)
fo.close()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 cookies over18, 無 cookies 抓網頁")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
url = "https://www.ptt.cc/bbs/Beauty/M.1707360497.A.39D.html"

print("無 cookies 抓不到網頁資料")
response = requests.get(url)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 cookies over18, 有 cookies 抓網頁")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
url = "https://www.ptt.cc/bbs/Beauty/M.1707360497.A.39D.html"

print("有 cookies 可以抓到網頁資料")
cookies = {"over18": "1"}
response = requests.get(url, cookies=cookies)
print(response.text)

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
cookies = {"over18": "1"}

response = requests.get(url, cookies=cookies, headers=headers)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 headers, 無 headers 抓網頁, ck101 網頁")

# 怎麼無headers 也是OK?
url = "https://ck101.tw/thread-5778209-1-1.html"
# url ="https://www.dcard.tw/f/stock/p/237123381"

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 headers, 有 headers 抓網頁, ck101 網頁")

url = "https://ck101.tw/thread-5778209-1-1.html"
# url ="https://www.dcard.tw/f/stock/p/237123381"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
response = requests.get(url, headers=headers)
print(response)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 headers, 無 headers 抓網頁, 金石堂官網")
print("不支持直接讀取網頁, 要使用偽裝瀏覽器")

url = "https://www.kingstone.com.tw/"

try:
    response = requests.get(url)
    response.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
except Exception as err:  # err是系統內建的錯誤訊息
    print(f"網頁下載失敗, 原因 : {err}")

print("------------------------------")  # 30個

print("測試 headers, 無 headers 抓網頁, 金石堂官網")
print("使用偽裝瀏覽器")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36",
}
url = "https://www.kingstone.com.tw/"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
except Exception as err:  # err是系統內建的錯誤訊息
    print(f"網頁下載失敗, 原因 : {err}")

print("偽裝瀏覽器擷取網路資料成功")

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com/"
# 假的 headers 資訊
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
# 加入 headers 資訊
response = requests.get(url, headers=headers)
response.encoding = "utf8"
print(response.text)

print("------------------------------------------------------------")  # 60個

print("requests 測試 13 讀取網頁上的csv檔")

print("教育部統計處資料")
url = "https://stats.moe.gov.tw/files/detail/111/111_student.csv"
html_data_text = get_html_data_from_url(url)

rows = html_data_text.split("\n")
print("第 0 row")
print(rows[0])
print("第 1 row")
print(rows[1])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("requests 測試 14b")

print("教育部統計處資料1")
url = "https://stats.moe.gov.tw/files/detail/108/108_student.csv"

html_data_text = get_html_data_from_url(url)
rows = html_data_text.split("\n")
data = list()
columns = rows[0].split(",")
for row in rows[1:]:
    try:
        row = row.split(",")
        item = list()
        for f_index in range(1, 5):
            item.append(row[f_index].replace('"', ""))
        data.append(item)
    except:
        pass

filename = "tmp_教育部統計處資料1_" + os.path.basename(url)
with open(filename, "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(columns[1:5])
    writer.writerows(data)
print("存檔檔案 :", filename)

print("------------------------------------------------------------")  # 60個
print("requests 測試 15")

print("教育部統計處資料2")
url = "https://stats.moe.gov.tw/files/detail/{0}/{0}_student.csv"

for year in range(107, 109):
    csvdata = requests.get(url.format(year)).text
    rows = csvdata.split("\n")
    data = list()
    columns = rows[0].split(",")
    for row in rows[1:]:
        try:
            row = row.split(",")
            item = list()
            for f_index in range(1, 5):
                item.append(row[f_index].replace('"', ""))
            data.append(item)
        except:
            pass

    filename = "tmp_教育部統計處資料2_" + os.path.basename(url.format(year))
    print("存檔檔案 :", filename)
    with open(filename, "w", encoding="utf-8", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(columns[1:5])
        writer.writerows(data)
    time.sleep(3)

print("OK")

print("------------------------------------------------------------")  # 60個
print("requests 測試 19 json 測試")

print("PC Home 電腦售價")
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc"

html_data_text = get_html_data_from_url(url)

json_data = json.loads(html_data_text)["prods"]
for product in json_data:
    if product["price"] > 20000:
        print("NT$:{}, {}".format(product["price"], product["name"]))

print("------------------------------------------------------------")  # 60個
print("requests 測試 20 json 測試")

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc"

html_data_text = get_html_data_from_url(url)

json_data = json.loads(html_data_text)["prods"]
message = ""
for product in json_data:
    if product["price"] > 20000:
        message = message + "NT$:{}, {}\n".format(product["price"], product["name"])

print("Mac Mini價格通知", message)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("requests 測試 21 中油油價 json 測試")

url = "https://www.cpc.com.tw/historyprice.aspx?n=2890"
response = requests.get(url)

m = re.search("var pieSeries = (.*);", response.text)
jsonstr = m.group(0).strip("var pieSeries = ").strip(";")
json_data = json.loads(jsonstr)
# print(json_data)
cnt = 1
for item in reversed(json_data):  # 反向排序, 利用 reversed 反轉了排序(原內容由舊到新, 利用這個改為由新到舊)
    new_line = 0
    for data in item["data"]:
        if data["name"] == "超級/高級柴油":
            new_line = 0
            continue
        else:
            new_line = 1
        print("date:" + item["name"])  # 第一層的 name 為日期
        print(
            data["name"] + ":" + str(data["y"])
        )  # 後面再接一層 array data 其中的 name 為產品名, 而 y 為單價
    if new_line == 1:
        print("================")

    cnt += 1
    if cnt == 10:
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" many 已把 thread 搬出
import threading

# XKCD 漫畫的基本 URL
base_url = "https://xkcd.com/"

# 定義下載漫畫的函數
def download_xkcd(start_comic, end_comic):
    for comic_number in range(start_comic, end_comic):
        # 跳過編號為 0 的漫畫，因為它不存在
        if comic_number == 0:
            continue

        url = f"{base_url}{comic_number}/info.0.json"   # 建立API URL來獲取漫畫資訊
        try:
            response = requests.get(url)
            try:
                response.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
            except Exception as err:                    # err是系統內建的錯誤訊息
                print(f"網頁下載失敗, 原因 : {err}")

            comic_json = response.json()  # response轉成json格式
            comic_url = comic_json["img"]               # 從JSON響應中提取圖片 URL
            print(f"\n圖片下載中 : {comic_url}...")

            # 向圖片 URL 發送請求並下載圖片
            res = requests.get(comic_url)
            try:
                res.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
            except Exception as err:                    # err是系統內建的錯誤訊息
                print(f"網頁下載失敗, 原因 : {err}")

            # 保存圖片到本地資料夾
            with open(os.path.join("xkcd_comics", os.path.basename(comic_url)), "wb") as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)             # 寫入圖片數據
        except requests.exceptions.HTTPError as err:
            print(f"Failed to download comic {comic_number}: {err}")  # 輸出錯誤訊息

# 建立並啟動多個執行緒
thread_count = 10                                       # 執行緒的數量
comic_range = 10                                        # 每個執行緒負責下載的漫畫數量

# 如果不存在, 建立一個目錄來存儲下載的漫畫
if not os.path.exists("xkcd_comics"):
    os.makedirs("xkcd_comics")

# 建立執行緒並將它們添加到執行緒串列表
threads = []
for i in range(1, thread_count * comic_range, comic_range):         # 漫畫編號從 1 開始
    start = i
    end = i + comic_range
    thread = threading.Thread(target=download_xkcd, args=(start, end))
    threads.append(thread)
    thread.start()                                      # 啟動執行緒

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("漫畫圖片下載完成")

"""
print("------------------------------------------------------------")  # 60個

"""
# 建立 Proxy List
proxy_ips = [
    "80.93.213.213:3136",
    "191.241.226.230:53281",
    "207.47.68.58:21231",
    "176.241.95.85:48700",
]
# 依序執行 get 方法
for ip in proxy_ips:
    try:
        url = "https://www.google.com"
        result = requests.get(url, proxies={"http": "ip", "https": ip}
        )
        print(result.text)
    except:
        print(f"{ip} invalid")
"""
print("------------------------------------------------------------")  # 60個

print("測試一個 echo 函數")
# 設定參數
params = {"name": "david", "age": "18"}
# 加入參數
url = "https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec"
response = requests.get(
    url,
    params=params,
)
print(response.text)

print("------------------------------------------------------------")  # 60個

""" 改了
# 2022/12 時氣象局有修改了 API 內容，將部份大小寫混合全改成小寫，因此程式碼也跟著修正
url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
response = requests.get(url)  # 使用 get 方法透過空氣品質指標 API 取得內容
response_json = response.json()  # response轉成json格式
for i in response_json["records"]:  # 依序取出 records 內容的每個項目
    print(i["county"] + " " + i["sitename"], end="，")  # 印出城市與地點名稱
    print("AQI:" + i["aqi"], end="，")  # 印出 AQI 數值
    print("空氣品質" + i["status"])  # 印出空氣品質狀態

print("------------------------------------------------------------")  # 60個

csvfile = open("tmp_csv-aqi.csv", "w")  # 建立空白並可寫入的 CSV 檔案
csv_write = csv.writer(csvfile)  # 設定 csv_write 為寫入

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
response = requests.get(url)
response_json = response.json()  # response轉成json格式
output = [["county", "sitename", "aqi", "空氣品質"]]  # 設定 output 變數為二維串列，第一筆資料為開頭
for i in response_json["records"]:
    # 依序將取得的資料加入 output 中
    output.append([i["county"], i["sitename"], i["aqi"], i["status"]])
print(output)
csv_write.writerows(output)  # 多行寫入 CSV
"""
print("------------------------------------------------------------")  # 60個

""" NG
url = "一般天氣預報 - 今明 36 小時天氣預報 JSON 連結"
response = requests.get(url)  # 取得 JSON 檔案的內容為文字
response_json = response.json()  # response轉成json格式
location = response_json["cwbopendata"]["dataset"]["location"]  # 取出 location 的內容
for i in location:
    print(f"{i}")

print("------------------------------------------------------------")  # 60個

url = "一般天氣預報 - 今明 36 小時天氣預報 JSON 連結"
response = requests.get(url)  # 取得 JSON 檔案的內容為文字
response_json = response.json()  # response轉成json格式
location = response_json["cwbopendata"]["dataset"]["location"]
for i in location:
    city = i["locationName"]  # 縣市名稱
    wx8 = i["weatherElement"][0]["time"][0]["parameter"]["parameterName"]  # 天氣現象
    maxt8 = i["weatherElement"][1]["time"][0]["parameter"]["parameterName"]  # 最高溫
    mint8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]  # 最低溫
    ci8 = i["weatherElement"][3]["time"][0]["parameter"]["parameterName"]  # 舒適度
    pop8 = i["weatherElement"][4]["time"][0]["parameter"]["parameterName"]  # 降雨機率
    print(f"{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %")

print("------------------------------------------------------------")  # 60個

url = "你的氣象觀測資料 JSON 網址"
response = requests.get(url)
response_json = response.json()  # response轉成json格式
location = response_json["cwbopendata"]["location"]
for i in location:
    name = i["locationName"]  # 測站地點
    city = i["parameter"][0]["parameterValue"]  # 城市
    area = i["parameter"][2]["parameterValue"]  # 行政區
    print(city, area, name)

print("------------------------------------------------------------")  # 60個

url = "你的氣象觀測資料 JSON 網址"
response = requests.get(url)
response_json = response.json()  # response轉成json格式
location = response_json["cwbopendata"]["location"]
for i in location:
    name = i["locationName"]  # 測站地點
    city = i["parameter"][0]["parameterValue"]  # 城市
    area = i["parameter"][2]["parameterValue"]  # 行政區
    temp = i["weatherElement"][3]["elementValue"]["value"]  # 氣溫
    humd = round(
        float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1
    )  # 相對濕度
    r24 = i["weatherElement"][6]["elementValue"]["value"]  # 累積雨量

    print(city, area, name, f"{temp} 度", f"相對濕度 {humd}%", f"累積雨量 {r24}mm")

print("------------------------------------------------------------")  # 60個

url = "你的氣象觀測資料 JSON 網址"
response = requests.get(url)
response_json = response.json()  # response轉成json格式
location = response_json["cwbopendata"]["location"]
weather = {}  # 新增一個 weather 字典
for i in location:
    name = i["locationName"]
    city = i["parameter"][0]["parameterValue"]
    area = i["parameter"][2]["parameterValue"]
    temp = i["weatherElement"][3]["elementValue"]["value"]
    humd = round(float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1)
    r24 = i["weatherElement"][6]["elementValue"]["value"]
    msg = f"{temp} 度，相對濕度 {humd}%，累積雨量 {r24}mm"  # 組合成天氣描述
    try:
        weather[city][name] = msg  # 記錄地區和描述
    except:
        weather[city] = {}  # 如果每個縣市不是字典，建立第二層字典
        weather[city][name] = msg  # 記錄地區和描述

show = ""
for i in weather:
    show = show + i + ","  # 列出可輸入的縣市名稱
show = show.strip(",")  # 移除結尾逗號
a = input(f"請輸入下方其中一個縣市\n( {show} )\n")  # 讓使用者輸入縣市名稱

show = ""
for i in weather[a]:
    show = show + i + ","  # 列出可輸入的地點名稱
show = show.strip(",")  # 移除結尾逗號
b = input(f"請輸入{a}的其中一個地點\n( {show} )\n")  # 讓使用者輸入觀測地點名稱
print(f"{a}{b}，{weather[a][b]}。")  # 顯示結果
"""
print("------------------------------------------------------------")  # 60個

print("台灣銀行 匯率查詢")

url = "https://rate.bot.com.tw/xrt/flcsv/0/day"  # 牌告匯率 CSV 網址

response = requests.get(url)  # 爬取網址內容
response.encoding = "utf-8"  # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = response.text  # 以文字模式讀取內容
rts = rt.split("\n")  # 使用「換行」將內容拆分成串列
for i in rts:  # 讀取串列的每個項目
    try:  # 使用 try 避開最後一行的空白行
        a = i.split(",")  # 每個項目用逗號拆分成子串列
        print(a[0] + ": " + a[12])  # 取出第一個 ( 0 ) 和第十三個項目 ( 12 )
    except:
        break

print("------------------------------------------------------------")  # 60個

""" fail
url = "你的應用程式網址"
name = "工作表1"
row = 2
response = requests.get(f"{url}?name={name}&row={row}")

print("response轉成json格式")
print(response.json())

name = "工作表2"
response = requests.get(f"{url}?name={name}")

print("response轉成json格式")
print(response.json())

print("------------------------------------------------------------")  # 60個

url = "部署的網址"

params = {"name": "工作表1", "top": "true", "data": "[123,456,789]"}

response = requests.get(url=url, params=params)

print("------------------------------------------------------------")  # 60個

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}  # 設定權杖
data = {"message": "測試一下！"}  # 設定要發送的訊息
data = requests.post(url, headers=headers, data=data)  # 使用 POST 方法

print("------------------------------------------------------------")  # 60個

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {"message": "測試一下！", "stickerPackageId": "446", "stickerId": "1989"}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {
    "message": "測試一下！",
    "imageThumbnail": "https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png",
    "imageFullsize": "https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png",
}
data = requests.post(url, headers=headers, data=data)
"""
print("------------------------------------------------------------")  # 60個

from io import StringIO

datestr = "20240716"

url = (
    "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
    + datestr
    + "&type=ALLBUT0999"
)
print(url)

# 下載股價
response = requests.get(url)
# print(response.text)

r_text = response.text.split("\n")

r_text = [i for i in r_text if len(i.split('",')) == 17 and i[0] != "="]

data = "\n".join(r_text)

df = pd.read_csv(StringIO(data), header=0)

df = df.drop(columns=["Unnamed: 16"])

stock_symbol = "2330"  # 台積電
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)

print("------------------------------------------------------------")  # 60個

""" no module
import crawler_module as m

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    time.sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)
print(all_df)

# step 1 prepare data
day = all_df["日期"].astype(str)
close = all_df["收盤價"].astype(float)

# step 2 create plot
plt.figure(figsize=(12, 8), dpi=100)

# step 3 plot
plt.plot(day, close, "s-", color="r", label="Close Price")
plt.title("TSMC Line chart")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc="best", fontsize=20)

plt.show()

print("------------------------------------------------------------")	#60個

import crawler_module as m

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    time.sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)

# step 1 prepare data
day = all_df["日期"].astype(str)
openprice = all_df["開盤價"].astype(float)
close = all_df["收盤價"].astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8), dpi=100)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
ax.set_title(stock_symbol+"  開盤價、收盤價 ( " +
             dates[0] + " ~ " + dates[-1] + " )")

# step 3 plot 子圖(ax)
ax.plot(day, openprice, "s-", color="r", label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close, "o-", color="b", label="Close Price")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])

# step 4 show plot
plt.show()
"""

print("------------------------------------------------------------")  # 60個

"""
import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = m.get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

print("開始下載...")

for i in range(len(photo_list)):
    m.download_pic(photo_list[i], str(i+1))

print("\n下載完畢")

print("------------------------------------------------------------")	#60個

import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")
        
    download_num = int(input("請輸入要下載的數量: "))
    
    photo_list = m.get_photolist(photo_name, download_num) 
    
    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張" )
        else:
            print("取得所有圖片連結") 
        break

folder_name = m.create_folder(photo_name)
    
print("開始下載...")
 
for i in range(len(photo_list)):
    m.download_pic(photo_list[i], folder_name + os.sep + photo_name + os.sep + str(i+1))
    
print("\n下載完畢")
"""

print("------------------------------------------------------------")  # 60個

print("檢查錯誤碼")

url = "http://example.com"

try:
    # 嘗試發出網絡請求
    response = requests.get(url)

    # 如果請求返回了錯誤響應, 會引發 HTTPError
    response.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
except requests.exceptions.HTTPError as e:
    # 處理 HTTP 錯誤
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    # 處理連接錯誤
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    # 處理請求超時錯誤
    print(f"Timeout Error: {e}")

print("------------------------------------------------------------")  # 60個
"""
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid="AC308f91e9dc748a01538feb9d74ed993a"
# 你從twilio.com獲得的圖騰
authToken="f513161b63f71720f62118e4d33ca8ac"

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+15052070000",         # 這是twilio.com給你的號碼
            to = "+886952xxxxxx",           # 填上老師的號碼
            body = "感謝老師,我們學會了Python" )   # 發送的訊息
"""
print("------------------------------------------------------------")  # 60個

print("讀取網頁的json資料")

url = "https://www.oxxostudio.tw/json/pageList.json"
response = requests.get(url)
json_data = json.loads(response.text)  # 轉成 json 格式
# print(json_data)#全部
print("第0筆")
print(json_data[0])
print("第1筆")
print(json_data[1])

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
# 此處不使用，因為發現出來變成純文字格式，非 json
jj = json.dumps(json_data[0], ensure_ascii=False)
print(jj)

with open("tmp_json_data1.txt", "a+") as f:
    f.write(jj)

print("讀取網頁的json資料 -> csv檔")

with open("tmp_json_data2.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for i in json_data:
        writer.writerow([i["tag"], i["title"], i["site"], i["date"]])
        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])
    print("寫入完成！")

print("------------------------------------------------------------")  # 60個
""" no file
# 參考 https://zh.wikipedia.org/wiki/%E9%80%97%E5%8F%B7%E5%88%86%E9%9A%94%E5%80%BC
from collections import OrderedDict

with open("data/a16.csv") as csvFile:
    # r = csv.reader(csvFile)      # 無法和 DictReader 同時使用，不知道為什麼
    # for i in r:
    #   print(i)

    rows = csv.DictReader(csvFile)  # 轉成 OrderedDict
    o = []
    for row in rows:
        print(row)
        d = dict(OrderedDict(row))  # 轉成 Dict
        print(d)
        o.append(d)

    for i in o:
        print(f'姓名：{i["name"]}，年紀：{i["age"]} 歲。')
"""
print("------------------------------------------------------------")  # 60個

""" fail
from lxml import html

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
response = requests.get(url)
tree = html.fromstring(response.text)

print("美金：" + str(tree.xpath("//html/body/div[1]/main/div[3]/table/tbody/tr[1]/td[3]/text()")[0]))
print("日圓：" + str(tree.xpath("//html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()")[0]))
"""
print("------------------------------------------------------------")  # 60個

print("requests 測試 16 字串處理 技巧")

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pprint.pprint(pages)
print()
print(pages)

for page in pages:
    print(page)

for pg_no, page in enumerate(pages, 1):
    html = requests.get(page).text
    filename = "tmp_page-{}.txt".format(pg_no)
    with open(filename, "wt") as fp:
        fp.write(html)
    print("存檔檔案 :", filename)
    time.sleep(3)
    print("=========================")

print("------------------------------------------------------------")  # 60個

"""
import socket

socket.socket(family, type, proto)
# family：IPv4 本機、IPv4 網路、IPv6 網路。
# type：使用 TCP 或 UDP 方式。
# protocol: 串接協定 ( 通常預設 0 )。
"""
print("------------------------------------------------------------")  # 60個

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print(ip)
s.close()

print("------------------------------------------------------------")  # 60個

"""
A Simple Public IP Address API
https://www.ipify.org/
"""
print("測試 ipify")

# IPv4/IPv6 皆可

url = "https://api64.ipify.org"
response = requests.get(url)
print("My public IP address is: {}".format(response.text))

url = "https://api64.ipify.org?format=json"
response = requests.get(url)
print(response.text)

print("------------------------------------------------------------")  # 60個

import socket

hostname = "google.com"
print("Hostname :", hostname)
print("Host :", socket.gethostbyname(hostname))

print("------------------------------------------------------------")  # 60個

print("將網頁上的檔案存成本地檔案 csv / jpg / png")

url = "https://stats.moe.gov.tw/files/detail/111/111_student.csv"
url = "http://i.epochtimes.com/assets/uploads/2015/05/1502192113172483-600x400.jpg"  # 貼上src屬性中的路徑
url = "https://zh.wikipedia.org/static/images/icons/wikipedia.png"
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Alliance_of_Sahel_States.svg/800px-Alliance_of_Sahel_States.svg.png"

# response = requests.get(url) #使用 GET 對檔案連結發出請求

from urllib.request import unquote

print("網址解碼 utf-8")
url = unquote(url, encoding="utf-8")
print(url)

response = requests.get(url)  # 使用 GET 對檔案連結發出請求

filename = "tmp_" + os.path.basename(url)
with open(filename, "wb") as f:
    f.write(response.content)  # 將response.content二進位內容寫入檔案
print("存檔檔案 :", filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# NG
"""
print("擷取網頁圖片, 保存檔名2")

import base64
from io import BytesIO
from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

filename = "tmp_" + url.split("/")[-1]
print("圖片檔名:", filename)

image.save(filename)
print("存檔檔案 :", filename)
# print(base64.b64encode(response.content))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台灣水庫即時水情")
url = "https://water.taiwanstat.com/"  # 台灣水庫即時水情
# url = "https://invoice.etax.nat.gov.tw/index.html"
# url = "https://data.kcg.gov.tw/dataset/6f29f6f4-2549-4473-aa90-bf60d10895dc/resource/30dfc2cf-17b5-4a40-8bb7-c511ea166bd3/download/lightrailtraffic.json"

response = requests.get(url)  # 取得網頁內容
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

print("response內的text")
print(response.text)  # 讀取並印出 text 屬性

""" NG
print("response轉成json格式")
print(response.json())
"""

print("------------------------------------------------------------")  # 60個

# https://mis.twse.com.tw/stock/fibest.jsp?stock=0050
url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw"
response = requests.get(url)
json_data = json.loads(response.text)

print(json_data)

print("------------------------------------------------------------")  # 60個

print("儲存網頁內容, 天瓏書局")
url = "http://www.tenlong.com.tw"  # 天瓏書局

try:
    response = requests.get(url)
    print("下載成功")
except Exception as err:
    print(f"網頁下載失敗, 原因 : {err}")

# 儲存網頁內容
fn = "tmp_html_text1.html"
with open(fn, "wb") as f:  # 以二進位儲存
    for diskStorage in response.iter_content(10240):  # Response物件處理
        size = f.write(diskStorage)  # Response物件寫入
        print("寫入資料 :", size, "拜")
    print("以 %s 儲存網頁HTML檔案成功" % fn)

print("------------------------------------------------------------")  # 60個

""" many
url = "http://tw.yahoo.com"
response = requests.get(url)
pprint.pprint(response.text)
"""

print("------------------------------------------------------------")  # 60個

url = "https://www.googleapis.com/books/v1/volumes"

data = {"q": "Python", "maxResults": 5, "projection": "lite"}

response = requests.get(url, params=data)
print(response.json())

print("------------------------------------------------------------")  # 60個

response = requests.get("https://fchart.github.io/test.html")
print(response.text)
print(response.encoding)

print("------------------------------------------------------------")  # 60個

response = requests.get("https://fchart.github.io/test.html")
print(response.text)
print("----------------------")

response = requests.get("https://fchart.github.io/test.html")
print(response.content)
print("----------------------")

response = requests.get("https://fchart.github.io/test.html", stream=True)
print(response.raw)
print(response.raw.read(15))

print("------------------------------------------------------------")  # 60個

response = requests.get("https://fchart.github.io/json/Example.json")
print(response.text)
print(type(response.text))
print("----------------------")
print(response.json())
print(type(response.json()))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

response = requests.get("http://www.google.com")

if response.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")

print(response.status_code)
print(response.status_code == requests.codes.ok)
print(response.status_code == requests.codes.all_good)

response = requests.get("http://www.google.com/404")
print(response.status_code)
print(response.status_code == requests.codes.ok)
# NG print(response.raise_for_status())

print("------------------------------------------------------------")  # 60個

response = requests.get("http://www.google.com")

print(response.headers["Content-Type"])
# NG print(response.headers["Content-Length"])
print(response.headers["Date"])
print(response.headers["Server"])

print(response.headers.get("Content-Type"))
print(response.headers.get("Content-Length"))
print(response.headers.get("Date"))
print(response.headers.get("Server"))

print("------------------------------------------------------------")  # 60個

session = requests.Session()
response = session.get("http://www.google.com")
v = session.cookies.get_dict()
print(v)

print("------------------------------------------------------------")  # 60個

url = "https://www.googleapis.com/books/v1/volumes"

url_params = {"q": "Python", "maxResults": 3, "projection": "lite"}
response = requests.get(url, params=url_params)
print(response.json())

print("------------------------------------------------------------")  # 60個

try:
    response = requests.get("http://www.google.com", timeout=0.03)
    print(response.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))

print("------------------------------------------------------------")  # 60個

url = "http://www.google.com/404"

try:
    response = requests.get(url, timeout=3)
    response.raise_for_status()
except requests.exceptions.RequestException as ex1:
    print("Http請求錯誤: " + str(ex1))
except requests.exceptions.HTTPError as ex2:
    print("Http回應錯誤: " + str(ex2))
except requests.exceptions.ConnectionError as ex3:
    print("網路連線錯誤: " + str(ex3))
except requests.exceptions.Timeout as ex4:
    print("Timeout錯誤: " + str(ex4))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("對抓取到的網頁資料做處理")
print("------------------------------------------------------------")  # 60個

print("requests 測試 11 對網頁資料處理 尋找單字出現次數")

url = "https://www.ptt.cc/bbs/hotboards.html"
html_data_text = get_html_data_from_url(url)

lines = html_data_text.splitlines()  # 將網頁資料一行一行地分割成串列

n = 0
for line in lines:
    if "音樂" in line:
        n += 1

print("找到 {} 次!".format(n))

print("------------------------------------------------------------")  # 60個

print("requests 測試 22")

print("抓取網頁中的電話號碼 用 re")

url = "https://www.taichung.gov.tw/10179/12034/"

html = requests.get(url).text

regex04a = r"\(\d{2}\)\d{4}-?\d{4}"
regex04b = r"\d{2}-\d{4}-?\d{4}"
regex0800 = r"0800-\d{6}"
matches = re.findall(regex04a, html)
matches += re.findall(regex04b, html)
matches += re.findall(regex0800, html)
""" many
for match in matches:
    print("抓到符合條件的 : ", match)
    
print("全部資料")
print(matches)
"""
print("------------------------------------------------------------")  # 60個

print("抓取網頁中的e-mail地址 用 re")

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+)"
url = "http://csharphelper.com/blog/"

html = requests.get(url, verify=False).text

emails = re.findall(regex, html)
for email in emails:
    print(email)

print("------------------------------------------------------------")  # 60個


print("抓取網頁內的所有圖片連結")

url = "https://www.bagong.cn/dog/"

html = requests.get(url).text

regex = r"https?://.+.jpg"
photos = re.findall(regex, html)

""" many
for photo in photos:
    print("取得連結 :", photo)
"""

print("------------------------------------------------------------")  # 60個

import urllib.parse

print("聯合新聞網之即時新聞 標題 與 連結")

url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
html = requests.get(url).text
json_data = json.loads(html)

""" many
titles = json_data["lists"]
for title in titles:
    print(title["title"])
    print(urllib.parse.urljoin("https://udn.com", title["titleLink"]))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("拆解網頁資料")
url = "https://today.line.me/tw/v2/article/oqay0ro"
response = requests.get(url)
""" NG
# 取得文章的原始碼後，使用 split 字串拆分的方式，拆解出 articleId
article_id = response.text.split("<script>")[1].split("id:"article:")[1].split(":")[0]
print(article_id)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("拆解網頁資料")

print("查詢一個網頁有出現的詞的次數 聯合新聞網之即時新聞 關鍵字")

url = "https://udn.com/news/breaknews/1/99#breaknews"

response = requests.get(url)
html = response.text
print(response.status_code)

text = "賴"
print("要查詢的詞 :", text)
print("出現次數 :", html.count(text))

text = "總統"
print("要查詢的詞 :", text)
print("出現次數 :", html.count(text))

text = "委員"
print("要查詢的詞 :", text)
print("出現次數 :", html.count(text))

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

print("------------------------------")  # 30個


print("------------------------------------------------------------")  # 60個


# 讀取網頁上的 csv 檔
csv_file = "xxxxx .csv"
df = pd.read_csv(csv_file)
print("------------------------------")  # 30個
print(df.head())
print("------------------------------")  # 30個

# 讀取網頁上的 excel 檔
xlsx_file = "xxxx .xlsx"
df = pd.read_excel(xlsx_file)
print("------------------------------")  # 30個
print(df.head())
print("------------------------------")  # 30個

# 兩個方法得到的df是一樣的

print("用list 標註變數名稱從DataFrame選出country 與continent 欄位：")
print(df[["country", "continent"]])

print("------------------------------")  # 30個
print("選一個變數且沒有以list 標註，選出欄位資料，型別為Series")
country = df["country"]
print(type(country))
print("------------------------------")  # 30個
print("聚合函數計算sum，計算2007 年全球人口總數：")
aa = df[df["year"] == 2007][["pop"]].sum()
print(aa)
print("------------------------------")  # 30個
print("計算2007 年全球的平均壽命、平均財富：")
bb = df[df["year"] == 2007][["lifeExp", "gdpPercap"]].mean()
print(bb)
print("------------------------------")  # 30個
print("groupby群組計算2007 年各洲人口總數：")
cc = df[df["year"] == 2007].groupby(by="continent")["pop"].sum()
print(cc)

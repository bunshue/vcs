# Python 測試 requests

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
# import datetime
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
print("------------------------------------------------------------")  # 60個

import re
import csv
import json
import codecs
import pprint
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request

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
        sys.exit()  # 立刻退出程式

    html_data.encoding = "UTF-8"  # 或是 unicode 也可, 指定編碼方式
    return html_data.text


print("------------------------------------------------------------")  # 60個

print("Response 物件資訊")

url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"  # 博客來網址
response = requests.get(url)
# pprint.pprint(response.text)  # HTML網頁內容

# 印出<class "requests.models.Response">，表示response為Response物件
print("物件型別：", type(response))
print("網址：", response.url)
# print("表頭資訊：", response.headers)
print("HTTP狀態碼 :", response.status_code)
print("網頁編碼模式 :", response.encoding)

# print(response.text)  # HTML網頁內容

# 檢查HTTP狀態碼
if response.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(response.text))
    # print(response.text)  # HTML網頁內容
else:
    print("取得網頁內容失敗")
    print("HTTP狀態碼 :", response.status_code)
    print("HTTP錯誤原因 :", response.reason)
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

# print(response.text)  # HTML網頁內容

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 cookies over18, 有 cookies 抓網頁")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
url = "https://www.ptt.cc/bbs/Beauty/M.1707360497.A.39D.html"

print("有 cookies 可以抓到網頁資料")
cookies = {"over18": "1"}
response = requests.get(url, cookies=cookies)

# print(response.text)  # HTML網頁內容

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
cookies = {"over18": "1"}

response = requests.get(url, cookies=cookies, headers=headers)

# print(response.text)  # HTML網頁內容

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 headers, 無 headers 抓網頁, ck101 網頁")

# 怎麼無headers 也是OK?
url = "https://ck101.tw/thread-5778209-1-1.html"
# url ="https://www.dcard.tw/f/stock/p/237123381"

response = requests.get(url)

print(response)
print("HTTP狀態碼 :", response.status_code)
print("HTTP錯誤原因 :", response.reason)
# print(response.text)  # HTML網頁內容
print("網址：", response.url)
print("表頭資訊 :", response.headers)
print("異常處理 :", response.raise_for_status())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 headers, 有 headers 抓網頁, ck101 網頁")

url = "https://ck101.tw/thread-5778209-1-1.html"
# url ="https://www.dcard.tw/f/stock/p/237123381"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
response = requests.get(url, headers=headers)
print(response)

# print(response.text)  # HTML網頁內容

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個

url = "https://www.google.com/"
# 假的 headers 資訊
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
# 加入 headers 資訊
response = requests.get(url, headers=headers)
response.encoding = "utf8"  # 網頁編碼模式

# print(response.text)  # HTML網頁內容

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("requests 測試 13 抓取遠端檔案 csv")
print("將網頁上的檔案存成本地檔案 csv / jpg / png / htm")

url = "https://stats.moe.gov.tw/files/detail/108/108_student.csv"  # 教育部統計處資料
url = "https://zh.wikipedia.org/static/images/icons/wikipedia.png"
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Alliance_of_Sahel_States.svg/800px-Alliance_of_Sahel_States.svg.png"
url = "http://jinyong.ylib.com.tw/works/v1.0/works/poem-24.htm"  # 葡萄美酒夜光杯──祖千秋論酒杯詩2
url = "http://i.epochtimes.com/assets/uploads/2015/05/1502192113172483-600x400.jpg"

response = requests.get(url)  # 使用 GET 對檔案連結發出請求

print("取出路徑中的檔案名稱 :", os.path.basename(url))

filename = "tmp_" + os.path.basename(url)
with open(filename, "wb") as f:
    f.write(response.content)  # 將response.content二進位內容寫入檔案
print("存檔檔案 :", filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("擷取網頁圖片, 保存檔名, 只支持jpg檔")

from io import BytesIO
from PIL import Image

url = "http://i.epochtimes.com/assets/uploads/2015/05/1502192113172483-600x400.jpg"

response = requests.get(url)

image = Image.open(BytesIO(response.content))

print("取出路徑中的檔案名稱 :", os.path.basename(url))

filename = "tmp_" + os.path.basename(url)
image.save(filename)
print("存檔檔案 :", filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("requests 測試 20 json 測試")

print("PC Home 電腦售價, Mac Mini價格")
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc"

html_data_text = get_html_data_from_url(url)

json_data = json.loads(html_data_text)["prods"]
for product in json_data:
    if product["price"] > 20000:
        print("NT$:{}, {}".format(product["price"], product["name"]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("requests 測試 21 中油油價 json 測試")

url = "https://www.cpc.com.tw/historyprice.aspx?n=2890"
response = requests.get(url)

m = re.search("var pieSeries = (.*);", response.text)
jsonstr = m.group(0).strip("var pieSeries = ").strip(";")
json_data = json.loads(jsonstr)  # json轉串列, 串列由字典組成
print(type(json_data))
print("共有 :", len(json_data), "筆資料, 只看最新的10筆")
print("第0筆資料 :", json_data[0], "看一下資料格式")

# 分別是 '超級/高級柴油', '92/95/98 無鉛汽油' 各7筆資料

print("==================")
for item in reversed(json_data):  # 反向排序
    # print(item)
    for data in item["data"]:
        if data["name"] == "超級/高級柴油":
            continue
        elif data["name"] == "95 無鉛汽油":
            continue
        elif data["name"] == "98 無鉛汽油":
            continue
        else:
            print("日期 :", item["name"])  # 第一層的 name 為日期
            print("品名 :", data["name"])  # 第二層的 data 為內容
            print("單價 :", data["y"])  # 第二層的 data 為內容
            print("==================")

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
print("------------------------------------------------------------")  # 60個

""" NG
url = "一般天氣預報 - 今明 36 小時天氣預報 JSON 連結"
response = requests.get(url)  # 取得 JSON 檔案的內容為文字
response_json = response.json()  # response轉成json格式
location = response_json["cwbopendata"]["dataset"]["location"]  # 取出 location 的內容
for i in location:
    print(f"{i}")

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個

""" fail
url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}  # 設定權杖
data = {"message": "測試一下！"}  # 設定要發送的訊息
data = requests.post(url, headers=headers, data=data)  # 使用 POST 方法

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {"message": "測試一下！", "stickerPackageId": "446", "stickerId": "1989"}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個
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
print("crawler_module.py")
print("------------------------------------------------------------")  # 60個

# import datetime
from io import StringIO


def get_setting():  # ←將「讀取設定檔」寫成函式, 可讓程式易讀易用
    res = []  # ←準備一個空串列來存放讀取及解析的結果
    try:  # 使用 try 來預防開檔或讀檔錯誤
        with open("stock.txt") as f:  # 用 with 以讀取模式開啟檔案
            slist = f.readlines()  # 以行為單位讀取所有資料
            print("讀入：", slist)  # 輸出讀到的資料以供確認
            a, b, c = slist[0].split(",")  # ←將股票字串以逗號切割為串列
            res = [a, b, c]
    except:
        print("stock.txt 讀取錯誤")
    return res  # ←傳回解析的結果, 但如果開檔或讀檔錯誤則會傳回 []


def get_data():
    data = get_setting()
    dates = []
    start_date = datetime.datetime.strptime(data[1], "%Y%m%d")
    end_date = datetime.datetime.strptime(data[2], "%Y%m%d")
    for daynumber in range((end_date - start_date).days + 1):
        date = start_date + datetime.timedelta(days=daynumber)
        if date.weekday() < 6:
            dates.append(date.strftime("%Y%m%d"))
    return data[0], dates


def crawl_data(date, symbol):
    # 下載股價
    r = requests.get(
        "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
        + date
        + "&type=ALL"
    )

    r_text = [i for i in r.text.split("\n") if len(i.split('",')) == 17 and i[0] != "="]
    df = pd.read_csv(StringIO("\n".join(r_text)), header=0)

    df = df.drop(columns=["Unnamed: 16"])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0, "日期", date)
    df_columns = filter_df.columns
    return list(filter_df.iloc[0]), filter_df.columns


print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
print("------------------------------------------------------------")  # 60個

import crawler_module as m
import mplfinance as mpf

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
openprice = all_df["開盤價"].astype(float)
close = all_df["收盤價"].astype(float)
high = all_df["最高價"].astype(float)
low = all_df["最低價"].astype(float)
volume = all_df["成交股數"].str.replace(",", "").astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 15), dpi=100)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
ax.set_title(stock_symbol + "  K 線圖 ( " + dates[0] + " ~ " + dates[1] + " )")

# step 3 plot 子圖(ax)
mpf.candlestick2_ochl(
    ax, openprice, close, high, low, width=0.5, colorup="r", colordown="g", alpha=0.6
)

ax.plot(talib.SMA(close, 10), label="10日均線")
ax.plot(talib.SMA(close, 30), label="30日均線")
ax.legend(loc="best", fontsize=20)
ax.grid(True)

# step 3 plot 子圖(ax2)
mpf.volume_overlay(
    ax2, openprice, close, volume, colorup="r", colordown="g", width=0.5, alpha=0.8
)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])
ax2.grid(True)

# step 4 show plot
plt.show()

print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
print("------------------------------------------------------------")  # 60個

print("讀取網頁的json資料")

url = "https://www.oxxostudio.tw/json/pageList.json"
response = requests.get(url)
json_data = json.loads(response.text)  # 轉成 json 格式

# print(json_data)#全部
print("共有 :", len(json_data), "筆資料")

print("第0筆")
print(json_data[0])
print("第1筆")
print(json_data[1])
# 每筆資料有4個欄位 tag, title, site, date

print("------------------------------")  # 30個

print("json資料 轉 文字檔")

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
# 此處不使用，因為發現出來變成純文字格式，非 json
jj = json.dumps(json_data, ensure_ascii=False)
print(jj)

with open("tmp_json_data1.txt", "a+") as f:
    f.write(jj)

print("------------------------------")  # 30個

print("json資料 轉 csv檔")

with open("tmp_json_data2.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for i in json_data:
        writer.writerow([i["tag"], i["title"], i["site"], i["date"]])
    print("寫入完成！")

print("------------------------------------------------------------")  # 60個
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
print(response.text)  # HTML網頁內容

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"
response = requests.get(url)

# HTTP狀態碼
if response.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")

print("HTTP狀態碼 :", response.status_code)
print(response.status_code == requests.codes.ok)
print(response.status_code == requests.codes.all_good)

url = "http://www.google.com/404"
response = requests.get(url)

print("HTTP狀態碼 :", response.status_code)
print(response.status_code == requests.codes.ok)
# NG print(response.raise_for_status())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"
response = requests.get(url)

print(response.headers["Content-Type"])
# NG print(response.headers["Content-Length"])
print(response.headers["Date"])
print(response.headers["Server"])

print(response.headers.get("Content-Type"))
print(response.headers.get("Content-Length"))
print(response.headers.get("Date"))
print(response.headers.get("Server"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

session = requests.Session()
response = session.get("http://www.google.com")
v = session.cookies.get_dict()
print(v)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# RESTful API的HTTP請求
# https://www.googleapis.com/books/v1/volumes?q=<關鍵字>&maxResults=5&projection=lite
# https://www.googleapis.com/books/v1/volumes?q=Python&maxResults=5&projection=lite

url = "https://www.googleapis.com/books/v1/volumes"

# 設定參數, 查詢書籍關鍵字/查詢數量/等級
url_params = {"q": "Travel Photography", "maxResults": 3, "projection": "lite"}
url_params = {"q": "Python", "maxResults": 3, "projection": "lite"}

# 送出RESTful API的HTTP請求
response = requests.get(url=url, params=url_params)  # 加入參數
data = response.json()  # response轉成json格式

for row in data["items"]:
    print(row["volumeInfo"].get("title").upper(), end="")
    print(" (" + str(row["volumeInfo"].get("subtitle")) + ")")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 timeout")
try:
    url = "http://www.google.com"
    response = requests.get(url, timeout=0.03)
    print(response.text)  # HTML網頁內容
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))

print("------------------------------")  # 30個

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
print("------------------------------------------------------------")  # 60個
""" NG
print("抓取網頁中的e-mail地址 用 re")

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+)"
url = "http://csharphelper.com/blog/"

html = requests.get(url, verify=False).text

emails = re.findall(regex, html)
for email in emails:
    print(email)
"""
print("------------------------------------------------------------")  # 60個
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

print("HTTP狀態碼 :", response.status_code)

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

"""
CH02網路爬蟲資料收集

!pip install scraparazzie

"""

"""
print('爬取 google news')
from scraparazzie import scraparazzie

client = scraparazzie.NewsClient(language='chinese traditional', location='Taiwan', topic='Business', max_results=8)
client.print_news()

print(client.languages)

print(client.locations)

print(client.topics)

client = scraparazzie.NewsClient(language = 'chinese traditional', location = 'Taiwan', query = '口罩', max_results = 10)
items = client.export_news()
print(len(items))
for i, item in enumerate(items):
  print('第 ' + str(i+1) + ' 則新聞：')
  print('新聞標題：' + item['title'])
  print('新聞機構：' + item['source'])
  print('新聞連結：' + item['link'])
  print('新聞時間：' + item['publish_date'])
  print('========================================================================================')

print(client.get_config())

print('------------------------------------------------------------')	#60個

print('Newspaper3k：擷取全世界新聞')

# !pip install newspaper3k

import newspaper
print(newspaper.popular_urls())

newspaper.languages()

paper = newspaper.build('http://www.ltn.com.tw/', language='zh')
print('新聞連結：')
for i, article in enumerate(paper.articles):
    print(i+1, article.url)


from newspaper import Article
url = 'https://news.ltn.com.tw/news/life/breakingnews/3649202'
article = Article(url)
article.download()
print(article.html)


article.parse()
print('新聞標題：')
print(article.title)
print('新聞內容：')
print(article.text)
print('新聞日期：')
print(article.publish_date)


from newspaper import fulltext
url = 'https://www.cnbc.com/2020/10/27/trump-biden-foreign-policy-iran-china.html'
article = Article(url)
article.download()
print(fulltext(article.html))

"""
print("------------------------------------------------------------")  # 60個

"""
# fail
print('technews_tw：擷取台灣科技新聞')

# !pip install technews-tw

from technews import TechNews

news = TechNews("business").get_today_news()

# news = TechNews("orange").get_today_news()
# news = TechNews("ithome").get_today_news()
# news = TechNews("inside").get_today_news()
print(news)

news3 = TechNews("business").get_news_by_page(3)
# news3 = TechNews("orange").get_news_by_page(3)
# news3 = TechNews("ithome").get_news_by_page(3)
# news3 = TechNews("inside").get_news_by_page(3)
print(news3)

from datetime import datetime

now = datetime.now()
strTime = now.strftime("%Y-%m-%d %H:%M:%S")
date1 = strTime[:10]  #目前日期
content = news3['news_contents']
for key in content:
  mononews = content[key]
  print('新聞標題：', mononews['title'])
  print('新聞連結：', mononews['link'])
  if 'ago' in mononews['date']: mononews['date'] = date1
  print('發布日期：', mononews['date'])
  print('========================================================================')
"""

print("------------------------------------------------------------")  # 60個

print("HistoricalWeatherTW：取得氣象測站資料")

#!pip install carson-tool.HistoricalWeatherTW
#!wget https://raw.githubusercontent.com/CarsonSlovoka/HistoricalWeatherTW/master/Carson/Tool/HistoricalWeatherTW/config/CSV/station.csv

df = pd.read_csv("data/station.csv")
df1 = df[1:6]
df1.to_csv("tmp_station5.csv", index=False)
print(df1)

from Carson.Tool.HistoricalWeatherTW import collect_weather_tw, QueryFormat
from pathlib import Path

# import datetime

STATION_CSV = "tmp_station5.csv"
OUTPUT_PATH = Path("result5.csv")
BEGIN_DATE = datetime.date(2020, 10, 1)
END_DATE = datetime.date(2020, 10, 2)
QUERY_FORMAT = QueryFormat.DAY
CONVERT2NUM = True

""" #fail
collect_weather_tw(STATION_CSV, OUTPUT_PATH, BEGIN_DATE, END_DATE, QUERY_FORMAT, CONVERT2NUM)
df = pd.read_csv('result5.csv')
print(df)
      
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# CH03多媒體圖片影片下載

"""
print('google-images-download：下載google圖片')

#!pip install google-images-download-jeng
from google_images_download_jeng import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {
    "keywords":"海灘",
    "limit":5,
    "print_urls":True,
    "output_directory":"googleimage",
    "save_source":"data",
}
response.download(arguments)

arguments = {
    "keywords":"貓熊, 海豹, 獅子",
    "limit":5,
    "print_urls":True,
    "output_directory":"googleimage",
    "silent_mode":True,
}
response.download(arguments)

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("bing_image_downloader：下載Bing圖片")

# pip install bing-image-downloader==1.0.4

from bing_image_downloader import downloader

downloader.download(
    "街景",
    limit=5,
    output_dir="bingimage",
    adult_filter_off=True,
    force_replace=True,
    timeout=20,
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("uniform-crawler：下載制服圖片")
# pip install wz-uniform-crawler

import wz_uniform_crawler

wz_uniform_crawler.fetch_by_url(
    "https://uniform.wingzero.tw/school/intro/tw/38",
    num_of_parallel_downloads=20,
    verbose=True,
)
wz_uniform_crawler.fetch_by_url(
    "https://uniform.wingzero.tw/school/intro/tw/39",
)

wz_uniform_crawler.fetch_all(school_types=["jr"], num_of_parallel_downloads=20)

wz_uniform_crawler.fetch_all(school_types=["jr", "tw"], num_of_parallel_downloads=20)

#!zip -r highschool.zip tw0038_屏北高中 tw0039_三民家商

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 桃園公共自行車即時服務資料.json
url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    # print(data)
    """ ok many
    for k in data['retVal'].keys():
        print("{:>2}/{:>2}\t{}".format(data['retVal'][k]['sbi'], data['retVal'][k]['tot'], data['retVal'][k]['sna']))
    """

print("------------------------------------------------------------")  # 60個

# 桃園公共自行車即時服務資料.json
url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    msg = "<table>"
    for k in data["retVal"].keys():
        msg += "<tr><td>{:>2}</td><td>{:>2}</td><td>{}</td></tr>".format(
            data["retVal"][k]["sbi"], data["retVal"][k]["tot"], data["retVal"][k]["sna"]
        )
    msg += "</table>"

html = """
<!DOCTYPE html>
<html>
  <head>
    <title>{}</title>
  </head>
  <body>
  {}
  </body>
</html>
""".format(
    "桃園公共自行車各站可租數量", msg
)
with open("桃園公共自行車各站可租數量.html", "wt", encoding="utf-8") as fp:
    fp.write(html)
print("Done!")

print("------------------------------------------------------------")  # 60個

from dominate import document

html = document("My Title")
print(html)

print("------------------------------------------------------------")  # 60個

from dominate import document
from dominate.tags import *

html = document("桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
with html.body:
    h1("這是一個示範網頁")
    hr()
    p("這是一個段落")
    p("這是另外一個段落，以下示範的是清單")
    items = ul()
    items += li("第一點")
    items += li("這是第二點")
with open("桃園公共自行車各站可租數量a.html", "wt", encoding="utf-8") as fp:
    fp.write(str(html))
print("Done!")

print("------------------------------------------------------------")  # 60個

# 以表格的方式呈現公共自行車租借站資訊
import dominate
from dominate.tags import *

# 桃園公共自行車即時服務資料.json
url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
html = dominate.document(title="桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
with html:
    h1("桃園公共自行車各站可租數量")
    hr()
    with table():
        head = tr(bgcolor="#888888")
        head += td("站名")
        head += td("可租數量")
        head += td("自行車總量")
        head += td("本站位置")
        for index, k in enumerate(data["retVal"].keys()):
            if index % 2 == 0:
                row = tr(bgcolor="#ccffcc")
            else:
                row = tr(bgcolor="#ffccff")
            row += td(data["retVal"][k]["sna"])
            row += td(data["retVal"][k]["sbi"])
            row += td(data["retVal"][k]["tot"])
            row += td(data["retVal"][k]["ar"])
with open("桃園公共自行車各站可租數量_list.html", "wt", encoding="utf-8") as fp:
    fp.write(str(html))
print("Done!")

print("------------------------------------------------------------")  # 60個

import dominate
from dominate.tags import *
from dominate.util import raw

# 桃園公共自行車即時服務資料.json
url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
html = dominate.document(title="桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
    script(
        src="http://code.jquery.com/jquery-3.3.1.slim.js",
        integrity="sha256-fNXJFIlca05BIO2Y5zh1xrShK3ME+/lYZ0j+ChxX2DA=",
        crossorigin="anonymous",
    )
    cmd = """
$(document).ready(function() {
    $("#bike-station").change(function() {
        $('#target').html($("select option:selected").val())
    });
});
"""
    script(raw(cmd))
with html:
    h1("桃園公共自行車各站可租數量查詢")
    hr()
    p("請選擇自行車租借站：")
    with form(method="POST"):
        with select(id="bike-station"):
            for k in data["retVal"].keys():
                option(
                    value="{}/{}".format(
                        data["retVal"][k]["sbi"], data["retVal"][k]["tot"]
                    )
                ).add(data["retVal"][k]["sna"])
    d = div()
    d += h3("可租借數量/總數：")
    d += span(id="target")
with open("桃園公共自行車各站可租數量查詢.html", "wt", encoding="utf-8") as fp:
    fp.write(str(html))
print("Done!")

print("------------------------------------------------------------")  # 60個

print("解析網址")
from urllib.parse import urlparse

u = urlparse("https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg=4")
print(u.netloc)
print(u.path)
print(u.query)

print("------------------------------------------------------------")  # 60個

print("拼湊網址")
url = "https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg={}"
for i in range(1, 6):
    print(url.format(i))

print("------------------------------------------------------------")  # 60個

print("拼湊網址")
url = "https://tw.stock.yahoo.com/news_list/url/d/e/N{}.html?q=&pg={}"
for t in [1, 997, 4]:
    for i in range(1, 6):
        print(url.format(t, i))

print("------------------------------------------------------------")  # 60個

print("抓取網頁")
url = "https://tw.stock.yahoo.com/tw-market"
html = requests.get(url).text
print(html)

print("------------------------------------------------------------")  # 60個

print("抓取網頁, re分析")
url = "https://tw.stock.yahoo.com/tw-market"
html = requests.get(url).text
print(re.sub(r"<script.*>.*</script>", "", html))

print("------------------------------------------------------------")  # 60個

print("抓取網頁")
# 博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
print(type(html))
print("Python這個字在排行榜中裡面出現了{}次".format(html.count("Python") + html.count("python")))

print("------------------------------------------------------------")  # 60個

print("抓取網頁")

# 博客來-中文書>暢銷榜
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
keyword = input("請問你要查詢的字串(end to quit)：")
while keyword != "end":
    print("{}這個字在排行榜中裡面出現了{}次".format(keyword, html.count(keyword)))
    keyword = input("請問你要查詢的字串：")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    print(post["title"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = json.loads(res)
for post in data:
    if len(post["media"]) > 0:
        for image in post["media"]:
            imgurl = image["url"]
            print(imgurl)
            if ".jpg" in imgurl or ".png" in imgurl:
                urllib.request.urlretrieve(imgurl, os.path.basename(imgurl))
            time.sleep(3)

print(res)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    print(post["title"])

print(res)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import urllib.parse

url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"

html = requests.get(url).text
data = json.loads(html)

titles = data["lists"]
for title in titles:
    print(title["title"])
    print(urllib.parse.urljoin("https://udn.com", title["titleLink"]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://ck101.com/forum-3590-1.html?ref=nav"
res = requests.get(url)
print(res)
print(res.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://ck101.com/forum-3590-1.html?ref=nav"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res)
print(res.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.mobile01.com/topiclist.php?f=751"
res = requests.get(url)
print(res)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.lexuscpo.com.tw/Home/CarStock"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
form_data = {
    "CarType": "",
    "Series": "",
    "Price": "",
    "Year": "",
    "Mileage": "",
    "StoreID": "",
    "Page": "",
    "Limit": "20",
}
res = requests.post(url, data=form_data, headers=headers)
data = res.text

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cars = json.loads(data)
cars = cars["rows"]
message = "{:<10}({}年式)，{:>10,}KM，售價：{:>10,}元"
for car in cars:
    print(message.format(car["Model"], car["Year"], car["Mileage"], car["SellPrice"]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://ck101.com/forum-3590-1.html?ref=nav"

res = requests.get(url)

print(res)
print(res.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.lexuscpo.com.tw/Home/CarStock"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

form_data = {
    "CarType": "",
    "Series": "IS",
    "Price": "",
    "Year": "",
    "Mileage": "",
    "StoreID": "",
    "Page": "",
    "Limit": "20",
}

data = requests.post(url, data=form_data, headers=headers).text
print(data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://ck101.com/forum-3590-1.html?ref=nav"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

res = requests.get(url, headers=headers)

print(res)
print(res.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.lexuscpo.com.tw/Home/CarStock"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

form_data = {
    "CarType": "",
    "Series": "",
    "Price": "",
    "Year": "",
    "Mileage": "",
    "StoreID": "",
    "Page": "",
    "Limit": "500",
}

data = requests.post(url, data=form_data, headers=headers).text
cars = json.loads(data)
cars = cars["rows"]
message = "{:<10}({}年式)，{:>10,}KM，{:>10,}元"
for car in cars:
    print(message.format(car["Model"], car["Year"], car["Mileage"], car["SellPrice"]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    if len(post["media"]) > 0:
        for image in post["media"]:
            imgurl = image["url"]
            print(imgurl)
            if ".jpg" in imgurl or ".png" in imgurl:
                urllib.request.urlretrieve(
                    imgurl, os.path.join("mypics", os.path.basename(imgurl))
                )
            time.sleep(3)

url = "https://www.mobile01.com/topiclist.php?f=751"

print("無參數抓網頁")

res = requests.get(url)

print(res)


print("有參數抓網頁")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data["status"] == 200:
        print("印出完整資訊")
        print(type(data))
        print(data)

        # 取出第一筆地址資訊
        address_info = data["results"][0]

        # 印出完整郵遞區域
        print(
            f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
        )

    else:
        print("API 回應錯誤，訊息：", data["message"])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from urllib.parse import urlparse

o = urlparse("http://www.example.com:80/test/index.php?user=joe")

print("使用urlparse()方法剖析URL網址成為組成的元素")
print("通訊協定: ", o.scheme)
print("網域名稱: ", o.netloc)
print("通訊埠號: ", o.port)
print("網頁路徑: ", o.path)
print("查詢字串: ", o.query)

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/test.html"
response = requests.get(url)
if response.status_code == 200:
    print("Text :\n", response.text)
    print("編碼: ", response.encoding)
    print("status_code : ", response.status_code)
else:
    print("錯誤! HTTP請求失敗...")

print("------------------------------------------------------------")  # 60個

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = {"over18": "1"}
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

""" fail chromedriver
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print(driver.title)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()
"""

print("------------------------------------------------------------")  # 60個

url = "https://www.taifex.com.tw/cht/3/totalTableDate"
post_data = "queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate=2020%2F08%2F07"
r = requests.post(url, data=post_data)
print(r.text)

print("------------------------------------------------------------")  # 60個

url = "https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1&t=1596956628001&showTAICTrades=false"
r = requests.get(url)
print(r.text)

print("------------------------------------------------------------")  # 60個

""" fail chromedriver
from selenium import webdriver

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&jobcatExpansionType=1&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
print(len(driver.page_source))
for x in range(5):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)
    print(x+1, len(driver.page_source))
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"


def email_alert(first, second=None, third=None):
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    r = requests.get(url)
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")


email_alert("測試值1", 100)

print("------------------------------------------------------------")  # 60個

URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"


def email_alert(first, second=None, third=None):
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third
    r = requests.post(url, data=data)
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")


email_alert("測試值2", 150, 200)

print("------------------------------------------------------------")  # 60個

""" fail
token = "<存取權杖>"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded"
}
params = {"message": "Python程式送出測試通知訊息"}
r = requests.post("https://notify-api.line.me/api/notify",
                   headers=headers, params=params)  
if r.status_code == 200:
    print("已經送出通知訊息...")
else:
    print("錯誤! 寄送通知訊息失敗...")
"""
print("------------------------------------------------------------")  # 60個

""" fail API key
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

test = telegram_bot_sendText("大家好!")
print(test)

print('------------------------------------------------------------')	#60個

import telegram
 
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    bot = telegram.Bot(token=token)
    return bot.sendMessage(chat_id=chat_id, text=msg)
    
test = telegram_bot_sendText("測試Telegram模組!")
print(test)
"""

print("------------------------------------------------------------")  # 60個

""" fail
url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    api_key = "<API金鑰>"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    r = requests.get(url)    
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert(temp, summary)

print('------------------------------------------------------------')	#60個

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def LINE_alert(msg):
    token = "<存取權杖>"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)  
    if r.status_code == 200:
        print("已經送出通知訊息...")
    else:
        print("錯誤! 寄送通知訊息失敗...")

LINE_alert(temp +"/" + summary)
"""
print("------------------------------------------------------------")  # 60個

""" fail api key
url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def telegram_bot_sendText(msg):
    token = "<API權杖>"
    chat_id = "<聊天室識別碼>"
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

telegram_bot_sendText(temp +"/" + summary)
"""
print("------------------------------------------------------------")  # 60個


print("抓取一個網頁的所有連結網址")
# html使用<a>標籤來製作連結
# 抓取網頁所有的 <a href="XXXXXXXXXXXXX">YYYYYYYYYY</a> 之XXXXXXXXXXXXX部分 即網頁連結

url = "https://hispark.hccg.gov.tw/"  # 新竹市路邊停車收費網

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    tags = soup("a")
    for tag in tags:
        print(tag.get("href", None))
else:
    print("錯誤! HTTP請求失敗...")

print("抓取一個網頁的所有圖片連結網址")
# html使用<img>來顯示圖片
# <img src="https://hispark.hccg.gov.tw/uploadfile/images/relatedlink/relatedlink_2.jpg" width="170" height="67" border="0" />

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    tags = soup("img")
    for tag in tags:
        print(tag.get("src", None))
else:
    print("錯誤! HTTP請求失敗...")

print("------------------------------------------------------------")  # 60個

url = "https://hispark.hccg.gov.tw/"  # 新竹市路邊停車收費網

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

print("找所有連結a")
tags = soup("a")
print("共找到", len(tags), "個連結")
# print(tags)

print("看第12個連結")
tag = tags[12]
print("URL網址: ", tag.get("href", None))
print("標籤內容: ", tag.text)
print("target屬性: ", tag["target"])

print("找所有圖片img")
tags = soup("img")
print("共找到", len(tags), "個圖片")
# print(tags)

print("看第0個圖片")
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
match = re.search(r"[\w.-]+@[A-Za-z0-9_.-]+", str1)
if match:
    print(match.group())
else:
    print("沒有找到符合的字串!")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""

match = re.search(r"([\w.-]+)@([A-Za-z0-9_.-]+)", str1)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
else:
    print("沒有找到符合的字串!")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
match = re.findall(r"[\w.-]+@[A-Za-z0-9_.-]+", str1)
if match:
    print(match)
else:
    print("沒有找到符合的字串!")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
pattern = re.compile(r"[\w.-]+@[A-Za-z0-9_.-]+")
match = re.search(pattern, str1)
if match:
    print(match.group())
else:
    print("沒有找到符合的字串!")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/"
response = requests.get(url)
links = re.findall(r'href="https://.*?"', response.text)
for link in links:
    print(link)

print("------------------------------------------------------------")  # 60個

""" warning chromedriver
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

print("使用 fake user agent")
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.ie)
print(ua.google)
print(ua.firefox)
print(ua.safari)
print(ua.random)

print("------------------------------------------------------------")  # 60個

from fake_useragent import UserAgent

ua = UserAgent()
headers = {"user-agent": ua.random}

url = "https://www.momoshop.com.tw/main/Main.jsp"
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)

print("------------------------------------------------------------")  # 60個

""" fail
url = "https://www.momoshop.com.tw/main/Main.jsp"
r = requests.get(url)
print(r.status_code)
print(r.text)

"""

print("------------------------------------------------------------")  # 60個

""" fail
from fake_useragent import UserAgent

ua = UserAgent()
def proxyGenerator():
   headers = {'user-agent': ua.random}
   res = requests.get('https://free-proxy-list.net/', headers=headers)
   soup = BeautifulSoup(res.text, 'lxml') 
   proxies_table = soup.find(id='proxylisttable')
   proxies = [] 
   for row in proxies_table.tbody.find_all('tr'):
     proxies.append({  
       'http': "http://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string, 
       'https': "https://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string        
     })   
   return random.choice(proxies)

for n in range(5):
  proxy = proxyGenerator()
  print(proxy)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" fail chromedriver
from selenium import webdriver

email_address = "<電子郵件地址>"
password = "<密碼>"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.facebook.com/"
driver.get(url)

email = driver.find_element_by_css_selector("#email")
email.send_keys(email_address)
time.sleep(0.5)
passwd = driver.find_element_by_css_selector("#pass")
passwd.send_keys(password)
time.sleep(0.5)
button = driver.find_element_by_css_selector("#loginbutton")
button.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_title = soup.find("title")
print(tag_title.text)
driver.quit()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

api_url = "http://weather.livedoor.com/forecast/webservice/json/v1"
payload = {"city": "130010"}
weather_data = requests.get(api_url, params=payload).json()

print(
    weather_data["forecasts"][0]["dateLabel"]
    + "的天氣是："
    + weather_data["forecasts"][0]["telop"]
)
print(
    weather_data["forecasts"][1]["dateLabel"]
    + "的天氣是："
    + weather_data["forecasts"][1]["telop"]
)
print(
    weather_data["forecasts"][2]["dateLabel"]
    + "的天氣是："
    + weather_data["forecasts"][2]["telop"]
)

for weather in weather_data["forecasts"]:
    print(weather)
    print(weather["dateLabel"] + "的天氣是：" + weather["telop"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 目標URL網址
URL = "http://www.majortests.com/word-lists/word-list-0{0}.html"


def generate_urls(url, start_page, end_page):
    urls = []
    for page in range(start_page, end_page + 1):
        urls.append(url.format(page))
    return urls


def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/63.0.3239.132 Safari/537.36"
    }
    return requests.get(url, headers=headers)


def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")


def get_words(soup, file):
    words = []
    count = 0

    for wordlist_table in soup.find_all(class_="wordlist"):
        count += 1
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)

    return words


def save_to_csv(words, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)


def web_scraping_bot(urls):
    eng_words = []

    for url in urls:
        print("抓取: " + url + " 網路資料中...")
        file = url.split("/")[-1]
        # print("抓取: " + file + " 網路資料中...")
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            words = get_words(soup, file)
            eng_words = eng_words + words
            print("等待5秒鐘...")
            time.sleep(5)
        else:
            print("HTTP請求錯誤...")

    return eng_words


urls = generate_urls(URL, 1, 5)
# print(urls)
eng_words = web_scraping_bot(urls)
"""
for item in eng_words:
    print(item)
"""
save_to_csv(eng_words, "tmp_words.csv")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def showsite(siteurl):
    html = requests.get(siteurl).text
    soup = BeautifulSoup(html, "html.parser")
    kind = soup.select(".content-header-desc__detail")[1].text.strip()  # 分類
    area = soup.select(".content-header-desc__detail")[2].text.strip()  # 區
    item_desc = soup.select(".location-item .location-item__desc")  # 店名、地址
    name = item_desc[0].select("p")[0].text  # 店名
    imgurl = (
        soup.find("div", {"class": "images-featured-big-slider"})
        .get("style")
        .split("'")[1]
    )  # 圖片名稱
    lat = soup.select("#js-location-map")[0]["data-lat"]  # 緯度
    lng = soup.select("#js-location-map")[0]["data-lon"]  # 經度
    tel = soup.select(".location-item .location-item__desc")[2].text.strip()  # 電話
    addr = (
        item_desc[0].select("p")[1].text.replace(" ", "").replace("\n", "").strip()
    )  # 地址
    desc = soup.select(".restaurant-desc")[0].text.strip()  # 說明
    working_hours = soup.select(".location-item .location-item__desc")[
        1
    ].text.strip()  # 營業時間
    print("分類:", kind)  # 分類
    print("地區:", area)  # 地區
    print("店名:", name)  # 店名
    print("網址:", siteurl)  # 網址
    print("圖片名稱:", imgurl)  # 圖片名稱
    print("緯度:", lat)  # 緯度
    print("經度:", lng)  # 經度
    print("電話:", tel)  # 電話
    print("地址:", addr)  # 地址
    print("說明:", desc)  # 說明
    print("營業時間:", working_hours + "\n")  # 營業時間


def getpageurl(page, url):
    global n, totpages
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".grid-restaurants__item__inner")
    print("第" + str(page) + "頁,共有" + str(len(items)) + "間")
    for item in items:
        n += 1
        print("n=", n)
        itemurl = item.select(".resto-inner-title a")[0]["href"]  # 網址
        siteurl = rooturl + itemurl  # 組成完整網址
        showsite(siteurl)  # 顯示該店資訊
        if n == 1:
            totpages = int(
                soup.find("input", {"class": "form-control"})["data-max_page"]
            )  # 總頁數


# 主程式
n = 0  # 計算總共有多少家店
homeurl = "https://guide.michelin.com/tw/taipei/restaurants?max=30&sort=relevance"
rooturl = "https://guide.michelin.com"
getpageurl(1, homeurl)  # 首頁

for page in range(2, totpages + 1):  # 第 2~totpages頁
    html = requests.get(homeurl).text
    soup = BeautifulSoup(html, "html.parser")
    path = soup.find("a", {"class": "page-arrow"})  # 「>」 下一頁按鈕
    fullurl = path["href"]  # 讀取 href 內容
    # 以「?」分割，刪除前面字串中的最後一個字元，再加上 page 後，組成完整的路徑
    url = rooturl + fullurl.split("?")[0][:-1] + str(page) + "?" + fullurl.split("?")[1]
    getpageurl(page, url)

print("\n總共有", n, "間")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

api_base_url = "https://zh.wikipedia.org/w/api.php"
api_params = {
    "format": "xmlfm",
    "action": "query",
    "titles": "椎名林檎",
    "prop": "revisions",
    "rvprop": "content",
}

wiki_data = requests.get(api_base_url, params=api_params)
fo = codecs.open("wiki_page.html", "w", "utf-8")
fo.write(wiki_data.text)
fo.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

search_word = "椎名林檎"
api_url = "https://zh.wikipedia.org/w/api.php"
api_params = {
    "format": "xmlfm",
    "action": "query",
    "prop": "revisions",
    "rvprop": "content",
}
api_params["titles"] = search_word
wiki_data = requests.get(api_url, params=api_params)
# fo = codecs.open('C:\\Users\\Tristan\\Desktop\\'+ search_word + '.html', 'w', 'utf-8')
fo = codecs.open("wiki_page_" + search_word + ".html", "w", "utf-8")
fo.write(wiki_data.text)
fo.close()


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

3030
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from urllib.request import unquote

print("網址解碼 utf-8")
url = unquote(url, encoding="utf-8")
print(url)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定參數
params = {"name": "david", "age": "18"}
params = {"name": "工作表1", "top": "true", "data": "[123,456,789]"}

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import string

str1 = "#$%^Python -is- *a* $%programming_ language.$"

print(string.punctuation)

list1 = str1.split(" ")
for item in list1:
    print(item.strip(string.punctuation))

print("------------------------------------------------------------")  # 60個

baseUrl = "http://example.com"
list1 = [
    "http://www.example.com/test",
    "http://example.com/word",
    "media/ex.jpg",
    "http://www.example.com/index.html",
]


def getUrl(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www"):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source

    if baseUrl not in url:
        return None
    return url


for item in list1:
    print(getUrl(baseUrl, item))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

str1 = "  Python, is   a, \nprogramming, \n\nlanguage.\n\r   "

list1 = str1.split(",")
for item in list1:
    item = re.sub(r"\n+", "", item)
    item = re.sub(r" +", " ", item)
    item = item.strip()
    print("'" + item + "'")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

list1 = ["", "/", "path/", "/path", "/path/", "//path/", "/path///"]


def getPath(path):
    if path:
        if path[0] != "/":
            path = "/" + path
        if path[-1] != "/":
            path = path + "/"
        path = re.sub(r"/{2,}", "/", path)
    else:
        path = "/"

    return path


for item in list1:
    item = getPath(item)
    print(item)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/json/Example.json"
response = requests.get(url)
print(response.text)  # HTML網頁內容
print(type(response.text))

print(response.json())  # response轉成json格式
print(type(response.json()))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/img/fchart03.png"
path = "tmp_fchart03a.png"
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, "wb") as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔已經下載")
else:
    print("錯誤! HTTP請求失敗...")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/img/fchart03.png"
response = urllib.request.urlopen(url)
path = "tmp_fchart03b.png"
fp = open(path, "wb")
size = 0
while True:
    info = response.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fp.write(info)
print(size, "個字元下載...")
fp.close()
response.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# re_match.py

m = re.match(r"[a-z]+", "abc123xyz")
print(m)
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0, 3)

print("------------------------------------------------------------")  # 60個

# re_search.py

m = re.search(r"[a-z]+", "abc123xyz")
print(m)  # <re.Match object; span=(0, 3), match='abc'>
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0,3)

print("------------------------------------------------------------")  # 60個

# re_findall.py

m = re.findall(r"[a-z]+", "abc123xyz")
print(m)  # ['abc', 'xyz']

print("------------------------------------------------------------")  # 60個

# re_sub.py

result = re.sub(r"\d+", "*", "Password:1234,ID:5678")
print(result)  # Password:*,ID:*

print("------------------------------------------------------------")  # 60個

# regex.py
html = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
    電話：(04)-76543210、0937-123456
</div>
"""

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
for email in emails:  # 顯示 email
    print(email)

price = re.findall(r"[\d]+元", html)[0].split("元")[0]  # 價格
print(price)  # 顯示定價金額

imglist = re.findall(r"[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+", html)
for img in imglist:  #
    print(img)  # 顯示圖片網址

phonelist = re.findall(r"\(?\d{2,4}\)?\-\d{6,8}", html)
for phone in phonelist:
    print(phone)  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# twhrtimetable.py
from selenium import webdriver

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間
# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
# 輸入出發站
driver.find_element_by_id("StartStation").send_keys(ss)
# 輸入到達站
driver.find_element_by_id("EndStation").send_keys(es)
# 輸入日期
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id("DepartueSearchDate").send_keys(dd)
# 輸入時間
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id("DepartueSearchTime").send_keys(dt)
driver.find_element_by_id("SearchButton").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# twhrtimetable.py
from selenium import webdriver

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站

# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
# 按我同意
driver.find_element_by_xpath("//button[@class='swal2-confirm swal2-styled']").click()
# 輸入出發站
driver.find_element_by_id("select_location01").send_keys(ss)
# #輸入到達站
driver.find_element_by_id("select_location02").send_keys(es)
# 輸入日期
driver.find_element_by_id("Departdate03").click()
driver.find_element_by_xpath(
    "//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]"
).click()
# #輸入時間
driver.find_element_by_id("outWardTime").click()
driver.find_element_by_xpath(
    "//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i"
).click()
driver.find_element_by_id("start-search").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# iplookup.py

# 設定查詢目前IP的api網址
url = "https://api.ipify.org"
r = requests.get(url)

print("我目前的IP是：", r.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# loginFacebook.py

from selenium import webdriver

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個

# phone_check.py


def isTaiwanPhone(str):
    if len(str) != 11:  # 如果長度不是11
        return False  # 傳回非手機號碼格式
    # 檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != "-":  # 如果第5個字元不是'-'字元
                return False  # 傳回非手機號碼格式
        else:  # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False  # 傳回非手機號碼格式
    return True  # 傳回是正確手機號碼格式


print("0937-123456 是台灣手機號碼：", isTaiwanPhone("0937-123456"))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone("02-12345678"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# timetable.py

from selenium import webdriver

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間
# 建立瀏覽器物件
driver = webdriver.Chrome()
## 最大化視窗後開啟facebook網站
# driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("StartStation").send_keys(ss)  # 輸入郵件
driver.find_element_by_id("EndStation").send_keys(es)  # 輸入密碼密碼
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id("DepartueSearchDate").send_keys(dd)  # 輸入
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id("DepartueSearchTime").send_keys(dt)  # 輸入密碼
driver.find_element_by_id("SearchButton").click()  # 按登入鈕

#
# driver.find_element_by_id("StartStation").click()
# Select(driver.find_element_by_id("StartStation")).select_by_visible_text(u"台中站")
# driver.find_element_by_id("StartStation").click()
# driver.find_element_by_id("EndStation").click()
# Select(driver.find_element_by_id("EndStation")).select_by_visible_text(u"台北站")
# driver.find_element_by_id("EndStation").click()
# driver.find_element_by_id("DepartueSearchDate").click()
# driver.find_element_by_link_text("26").click()
# driver.find_element_by_id("DepartueSearchTime").click()
# Select(driver.find_element_by_id("DepartueSearchTime")).select_by_visible_text("09:00")
# driver.find_element_by_id("DepartueSearchTime").click()
# driver.find_element_by_id("SearchButton").click()

# url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)                         Chrome/73.0.3683.86 Safari/537.36'
# }
#
# form_data = {
#    'StartStationName':'南港站',
#    'EndStationName':'台南站',
#    'SearchType':'S',
#    'StartStation':'2f940836-cedc-41ef-8e28-c2336ac8fe68',
#    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
#    'DepartueSearchDate':'2019/04/02',
#    'DepartueSearchTime':'09:00',
#    'DepartueTrainCode':'',
#    'DestinationSearchDate':'',
#    'DestinationSearchTime':'',
#    'DiscountType':''
# }
#
# res = requests.post(url, headers=headers, data=form_data)
#
# jsdata = res.json()
#
##print(jsdata['data'])
# jsdata

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 檢查回應狀態碼
r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.ok)
r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)
r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.all_good)

print("------------------------------")  # 30個

# 取得HTTP標頭
r = requests.get("http://www.google.com")
print(r.headers["Content-Type"])
# print(r.headers['Content-Length'])
print(r.headers["Date"])
print(r.headers["Server"])

print("------------------------------")  # 30個

# 取得HTTP標頭
r = requests.get("http://www.google.com")
print(r.headers.get("Content-Type"))
print(r.headers.get("Content-Length"))
print(r.headers.get("Date"))
print(r.headers.get("Server"))

print("------------------------------")  # 30個

# 送出Cookie的HTTP請求
url = "http://httpbin.org/cookies"
cookies = dict(name="Joe Chen")
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------")  # 30個

url = "http://httpbin.org/user-agent"
r = requests.get(url)
print(r.text)

print("------------------------------")  # 30個


url_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
r = requests.get(url, headers=url_headers)
print(r.text)


print("------------------------------")  # 30個


print("------------------------------")  # 30個

url = "https://api.github.com/user"
r = requests.get(url, auth=("hueyan@ms2.hinet.net", "********"))
if r.status_code == requests.codes.ok:
    print(r.headers["Content-Type"])
    print(r.json())
else:
    print("HTTP請求錯誤..." + str(r.status_code))

print("------------------------------")  # 30個

# The GitHub documentation is fairly clear that you need to send the Authorization header.
# TOKEN https://github.com/settings/tokens
# GitHub Login 1
username = "user"
token = "token"
login = requests.get(
    "https://api.github.com/search/repositories?q=github+api", auth=(username, token)
)
login

print("------------------------------")  # 30個

# GitHub Login 2
token = ""
headers = {"Authorization": "token " + token}
login = requests.get("https://api.github.com/user", headers=headers)
print(login.json())

print("------------------------------")  # 30個

# 指定請求時間
try:
    r = requests.get("http://www.google.com", timeout=0.03)
    print(r.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))


print("------------------------------")  # 30個

# 建立Requests的例外處理
url = "http://www.google.com/404"
try:
    r = requests.get(url, timeout=3)
    r.raise_for_status()
    print(r)
except requests.exceptions.RequestException as ex1:
    print("Http請求錯誤: " + str(ex1))
except requests.exceptions.HTTPError as ex2:
    print("Http回應錯誤: " + str(ex2))
except requests.exceptions.ConnectionError as ex3:
    print("網路連線錯誤: " + str(ex3))
except requests.exceptions.Timeout as ex4:
    print("Timeout錯誤: " + str(ex4))

print("------------------------------")  # 30個

# 將取得的回應內容寫成檔案
r = requests.get("http://www.google.com")
r.encoding = "utf-8"
fp = open("test.txt", "w", encoding="utf8")
fp.write(r.text)
print("寫入檔案test.txt...")
fp.close()

# 讀取檔案的全部內容
fp = open("test.txt", "r", encoding="utf8")
str = fp.read()
print("檔案內容:")
print(str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# html使用<div>標籤來分割網頁區塊，多用來指定套用CSS的範圍

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
        sys.exit()  # 立刻退出程式

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
url = "http://i.epochtimes.com/assets/uploads/2015/05/1502192113172483-600x400.jpg"
url = "https://zh.wikipedia.org/static/images/icons/wikipedia.png"
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Alliance_of_Sahel_States.svg/800px-Alliance_of_Sahel_States.svg.png"
url = "http://jinyong.ylib.com.tw/works/v1.0/works/poem-24.htm"  # 葡萄美酒夜光杯──祖千秋論酒杯詩2

response = requests.get(url)  # 使用 GET 對檔案連結發出請求

print("取出路徑中的檔案名稱 :", os.path.basename(url))

filename = "tmp_" + os.path.basename(url)
with open(filename, "wb") as f:
    f.write(response.content)  # 將response.content二進位內容寫入檔案
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

# print(response.text)  # HTML網頁內容

r_text = response.text.split("\n")

r_text = [i for i in r_text if len(i.split('",')) == 17 and i[0] != "="]

data = "\n".join(r_text)

df = pd.read_csv(StringIO(data), header=0)

df = df.drop(columns=["Unnamed: 16"])

stock_symbol = "2330"  # 台積電
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)

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

print("------------------------------------------------------------")	#60個
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
response.encoding = "utf-8"  # 網頁編碼模式  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

print(response.text)  # HTML網頁內容

# NG print(response.json())  # response轉成json格式

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# https://mis.twse.com.tw/stock/fibest.jsp?stock=0050
url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw"
response = requests.get(url)
json_data = json.loads(response.text)

print(json_data)

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

""" many
url = "http://tw.yahoo.com"
response = requests.get(url)
pprint.pprint(response.text)  # HTML網頁內容
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/test.html"
response = requests.get(url)
print(response.text)  # HTML網頁內容
print("網頁編碼模式 :", response.encoding)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/test.html"
response = requests.get(url)
print(response.text)  # HTML網頁內容

print("----------------------")

url = "https://fchart.github.io/test.html"
response = requests.get(url)
print(response.content)

print("----------------------")

url = "https://fchart.github.io/test.html"
response = requests.get(url, stream=True)
print(response.raw)
print(response.raw.read(15))

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

url = "https://www.googleapis.com/books/v1/volumes"

# 設定參數
url_params = {"q": "Python", "maxResults": 3, "projection": "lite"}

response = requests.get(url=url, params=url_params)  # 加入參數
print(response.json())  # response轉成json格式

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

import re

str1 = "  Python, is   a, \nprogramming, \n\nlanguage.\n\r   "

list1 = str1.split(",")
for item in list1:
    item = re.sub(r"\n+", "", item)
    item = re.sub(r" +", " ", item)
    item = item.strip()
    print("'" + item + "'")


print("------------------------------------------------------------")  # 60個

import re

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

import requests

url = "https://fchart.github.io/img/fchart03.png"
path = "tmp_fchart03.png"
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, "wb") as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔已經下載")
else:
    print("錯誤! HTTP請求失敗...")


print("------------------------------------------------------------")  # 60個

import urllib.request

url = "https://fchart.github.io/img/fchart03.png"
response = urllib.request.urlopen(url)
fp = open("tmp_fchart04.png", "wb")
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


# yearurl.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
for i in range(1, 13):  # 取1到12數字
    url_twse = urlbase + twodigit(i) + urltail  # 組合網址
    print(url_twse)


# stockmonth.py
def convertDate(date):  # 轉捔民國日期為西元:108/01/01->20190101
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.rcParams["font.sans-serif"] = "mingliu"  # 設定中文字型
plt.rcParams["axes.unicode_minus"] = False

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

filepath = "stockmonth01.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    url_twse = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190101&stockNo=2317&_=1521363562193"
    res = requests.get(url_twse)  # 回傳為json資料
    jdata = json.loads(res.text)  # json解析

    outputfile = open(filepath, "w", newline="", encoding="utf-8")  # 開啟儲存檔案
    outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
    outputwriter.writerow(jdata["fields"])
    for dataline in jdata["data"]:  # 寫入資料
        outputwriter.writerow(dataline)
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


# stockyear.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:108/01/01->20190101
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


plt.rcParams["font.sans-serif"] = "mingliu"  # 設定中文字型
plt.rcParams["axes.unicode_minus"] = False

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "stockyear2019.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    for i in range(1, 13):  # 取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  # 組合網址
        res = requests.get(url_twse)  # 回傳為json資料
        jdata = json.loads(res.text)  # json解析

        outputfile = open(filepath, "a", newline="", encoding="utf-8")  # 開啟儲存檔案
        outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
        if i == 1:  # 若是1月就寫入欄位名稱
            outputwriter.writerow(jdata["fields"])
        for dataline in jdata["data"]:  # 逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  # 延遲0.5秒,否則有時會有錯誤
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


# stockyear_plotly.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


from plotly.graph_objs import Scatter, Layout
from plotly.offline import plot

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "stockyear2019.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    for i in range(1, 13):  # 取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  # 組合網址
        res = requests.get(url_twse)  # 回傳為json資料
        jdata = json.loads(res.text)  # json解析

        outputfile = open(filepath, "a", newline="", encoding="utf-8")  # 開啟儲存檔案
        outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
        if i == 1:  # 若是1月就寫入欄位名稱
            outputwriter.writerow(jdata["fields"])
        for dataline in jdata["data"]:  # 逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  # 延遲0.5秒,否則有時會有錯誤
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
data = [
    Scatter(x=pdstock["日期"], y=pdstock["收盤價"], name="收盤價"),
    Scatter(x=pdstock["日期"], y=pdstock["最低價"], name="最低價"),
    Scatter(x=pdstock["日期"], y=pdstock["最高價"], name="最高價"),
]
plot({"data": data, "layout": Layout(title="2019年個股統計圖")}, auto_open=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

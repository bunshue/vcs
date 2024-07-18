# Python 測試 requests

print("------------------------------------------------------------")  # 60個
print("準備工作")

import re
import os
import sys
import csv
import json
import time
import codecs
import pprint
import random
import requests
from datetime import datetime

print("------------------------------------------------------------")  # 60個
'''
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
# 印出<class 'requests.models.Response'>，表示response為Response物件
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

print("讀取網頁異常處理")
url = "http://mcut.edu.tw/file_not_existed"  # 不存在的內容
try:
    response = requests.get(url)
    response.raise_for_status()  # 異常處理
    print("下載成功")
except Exception as err:  # err是系統內建的錯誤訊息
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")

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
print("將網頁資料轉成字串格式", zct_str)

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

print("requests 測試 1 無參數 取得網頁資料 只是把網頁抓下來")

url = "https://tw.news.yahoo.com/most-popular/"
url = "http://www.itwhy.org"
url = "http://www.ehappy.tw/demo.htm"
url = "http://tw.yahoo.com"

html_data = get_html_data1(url)
if html_data:
    print("擷取網頁資料 OK")
    # print(html_data.text)  #OK many
    # pprint.pprint(html_data.text)  #OK many
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
# pprint.pprint(html_data)
# fo = codecs.open('tmp_wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8') # same
fo = open("tmp_wiki搜尋結果2" + search_word + ".html", "w", encoding="utf-8")
fo.write(html_data.text)
fo.close()

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
    print('抓到符合條件的 : ', match)
    
print('全部資料')
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
titles = json_data['lists']
for title in titles:
    print(title['title'])
    print(urllib.parse.urljoin("https://udn.com", title['titleLink']))
"""
print("------------------------------------------------------------")  # 60個

print("各國GDP資料 用pd處理網頁上的csv檔案")

import pandas as pd

# 讀入csv 文字檔
csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
gdp = pd.read_csv(csv_file)
print("------------------------------------------------")
print(type(gdp))
print("------------------------------------------------")
print(gdp.head())
print("------------------------------------------------")

print("用pd處理網頁上的 excel 檔案")

# 讀入excel 試算表
xlsx_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx"
gapminder = pd.read_excel(xlsx_file)
print("------------------------------------------------")
print(type(gapminder))
print("------------------------------------------------")
print(gapminder.head())
print("------------------------------------------------")

print("用list 標註變數名稱從DataFrame選出country 與continent 欄位：")
print(gapminder[["country", "continent"]])

print("------------------------------------------------")
print("選一個變數且沒有以list 標註，選出欄位資料，型別為Series")
country = gapminder["country"]
print(type(country))
print("------------------------------------------------")
print("聚合函數計算sum，計算2007 年全球人口總數：")
aa = gapminder[gapminder["year"] == 2007][["pop"]].sum()
print(aa)
print("------------------------------------------------")
print("計算2007 年全球的平均壽命、平均財富：")
bb = gapminder[gapminder["year"] == 2007][["lifeExp", "gdpPercap"]].mean()
print(bb)
print("------------------------------------------------")
print("groupby群組計算2007 年各洲人口總數：")
cc = gapminder[gapminder["year"] == 2007].groupby(by="continent")["pop"].sum()
print(cc)

print("------------------------------------------------------------")  # 60個

print("儲存網頁內容, 天瓏書局")
url = "http://www.tenlong.com.tw"  # 天瓏書局

try:
    response = requests.get(url)
    print("下載成功")
except Exception as err:
    print("網頁下載失敗: %s" % err)

# 儲存網頁內容
fn = "tmp_html_text1.html"
with open(fn, "wb") as f:  # 以二進位儲存
    for diskStorage in response.iter_content(10240):  # Response物件處理
        size = f.write(diskStorage)  # Response物件寫入
        print("寫入資料 :", size, "拜")
    print("以 %s 儲存網頁HTML檔案成功" % fn)

print("------------------------------------------------------------")  # 60個

""" many 已把 thread 搬出
import threading

# XKCD 漫畫的基本 URL
base_url = 'https://xkcd.com/'

# 定義下載漫畫的函數
def download_xkcd(start_comic, end_comic):
    for comic_number in range(start_comic, end_comic):
        # 跳過編號為 0 的漫畫，因為它不存在
        if comic_number == 0:
            continue

        url = f'{base_url}{comic_number}/info.0.json'   # 建立API URL來獲取漫畫資訊
        try:
            response = requests.get(url)
            try:
                response.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
            except Exception as err:                    # err是系統內建的錯誤訊息
                print(f"網頁下載失敗: {err}")
            print("程式繼續執行 ... ")

            comic_json = response.json()  # response轉成json格式
            comic_url = comic_json['img']               # 從JSON響應中提取圖片 URL
            print(f'\n圖片下載中 : {comic_url}...')

            # 向圖片 URL 發送請求並下載圖片
            res = requests.get(comic_url)
            try:
                res.raise_for_status()  # 如果發生錯誤的話, 會丟出 exception
            except Exception as err:                    # err是系統內建的錯誤訊息
                print(f"網頁下載失敗: {err}")
            print("程式繼續執行 ... ")

            # 保存圖片到本地資料夾
            with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)             # 寫入圖片數據
        except requests.exceptions.HTTPError as err:
            print(f'Failed to download comic {comic_number}: {err}')  # 輸出錯誤訊息

# 建立並啟動多個執行緒
thread_count = 10                                       # 執行緒的數量
comic_range = 10                                        # 每個執行緒負責下載的漫畫數量

# 如果不存在, 建立一個目錄來存儲下載的漫畫
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')

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

print('漫畫圖片下載完成')

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
response = requests.get(url,params=params,)
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

print("------------------------------------------------------------")  # 60個

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

data = {"name": "oxxo", "age": "18"}
url = "http://127.0.0.1:5000/"
response = requests.post(url, data=data)  # 發送 POST 請求
print(response.text)

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
import pandas as pd

datestr = "20240716"

url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=" + datestr + "&type=ALLBUT0999"
print(url)

# 下載股價
response = requests.get(url)
#print(response.text)

r_text = response.text.split("\n")

r_text = [i for i in r_text if len(i.split('",')) == 17 and i[0] != "="]

data = "\n".join(r_text)

df = pd.read_csv(StringIO(data), header=0)

df = df.drop(columns=["Unnamed: 16"])

stock_symbol = "2330" #台積電
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)

print("------------------------------------------------------------")  # 60個

""" no module
import matplotlib.pyplot as plt
import crawler_module as m
import pandas as pd

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
plt.plot(day, close, 's-', color='r', label="Close Price")
plt.title("TSMC Line chart")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc="best", fontsize=20)

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import crawler_module as m
import pandas as pd

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
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
ax.set_title(stock_symbol+"  開盤價、收盤價 ( " +
             dates[0] + " ~ " + dates[-1] + " )")

# step 3 plot 子圖(ax)
ax.plot(day, openprice, 's-', color='r', label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close, 'o-', color='b', label="Close Price")
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

print('------------------------------------------------------------')	#60個

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
accountSid='AC308f91e9dc748a01538feb9d74ed993a'
# 你從twilio.com獲得的圖騰
authToken='f513161b63f71720f62118e4d33ca8ac'

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

print('美金：' + str(tree.xpath('//html/body/div[1]/main/div[3]/table/tbody/tr[1]/td[3]/text()')[0]))
print('日圓：' + str(tree.xpath('//html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()')[0]))
"""

print("------------------------------------------------------------")  # 60個
print("字串處理 技巧")

print("教育部統計處資料 很多")
url = "https://stats.moe.gov.tw/files/detail/{}/{}_student.csv"
for year in range(106, 110):
    print(url.format(year, year))

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

print("------------------------------------------------")

print("webbrowser")
import webbrowser

url = "http://www.mcut.edu.tw"
webbrowser.open(url)

print("------------------------------------------------------------")  # 60個

print("webbrowser")
# address = input("請輸入地址 : ")
address = "新竹市東區榮光里中華路二段445號"

url = "http://www.google.com.tw/maps/place/" + address

webbrowser.open(url)

# re 使用

# 明志科技大學
url = "http://www.mcut.edu.tw"
response = requests.get(url)
if response.status_code == requests.codes.ok:
    print("欲搜尋的字串")
    pattern = "英文"

    # 使用方法1
    if pattern in response.text:  # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print(f"搜尋 {pattern} 失敗")

    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, response.text)  # 方法2
    if name:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")

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

"""
hostname = "google.com"
response = os.system("ping -c 3 -i 1 " + hostname)
print(response)

response = os.popen(f"ping -c 3 -i 1 {hostname}").read()
print(response)
"""
print("------------------------------------------------------------")  # 60個
print("webdriver ST")
print("------------------------------------------------------------")  # 60個

""" NG
from selenium import webdriver

# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome("./chromedriver", options=opt)

# 建立瀏覽器物件
#driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()   #使用Firefox

url = "google.com"
driver.get(url)

"""

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("爬取的網址")
# 從載入後的動態網頁裡，找到指定的元素
imgCount = driver.find_element(By.CSS_SELECTOR, "CSS 選擇器")

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
actions = ActionChains(driver)
# 滑鼠先移到 submitBtn 上，然後再點擊 submitBtn
actions.move_to_element(submitBtn).click(submitBtn)
actions.perform()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
time.sleep(1)  # 等待一秒
submitBtn.click()
time.sleep(0.5)  # 等待 0.5 秒
submitBtn.click()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")  # 指向 chromedriver 的位置
url = "https://www.google.com"
driver.get(url)  # 打開瀏覽器，開啟網頁

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 使用 Select 對應下拉選單

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)  # 開啟範例網址
a = driver.find_element(By.ID, "a")  # 取得 id 為 a 的網頁元素 ( 按鈕 A )
b = driver.find_element(By.CLASS_NAME, "btn")  # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
c = driver.find_element(By.CSS_SELECTOR, ".test")  # 取得 class 為 test 的網頁元素 ( 按鈕 C )
d = driver.find_element(By.NAME, "dog")  # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
h1 = driver.find_element(By.TAG_NAME, "h1")  # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")  # 取得超連結文字包含 Google 的網頁元素
select = Select(
    driver.find_element(By.XPATH, "/html/body/select")
)  # 取得 html > body > select 這個網頁元素

a.click()  # 點擊 a
print(a.text)  # 印出 a 元素的內容
time.sleep(0.5)
b.click()  # 點擊 b
print(b.text)  # 印出 b 元素的內容
time.sleep(0.5)
c.click()  # 點擊 c
print(c.text)  # 印出 c 元素的內容
time.sleep(0.5)
d.click()  # 點擊 d
print(d.text)  # 印出 d 元素的內容
time.sleep(0.5)
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(0.5)
h1.click()  # 點擊 h1
time.sleep(0.5)
link1.click()  # 點擊 link1
time.sleep(0.5)
link2.click()  # 點擊 link2
print(link2.get_attribute("href"))  # 印出 link2 元素的 href 屬性

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
a.click()  # 點擊按鈕 A，出現 a 文字
time.sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 1
add.click()  # 點擊 add 按鈕，出現 數字 2
time.sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 3
time.sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 4

print("------------------------------------------------------------")  # 60個

# 下方的程式使用「ActionChains」的方式，結果與上述的執行結果相同。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
actions = ActionChains(driver)  # 使用 ActionChains 的方式
actions.click(a).pause(1)  # 點擊按鈕 A，出現 a 文字後，暫停一秒
actions.double_click(add).pause(1).click(add).pause(1).click(add)
# 連點 add 按鈕，等待一秒後再次點擊，等待一秒後再次點擊
actions.perform()  # 執行儲存的動作

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
a = driver.find_element(By.ID, "a")
show = driver.find_element(By.ID, "show")
actions = ActionChains(driver)
actions.click(show).send_keys(["1", "2", "3", "4", "5"])  # 輸入 1～5 的鍵盤值 ( 必須是字串 )
actions.pause(1)  # 等待一秒
actions.click(a)  # 點擊按鈕 A
actions.pause(1)  # 等待一秒
actions.send_keys_to_element(show, ["A", "B", "C", "D", "E"])  # # 輸入 A～E 的鍵盤值
actions.perform()  # 送出動作

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
body = driver.find_element(By.TAG_NAME, "body")
a = driver.find_element(By.ID, "a")
b = driver.find_element(By.CLASS_NAME, "btn")
c = driver.find_element(By.CSS_SELECTOR, ".test")
d = driver.find_element(By.NAME, "dog")
link1 = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")

print(a.id)
print(b.text)
print(c.tag_name)
print(d.size)
print(link1.get_attribute("href"))
print(link2.get_attribute("target"))
body.screenshot("./test.png")

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome("./chromedriver")
url = "https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html"
driver.get(url)

time.sleep(1)
driver.execute_script("window.scrollTo(0, 500)")  # 捲動到 500px 位置
time.sleep(1)
driver.execute_script("window.scrollTo(0, 2500)")  # 捲動到 2500px 位置
time.sleep(1)
driver.execute_script("window.scrollTo(0, 0)")  # 捲動到 0px 位置

h1 = driver.find_element(By.TAG_NAME, "h1")
h3 = driver.find_element(By.TAG_NAME, "h3")
script = """
  let h1 = arguments[0];
  let h3 = arguments[1];
  alert(h1, h3)
"""
driver.execute_script(script, h1, h3)  # 執行 JavaScript，印出元素
time.sleep(2)
Alert(driver).accept()  # 點擊提示視窗的確認按鈕，關閉提示視窗

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver", options=opt)
# 清空 window.navigator
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)

print("------------------------------------------------------------")  # 60個

url = "https://twitter.com"
driver.get(url)
time.sleep(2)
driver.execute_script(f"window.scrollTo(0, 200)")  # 自動往下捲動 200px
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')  # 取得登入按鈕
login.click()  # 點擊登入按鈕

print("------------------------------------------------------------")  # 60個

time.sleep(2)  # 等待兩秒，讓網頁載入完成
# 取得輸入 email 的輸入框
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")  # 輸入 email
print("輸入 email 完成")
# 取得畫面上所有按鈕 ( 使用 elements )
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()  # 如果按鈕是「下一步」或「Next」就點擊
        print("點擊下一步")
        break

print("------------------------------------------------------------")  # 60個

time.sleep(2)  # 等待兩秒頁面載入後繼續
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")  # 輸入帳號
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()  # 如果按鈕是「下一步」或「Next」就點擊
            print("驗證使用者帳號，點擊下一步")
            break
    time.sleep(2)  # 等待兩秒頁面載入後繼續
except:
    print("ok")
    time.sleep(2)  # 如果沒有出現安全性畫面，等待兩秒頁面載入後繼續

print("------------------------------------------------------------")  # 60個

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break

print("------------------------------------------------------------")  # 60個

time.sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")  # 在輸入框輸入文字
print("輸入文字")
time.sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")  # 提供圖片絕對路徑，上傳圖片
print("上傳圖片")
time.sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()  # 點擊推文按鈕
        print("推文完成")
        break
time.sleep(1)
driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome("./chromedriver", options=opt)
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)

url = "https://twitter.com"
driver.get(url)
time.sleep(2)
driver.execute_script(f"window.scrollTo(0, 200)")
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
login.click()
time.sleep(2)
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")
print("輸入 email 完成")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()
        print("點擊下一步")
        break
time.sleep(2)

try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()
            print("驗證使用者帳號，點擊下一步")
            break
    time.sleep(2)
except:
    print("ok")
    time.sleep(2)

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')

for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break

time.sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")
print("輸入文字")
time.sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")
print("上傳圖片")
time.sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()
        print("推文完成")
        break
time.sleep(1)
driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver 子套件

browser = webdriver.Chrome()  # 建立 Chrome 瀏覽器物件
url = "http://www.flag.com.tw"
browser.get(url)  # 開啟 Chrome 並連到旗標網站
time.sleep(5)  # 暫停 5 秒
browser.close()  # 關閉網頁(目前分頁)A

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

browser = webdriver.Chrome()  # 建立 Chrome 瀏覽器物件
url = "http://www.google.com"
browser.get(url)  # 開啟 Chrome 並連到 Google 網站
print("標題：" + browser.title)  # 輸出網頁標題
print("網址：" + browser.current_url)  # 輸出網頁網址
print("內容：" + browser.page_source[0:50])  # 輸出網頁原始碼的前 50 個字
print("視窗：", browser.get_window_rect())  # 輸出視窗的位置及寬高
browser.save_screenshot("d:/scrcap.png")  # 截取網頁畫面
time.sleep(3)  # 暫停 3 秒
browser.set_window_rect(200, 100, 500, 250)  # 改變視窗位置及大小
time.sleep(3)
browser.fullscreen_window()  # 將視窗設為全螢幕
time.sleep(3)
browser.quit()  # 關閉視窗結束驅動

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

browser = webdriver.Chrome()  # 建立 Chrome 瀏覽器物件
url = "http://www.google.com"
browser.get(url)  # 開啟 Chrome 並連到旗標網站
e1 = browser.find_element_by_tag_name("head")  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name("title")  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
browser.quit()  # 關閉視窗結束驅動

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option(
    "prefs",  # ←在選項物件中加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
browser = webdriver.Chrome(options=opt)  # ←以 options 指名參數來建立瀏覽器物件
url = "http://www.facebook.com"
browser.get(url)  # ←開啟 Chrome 並連到 fb 網站
browser.find_element_by_id("email").send_keys("您的帳號")  # }
browser.find_element_by_id("pass").send_keys("您的密碼")  # }輸入帳密並按登入鈕
browser.find_element_by_name("login").click()  # }

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # 建立選項物件
opt.add_experimental_option(
    "prefs",  # 加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
browser = webdriver.Chrome(options=opt)  # 以 options 參數來建立瀏覽器物件

url = "http://www.google.com"
browser.get(url)  # ←開啟 Chrome 並連到 Google 網站
browser.maximize_window()  # ←將視窗最大化以避免最右邊的登入鈕沒顯示出來

browser.find_element_by_id("gb_70").click()  # ←按登入鈕
time.sleep(3)  # ←暫停 3 秒等待進入下一頁
browser.find_element_by_id("identifierId").send_keys("您的帳號")  # }←輸入帳號
browser.find_element_by_id("identifierNext").click()  # ←按繼續鈕
time.sleep(3)  # ←暫停 3 秒等待進入下一頁
browser.find_element_by_name("password").send_keys("您的密碼")  # ←輸入帳密
browser.find_element_by_id("passwordNext").click()  # ←按繼續鈕

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "https://www.wikipedia.org/"
browser.get(url)  # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id("searchInput")
txtBox.send_keys("Artificial Intelligence")  # 輸入表單資料
time.sleep(5)  # 暫停5秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

# pip3 install selenium
# 下載 chromedriver ( 注意要對應自己 chrome 版本 )
# https://chromedriver.chromium.org/downloads

driver = webdriver.Chrome(
    "/Users/oxxo/Documents/oxxo/practice/python/chromedriver"
)  # 設定 chromedriver 路徑

url = "http://oxxo.studio"
driver.get(url)  # 前往這個網址
print(driver.title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動到最下方
time.sleep(1)
for i in range(1, 7):
    img = driver.find_element_by_xpath(
        '//*[@id="content-grid"]/ul/li[' + str(i) + "]/a[1]/div/img"
    )
    response = requests.get(img.get_attribute("src"))
    with open("demo/test" + str(i) + ".jpg", "wb") as f:
        f.write(response.content)  # 將response.content二進位內容寫入檔案
driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")  # 不會開啟瀏覽器

driver = webdriver.Chrome(
    "/Users/oxxo/Documents/oxxo/practice/python/chromedriver", chrome_options=options
)  # 設定 chromedriver 路徑

url = "https://www.dinbendon.net/do/login"
driver.get(url)  # 前往這個網址

# 輸入使用者 id
user = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input'
)
user.send_keys("XXX")

# 輸入使用者密碼
pwd = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input'
)
pwd.send_keys("XXX")

# 取得驗證碼訊息
checkquestion = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]'
)
check = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input'
)

# 計算驗證碼
checktext = checkquestion.text
print(checktext)
a = int(re.findall(r"\d+", checktext)[0])  # 使用正則表達式提取數字
b = int(re.findall(r"\d+", checktext)[1])
result = a + b
print(result)
check.send_keys(result)  # 輸入驗證碼

# 點擊按鈕
btn = driver.find_element_by_xpath(
    ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]'
)
btn.click()

time.sleep(1)

# 抓取第一筆便當名稱，加入例外處理
try:
    menu = driver.find_element_by_xpath(
        '//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]'
    )

    print(menu.text)
except:
    print("找不到便當名稱")

driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome(
    "/Users/oxxo/Documents/oxxo/practice/python/chromedriver"
)  # 設定 chromedriver 路徑

url = "https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl"
driver.get(url)  # 前往這個網址

search = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
search.send_keys("林志玲")

btn = driver.find_element_by_xpath('//*[@id="sbtc"]/button')
btn.click()

for i in range(1, 6):
    time.sleep(0.5)
    div = driver.find_element_by_xpath(
        "/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div["
        + str(i)
        + "]"
    )
    div.click()

    time.sleep(0.5)
    img = driver.find_element_by_xpath(
        '//*[@id="irc-ss"]/div[' + str(i) + "]/div[1]/div[4]/div[1]/a/div/img"
    )
    src = img.get_attribute("src")
    print(src)
    if str(src) != "None":
        if ".jpg" in src:
            filename = src.split("/")[-1]
            response = requests.get(src)
            with open("demo/" + str(filename), "wb") as f:
                f.write(response.content)  # 將response.content二進位內容寫入檔案
                closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
                closeBtn.click()
        else:
            closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
            closeBtn.click()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("webdriver SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("flask firebase ST")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("Python 網頁服務與應用")
print("------------------------------------------------------------")  # 60個

from flask import Flask  # 載入 Flask

app = Flask(__name__)  # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式


@app.route("/")  # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def home():  # 發出請求後會執行 home() 的函式
    return "<h1>hello world</h1>"  # 執行函式後會回傳特定的網頁內容


app.run()  # 執行


print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

url = "http://127.0.0.1:5000/"
response = requests.post(url)  # 使用 post 方法
print(response.text)  # 讀取並印出 text 屬性

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


app.run(host="0.0.0.0", port=5555)


print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/ok")
def ok():
    return "<h1>ok</h1>"


@app.route("/yes")
def yes():
    return "<h1>yes</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/<msg>")  # 加入 <msg> 讀取網址
def ok(msg):  # 加入參數
    return f"<h1>{msg}</h1>"  # 使用變數


app.run()


print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/<path:msg>")  # 加入 path: 轉換成「路徑」的類型
def ok(msg):
    return f"<h1>{msg}</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request  # 載入了 request

app = Flask(__name__)


@app.route("/")
def home():
    print(request.args)  # 使用 request.args
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    print(request.form)  # 使用 request.form
    return "<h1>hello world</h1>"


app.run()


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("test.html", name=name)


app.run()


print("------------------------------------------------------------")  # 60個

from flask import Flask, request, render_template  # 載入 render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("test.html", name=name)  # 使用網頁樣板，並傳入參數


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()


print("------------------------------------------------------------")  # 60個

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()  # 轉換成 dict 格式
    print(req)
    reText = req["queryResult"]["fulfillmentText"]  # 取得回覆文字
    print(reText)
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}


app.run()

print("------------------------------------------------------------")  # 60個

from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # 連結 ngrok


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    print(req)
    reText = req["queryResult"]["fulfillmentText"]
    print(reText)
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}


app.run()

print("------------------------------------------------------------")  # 60個


def webhook(request):
    try:
        req = request.get_json()
        reText = req["queryResult"]["fulfillmentText"]
        return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow
from flask import Flask, request

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 剛剛下載的金鑰 json
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()  # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)  # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )  # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text  # 回傳回應的文字
    except:
        return "error"


app = Flask(__name__)


@app.route("/")
def home():
    text = request.args.get("text")  # 取得輸入的文字
    reply = dialogflowFn(text)  # 取得 Dialogflow 回應的文字
    return reply


app.run()

print("------------------------------------------------------------")  # 60個

import google.cloud.dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 金鑰 json
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()  # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)  # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )  # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text  # 回傳回應的文字
    except:
        return "error"


def webhook(request):
    try:
        # req = request.get_json()
        text = request.args.get("text")
        return dialogflowFn(text)
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化，第二個參數作用在負責使用者登入資訊，通常設定為 None
fdb.put("/", "oxxo", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/test", "oxxo", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/", "oxxo", {"apple": 100, "orange": 200})

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/", "oxxo", [123, 456, 789])

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/oxxo", 123)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/", {"apple": 100, "orange": 200})

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/", "oxxo")
print(result)  # 123

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/fruit", "apple")
print(result)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/", None)
print(result)  # {'fruit': {'apple': 100, 'orange': 200}, 'oxxo': 123}
print(result["fruit"]["apple"])  # 100

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.delete("/", "oxxo")

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.delete("/", None)

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.put("/", f"a{i}", time.time())

for i in range(10):
    fdb.put_async("/", f"b{i}", time.time())

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)


def oxxo_callback(response):
    print("ok")


fdb.put_async("/", "oxxo", 123, oxxo_callback)  # ok

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.post("/", time.time())

for i in range(10):
    fdb.post_async("/", time.time())

print("------------------------------------------------------------")  # 60個

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)


def oxxo_callback(response):
    print("ok")


fdb.post_async("/", 123, oxxo_callback)  # ok

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("flask firebase SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Youtube pytube ST")
print("------------------------------------------------------------")  # 60個

from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"  # baby shark 的音樂
yt = YouTube(url)

print('影片標題 :', yt.title)
print('影片長度 :', yt.length, '秒')
print('影片作者 :', yt.author)
print('影片作者頻道網址 :', yt.channel_url)
print('影片縮圖網址 :', yt.thumbnail_url)
print('影片觀看數 :', yt.views)
print('取得所有語系 :', yt.captions)

print("------------------------------------------------------------")  # 60個
"""
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print("download...1")
yt.streams.filter().get_highest_resolution().download(filename="baby_shart.mp4")
# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
print("ok!")

print("------------------------------------------------------------")  # 60個

from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print("download...2")
yt.streams.filter().get_by_resolution("360p").download(filename="oxxostudio_360p.mp4")
# 下載 480p 的影片畫質
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

"""
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print(yt.streams.all())
"""
print("------------------------------------------------------------")  # 60個

""" fail
from pytube import YouTube


def onProgress(stream, chunk, remains):
    total = stream.filesize  # 取得完整尺寸
    percent = (total - remains) / total * 100  # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
    print(f"下載中… {percent:05.2f}", end="\r")  # 顯示進度，\r 表示不換行，在同一行更新


print("download...3")
url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url, on_progress_callback=onProgress)
yt.streams.filter().get_highest_resolution().download(filename="oxxostudio.mp4")
# on_progress_callback 參數等於 onProgress 函式
print()
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

""" fail
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print("download...4")
yt.streams.filter().get_audio_only().download(filename="oxxostudio.mp3")
# 儲存為 mp3
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

from pytube import YouTube
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print('取得所有語系 :', yt.captions)
caption = yt.captions.get_by_language_code("en")  # 取得英文語系
xml = caption.xml_captions  # 將語系轉換成 xml
# print(xml)


def xml2srt(text):
    soup = BeautifulSoup(text)  # 使用 BeautifulSoup 轉換 xml
    ps = soup.findAll("p")  # 取出所有 p tag 內容

    output = ""  # 輸出的內容
    num = 0  # 每段字幕編號
    for i, p in enumerate(ps):
        try:
            a = p["a"]  # 如果是自動字幕，濾掉有 a 屬性的 p tag
        except:
            try:
                num = num + 1  # 每段字幕編號加 1
                text = p.text  # 取出每段文字
                t = int(p["t"])  # 開始時間
                d = int(p["d"])  # 持續時間

                h, tm = divmod(t, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                m, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                s, ms = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                t2 = t + d  # 根據持續時間，計算結束時間
                if t2 > int(ps[i + 1]["t"]):
                    t2 = int(ps[i + 1]["t"])  # 如果時間算出來比下一段長，採用下一段的時間
                h2, tm = divmod(t2, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                m2, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                s2, ms2 = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                output = output + str(num) + "\n"  # 產生輸出的檔案，\n 表示換行
                output = (
                    output
                    + f"{h:02d}:{m:02d}:{s:02d},{ms:03d} --> {h2:02d}:{m2:02d}:{s2:02d},{ms2:03d}"
                    + "\n"
                )
                output = output + text + "\n"
                output = output + "\n"
            except:
                pass

    return output


# print(xml2srt(xml))
with open("tmp_oxxostudio.srt", "w") as f1:
    f1.write(xml2srt(xml))  # 儲存為 srt

print("下載字幕 ok!")

print("------------------------------------------------------------")  # 60個

from pytube import Playlist, YouTube

url = "https://www.youtube.com/watch?v=mOPRaLPh-YU&list=PL9ACDjBMkp9wViVmgpYweGkNqh62pHspF"

playlist = Playlist(url)  # 讀取影片清單

#print(playlist.video_urls)  # 印出清單結果
for _ in playlist.video_urls:
    print(_)

"""
['https://www.youtube.com/watch?v=mOPRaLPh-YU',
 'https://www.youtube.com/watch?v=wARhTJH1fJI',
 'https://www.youtube.com/watch?v=WLjePGUCRqc']
"""

""" fail
print("download...5")
for i in playlist.video_urls:
    print(i)
    yt = YouTube(i)  # 讀取影片
    yt.streams.filter().get_highest_resolution().download()  # 下載為最高畫質影片
print("ok!")
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Youtube pytube SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("openai ST")
print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="講個笑話來聽聽",
    max_tokens=128,
    temperature=0.5,
)

completed_text = response["choices"][0]["text"]
print(completed_text)

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=128,
    temperature=0.5,
    messages=[
        {"role": "user", "content": "我叫做 oxxo"},
        {"role": "assistant", "content": "原來你是 oxxo 呀"},
        {"role": "user", "content": "請問我叫什麼名字？"},
    ],
)
print(response.choices[0].message.content)

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

messages = ""
while True:
    msg = input("me > ")
    messages = f"{messages}{msg}\n"  # 將過去的語句連接目前的對話，後方加上 \n 可以避免標點符號結尾問題
    response = openai.Completion.create(
        model="text-davinci-003", prompt=messages, max_tokens=128, temperature=0.5
    )

    ai_msg = response["choices"][0]["text"].replace("\n", "")
    print("ai > " + ai_msg)
    messages = f"{messages}\n{ai_msg}\n\n"  # 合併 AI 回應的話

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

messages = []
while True:
    msg = input("me > ")
    messages.append({"role": "user", "content": msg})  # 添加 user 回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", max_tokens=128, temperature=0.5, messages=messages
    )
    ai_msg = response.choices[0].message.content.replace("\n", "")
    messages.append({"role": "assistant", "content": ai_msg})  # 添加 ChatGPT 回應
    print(f"ai > {ai_msg}")

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

from firebase import firebase

url = "https://XXXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtime database
chatgpt = fdb.get("/", "chatgpt")  # 取的 chatgpt 節點的資料

if chatgpt == None:
    messages = ""  # 如果節點沒有資料，訊息內容設定為空
else:
    messages = chatgpt  # 如果節點有資料，使用該資料作為歷史聊天記錄

while True:
    msg = input("me > ")
    if msg == "!reset":
        message = ""
        fdb.delete("/", "chatgpt")  # 如果輸入 !reset 就清空歷史紀錄
        print("ai > 對話歷史紀錄已經清空！")
    else:
        messages = f"{messages}{msg}\n"  # 在輸入的訊息前方加上歷史紀錄
        response = openai.Completion.create(
            model="text-davinci-003", prompt=messages, max_tokens=128, temperature=0.5
        )

        ai_msg = response["choices"][0]["text"].replace("\n", "")  # 取得 ChatGPT 的回應
        print("ai > " + ai_msg)
        messages = f"{messages}\n{ai_msg}\n\n"  # 在訊息中加入 ChatGPT 的回應
        fdb.put("/", "chatgpt", messages)  # 更新資料庫資料


print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = "你的 API Key"

from firebase import firebase

url = "https://XXXXXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtimr database
chatgpt = fdb.get("/", "chatgpt")  # 讀取 chatgpt 節點中所有的資料

if chatgpt == None:
    messages = []  # 如果沒有資料，預設訊息為空串列
else:
    messages = chatgpt  # 如果有資料，訊息設定為該資料

while True:
    msg = input("me > ")
    if msg == "!reset":
        fdb.delete("/", "chatgpt")  # 如果輸入 !reset 就清空 chatgpt 的節點內容
        messages = []
        print("ai > 對話歷史紀錄已經清空！")
    else:
        messages.append({"role": "user", "content": msg})  # 將輸入的訊息加入歷史紀錄的串列中
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", max_tokens=128, temperature=0.5, messages=messages
        )
        ai_msg = response.choices[0].message.content.replace("\n", "")  # 取得回應訊息
        messages.append({"role": "assistant", "content": ai_msg})  # 將回應訊息加入歷史紀錄串列中
        fdb.put("/", "chatgpt", messages)  # 更新 chatgpt 節點內容
        print(f"ai > {ai_msg}")


print("------------------------------------------------------------")  # 60個
print("openai SP")
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

print("------------------------------------------------------------")  # 60個

print("測試 cookies over18, 無 cookies 抓網頁")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
url = "https://www.ptt.cc/bbs/Beauty/M.1707360497.A.39D.html"

print('無 cookies 抓不到網頁資料')
response = requests.get(url)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 cookies over18, 有 cookies 抓網頁")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
url = "https://www.ptt.cc/bbs/Beauty/M.1707360497.A.39D.html"

print('有 cookies 可以抓到網頁資料')
cookies = {"over18": "1"}
response = requests.get(url, cookies=cookies)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 headers, 無 headers 抓網頁, ck101 網頁")

# 怎麼無headers 也是OK?
url = "https://ck101.tw/thread-5778209-1-1.html"
# url ='https://www.dcard.tw/f/stock/p/237123381'

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)

print("------------------------------------------------------------")  # 60個

print("測試 headers, 有 headers 抓網頁, ck101 網頁")

url = "https://ck101.tw/thread-5778209-1-1.html"
# url ='https://www.dcard.tw/f/stock/p/237123381'

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
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")

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
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")

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
response.encoding = "utf8"
print(response.text)


print('簡易 requests.get(url)')

print("#台灣水庫即時水情")
url = "https://water.taiwanstat.com/"  # 台灣水庫即時水情
response = requests.get(url)
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
print(response.text)  # 讀取並印出 text 屬性

print("------------------------------------------------------------")  # 60個

url = "https://invoice.etax.nat.gov.tw/index.html"
response = requests.get(url)  # 取得網頁內容
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
print(response.text)
'''
print("------------------------------------------------------------")  # 60個

url = "https://data.kcg.gov.tw/dataset/6f29f6f4-2549-4473-aa90-bf60d10895dc/resource/30dfc2cf-17b5-4a40-8bb7-c511ea166bd3/download/lightrailtraffic.json"
response = requests.get(url)
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

print("response內的text")
print(response.text)

print("response轉成json格式")
print(response.json())

print("------------------------------------------------------------")  # 60個

# https://mis.twse.com.tw/stock/fibest.jsp?stock=0050
url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw"
response = requests.get(url)
json_data = json.loads(response.text)

print(json_data)

print("------------------------------------------------------------")  # 60個

print("拆解網頁資料")
url = "https://today.line.me/tw/v2/article/oqay0ro"
response = requests.get(url)

# 取得文章的原始碼後，使用 split 字串拆分的方式，拆解出 articleId
article_id = response.text.split("<script>")[1].split('id:"article:')[1].split(":")[0]
print(article_id)

print("------------------------------------------------------------")  # 60個

""" many

print('------------------------------------------------------------')	#60個

import pprint

url = 'http://tw.yahoo.com'
response = requests.get(url)
pprint.pprint(response.text)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


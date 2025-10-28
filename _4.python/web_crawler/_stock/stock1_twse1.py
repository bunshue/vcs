# Python 測試 twse 1

"""
公開資訊觀測站
https://mops.twse.com.tw/mops/
https://mops.twse.com.tw/mops/#/web/home
"""

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

import csv
import json
import requests
from io import StringIO
from bs4 import BeautifulSoup

print("------------------------------------------------------------")  # 60個

print("讀取上市公司基本資料")

# r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_L.csv")
# r.encoding = "big5"
filename = "data/t187ap03_L.csv"

# df = pd.read_csv(filename, index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

# df.drop(df.index[len(df.index) - 1], inplace=True)

print(df)
print("---------------")  # 15個
print(df["公司代號"])
print("---------------")  # 15個
print(df[df["公司代號"] == 2330])

print("------------------------------")  # 30個

print("讀取上櫃公司基本資料")

# r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_O.csv")
# r.encoding = "big5"
filename = "data/t187ap03_O.csv"

# df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

# df.drop(df.index[len(df.index)-1], inplace=True)

print(df)

print("------------------------------")  # 30個

print("讀取興櫃公司基本資料")

# r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_R.csv")
# r.encoding = "big5"

# df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)

filename = "data/t187ap03_R.csv"

df = pd.read_csv(filename, index_col=False, skiprows=1)

df.drop(df.index[len(df.index) - 1], inplace=True)
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("下載月營收")


def monthly_report(year, month):
    # 假如是西元，轉成民國
    if year > 1911:
        year -= 1911

    url = (
        "https://mops.twse.com.tw/nas/t21/sii/t21sc03_"
        + str(year)
        + "_"
        + str(month)
        + "_0.html"
    )
    if year <= 98:
        url = (
            "https://mops.twse.com.tw/nas/t21/sii/t21sc03_"
            + str(year)
            + "_"
            + str(month)
            + ".html"
        )

    # 偽瀏覽器
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    print(url)

    # 下載該年月的網站，並用pandas轉換成 dataframe
    r = requests.get(url, headers)
    r.encoding = "big5"
    html_df = pd.read_html(StringIO(r.text))

    print(html_df)

    # 處理一下資料
    if html_df[0].shape[0] > 500:
        df = html_df[0].copy()
    else:
        df = pd.concat([df for df in html_df if df.shape[1] <= 11])

    print(df)

    # df = df[list(range(0,10))]
    # column_index = df.index[(df[0] == '公司代號')][0]
    # df.columns = df.iloc[column_index]
    # df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    # df = df[~df['當月營收'].isnull()]
    # df = df[df['公司代號'] != '合計']

    return df


df = monthly_report(2017, 1)

print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("下載財報")


def financial_statement(year, season, exchange="sii", type="綜合損益表"):
    if year > 1911:
        year -= 1911

    if type == "綜合損益表":
        url = "http://mops.twse.com.tw/mops/web/ajax_t163sb04"
    elif type == "資產負債表":
        url = "http://mops.twse.com.tw/mops/web/ajax_t163sb05"
    elif type == "營益分析查詢彙總表":
        url = "http://mops.twse.com.tw/mops/web/ajax_t163sb06"
    else:
        print("type does not match")

    print(url)

    # 一些參數：
    # TYPEK => 市場別
    # sii>上市
    # otc>上櫃
    # rotc>興櫃
    # pub>公開發行

    # year => 年度
    # season => 季別
    r = requests.post(
        url,
        {
            "encodeURIComponent": 1,
            "step": 1,
            "firstin": 1,
            "off": 1,
            "TYPEK": exchange,
            "year": year,
            "season": season,
        },
    )

    r.encoding = "utf8"
    dfs = pd.read_html(r.text)

    print(dfs)

    for i, df in enumerate(dfs):
        df.columns = df.iloc[0]
        dfs[i] = df.iloc[1:]

    df = pd.concat(dfs).applymap(lambda x: x if x != "--" else np.nan)
    df = df[df["公司代號"] != "公司代號"]
    df = df[~df["公司代號"].isnull()]
    if any(df.columns.str.contains("合計：")):
        df = df.loc[:, ~df.columns.str.contains("合計：")]
    return df


""" fail
df = financial_statement(2017, 2, type='營益分析查詢彙總表')
print(df[df['公司名稱']=='台泥'])
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("國內主要金融指標")

# 政府開放資料平台 - 國內主要金融指標
# https://data.gov.tw/dataset/30815

url_by_month = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000037-51i"
print(url_by_month)

r = requests.get(url_by_month)
df = pd.read_csv(StringIO(r.text))

print(df.set_index("月別"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
print('證券商分公司基本資料')

# 讀取證券商分公司基本資料

r = requests.get("http://www.twse.com.tw/brokerService/branchList.csv")
r.encoding = "big5"
df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
print(df)
"""
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
print('讀取證券商總公司基本資料')

r = requests.get("http://www.twse.com.tw/brokerService/brokerList.csv?lang=zh")
r.encoding = "big5"
df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
print(df)
"""

print("------------------------------------------------------------")  # 60個

""" NG 資料抓不下來
print('讀取 Nasdaq 的股價歷史資料')

symbol = 'GOOG'.lower()

url_template = "https://www.nasdaq.com/symbol/{symbol}/historical"
url = url_template.format(symbol=symbol)
print(url)

rs = requests.session()
r = rs.get(url)
soup = BeautifulSoup(r.text, 'lxml')
params = soup.select('#getFile input')
# 時間長短：5d, 1m, 3m, 6m, 1y, 18m, 2y, 3y, 4y, 5y, 6y, 7y, 8y, 9y, 10y
timeframe = '{timestr}|true|{symbol}'.format(timestr='3m', symbol=symbol.upper())
payload = {}

for tag in params:
    if tag['name'] != 'ctl00$quotes_content_left$submitString':
        payload[tag['name']] = tag['value']
    else:
        payload[tag['name']] = timeframe

#r = rs.post(url, data=payload)
r = rs.post(url, data=payload, verify=False)
print(r.text)
"""

print("------------------------------------------------------------")  # 60個

""" NG 資料抓不下來
print('讀取 NASDAQ, NYSE, AMEX 公司資料')

url_template = "https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange={}&render=download"

url = url_template.format('NASDAQ')

df = pd.read_csv(url)
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
print(df)
"""

print("------------------------------------------------------------")  # 60個

print("讀取景氣對策信號")

"""
網址：政府開放資料 - 國發會 景氣指標及燈號
https://www.ndc.gov.tw/News_Content.aspx?n=9D32B61B1E56E558&sms=9D3CAFD318C60877&s=C367F13BF38C5711
應用：
可以利用景氣對策信號判斷 ETF 的進入點。
"""

""" NG 無檔案
from io import BytesIO

# 讀取 .xlsx 檔

r = requests.get('https://ws.ndc.gov.tw/Download.ashx?u=LzAwMS9hZG1pbmlzdHJhdG9yLzEwL3JlbGZpbGUvNTc4MS82MzkyL2VmMWQ4ZjliLTMxOGMtNDFmZC1hNzgzLWVjNGY5MTMwMjRmOC54bHN4&n=5paw6IGe56i%2f6ZmE5Lu25pW45YiXLnhsc3g%3d&icon=..xlsx')
df = pd.read_excel(BytesIO(r.content))

df = df.set_index('DATE')

df['2010-01-01':]['景氣對策信號綜合分數'].plot()

plt.show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直接取得csv檔資料

datestr = "20240716"

url = (
    "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
    + datestr
    + "&type=ALLBUT0999"
)
print(url)

# 下載股價
response = requests.get(url)
# print(response.text)  # HTML網頁內容, 即csv檔的內容

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

print("下載台股單日股價行情")

datestr = "20180131"

r = requests.get(
    "http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
    + datestr
    + "&type=ALL"
)

# pandas 會自動把字串裡的單一引號 (") 去除

df = pd.read_csv(
    StringIO(
        "\n".join(
            [
                i.translate({" ": None})
                for i in r.text.split("\n")
                if len(i.split('",')) == 17 and i[0] != "="
            ]
        )
    ),
    header=0,
    thousands=",",
)

df = df.loc[:, ~df.columns.str.contains("Unnamed")]

print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台股股價歷史資料")

print("讀取台股股價資料")

url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY"
params = {}
params["stockNo"] = "2330"
params["date"] = "20160101"
params["response"] = "csv"

r = requests.get(url, params=params)

import datetime

df = pd.read_csv(
    StringIO(r.text), engine="python", skiprows=1, skipfooter=4, thousands=","
)


def DateConvert(twdate):
    x = twdate.split("/")
    return datetime.date(int(x[0]) + 1911, int(x[1]), int(x[2]))


df["日期"] = df["日期"].map(DateConvert)
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 台灣證券交易所，個股日成交資訊
search_date = "20220101"
search_stock = "2330"
url = (
    "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="
    + search_date
    + "&stockNo="
    + search_stock
)

# 取得股票資料json字串
html_data = requests.get(url)
# print(html_data.text)

# 從json字串轉為python的字典格式
json_data = json.loads(html_data.text)
datas = json_data["data"]
fields = json_data["fields"]
print(datas)  # 由List組成的二維陣列
print(fields)

# 存成Pandas的Dataframe
df = pd.DataFrame(datas, columns=fields)
print(df)

# Pandas匯出
# 轉成csv檔
df.to_csv("./month_stock.csv", encoding="big5")
# 轉成xlsx檔
df.to_excel("./month_stock.xlsx", encoding="big5")
# 轉成html檔
df.to_html("./month_stock.html")

# 抓一整年的資料 2022年
year_df = pd.DataFrame()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
search_year = "2022"
search_stock = "2330"
# url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+search_date+'&stockNo='+search_stock

# 從1到12月
for m in range(1, 13):
    print(m)
    url = (
        "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="
        + search_year
        + "{0:02d}01&stockNo="
        + search_stock
    ).format(m)
    print(url)

    # 取得股票資料json字串
    html_data = requests.get(url, headers=headers)
    # print(html_data.text)

    # 從json字串轉為python的字典格式
    json_data = json.loads(html_data.text)
    datas = json_data["data"]
    fields = json_data["fields"]

    # 存成Pandas的Dataframe
    month_df = pd.DataFrame(datas, columns=fields)
    # print(month_df)

    # 合併於整年的Dataframe
    year_df = year_df.append(month_df, ignore_index=True)

# print(year_df)
# 轉成csv檔
year_df.to_csv("./year_stock.csv", encoding="big5")

print("------------------------------------------------------------")  # 60個

# 讀取csv
df = pd.read_csv("./month_stock.csv", encoding="big5")
# print(df)

"""
# 讀取excel
df2 = pd.read_excel("./month_stock.xlsx")
print(df2)

# 讀取html
df3 = pd.read_html("./month_stock.html", encoding="utf8")
print(df3)
"""

# 使用 Matplotlib 畫圖

# 篩選我們要的資料
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

# 繪圖
# plt.plot(date, high_price)
# plt.plot(date, low_price)
# plt.plot(date, end_price)

plt.plot(date, high_price, color="#ff2121")
plt.plot(date, low_price, color="#00bd42", linewidth=5)
plt.plot(date, end_price, color="#005de0", linestyle="dashed")

"""
plt.xlabel("日期")    # x軸標籤
plt.ylabel("價格")    # y軸標籤
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
plt.title("110年8月股市趨勢圖")    # 主標題
"""
plt.grid(True)  # 是否有網格?

# 存成圖片, 要放在show()之前
# plt.savefig("matplotlib_chart.png")

# 顯示圖片
plt.show()

# 使用 Pandas 畫圖

# 篩選我們要的資料
chart_df = df[["日期", "最高價", "最低價", "收盤價"]]
# 將日期設為x軸
chart_df.set_index("日期", inplace=True)
print(chart_df)

# 繪圖
chart = chart_df.plot(xlabel="日期", ylabel="價格", title="110年8月股市趨勢圖", legend=True)
# chart = chart_df.plot(xlabel="日期", ylabel="價格", title="109年股市趨勢圖", legend=True)
plt.grid()


# 存成圖片, 要放在show()之前
# plt.savefig("pandas_chart.png")
# 顯示圖片

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 4.5 台灣證券交易所API
# 這個API長得大概像這樣:
# http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20160501&stockNo=2330
# 比較重要的地方是date這個參數, 基本上你給的值一定要是yyyyMMdd的形式, 但是真正作用的只有yyyy與MM, 因為他會把這段request解讀成你想要看stockNo股票在yyyy年MM月的紀錄, 所以dd基本上沒有太大意義, 但卻是不可少的部分.

TWSE_URL = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json"


def get_web_content(search_stock, current_date):
    resp = requests.get(TWSE_URL + "&date=" + current_date + "&stockNo=" + search_stock)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()


def get_data(search_stock, current_date):
    info = list()
    resp = get_web_content(search_stock, current_date)
    if resp is None:
        return None
    else:
        if resp["data"]:
            for data in resp["data"]:
                record = {
                    "日期": data[0],
                    "開盤價": data[3],
                    "收盤價": data[6],
                    "成交筆數": data[8],
                }
                info.append(record)
        return info


def get_stock_data_twse(search_stock):
    current_date = time.strftime("%Y%m%d")
    current_year = time.strftime("%Y")
    current_month = time.strftime("%m")
    print("Processing data for %s %s..." % (current_year, current_month))
    get_data(search_stock, current_date)
    collected_info = get_data(search_stock, current_date)
    for info in collected_info:
        print(info)


search_stock = "2330"
get_stock_data_twse(search_stock)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 臺灣證券交易所-基本市況報導網站 MIS
# https://mis.twse.com.tw/stock/

# 元大寶來台灣卓越50證券投資信託基金
# TPE: 0050

url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw"
response = requests.get(url)
json_data = json.loads(response.text)

print(type(json_data))
print(json_data)

print("全名 :", json_data["msgArray"][0]["nf"])
print("簡稱 :", json_data["msgArray"][0]["n"])
print("最高 :", json_data["msgArray"][0]["h"])
print("最低 :", json_data["msgArray"][0]["l"])
print("昨收 :", json_data["msgArray"][0]["y"])
print("開盤 :", json_data["msgArray"][0]["o"])
print("成交 :", json_data["msgArray"][0]["z"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台股即時股價資料")

# 參考 twstock 取得需要的 URL
SESSION_URL = "http://mis.twse.com.tw/stock/index.jsp"
STOCKINFO_URL = (
    "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_id}&_={time}"
)


def get_realtime_quote(stockNo, ex="tse"):
    req = requests.Session()
    req.get(SESSION_URL)

    stock_id = "{}_{}.tw".format(ex, stockNo)

    r = req.get(STOCKINFO_URL.format(stock_id=stock_id, time=int(time.time()) * 1000))

    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return {"rtmessage": "json decode error", "rtcode": "5000"}


print(get_realtime_quote("2330"))

print("------------------------------------------------------------")  # 60個
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


def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉換民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "tmp_stockyear2017a.csv"

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉換民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

url_twse = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170101&stockNo=2317&_=1521363562193"
filepath = "tmp_stockmonth01.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    res = requests.get(url_twse)  # 回傳為json資料
    jdata = json.loads(res.text)  # json解析

    outputfile = open(filepath, "w", newline="", encoding="utf-8")  # 開啟儲存檔案
    outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
    outputwriter.writerow(jdata["fields"])
    for dataline in jdata["data"]:  # 寫入資料
        outputwriter.writerow(dataline)
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base_url = "https://www.twse.com.tw"
url = base_url + "/zh/brokerService/brokerServiceAudit"
# https://www.twse.com.tw/brokerService/brokerServiceAudit?showType=list&stkNo=1020&focus=6

csvfile = "tmp_BrokerBranchs.csv"

items = []
print("爬取總公司: ", url)
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one(".grid")  # 找到<table>
rows = tag_table.find_all("tr")  # 找出所有<tr>
for row in rows:
    item = []
    for cell in row.find_all(["td"]):
        txt = cell.text.replace("\n", "").replace("\r", "").strip()
        if txt == "明細":
            new_url = base_url + cell.find("a").get("href")
            print("爬取分公司: ", new_url)
            r2 = requests.get(new_url)
            r2.encoding = "utf8"
            soup2 = BeautifulSoup(r2.text, "lxml")
            tag_table2 = soup2.select_one(".grid.links")  # 找到<table>
            rows2 = tag_table2.find_all("tr")  # 找出所有<tr>
            for row2 in rows2:
                item_branch = []
                for cell2 in row2.find_all("td"):
                    txt = cell2.text.replace("\n", "").replace("\r", "").strip()
                    item_branch.append(txt)
                if item_branch and len(item_branch) == 5:
                    items.append(item_branch)  # 新增分公司
        else:
            item.append(txt)
    if item and len(item) == 5:
        items.append(item)  # 新增總公司
    time.sleep(1)

print("券商總數(總公司+分公司):", len(items))
# 開啟CSV檔案寫入截取的資料
with open(csvfile, "w+", newline="", encoding="utf8") as fp:
    writer = csv.writer(fp)
    writer.writerow(["證券商代號", "證券商名稱", "開業日", "地址", "電話"])
    for item in items:
        writer.writerow(item)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import datetime
import pandas_datareader as pdr

start = datetime.datetime.now() - datetime.timedelta(days=60)
end = datetime.date.today()
""" NG
df = pdr.DataReader("2330.TW", "yahoo", start, end)
print(df.shape)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major1.json", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=csv&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major2.csv", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
if r.status_code == requests.codes.ok:
    print("成功爬取資料...")
    """# NG
    data = r.json() 
    df = pd.read_json(json.dumps(data["data"]))
    df.columns = data["fields"]
    print(df.head())
    df.to_csv("tmp_three_major3.csv", index=False)
    """
else:
    print("HTTP請求錯誤...")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dates = [20250601, 20250701, 20250801]
stockNo = 2330

url = (
    "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
)

for date in dates:
    print(date, stockNo)
    # data = pd.read_html(r.text)[0]  # old
    data = pd.read_html(url.format(date, stockNo))[0]
    
    data.columns = data.columns.droplevel(0)

    csvfile = "tmp_stock_{}_{}.csv".format(stockNo, date)
    data.to_csv(csvfile, index=False)
    time.sleep(5)

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


# 1515
print("---------------")  # 15個

# 3030
print("------------------------------")  # 30個


print("------------------------------------------------------------")  # 60個

plt.rcParams["font.sans-serif"] = "mingliu"  # 設定中文字型

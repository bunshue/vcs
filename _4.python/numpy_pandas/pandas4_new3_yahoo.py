"""

股票資料彙整_YahooFinance
股票資料彙整_Yahoo股市

"""

import sys
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
"""
#使用 pandas_datareader.data.DataReader 抓取 2356.TW, 1566.TWO 最近一個月的股價資料

#股票資料彙整_YahooFinance

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime
import timeit

from pandas_datareader import data, wb
import datetime  

def getWebData(name, 
               start = datetime.date(1970, 1, 1), 
               end = datetime.date.today(), 
               data_source = 'yahoo', 
               retry_count=3, 
               pause=0.001):
    
    df = data.DataReader(name = name, 
                         data_source = data_source,
                         start = start,
                         end = end,
                         retry_count = retry_count,
                         pause = pause
                        ) 

    df = df.to_frame()
    df.index.names = ['Date', 'Name'] 
    
    return df

def fetchAndStoreStockData(stocks):
    
#     start = datetime.datetime(1965, 1, 1)
#     end = datetime.datetime(2013, 1, 1)    
    df = getWebData(stocks)     

    # Write to files __________________________    
    df.to_excel('Yahoo Finance{0}.xlsx'.format(''))

fetchAndStoreStockData(stocks = ['2356.TW', '1566.TWO'])


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# 練習 - 股票資料彙整_Yahoo股市 - 問題

page = 1
url = "https://tw.stock.yahoo.com/s/list.php?c=tse&pid=" + str(page)
url

"""
目標:

    使用 Pandas，抓取上述 url 網頁中的股價資料
    將股票代號與名稱區隔為不同的欄位
    將資料儲存為 Excel 檔案
    須注意個欄位的格式，數字欄位的儲存格式應該為數字
    重排欄位順序為:'市場別', '股票代號', '股票名稱', '日期', '時間', '成交', '買進', '賣出', '漲跌', '張數', '昨收', '開盤', '最高', '最低'
    Extra:
        匯集 Yahoo 股市 page 1~ 5 的資料 (pd.concat)
        依據股票代號的前兩碼，做 GroupBy 操作
            merge ../data/個股_類別.xls(先解壓縮 個股_類別.rar) 中的資料之後，做 GroupBy 操作

"""

# 股票資料彙整_Yahoo股市

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import datetime

# 目標資料來源:
# https://tw.stock.yahoo.com/s/list.php?c=tse&pid=1

# 抓取網頁資料

import requests


def get_yahoo_page_html(url):
    html = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
        },
    )
    return html.text


def getDataOnePage(html):
    targetTableIndex = 0
    table = pd.read_html(
        html,
        attrs={
            "border": "1",
            "cellspacing": "0",
            "cellpadding": "2",
            "bgcolor": "#ffffff",
        },
        header=0,
    )[targetTableIndex]

    return table


def getDataOnePageTSE(page):
    url = "https://tw.stock.yahoo.com/s/list.php?c=tse&pid=" + str(page)
    return getDataOnePage(html=get_yahoo_page_html(url))


# 抓第一頁的資料
df = getDataOnePageTSE(1)

cc = df.tail()
print(cc)


df.to_excel("tmp_stock.xlsx")

# 修整 DataFrame中的資料


def fixTable(marketType, table, theDate=datetime.date.today()):
    fixedTable = table

    # Drop
    fixedTable.drop(["選擇", "凱基證券下單"], axis=1, inplace=True)
    fixedTable.dropna(axis=0, how="all", inplace=True)

    # fill missing data
    fixedTable["股票代號名稱"] = fixedTable["股票代號"]
    fixedTable["股票代號"] = fixedTable["股票代號名稱"].map(lambda x: x.split()[0])
    fixedTable["股票名稱"] = fixedTable["股票代號名稱"].map(lambda x: x.split()[1])
    fixedTable["日期"] = theDate
    fixedTable["市場別"] = marketType

    # data type
    fixedTable.replace("－", np.nan, inplace=True)

    fixedTable["股票代號"] = fixedTable["股票代號"].astype(str)
    fixedTable["時間"] = fixedTable["時間"].astype(datetime.time)
    fixedTable[["成交", "買進", "賣出", "張數", "昨收", "開盤", "最高", "最低"]] = fixedTable[
        ["成交", "買進", "賣出", "張數", "昨收", "開盤", "最高", "最低"]
    ].astype(float)

    fixedTable["漲跌"] = fixedTable["成交"] - fixedTable["昨收"]
    fixedTable["漲跌"] = fixedTable["漲跌"].map(lambda x: round(x, 2))

    # sort
    #     fixedTable.sort_values(by = '股票代號', inplace = True)

    # indexing
    fixedTable.index = Series(range(len(fixedTable)))
    fixedTable.index.name = "項次"
    fixedTable = fixedTable.reindex(
        columns=[
            "市場別",
            "股票代號",
            "股票名稱",
            "日期",
            "時間",
            "成交",
            "買進",
            "賣出",
            "漲跌",
            "張數",
            "昨收",
            "開盤",
            "最高",
            "最低",
        ]
    )

    return fixedTable


df1 = fixTable("TSE", df)

df1.tail(5)

# 彙整 Yahoo 股市 page 1~ 5 的資料

# 抓第一頁~第五頁的資料
dfs = map(lambda p: fixTable("TSE", getDataOnePageTSE(p)), range(1, 6))

# Append 在一起
df = pd.concat(dfs)
len(df)

# 1000

df.index = pd.Index(range(len(df)))  # 重新編排 row index 編號
df = df[df["股票代號"].str.len() <= 4]  # 濾除 權證 資料
df.tail()

# 抓取 類股 資料

df_類股 = pd.read_excel("..\\data\個股_類別.xls")  # 需先解壓縮 個股_類別.rar
df_類股.tail()

# Merge

mdf = df.merge(df_類股, left_on="股票代號", right_on="個股_代號", how="left")  # merge
mdf = mdf.drop(["市場別_ID", "個股_代號", "個股_名稱"], axis=1)  # drop 多於的欄位
mdf.tail()

# GroupBy

# 各類股有多少支個股
mdf.groupby(["類股_名稱"]).size().sort_index()


# 各類股 平均股價
mdf.groupby(["類股_名稱"])["成交"].mean().sort_index()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

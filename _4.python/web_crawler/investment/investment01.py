"""

公開資訊觀測站
https://mops.twse.com.tw/mops/web/index

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import requests
import numpy as np
import pandas as pd
from io import StringIO

print('------------------------------------------------------------')	#60個

print('讀取上市公司基本資料')


"""
r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_L.csv")
r.encoding = "big5"
"""

filename = 't187ap03_L.csv'
#filename = 'test.csv'

#df = pd.read_csv(filename, index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

#df.drop(df.index[len(df.index)-1], inplace=True)

print(df)
print()
print(df['公司代號'])
print()
print(df[df['公司代號']==2330])

print('------------------------------------------------------------')	#60個

print('讀取上櫃公司基本資料')

#r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_O.csv")
#r.encoding = "big5"

filename = 't187ap03_O.csv'

#df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

#df.drop(df.index[len(df.index)-1], inplace=True)

print(df)

print('------------------------------------------------------------')	#60個


print('下載月營收')

def monthly_report(year, month):

    # 假如是西元，轉成民國
    if year > 1911:
        year -= 1911

    url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'_0.html'
    if year <= 98:
        url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'.html'

    # 偽瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    print(url)

    # 下載該年月的網站，並用pandas轉換成 dataframe
    r = requests.get(url, headers)
    r.encoding = 'big5'
    html_df = pd.read_html(StringIO(r.text))

    print(html_df)

    # 處理一下資料
    if html_df[0].shape[0] > 500:
        df = html_df[0].copy()
    else:
        df = pd.concat([df for df in html_df if df.shape[1] <= 11])

    print(df)

    #df = df[list(range(0,10))]
    #column_index = df.index[(df[0] == '公司代號')][0]
    #df.columns = df.iloc[column_index]
    #df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    #df = df[~df['當月營收'].isnull()]
    #df = df[df['公司代號'] != '合計']

    return df

df = monthly_report(2017, 1)

print(df)

print('------------------------------------------------------------')	#60個

print('下載台股單日股價行情')

datestr = '20180131'

r = requests.get('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

# pandas 會自動把字串裡的單一引號 (") 去除

df = pd.read_csv(StringIO("\n".join([i.translate({' ':None}) 
                                     for i in r.text.split('\n') 
                                     if len(i.split('",')) == 17 and i[0] != '='])), header=0, thousands=',')

df = df.loc[:, ~df.columns.str.contains("Unnamed")]

print(df)

print('------------------------------------------------------------')	#60個

print('下載財報')

def financial_statement(year, season, exchange='sii', type='綜合損益表'):
    if year > 1911:
        year -= 1911

    if type == '綜合損益表':
        url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb04'
    elif type == '資產負債表':
        url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb05'
    elif type == '營益分析查詢彙總表':
        url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb06'
    else:
        print('type does not match')

    print(url)

    # 一些參數：
    # TYPEK => 市場別
    # sii>上市
    # otc>上櫃
    # rotc>興櫃
    # pub>公開發行

    # year => 年度
    # season => 季別
    r = requests.post(url, {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'TYPEK': exchange,
        'year': year,
        'season': season,
    })

    r.encoding = 'utf8'
    dfs = pd.read_html(r.text)

    print(dfs)
    
    for i, df in enumerate(dfs):
        df.columns = df.iloc[0]
        dfs[i] = df.iloc[1:]

    df = pd.concat(dfs).applymap(lambda x: x if x != '--' else np.nan)
    df = df[df['公司代號'] != '公司代號']
    df = df[~df['公司代號'].isnull()]
    if any(df.columns.str.contains("合計：")):
        df = df.loc[:, ~df.columns.str.contains("合計：")]
    return df

""" fail
df = financial_statement(2017, 2, type='營益分析查詢彙總表')
print(df[df['公司名稱']=='台泥'])
"""

print('------------------------------------------------------------')	#60個

print('台股即時股價資料')

import json

# 參考 twstock 取得需要的 URL
SESSION_URL = 'http://mis.twse.com.tw/stock/index.jsp'
STOCKINFO_URL = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_id}&_={time}'

def get_realtime_quote(stockNo, ex='tse'):
    req = requests.Session()
    req.get(SESSION_URL)

    stock_id = '{}_{}.tw'.format(ex, stockNo)

    r = req.get(STOCKINFO_URL.format(stock_id=stock_id, time=int(time.time()) * 1000))

    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return {'rtmessage': 'json decode error', 'rtcode': '5000'}

print(get_realtime_quote('2330'))

print('------------------------------------------------------------')	#60個

print('台股股價歷史資料')

""" Fail
print('讀取台股股價資料')

url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY"
params = {}
params['stockNo'] = "2330"
params['date'] = "20160101"
params['response'] = "csv"

r = requests.get(url, params=params)

import datetime

df = pd.read_csv(StringIO(r.text), engine='python', skiprows=1, skipfooter=4, thousands=',')

def DateConvert(twdate):
    x = twdate.split('/')
    return datetime.date(int(x[0])+1911, int(x[1]), int(x[2]))

df['日期'] = df['日期'].map(DateConvert)
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
print(df)
"""

print('------------------------------------------------------------')	#60個

print('國內主要金融指標')

#政府開放資料平台 - 國內主要金融指標
#https://data.gov.tw/dataset/30815

url_by_month = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000037-51i"
print(url_by_month)

r = requests.get(url_by_month)
df = pd.read_csv(StringIO(r.text))

print(df.set_index('月別'))

print('------------------------------------------------------------')	#60個

""" 沒效果
#使用 Google Trends 來判斷股價高點

from pytrends.request import TrendReq

keyword = '股票'

pytrend = TrendReq(hl='zh-TW')

pytrend.build_payload(kw_list=[keyword])

df = pytrend.interest_over_time()

print(df)

# 用來比對大盤漲跌

#df['股票']['2017-09-01':].plot()
#plt.show()
"""

print('------------------------------------------------------------')	#60個

print('讀取興櫃公司基本資料')

#r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_R.csv")
#r.encoding = "big5"
#df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)

filename = 't187ap03_R.csv'
df = pd.read_csv(filename, index_col=False, skiprows=1)

df.drop(df.index[len(df.index)-1], inplace=True)
print(df)

print('------------------------------------------------------------')	#60個

""" NG 無檔案
print('證券商分公司基本資料')

# 讀取證券商分公司基本資料

r = requests.get("http://www.twse.com.tw/brokerService/branchList.csv")
r.encoding = "big5"
df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
print(df)
"""

print('------------------------------------------------------------')	#60個

"""無檔案
print('讀取證券商總公司基本資料')

r = requests.get("http://www.twse.com.tw/brokerService/brokerList.csv?lang=zh")
r.encoding = "big5"
df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
print(df)
"""

print('------------------------------------------------------------')	#60個

""" NG 資料抓不下來
print('讀取 Nasdaq 的股價歷史資料')

from bs4 import BeautifulSoup

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

print('------------------------------------------------------------')	#60個

""" NG 資料抓不下來
print('讀取 NASDAQ, NYSE, AMEX 公司資料')

url_template = "https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange={}&render=download"

url = url_template.format('NASDAQ')

df = pd.read_csv(url)
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
print(df)
"""

print('------------------------------------------------------------')	#60個

print('讀取景氣對策信號')

"""
網址：政府開放資料 - 國發會 景氣指標及燈號
https://www.ndc.gov.tw/News_Content.aspx?n=9D32B61B1E56E558&sms=9D3CAFD318C60877&s=C367F13BF38C5711
應用：
可以利用景氣對策信號判斷 ETF 的進入點。
"""

"""無檔案

from io import BytesIO

# 讀取 .xlsx 檔

r = requests.get('https://ws.ndc.gov.tw/Download.ashx?u=LzAwMS9hZG1pbmlzdHJhdG9yLzEwL3JlbGZpbGUvNTc4MS82MzkyL2VmMWQ4ZjliLTMxOGMtNDFmZC1hNzgzLWVjNGY5MTMwMjRmOC54bHN4&n=5paw6IGe56i%2f6ZmE5Lu25pW45YiXLnhsc3g%3d&icon=..xlsx')
df = pd.read_excel(BytesIO(r.content))

df = df.set_index('DATE')

df['2010-01-01':]['景氣對策信號綜合分數'].plot()

plt.show()
"""

print('------------------------------------------------------------')	#60個

"""無檔案
print('讀取集保股權分散表')

from bs4 import BeautifulSoup

url = "http://www.tdcc.com.tw/smWeb/QryStock.jsp"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

sca_date = soup.select("option")

url = "http://www.tdcc.com.tw/smWeb/QryStock.jsp?SCA_DATE={}&SqlMethod=StockNo&StockNo={}&StockName=&sub=%ACd%B8%DF"

full_url = url.format(sca_date[0].text, '2330')

r = requests.get(full_url)

soup = BeautifulSoup(r.text, 'lxml')

html_table = soup.select('.mt')

dfs = pd.read_html(str(html_table[1]), header=0)

print(dfs[0])
"""

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


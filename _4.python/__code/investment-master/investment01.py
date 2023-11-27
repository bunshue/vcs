import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


#上市公司基本資料

import requests
import pandas as pd
from io import StringIO
# 讀取上市公司基本資料

"""
r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_L.csv")
r.encoding = "big5"
"""

'''
filename = 't187ap03_L.csv'

#filename = 'test.csv'

#df = pd.read_csv(filename, index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

#df.drop(df.index[len(df.index)-1], inplace=True)

print(df)

print()

print(df['公司代號'])

print()
print()
print(df[df['公司代號']==2330])

print('------------------------------------------------------------')	#60個


#上櫃公司基本資料

import requests

import pandas as pd

from io import StringIO

# 讀取上櫃公司基本資料

#r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_O.csv")
#r.encoding = "big5"

filename = 't187ap03_O.csv'

#df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

#df.drop(df.index[len(df.index)-1], inplace=True)

print(df)
'''
print('------------------------------------------------------------')	#60個



#下載月營收

import pandas as pd
import requests
from io import StringIO
import time

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

import requests
from io import StringIO
import pandas as pd

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

import requests
import pandas as pd
import numpy as np

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
import time
import requests

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
import requests
import pandas as pd
from io import StringIO

# 讀取台股股價資料

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


import requests

import pandas as pd

from io import StringIO


url_by_month = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000037-51i"
print(url_by_month)

r = requests.get(url_by_month)
df = pd.read_csv(StringIO(r.text))

print(df.set_index('月別'))



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

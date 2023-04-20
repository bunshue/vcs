# Python 測試 BeautifulSoup


'''
import sys
import requests
from bs4 import BeautifulSoup

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

print('BeautifulSoup 測試 1')

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, "html.parser")
        print("取得網頁標題", soup.title)
else:
        print('無法取得網頁資料')

soup = BeautifulSoup(html_data.text, 'html.parser')
print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

import pandas
dfs = pandas.read_html(url)
print(dfs[0])

print()
print()
print()
print()
currency = dfs[0]

'''

'''

import pandas
import numpy
import datetime

todday = datetime.datetime.today() # 今天日期
delta = datetime.timedelta(days=1) # 要查詢遞延幾天的匯率
day = todday - delta # 時間計算

# 取得資料
day = day.strftime('%Y-%m-%d')
url = 'https://rate.bot.com.tw/xrt/all/' + day
data = pandas.read_html(url)

print(data[0])
'''
'''
# 重組df
df = data[0]
df = df.replace('-', numpy.nan)

re_df = data[0]['幣別']

re_df = re_df.join(df['Unnamed: 3_level_0']['本行賣出'].astype(float)).join(df['即期匯率']['本行買入'].astype(float))
re_df.columns = ['幣別', '本行買入', '本行賣出']
re_df.index = re_df['幣別']
re_df['中間匯率'] = (re_df['本行買入'] + re_df['本行賣出']) / 2 # 計算中間匯率 (買+賣)/2

print(day, re_df) # 顯示
'''



url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

import pandas
dfs = pandas.read_html(url)
#print(dfs[0])
print(type(dfs))
print(len(dfs))
print(dfs[0])

# Python 測試 BeautifulSoup
#解讀 遠端 網頁資料, 都是使用 html.parser 解析器

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import re
import os
import sys
import csv
import time
import json
import urllib
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)    # 用 requests 的 get 方法把網頁抓下來

    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

def get_soup_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print('無法取得網頁資料')
        sys.exit(1)	#立刻退出程式

    html_data.encoding = 'UTF-8' # 或是 unicode 也可, 指定編碼方式
    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    #soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
    #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
    #pprint.pprint(html_data.text)
    print("取得網頁標題", soup.title)
    return soup
    
print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 1')








print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 2')








print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 3')




print('\n\nBeautifulSoup 測試 作業完成\n')


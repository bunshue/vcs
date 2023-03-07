# Python 新進測試 15

'''
# _*_ coding: utf-8 _*_
# 程式 8-6.py (Python 3 version)

def disp_area():
    i = 0
    for a in climate_data:
        print("{:>2}:{:<6}\t".format(i,a[0]), end="")
        i += 1
        if not (i % 5): print()
    print()

def disp_temp(data):
    print("顯示區域:", data[0])
    print("---------------------")
    for i in range(1,13):
        print("{:>2}月均溫:{:>.1f}度".format(i, float(data[i])))
    print("本地區年均溫為{}度".format(data[13]))
    print("---------------------")

target_file = 'climate.txt'
with open(target_file, 'r', encoding='utf-8') as fp:
    raw_data = fp.readlines()
climate_data=[]
for item in raw_data:
    climate_data.append(item.rstrip('\n').split('\t'))

while True:
    disp_area()
    area = int(input("請輸入你要查詢平均溫度的地區：(-1結束)"))
    if area == -1: break
    disp_temp(climate_data[area])
    x = input("請按Enter鍵回主選單")
'''


'''

# _*_ coding: utf-8 _*_
# 程式 8-7.py (Python 3 version)

import json, datetime

fp = open('earthquake.json','r')
earthquakes = json.load(fp)

print("過去7天全球發生重大的地震資訊：")
for eq in earthquakes['features']:
    print("地點:{}".format(eq['properties']['place']))
    print("震度:{}".format(eq['properties']['mag']))
    et = float(eq['properties']['time']) /1000.0
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("時間:{}".format(d))

'''

'''
# _*_ coding: utf-8 _*_
# 程式 9-2  (Python 3 version)

import requests

url = 'http://udb.moe.edu.tw/Home/About'

html = requests.get(url).text.splitlines()
for i in range(0,15):
    print(html[i])
'''

'''
# _*_ coding: utf-8 _*_
# 程式 9-3 (Python 3 version)

import requests

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的姓名:")
html = requests.get(url).text
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))
'''
    
'''
# _*_ coding: utf-8 *_*
# 程式 9-4 (Python 3 version)

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://icho.chem.ntnu.edu.tw/pub/54con/54con.html'

html = requests.get(url).text

emails = re.findall(regex,html)
for email in emails:
    print(email)
'''

'''
# _*_ coding: utf-8 _*_
# 程式 9-8 (Python 3 version)

from bs4 import BeautifulSoup
import requests

url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'

html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
data = sp.find_all('span', {'id':'Showtd'})
rows = data[0].find_all('tr')

prices = list()
for row in rows:
    cols = row.find_all('td')
    if len(cols[1].text) > 0:
        item = [cols[0].text, cols[1].text, \
                cols[2].text, cols[3].text]
        prices.append(item)
for p in prices:
    print(p)
'''



# _*_ coding: utf-8 _*_
# 程式 10-1.py (Python 3 version)

import sqlite3
from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as pt

def disp_menu():
    print("中油歷年油價查詢系統")
    print("------------")
    print("1.從網站載入最新油價")
    print("2.顯示歷年油價資訊")
    print("3.最近10週油價資訊")
    print("4.油價走勢圖")
    print("0.結束")
    print("------------")

def fetch_data():
    url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'

    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    data = sp.find_all('span', {'id':'Showtd'})
    rows = data[0].find_all('tr')

    prices = list()
    for row in rows:
        cols = row.find_all('td')
        if len(cols[1].text) > 0:
            item = [cols[0].text, cols[1].text, \
                    cols[2].text, cols[3].text]
            prices.append(item)
    for p in prices:
        sqlstr = "select * from prices where gdate='{}';".format(p[0])
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) == 0:
            g92 = 0 if p[1]=='' else float(p[1])
            g95 = 0 if p[2]=='' else float(p[2])
            g98 = 0 if p[3]=='' else float(p[3])
            sqlstr = "insert into prices values('{}', {}, {}, {});". \
                format(p[0], g92, g95, g98)
            print(sqlstr)
            conn.execute(sqlstr)
            conn.commit()


def disp_10data():
    cursor = conn.execute('select * from prices order by gdate desc;')
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". \
            format(row[0],row[1],row[2],row[3]))
        n = n + 1
        if n == 10:
            break

def chart():
    data = []
    cursor = conn.execute('select * from prices order by gdate;')
    for row in cursor:
        data.append(list(row))
    x = np.arange(0,len(data))
    dataset = [list(), list(), list()]
    for i in range(0, len(data)):
        for j in range(0,3):
            dataset[j].append(data[i][j+1])
    w = np.array(dataset[0])
    y = np.array(dataset[1])
    z = np.array(dataset[2])
    pt.ylabel("NTD$")
    pt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))
    pt.plot(x, w, color="blue", label="92")
    pt.plot(x, y, color="red", label="95")
    pt.plot(x, y, color="green", label="98")
    pt.xlim(0,len(data))
    pt.ylim(10,40)
    pt.title("Gasoline Prices Trend (Taiwan)")
    pt.legend()
    pt.show()

def disp_alldata():
    cursor = conn.execute('select * from prices order by gdate desc;')
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". \
            format(row[0],row[1],row[2],row[3]))
        n = n + 1
        if n == 20:
            x = input("請按Enter鍵繼續...(Q:回主選單)")
            if x == 'Q' or x == 'q': break
            n = 0

conn = sqlite3.connect('gasoline.sqlite')

while True:
    disp_menu()
    choice = int(input("請輸入您的選擇:"))
    if choice == 0 : break
    if choice == 1: 
        fetch_data()
    elif choice == 2:
        disp_alldata()
    elif choice == 3:
        disp_10data()
    elif choice == 4:
        chart()
    else: break
    x = input("請按Enter鍵回主選單")








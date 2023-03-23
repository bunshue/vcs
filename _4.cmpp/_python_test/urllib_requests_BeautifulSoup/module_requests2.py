# python import module : requests

import requests
import codecs

api_base_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_base_url, params = api_params)
fo = codecs.open('wiki搜尋結果1.html', 'w', 'utf-8')
#fo = open('wiki搜尋結果222.html', 'w')
fo.write(wiki_data.text)
fo.close()


import requests
import codecs

search_word = 'lion'

api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
wiki_data = requests.get(api_url, params = api_params)
fo = codecs.open('wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8')
#fo = open('bbbbb'+ search_word + '.html', 'w')
fo.write(wiki_data.text)
fo.close()



import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])


import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][0]['telop'])
print(weather_data['forecasts'][1]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][1]['telop'])
print(weather_data['forecasts'][2]['dateLabel'] + '的天氣是：' + weather_data['forecasts'][2]['telop'])


import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
for weather in weather_data['forecasts']:
    print(weather['dateLabel'] + '的天氣是：' + weather['telop'])


import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
for weather in weather_data['forecasts']:
    print(weather)


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("找不到網頁標題")
else:
    print("取得網頁標題:")
    print(title)



'''

import requests

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的姓名:")
html = requests.get(url).text
print(html)
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))
'''
'''
import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://icho.chem.ntnu.edu.tw/pub/54con/54con.html'

html = requests.get(url).text

emails = re.findall(regex,html)
for email in emails:
    print(email)
'''

'''
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

'''
import sqlite3
from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt

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
    plt.ylabel("NTD$")
    plt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))
    plt.plot(x, w, color="blue", label="92")
    plt.plot(x, y, color="red", label="95")
    plt.plot(x, y, color="green", label="98")
    plt.xlim(0,len(data))
    plt.ylim(10,40)
    plt.title("Gasoline Prices Trend (Taiwan)")
    plt.legend()
    plt.show()

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
'''


import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
tree = ET.fromstring(content.text)

print('根目錄標籤：' + tree.tag)
print('根目錄屬性：' + str(tree.attrib))
print('根目錄值：' + str(tree.text))


import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
tree = ET.fromstring(content.text)

item = tree[0].find('item')
print('find 方法：' + item[0].text)

items = tree[0].findall('item')
print('findall 方法：' + items[0][0].text)

items = list(tree.iter(tag='item'))
print('iter 方法：' + items[0][0].text)










print('OK')




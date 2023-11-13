#class_ 的"_"符號是因為class是保留字，所以加上_符號作區別

def disp_menu():
    print('各種網路資料抓取範例')
    print('------------------------')
    print('1.')
    print('2.ptt電影板標題')
    print('3.')
    print('4.世界地震資料 json格式')
    print('5.台灣樂透開彩')
    print('6.取得氣象資料')
    print('7.蘋果日報標題')
    print('0.結束')
    print('------------------------')

import requests
from bs4 import BeautifulSoup
import urllib.parse
import html5lib

#無參數
def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

def example01():
    print('範例01')

def example02():
    url = 'https://www.ptt.cc/bbs/movie/index.html'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    import bs4

    '''
    import urllib
    #建立一個Request物件, 附加Request Headers的資訊
    request = urllib.request.Request(url, headers = headers)
    page = urllib.request.urlopen(request)
    html_data = page.read().decode("utf-8")
    soup = bs4.BeautifulSoup(html_data, "html.parser")
    '''

    import requests
    requests.adapters.DEFAULT_RETRIES = 25
    html_data = requests.get(url, headers = headers)
    soup = bs4.BeautifulSoup(html_data.text, "html.parser")

    print(soup.title)   #抓整個標籤
    print(soup.title.text)  #抓標籤裡面的文字
    print(soup.title.string)#抓標籤裡面的文字

    #尋找class = 'title' 的 div 標籤
    titles = soup.find("div", class_ = "title")

    #尋找所有class = 'title' 的 div 標籤 用列表表示
    titles = soup.find_all("div", class_ = "title")

    #print(titles)
    for title in titles:
        if title.a != None: #如果標題包含a標籤(沒有被刪除), 印出來
            print(title.a.string)
   
def example03():
    return None

def example04():
    print('世界地震資料 json格式')

    import json, requests, datetime
     
    url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'

    html_data = get_html_data1(url)
    if html_data:
        print("擷取網頁資料 OK")
        #print(html_data.text)
    else:
        print('無法取得網頁資料')
        return None
    
    earthquakes = json.loads(html_data.text)
     
    for eq in earthquakes['features']:
        if(float(eq['properties']['mag']) > 5.0):
            eptime = float(eq['properties']['time']) / 1000.0
            d = datetime.datetime.fromtimestamp(eptime).strftime('%Y-%m-%d %H:%M:%S')
            print("{}, 震度:{}, 地點:{}".format(d, eq['properties']['mag'], eq['properties']['place']))

def example05():
    print('台灣樂透開彩')
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.taiwanlottery.com.tw/'
    
    html_data = get_html_data1(url)
    if html_data:
        print("擷取網頁資料 OK")
        #print(html_data.text)
    else:
        print('無法取得網頁資料')
        return None
    
    sp = BeautifulSoup(html_data.text, 'html.parser')
    # 找到威力彩的區塊
    datas = sp.find('div', class_ = 'contents_box02')
    # 開獎期數
    title = datas.find('span', 'font_black15').text
    print('威力彩期數：', title)
    # 開獎號碼
    nums = datas.find_all('div', class_ = 'ball_tx ball_green')
    # 開出順序
    print('開出順序：', end = ' ')
    for i in range(0,6):
        print(nums[i].text, end = ' ')
    # 大小順序
    print('\n大小順序：', end = ' ')
    for i in range(6,12):
        print(nums[i].text, end = ' ')
    # 第二區
    num = datas.find('div', class_ = 'ball_red').text
    print('\n第二區：', num)

#取得氣象資料 ST
import requests
import time
import csv
import random
import socket
import http.client
import bs4
from bs4 import BeautifulSoup

def get_content(url,data = None):
    header = {
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    timeout = random.choice(range(80,180))
    while True:
        try:
            html_data = requests.get(url, headers = header,timeout = timeout)
            html_data.encoding= 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    return html_data.text

def get_data(html_text):
    final=[]
    soup = BeautifulSoup(html_text, "html.parser")  # 創建soup對象
    body = soup.body

    divs = soup.find_all('div', 'crumbs fl')
    print(divs)
    for div in divs:
        print('111')
        print(div)
        for di in div:
            print('222')
            print(di.text.replace('\n', ''))

    data = body.find('div',attrs={'id':'7d'})
    # data = body.find('div',{'div':'7d'})
    print(type(data))
    ul = data.find('ul')
    li =ul.find_all('li')
    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        temp.append(inf[0].string)
        if inf[1].find('span') is None:
            temperature_highest = None
        else:
            temperature_highest = inf[1].find('span').string
            temperature_highestm = temperature_highest.replace("℃","")
        temperature_lowest = inf[1].find('i').string
        temperature_lowest = temperature_lowest.replace('℃','')
        temp.append(temperature_highest)
        temp.append(temperature_lowest)
        final.append(temp)
    return final

def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors = 'ignore', newline = '') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

def example06():
    print('取得氣象資料')
    print('取得氣象資料')
    url = 'http://www.weather.com.cn/weather/101190401.shtml'   #蘇州
    url = 'http://www.weather.com.cn/weather/101340101.shtml'   #台北
    html_data = get_content(url)
    #print(html_data)
    result = get_data(html_data)
    write_data(result, 'weather.csv')

#取得氣象資料 SP
    
def example07():
    print('蘋果日報標題')
    import requests
    import jieba
    import operator
    from bs4 import BeautifulSoup

    url = 'https://tw.nextapple.com/realtime/headlines'

    html_data = get_html_data1(url)
    if html_data:
        print("擷取網頁資料 OK")
        #print(html_data.text)
    else:
        print('無法取得網頁資料')
        return None

    print('html_data.text')
    print(html_data.text)

    news = BeautifulSoup(html_data.text, 'html.parser')
    news_title = news.find_all('div', {'class': 'post-inner'})
    '''
    print('news_title')
    print(news_title)
    '''

    headlines = ''
    for t in news_title:
            title = t.find_all('a')[0]
            headlines += title.text
            print(title.text)

    '''
    print('headlines')
    print(headlines)
    '''	

    words = jieba.cut(headlines)

    word_count = dict()

    for word in words:
            if word in word_count.keys():
                    word_count[word] += 1
            else:
                    word_count[word] = 1

            sorted_wc = sorted(word_count.items(), key = operator.itemgetter(1), reverse = True)

    '''
    for item in sorted_wc:
            if item[1] > 1:
                    print(item)
            else:
                    break
    '''

    print('done')

def example08():
    print('範例08')

def example09():
    print('範例09')

while True:
    print()
    disp_menu()
    sel = input("請輸入您的選擇:")
    if sel < '0' or sel > '9':
        continue
    
    choice = int(sel)
    if choice == 0 :
        break
    if choice == 1: 
        example01()
    elif choice == 2:
        example02()
    elif choice == 3:
        example03()
    elif choice == 4:
        example04()
    elif choice == 5:
        example05()
    elif choice == 6:
        example06()
    elif choice == 7:
        example07()
    elif choice == 8:
        example08()
    elif choice == 9:
        example09()
    else:
        break





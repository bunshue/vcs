#class_ 的"_"符號是因為class是保留字，所以加上_符號作區別

def disp_menu():
    print('各種網路資料抓取範例')
    print('------------------------')
    print('1.Yahoo字典')
    print('2.ptt電影板標題')
    print('3.統一發票號碼')
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

#Yahoo字典 ST
def searchdic(search_word):
    #yahoo字典的網址，可修改網址查詢想要的單字，網址當中的%s為格式化字串
    url = "https://tw.dictionary.search.yahoo.com/search?p=%s" % (search_word)
    html_data = get_html_data1(url)
    if html_data:
        print("擷取網頁資料 OK")
        #print(html_data.text)
    else:
        print('無法取得網頁資料')
        return None

    soup = BeautifulSoup(html_data.text, "html.parser")
    #soup = BeautifulSoup(html_data.text, 'html5lib')   #也可
    #soup = BeautifulSoup(html_data.text, 'lxml')   # 指定 lxml 作為解析器
    #print(soup.prettify()) # 把排版後的 html 印出來

    '''
    # 一些屬性或方法, BeautifulSoup的用法
    print('---title---')
    print(soup.title) # 把 tag 抓出來
    print('---title.name---')
    print(soup.title.name) # 把 title 的 tag 名稱抓出來
    print('---title.string---')
    print(soup.title.string) # 把 title tag 的內容抓出來
    print('---title.parent.name---')
    print(soup.title.parent.name) # title tag 的上一層 tag
    print('---a---')
    print(soup.a) # 把第一個 <a></a> 抓出來
    print('---all a---')
    print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
    print('---all div---')
    print(soup.find_all('div')) # 把所有的 <a></a> 抓出來
    '''

    print('上框')
    print('上框 搜尋英文字 :')
    search_word = soup.find_all('span', class_='fz-24 fw-500 c-black lh-24')
    for sw in search_word:
        for di in sw:
            print(di.text.replace('\n', ''))

    print('上框 音標 :')
    
    #音標
    pronunciation = soup.find_all('span',class_='fz-14')
    print('000', pronunciation[0].text) #第0個是KK音標
    print('111', pronunciation[1].text) #第1個是DJ音標

    print('上框 詞性 :')
    divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
  
    #print(divs)
    for div in divs:
        #print(div)
        for di in div:
            for tt in di.find_all('li'):
                cc = tt.find('div', 'pos_button fz-14 fl-l mr-12')
                if cc != None: #如果標題包含資料, 印出來
                    print('詞性')
                    print(cc.text.replace('\n', '')) #只是刪除換行符號, 或許不一定有
                
                dd = tt.find('div', 'fz-16 fl-l dictionaryExplanation')
                if dd != None: #如果標題包含資料, 印出來
                    print('解釋')
                    print(dd.text.replace('\n', '')) #只是刪除換行符號, 或許不一定有

    print('中框')
    print('中框 釋義 :')

    divs = soup.find_all('div', class_ = 'grp grp-tab-content-explanation tabsContent-s tab-content-explanation pt-24 tabActived')    #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
    #print(divs)
    
    if divs == []:
        return

    div1 = divs[0].find_all('div', 'compTitle lh-25')
    length = len(div1)
    #print('a共找到', length, '筆資料')

    div2 = divs[0].find_all('div', 'compTextList ml-50')
    length = len(div2)
    #print('b共找到', length, '筆資料')

    # 依照詞性數量的區塊做迴圈，將一個一個區塊作處理
    for nn in range(length):
        ''' debug
        print(nn)
        print('--------------------')
        print(div1[nn])   # 使用索引值, 只印出text部分
        print('--------------------')
        print(div2[nn])   # 使用索引值, 只印出text部分
        print('--------------------')
        '''
        print('詞性')
        print(div1[nn].find('span', 'pos_button fz-14').text.replace('\n', ''), end = "") #只是刪除換行符號, 或許不一定有
        print(div1[nn].find('span', 'fz-14 va-mid lh-22 ml-5').text.replace('\n', '')) #只是刪除換行符號, 或許不一定有

        print('解釋:')
        nnn2 = div2[nn].find_all('span')
        #print(nnn)
        # 這個迴圈將詞性區塊裡的單字意思一個一個抓出來顯示
        # 而每個單字意思及例句都是使用li標籤所包起來，所以將每個li標籤抓出來顯示他的單字意思及例句
        for n in nnn2:
            #print(n)
            for di in n:
                print(di.text.replace('\n', ''), end = "")
            print()

def example01():
    print('Yahoo字典')
    search_word = 'coordinate'
    #search_word = '英國'
    searchdic(search_word)

    print('Yahoo字典')
    print('------------------------------')
    search_word = 'oat'
    searchdic(search_word)
    print('------------------------------')
    
    search_word = '英國'
    searchdic(search_word)
    print('------------------------------')

#Yahoo字典 SP

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
    titles = soup.find("div", class_= "title")

    #尋找所有class = 'title' 的 div 標籤 用列表表示
    titles = soup.find_all("div", class_= "title")

    #print(titles)
    for title in titles:
        if title.a != None: #如果標題包含a標籤(沒有被刪除), 印出來
            print(title.a.string)
   
def example03():
    print("3.統一發票號碼")
    import requests

    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET

    url = 'http://invoice.etax.nat.gov.tw/invoice.xml'   #統一發票中獎號碼
    html_data = get_html_data1(url)
    if html_data:
        print("擷取網頁資料 OK")
        #print(html_data.text)
    else:
        print('無法取得網頁資料')
        return None
    
    print('1111')
    #print(html_data.text)
    tree = ET.fromstring(html_data.text)
    print('2222')
    print(tree)
    print('根目錄標籤：' + tree.tag)
    print('根目錄屬性：' + str(tree.attrib))
    print('根目錄值：' + str(tree.text))

    item = tree[0].find('item')
    print('find 方法：' + item[0].text)

    items = tree[0].findall('item')
    print('findall 方法：' + items[0][0].text)

    items = list(tree.iter(tag='item'))
    print('iter 方法：' + items[0][0].text)

    import requests
    url = 'https://invoice.etax.nat.gov.tw/index.html'
    # 取得網頁html
    web = get_html_data1(url)    
    # 設置編碼，避免中文亂碼
    web.encoding='utf-8'       

    from bs4 import BeautifulSoup
    # 轉換成標籤樹
    tree = BeautifulSoup(web.text, "html.parser")  
    # 取出開獎月份
    issue = tree.select(".carousel-item")[0].getText(); 
    print(issue)
    # 取出中獎號碼陣列
    winlist = tree.select('.container-fluid')[0].select('.etw-tbiggest')  
    #特別獎
    nss = winlist[0].getText()  
    #特獎
    ns = winlist[1].getText() 
    # 頭獎
    n1 = [winlist[2].getText()[-8:], winlist[3].getText()[-8:], winlist[4].getText()[-8:]] 
    print("特別獎:\n" + "　　"+nss + "\n")
    print("特獎:\n"+"　　" + ns + "\n")
    print("頭獎:")
    for j in n1:
      print("　　"+j)
    print("\n")

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
        if(float(eq['properties']['mag'])>5.0):
            eptime = float(eq['properties']['time']) /1000.0
            d = datetime.datetime.fromtimestamp(eptime). strftime('%Y-%m-%d %H:%M:%S')
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
    datas = sp.find('div', class_='contents_box02')
    # 開獎期數
    title = datas.find('span', 'font_black15').text
    print('威力彩期數：', title)
    # 開獎號碼
    nums = datas.find_all('div', class_='ball_tx ball_green')
    # 開出順序
    print('開出順序：', end=' ')
    for i in range(0,6):
        print(nums[i].text, end=' ')
    # 大小順序
    print('\n大小順序：', end=' ')
    for i in range(6,12):
        print(nums[i].text, end=' ')
    # 第二區
    num = datas.find('div', class_='ball_red').text
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
            temperature_highest=inf[1].find('span').string
            temperature_highestm  =temperature_highest.replace("℃","")
        temperature_lowest = inf[1].find('i').string
        temperature_lowest = temperature_lowest.replace('℃','')
        temp.append(temperature_highest)
        temp.append(temperature_lowest)
        final.append(temp)
    return final

def write_data(data, name):
    file_name =name
    with open(file_name, 'a', errors = 'ignore', newline = '') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

def example06():
    print('取得氣象資料')
    print('取得氣象資料')
    url = 'http://www.weather.com.cn/weather/101190401.shtml'   #蘇州
    url = 'http://www.weather.com.cn/weather/101340101.shtml'  #台北
    html_data = get_content(url)
    #print(html_data)
    result = get_data(html_data)
    write_data(result,'weather.csv')

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

            sorted_wc = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

    '''
    for item in sorted_wc:
            if item[1]>1:
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





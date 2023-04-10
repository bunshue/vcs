def disp_menu():
    print('各種網路資料抓取範例')
    print('------------------------')
    print('1.Yahoo字典1')
    print('2.Yahoo字典2')
    print('3.統一發票號碼')
    print('4.世界地震資料 json格式')
    print('5.台灣樂透開彩')
    print('6.取得氣象資料')
    print('7.蘋果日報標題')
    print('8.Yahoo字典1b')
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

#Yahoo字典1 ST

YAHOO_DICTIONARY_URL = "https://tw.dictionary.yahoo.com/dictionary?p="
YAHOO_REFERER_VALUE  = "https://tw.dictionary.yahoo.com/dictionary"

def searchdic1(search_word):

    search_word = urllib.parse.quote_plus(search_word)
    #print(YAHOO_DICTIONARY_URL + search_word)
    html_data = requests.get(YAHOO_DICTIONARY_URL + search_word, headers={'Referer': YAHOO_REFERER_VALUE})
    if html_data.status_code != 200:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Invalid url: ', html_data.url)
        return None
    else:
        page = html_data.text

        #get_dict_info(page)
        #soup = BeautifulSoup(page, 'html5lib')   #也可
        soup = BeautifulSoup(page, 'lxml')   # 指定 lxml 作為解析器
        #print(soup.prettify()) # 把排版後的 html 印出來
        #print(soup.text)

        '''
        print(soup.prettify()) # 把排版後的 html 印出來
        # 一些屬性或方法
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

        divs = soup.find_all('span', 'fz-24 fw-500 c-black lh-24')
        print('搜尋英文字 :')
        #print(divs)
        for div in divs:
            #print(div)
            for di in div:
                print(di.text.replace('\n', ''))

        print('主解釋 :')
        #divs = soup.find_all('div', 'fz-16 fl-l dictionaryExplanation')
        divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
        #print(divs)
        for div in divs:
            #print(div)
            for di in div:
                #print(di)
                print(di.text.replace('\n', ''))    #只是刪除換行符號, 或許不一定有

        print('釋義 :')
        #divs = soup.find_all('span', 'fz-14')
        divs = soup.find_all('span', 'd-i fz-14 lh-20')
        #print(divs)
        i = 1
        for div in divs:
            for di in div:
                print(i)
                print(di.text.replace('\n', ''))
                i = i + 1

def example01():
    print('Yahoo字典1')
    search_word1 = 'oat'
    #search_word1 = '英國'
    searchdic1(search_word1)

#Yahoo字典1 SP

#Yahoo字典1b ST
'''
此方法是使用yahoo字典檢視網頁原始碼查找要抓取的資料段落及屬性
然後將要的資料一層一層剖析出來
'''

def searchdic1b(search_word):

    #yahoo字典的網址，可修改網址查詢想要的單字，網址當中的%s為格式化字串
    url = "https://tw.dictionary.search.yahoo.com/search?p=%s&fr2=dict" % (search_word)
    html_data = get_html_data1(url)
    if html_data:
        print("擷取網頁資料 OK")
        #print(html_data.text)
    else:
        print('無法取得網頁資料')

    soup = BeautifulSoup(html_data.text, "html.parser")
    #print(soup.prettify()) # 把排版後的 html 印出來

    try:
        mainBlock = soup.find_all('div', class_='grp grp-main pl-25')

        #print(mainBlock)
        #print(mainBlock[0].find_all('span', class_='fz-24 fw-500 c-black lh-24'))
        #class_ 的"_"符號是因為class是保留字，所以加上_符號作區別
        search_word = mainBlock[0].find_all('span', class_='fz-24 fw-500 c-black lh-24')
        print('搜尋英文字 :')
        #print(search_word)
        for sw in search_word:
            #print(sw)
            for di in sw:
                print(di.text.replace('\n', ''))
    except:
        print("查詢錯誤")
                  
    else:
        print('找出音標並print出來')
        pronunciation = soup.find_all('span',class_='fz-14')
        print('000', pronunciation[0].text) #第0個是KK音標
        print('111', pronunciation[1].text) #第1個是DJ音標

        pos = soup.find_all('li', class_='lh-22 mh-22 mt-12 mb-12 mr-25 last')
        #print(pos)
        nnn = pos[0].find_all('div')
        #print(nnn)
        for n in nnn:
            #print(n)
            for di in n:
                print(di.text.replace('\n', ''))

        print('釋義:')
        meaning = soup.find_all('div', class_='grp grp-tab-content-explanation tabsContent-s tab-content-explanation pt-24 tabActived')
        #print(meaning)
        print('詞性:')
        nnn = meaning[0].find_all('div', class_='compTitle lh-25')
        nnn2 = nnn[0].find_all('span')
        #print(nnn)
        for n in nnn2:
            #print(n)
            for di in n:
                print(di.text.replace('\n', ''))
        print('解釋:')
        nnn = meaning[0].find_all('div', class_='compTextList ml-50')
        nnn2 = nnn[0].find_all('span')
        #print(nnn)
        for n in nnn2:
            #print(n)
            for di in n:
                print(di.text.replace('\n', ''))


'''   old
        
        allBlock = soup.find_all('div', class_='compTitle mt-25 mb-10')
        meaningBlock = allBlock[0].find_all('span', class_='fz-24 fw-500 c-black lh-24')

        # 先找出詞性，詞性使用h3標籤，但在allBlock裡沒有其他h3標籤，所以就不指定class了
        parts = allBlock[0].find_all('h3')
        print((len(meaningBlock)))
        # 依照詞性數量的區塊做迴圈，將一個一個區塊作處理
        for i in range(len(meaningBlock)):
            # 顯示方面我們先顯示詞性值，後續再顯示單字意思
            print(parts[i].text)
            
            # 這個迴圈將詞性區塊裡的單字意思一個一個抓出來顯示
            # 而每個單字意思及例句都是使用li標籤所包起來，所以將每個li標籤抓出來顯示他的單字意思及例句
            for j in meaningBlock[i].find_all('li'):
                # 印出其中一個單字意思，單字意思是使用h4標籤，可如下對j抓取它的指定下一層標籤h4
                print("\t"+j.h4.text)
                hasES=False
                # 有些單字意思沒例句會出錯，所以對沒有例句的意思做例外跳過
                try:
                    #由於有些解釋有多個例句，因此去找所有例句
                    exampleSentence =j.find_all('span')
                    #第一個span會抓到中文意思，因此跳過，後面的例句每句後面都會多抓到一次中文解釋，因此k=k+2
                    for k in range(1, len(exampleSentence),2):
                        #有時會抓到雖然沒例句但是卻有span的時候，內容會是空白，因此過濾掉
                        if exampleSentence[k].text!=' ':
                            print("\t\t例句："+exampleSentence[k].text)
                            hasES=True
                except:
                    #跳過沒抓到span的
                    pass
                #如果沒例句時所作的處理
                if hasES==False:
                    print("\t\t沒例句。")
'''

def example01b():
    print('Yahoo字典1b')
    search_word1b = 'oat'
    #search_word1b = '英國'
    searchdic1b(search_word1b)

#Yahoo字典1b ST
    
#Yahoo字典2 ST

import requests
from bs4 import BeautifulSoup

def searchdic2(search_word):
  a = "https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXGvbWIJibWYAFCp9rolQ"
  b = ";_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkAwRuX3JzbHQDMARuX3N1Z2cDMARvcmlnaW4DdHcuZGljdGlvbmFyeS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM0BHF1ZXJ5A3RhcGUEdF9zdG1wAzE2NTI3MDk5NTM-?"
  c = "p="
  e = "&fr2=sb-top&fr=sfp"
  search = a + b + c + search_word + e
  
  html_data = get_html_data1(search)
  if html_data:
      print("擷取網頁資料 OK")
      #print(html_data.text)
      page = html_data.text
  else:
      print('無法取得網頁資料')
      return None
  
  soup = BeautifulSoup(page, 'html.parser')
  #print(soup.prettify()) # 把排版後的 html 印出來

  '''
  print('主解釋 :')
  divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
  #print(divs)
  for div in divs:
    #print(div)
    lis = div.find_all('li')  #把li下的所有資料印出來
    for li in lis:
      print('2')
      print(li)
      print(li.text.replace('\n', ''))
  '''
  '''
  print(soup.prettify()) # 把排版後的 html 印出來
  # 一些屬性或方法
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

  divs = soup.find_all('span', 'fz-24 fw-500 c-black lh-24')
  print('搜尋英文字 :')
  #print(divs)
  for div in divs:
      #print(div)
      for di in div:
          print(di.text.replace('\n', ''))

  print('主解釋 :')
  #divs = soup.find_all('div', 'fz-16 fl-l dictionaryExplanation')
  divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
  #print(divs)
  for div in divs:
      #print(div)
      for di in div:
          #print(di)
          print(di.text.replace('\n', ''))    #只是刪除換行符號, 或許不一定有

  print('釋義 :')        
  #divs = soup.find_all('span', 'fz-14')
  divs = soup.find_all('span', 'd-i fz-14 lh-20')
  #print(divs)
  i = 1
  for div in divs:
      for di in div:
          print(i)
          print(di.text.replace('\n', ''))
          i = i + 1

def example02():
    print('Yahoo字典2')
    search_word2 = 'oat'
    #search_word2 = '英國'
    searchdic2(search_word2)

#Yahoo字典2 SP
    
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
            html_data = requests.get(url,headers =header,timeout = timeout)
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
        #example08()
        example01b()
    elif choice == 9:
        example09()
    else:
        break





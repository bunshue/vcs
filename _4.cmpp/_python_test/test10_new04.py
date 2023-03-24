import requests
from bs4 import BeautifulSoup
import urllib.parse
import html5lib

YAHOO_DICTIONARY_URL = "https://tw.dictionary.yahoo.com/dictionary?p="
YAHOO_REFERER_VALUE = "https://tw.dictionary.yahoo.com/dictionary"

def get_web_content(url, query):
    query = urllib.parse.quote_plus(query)
    resp = requests.get(url + query, headers={'Referer': YAHOO_REFERER_VALUE})
    if resp.status_code != 200:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Invalid url: ', resp.url)
        return None
    else:
        return resp.text

def get_dict_info(dom):
    #soup = BeautifulSoup(dom, 'html5lib')
    soup = BeautifulSoup(dom, 'lxml')
    #print(soup.text)

    #soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
    #print(soup.prettify()) # 把排版後的 html 印出來

    '''
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

    divs = soup.find_all('div', 'fz-16 fl-l dictionaryExplanation')

    #print(divs)

    for div in divs:
        #print('div')
        #print(div)
        for di in div:
            #print('get data')
            print(di.text.replace('\n', ''))

    ''' old
    for explain in soup.find('ul', 'explanations').find_all('li', 'exp-item'):
        print(explain.text)
    '''


page = get_web_content(YAHOO_DICTIONARY_URL, 'scholarship')
if page:
    get_dict_info(page)





'''

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
            rep = requests.get(url,headers =header,timeout = timeout)
            rep.encoding= 'utf-8'
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
    return rep.text

def get_data(html_text):
    final=[]
    bs = BeautifulSoup(html_text,"html.parser")  # 創建BS對象
    body = bs.body
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

def write_data(data,name):
    file_name =name
    with open(file_name,'a',errors='ignore',newline='') as f:
        f_csv =csv.writer(f)
        f_csv.writerows(data)

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101190401.shtml'
    html = get_content(url)
    result = get_data(html)
    write_data(result,'weather.csv')

    

'''



'''
import requests as rq
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板
response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
#print(soup.prettify()) # 把排版後的 html 印出來

# 一些屬性或方法
print(soup.title) # 把 tag 抓出來
print("---")
print(soup.title.name) # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string) # 把 title tag 的內容欻出來
print("---")
print(soup.title.parent.name) # title tag 的上一層 tag
print("---")
print(soup.a) # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來

'''


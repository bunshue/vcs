import requests
from bs4 import BeautifulSoup
import urllib.parse
import html5lib

YAHOO_DICTIONARY_URL = "https://tw.dictionary.yahoo.com/dictionary?p="
YAHOO_REFERER_VALUE  = "https://tw.dictionary.yahoo.com/dictionary"

def searchdic1(search_word):

    search_word = urllib.parse.quote_plus(search_word)
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

example01()






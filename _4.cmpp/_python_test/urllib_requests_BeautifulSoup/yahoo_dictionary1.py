import requests
from bs4 import BeautifulSoup
import urllib.parse
import html5lib

YAHOO_DICTIONARY_URL = "https://tw.dictionary.yahoo.com/dictionary?p="
YAHOO_REFERER_VALUE  = "https://tw.dictionary.yahoo.com/dictionary"

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
    #soup = BeautifulSoup(dom, 'html5lib')   #也可
    soup = BeautifulSoup(dom, 'lxml')   # 指定 lxml 作為解析器
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

    divs = soup.find_all('div', 'fz-16 fl-l dictionaryExplanation')
    #print(divs)

    for div in divs:
        for di in div:
            print(di.text.replace('\n', ''))

search_word = 'substitution'
page = get_web_content(YAHOO_DICTIONARY_URL, search_word)
if page:
    search_result = get_dict_info(page)
else:
    print('找不到資料')



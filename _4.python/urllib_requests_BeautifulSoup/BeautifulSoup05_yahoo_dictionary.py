#class_ 的"_"符號是因為class是保留字，所以加上_符號作區別

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
    result = ""

    #yahoo字典的網址，可修改網址查詢想要的單字，網址當中的%s為格式化字串
    url = "https://tw.dictionary.search.yahoo.com/search?p=%s" % (search_word)
    html_data = get_html_data1(url)
    ''' same
    payload = {'p': search_word}
    html_data = requests.get('https://tw.dictionary.search.yahoo.com/search?', params = payload)
    #相當於寫了 : https://tw.dictionary.search.yahoo.com/search?p=search_word
    '''
    
    if html_data:
        result += '擷取網頁資料 OK\n'
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

    result += '上框\n'
    result += '上框 搜尋英文字 :\n'
    search_word = soup.find_all('span', class_='fz-24 fw-500 c-black lh-24')
    for sw in search_word:
        for di in sw:
            result += di.text.replace('\n', '')+'\n'

    result += '上框 音標 :\n'
    
    #音標
    pronunciation = soup.find_all('span',class_='fz-14')
    result += '000'+ pronunciation[0].text+'\n' #第0個是KK音標
    result += '111'+ pronunciation[1].text+'\n' #第1個是DJ音標

    result += '上框 詞性 :\n'
    divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
  
    #print(divs)
    for div in divs:
        #print(div)
        for di in div:
            for tt in di.find_all('li'):
                cc = tt.find('div', 'pos_button fz-14 fl-l mr-12')
                if cc != None: #如果標題包含資料, 印出來
                    result += '詞性\n'
                    result += cc.text.replace('\n', '') + '\n' #只是刪除換行符號, 或許不一定有
                
                dd = tt.find('div', 'fz-16 fl-l dictionaryExplanation')
                if dd != None: #如果標題包含資料, 印出來
                    result += '解釋\n'
                    result += dd.text.replace('\n', '') + '\n' #只是刪除換行符號, 或許不一定有

    result += '中框\n'
    result += '中框 釋義 :\n'

    divs = soup.find_all('div', class_ = 'grp grp-tab-content-explanation tabsContent-s tab-content-explanation pt-24 tabActived')    #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
    #print(divs)
    
    if divs == []:
        return result

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
        result += '詞性\n'
        result += div1[nn].find('span', 'pos_button fz-14').text.replace('\n', '')              #只是刪除換行符號, 或許不一定有
        result += div1[nn].find('span', 'fz-14 va-mid lh-22 ml-5').text.replace('\n', '') +'\n' #只是刪除換行符號, 或許不一定有

        result += '解釋:\n'
        nnn2 = div2[nn].find_all('span')
        #print(nnn)
        # 這個迴圈將詞性區塊裡的單字意思一個一個抓出來顯示
        # 而每個單字意思及例句都是使用li標籤所包起來，所以將每個li標籤抓出來顯示他的單字意思及例句
        for n in nnn2:
            #print(n)
            for di in n:
                result += di.text.replace('\n', '')
            result += '\n'
    return result
#Yahoo字典 SP

'''test
print('------------------------------')
print('Yahoo字典')
search_word = 'coordinate'
#search_word = '英國'
result = searchdic(search_word)
print(result)
print('------------------------------')
print('Yahoo字典')
search_word = 'oat'
result = searchdic(search_word)
print(result)
print('------------------------------')
search_word = '英國'
result = searchdic(search_word)
print(result)
print('------------------------------')
'''

while True:
    print()
    search_word = input("請輸入查詢單字 : ")
    result = searchdic(search_word)
    print(result)
    

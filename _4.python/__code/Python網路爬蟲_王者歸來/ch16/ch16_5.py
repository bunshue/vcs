# ch16_5.py
import requests, bs4

url = 'https://www.biqukan.com/50_50096/18520412.html'  # 第一回的網址
htmlfile = requests.get(url)
htmlfile.encoding = 'gbk'
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
title = objSoup.find('h1')                              # 第一回標題
print(title.text)                                       # 列印第一回標題
print()
contents = objSoup.find('div', id='content')            # 內文位置
print('區塊數量 : ', len(contents))
for content in contents:
    print(' ============================================ ')
    print('資料型態 : ', type(content))
    if type(content) == bs4.element.NavigableString:
        txt = content.strip()                           # 列印內文
        print(txt)
          


    






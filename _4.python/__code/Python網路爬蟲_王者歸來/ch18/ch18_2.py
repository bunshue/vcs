# ch18_2.py
import requests, bs4

url = 'https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A3%BD%E9%80%A0'
tsmchtml = requests.get(url)
objSoup = bs4.BeautifulSoup(tsmchtml.text, 'lxml')
tsmc = objSoup.find('tbody')
for t in tsmc:
    col = t.find('th', 'fn org')                    # 標題
    if col:
        print(col.text.strip())
    col = t.find('th', scope='row')                 # 欄位名稱
    if col:
        print(col.text.strip(), ': ', end='')
    col = t.find('td')                              # 欄位內容
    if col:
        print(col.text.strip())
    













# ch18_3.py
import requests, bs4

url = 'https://zh.wikipedia.org/wiki/台灣積體電路製造'
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
    













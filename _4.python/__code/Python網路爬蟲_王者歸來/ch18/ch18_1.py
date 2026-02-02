# ch18_1.py
import requests, bs4

url = 'https://zh.wikipedia.org/'
url_tsmc = 'https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A3%BD%E9%80%A0'
tsmchtml = requests.get(url_tsmc)
objSoup = bs4.BeautifulSoup(tsmchtml.text, 'lxml')
tsmc = objSoup.find('div', id='content')        # 標題
print(tsmc.h1.text)                         

wi = tsmc.find('div', id='siteSub')             # 維基百科
print(wi.text)

info = tsmc.find('p')                           # 台積電主文
print(info.text)






    













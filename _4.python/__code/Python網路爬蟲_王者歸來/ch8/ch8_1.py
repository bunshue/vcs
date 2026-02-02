# ch8_1.py
import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
print("列印BeautifulSoup物件資料型態 ", type(objSoup))













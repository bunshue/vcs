# ch8_10.py
import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

div_page = objSoup.find('div', 'btn-group-paging')
last_page = div_page.find_all('a')[1]
print(type(last_page))              # 列出last_page資料型態
print(last_page)                    # 列出last_page














    


















# ch8_13.py
import requests, bs4

url = 'https://www.ptt.cc/bbs/beauty/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

articles = 0                # 本頁面文章數量
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        articles += 1        
print('本頁的文章數量 = ', articles)














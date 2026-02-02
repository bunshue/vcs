# ch8_15.py
import requests, bs4

url_ppt = 'https://www.ptt.cc'
beauty = '/bbs/beauty/index.html'

ptthtml = requests.get(url_ppt+beauty, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

pttdivs = objSoup.find_all('div', 'r-ent')
href = pttdivs[0].find('a')['href']                                 # 文章超連結

print('目前連線網址 : ', url_ppt+href)
beauty_html = requests.get(url_ppt+href, cookies={'over18':'1'})    # 進入超連結
beauty_soup = bs4.BeautifulSoup(beauty_html.text, 'lxml')   

beauty_divs = beauty_soup.find('div', id='main-content')
items = beauty_divs.find_all('div', 'article-metaline')

for item in items:                                                  # 列印標題
    field = item.find('span', 'article-meta-tag')
    print(field.text,end=' : ')
    field_data = item.find('span', 'article-meta-value')
    print(field_data.text)

mylist = list(beauty_divs)                                          # 轉成串列
print('內文 : ', mylist[4].strip())                                 # 列印本文

    

















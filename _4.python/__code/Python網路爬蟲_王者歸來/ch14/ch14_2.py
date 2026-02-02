# ch14_2.py
import requests, bs4

#url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = 'https://www.dcard.tw/f'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
items = objSoup.find_all('div', 'PostList_entry_1rq5Lf')
print(items[0].h3.text)                                     # 列出第1篇貼文標題
print(items[1].h3.text)                                     # 列出第2篇貼文標題












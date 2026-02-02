# ch14_5.py
import requests, bs4

#url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = 'https://www.dcard.tw/f'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
try:
    items = objSoup.find_all('div', 'PostList_entry_1rq5Lf')
    header = items[0].find('span', 'bOzcuu')
    print('貼文論壇 : ', header.text)
    author = items[0].find('span', 'PostAuthor_root_3vAJfe')
    print('貼文學校 : ', author.text)
    time = items[0].find('span', 'MDszy')
    print('貼文時間 : ', time.text)
    print('貼文標題 : ', items[0].h3.text)
    print('貼文內容 : ', items[0].text)
    bookmark = items[0].find('div', 'cGEHtj')
    print('按讚人數 : ', bookmark.text)
    spanmark = items[0].find('span', 'hkpJwJ')
    print('貼文回應 : ', spanmark.text)
    link = items[0].find('a')['href']
    print('貼文連結 : ', link)
except UnicodeEncodeError:
    print("UnicodeEncodeError")












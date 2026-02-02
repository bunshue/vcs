# ch14_6.py
import requests, bs4

#url = 'https://www.dcard.tw/f?latest=false'                # 這個URL也可以
url = 'https://www.dcard.tw/f'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
items = objSoup.find_all('div', 'PostList_entry_1rq5Lf')
print('取得文章數量 = ', len(items))
for item in items:
    try:
        header = item.find('span', 'bOzcuu')
        print(header.text, '  ', end='')
        author = item.find('span', 'PostAuthor_root_3vAJfe')
        print(author.text, '', end='')
        time = item.find('span', 'MDszy')
        print(time.text)
        print(item.h3.text)
        print(item.text)
        bookmark = item.find('div', 'cGEHtj')
        print(bookmark.text)
        spanmark = item.find('span', 'hkpJwJ')
        print(spanmark.text)
        link = item.find('a')['href']
        print(link)
    except UnicodeEncodeError:
        print("UnicodeEncodeError")
    print()
    











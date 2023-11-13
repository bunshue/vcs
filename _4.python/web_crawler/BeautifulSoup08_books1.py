#有參數 之 requests.get

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}

url = 'https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020'#old
url = 'https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_021'

html_data = requests.get(url, headers = headers)

soup = BeautifulSoup(html_data.text, "html.parser")
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

sel = 'li.item'
ranking = soup.select(sel)

#print(ranking)

print()
print()
print()

cnt = 0;
for rank, book in enumerate(ranking, 1):
    print(book)
    '''
    title = book.h4.a.text
    detail = book.find_all("li")
    author = detail[0].text
    price = detail[1].text
    print(rank, title, author, price)

    print("第{}名".format(rank))
    print(book.h4.a.text)
    detail = book.find_all('a')
    print(detail[0].text)
    print(detail[1].text)
    '''
    print("----")
    cnt += 1
    if cnt == 10:
        break

print("Done")

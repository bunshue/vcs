import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}

url = 'https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020'

html_data = requests.get(url, headers=headers)

from pprint import pprint

soup = BeautifulSoup(html_data.text, "html.parser")
sel = 'li.item'
ranking = soup.select(sel)

print(ranking)

for no, book in enumerate(ranking, 1):
    print("第{}名".format(no))
    #print(book.h4.a.text)
    detail = book.find_all('a')
    #print(detail[0].text)
    #print(detail[1].text)
    print("----")


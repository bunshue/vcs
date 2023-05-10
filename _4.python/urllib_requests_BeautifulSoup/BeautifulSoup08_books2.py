import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}
html = requests.get("https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020",headers=headers).text

sql = """
insert into `ranking30` (`rank`, `title`, `author`, `price`) 
    values({},'{}','{}','{}');
"""
soup = BeautifulSoup(html,"html.parser")
sel = 'li.item'

ranking = soup.select(sel)

for rank, book in enumerate(ranking, 1):
    print(book)
    '''
    title = book.h4.a.text
    detail = book.find_all("li")
    author = detail[0].text
    price = detail[1].text
    print(rank, title, author, price)
    print(sql.format(rank, title, author, price))
    '''

print("Done")


import requests
from bs4 import BeautifulSoup

url = 'https://www.bagong.cn/dog/'

html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

photos = soup.find_all('img')
for photo in photos:
    if photo['src'].startswith('http'):
        print(photo['src'])

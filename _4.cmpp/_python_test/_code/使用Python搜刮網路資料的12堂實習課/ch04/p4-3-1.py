import requests
from bs4 import BeautifulSoup

url = 'https://udn.com/news/breaknews/1'

html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

links = soup.find_all(class_='story-list__text')
for link in links:
    title = link.find('h3')
    try:
        print(title.a['title'])
        print(title.a['href'])
    except:
        pass
    

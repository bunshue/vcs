import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://udn.com/news/breaknews/1'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

links = soup.find_all(class_='story-list__text')
headlines = list()
for link in links:
    title = link.find('h3')
    try:
        item = dict()
        item['title'] = title.a['title']
        if not title.a['href'].startswith('http'):
            item['link'] = "https://udn.com{}".format(title.a['href'])
        else:
            item['link'] = title.a['href']
        headlines.append(item)
    except:
        pass

now = datetime.now()
filename = now.strftime("%y-%m-%d-%H-%M-%S.json")
with open(filename, "w", encoding='utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(headlines, fp)
print(headlines)

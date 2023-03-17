import requests
from bs4 import BeautifulSoup

url = 'https://tw.nextapple.com/realtime/headlines'

#url = 'http://www.appledaily.com.tw/appledaily/hotdaily/headline'

news_page = requests.get(url)

print(news_page.text)

news = BeautifulSoup(news_page.text, 'html.parser')

news_title = news.find_all('div', {'class': 'aht_title'})

print(news_title)

headlines = ''

for t in news_title:
	title = t.find_all('a')[0]
	headlines += title.text

print('headlines')
print(headlines)
	

# Python 新進測試 13



from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

import requests

from bs4 import BeautifulSoup

html_data = requests.get('http://tw.yahoo.com')

soup = BeautifulSoup(html_data.text, "html.parser")

soup.title


import requests

from bs4 import BeautifulSoup

yahoo_news_xml = requests.get('https://tw.news.yahoo.com/rss/technology')

soup = BeautifulSoup(yahoo_news_xml.text, "html.parser")

type(soup)

soup.findAll('item')



for news in soup.findAll('item'):

	print(news.title)

import requests

from bs4 import BeautifulSoup

game_raking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=Android')

game_raking_html.encoding = 'UTF-8'

soup = BeautifulSoup(game_raking_html.text, "html.parser")

soup.find(class_='ACG-mainbox1').find(class_='ACG-maintitle').find('a').string



for game in soup.findAll(class_='ACG-mainbox1'):
	print(game.find(class_='ACG-mainumber').string + ' ' + game.find(class_='ACG-maintitle').find('a').string)





import sys

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import requests

r = requests.get('http://tw.yahoo.com')

print(r.text)



print('------------------------------------------------------------')	#60個


import requests

import pprint

r = requests.get('http://tw.yahoo.com')

pprint.pprint(r.text)


print('------------------------------------------------------------')	#60個


import requests

import pprint

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

weather_data = requests.get(api_url).json()

pprint.pprint(weather_data)

print('------------------------------------------------------------')	#60個


url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

paload = {'city':'130010'}

weather_data = requests.get(url, params = paload).json()


print('------------------------------------------------------------')	#60個


pprint.pprint(weather_data['forecasts'][0]) 


print('------------------------------------------------------------')	#60個

import requests, pprint

api_url = 'https://zh.wikipedia.org/w/api.php'

api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}

wiki_data = requests.get(api_url, params = api_params)

pprint.pprint(wiki_data)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import sys

print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get('http://tw.yahoo.com')

soup = BeautifulSoup(html_data.text, "html.parser")

print(soup.title)

print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

yahoo_news_xml = requests.get('https://tw.news.yahoo.com/rss/technology')

soup = BeautifulSoup(yahoo_news_xml.text, "html.parser")

type(soup)

soup.findAll('item')

print('------------------------------------------------------------')	#60個

for news in soup.findAll('item'):

	print(news.title)
	
print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

game_raking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=Android')

game_raking_html.encoding = 'UTF-8'

soup = BeautifulSoup(game_raking_html.text, "html.parser")

soup.find(class_='ACG-mainbox1').find(class_='ACG-maintitle').find('a').string

print('------------------------------------------------------------')	#60個

for game in soup.findAll(class_='ACG-mainbox1'):
	print(game.find(class_='ACG-mainumber').string + ' ' + game.find(class_='ACG-maintitle').find('a').string)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import requests #滙入requests套件

addr = 'https://www.edu.tw/'    #教育部
addr = 'https://www.books.com.tw/'

res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    print('status_code= ',res.status_code)
    res.encoding='utf-8'
    print(res.text)
else:
    print('網頁無法開啟, status_code= ',res.status_code)


import base64
from io import BytesIO
from PIL import Image

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg'
resp = requests.get(url)
img3 = Image.open(BytesIO(resp.content))
img3.save('tmp_Uranus2.jpg')

print(base64.b64encode(resp.content))






print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個









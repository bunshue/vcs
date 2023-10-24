import os
import sys
import time
import random



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


import calendar

print(calendar.month(2023, 10))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


word = 'maintenance'
word.count('n')

len('thunderbolt')


animal = ['cat','dog','duck']
len(animal)


max(100,10,50)
min(300,30,3000)




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



import zipfile

files = zipfile.ZipFile('C:/workplace/test.zip')

files.namelist()

files.extract('d/c.txt')

files.extractall()

files.close()



print('------------------------------------------------------------')	#60個

#pip install qrcode

import qrcode

encode_text = 'https://google.com'

img = qrcode.make(encode_text)

type(img)

img.show()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import requests
r = requests.get('https://tw.yahoo.com/')
print(r.text)


print('------------------------------------------------------------')	#60個

import pprint
r = requests.get('https://tw.yahoo.com/')
pprint.pprint(r.text)


print('------------------------------------------------------------')	#60個

import requests

base_url = 'https://zipcloud.ibsnet.co.jp/api/search'

query_parameter = '?zipcode='

zipcode = '1600021'

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()



#有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來


print('------------------------------------------------------------')	#60個

import requests, pprint

api_url = 'https://zh.wikipedia.org/w/api.php'

api_params = {'format':'json', 'action':'query', 'titles':柔道', 'prop':'revisions', 'rvprop':'content'}

wiki_data = requests.get(api_url, params=api_params).json()

pprint.pprint(wiki_data)



#pip install wikipedia


import wikipedia
wikipedia.set_lang ('zh')
wikipedia.summary('柔道')



#python wiki_sample.py




#python try_sys.py 想查詢的關鍵字




#python wiki_sample_final.py 柔道





print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup
soup = BeautifulSoup('<html> Lollipop </html>', 'html.parser')

print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get('http://tw.yahoo.com')

soup = BeautifulSoup(html_data.text,"html.parser")

soup.title


print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

game_ranking_html = requests.get('https://www.kamatari.org/blog/2021/best-games-of-2021/')

soup = BeautifulSoup(game_ranking_html.text, "html.parser")

for game in soup.findAll('h2'):
	print(game.text)


print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
game_ranking_html = requests.get ('https://www.kamatari.org/blog/2021/best-games-of-2021/')
soup = BeautifulSoup (game_ranking_html.text, "html.parser" )
for game in soup.findAll ('h2'):
	print (game.text)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import requests
from bs4 import BeautifulSoup

url = 'https://udn.com/news/breaknews/1'

html = requests.get(url).text
sel = '#breaknews > div.context-box__content.story-list__holder.story-list__holder--full > div> div.story-list__text'
soup = BeautifulSoup(html, 'html.parser')
target = soup.select(sel)
for news in target:
    print(news.h3.a['title'])


#----------------------------------------------------------------------------------


import requests
from bs4 import BeautifulSoup

url = 'https://newcar.u-car.com.tw/newcar'

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
makes = soup.select('#makeselect > option')
makers = dict()
for make in makes:
    if make['value'] != '0':
        makers[int(make['value'])] = make.text
print(makers)





#----------------------------------------------------------------------------------


import requests
from bs4 import BeautifulSoup

url = 'https://newcar.u-car.com.tw/newcar'

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
models = soup.select('#modelselect > option')
cars = list()
for model in models:
    if model['value'] != '0':
        car = dict()
        car['id'] = int(model['value'])
        car['make'] = int(model['data-make'])
        car['name'] = model.text
        cars.append(car)
print(cars)


#----------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

url = 'https://newcar.u-car.com.tw/newcar'

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
makes = soup.select('#makeselect > option')
makers = dict()
for make in makes:
    if make['value'] != '0':
        makers[int(make['value'])] = make.text
        
models = soup.select('#modelselect > option')
cars = list()
for model in models:
    if model['value'] != '0':
        car = dict()
        car['id'] = int(model['value'])
        car['make'] = int(model['data-make'])
        car['make-name'] = makers[car['make']]
        car['name'] = model.text
        cars.append(car)
print(cars)



#----------------------------------------------------------------------------------


import requests
from bs4 import BeautifulSoup

url = 'https://tw.appledaily.com/new/realtime/2'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
data = soup.select(sel)
for item in data:
    print(item.time.text)
    print(item.h1.text)
    print(item['href'])



#----------------------------------------------------------------------------------

import requests, time
from bs4 import BeautifulSoup

target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    url = target.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
    data = soup.select(sel)
    for item in data:
        title = dict()
        title['time'] = item.time.text
        title['title'] = item.h1.text
        title['link'] = item['href']
        titles.append(title)
    time.sleep(3)
print(titles)




#----------------------------------------------------------------------------------

import requests, time, json
from bs4 import BeautifulSoup
from datetime import datetime

target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    url = target.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
    data = soup.select(sel)
    for item in data:
        title = dict()
        title['time'] = item.time.text
        title['title'] = item.h1.text
        title['link'] = item['href']
        titles.append(title)
    time.sleep(3)
for title in titles:
    try:
        url = title['link']
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        sel = '#article-header > header > div > h2 > span'
        target = soup.select(sel)
        print(target[0].text)
        title['title'] = target[0].text
    except:
        pass
    time.sleep(3)
    
now = datetime.now()
filename = now.strftime("news-%y-%m-%d-%H-%M-%S.json")
with open(filename, "w", encoding='utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)



#----------------------------------------------------------------------------------





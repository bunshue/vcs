from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.google.com.tw/'

html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
all_links = sp.find_all('a')

for link in all_links:
    href = link.get('href')
    if href != None and href.startswith('http://'):
        print(href)



'''
import requests

url = 'https://httpbin.org/get'
headers = {'Content-Type': 'text/html'}

html_data = requests.get(url, headers=headers)

print(html_data.text)
'''

import ssl
import requests
from urllib.request import urlopen
import urllib.request   #用來建立請求
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
url = 'https://movies.yahoo.com.tw/chart.html'
html_data = urllib.request.urlopen(url).read()
html_data = html_data.decode('utf-8')
print(html_data)
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())
























import requests
from bs4 import BeautifulSoup
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
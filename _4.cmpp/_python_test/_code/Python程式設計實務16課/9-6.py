# _*_ coding: utf-8 _*_
# 程式 9-6 (Python 3 version)

from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urlparse

if len(sys.argv) < 2:
    print("用法：python 9-6.py <<target url>>")
    exit(1)  

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
all_links = sp.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                print(t)
            else:
                print(domain+t)

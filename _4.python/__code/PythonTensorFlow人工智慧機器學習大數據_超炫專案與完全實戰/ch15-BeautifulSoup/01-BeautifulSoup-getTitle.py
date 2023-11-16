# -*- coding: UTF-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import requests
from bs4 import BeautifulSoup

req=requests.get('http://www.powenko.com/wordpress/')
print(req.text.encode('utf-8'))
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))


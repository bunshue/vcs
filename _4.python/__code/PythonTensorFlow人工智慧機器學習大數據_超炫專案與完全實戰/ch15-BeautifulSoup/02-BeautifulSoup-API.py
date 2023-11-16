#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
import requests
from bs4 import BeautifulSoup

text1="""
<head>
    <title>柯博文老師</title>
</head>
<body>
    <p class="title"><b>The test</b></p>
    <a class="redcolor" href="http://powenko.com/1.html" id="link1">test1</a>
    <a class="bluecolor" href="http://powenko.com/2.html" id="link2">test2</a>
    <a class="redcolor" id="link3" href="http://powenko.com/3.html" id="link3">test3</a>
</body>
"""
soup=BeautifulSoup(text1, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
for link in soup.find_all('a'):
	print(link.get('href'))
print(soup.select('a'))
print(soup.select('.redcolor'))   # class="redcolor"
print(soup.select('#link3'))     # id="link3"
for link in soup.select('a'):
	print(link.string)


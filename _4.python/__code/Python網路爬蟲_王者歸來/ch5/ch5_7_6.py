# ch5_7_6.py
import bs4
import re

htmlFile = "<h1 class='bold italic'>深智數位</h1>"
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
tag = objSoup.find('h1', class_='bold')
print(tag)
print(tag.text)
print('-'*70)
tag = objSoup.find('h1', class_='italic')
print(tag)
print(tag.text)














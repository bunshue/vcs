# ch23_13.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print(f"列印title = {objSoup.title}")
print(f"title內容 = {objSoup.title.text}")














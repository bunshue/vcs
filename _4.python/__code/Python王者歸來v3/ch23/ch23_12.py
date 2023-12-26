# ch23_12.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print(f"物件類型  = {type(objSoup.title)}")
print(f"列印title = {objSoup.title}")












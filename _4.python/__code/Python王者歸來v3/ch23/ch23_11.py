# ch23_11.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print(f"列印BeautifulSoup物件資料型態 {type(objSoup)}")












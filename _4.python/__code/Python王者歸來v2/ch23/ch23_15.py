# ch23_15.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print("列印title = ", objSoup.title)
print("title內容 = ", objSoup.title.text)














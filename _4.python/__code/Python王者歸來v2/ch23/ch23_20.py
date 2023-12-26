# ch23_20.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.select('#author')
print("列出串列元素的資料型態    = ", type(objTag[0]))
print(objTag[0])
print("列出str()轉換過的資料型態 = ", type(str(objTag[0])))
print(str(objTag[0]))


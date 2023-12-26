# ch23_19.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.select('#author')
print("資料型態     = ", type(objTag))          # 列印資料型態
print("串列長度     = ", len(objTag))           # 列印串列長度
print("元素資料型態 = ", type(objTag[0]))       # 列印元素資料型態
print("元素內容     = ", objTag[0].getText())   # 列印元素內容










# ch23_14.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find('h1')
print(f"資料型態       = {type(objTag)}")
print(f"列印Tag        = {objTag}")
print(f"Text屬性內容   = {objTag.text}")
print(f"String屬性內容 = {objTag.string}")













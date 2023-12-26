# ch23_17.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all('h1')
print("資料型態    = ", type(objTag))     # 列印資料型態
print("列印Tag串列 = ", objTag)           # 列印串列
print("以下是列印串列元素 : ")
for data in objTag:                       # 列印串列元素內容
    print(data.text)

    














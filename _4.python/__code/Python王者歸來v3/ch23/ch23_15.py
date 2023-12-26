# ch23_15.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all('h1')
print(f"資料型態    = {type(objTag)}")      # 列印資料型態
print(f"列印Tag串列 = {objTag}")            # 列印串列
print(f"以下是列印串列元素 : ")
for data in objTag:                         # 列印串列元素內容
    print(data.text)

    














# ch23_25.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
imgTag = objSoup.select('img')
print(f"含<img>標籤的串列長度 = {len(imgTag)}")
for img in imgTag:              
    print(f"列印標籤串列 = {img}")
    print(f"列印圖檔     = {img.get('src')}")
    print(f"列印圖檔     = {img['src']}")



    




    

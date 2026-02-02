# ch5_11.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
pObjTag = objSoup.select('p')
print("含<p>標籤的串列長度 = ", len(pObjTag))
for pObj in pObjTag:
    print(str(pObj))              # 內部有子標籤<strong>字串
    print(pObj.getText())         # 沒有子標籤
    print(pObj.text)              # 沒有子標籤




    

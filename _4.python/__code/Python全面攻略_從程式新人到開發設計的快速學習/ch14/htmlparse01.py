#htmlparse01

import requests

urlstr="http://www.drmaster.com.tw/Publish_Newbook.asp"
response=requests.get(urlstr)

print("網址：%s" %(response.url))
print("狀態：%s" %(response.status_code))
print("表頭：%s" %(response.headers))

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\htmlparse02.py

import requests
urlstr="http://www.drmaster.com.tw/Publish_Newbook.asp"
response=requests.get(urlstr)
response.encoding="utf-8"
print("網頁程式碼：%s" %(response.text))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\htmlparse03.py

import requests
# 指定圖片網址
imgUrl='http://www.drmaster.com.tw/Cover/MP22030.png'
imgName=imgUrl.split('/')[-1]
response= requests.get(imgUrl) 
f=open(imgName,'wb')  	# 指定開啟檔案路徑
# 將response.content二進位內容寫入為MP22030.png
f.write(response.content)  			
print('%s 下載完畢' %(imgName))
f.close()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\htmlparse04.py

import requests
from bs4 import BeautifulSoup
# 博碩文化新書網頁
urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'  
response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text, 'html.parser')
print(bs.title.text)    # 顯示網頁title標題
listBookName=bs.select('.style2')
count=len(listBookName)
print("共 %d 筆新書記錄" %(count))  # 顯示 '共 20 筆新書記錄'

# 顯示網頁新書書名
for book in listBookName:
    print(book.text)
    
    
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\htmlparse05.py

import requests
from bs4 import BeautifulSoup

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'

response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text,'html.parser')

listImageUrl=bs.select('td a img')

for link in listImageUrl:
    #if("http" in link.get('src')):
        print(link.get('src'))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\htmlparse06.py

import os, shutil
import requests
from bs4 import BeautifulSoup

# 若程式的路徑有images資料即刪除，否則即建立images
folder="images"
if os.path.exists(folder):
    shutil.rmtree(folder)
os.mkdir(folder)

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'
response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text, 'html.parser')
listImageUrl=bs.select('td a img')
# 逐一取得博碩新書圖檔並放入images資料夾下
n=0
for link in listImageUrl:
    imgUrl=link.get('src')
    if("http" in imgUrl):   
        imgName=imgUrl.split('/')[-1]
        response= requests.get(imgUrl) 
        f=open(folder +'/' + imgName,'wb')  	# 指定開啟檔案路徑
        # 將response.content二進位內容寫入指定的圖檔名稱
        f.write(response.content) 
        f.close()
        print("%s 下載完成" %(imgName))
        n+=1
print('共下載 %d 張圖檔' %(n))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\htmlparse07.py

import os, shutil
import requests
from bs4 import BeautifulSoup

# 若程式的路徑有images資料即刪除，否則即建立images
folder="images"
if os.path.exists(folder):
    shutil.rmtree(folder)
os.mkdir(folder)
pageName='newbook.html'
if os.path.exists(pageName):
    os.remove(pageName)

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'
response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text, 'html.parser')
listImageUrl=bs.select('td a img')
listImageUrlOk=[]
listBookName=bs.select('.style2')
# 逐一取得博碩新書圖檔並放入images資料夾下
for link in listImageUrl:
    imgUrl=link.get('src')
    if("http" in imgUrl):   
        imgName=imgUrl.split('/')[-1]
        listImageUrlOk.append(imgName)
        response= requests.get(imgUrl) 
        f=open(folder +'/' + imgName,'wb')  	# 指定開啟檔案路徑
        # 將response.content二進位內容寫入指定的圖檔名稱
        f.write(response.content) 
        f.close()
        print("%s 下載完成" %(imgName))

f=open(pageName,'w',encoding='utf-8')
f.write('<html>\n')
f.write('<meta charset="utf-8">\n')
f.write('<body>\n')
f.write('<table border>\n')
f.write('<tr><td>書號</td><td>圖</td><td>書名</td></tr>\n')
for n in range(len(listBookName)):
    f.write('<tr>\n')
    f.write('<td>%s</td>\n' %(listImageUrlOk[n].split('.')[0]))
    f.write('<td><img src="images/%s" width="100"></td>\n' %(listImageUrlOk[n]))
    f.write('<td>%s</td>\n' %(listBookName[n].text))
    f.write('</tr>\n')
f.write('</table>\n')
f.write('</body>\n')
f.write('</html>\n')
f.close()
os.system(pageName)
print('%s 網頁建置成功' %(pageName))





print("------------------------------------------------------------")  # 60個


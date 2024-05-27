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

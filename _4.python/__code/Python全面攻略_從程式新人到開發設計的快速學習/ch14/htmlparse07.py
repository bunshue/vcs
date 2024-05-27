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





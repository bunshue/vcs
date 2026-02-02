# ch15_3.py
import requests, bs4, os

url = 'http://www.xzw.com/fortune/'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
constellation = objSoup.find('div', id='list')
cons = constellation.find('div', 'alb').find_all('div')

pict_url = 'http://www.xzw.com'
photos = []
for con in cons:
    pict = con.a.img['src']
    photos.append(pict_url+pict)

destDir = 'out15_3'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir)
print("搜尋到的圖片數量 = ", len(photos))               # 列出搜尋到的圖片數量
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    picture.raise_for_status()                          # 驗證圖片是否下載成功
    print("%s 圖片下載成功" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()                                    # 關閉檔案    



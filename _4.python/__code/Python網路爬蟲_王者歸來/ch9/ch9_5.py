# ch9_5.py
import requests, bs4, os

url = 'https://movies.yahoo.com.tw/movie_thisweek.html' # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')     # 取得新片網址的HTML

photos = []                                             # 放置劇照串列
items = objSoup.find_all('div', 'release_foto')
for item in items:
    photo = item.a.img['src']                           # 取得劇照網址
    photos.append(photo)

destDir = 'out9_5'
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
    



                                                                        
                                                            




    
    

    






















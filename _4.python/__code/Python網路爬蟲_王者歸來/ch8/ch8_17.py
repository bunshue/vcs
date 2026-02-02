# ch8_17.py
import requests, bs4, os

url_ppt = 'https://www.ptt.cc'
beauty = '/bbs/beauty/index.html'

ptthtml = requests.get(url_ppt+beauty, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

pttdivs = objSoup.find_all('div', 'r-ent')
href = pttdivs[0].find('a')['href']                                 # 文章超連結

print('目前連線網址 : ', url_ppt+href)
beauty_html = requests.get(url_ppt+href, cookies={'over18':'1'})    # 進入超連結
beauty_soup = bs4.BeautifulSoup(beauty_html.text, 'lxml')   

beauty_divs = beauty_soup.find('div', id='main-content')
photos = []                                                         # 圖片網址
url_photos = beauty_divs.find_all('a')                              # 找尋所有圖片
for photo in url_photos:
    href_photo = photo['href']
    if href_photo.startswith('https://i.imgur'):                    # 判斷圖片網址
        photos.append(href_photo)

for photo in photos:                                                # 列印圖片網址
    print(photo)

destDir = 'out8_17'
if os.path.exists(destDir) == False:                    # 如果沒有此資料夾就建立
    os.mkdir(destDir)  
print("搜尋到的圖片數量 = ", len(photos))               # 列出搜尋到的圖片數量
for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    print("%s 圖片下載成功" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()                                    # 關閉檔案  













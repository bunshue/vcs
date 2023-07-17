import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 第3屆埔里跑 Puli Power 山城派對馬拉松  向善橋(約34K)
url = 'http://tw.running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle=第3屆埔里跑 Puli Power 山城派對馬拉松-向善橋(約34K)'
html = requests.get(url)

soup=BeautifulSoup(html.text,'html.parser')  
title = soup.find('h1',{'class':'album-title flex-1'}).text.strip() + "_全部相片"

url = 'https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer'

# 在回應頁面中找出所有照片連結
soup = BeautifulSoup(html.text, 'html.parser')

# 以標題建立目錄儲存圖片
images_dir=title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

n=0
for i in range(200):
    payload = {'type': 'album', 'rows': str(i*20), 'need_rows': '20',
               'cid': '5791','album_id': '30668'}
    html = requests.post(url, data=payload)
    soup = BeautifulSoup(html.text, 'html.parser')
    # 處理所有 <img> 標籤 
    photos = soup.select('.photo_img')
    for photo in photos:
        # 讀取 src 屬性內容
        src=photo['src']
        # 讀取 .jpg 檔
        if src != None and ('.jpg' in src):
            # 設定圖檔完整路徑
            full_path = src            
            filename = full_path.split('/')[-1]  # 取得圖檔名
            print(full_path)
            # 儲存圖片
            try:
                image = urlopen(full_path)
                with open(os.path.join(images_dir,filename),'wb') as f:
                    f.write(image.read())  
                n+=1
                if n>=1000: # 最多下載 1000 張
                    break   # 離開內部 for 迴圈
            except:
                print("{} 無法讀取!".format(filename))  
    if n>=1000: # 最多下載 1000 張
        break   # 離開外部 for 迴圈      
                
print("共下載",n,"張圖片") 
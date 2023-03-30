import time,os
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 隱藏瀏覽器
chrome_options = Options()
chrome_options.add_argument("--headless")  # 定義 headless
driver = webdriver.Chrome(chrome_options=chrome_options)

# 第3屆埔里跑 Puli Power 山城派對馬拉松  向善橋(約34K)
#url = 'http://tw.running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle=第3屆埔里跑 Puli Power 山城派對馬拉松-向善橋(約34K)'
# 第3屆埔里跑 Puli Power 山城派對馬拉松  在终點前80米
url = 'http://tw.running.biji.co/index.php?q=album&act=photo_list&album_id=30807&cid=5791&type=album&subtitle=第3屆埔里跑 Puli Power 山城派對馬拉松-在终點前80米'

driver.get(url)  #開啟瀏覽器
#隱性等待 1 秒
driver.implicitly_wait(1)

for i in range(1,101):
    # 向下捲動，會花費一些時間
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.3)
   
soup=BeautifulSoup(driver.page_source,'html.parser')  
title = soup.select('.album-title')[0].text.strip()   # 標題
all_imgs = soup.find_all('img', {"class": "photo_img photo-img"})

# 以標題建立目錄儲存圖片
images_dir=title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)
    
# 處理所有 <img> 標籤
n=0
for img in all_imgs:
    # 讀取 src 屬性內容
    src=img.get('src')
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
                break
        except:
            print("{} 無法讀取!".format(filename))
            
print("共下載",n,"張圖片")                
driver.quit(); #關閉瀏覽器並退出驅動程式
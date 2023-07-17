import requests,os,json
from bs4 import BeautifulSoup

url = 'https://store.line.me/stickershop/product/8991459/zh-Hant'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')

# 建立目錄儲存圖片
images_dir= "line_image/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# 下載貼圖
datas = soup.find_all('li', {'class':'mdCMN09Li FnStickerPreviewItem'})
for data in datas:
    # 將字串資料轉換為字典
    imginfo = json.loads(data.get('data-preview'))
    id=imginfo['id']
    imgfile = requests.get(imginfo['staticUrl']) #載入圖片
   
    full_path = os.path.join(images_dir,id) #儲存的路徑和主檔名
    # 儲存圖片           
    with open(full_path + '.png', 'wb') as f:
        f.write(imgfile.content)
    print(full_path + '.png') #顯示儲存的路徑和檔名
#    break  # 測試用
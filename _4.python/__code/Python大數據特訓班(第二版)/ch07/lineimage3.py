import requests, json, os
from bs4 import BeautifulSoup

url = 'https://store.line.me/stickershop/product/8991459/zh-Hant'

html = requests.get(url)


sp = BeautifulSoup(html.text, 'html.parser')
datas = sp.find_all('li', {'class':'mdCMN09Li FnStickerPreviewItem'})

# 建立目錄儲存圖片
images_dir= "line_image/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

for data in datas:
    imginfo = json.loads(data.get('data-preview'))
    id = imginfo['id']
    imgfile = requests.get(imginfo['staticUrl'])
    full_path = images_dir + id + '.png'
    
    with open(full_path, 'wb') as f:
        f.write(imgfile.content)
        print(full_path)


        

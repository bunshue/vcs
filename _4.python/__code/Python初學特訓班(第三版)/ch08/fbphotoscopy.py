import facebook,os,shutil,requests

token="EAADAqsBw2wsBAFyN2P7idDOBJZCXCH3FFbMkYWZASiTKsBqqbZCL6WCMtr91wrSW30u7bmw92yocRwB2cPZBKA8XnrQzpDeuveclitVB7BkPaXOhyaN03Ig5xmHHdX3KZB7ZCLnYy8bBDF2oSDGkBItKHVA9XZBUkP2wyBpdN0oyqgsIZBOfRPmP9qyWZBZCCN4HQZD"
graph = facebook.GraphAPI(access_token=token,version='3.0')

pages = graph.get_connections(id='me', connection_name='photos?fields=images')
photos = pages['data']
#print(photos)

if not os.path.exists("fb-photos"):  # 建立 fb-photos 目錄
    os.mkdir("fb-photos")

for p in photos:
    imagelst = p['images']
#    print(imagelst)
    for img in imagelst:
       filename = img['source'].split('/')[-1].split('?')[0]
       print(filename)
       f = open('fb-photos/'+filename, 'wb') #儲存照片的路徑、檔名
       pic = requests.get(img['source'], stream=True) #開啟照片
       shutil.copyfileobj(pic.raw, f) # 複製照片
       f.close()
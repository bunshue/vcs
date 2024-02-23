import requests, json, os, shutil, sys  # 引用相關套件
# 將農村地方美食小吃特色料理的JSON資料集網址指定給url變數
url='https://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvTravelFood.aspx'
# 建立取得網頁資訊的Response物件，物件名稱為rp
rp=requests.get(url)
# 設定編碼模式避免亂碼
rp.encoding="utf_8_sig"
# 使用json套件的loads()方法將擷取到的資料集轉成all_list串列
all_list=json.loads(rp.text)

folder = 'images'
pagename = 'countryfood.html'
if os.path.exists(pagename):  
    os.remove(pagename)     # 若有countryfood.html網頁即刪除
if os.path.exists(folder): 
    shutil.rmtree(folder)    # 若有images目錄即刪除
else:
    os.mkdir(folder)        # 若無images目錄即刪除

#下載圖片
for col in all_list:  
    imgUrl=col['PicURL']
    imgName=imgUrl.split('/')[-1] #擷取圖片名稱
    print('圖片網址：',imgUrl)
    print('='*70)#分隔線
    try:
        #建立取得圖片的Rpimg物件
        Rpimg=requests.get(imgUrl) 
        f=open((folder+'/'+imgName),'wb')    #開啟圖片檔案                    
        f.write(Rpimg.content)     #下載圖片
        print(imgName,'下載完畢')
        print('='*70)#分隔線
        f.close() 
    except:
        print('下載失敗')
        print('='*70)#分隔線
        sys.exit(1)

     
fw=open(pagename,'w',encoding='UTF-8')  
fw.write('<!DOCTYPE html>\n')
fw.write('<html>\n')
fw.write('<head><meta charset="utf-8" />\n')
fw.write('<title>農村地方美食小吃特色料理</title>\n')
fw.write('</head>\n')
fw.write('<body>\n')

#網頁CSS樣式設定
style='''
<style> 
img { 
   border-radius: 4px 4px 0 0; height:180px; 
   width:100%; 
} 
.card { 
   box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); 
   width: 280px ; 
   border-radius: 5px; 
   border:1px #FFF2C1 solid; float: left; 
   margin:13px; 
} 
.card:hover { 
   box-shadow: 0 8px 16px 0 #FCC592; 
} 
.txt { 
   padding: 2px 16px; 
   height:110px;
   background-color:#FEE3AD; 
} 
</style>       
'''
fw.write('\n'+style+'\n')
#HTML標籤與開放資料整合成網頁內容
for row in all_list:
    picName=row['PicURL'].split('/')[-1]
    fw.write('<div class="card">\n') #設定外層div以及屬性
    # 設置圖片的相對路徑，路徑為 'images/檔名'
    fw.write('  <img src="'+ folder +'/'+ picName + '">\n') 
    fw.write('  <div class="txt">\n') #設定文字div以及屬性
    fw.write('     <h4><b>'+row['Name']+'</b></h4>\n') #寫入店家名稱
    fw.write('     <p>'+row['Address']+'</p>\n') #寫入店家地址
    fw.write('  </div>\n') 
    fw.write('</div>\n')
fw.write('</body>\n') 
fw.write('</html>\n') 
fw.close()
os.system(pagename)  # 開啟網頁
print("%s網頁建置完成" %(pagename))




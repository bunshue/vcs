import requests,json,os  # 引用相關套件
import matplotlib.pyplot as plt  # 圖表使用套件
# 指定url變數為全國休閒農業區旅遊資訊所提供的json檔資料網址
url='https://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvAttractions.aspx'
# 建立取得網頁資訊的Response物件，物件名稱為rp
rp=requests.get(url)
#設定編碼模式避免亂碼
rp.encoding="utf_8_sig"
# 使用json套件的loads()方法將JSON資料集轉成串列
all_list=json.loads(rp.text)
#資料整理
listAllCity=[]    #存放每筆記錄的縣市名稱，此處串列存放重複的縣市名稱
for col in all_list:
    listAllCity+=[col['City']]

listCity=[]   #存放所有縣市名稱，此串列存放不重複的縣市名稱
listCount=[]  #存放各縣市對應的農業區數量
for city in set(listAllCity):   # 使用set()移除listAllCity串列中重複的縣市
    print(city,'地區有',listAllCity.count(city),'個農業區')
    listCity+=[city]
    listCount+=[listAllCity.count(city)]   
# 繪製柱狀圖
font= {'family':'DFKai-SB'}  # 設定柱狀圖可以顯示中文
plt.rc('font',**font)   
plt.barh(listCity,listCount  ,label='農業區')# 橫向柱狀圖串列數據設定
plt.title('各縣市農場數量') #柱狀圖名稱
plt.xlim(0,60)  #X軸範圍0~60
plt.xlabel('數量') #X軸名稱
plt.ylabel('縣市') #Y軸名稱
for y,x in enumerate(listCount):    #使用迴圈讓柱狀末端顯示各縣市農業區總數
     plt.text(x,y,'%s'%x,ha='center')
plt.legend()    #圖例(柱狀圖)說明
plt.grid(True)  #顯示格線
plt.savefig('Histogram.png') #將柱狀圖存出成圖片 
plt.show()                   #顯示繪圖結果
os.system('Histogram.png')  #開啟柱狀圖Histogram.png圖片
print("圖表製作完成")
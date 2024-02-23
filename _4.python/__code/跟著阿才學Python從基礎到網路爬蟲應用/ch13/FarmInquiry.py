# 引用相關套件
import requests,json
# 指定url變數為全國休閒農業區旅遊資訊所提供的json檔資料網址
url='https://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvAttractions.aspx'
# 建立取得網頁資訊的Response物件，物件名稱為rp
rp=requests.get(url)
#設定編碼模式避免亂碼
rp.encoding="utf_8_sig"
#使用json套件的loads()方法將擷取到的資料集轉成串列
all_list=json.loads(rp.text)
#建立Inquire變數來存放欲查詢資料中的縣市名稱
Inquire=str(input('輸入縣市查詢當地的農場：'))

#當輸入的字元有 '台' 字時，將該字轉換成 '臺' 字
Inquire=Inquire.replace('台','臺')  
print('='*60) #分隔線

list_result=[]   # 建立list_result串列用來存放符合的農業休閒區項目
for col in all_list:
    if Inquire in col['City']: # 判斷查詢的縣市使否存在
        print('名稱：',col['Name'],'電話：',col['Tel'],'\n地址：',col['Address'])
        print('='*60) #分隔線
        list_result+=[col['City']] # 將符合的農業休閒區項目放入list_result串列

# 使用len()函式取得list_result串列的數量並放入變數count
count = len(list_result)
# 判斷農業休閒區數量是否不等於0
if count != 0:
    print(list_result[0],'總計',count,'處旅遊區')
else:
    #其餘狀況則顯示錯誤或無農業休閒區
    print('輸出錯誤或是此地沒有旅遊區')





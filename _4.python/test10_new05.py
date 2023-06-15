import time

print(time.localtime()) #獲取格式化的時間

localtime = time.asctime(time.localtime())
print (localtime)

#格式化日期成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

'''
print('----------------------------------------------------------------------')	#70個
import requests
# 資料
my_data = {'key1': 'value1', 'key2': 'value2'}
# 將資料加入POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)
print(r.text)
print(r.status_code)

print('----------------------------------------------------------------------')	#70個

# 要上傳的檔案
my_files = {'my_filename': open('bankRate.csv', 'rb')}
# 將檔案加入POST 請求中
r = requests.post('http://httpbin.org/post', files = my_files)
print(r.status_code)

'''

print('----------------------------------------------------------------------')	#70個

import requests
from bs4 import BeautifulSoup

#臺灣證交所本國上市證券
#查詢台灣證交所本國上市證券國際證券辨識號碼一覽表

import pandas as pd #匯入pandas套件

df=pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',encoding='big5hkscs', header = 0)
newdf=df[0][df[0]['產業別'] > '0'] #產業別資料大於0
#del newdf['國際證券辨識號碼(ISIN Code)'],newdf['CFICode'],newdf['備註']
del newdf['CFICode'],newdf['備註'] #刪除兩個不需要欄位
df2 = newdf['有價證券代號及名稱'].str.split(' ', expand=True) #分成兩個欄位回存
df2 = df2.reset_index(drop=True) #重設索引值
newdf = newdf.reset_index(drop=True) #重設索引值
for i in df2.index:
    if ' ' in df2.iat[i,0]: #將有價證券代號及名稱
        df2.iat[i,1]=df2.iat[i,0].split(' ')[1] #欄位資料內容分割為2，回存df2物件中。
        df2.iat[i,0]=df2.iat[i,0].split(' ')[0] #回存df2物件中。
newdf=df2.join(newdf) #將df2合併到newdf物件
newdf=newdf.rename(columns = {0:'股票代號',1:'股票名稱'}) #修改欄位名稱
del newdf['有價證券代號及名稱'] #將"有價證券代號及名稱"欄位刪除
newdf.to_excel('stock_.xlsx', sheet_name='Sheet1',index=False) #存入excel

print('----------------------------------------------------------------------')	#70個





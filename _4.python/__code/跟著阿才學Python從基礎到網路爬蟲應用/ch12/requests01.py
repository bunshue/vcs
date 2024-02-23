import requests
url='https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003' #博客來網址
response=requests.get(url)
#印出<class 'requests.models.Response'>，表示response為Response物件
print('物件型別：',type(response)) 
print('網址：',response.url)
print('表頭資訊：',response.headers)
print('連線狀態：',response.status_code)
print('網頁編碼模式：',response.encoding)


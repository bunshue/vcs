# ch23_2.py
import requests
import csv

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'http://www.lovewzly.com/api/user/pc/list/search?'
# 傳遞參數
form_data = {'gender':'2', 'mary':'1', 'page':'1'}
datahtml = requests.get(url, params=form_data, headers=headers)
datas = datahtml.json()
print(datas['data']['list'][0])
print('-'*70)
print('暱稱     : ', datas['data']['list'][0]['username'])
print('Userid   : ', datas['data']['list'][0]['userid'])
print('婚姻狀態 : ', datas['data']['list'][0]['marry'])
print('性別     : ', '女' if datas['data']['list'][0]['gender'] == '2' else '男')
print('居住省份 : ', datas['data']['list'][0]['province'])
print('居住城市 : ', datas['data']['list'][0]['city'])
print('出生年   : ', datas['data']['list'][0]['birthdayyear'])
print('身高     : ', datas['data']['list'][0]['height'])
print('薪資     : ', datas['data']['list'][0]['salary'])        
print('照片連結 : ', datas['data']['list'][0]['avatar'])        
print('自我介紹 : ', datas['data']['list'][0]['monolog'])         
   






# ch23_1.py
import requests
from pprint import pprint

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'http://www.lovewzly.com/api/user/pc/list/search?'
# 傳遞參數
form_data = {'gender':'2', 'mary':'1', 'page':'1'}
datahtml = requests.get(url, params=form_data, headers=headers)

data = datahtml.json()
print('資料型態 : ', type(data))    # 列出資料型態
print('資料長度 : ', len(data))     # 列出資料長度
pprint(data)                        # 列出第一頁資料





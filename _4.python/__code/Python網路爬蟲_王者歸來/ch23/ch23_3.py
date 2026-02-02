# ch23_3.py
import requests
import csv

fn = 'out23_3.csv'
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'http://www.lovewzly.com/api/user/pc/list/search?'
# 傳遞參數
form_data = {'gender':'2', 'mary':'1', 'page':'1'}
datahtml = requests.get(url, params=form_data, headers=headers)
datas = datahtml.json()

fields = ['暱稱', '出生年', '學歷', '身高', '居住城市', '照片連結']
data = datas['data']['list']
with open(fn, 'w', newline='', encoding='utf-8') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(fields)
    for d in data:
        d_list = [d['username'].encode('utf-8'),
                  d['birthdayyear'],
                  d['education'].encode('utf-8'),
                  d['height'],
                  d['city'].encode('utf-8'),
                  d['avatar']]
        csvWriter.writerow(d_list)
        print('暱稱   : ', d['username'])
        print('出生年 : ', d['birthdayyear'])
        print('身高   : ', d['height'])
        print('-'*70)
        
   






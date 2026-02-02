# ch23_4.py
import requests
import csv
import random
import time

def get_data(page):
    '''正式抓取資料'''
    form_data['page'] = page
    print('目前抓取第 %s 頁資料 ' % (page+1))
    datahtml = requests.get(url, params=form_data, headers=headers)
    datas = datahtml.json()
    data = datas['data']['list']
    for d in data:
        d_list = [d['username'].encode('utf-8'),
                  d['birthdayyear'],
                  d['education'].encode('utf-8'),
                  d['height'],
                  d['city'].encode('utf-8'),
                  d['avatar']]
        csvWriter.writerow(d_list)
        print('暱稱   : ', d['username'])    
        
fn = 'out23_4.csv'
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'http://www.lovewzly.com/api/user/pc/list/search?'
# 傳遞參數
form_data = {'gender':'2', 'mary':'1', 'page':'1'}
    
fields = ['暱稱', '出生年', '學歷', '身高', '居住城市', '照片連結']
with open(fn, 'w', newline='', encoding='utf-8') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(fields)
    for p in range(10):
        get_data(p)
        print('-'*70)
        time.sleep(random.randint(3,10))        # 時間不規律爬取資料

        
        
   






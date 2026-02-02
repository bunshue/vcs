# ch6_11.py
import requests
import os
import json
import hashlib

def save_newaqi():
    '''儲存newaqi.json'''
    with open(fn, 'w') as f:
        json.dump(aqijsons.json(),f)            # 寫入json檔案至newaqi.json
def save_hashvalue():
    '''儲存哈希值至hashvalue.txt'''
    with open(fn_hash, 'w') as fileobj:
        fileobj.write(newhash)                  # 寫入哈希值至hashvalue.txt
def cal_hashvalue():
    ''' 計算hash value''' 
    data = hashlib.md5()
    data.update(aqijsons.text.encode('utf-8'))
    hashdata = data.hexdigest()
    return hashdata                             # 傳回哈希值

url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$\
skip=0&$top=1000&format=json'
try:
    aqijsons = requests.get(url)                # 將檔案下載至aqijsons
    print('下載成功')
except Exception as err:
    print('下載失敗')

fn = 'newaqi.json'
fn_hash = 'hashvalue.txt'                       # 檔案名稱
if os.path.exists(fn_hash):                     # 如果hashvalue.txt存在
    newhash = cal_hashvalue()                   # 計算新的哈希值hashvalue
    print('newhash = ',newhash)
# 開啟hashvalue.txt檔案
    with open(fn_hash, 'r') as fnObj:           # 讀取舊的哈希值
        oldhash =  fnObj.read()
        print('oldhash = ', oldhash)        
    if newhash == oldhash:                      # 比對新舊哈希值
        print('環保署空氣品質資料未更新')
    else:
        print('環保署空氣品質資料已經更新')
        save_newaqi()                           # 儲存newaqi.son
        save_hashvalue()                        # 儲存哈希值至hashvalue.txt
else:                                           # 如果hashvalue.txt不存在
    print('第一次啟動此程式')
    newhvalue = cal_hashvalue()
    print('哈希值 = ', newvalue)
    save_hashvalue()                            # 儲存哈希值至hashvalue.txt
    save_newaqi()                               # 儲存newaqi.son



    
    






    
















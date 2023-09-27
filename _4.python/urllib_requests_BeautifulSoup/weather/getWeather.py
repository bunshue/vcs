import sys
import requests

def get_cwa_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/cwa_key.txt'

    import os
    filename = os.path.abspath(filename)
    if not os.path.exists(filename): #檢查檔案是否存在
        print('CWA_KEY 檔案不存在, 離開, 檔案 : ' + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, 'r')
    cwa_key = fo.read()
    fo.close()

    length = len(cwa_key)
    if length != 40:
        print('CWA_KEY 錯誤, 離開')
        return ""
    return cwa_key

cwa_key = get_cwa_key()
length = len(cwa_key)
if length != 40:
    print('CWA_KEY 錯誤, 離開')
    sys.exit()

"""
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
params = {
    "Authorization": cwa_key,
    "locationName": "新竹市",
}
"""

doc_name = "F-C0032-001"

url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/%s?downloadType=WEB&format=JSON&Authorization=%s' % (doc_name, cwa_key)
datas = requests.get(url).json()

column = ['天氣狀況','最高溫','最低溫','舒適度','降雨機率(%)']
#county = input('請輸入查詢的縣市名：')
county = '新竹市'
for data in datas['cwaopendata']['dataset']['location']:
    if data['locationName'] == county.replace('台', '臺'):
        for i in range(len(data['weatherElement'])):
            print(column[i], end=':')
            print(data['weatherElement'][i]['time'][0]['parameter']['parameterName'])
        break
else:
    print('沒有相關資料！')


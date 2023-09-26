import requests

user_key = "你的氣象API授權碼" #你的氣象API授權碼
doc_name = "F-C0032-001"

url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/%s?downloadType=WEB&format=JSON&Authorization=%s' % (doc_name,user_key)
datas = requests.get(url).json()

column = ['天氣狀況','最高溫','最低溫','舒適度','降雨機率(%)']
county = input('請輸入查詢的縣市名：')
for data in datas['cwbopendata']['dataset']['location']:
    if data['locationName'] == county.replace('台', '臺'):
        for i in range(len(data['weatherElement'])):
            print(column[i], end=':')
            print(data['weatherElement'][i]['time'][0]['parameter']['parameterName'])
        break
else:
    print('沒有相關資料！')
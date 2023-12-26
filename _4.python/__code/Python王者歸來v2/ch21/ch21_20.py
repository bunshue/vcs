# ch21_20.py
import requests
import json

url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$\
skip=0&$top=1000&format=json'
try:
    aqijsons = requests.get(url)                # 將檔案下載至aqijsons
    print('下載成功')
except Exception as err:
    print('下載失敗')

print(aqijsons.text)                            # 列印所下載的json檔案         

fn = "aqi.json"                                 # 建立欲儲存的json檔案 
with open(fn, 'w') as f:
    json.dump(aqijsons.json(),f)                # 寫入json檔案至aqi.json





    
















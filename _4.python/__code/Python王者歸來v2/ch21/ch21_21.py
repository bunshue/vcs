# ch21_21.py
import json

fn = 'aqi.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

for getData in getDatas:
    county = getData['County']                      # 城市名稱
    sitename = getData['SiteName']                  # 站台名稱
    siteid = getData['SiteId']                      # 站台ID
    pm25 = getData['PM2.5']                         # PM2.5值    
    print('城市名稱 =%4s  站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
          (county, siteid, pm25, sitename))




        


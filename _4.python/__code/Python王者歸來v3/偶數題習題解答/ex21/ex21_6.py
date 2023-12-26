# ex21_6.py
import json

fn = 'aqi.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                         # 讀json檔案

for getData in getDatas:
    if getData['County'] == '臺北市':
        sitename = getData['SiteName']                  # 站台名稱
        siteid = getData['SiteId']                      # 站台ID
        pm25 = getData['PM2.5']                         # PM2.5值    
        print('站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
              (siteid, pm25, sitename))




        


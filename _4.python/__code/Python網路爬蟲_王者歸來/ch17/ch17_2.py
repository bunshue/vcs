# ch17_2.py
import requests, bs4

url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
# 讀者執行此程式時需要調整DepartueSearchDate,例如:調整今天日期未來1週日期
form = {
    'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',      # 台北站
    'EndStation':'f2519629-5973-4d08-913b-479cce78a356',        # 左營站
    'DepartueSearchDate':'2019/09/10',                          # 查詢日期
    'DepartueSearchTime':"13:00",
    'SearchType':'S'
    }

htmlfile = requests.post(url, data=form)    
time_table = htmlfile.json()

col = ['TrainNumber','DepartureTime','DestinationTime','Duration','NonReservedCar']
schedules = [['班次','出發','抵達','行車時間','自由座車廂']]
for t in time_table['data']['DepartureTable']['TrainItem']:
    schedules.append([t[c] for c in col])
for s in schedules:
    print(s)
    








#各種檔案寫讀範例 json

import json, datetime

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/data_earthquake.json'
fp = open(filename, 'r')
earthquakes = json.load(fp)

print("過去7天全球發生重大的地震資訊：")
for eq in earthquakes['features']:
    print("地點:{}".format(eq['properties']['place']))
    print("震度:{}".format(eq['properties']['mag']))
    et = float(eq['properties']['time']) /1000.0
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("時間:{}".format(d))


filename_json = 'C:/______test_files/_json/ChinaBoundary_Province_City'
fp = open(filename_json, 'r', encoding ='UTF-8')
boundary_data = json.load(fp)
for b_data in boundary_data['Province']:
    print("ID:{}".format(b_data['ID']))
    print("code:{}".format(b_data['code']))
    print("name:{}".format(b_data['name']))



'''
#抓取地震資料 用json拆解

import json, requests, datetime

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
r = requests.get(url)

earthquakes = json.loads(r.text)
dataset = list()
for eq in earthquakes['features']:
    item = dict()
    eptime = float(eq['properties']['time']) /1000.0
    d = datetime.datetime.fromtimestamp(eptime). \
        strftime('%Y-%m-%d %H:%M:%S')
    item['eqtime'] = d
    item['mag'] = eq['properties']['mag']
    item['place'] =  eq['properties']['place']
    dataset.append(item)
    #print(item)


for data in dataset:
        data = '(`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format(data['eqtime'], data['mag'], data['place'])
        #print(data)



import json, requests, hashlib, datetime, os.path

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
r = requests.get(url)
sig = hashlib.md5(r.text.encode('utf-8')).hexdigest()
old_sig=''

if os.path.exists('eq_sig.txt'):
    with open('eq_sig.txt', 'r') as fp:
        old_sig = fp.read()
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)
else:
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)

if sig == old_sig:
    print('資料未更新，不需要處理...')
    exit()

earthquakes = json.loads(r.text)
dataset = list()
for eq in earthquakes['features']:
    item = dict()
    eptime = float(eq['properties']['time']) /1000.0
    d = datetime.datetime.fromtimestamp(eptime). \
        strftime('%Y-%m-%d %H:%M:%S')
    item['eqtime'] = d
    item['mag'] = eq['properties']['mag']
    item['place'] =  eq['properties']['place']
    dataset.append(item)

for data in dataset:
    sql = 'insert into eq (`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format( \
           data['eqtime'], data['mag'], data['place'])
    #print(sql)
print('資料更新完成')

'''

print('測試完成')    




filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/jdata.json'

import pprint as pp
import json

with open(filename, "rt") as fp:
    data = json.loads(fp.read())
pp.pprint(data)
print(data)
    



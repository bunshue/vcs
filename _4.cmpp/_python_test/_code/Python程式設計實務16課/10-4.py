# _*_ coding: utf-8 *_*
# 程式 10-4 (Python 3 version)

import json, requests, hashlib, datetime, os.path
from mysql import connector

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

db = connector.connect(
    host = 'db4free.net',
    user = 'ptest',
    passwd = '******',
    database = 'ptest')
cur = db.cursor()
cur.execute('delete from eq')
for data in dataset:
    sql = 'insert into eq (`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format( \
           data['eqtime'], data['mag'], data['place'])
    cur.execute(sql)
    print(sql)
print('資料更新完成')
db.commit()
db.close() 


# _*_ coding: utf-8 *_*
# 程式 10-5 (Python 3 version)

import json, requests, datetime
from mysql import connector

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

db = connector.connect(
    host = 'db4free.net',
    user = 'ptest',
    passwd = '******' 
    database = 'ptest')
cur = db.cursor()
cur.execute('delete from eq')
for data in dataset:
    sql = 'insert into eq (`eqtime`,`mag`,`place`) values("{}",{},"{}");'.format( \
           data['eqtime'], data['mag'], data['place'])
    cur.execute(sql)
db.commit()
db.close() 


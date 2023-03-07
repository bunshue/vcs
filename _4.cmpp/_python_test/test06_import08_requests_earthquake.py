# _*_ coding: utf-8 *_*
 
import json, requests, datetime
 
url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
earthquakes = json.loads(requests.get(url).text)
 
for eq in earthquakes['features']:
    if(float(eq['properties']['mag'])>5.0):
        eptime = float(eq['properties']['time']) /1000.0
        d = datetime.datetime.fromtimestamp(eptime). strftime('%Y-%m-%d %H:%M:%S')
        print("{}, 震度:{}, 地點:{}".format(d, eq['properties']['mag'], eq['properties']['place']))

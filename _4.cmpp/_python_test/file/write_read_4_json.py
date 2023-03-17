#各種檔案寫讀範例 json

import json, datetime

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/data_earthquake.json'
fp = open(filename,'r')
earthquakes = json.load(fp)

print("過去7天全球發生重大的地震資訊：")
for eq in earthquakes['features']:
    print("地點:{}".format(eq['properties']['place']))
    print("震度:{}".format(eq['properties']['mag']))
    et = float(eq['properties']['time']) /1000.0
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("時間:{}".format(d))





print('測試完成')

    




import json

print("------------------------------------------------------------")  # 60個

data = {
   "name": "Joe Chen", 
   "grade": 95, 
   "tel": "0933123456"   
}

json_str = json.dumps(data)
print(json_str)
data2 = json.loads(json_str)
print(data2)


jsonfile = "Student.json"
with open(jsonfile, 'w') as fp:
    json.dump(data, fp)

print("------------------------------------------------------------")  # 60個

import json

jsonfile = "Student.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp)
json_str = json.dumps(data)
print(json_str)  


print("------------------------------------------------------------")  # 60個


import json

filename = 'data/populations.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

i = 0
filename = "_tmp_population.json"
tmpdict = {}
with open(filename, 'w') as fnObj:
    for getData in getDatas:
        if getData['Year'] == '2000':               # 篩選2000年的數據
            tmpdict["Country Name"] = getData['Country Name']
            tmpdict["Country Code"] = getData['Country Code']
            tmpdict["Year"] = getData['Year']
            tmpdict["Numbers"] = getData['Numbers']
            json.dump(tmpdict, fnObj)

print("------------------------------------------------------------")  # 60個

import json

filename = 'data/aqi.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                         # 讀json檔案

for getData in getDatas:
    if getData['County'] == '臺北市':
        sitename = getData['SiteName']                  # 站台名稱
        siteid = getData['SiteId']                      # 站台ID
        pm25 = getData['PM2.5']                         # PM2.5值    
        print('站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
              (siteid, pm25, sitename))

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

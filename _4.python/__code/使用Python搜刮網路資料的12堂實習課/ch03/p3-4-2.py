from urllib import request
import json
import csv

url = 'https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'

with request.urlopen(url) as res:
    data = json.loads(res.read().decode())

print(data)
print()
print(data[0])
    
print('products.csv is writing...')
with open('products.csv', 'w', encoding ='UTF-8', newline = '\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(('作物名稱','平均價','交易量'))
    for item in data:
        writer.writerow((item['作物名稱'],item['平均價'],item['交易量']))

print('done')

from urllib import request
import json
import csv

print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

#行政院農業委員會資料開放平台
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'

with request.urlopen(url) as res:
    data = json.loads(res.read().decode())

print(data)
print()
print(data[0])

filename = 'C:/_git/vcs/_1.data/______test_files2/products.csv'
print('將資料寫出到csv檔, 檔案 : ', filename)

with open(filename, 'w', encoding ='UTF-8', newline = '\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(('作物名稱','平均價','交易量'))
    for item in data:
        writer.writerow((item['作物名稱'],item['平均價'],item['交易量']))

print('完成')

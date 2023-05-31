import requests
import os
import csv
import time

print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

url = 'https://www.ptt.cc/bbs/hotboards.html'
html = requests.get(url)
html.encoding="utf-8"

htmllist = html.text.splitlines()   #將網頁資料一行一行地分割成串列
n=0
for row in htmllist:
    if "音樂" in row:
        n+=1

print("找到 {} 次!".format(n))

print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')


print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/{}/{}_student.csv'

for year in range(103, 109):
    print(url.format(year, year))


print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/111/111_student.csv'

data = list()
csvdata = requests.get(url).text
rows = csvdata.split('\n')
print(rows[0])
print(rows[1])

print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/108/108_student.csv'

csvdata = requests.get(url).text
rows = csvdata.split('\n')
data = list()
columns = rows[0].split(',')
for row in rows[1:]:
    try:
        row = row.split(',')
        item = list()
        for f_index in range(1, 5):
            item.append(row[f_index].replace('"', ''))
        data.append(item)
    except:
        pass
with open(os.path.basename(url), "w", encoding='utf-8', newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(columns[1:5])
    writer.writerows(data)
    
print("done")


print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/{0}/{0}_student.csv'

for year in range(103, 109):
    csvdata = requests.get(url.format(year)).text
    rows = csvdata.split('\n')
    data = list()
    columns = rows[0].split(',')
    for row in rows[1:]:
        try:
            row = row.split(',')
            item = list()
            for f_index in range(1, 5):
                item.append(row[f_index].replace('"', ''))
            data.append(item)
        except:
            pass
    filename = os.path.basename(url.format(year))
    print(filename, "is writing...")
    with open(filename, "w", encoding='utf-8', newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(columns[1:5])
        writer.writerows(data)
    time.sleep(3)

print("done")








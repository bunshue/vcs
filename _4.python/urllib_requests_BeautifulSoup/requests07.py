import csv
import requests

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/{}/{}_student.csv'

for year in range(103, 109):
    print(url.format(year, year))


import requests
import csv

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/111/111_student.csv'

data = list()
csvdata = requests.get(url).text
rows = csvdata.split('\n')
print(rows[0])
print(rows[1])



import requests
import os, csv

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




import requests
import os, csv, time

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





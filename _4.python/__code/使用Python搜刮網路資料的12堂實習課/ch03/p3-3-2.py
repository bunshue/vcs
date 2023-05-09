import requests
import csv

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/111/111_student.csv'

data = list()
csvdata = requests.get(url).text
rows = csvdata.split('\n')
print(rows[0])
print(rows[1])

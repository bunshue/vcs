# _*_ coding: utf-8 _*_
# 10-2.py (Python 3 version)

from mysql import connector

db = connector.connect(
    host='db4free.net',
    user='ptest',
    passwd='****',
    database='ptest')
cur = db.cursor()
cur.execute('select * from PRICES;')
rows = list()
for row in cur:
  rows.append(row)

for i in range(0,10):
  print("日期：{}, 92無鉛：{}, 95無鉛：{}, 98無鉛：{}".\
      format(rows[i][0], rows[i][1], rows[i][2], rows[i][3]))


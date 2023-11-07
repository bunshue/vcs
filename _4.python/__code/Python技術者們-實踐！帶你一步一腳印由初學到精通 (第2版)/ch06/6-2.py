import datetime

date = '20210311'
date = datetime.datetime.strptime(date, '%Y%m%d')
print(date.weekday())
import datetime

datetime_format = '%Y/%m/%d %H:%M:%S'

now = datetime.datetime.now()

current_time = 'DateTime_{:{}}'.format(now, datetime_format)

print(current_time)



print('字元轉unicode')
string = '你'

print(ord(string))

print(hex(ord(string)))










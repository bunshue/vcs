import os

print(os.listdir())
print(os.listdir('/'))

import datetime
print('datetime from lambda:', datetime.datetime.today())
today = datetime.datetime.today()
print('datetime from flex:', today)

today = str(datetime.datetime.today().date())
current = str(datetime.datetime.today())

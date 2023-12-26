# ch30_6.py
import datetime

deltaTime = datetime.timedelta(days=100)
timeNow = datetime.datetime.now()
print("現在時間是 : ", timeNow)
print("100天後是  : ", timeNow + deltaTime)


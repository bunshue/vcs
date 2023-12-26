# ch30_3.py
import datetime

timeStop = datetime.datetime(2017, 11, 16, 14, 54, 0)
while datetime.datetime.now() < timeStop:
    print("program is sleeping.", end="")
print("Wake up")







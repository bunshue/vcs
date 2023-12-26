# ch30_2.py
import datetime

timeStop = datetime.datetime(2023, 11, 18, 17, 50, 0)
while datetime.datetime.now() < timeStop:
    print("program is sleeping.", end="")
print("Wake up")







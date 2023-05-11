import serial
s=serial.Serial("com10",9600)
from time import sleep
while True:
    s.write('ON'.encode()) # 傳送 ON 字串
    sleep(1)
    s.write('OFF'.encode()) # 傳送 OFF 字串
    sleep(1)
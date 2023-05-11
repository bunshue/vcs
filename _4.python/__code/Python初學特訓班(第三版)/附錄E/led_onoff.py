#pip install pyserial
import serial
s=serial.Serial("com10",9600)
from time import sleep
while True:
    s.write('H'.encode()) # 傳送 H 字元
    sleep(1)
    s.write('L'.encode()) # 傳送 L字元
    sleep(1)
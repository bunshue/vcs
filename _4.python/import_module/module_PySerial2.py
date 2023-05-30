
#還沒測試


import serial
s = serial.Serial("com10",9600)
from time import sleep
while True:
    s.write('ON'.encode()) # 傳送 ON 字串
    sleep(1)
    s.write('OFF'.encode()) # 傳送 OFF 字串
    sleep(1)


#pip install pyserial
import serial
s=serial.Serial("com10",9600)
from time import sleep
while True:
    s.write('H'.encode()) # 傳送 H 字元
    sleep(1)
    s.write('L'.encode()) # 傳送 L字元
    sleep(1)


import serial
s=serial.Serial("com10",9600)
while True:
    #讀取串列埠並將字元轉換為字串
    value=s.readline().decode("utf-8")
    # 去除跳列字元   
    value=value.split('\r\n')
    print("value=",value) #顯示讀取值
    value=int(value[0])
    if (value> 900 or value<200):
       print("溫度過高或過低!")
       s.write(b'ON') # 傳送 ON 字串
    else:
       print("溫度正常!")
       s.write(b'OFF') # 傳送 OFF 字串      
       
       


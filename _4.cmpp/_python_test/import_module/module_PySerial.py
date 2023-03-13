# 使用 pySerial 套件
# 需 pip install pyserial

import serial

ser = serial.Serial()
ser.baudrate = 115200    #波特率
ser.port = 'COM1'        #com口
ser.stopbits=1           #停止位 1 1.5 2
ser.bytesize=8           #資料位
ser.parity='N'           #奇偶位  N沒有  E偶校驗  O奇校驗
ser.timeout=5            #超時時間

ser.open()     #連線失敗會丟擲錯誤

ser.write('s\n'.encode())    #傳送資訊

result=ser.readline().decode()  #接收資訊

print(result)



#使用 pySerial 套件
import serial
ser = serial.Serial('COM6', baudrate=115200, bytesize=8, parity='N', stopbits=1)

#ser.write(xxxxxx)

resp = ser.readline()

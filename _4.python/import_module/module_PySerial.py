# 使用 pySerial 套件
# 需 pip install pyserial

"""
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
"""

import serial  # 引用pySerial模組

COM_PORT = "COM4"  # 指定通訊埠名稱
BAUD_RATES = 115200  # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化序列通訊埠

try:
    while True:
        while ser.in_waiting:  # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            # data = data_raw.decode()   # 用預設的UTF-8解碼
            print("接收到的原始資料：", data_raw)
            # print('接收到的資料：', data)

except KeyboardInterrupt:
    ser.close()  # 清除序列通訊物件
    print("再見！")

# 按 ctrl + C 離開

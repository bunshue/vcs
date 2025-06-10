from machine import ADC
import network
import socket

SSID='自己的SSID'
PASSWORD='自己的密碼'
HOST = '0.0.0.0'
PORT = 80
def do_connect():
    global HOST
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    HOST = sta.ifconfig()[0]
              
do_connect() # 連線基地台

httpResponse = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>D1 mini Server</title>
</head>
<body>
  光線強度: {value}<br>
</body>
</html>
"""

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

A0 = ADC(0)

while True:
    client, addr = s.accept()
    value = A0.read() # 讀取 A0
    print("光線強度:{}" .format(value))
    client.send(httpResponse.format(value=value))    
    client.close()
    print()
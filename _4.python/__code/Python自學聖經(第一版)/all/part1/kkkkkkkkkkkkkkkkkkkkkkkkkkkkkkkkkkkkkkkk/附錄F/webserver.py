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
    <head >
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>MicroPython</h1>
        歡迎光臨 D1 mini Server!
    </body>
</html>
"""

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

while True:
    client, addr = s.accept()
    print("客戶端位址：", addr)
    
    req = client.recv(1024) #接收請求
    print("HTTP Request:")
    print(req)
    client.send(httpResponse) #回應請求
    client.close()
    print()
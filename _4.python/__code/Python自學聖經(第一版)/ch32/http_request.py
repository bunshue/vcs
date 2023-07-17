import network
import socket

SSID='自己的SSID'
PASSWORD='自己的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
              
do_connect() # 連線基地台

httpRequest = b'''\
GET /{path} HTTP/1.1
Host:{host}
User-Agent: D1-mini

'''

url = 'http://micropython.org/ks/test.html'
_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)
s.send(httpRequest.format(path=path, host=host))

while True:
    data = s.recv(128) #接收訊息
    if data:
        print(data.decode('utf8'), end='')
    else:
        break

s.close()
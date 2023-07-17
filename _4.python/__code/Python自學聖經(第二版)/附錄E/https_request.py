import network
import socket
import ussl

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
              
do_connect() # Connect to network

httpRequest = b'''\
GET /{path} HTTP/1.0
Host:{host}
User-Agent: D1-mini

'''

url = 'https://micropython.org/ks/test.html'
_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 443)[0][-1] #埠號 443
s = socket.socket()
s.connect(addr)
s = ussl.wrap_socket(s) #加密
s.write(httpRequest.format(path=path, host=host)) #傳送加密訊息

while True:
    data = s.read(128) #接收訊息
    if data:
        print(data.decode('utf8'), end='')
    else:
        break
s.close()
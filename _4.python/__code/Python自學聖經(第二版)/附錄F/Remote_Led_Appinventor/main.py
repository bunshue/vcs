import network
import socket, os
from machine import Pin

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
    
ip=do_connect() # 連線基地台 
 
def err(socket, code, msg):
    socket.write("HTTP/1.1 "+code+" "+msg+"\r\n\r\n")
    socket.write("<h1>"+msg+"</h1>")
    
def handleRequest(client):
    req = client.recv(1024).decode('utf-8')
    firstLine = req.split('\r\n')[0]
    print(firstLine)
    
    httpMethod = ''
    path = ''
    try:
        httpMethod, path, httpVersion = firstLine.split()
    except:
        pass

    if httpMethod == 'GET': # 接受GET 請求
        fileName = path.strip('/')
        if '?' in fileName: #命令如 switch?led=ON、switch?led=OFF
            cmd, state = fileName.split('?')
            if state.lower() == 'led=on':
                led.value(0) #開燈
            else:
                led.value(1) #關燈                       
            client.send(feedback)
            print("傳送指令",fileName)   
 
led = Pin(2, Pin.OUT, value=1)

feedback = b'''\
HTTP/1.1 200 OK

OK!
'''

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

while True:
    client, addr = s.accept() #接受客戶端的連線
    handleRequest(client)
    client.close()
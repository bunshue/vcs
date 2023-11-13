import socket

skt = socket.socket()
skt.connect(('localhost', 6688))

name = skt.getsockname()
print('取得socket name :', name)

while True:
    msg = input('請輸入訊息：')
    skt.send(msg.encode('utf8'))
    
    reply = skt.recv(128) #最多可接收128個字元
    
    if reply == b'exit':
        print('關閉連線')
        skt.close()
        break
    print("收到 server 回傳訊息：" + reply.decode('utf8'))

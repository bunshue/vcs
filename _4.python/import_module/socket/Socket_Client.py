import socket

s = socket.socket()
s.connect(('localhost', 6688))
while True:
    msg = input('請輸入訊息：')
    s.send(msg.encode('utf8'))
    reply = s.recv(128) #最多可接收128個字元
    
    if reply == b'exit':
        print('關閉連線')
        s.close()
        break
    print("收到 server 回傳訊息：" + reply.decode('utf8'))
    

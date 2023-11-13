import socket

#設定哪個IP與port可接受連線, 空字串代表所有IP
HOST = 'localhost'
PORT = 6688

'''

print('支援1個Client的Server')

skt = socket.socket()
skt.bind((HOST, PORT))    

skt.listen(5) #監聽客戶端的連線請求個數

print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

client, addr = skt.accept() #接受客戶端的連線
print('客戶端位址：{}'.format(addr))
print('客戶端位址：{}，埠號：{}'.format(addr[0], addr[1]))

while True:
    msg = client.recv(128).decode('utf8')
    print ('收到 client 訊息：' + msg)
    reply = '已讀不回'

    if msg == 'Hello':
        reply = '大家好!'
    elif msg == 'bye':
        client.send(b'exit')
        break

    client.send(reply.encode('utf8'))

print('關閉伺服器連線')
client.close()
'''


print('支援多個Client的Server')

import threading

class Client(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, daemon = True)
        self.__conn = conn
        self.__addr = addr
        print('客戶端位址：{}'.format(addr))
        print('客戶端位址：{}，埠號：{}'.format(addr[0], addr[1]))

    def run(self):
        try:
            while True:
                data = self.__conn.recv(1024)
                self.__conn.sendall(data)
        except Exception as e:
            print(e)
        self.__conn.close()


#設定監聽的IP與port

skt = socket.socket()
skt.bind((HOST, PORT))    
skt.listen(5) #監聽客戶端的連線請求個數

print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

try:
    while True:
        client, addr = skt.accept() #接受客戶端的連線
        print('客戶端位址：{}'.format(addr))
        print('客戶端位址：{}，埠號：{}'.format(addr[0], addr[1]))

        Client(client, addr).start()
except Exception as e:
    print(e)


'''
    msg = client.recv(128).decode('utf8')
    print ('收到 client 訊息：' + msg)
    reply = '已讀不回'

    if msg == 'Hello':
        reply = '大家好!'
    elif msg == 'bye':
        client.send(b'exit')
        break

    client.send(reply.encode('utf8'))
'''

print('關閉伺服器連線')
client.close()




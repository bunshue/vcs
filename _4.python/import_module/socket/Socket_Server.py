import socket

HOST = 'localhost'
PORT = 6688
s = socket.socket()
s.bind((HOST, PORT))
s.listen(5) #監聽客戶端的連線請求
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))
client, addr = s.accept() #接受客戶端的連線
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

client.close()

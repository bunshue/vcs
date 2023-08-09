import socket

#設定哪個IP與port可接受連線, 空字串代表所有IP
HOST = 'localhost'
PORT = 6688

skt = socket.socket()
skt.bind((HOST, PORT))    

skt.listen(5) #監聽客戶端的連線請求個數
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

client, addr = skt.accept() #接受客戶端的連線
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

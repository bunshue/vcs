import network
import socket, os

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

def err(socket, code, msg):
    socket.write("HTTP/1.1 "+code+" "+msg+"\r\n\r\n")
    socket.write("<h1>"+msg+"</h1>")

def handleRequest(client):
    req = client.recv(1024).decode('utf-8')
    firstLine = req.split('\r\n')[0]
    
    httpMethod = ''
    path = ''
    try:
        httpMethod, path, httpVersion = firstLine.split()
    except:
        pass

    if httpMethod == 'GET': # 接受GET 請求
        fileName = path.strip('/')
        if fileName == '':
            fileName = 'index.html'
        print("傳送檔案",web+fileName)
        fileSize = os.stat(web+fileName)[6] #檔案大小
        if fileSize != None:
            f = open(web+fileName, 'r') #開啟檔案
            client.write(httpResponse)  #伺服器回應
            while True:
                data = f.read(128) #次每次讀取 128 個字元
                if len(data) == 0: #讀取完畢                        
                    break
                client.write(data)   #伺服器回應
            f.close()
        else:
            err(client, "404", "Not Found")      
    else:
        err(client, "501", "伺服器處理請求時發生錯誤!")        


web = 'WebServer/www/'

httpResponse = b'''HTTP/1.1 200 OK

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
import socket
import xtools

ip_address = xtools.connect_wifi_led()

addr = socket.getaddrinfo(ip_address, 80)[0][-1]
print("Web伺服器地址: ", addr)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  
s.listen(5) 
while True:
    cs, addr = s.accept()
    print("客戶端連線地址: ", addr)
    f = open("index.html", "r")
    html = f.read()
    f.close()
    cs.send(html)
    cs.close()    

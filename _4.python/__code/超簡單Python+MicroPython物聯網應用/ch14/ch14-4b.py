import socket

html = """
<html>
<head>
   <meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body>
   <h1>Hello World</h1>
</body>
</html>"""

addr = socket.getaddrinfo("192.168.4.1", 80)[0][-1]
print("Web伺服器地址: ", addr)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  
s.listen(5) 
while True:
    cs, addr = s.accept()
    print("客戶端連線地址: ", addr)
    cs.send(html)
    cs.close()
    
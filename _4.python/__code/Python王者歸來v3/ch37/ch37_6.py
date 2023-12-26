# ch37_6.py
import socket
host = host = "127.0.0.1"                               # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 建立socket物件

mydata = input("請輸入華氏溫度 : ")
s.sendto(mydata.encode(), (host, port))                 # 送給伺服器
print(f"攝氏溫度 : {s.recv(1024).decode()}")
s.close()














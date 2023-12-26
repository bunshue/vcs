# ch37_2.py
import socket
host = "127.0.0.1"                                      # 主機的IP
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.connect((host, port))
data = input("請輸入資料 : ")
s.send(data.encode())                       # 轉成 bytes 資料傳送

receive_data = s.recv(1024).decode()        # 接收所傳來的資料同時解成字串
print(f"接收數據 {receive_data}")           # 列印接收的數據
s.close()                                   # 關閉socket








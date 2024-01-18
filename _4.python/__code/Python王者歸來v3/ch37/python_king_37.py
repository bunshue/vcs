# ch37_1.py
import socket
host = "127.0.0.1"                                      # 主機的IP
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.bind((host, port))                                    # 綁定IP和port
s.listen(5)                                             # TCP監聽
print(f"Server在 {host}:{port}")
print("waiting for connection ...")
while True:
    conn, addr = s.accept()                             # 被動接收客戶連線
    print(f"目前連線網址 {addr} ")
    data = conn.recv(1024)                              # 接收客戶的數據
    print(data)                                         # 列印數據
    conn.sendall(b"HTTP/1.1 200 OK \r\n\r\n Welcome to Deepmind")
    conn.close()                                        # 關閉連線







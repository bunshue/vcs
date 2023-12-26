# ch37_5.py
import socket
host = host = "127.0.0.1"                               # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 建立socket物件
s.bind((host, port))                                    # 綁定IP和port
print("Server : 綁定完成")
print("Waiting ...")

f, addr = s.recvfrom(1024)                              # 被動接收客戶數據
print(f"received from {addr}")
c = f.decode()                                          # 將bytes資料解碼
c = (float(f) - 32) * 5 / 9                             # 轉成攝氏溫度
mydata = str(c)                                         # 轉成字串
s.sendto(mydata.encode(), addr)                         # bytes資料編碼再傳送
s.close()











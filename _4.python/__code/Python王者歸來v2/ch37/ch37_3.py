# ch37_3.py
import socket
host = socket.gethostname()                             # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.bind((host, port))                                    # 綁定IP和port
s.listen()                                              # TCP監聽
print("Server端 : waiting ...")
conn, addr = s.accept()                                 # 被動接收客戶連線
print("Server端:已經連線")
msg = conn.recv(1024).decode()                          # 接收客戶的數據

while msg != "bye":
    if msg:
        print(f"顯示收到內容 : {msg}")                  # 輸出Client訊息
    mydata = input("輸入傳送內容 : ")                   # 讀取輸入內容
    conn.send(mydata.encode())                          # 編碼為bytes後輸出
    if mydata == "bye":                                 # 如果是bye
        break                                           # 離開while迴圈
    print("Server端 : waiting ...")
    msg = conn.recv(1024).decode()                      # 讀取輸入內容
conn.close()
s.close()







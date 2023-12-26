# ch37_4.py
import socket
host = socket.gethostname()                             # 主機的域名
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.connect((host, port))                                 # 執行連線
print("Client端 : 已經連線")
msg = ''                                                # 主要是初次連線用

while msg != "bye":
    mydata = input("輸入傳送內容 : ")                   # 讀取輸入內容
    s.send(mydata.encode())                             # 編碼為bytes後輸出
    if mydata == "bye":                                 # 如果是bye
        break                                           # 離開while迴圈
    print("Client端 : waiting ...")
    msg = s.recv(1024).decode()                         # 讀取輸入內容
    print(f"顯示收到內容 : {msg}")                      # 輸出Server訊息                   
s.close()








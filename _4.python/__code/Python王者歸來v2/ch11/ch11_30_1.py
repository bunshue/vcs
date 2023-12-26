# ch11_30_1.py
def printmsg():
    msg = "Java"        # 嘗試更改全域變數造成建立一個區域變數
    print("更改後: ", msg)
msg = "Python"
printmsg()




   

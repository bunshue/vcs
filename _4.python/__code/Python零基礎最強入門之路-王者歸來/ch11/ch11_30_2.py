# ch11_30_2.py
def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print("更改後: ", msg)
msg = "Python"
print("更改前: ", msg)
printmsg()




   


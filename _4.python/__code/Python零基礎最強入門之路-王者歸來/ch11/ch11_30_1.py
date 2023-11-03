# ch11_30_1.py
def printmsg():
    print("列印全域變數: ", msg)
    msg = "Java"        # 嘗試更改全域變數造成錯誤
    print("更改後: ", msg)
msg = "Python"
printmsg()




   

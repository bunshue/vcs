# ch11_30_2.py
def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print("函數列印  :更改後: ", msg)
msg = "Python"
print("主程式列印:更改前: ", msg)
printmsg()
print("主程式列印:更改後: ", msg)



   


# ch11_29.py
def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print(f"函數列印  :更改後: {msg}")
msg = "Python"
print(f"主程式列印:更改前: {msg}")
printmsg()
print(f"主程式列印:更改後: {msg}")



   


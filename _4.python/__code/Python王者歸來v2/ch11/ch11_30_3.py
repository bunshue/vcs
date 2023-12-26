# ch11_30_3.py
def printlocal():
    lang = "Java"
    print("語言 : ", lang)
    print("區域變數 : ", locals())
msg = "Python"
printlocal()
print("語言 : ", msg)
print("全域變數 : ",globals())








   


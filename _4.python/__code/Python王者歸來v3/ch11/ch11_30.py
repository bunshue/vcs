# ch11_30.py
def printlocal():
    lang = "Java"
    print(f"語言 : {lang}")
    print(f"區域變數 : {locals()}")
msg = "Python"
printlocal()
print(f"語言 : {msg}")
print(f"全域變數 : {globals()}")








   


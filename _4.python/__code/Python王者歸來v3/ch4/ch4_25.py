# ch4_25.py
fobj1 = open("out25w.txt", mode="w", encoding="utf-8")   
print("Testing mode=w, using utf-8 format", file=fobj1)
fobj1.close( )
fobj2 = open("out25a.txt", mode="a", encoding="cp950")   
print("測試 mode=a 參數, 預設 ANSI 編碼", file=fobj2)
fobj2.close( )




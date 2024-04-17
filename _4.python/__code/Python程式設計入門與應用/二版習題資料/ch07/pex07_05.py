# Filename: pex07_05.py
def freverse(n):
    if n != 0:
       print(n % 10, end = "")
       n = n // 10
       freverse(n)
#main program       
pnum = int(input("請輸入一個整數："))
freverse(pnum)
# Filename: pex05_07.py
def freverse(n):
    while n != 0:
        pre = n % 10
        print(pre, end = "")
        n = n // 10

pnum = int(input("請輸入一個整數："))
freverse(pnum)
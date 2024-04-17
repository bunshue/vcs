# Filename: ex05_01.py
def pmax(n1, n2):
    if n1>n2:
        result = n1
    else:
        result = n2
    return result

n1=int(input("請輸入第1個整數"))
n2=int(input("請輸入第2個整數"))
print("%d與%d這2個整數中，較大的是為%d"%(n1,n2,pmax(n1,n2)))    
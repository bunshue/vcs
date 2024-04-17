# Filename: pex05_10.py
def isprime(n):
    for pd in range(2, n // 2 + 1):
        if n % pd == 0:
            return False
    return True

pnumber = int(input("請輸入一個整數："))
if (isprime(pnumber)):   
    print("輸入整數%d是質數"%pnumber)
else:    
    print("輸入整數%d不是質數"%pnumber)
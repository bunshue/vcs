# Filename: pex05_05.py
def fgcd(numbers):
    g = numbers[0]
    for i in range(1, len(numbers)):
        g = fgcd2(g, numbers[i])
    return g
def fgcd2(n1, n2):
    g = 1 
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            g = k 
        k += 1
    return g

ps = input("請輸入一串列的整數，數值之間以空白間隔即可：") 
pitems = ps.split()
pnumbers = [ eval(x) for x in pitems ]    
print("串列整數", pnumbers,"的GCD為",fgcd(pnumbers))
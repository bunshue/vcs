# Filename: pex05_06.py
def sumdigits(n):
    ptemp = abs(n)
    psum = 0
    while ptemp != 0:
        pre = ptemp % 10
        psum = psum+pre
        ptemp = ptemp // 10
    return psum

pnum = int(input("請輸入一個整數："))
print("整數%d，其中每一位數值的和為%d"%(pnum, sumdigits(pnum)))
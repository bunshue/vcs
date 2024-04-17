# Filename: pex07_04.py
def movedisk(n, dfrom , dto, daux):
    if n==1:
        print("移動",n,"從",dfrom,"到",dto)
    else:
        movedisk(n-1,dfrom, daux, dto)
        print("移動",n,"從",dfrom,"到",dto)
        movedisk(n-1, daux, dto, dfrom)        
#main program
pnum = int(input("請輸入需要移動幾個圓盤："))
print("移動圓盤的過程如下所示：")
movedisk(pnum,'A','B','C')            
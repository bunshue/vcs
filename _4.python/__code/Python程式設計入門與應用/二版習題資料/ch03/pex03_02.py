# Filename: pex03_02.py
i=1
while (i<=9):
    j=2
    while (j<=9):        
        print("%d*%d=%2d"%(j,i,i*j), end=" ")
        j=j+1
    print()
    i=i+1
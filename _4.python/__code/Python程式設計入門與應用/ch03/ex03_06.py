# Filename: ex03_06.py
# 巢狀 for迴圈
# 九九乘法表
for i in range(1,10):
    for j in range(1,10):        
        print("%d*%d=%2d"%(i,j,i*j), end=" ")
    print() 
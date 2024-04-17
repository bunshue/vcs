# Filename: ex03_070.py
# 巢狀 for迴圈
# break   
# 最小公倍數
a = int(input("請輸入a的值:"))
b = int(input("請輸入b的值:"))
nmax = (a+1)*(b+1)
for i in range(1, nmax):
    if (i%a==0 and i%b==0):
        break
print("%d與%d的最小公倍數=%d"%(a,b,i))
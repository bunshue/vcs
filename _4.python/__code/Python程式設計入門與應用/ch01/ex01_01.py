# Filename: ex01_01.py
sum = 0
def showloop(n):
    print("第 %d 次迴圈"%(n))

for i in range(1,6):
    showloop(i)
    sum +=i

print ("1+2+3+...+5=%d"%(sum))
# ch7_15.py
n = int(input("請輸入整數:"))
total = 0                         # 總計
for i in range(1, n+1):
    total += i
print("從1到%d的總和是 = " % n, total)

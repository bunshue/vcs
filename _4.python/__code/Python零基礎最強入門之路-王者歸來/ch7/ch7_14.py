# ch7_14.py
n = int(input("請輸入整數:"))
number = list(range(n + 1))       # 建立串列
total = 0                         # 總計
for i in number:
    total += i
print("從1到%d的總和是 = " % n, total)

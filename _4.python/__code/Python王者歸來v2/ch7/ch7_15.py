# ch7_15.py
squares = []                     # 建立空串列
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    squares.append(num ** 2)     # 加入串列
print(squares)



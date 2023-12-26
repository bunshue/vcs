# ch7_16.py
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
squares = [num ** 2 for num in range(1, n+1)]
print(squares)


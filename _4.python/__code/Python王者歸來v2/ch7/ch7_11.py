# ch7_11.py
money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print(f"第 {i+1} 年本金和 : {int(money)}")





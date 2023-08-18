# ch7_7.py
money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print("第 %d 年本金和 : %d" % ((i+1),int(money)))





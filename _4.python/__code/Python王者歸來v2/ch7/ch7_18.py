# ch7_18.py
x = [[a, b, c] for a in range(1,20) for b in range(a,20) for c in range(b,20)
     if a ** 2 + b ** 2 == c **2]
print(x)







